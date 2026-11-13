import json,hashlib,os,stat
from pathlib import Path
p=Path(__file__).parent
groups=json.loads((p/'疑似重复待核.json').read_text())
out=[]
for name,paths in groups.items():
    if not name.startswith('Amanda'):continue
    hashes=[]
    for path in paths:
        f=Path(path)
        if any(q.is_symlink() for q in [f,*f.parents]):raise RuntimeError('symlink')
        fd=os.open(f,os.O_RDONLY|os.O_NOFOLLOW)
        with os.fdopen(fd,'rb') as stream:
            a=os.fstat(stream.fileno())
            if not stat.S_ISREG(a.st_mode) or not 1778389200<=a.st_mtime<1794376800:raise RuntimeError('window/type')
            data=stream.read();b=os.fstat(stream.fileno())
        if (a.st_mtime_ns,a.st_ctime_ns,a.st_size)!=(b.st_mtime_ns,b.st_ctime_ns,b.st_size):raise RuntimeError('changed')
        hashes.append({'path':path,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
    out.append({'name':name,'files':hashes,'byte_identical':len({x['sha256'] for x in hashes})==1,'authority':'未核，字节一致不证明主源权威'})
(p/'业务摘要字节去重.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps({'groups':len(out),'identical':sum(x['byte_identical'] for x in out),'files':sum(len(x['files']) for x in out),'redundant':sum(len(x['files'])-1 for x in out if x['byte_identical'])}))
