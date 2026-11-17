"""Apply a bounded scope exclusion from existing vault governance evidence."""
import json
import datetime as dt
from pathlib import Path
from collections import Counter
from zoneinfo import ZoneInfo

B = Path(__file__).resolve().parent
names = ['项目入口队列.json', '每日新增路径核定.json', '扫描覆盖.json']
raw = {n: (B / n).read_bytes() for n in names}
projects, report, coverage = [json.loads(raw[n]) for n in names]
ledger = json.loads((B / '非RW_Jasper核定.json').read_text())
e = next(r for r in ledger['entry_decisions'] if r['id'] == 'E021')
g = next(r for r in ledger['governance_reads'] if r['id'] == 'G014')
assert '仪表盘属工程OB' in e['reason']
path = g['path']
row = next(r for r in projects if r['path'] == path)
record = next(r for r in report['records'] if r['path'] == path)
assert record['status'] == '范围证据待核'
old = dict(record)
record.update(status='工程OB范围排除', checked=dt.datetime.now(ZoneInfo('America/Chicago')).isoformat(), reason='E021既有治理识别明确仪表盘属工程OB；沿用用户范围排除，不因mtime变化重读，不证明当前正文内容或用途已独立复验', review_status='独立核查限定通过：范围处置，不是当前正文核实', evidence={'ledger': '非RW_Jasper核定.json', 'entry_id': 'E021', 'governance_id': 'G014'}, previous_reconciliation=old)
row['daily_admission_reconciliation'] = record
report['counts'] = dict(Counter(r['status'] for r in report['records']))
report['remaining_groups'] = dict(Counter(r['parent_group'] for r in report['records'] if r['status'] == '范围证据待核'))
report['g014_scope_resolution'] = {'checked': record['checked'], 'path': path, 'source_read_bytes': 0, 'review_agent': '01a1deb2-0e65-73e3-b5b1-efb774497155', 'boundary': 'one path only; parent container not excluded'}
coverage['daily_increment']['admission_reconciliation'] = {k: v for k, v in report.items() if k != 'records'}
if any((B / n).read_bytes() != raw[n] for n in names):
    raise RuntimeError('Concurrent update')
for n, obj in zip(names, (projects, report, coverage)):
    if (B / n).read_bytes() != raw[n]:
        raise RuntimeError('Concurrent update before replacement')
    temp = B / (n + '.g014.tmp')
    with temp.open('x') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write('\n')
    temp.replace(B / n)
print(report['counts'])
print(record['checked'])
