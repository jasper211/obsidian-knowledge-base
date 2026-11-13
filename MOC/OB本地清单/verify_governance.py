import json,collections
from pathlib import Path
p=Path(__file__).parent
base=json.loads((p/'295项处置明细.json').read_text())
expected={x['path'] for x in base if x['status']=='治理证据暂缓'}
rows=[];missing=[]
for i in range(3):
    f=p/f'治理{i}_处置.json'
    if not f.exists():missing.append(i);continue
    a=json.loads(f.read_text())
    if isinstance(a,dict):a=next((a[k] for k in ['items','records','rows','files'] if k in a),[])
    rows.extend(a)
paths=[r['path'] for r in rows]
result=dict(expected=len(expected),records=len(rows),missing_shards=missing,missing_paths=sorted(expected-set(paths)),unexpected=sorted(set(paths)-expected),duplicates=[k for k,v in collections.Counter(paths).items() if v>1],statuses=dict(collections.Counter(r['status'] for r in rows)))
result['coverage_complete']=not any(result[k] for k in ['missing_shards','missing_paths','unexpected','duplicates'])
(p/'85项覆盖核对.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps(result,ensure_ascii=False))
