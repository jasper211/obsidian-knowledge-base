"""Bind returned metadata-only review to its exact proposal."""
import hashlib
import json
from pathlib import Path
B = Path(__file__).resolve().parent
p = B / 'daily_proposal_20261125T200303805726.json'
raw = p.read_bytes()
assert hashlib.sha256(raw).hexdigest() == 'aa674fd4df88d8e225bab829499f1c0053783242dc1ce1abd04c34b17e7cae89'
o = json.loads(raw)
for n, h in o['base_sha256'].items():
    assert hashlib.sha256((B / n).read_bytes()).hexdigest() == h
o['independent_review'] = {'agent_id': '01a21597-e725-7650-9d14-b01d66589089', 'approved_for_metadata_merge': True, 'scope': 'Returned metadata-only approval; no source verification or business admission', 'output_sha256': {n: hashlib.sha256((json.dumps(v, ensure_ascii=False, indent=2) + '\n').encode()).hexdigest() for n, v in o['outputs'].items()}}
assert p.read_bytes() == raw
t = p.with_suffix('.review.tmp')
with t.open('x') as f:
    json.dump(o, f, ensure_ascii=False, indent=2)
    f.write('\n')
t.replace(p)
