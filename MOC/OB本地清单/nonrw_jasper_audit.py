import os,json,stat,hashlib,re
from pathlib import Path
from html.parser import HTMLParser
ROOT=Path("/Users/a112233/Desktop/Jasper工作文档（不含EA项目）")
VAULT=ROOT/"OB知识库_vault"
SCOPES=["A_大模型接手准则","项目工作区/00_EE方法论标准","项目工作区/合规引擎本体项目工作区","项目工作区/自动续保提醒及例行客户通信项目工作区","项目工作区/蓝象合规引擎项目工作区","项目工作区/规则分析_价值节点工作区/01_价值节点盘点"]
STOP={"workbench":"技术实现边界","schema":"技术schema","precheck":"技术校验","pilot":"试点实体数据未明确脱敏","eval":"技术测试","06_程序":"技术程序","07_运行输出_含客户数据仅本地":"明确客户数据边界","00_原始材料_含客户数据仅本地":"明确客户数据边界","09_安装包":"技术安装包","08_工作台原型":"实验原型","_仅合规留存":"用途受限留存","node_modules":"依赖","90_EE准备稿归档":"工程准备稿","_脚本":"技术脚本","visual-check":"技术视觉测试","Demo交互复刻_Codex_20260924":"已由同源Demo说明确认实验"}
def sig(s):
 return dict(dev=str(s.st_dev),ino=str(s.st_ino),size=s.st_size,mtime_ns=str(s.st_mtime_ns),ctime_ns=str(s.st_ctime_ns))
def walk():
 out=[]; boundaries=[]
 def visit(p):
  for x in sorted(p.iterdir(),key=lambda p:str(p)):
   if x.name.startswith("."):boundaries.append(dict(path=str(x),reason="隐藏入口不读",kind="boundary"));continue
   s=x.lstat()
   if stat.S_ISLNK(s.st_mode):boundaries.append(dict(path=str(x),reason="拒绝链接",kind="boundary"));continue
   if stat.S_ISDIR(s.st_mode):
    if x.name in STOP:boundaries.append(dict(path=str(x),reason=STOP[x.name],kind="boundary"))
    else:visit(x)
   else:
    ext=x.suffix.lower()
    typ="MD" if ext==".md" else "HTML" if ext in (".html",".htm") else "Office元数据" if ext in (".docx",".doc",".xlsx",".xls",".pptx",".ppt") else "非准入类型元数据"
    status="候选正文" if typ in ("MD","HTML") else "仅元数据"
    if status=="候选正文" and not 1778389200<=s.st_mtime<1794376800:status="后期增量" if s.st_mtime>=1794376800 else "早于窗口"
    out.append(dict(path=str(x),type=typ,mtime=s.st_mtime,size=s.st_size,status=status,stat_inventory=sig(s),read_chars=0,read_bytes=0,source_hash=None,locators=[]))
 for s in SCOPES:visit(ROOT/s)
 return out,boundaries
class Visible(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.stack=[];self.parts=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs);blocked=tag in ("script","style","noscript","template","head") or "hidden" in a or a.get("aria-hidden")=="true" or any(t in a.get("style","").replace(" ","").lower() for t in ("display:none","visibility:hidden"))
  if tag not in ("meta","br","img","input","hr","link","source","wbr","area","base","embed","param","track"):self.stack.append((tag,blocked))
 def handle_endtag(self,tag):
  for i in range(len(self.stack)-1,-1,-1):
   if self.stack[i][0]==tag:self.stack=self.stack[:i];break
 def handle_data(self,data):
  if data.strip() and not any(b for _,b in self.stack):self.parts.append((self.getpos()[0],data.strip()))
def read(p,limit=1200,byte_limit=4096):
 p=Path(p)
 for c in [p,*p.parents]:
  if stat.S_ISLNK(c.lstat().st_mode):raise ValueError("拒绝链接")
 if p.suffix.lower() not in (".md",".html",".htm"):raise ValueError("非准入类型")
 s=p.stat()
 if not 1778389200<=s.st_mtime<1794376800:raise ValueError("不在窗口")
 fd=os.open("/",os.O_RDONLY|os.O_DIRECTORY)
 try:
  for c in p.parts[1:-1]:
   n=os.open(c,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW,dir_fd=fd);os.close(fd);fd=n
  ff=os.open(p.name,os.O_RDONLY|os.O_NOFOLLOW,dir_fd=fd)
 finally:os.close(fd)
 with os.fdopen(ff,"rb") as f:
  assert sig(os.fstat(f.fileno()))==sig(s)
  raw=f.read(byte_limit)
  assert sig(os.fstat(f.fileno()))==sig(s)
 complete=len(raw)==s.st_size
 decoder=__import__("codecs").getincrementaldecoder("utf-8-sig")()
 t=decoder.decode(raw,final=complete)
 if not complete and "\n" in t:t=t.rsplit("\n",1)[0]
 if p.suffix.lower() in (".html",".htm"):
  parser=Visible();parser.feed(t);parts=parser.parts
 else:
  parts=[];fence=None;comment=False
  for i,line in enumerate(t.splitlines(),1):
   if re.match(r"^\s*(```|~~~)",line):
    fence=None if fence else line.strip()[:3];continue
   if fence:continue
   line=re.sub(r"<script\b[^>]*>.*?</script>|<style\b[^>]*>.*?</style>","",line,flags=re.I)
   if "<!--" in line:comment=True
   if comment:
    if "-->" in line:comment=False
    continue
   if line.strip():parts.append((i,line))
 selected=[];n=0
 for line,txt in parts:
  if n+len(txt)>limit and selected:break
  if not selected and len(txt)>limit:txt=txt[:limit]
  selected.append((line,txt));n+=len(txt)+1
 after=p.stat();assert sig(after)==sig(s)
 return dict(path=str(p),source_hash=hashlib.sha256(raw).hexdigest() if complete else None,fragment_hash=hashlib.sha256(raw).hexdigest(),hash_scope="full_file" if complete else "prefix_bytes",byte_range=[0,len(raw)],mtime=s.st_mtime,stat_before=sig(s),stat_after=sig(after),stable=True,read_bytes=len(raw),read_chars=sum(len(t) for _,t in selected),visible_fragment_chars=sum(len(t) for _,t in parts),locators=[dict(line_start=i,line_end=i) for i,t in selected],text="\n".join(f"L{i}: {t}" for i,t in selected),purpose="最小正文类型及业务片段核定",limit_chars=limit,byte_limit=byte_limit,complete_file_io=complete)
if __name__=="__main__":
 import sys
 if sys.argv[1]=="inventory":
  a,b=walk();print(json.dumps(dict(files=a,boundaries=b),ensure_ascii=False))
 elif sys.argv[1]=="read":
  paths=json.loads(sys.argv[2]);print(json.dumps([read(p,int(sys.argv[3]),int(sys.argv[4]) if len(sys.argv)>4 else 4096) for p in paths],ensure_ascii=False))

