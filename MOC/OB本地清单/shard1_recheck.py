import hashlib
import json
import os
import stat
import sys
from pathlib import Path
from shard1_audit import no_links, snapshot

BASE = Path(__file__).parent
OUT = BASE / '分片1_处置.json'

def main():
    rows = json.loads(OUT.read_text())
    wanted = {int(s) for s in sys.argv[1].split(',')}
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    stop = int(sys.argv[3]) if len(sys.argv) > 3 else 85
    for r in rows:
        if r['index'] not in wanted:
            continue
        p = Path(r['path'])
        assert str(p).startswith('/Users/a112233/Desktop/Rw权益项目/')
        assert p.suffix.lower() == '.md'
        assert 1778389200 <= r['stat_before']['mtime_ns']/1e9 < 1794376800
        no_links(p)
        s = p.lstat()
        assert stat.S_ISREG(s.st_mode)
        assert 1778389200 <= s.st_mtime < 1794376800
        with os.fdopen(os.open(p, os.O_RDONLY | os.O_NOFOLLOW), 'rb') as f:
            assert snapshot(s) == snapshot(os.fstat(f.fileno()))
            data = f.read()
            after = os.fstat(f.fileno())
        no_links(p)
        end = p.lstat()
        assert snapshot(s) == snapshot(after) == snapshot(end)
        sha = hashlib.sha256(data).hexdigest()
        if r['source_hash']:
            assert r['source_hash'] == sha, 'Source changed since prior read'
        t = data.decode('utf-8-sig')
        lines = t.splitlines(keepends=True)
        selected = lines[start-1:stop]
        evidence = dict(stat_before=snapshot(s), stat_after=snapshot(end), stat_stable=True,
                        source_hash=sha, read_bytes=len(data), extracted_chars=len(t),
                        displayed_range=f'L{start}-L{min(stop,len(lines))}',
                        displayed_chars=sum(len(x) for x in selected))
        r.setdefault('recheck_reads', []).append(evidence)
        r.setdefault('prior_disposition', {k:r.get(k) for k in ('status','reason','locators','read_chars','read_bytes','source_hash','semantic_review')})
        r.update(source_hash=sha, source_hash_algorithm='sha256', hash_missing_reason=None,
                 read_bytes=len(data), read_chars=len(t), text_lines=len(lines),
                 content_gate='用户澄清授权业务片段核定；治理/财务/历史合规主题不作为禁读理由',
                 token_count=None,token_proxy={'method':'ceil(extracted_unicode_chars/2); 非真实token','value':(len(t)+1)//2})
        print(f'\n=== S{r["index"]} {p.name} ({len(lines)} lines) ===')
        for n,line in enumerate(selected,start):
            print(f'{n}: {line.rstrip()}')
    OUT.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')

if __name__ == '__main__':
    main()
