"""Bind returned metadata-only review to its exact proposal."""
import hashlib
import json
from pathlib import Path
B = Path(__file__).resolve().parent
p = B / 'daily_proposal_20261123T194718038322.json'
raw = p.read_bytes()
assert hashlib.sha256(raw).hexdigest() == '7c3135a7d791e282a4d4b542baf7d8b69fcb6410c3f4d0c15a3c550bd96689d8'
o = json.loads(raw)
for n, h in o['base_sha256'].items():
    assert hashlib.sha256((B / n).read_bytes()).hexdigest() == h
o['independent_review'] = {'agent_id': '01a20b3c-eb16-74c2-a9b9-8ba3d45741c0', 'approved_for_metadata_merge': True, 'scope': 'Returned metadata-only approval; no source verification or business admission', 'output_sha256': {n: hashlib.sha256((json.dumps(v, ensure_ascii=False, indent=2) + '\n').encode()).hexdigest() for n, v in o['outputs'].items()}}
assert p.read_bytes() == raw
t = p.with_suffix('.review.tmp')
with t.open('x') as f:
    json.dump(o, f, ensure_ascii=False, indent=2)
    f.write('\n')
t.replace(p)
