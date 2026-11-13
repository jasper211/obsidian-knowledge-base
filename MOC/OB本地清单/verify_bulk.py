"""Check all assigned sources have exactly one disposition; never read sources."""
import json,collections
from pathlib import Path
p=Path(__file__).parent
excluded={'45_TOB服务目录与验收口径_v0.2.md','45_TOI价值证明框架与报表模板_v0.2.md','45_SHARED权益资产字段冻结与变更规则_v0.2.md'}
original=json.loads((p/'295项处置明细.json').read_text())
expected={x['path'] for x in original if x['status']=='业务候选待内容核定' and Path(x['path']).name not in excluded}
allrows=[];missing=[]
for i in range(4):
    f=p/f'分片{i}_处置.json'
    if not f.exists():missing.append(i);continue
    data=json.loads(f.read_text())
    if isinstance(data,dict):
        data=next((data[k] for k in ['items','records','files','rows','dispositions'] if k in data),[])
    allrows.extend(data)
paths=[x['path'] for x in allrows]
result={'expected':len(expected),'records':len(paths),'missing_shards':missing,'missing_paths':sorted(expected-set(paths)),'unexpected':sorted(set(paths)-expected),'duplicates':[k for k,v in collections.Counter(paths).items() if v>1],'statuses':dict(collections.Counter(x['status'] for x in allrows))}
result['coverage_complete']=not any(result[k] for k in ['missing_shards','missing_paths','unexpected','duplicates'])
(p/'182项覆盖核对.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in result.items() if k not in ['missing_paths','unexpected']},ensure_ascii=False))
