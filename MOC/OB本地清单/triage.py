import json,re,collections
from pathlib import Path
p=Path(__file__).parent
a=json.loads((p/'文件准入队列.json').read_text())
rows=[]
for r in a:
    if r['decision']!='待核内容类型' or r.get('scan_presence'):continue
    n=Path(r['path']).name
    if re.search(r'Codex|AGENTS|PIPELINE|Zapier|DB建表|数据结构预设计|技术确认|系统产品蓝图|项目进度工作台',n,re.I):
        status='技术风险隔离'; reason='文件名技术信号，未读正文，不认定语义核验完成'
    elif n in ['acceptance_report.md','review_list.md','_INDEX.md'] or re.search(r'验收报告|自验报告|任务清单|任务书|执行记录|完成记录|日报|议程|纪要模板|预盘点|索引|对话记录|清洗任务|复核结果',n):
        status='治理证据暂缓';reason='低复用/过程证据，按需溯源，不逐件造原子'
    elif re.search(r'01_项目章程|02_0周启动会议议程|03_Phase0_治理冻结',n):
        status='已分析来源关联';reason='008-012已处理；不是当前事实批准'
    else:status='业务候选待内容核定';reason='仅路径初分，非正文准入或完成'
    theme='TOC服务与人才' if any(x in r['path'] for x in ['TOC','管家','香港','人才']) else ('会议与经营协同' if '03_AMANDA' in r['path'] else ('TOI价值证明' if 'TOI' in n else ('TOB机构交付' if 'TOB' in n else '资产治理与项目边界')))
    key=re.sub(r'\(\d+\)(?=\.)','',n)
    rows.append(dict(path=r['path'],status=status,reason=reason,theme=theme,duplicate_name_key=key,mtime=r['mtime'],content_read_allowed=False))
counts=collections.Counter(r['status'] for r in rows)
groups=collections.defaultdict(list)
for r in rows:groups[r['duplicate_name_key']].append(r['path'])
dups={k:v for k,v in groups.items() if len(v)>1 and k not in ['README.md','review_list.md','acceptance_report.md','_INDEX.md']}
(p/'295项处置明细.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
(p/'疑似重复待核.json').write_text(json.dumps(dups,ensure_ascii=False,indent=2))
print(json.dumps({'total':len(rows),'status':dict(counts),'themes':dict(collections.Counter(r['theme'] for r in rows)),'duplicate_name_groups':len(dups)},ensure_ascii=False))
