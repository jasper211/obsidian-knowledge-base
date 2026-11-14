import os, sys, stat, json, hashlib
from pathlib import Path
from datetime import datetime, timezone

BASE = Path(__file__).resolve().parent
OUT = BASE / '非RW_模型EA核定.json'
ROOTS = ['/Users/a112233/Desktop/业务模型', '/Users/a112233/Desktop/流程架构项目_jasper']
LOW, HIGH = 1778389200, 1794376800

def check(p):
    p = Path(p)
    for q in [*reversed(p.parents), p]:
        if stat.S_ISLNK(q.lstat().st_mode):
            raise ValueError('symlink rejected: ' + str(q))
    return p.lstat()

def snap(s):
    return dict(dev=s.st_dev, ino=s.st_ino, size=s.st_size, mtime_ns=s.st_mtime_ns, ctime_ns=s.st_ctime_ns)

def read(p, ranges=None):
    p = Path(p)
    s = check(p)
    assert any(str(p).startswith(r + '/') for r in ROOTS)
    assert p.suffix.lower() in ('.md', '.html', '.htm')
    assert LOW <= s.st_mtime < HIGH, 'outside window'
    fd = os.open(p, os.O_RDONLY | os.O_NOFOLLOW)
    with os.fdopen(fd, 'rb') as f:
        before = os.fstat(f.fileno())
        raw = f.read()
        after = os.fstat(f.fileno())
    assert snap(s) == snap(before) == snap(after) == snap(check(p)), 'unstable'
    txt = raw.decode('utf-8-sig')
    lines = txt.splitlines()
    ranges = ranges or [[1, len(lines)]]
    shown = [(i,line) for i,line in enumerate(lines,1) if any(a<=i<=b for a,b in ranges)]
    record = dict(path=str(p), mtime=s.st_mtime, mtime_utc=datetime.fromtimestamp(s.st_mtime, timezone.utc).isoformat(), source_hash=hashlib.sha256(raw).hexdigest(), first_stat=snap(s), after_stat=snap(after), stable=True, read_bytes=len(raw), read_chars=len(txt), lines=len(lines), displayed_ranges=ranges, displayed_chars=sum(len(t)+1 for _,t in shown), token_count=None, status='已读取待语义处置')
    data = json.loads(OUT.read_text()) if OUT.exists() else {'roots':ROOTS, 'reads':[]}
    data['reads'] = [x for x in data['reads'] if x['path'] != str(p)] + [record]
    for item in data['reads']:
        item.pop('token_proxy', None)
        item.pop('token_proxy_method', None)
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(record, ensure_ascii=False))
    for i, line in shown:
        print(f'{i}: {line}')

if __name__ == '__main__':
    read(sys.argv[1])
