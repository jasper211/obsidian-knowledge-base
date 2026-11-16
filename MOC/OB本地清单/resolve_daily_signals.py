"""Resolve schema comparison errors using vault evidence only, never source files."""
import datetime as dt
import json
from pathlib import Path
from zoneinfo import ZoneInfo

BASE = Path(__file__).resolve().parent
names = ['文件准入队列.json', '扫描覆盖.json']
raw = {n: (BASE / n).read_bytes() for n in names}
files, coverage = [json.loads(raw[n]) for n in names]
lookup = {r['path']: r for r in files}
daily = coverage['daily_increment']
now = dt.datetime.now(ZoneInfo('America/Chicago')).isoformat()
results = []
for signal in daily['signals']:
    if signal['signal'] != 'metadata_changed':
        continue
    r = lookup.get(signal['path'], {})
    observed = r.get('daily_metadata', {})
    # Prefer exact string nanoseconds captured in the earlier before/after pair.
    candidates = [(k, r.get(k, {})) for k in ('stat_after', 'stat_before', 'stat_inventory', 'stat')]
    match = next(((k, v) for k, v in candidates if isinstance(v, dict) and isinstance(v.get('mtime_ns'), str) and v.get('mtime_ns') == observed.get('mtime_ns') and v.get('size') == observed.get('size')), None)
    resolution = {'path': signal['path'], 'checked': now, 'source_read_bytes': 0, 'status': 'unresolved_metadata_signal'}
    if match:
        resolution.update(status='schema_false_positive', evidence_field=match[0], reason='Exact prior string mtime_ns and size equal daily observation; absent top-level size caused false comparison')
        signal['resolution'] = resolution
        observed['resolution'] = resolution
    results.append(resolution)
summary = {'checked': now, 'processed': len(results), 'schema_false_positives': sum(r['status'] == 'schema_false_positive' for r in results), 'unresolved': sum(r['status'] != 'schema_false_positive' for r in results), 'source_body_bytes': 0, 'actual_tokens': None, 'review_status': 'pending independent review', 'records': results}
coverage['daily_increment']['signal_reconciliation'] = summary
if any((BASE / n).read_bytes() != raw[n] for n in names):
    raise RuntimeError('Concurrent modification; abort')
for n, obj in zip(names, (files, coverage)):
    temp = BASE / (n + '.signal.tmp')
    with temp.open('x') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write('\n')
    if (BASE / n).read_bytes() != raw[n]:
        raise RuntimeError('Concurrent modification before replacement; abort')
    temp.replace(BASE / n)
print(json.dumps({k: v for k, v in summary.items() if k != 'records'}, ensure_ascii=False))
