import os, json, stat, hashlib
from pathlib import Path
from datetime import datetime, timezone
from html.parser import HTMLParser

V = Path(__file__).resolve().parents[2]
D = Path('/Users/a112233/Desktop')
Q = json.loads((V/'MOC/OB本地清单/项目入口队列.json').read_text())
OMIT = ['Jasper工作文档（不含EA项目）','业务模型','流程架构项目_jasper','Rw权益项目']
def assigned(p):
    return not any(p == str(D/x) or p.startswith(str(D/x)+'/') for x in OMIT)
old = {r['path']:r for r in Q if assigned(r['path'])}
paths = set(old)
listings = {}
for root in [D,D/'AI 培训',D/'临时工作区',D/'Grokbot本体项目']:
    if root.is_symlink():
        continue
    names = sorted(os.listdir(root))
    listings[str(root)] = names
    paths.update(str(root/n) for n in names if assigned(str(root/n)))

def snap(p):
    for a in [*Path(p).parents,Path(p)]:
        if stat.S_ISLNK(os.lstat(a).st_mode):
            raise ValueError('symbolic link rejected')
    s=os.lstat(p)
    return dict(size=s.st_size,mtime=s.st_mtime,mtime_ns=str(s.st_mtime_ns),ctime_ns=str(s.st_ctime_ns),ino=s.st_ino,dev=s.st_dev,mode=s.st_mode)

class Visible(HTMLParser):
    def __init__(self):
        super().__init__(); self.stack=[]; self.parts=[]
    def handle_starttag(self,t,a):
        a=dict(a)
        hidden=t in ['script','style','template','noscript','svg'] or 'hidden' in a or a.get('aria-hidden')=='true' or 'display:none' in a.get('style','').replace(' ','')
        self.stack.append((t,hidden)) if t not in ['meta','link','br','hr','img','input','source','wbr'] else None
    def handle_endtag(self,t):
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i][0]==t:
                del self.stack[i:]; break
    def handle_data(self,s):
        if not any(h for _,h in self.stack) and s.strip():
            self.parts.append((self.getpos()[0],s.strip()))

preview_names = ['2026年8月热点Top10_五大类别.html','2026年9月热点Top10_五大类别.html','2026年9月热点_五类.html','交接件_独立复跑说明.md','复跑_202609_五大类别热点Top10_报告.html','复跑_检索留痕清单.md','复跑_自报覆盖清单.md','月度热点报告_生成指令.md','模块0_20260923.html','模块0_v2_20260923.html','模块1_v2_20260923.html','模块1_目标态_20260923.html']
rows=[]
for p in sorted(paths):
    n=Path(p).name
    r=dict(path=p,old_queue_path=p in old,old_decision=old.get(p,{}).get('decision'),status='待核',reason='归属/项目状态未证实，不以文件名推定准入',source_hash=None,read_bytes=0,read_chars=0,locators=[],token_count=None,token_proxy=0,project_admission='待核',analysis_performed=False)
    rel=Path(p).relative_to(D); top=rel.parts[0]
    prohibited = top in ['P&L_EA小组Jasper','DW RO邮件同步','RW产品体系设计及Uniwin新动力协议方案.zip'] or 'KYC' in n or n=='钟明秀.xlsx' or '畅学' in n or 'CL_' in n or 'CL的' in n or any(w in n for w in ['账号','公钥','给运维','SFTP','Syncthing','同步设置','同步项目'])
    tool=top in ['workbuddy','梯子','画板_DrawBoard'] or any(w in n for w in ['Jev配置','JEV盲测','Claude Code工作全貌'])
    rw= n.lower().startswith(('u020','u20-'))
    if prohibited or tool or rw or top=='牌照和保司合同':
        r['status']='边界排除' if prohibited or tool or rw else '敏感待核'
        r['reason']=('RW/U020归属线索，本轮明确不碰；不据名称作正文结论' if rw else '工具/工程边界，不打开不展开' if tool else '敏感合同与权属未核，仅沿用旧队列路径，不打开不展开' if top=='牌照和保司合同' else '个人/邮件/P&L/RW/账号运维边界，仅沿用入口元数据，不打开不展开')
        r['metadata_basis']='旧队列或父目录名称列表；本轮未单独stat'
        r['mtime']=None; rows.append(r); continue
    try:
        s=snap(p); r.update(stat_before=s,mtime=s['mtime'],size=s['size'],mtime_utc=datetime.fromtimestamp(s['mtime'],timezone.utc).isoformat())
    except Exception as e:
        r.update(status='待核',reason=str(e),mtime=None); rows.append(r); continue
    ext=Path(p).suffix.lower()
    if n.startswith('.'):
        r.update(status='边界排除',reason='隐藏系统入口，不读正文')
    elif stat.S_ISDIR(s['mode']):
        r['reason']='仅直接层名称清单已覆盖；子树未准入、不递归' if p in listings else '新增或混合项目未准入，无根级治理入口证实归属；不递归'
        if top=='AI 培训': r.update(status='仅元数据',reason='已知培训引用入口；仅两PDF元数据，不解析正文')
    elif ext in ['.pdf','.docx','.doc','.xlsx','.xls','.pptx','.ppt']:
        r.update(status='仅元数据',reason='Office/PDF仅元数据引用；项目/版本/现行效力未凭文件名确认')
    elif ext in ['.zip','.mp4','.png','.jpg','.rtf','.txt','.py','.json','.code-workspace']:
        r.update(status='类型排除',reason='非内容型MD/HTML；压缩不解包，媒体不解析，工程/未知文本不读')
    elif n.startswith('鹈鹕骑自行车'):
        r.update(status='边界排除',reason='最大范围明确示例动画不属业务项目；不执行、不打开')
    elif n=='20260901T041201_session.md':
        r['reason']='未标明业务项目的会话记录，可能混合个人/技术内容；无最小治理入口，不打开'
    elif n in preview_names:
        if not 1778389200 <= s['mtime'] < 1794376800:
            r.update(status='窗口排除',reason='固定首次窗口外，不读内容')
        else:
            fd=os.open(p,os.O_RDONLY|os.O_NOFOLLOW)
            try:
                fs=os.fstat(fd)
                assert fs.st_ino==s['ino'] and fs.st_dev==s['dev']
                data=os.read(fd,16384 if ext=='.html' else 2400)
            finally: os.close(fd)
            after=snap(p)
            assert s==after, 'read stat changed'
            decoded=data.decode('utf-8',errors='replace')
            if ext=='.html':
                parser=Visible(); parser.feed(decoded)
                parts=parser.parts
            else:
                parts=list(enumerate(decoded.splitlines(),1))
            chosen=[]; length=0
            for ln,t in parts:
                if length>=1500: break
                t=t[:1500-length]; chosen.append((ln,t)); length+=len(t)
            r.update(read_bytes=len(data),read_chars=length,locators=[{'line':ln,'chars':len(t)} for ln,t in chosen],fragment_hash=hashlib.sha256(data).hexdigest(),hash_scope='prefix bytes only; not whole-source hash',stat_after=after,stat_stable=True,token_proxy=(length+3)//4,governance_preview=chosen,reason='最小治理片段辨归属；不作业务知识分析',read_purpose='最小项目/类型辨识，不是准入后业务分析')
    rows.append(r)
print(json.dumps(dict(queue_total=len(Q),old_scope_count=len(old),window=['2026-05-10T05:00:00Z','2026-11-11T06:00:00Z'],listings=listings,rows=rows),ensure_ascii=False))
