"""Join daily discoveries to exact existing vault evidence; never open sources."""
import datetime as dt
import json
from collections import Counter
from pathlib import Path
from zoneinfo import ZoneInfo

B = Path(__file__).resolve().parent
names = ['项目入口队列.json', '文件准入队列.json', '扫描覆盖.json']
raw = {n: (B / n).read_bytes() for n in names}
projects, files, coverage = [json.loads(raw[n]) for n in names]
pm, fm = [{r['path']: r for r in a} for a in (projects, files)]
j = json.loads((B / '非RW_Jasper核定.json').read_text())
rj = json.loads((B / 'Jasper待核再核定.json').read_text())
boundaries = {r['path']: r for r in rj['scope_decisions']}
governance = {r['path']: r for r in j['governance_reads']}
now = dt.datetime.now(ZoneInfo('America/Chicago')).isoformat()
records = []
for signal in coverage['daily_increment']['signals']:
    if signal.get('decision') not in {'待核不递归', '待核内容类型'}:
        continue
    path = signal['path']
    row = fm.get(path) or pm[path]
    obs = row['daily_metadata']
    result = {'path': path, 'checked': now, 'kind': obs['kind'], 'status': '范围证据待核', 'reason': '精确已核边界/治理记录未命中；不递归，不授予正文准入', 'source_body_bytes': 0, 'content_read_allowed': False, 'review_status': 'pending independent review'}
    if path in boundaries:
        prior = boundaries[path]
        result.update(status=prior['new_status'], reason=prior['reason'], evidence={'ledger': 'Jasper待核再核定.json', 'array': 'scope_decisions', 'id': prior['id']})
    elif path in governance:
        prior = governance[path]
        old = prior.get('stat_after', {})
        if old.get('mtime_ns') == obs.get('mtime_ns') and old.get('size') == obs.get('size'):
            result.update(status='既有治理识别关联', reason='精确路径/mtime_ns/size与既有治理识别一致；不是新增业务知识，不重读正文', evidence={'ledger': '非RW_Jasper核定.json', 'array': 'governance_reads', 'id': prior['id']})
        else:
            result.update(reason='既有治理入口元数据出现差异；项目仅范围容器，不自动准入正文，待最小治理用途核定', evidence={'ledger': '非RW_Jasper核定.json', 'array': 'governance_reads', 'id': prior['id'], 'prior_stat': old}, metadata_difference=True)
    # Keep parent groups as locators, never as inherited body authorization.
    parent = next((str(p) for p in Path(path).parents if str(p) in pm), str(Path(path).parent))
    result['parent_group'] = parent
    row['daily_admission_reconciliation'] = result
    records.append(result)
summary = {'checked': now, 'processed_paths': len(records), 'counts': dict(Counter(r['status'] for r in records)), 'kind_counts': dict(Counter(r['kind'] for r in records)), 'remaining_groups': dict(Counter(r['parent_group'] for r in records if r['status'] == '范围证据待核')), 'records': records, 'source_body_bytes': 0, 'new_business_analyses': 0, 'actual_tokens': None, 'review_status': 'pending independent review', 'local_acceptance': False}
coverage['daily_increment']['admission_reconciliation'] = {k: v for k, v in summary.items() if k != 'records'}
if any((B / n).read_bytes() != raw[n] for n in names):
    raise RuntimeError('Concurrent change; no writes')
for n, data in list(zip(names, (projects, files, coverage))) + [('每日新增路径核定.json', summary)]:
    temp = B / (n + '.admission.tmp')
    with temp.open('x') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    if n in raw and (B / n).read_bytes() != raw[n]:
        raise RuntimeError('Concurrent change; stop before replacement')
    temp.replace(B / n)
print(json.dumps({k: v for k, v in summary.items() if k not in {'records', 'remaining_groups'}}, ensure_ascii=False))
print('remaining_parent_groups', len(summary['remaining_groups']))
