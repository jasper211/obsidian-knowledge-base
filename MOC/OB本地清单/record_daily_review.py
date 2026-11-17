"""Record the explicitly returned independent review for this exact proposal."""
import hashlib
import json
from pathlib import Path

B = Path(__file__).resolve().parent
p = B / 'daily_proposal_20261116T135809355059.json'
raw = p.read_bytes()
obj = json.loads(raw)
for n, expected in obj['base_sha256'].items():
    assert hashlib.sha256((B / n).read_bytes()).hexdigest() == expected, 'base changed'
assert len(obj['outputs']['项目入口队列.json']) == 1275
assert len(obj['outputs']['文件准入队列.json']) == 4609
obj['independent_review'] = {'agent_id': '01a1deb2-0e65-73e3-b5b1-efb774497155', 'approved_for_metadata_merge': True, 'scope': 'This exact metadata output only; not body access or local acceptance', 'conditions': 'base hashes must match; non-cooperating writers must be quiescent; journaled non-atomic promotion', 'output_sha256': {n: hashlib.sha256((json.dumps(o, ensure_ascii=False, indent=2) + '\n').encode()).hexdigest() for n, o in obj['outputs'].items()}}
assert p.read_bytes() == raw
temp = p.with_suffix('.review.tmp')
with temp.open('x') as f:
    json.dump(obj, f, ensure_ascii=False, indent=2)
    f.write('\n')
temp.replace(p)
print('Recorded returned independent review; output content unchanged')
