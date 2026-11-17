"""Guarded proposal promotion with a journal; not a cross-file transaction."""
import fcntl
import hashlib
import json
import os
from pathlib import Path
import sys

B = Path(__file__).resolve().parent
NAMES = ['项目入口队列.json', '文件准入队列.json', '扫描覆盖.json']

def digest(data):
    return hashlib.sha256(data).hexdigest()

def validate_rows(old, new):
    before = {r['path']: r for r in old}
    after = {r['path']: r for r in new}
    if len(before) != len(old) or len(after) != len(new):
        raise ValueError('duplicate path')
    if not before.keys() <= after.keys():
        raise ValueError('old paths removed')
    allowed = {'daily_metadata', 'daily_presence'}
    for path, row in before.items():
        if {k: v for k, v in row.items() if k not in allowed} != {k: v for k, v in after[path].items() if k not in allowed}:
            raise ValueError('historical fields changed: ' + path)
    for path in after.keys() - before.keys():
        if after[path].get('content_read_allowed') is not False:
            raise ValueError('new path grants body access')
        if any(k in after[path] for k in ('admission_review', 'reassessment_review', 'manual_decision', 'analysis_status')):
            raise ValueError('new path carries unreviewed adjudication')

def main():
    proposal_path = B / Path(sys.argv[1]).name
    if proposal_path.is_symlink() or proposal_path.parent != B:
        raise ValueError('unsafe proposal')
    proposal = json.loads(proposal_path.read_bytes())
    if proposal.get('independent_review', {}).get('approved_for_metadata_merge') is not True:
        raise ValueError('independent metadata merge review required')
    lock_path = B / '.daily_promotion.lock'
    fd = os.open(lock_path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, 'w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        for previous in B.glob('daily_commit_*.json'):
            if json.loads(previous.read_bytes()).get('status') != 'complete':
                raise RuntimeError('incomplete journal requires reconciliation: ' + previous.name)
        original = {}
        for name in NAMES:
            if (B / name).is_symlink():
                raise ValueError('unsafe destination')
            original[name] = (B / name).read_bytes()
            if digest(original[name]) != proposal['base_sha256'][name]:
                raise RuntimeError('base changed; do not overwrite: ' + name)
        for name in NAMES[:2]:
            validate_rows(json.loads(original[name]), proposal['outputs'][name])
        staged = {n: (json.dumps(proposal['outputs'][n], ensure_ascii=False, indent=2) + '\n').encode() for n in NAMES}
        if {n: digest(b) for n, b in staged.items()} != proposal['independent_review'].get('output_sha256'):
            raise ValueError('reviewed output hashes do not match')
        old_coverage = json.loads(original[NAMES[2]])
        new_coverage = proposal['outputs'][NAMES[2]]
        if any(new_coverage.get(k) != v for k, v in old_coverage.items() if k not in {'daily_increment', 'daily_increment_history'}):
            raise ValueError('historical coverage modified')
        expected_history = old_coverage.get('daily_increment_history', []) + ([old_coverage['daily_increment']] if 'daily_increment' in old_coverage else [])
        if new_coverage.get('daily_increment_history') != expected_history:
            raise ValueError('daily history mismatch')
        journal_path = B / ('daily_commit_' + proposal_path.stem + '.json')
        journal = {'status': 'prepared', 'proposal': proposal_path.name, 'applied': [], 'base_sha256': proposal['base_sha256'], 'output_sha256': {n: digest(b) for n, b in staged.items()}, 'originals': {n: b.decode() for n, b in original.items()}, 'limitation': 'advisory lock only; no cross-file atomicity; non-cooperating writers must be quiescent'}
        def persist():
            tmp = journal_path.with_suffix('.tmp')
            with tmp.open('x') as f:
                json.dump(journal, f, ensure_ascii=False, indent=2)
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp, journal_path)
        persist()
        for name in NAMES:
            for other in NAMES:
                expected = staged[other] if other in journal['applied'] else original[other]
                if (B / other).read_bytes() != expected:
                    raise RuntimeError('concurrent update; journal retained for manual reconciliation')
            tmp = B / (name + '.promote.tmp')
            with tmp.open('xb') as f:
                f.write(staged[name])
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp, B / name)
            journal['applied'].append(name)
            journal['status'] = 'partial'
            persist()
        if any((B / n).read_bytes() != staged[n] for n in NAMES):
            raise RuntimeError('postcommit mismatch; journal retained')
        journal['status'] = 'complete'
        persist()
        print(json.dumps({'status': 'complete', 'journal': journal_path.name, 'rows': {n: len(proposal['outputs'][n]) for n in NAMES[:2]}}, ensure_ascii=False))

if __name__ == '__main__':
    main()
