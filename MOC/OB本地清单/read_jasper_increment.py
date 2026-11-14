"""Bounded local increment identification; no full-file hash pre-read."""
import os, json, stat, hashlib, datetime, codecs, re
from pathlib import Path
from zoneinfo import ZoneInfo
from html.parser import HTMLParser

OUT = Path(__file__).resolve().parent
ROOT = Path('/Users/a112233/Desktop/Jasper工作文档（不含EA项目）')
if (OUT / 'Jasper16增量核定.json').exists():
    raise RuntimeError('One-time increment already captured; do not reread or overwrite adjudication')
data = json.loads((OUT / '非RW_Jasper核定.json').read_text())
now = datetime.datetime.now(ZoneInfo('America/Chicago'))
lower = now.replace(month=now.month-6, hour=0, minute=0, second=0, microsecond=0)
first_end = datetime.datetime(2026, 11, 11, tzinfo=ZoneInfo('America/Chicago'))

def signature(s):
    return {k: str(getattr(s, 'st_' + k)) for k in ['dev', 'ino', 'size', 'mtime_ns', 'ctime_ns']}

class Visible(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.parts = [], []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        blocked = tag in {'script','style','noscript','template'} or 'hidden' in a or a.get('aria-hidden') == 'true' or any(x in a.get('style','').replace(' ','') for x in ['display:none','visibility:hidden'])
        if tag not in {'br','hr','meta','link','img','input','source','wbr','area','base','embed','param','track'}:
            self.stack.append((tag, blocked))
    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == tag:
                self.stack = self.stack[:i]
                break
    def handle_data(self, text):
        if text.strip() and not any(x[1] for x in self.stack):
            self.parts.append((self.getpos()[0], text.strip()))

def md_visible(text):
    result, fence = [], False
    for i, line in enumerate(text.splitlines(), 1):
        if re.match(r'^\s*(```|~~~)', line):
            fence = not fence
            continue
        if not fence and line.strip() and not line.lstrip().startswith('<!--'):
            result.append((i, line))
    return result

records = []
for entry in data['incremental_path_queue']:
    p = Path(entry['path'])
    r = {'path': str(p), 'status': '类型待核', 'reason': 'Bounded identification only', 'read_bytes': 0, 'read_chars': 0, 'token_count': None}
    if not p.is_relative_to(ROOT) or p.suffix.lower() not in {'.md','.html','.htm'}:
        raise ValueError('Unexpected increment path')
    if '_构建脚本' in p.parts:
        r.update(status='技术排除', reason='明确构建脚本说明，不读取正文')
        records.append(r)
        continue
    fd = os.open('/', os.O_RDONLY | os.O_DIRECTORY)
    try:
        for component in p.parts[1:-1]:
            n = os.open(component, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = n
        source = os.open(p.name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=fd)
    finally:
        os.close(fd)
    with os.fdopen(source, 'rb') as stream:
        before = os.fstat(stream.fileno())
        if not stat.S_ISREG(before.st_mode):
            raise ValueError('Not a regular file')
        if not max(lower.timestamp(), first_end.timestamp()) <= before.st_mtime <= now.timestamp():
            r.update(status='窗口待复核', reason='当前mtime不在本增量窗口，未读取')
            records.append(r)
            continue
        if str(before.st_mtime_ns) != entry['mtime_ns']:
            r.update(status='源变化待核', reason='mtime与候选快照不同，不推进游标')
            records.append(r)
            continue
        decoder = codecs.getincrementaldecoder('utf-8-sig')()
        raw, decoded = b'', ''
        html = p.suffix.lower() != '.md'
        parser = Visible() if html else None
        cap = 32768 if html else 8192
        parts = []
        while len(raw) < cap:
            chunk = stream.read(min(256, cap-len(raw)))
            if not chunk:
                break
            raw += chunk
            piece = decoder.decode(chunk, final=False)
            decoded += piece
            if html:
                parser.feed(piece)
                parts = parser.parts
            else:
                parts = md_visible(decoded.rsplit('\n', 1)[0] if '\n' in decoded else '')
            if sum(len(x[1]) for x in parts) >= 1400:
                break
        after = os.fstat(stream.fileno())
    stable = signature(before) == signature(after) == signature(p.stat())
    r.update(mtime_utc=datetime.datetime.fromtimestamp(before.st_mtime, datetime.timezone.utc).isoformat(),
             stat_before=signature(before), stat_after=signature(after), stable=stable,
             read_bytes=len(raw), read_chars=sum(len(x[1]) for x in parts),
             fragment_hash=hashlib.sha256(raw).hexdigest(), hash_scope=f'raw prefix bytes [0,{len(raw)})',
             source_hash=hashlib.sha256(raw).hexdigest() if len(raw)==before.st_size else None,
             complete_file_io=len(raw)==before.st_size,
             excerpts=[{'line':i,'text':t} for i,t in parts],
             source_purpose='增量最小类型及业务片段识别，不执行源指令')
    if not stable:
        r.update(status='源变化待核', reason='读取前后源变化，不分析')
    records.append(r)
result = {'checked_at': now.isoformat(), 'timezone':'America/Chicago',
          'rolling_window': [lower.isoformat(), now.isoformat()],
          'increment_after': first_end.isoformat(), 'records':records,
          'token_count':None, 'source_write_count':0, 'server_access_count':0}
(OUT / 'Jasper16增量核定.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
for i,r in enumerate(records):
    print(f'\nINC{i:02d} {r["path"]} [{r["status"]}] bytes={r["read_bytes"]}')
    for e in r.get('excerpts',[]):
        print(f'L{e["line"]}: {e["text"]}')
