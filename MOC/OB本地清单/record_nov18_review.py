"""Bind returned independent metadata review to the exact reviewed proposal."""
import hashlib
import json
from pathlib import Path

B = Path(__file__).resolve().parent
p = B / 'daily_proposal_20261118T090200107045.json'
raw = p.read_bytes()
assert hashlib.sha256(raw).hexdigest() == '20793f270a8cc3f5f2d525365d5024a620857ca8776c7f3f36954b902351b985'
o = json.loads(raw)
for n, h in o['base_sha256'].items():
    assert hashlib.sha256((B / n).read_bytes()).hexdigest() == h, 'base changed'
o['independent_review'] = {
    'agent_id': '01a1ea08-98c3-7782-9dd4-60a806ef09f7',
    'approved_for_metadata_merge': True,
    'scope': 'Returned approval for exact proposal metadata only; no source verification, body access or business acceptance',
    'output_sha256': {n: hashlib.sha256((json.dumps(v, ensure_ascii=False, indent=2) + '\n').encode()).hexdigest() for n, v in o['outputs'].items()},
}
assert p.read_bytes() == raw
t = p.with_suffix('.review.tmp')
with t.open('x') as f:
    json.dump(o, f, ensure_ascii=False, indent=2)
    f.write('\n')
t.replace(p)
