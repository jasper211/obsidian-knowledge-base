"""Metadata only. Never follows links or reads source content."""
import os, json, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

BASE = Path('/Users/a112233/Desktop')
OUT = Path(__file__).resolve().parent
now = datetime.datetime.now(ZoneInfo('America/Chicago'))
lo = datetime.datetime(2026, 5, 10, tzinfo=ZoneInfo('America/Chicago')).timestamp()
hi = datetime.datetime(2026, 11, 11, tzinfo=ZoneInfo('America/Chicago')).timestamp()
projects, files, failures = [], [], []
roots = ['Rw权益项目', 'Jasper工作文档（不含EA项目）', '流程架构项目_jasper', '业务模型', 'AI 培训', '牌照和保司合同', '临时工作区']
allowed = {'00_审计','00_索引','01_RW服务合同','02_RW权益服务项目','03_AMANDA','04_RW权益_TOC','05_佣金相关文档','07_项目立项启动'}
def entries(p):
    try:
        if any(q.is_symlink() for q in [p,*p.parents]) or not p.is_dir():
            failures.append({'path':str(p),'error':'link or not directory'})
            return []
        return sorted(p.iterdir())
    except OSError as e:
        failures.append({'path':str(p),'error':str(e)})
        return []
def row(p, decision, reason):
    return {'path':str(p),'decision':decision,'reason':reason,'checked':now.isoformat(),'content_read_allowed':False,'review_status':'待核'}
def walk(p):
    for f in entries(p):
        n=f.name.lower()
        if f.is_symlink() or n.startswith('.') or n in {'node_modules','__pycache__','venv','scratch','tmp','ob','codex','superpowers'} or any(t in n for t in ['p&l','eg-','fixture','工程','测试','ob知识库','obsidian-mcp','process-db-mcp']):
            files.append(row(f,'排除子树','链接/隐藏/工程临时，不跟随'))
        elif f.is_dir():
            if any(t in n for t in ['fixture','测试','工程','ob_','eg-']):
                files.append(row(f,'待核子树','工程测试/自身提炼风险，不展开'))
            else:
                walk(f)
        else:
            ext=f.suffix.lower()
            d='待核内容类型' if ext in {'.md','.html','.htm'} else ('仅引用' if ext in {'.doc','.docx','.xls','.xlsx','.ppt','.pptx','.pdf'} else '排除分析类型')
            r=row(f,d,'RW用户保留；扩展名不证明业务正文')
            try:
                s=f.stat(); r.update(size=s.st_size,mtime=datetime.datetime.fromtimestamp(s.st_mtime,ZoneInfo('America/Chicago')).isoformat(),mtime_ns=s.st_mtime_ns)
                r['window']='首次窗口内' if lo<=s.st_mtime<hi else ('早于窗口' if s.st_mtime<lo else '后续增量')
                if d=='待核内容类型' and r['window']!='首次窗口内': r['decision']='不读正文:'+r['window']
            except OSError as e: failures.append({'path':str(f),'error':str(e)});r['decision']='stat失败'
            files.append(r)
for name in roots:
    p=BASE/name
    projects.append(row(p,'限定保留' if name in {'Rw权益项目','流程架构项目_jasper'} else '待核','既有最大范围；EA仅价值链价值流'))
    for child in entries(p):
        keep=name=='Rw权益项目' and child.name in allowed and not child.is_symlink()
        projects.append(row(child,'保留筛类型' if keep else '待核不递归','既有RW准入目录' if keep else '项目状态/主源/敏感/技术边界未核'))
        if keep: walk(child)
        if name=='Jasper工作文档（不含EA项目）' and child.name=='项目工作区' and not child.is_symlink():
            projects.extend(row(x,'待核不递归','在用/实验/镜像待核') for x in entries(child))
known={r['path'] for r in projects}
for child in entries(BASE):
    if str(child) not in known:
        projects.append(row(child,'待核不递归','桌面剩余入口，归属未核，不读正文'))
for r in projects:
    n=Path(r['path']).name.lower()
    if any(t in n for t in ['p&l','eg-','ob知识库','fixture','obsidian-mcp','process-db-mcp']) or n in {'ob','scratch','tmp'} or n.startswith('.'):
        r.update(decision='排除',reason='既有排除/测试工程/OB自身/隐藏入口')
summary={'checked':now.isoformat(),'project_rows':len(projects),'file_rows':len(files),'failures':failures,'content_candidates':sum(r['decision']=='待核内容类型' for r in files),'reference_rows':sum(r['decision']=='仅引用' for r in files),'scope':'7个既有根直接入口；仅RW八个已准入子树递归；其余待核不递归，非本地全量验收'}
batch=now.strftime('%Y%m%dT%H%M%S%f')
summary.update(batch=batch,scope='Desktop直接入口、7个既有根、Jasper项目工作区入口已枚举；RW八准入子树元数据扫描；待核项目不递归，非全部本地文件验收')
if any(q.is_symlink() for q in [OUT,*OUT.parents]):raise RuntimeError('unsafe output')
for name,data in [('项目入口队列.json',projects),('文件准入队列.json',files)]:
    target=OUT/name
    if target.is_symlink():raise RuntimeError('unsafe output')
    old={r['path']:r for r in json.loads(target.read_text())} if target.exists() else {}
    for r in data:
        prev=old.get(r['path'],{})
        r['discovered']=prev.get('discovered',prev.get('checked',now.isoformat()))
        r['batch']=batch
        for key in ['analysis_status','manual_decision','review_notes']:
            if key in prev:r[key]=prev[key]
    unseen=[dict(r,scan_presence='本次未覆盖或未找到，不证明删除',content_read_allowed=False,review_status='待核',batch=batch,discovered=r.get('discovered',r.get('checked'))) for p,r in old.items() if p not in {x['path'] for x in data}]
    data.extend(unseen)
    with (OUT/(batch+'_'+name)).open('x') as f:json.dump(data,f,ensure_ascii=False,indent=2)
    temp=OUT/(batch+'_'+name+'.tmp')
    with temp.open('x') as f:json.dump(data,f,ensure_ascii=False,indent=2)
    os.replace(temp,target)
pending=[r for r in projects+files if '待核' in r['decision'] or r['decision']=='限定保留']
summary['pending_rows']=len(pending)
for name,data in [('待核隔离队列.json',pending),('扫描覆盖.json',summary)]:
    target=OUT/name
    if target.is_symlink():raise RuntimeError('unsafe output')
    temp=OUT/(batch+'_'+name+'.tmp')
    with temp.open('x') as f:json.dump(data,f,ensure_ascii=False,indent=2)
    os.replace(temp,target)
print(json.dumps(summary,ensure_ascii=False))
