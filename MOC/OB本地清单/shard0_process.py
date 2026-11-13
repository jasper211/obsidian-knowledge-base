import os, stat, json, hashlib, sys
from pathlib import Path
from html.parser import HTMLParser

BASE = Path(__file__).parent
EXCLUDED = {'45_TOB服务目录与验收口径_v0.2.md', '45_TOI价值证明框架与报表模板_v0.2.md', '45_SHARED权益资产字段冻结与变更规则_v0.2.md'}
FULL_READ = {0, 28, 36, 40, 44, 48, 52, 64, 68, 80, 132, 136, 140, 168, 176}
READ = set(range(0, 182, 4))
SENSITIVE = {4, 8, 12, 16, 20, 84, 100, 104, 112, 116, 120, 160}
TECH = {60, 72, 76}

class TextOnly(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'template', 'noscript'):
            self.skip += 1
        elif not self.skip and tag in ('p', 'div', 'section', 'article', 'li', 'tr', 'br', 'h1', 'h2', 'h3', 'h4'):
            self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'template', 'noscript') and self.skip:
            self.skip -= 1
        elif not self.skip and tag in ('p', 'div', 'section', 'article', 'li', 'tr', 'h1', 'h2', 'h3', 'h4'):
            self.parts.append('\n')
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

def signature(s):
    return [s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns, s.st_ctime_ns]

def safe_open(path):
    # Walk every component with O_NOFOLLOW, including directories.
    parts = Path(path).parts
    fd = os.open('/', os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in parts[1:-1]:
            nxt = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = nxt
        return os.open(parts[-1], os.O_RDONLY | os.O_NOFOLLOW, dir_fd=fd)
    finally:
        os.close(fd)

def run():
    source = json.loads((BASE / '295项处置明细.json').read_text())
    candidates = [r for r in source if r['status'] == '业务候选待内容核定']
    assert len(candidates) == 185
    paths = sorted(r['path'] for r in candidates if Path(r['path']).name not in EXCLUDED)
    assert len(paths) == 182
    entries = {r['path']: r for r in json.loads((BASE / '文件准入队列.json').read_text())}
    rows = []
    requested = set(map(int, sys.argv[1:]))
    for i, p in enumerate(paths):
        if i % 4:
            continue
        r = dict(path=p, sorted_index=i, status='待核', reason='', source_hash=None, mtime=None,
                 locators=[], read_chars=0, read_bytes=0, token_count=None, token_proxy=None,
                 project_evidence='文件准入队列.json: ' + entries.get(p, {}).get('reason', '无归属证据'))
        rows.append(r)
        if entries.get(p, {}).get('reason') != 'RW用户保留；扩展名不证明业务正文':
            r['reason'] = '项目RW归属未确认，隔离且未读正文'
            continue
        kind = '业务候选' if i in READ else ('敏感/合规未知' if i in SENSITIVE else ('技术/架构' if i in TECH else '治理/内容未知'))
        r['content_precheck'] = kind
        try:
            for component in [Path(p), *Path(p).parents]:
                if stat.S_ISLNK(component.lstat().st_mode):
                    raise ValueError('拒绝符号链接或链接父目录')
            s = os.stat(p, follow_symlinks=False)
            r.update(mtime=s.st_mtime, mtime_ns=s.st_mtime_ns, size_bytes=s.st_size, stat_before=signature(s))
            if not stat.S_ISREG(s.st_mode):
                r.update(status='排除', reason='非普通文件')
                continue
            if not 1778389200 <= s.st_mtime < 1794376800:
                r.update(status='排除', reason='首次stat不在授权首次窗口，未读正文')
                continue
            if Path(p).suffix.lower() not in ('.md', '.html'):
                r.update(status='排除', reason='非MD/HTML，未读正文')
                continue
            if i not in READ:
                r['reason'] = kind + '：仅文件名/既有清单预检，未读正文、不作业务分析；hash为空因未读取字节'
                r['stat_after'] = signature(os.stat(p, follow_symlinks=False))
                r['stat_stable'] = r['stat_before'] == r['stat_after']
                continue
            fd = safe_open(p)
            with os.fdopen(fd, 'rb') as f:
                before = os.fstat(f.fileno())
                if signature(before) != signature(s):
                    raise ValueError('打开前stat已变化')
                raw = f.read()
                after = os.fstat(f.fileno())
            post = os.stat(p, follow_symlinks=False)
            r.update(stat_after=signature(post), stat_stable=signature(s) == signature(after) == signature(post),
                     source_hash=hashlib.sha256(raw).hexdigest(), read_bytes=len(raw))
            if not r['stat_stable']:
                raise ValueError('读取前后stat不稳定，不纳入分析')
            text = raw.decode('utf-8-sig')
            if Path(p).suffix.lower() == '.html':
                parser = TextOnly()
                parser.feed(text)
                text = '\n'.join(line.strip() for line in ''.join(parser.parts).splitlines() if line.strip())
                r['locator_type'] = 'HTML静态去脚本样式文本行T'
            else:
                r['locator_type'] = 'MD源文件行L'
            total_chars = len(text)
            if i not in FULL_READ:
                text = text[:3500]
                if len(text) < total_chars:
                    text = text.rsplit('\n', 1)[0]
            r.update(read_chars=len(text), text_lines=len(text.splitlines()), extracted_total_chars=total_chars,
                     read_scope='全文静态文本' if len(text)==total_chars else '最小业务片段：源文开头至所列末行',
                     token_proxy={'method':'ceil(read_chars/2)，仅字符代理非真实token', 'value':(len(text)+1)//2}, reason='已安全读取，待逐文人工语义分析')
            if i in requested:
                print('\n===== INDEX', i, p, 'chars', len(text), '=====')
                print('\n'.join(f'{n}: {line}' for n, line in enumerate(text.splitlines(), 1)))
        except (OSError, ValueError, UnicodeError) as e:
            r.update(status='待核', reason='安全隔离: ' + str(e))
    if not requested:
        (BASE / '分片0_处置.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
        print(json.dumps({'total':len(rows), 'read':sum(r['read_chars']>0 for r in rows), 'rows':[(r['sorted_index'],r['reason'],r['read_chars']) for r in rows]},ensure_ascii=False))

if __name__ == '__main__':
    run()
