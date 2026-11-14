import os,sys,json,hashlib
from pathlib import Path
from nonrw_model_ea import BASE,check,LOW,HIGH

def snap(s):
    return dict(dev=s.st_dev,ino=s.st_ino,size=s.st_size,mtime_ns=str(s.st_mtime_ns),ctime_ns=str(s.st_ctime_ns))
SOURCE=BASE/'模型338续批冻结输入.json'
OUT=BASE/'模型续批_A.json'
EXPECTED='066ebd5afe0fa699e020b9b7e54e0017d975097277a7aa6f3ca163448bf9001d'

def init():
    raw=SOURCE.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==EXPECTED,'frozen source changed'
    base=json.loads(raw)
    paths=sorted(x['path'] for x in base['groups']['A'])
    assert len(paths)==79
    if OUT.exists():
        d=json.loads(OUT.read_text());assert d['scope_paths']==paths
        d.update(frozen_input=str(SOURCE),frozen_input_sha256=EXPECTED)
        return d
    return dict(schema_version='model-continuation-A-1',frozen_input=str(SOURCE),frozen_input_sha256=EXPECTED,scope_paths=paths,file_decisions=[dict(id=f'A{i:02}',path=p,status='待类型复筛',read_bytes=0,read_chars=0,source_hash=None,locators=[],read_events=[]) for i,p in enumerate(paths)],token_count=None)

def read(i,start=1,end=60):
    d=init();r=d['file_decisions'][i];p=Path(r['path']);s=check(p)
    assert p.suffix=='.md' and LOW<=s.st_mtime<HIGH
    with os.fdopen(os.open(p,os.O_RDONLY|os.O_NOFOLLOW),'rb') as f:
        before=os.fstat(f.fileno())
        lines=[]
        for j in range(end):
            line=f.readline()
            if not line:break
            lines.append(line)
        whole=sum(map(len,lines))==s.st_size
        after=os.fstat(f.fileno())
    assert snap(s)==snap(before)==snap(after)==snap(check(p))
    raw=b''.join(lines);txt=raw.decode('utf-8-sig');shown=txt.splitlines()[start-1:end]
    event=dict(first_stat=snap(s),after_stat=snap(after),stable=True,read_bytes=len(raw),read_chars=len(txt),displayed_ranges=[[start,min(end,len(lines))]],displayed_chars=sum(len(t)+1 for t in shown),whole_file=whole,fragment_hash=hashlib.sha256(raw).hexdigest())
    r['read_events'].append(event);r.update(mtime=s.st_mtime,mtime_ns=str(s.st_mtime_ns),size=s.st_size,read_bytes=sum(e['read_bytes'] for e in r['read_events']),read_chars=sum(e['read_chars'] for e in r['read_events']),status='已读待处置')
    if whole:r['source_hash']=hashlib.sha256(raw).hexdigest()
    OUT.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    print(f'=== {r["id"]} {p.name} | lines {start}-{min(end,len(lines))} whole={whole} ===')
    for j,t in enumerate(shown,start):print(f'{j}: {t}')

if __name__=='__main__':
    a,b=map(int,sys.argv[1:3]);end=int(sys.argv[3]) if len(sys.argv)>3 else 60
    for i in range(a,b):read(i,1,end)
