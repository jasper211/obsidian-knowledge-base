"""Reconcile the just-collected metadata only; no source access."""
import json
from pathlib import Path
from collections import Counter

base = Path(__file__).resolve().parent
names = ['项目入口队列.json', '文件准入队列.json', '扫描覆盖.json']
raw = {n: (base / n).read_bytes() for n in names}
projects, files, coverage = [json.loads(raw[n]) for n in names]
daily = coverage['daily_increment']
lookup = {r['path']: r for r in projects + files}
corrected = []
for signal in daily['signals']:
    r = lookup[signal['path']]
    observed = r.get('daily_metadata', {})
    previous = r.get('stat_inventory', r)
    old = previous.get('mtime_ns')
    if signal['signal'] == 'metadata_changed' and isinstance(old, (int, float)) and previous.get('size') == observed.get('size') and 0 < abs(int(old) - int(observed['mtime_ns'])) <= 1024:
        signal['signal'] = 'legacy_timestamp_precision_uncertain'
        signal['admission'] = 'Historical numeric ns precision differs; not confirmed source change; no body access'
        observed['signal'] = signal['signal']
        corrected.append(r['path'])
daily['precision_uncertain_count'] = len(corrected)
daily['signal_counts'] = dict(Counter(s['signal'] + ':' + s.get('decision', '') for s in daily['signals']))
daily['review_status'] = '独立核查有保留：历史字段保留/直接层只读成立；非完整增量验收'
daily['review_findings'] = ['Three-file commit is not transactional; no full historical snapshot diff performed', 'Missing child/type changes not exhaustively detected; historical admission is not fresh validation', 'Configured roots need future explicit isolation guard; no server access authorized', 'Numeric legacy timestamp precision differences are not confirmed source modifications']
daily['source_body_bytes'] = 0
if any((base / n).read_bytes() != raw[n] for n in names):
    raise RuntimeError('Concurrent change; abort')
for n, data in zip(names, [projects, files, coverage]):
    temp = base / (n + '.reconcile.tmp')
    with temp.open('x') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    if (base / n).read_bytes() != raw[n]:
        raise RuntimeError('Concurrent change before replace; stop')
    temp.replace(base / n)
print(json.dumps(daily['signal_counts'], ensure_ascii=False))
