"""Record Descartes' returned metadata-only review, without source access."""
import hashlib
import json
from pathlib import Path
B = Path(__file__).resolve().parent
p = B / 'daily_proposal_20261117T090214157237.json'
raw = p.read_bytes()
o = json.loads(raw)
for n, h in o['base_sha256'].items():
    assert hashlib.sha256((B / n).read_bytes()).hexdigest() == h, 'base changed'
assert len(o['outputs']['项目入口队列.json']) == 1276
assert len(o['outputs']['文件准入队列.json']) == 4609
o['independent_review'] = {'agent_id': '01a1ea08-98c3-7782-9dd4-60a806ef09f7', 'approved_for_metadata_merge': True, 'scope': 'Returned review: exact metadata proposal only; no source revalidation or business acceptance', 'output_sha256': {n: hashlib.sha256((json.dumps(v, ensure_ascii=False, indent=2) + '\n').encode()).hexdigest() for n, v in o['outputs'].items()}}
assert p.read_bytes() == raw
t = p.with_suffix('.review.tmp')
with t.open('x') as f:
    json.dump(o, f, ensure_ascii=False, indent=2)
    f.write('\n')
t.replace(p)
