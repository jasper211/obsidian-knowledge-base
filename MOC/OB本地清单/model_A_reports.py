"""Render source indexes from existing ledgers only; never open source files."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = ROOT / '非RW_模型EA核定.json'
FROZEN = ROOT / '模型338续批冻结输入.json'
assert hashlib.sha256(BASE.read_bytes()).hexdigest() == 'eee3b9398f2f8e2f16c9c7897d07277a215a3ad16c7a1054f6ba06bfe54853cf'
assert hashlib.sha256(FROZEN.read_bytes()).hexdigest() == '066ebd5afe0fa699e020b9b7e54e0017d975097277a7aa6f3ca163448bf9001d'
base = json.loads(BASE.read_text())
a = json.loads((ROOT / '模型续批_A.json').read_text())

def index(records, initial=False):
    out = ['## 每源定位与读取账本', '', '下列定位为已记录语义证据；字节/字符为实际读取代理，不是token。完整hash及逐次stat见对应JSON。', '']
    for n, r in enumerate(records):
        ident = f'S{n+1:02}' if initial else r['id']
        p = r['path']
        loc = ', '.join(r.get('locators', []))
        out += [f'### {ident} · {r["status"]}', '', f'[{Path(p).name}](<{p}>)', '',
                f'- 定位：{loc}。', f'- 处置依据：{r["reason"]}',
                f'- mtime：{r.get("mtime_utc", r.get("mtime"))}；读取{r["read_bytes"]}字节/{r["read_chars"]}字符。',
                f'- 完整源SHA256：{r.get("source_hash") or "未读取完整源；仅有片段hash，见read_events"}。', '']
    return '\n'.join(out)

initial = ROOT.parent / '非RW_模型EA业务主题.md'
text = initial.read_text().split('<!-- SOURCE_INDEX -->')[0]
text += '\n## audit_notes：冻结记录与后续限定\n\n'
text += '\n'.join('- ' + note for note in base['audit_notes'])
text += '\n\n以上为冻结账本原文，最后一项是当时核查状态；后续James对准入记录一致性限定通过，并非全面验收。特别保留3份治理文件整文件字节读取，以及价值节点V4整读混合正文后才隔离的问题，不追认最小性。旧账本纳秒字段为JSON number，存在跨工具安全整数精度风险；本报告不重读源文件或改写冻结记录消除历史风险。A续批使用字符串纳秒。\n\n<!-- SOURCE_INDEX -->\n\n'
initial.write_text(text + index(sorted(base['reads'], key=lambda r: r['path']), True) + '\n')
report = ROOT.parent / '模型业务主题_A.md'
report.write_text(report.read_text().split('<!-- SOURCE_INDEX -->')[0] + '<!-- SOURCE_INDEX -->\n\n' + index(a['records']) + '\n')
assert len(a['records']) == 79
assert set(r['path'] for r in a['records']) == set(a['scope_paths'])
assert len(set(r['path'] for r in a['records'])) == 79
for r in a['records']:
    assert all(k in r for k in ['path', 'status', 'reason', 'locators', 'read_chars', 'read_bytes'])
    assert r['stable_at_finalize']
def check_ns(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k.endswith('_ns'):
                assert isinstance(v, str), (k, type(v))
            check_ns(v)
    elif isinstance(obj, list):
        for v in obj:
            check_ns(v)
check_ns(a)
print(json.dumps(a['counts'], ensure_ascii=False))
print('Initial source index: 28; A source index: 79. Frozen input and baseline hashes unchanged.')
