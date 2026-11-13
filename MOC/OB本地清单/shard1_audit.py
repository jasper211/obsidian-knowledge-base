import os, stat, json, hashlib
from pathlib import Path
from html.parser import HTMLParser

BASE = Path(__file__).parent
EX = {'45_TOB服务目录与验收口径_v0.2.md', '45_TOI价值证明框架与报表模板_v0.2.md', '45_SHARED权益资产字段冻结与变更规则_v0.2.md'}
READ = {13,21,25,29,33,37,41,45,49,53,69,165,169,173,177,181}

class TextOnly(HTMLParser):
    def __init__(self):
        super().__init__(); self.hidden = 0; self.lines = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style'): self.hidden += 1
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.hidden = max(0, self.hidden - 1)
    def handle_data(self, data):
        if not self.hidden and data.strip(): self.lines.append(data.strip())

def snapshot(s):
    return dict(dev=s.st_dev, ino=s.st_ino, size=s.st_size, mtime_ns=s.st_mtime_ns, ctime_ns=s.st_ctime_ns)

def no_links(p):
    for part in [*reversed(p.parents), p]:
        if stat.S_ISLNK(part.lstat().st_mode): raise ValueError('路径或祖先为符号链接')

def main():
    original = json.loads((BASE/'295项处置明细.json').read_text())
    selected = sorted((r for r in original if r['status']=='业务候选待内容核定' and Path(r['path']).name not in EX), key=lambda r:r['path'])
    rows=[]; texts={}
    for i,item in enumerate(selected):
        if i%4 != 1: continue
        p=Path(item['path'])
        r=dict(path=str(p), index=i, status='待核', reason='', source_hash=None, mtime=None, locators=[], read_chars=0, read_bytes=0, token_count=None, token_proxy=None, project_basis='项目入口队列.json: /Users/a112233/Desktop/Rw权益项目 限定保留；仅归属证据，非内容批准')
        rows.append(r)
        if not str(p).startswith('/Users/a112233/Desktop/Rw权益项目/'):
            r['reason']='RW项目归属未确认'; continue
        r['content_gate']='必要业务文本候选' if i in READ else '治理/技术/合规或潜在敏感资料隔离，不读取正文'
        try:
            no_links(p); s=p.lstat(); r['mtime']=s.st_mtime; r['stat_before']=snapshot(s)
            if not stat.S_ISREG(s.st_mode): raise ValueError('不是普通文件')
            if p.suffix.lower() not in ('.md','.html'): raise ValueError('非MD/HTML')
            if not 1778389200 <= s.st_mtime < 1794376800:
                r.update(status='排除',reason='首次stat不在指定mtime窗口'); continue
            if i not in READ:
                r['reason']='文件用途指向治理、技术、合规或敏感经营记录；未获必要业务正文准入，单列待核，不据标题分析'
                r['stat_after']=snapshot(p.lstat()); r['stat_stable']=r['stat_before']==r['stat_after']; continue
            fd=os.open(p,os.O_RDONLY|os.O_NOFOLLOW)
            with os.fdopen(fd,'rb') as f:
                opened=os.fstat(f.fileno())
                if snapshot(opened)!=snapshot(s): raise ValueError('打开前stat变化')
                data=f.read(); after=os.fstat(f.fileno())
            no_links(p); end=p.lstat()
            r.update(stat_after=snapshot(end),stat_stable=snapshot(s)==snapshot(after)==snapshot(end),read_bytes=len(data),source_hash=hashlib.sha256(data).hexdigest())
            if not r['stat_stable']: raise ValueError('读取前后stat不稳定')
            text=data.decode('utf-8-sig')
            if p.suffix.lower()=='.html':
                parser=TextOnly(); parser.feed(text); text='\n'.join(parser.lines)
            r.update(read_chars=len(text),token_proxy={'method':'ceil(extracted_unicode_chars/2); 非真实token','value':(len(text)+1)//2},text_lines=len(text.splitlines()),locator_kind='HTML去script/style后文本行T' if p.suffix.lower()=='.html' else 'Markdown源行L')
            texts[str(i)]=text
            r['reason']='稳定读取完成，等待逐文人工语义处置'
        except (OSError,ValueError,UnicodeError) as e:
            r['reason']=str(e)
    (BASE/'分片1_读取证据.json').write_text(json.dumps({'rows':rows,'texts':texts},ensure_ascii=False,indent=2))
    print(json.dumps({'selected':len(rows),'read':[(r['index'],r['read_chars']) for r in rows if r['read_chars']]},ensure_ascii=False))

if __name__=='__main__': main()
