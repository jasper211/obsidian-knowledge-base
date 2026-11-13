import hashlib
import json
import os
import stat
import sys
from pathlib import Path

BASE=Path(__file__).parent
OUT=BASE/'治理1_处置.json'

def snap(s):
    return dict(dev=s.st_dev,ino=s.st_ino,size=s.st_size,mtime_ns=s.st_mtime_ns,ctime_ns=s.st_ctime_ns)

def no_links(p):
    for q in [*reversed(p.parents),p]:
        if stat.S_ISLNK(q.lstat().st_mode): raise ValueError('symlink refused')

def main():
    if sys.argv[1]=='init':
        assert not OUT.exists(), 'Do not overwrite existing work'
        source=json.loads((BASE/'295项处置明细.json').read_text())
        selected=sorted((r for r in source if r['status']=='治理证据暂缓'),key=lambda r:r['path'])
        assert len(selected)==85
        rows=[]
        for i,item in enumerate(selected):
            if i%3!=1: continue
            p=Path(item['path'])
            r=dict(path=str(p),index=i,status='待核',reason='正文类型待核定',mtime=None,source_hash=None,hash=None,locators=[],read_chars=0,read_bytes=0,token_count=None,knowledge=[],read_events=[])
            rows.append(r)
            try:
                no_links(p); s=p.lstat(); r.update(mtime=s.st_mtime,first_stat=snap(s),window_ok=1778389200<=s.st_mtime<1794376800)
                assert r['window_ok'], 'outside first-stat window'
                assert stat.S_ISREG(s.st_mode), 'not regular file'
                assert str(p).startswith('/Users/a112233/Desktop/Rw权益项目/'), 'project unknown'
                assert p.suffix.lower()=='.md', 'not allowed business text type'
            except (OSError,ValueError,AssertionError) as e:
                r['reason']=str(e); r['blocked_before_read']=True
            print(i,s.st_size if r['mtime'] else None,p.name)
        OUT.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
        return
    rows=json.loads(OUT.read_text())
    ids={int(i) for i in sys.argv[1].split(',')}
    lo=int(sys.argv[2]); hi=int(sys.argv[3])
    for r in rows:
        if r['index'] not in ids or r.get('blocked_before_read'): continue
        p=Path(r['path']); no_links(p); before=p.lstat()
        assert snap(before)==r['first_stat'], 'source metadata changed'
        with os.fdopen(os.open(p,os.O_RDONLY|os.O_NOFOLLOW),'rb') as f:
            assert snap(os.fstat(f.fileno()))==snap(before)
            data=f.read(); fd_after=os.fstat(f.fileno())
        no_links(p); after=p.lstat()
        assert snap(before)==snap(fd_after)==snap(after)
        sha=hashlib.sha256(data).hexdigest()
        assert not r['source_hash'] or r['source_hash']==sha
        text=data.decode('utf-8-sig'); lines=text.splitlines(keepends=True)
        excerpt=lines[lo-1:hi]
        r.update(source_hash=sha,hash=sha,hash_algorithm='sha256',read_bytes=len(data),read_chars=len(text),text_lines=len(lines),stat_after=snap(after),stat_stable=True,token_proxy={'method':'ceil(extracted_unicode_chars/2); not real tokens','value':(len(text)+1)//2})
        r['read_events'].append(dict(stat_before=snap(before),stat_after=snap(after),sha256=sha,read_bytes=len(data),extracted_chars=len(text),displayed_range=f'L{lo}-L{min(hi,len(lines))}',displayed_chars=sum(len(s) for s in excerpt)))
        print(f'\n=== G{r["index"]} {p.name} ({len(lines)} lines) ===')
        for n,line in enumerate(excerpt,lo): print(f'{n}: {line.rstrip()}')
    OUT.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__': main()
