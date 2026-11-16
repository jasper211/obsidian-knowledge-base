"""Bounded metadata refresh; source bodies are never opened."""
import calendar
import datetime as dt
import json
import hashlib
import os
import stat
from pathlib import Path
from zoneinfo import ZoneInfo

OUT = Path(__file__).resolve().parent
NOW = dt.datetime.now(ZoneInfo('America/Chicago'))
month = NOW.month - 6
year = NOW.year
if month < 1:
    month += 12
    year -= 1
LOW = NOW.replace(year=year, month=month, day=min(NOW.day, calendar.monthrange(year, month)[1]))
names = ['项目入口队列.json', '文件准入队列.json', '扫描覆盖.json']
original = {n: (OUT / n).read_bytes() for n in names}
projects, files = [json.loads(original[n]) for n in names[:2]]
pm, fm = [{r['path']: r for r in rows} for rows in (projects, files)]

def decision(r):
    reviewed = r.get('reassessment_review', {}).get('new_status') or r.get('admission_review', {}).get('decision')
    if reviewed:
        return reviewed
    reconciled = r.get('daily_admission_reconciliation', {}).get('status', '')
    if any(t in reconciled for t in ('隔离', '排除')):
        return reconciled
    return r.get('decision', '')

def hard_boundary(r):
    return any(t in decision(r) for t in ('隔离', '排除', '待决'))

def compare_metadata(previous, current):
    if previous.get('kind') and previous['kind'] != current['kind']:
        return 'kind_changed'
    old_ns = previous.get('mtime_ns')
    if old_ns is None or previous.get('size') is None:
        return 'incomplete_metadata_baseline'
    try:
        delta = abs(int(old_ns) - int(current['mtime_ns']))
    except (TypeError, ValueError, OverflowError):
        return 'invalid_metadata_baseline'
    if isinstance(old_ns, (int, float)) and 0 < delta <= 1024 and previous['size'] == current['size']:
        return 'legacy_timestamp_precision_uncertain'
    return 'metadata_changed' if delta or previous['size'] != current['size'] else 'metadata_unchanged'

approved = {'保留筛类型', '限定准入', '业务分支准入', '限定业务分支准入', '在用业务项目准入'}
containers = {'范围容器仅定位', '容器拆分', '容器分组核定', '容器分组核定（子项未知保留）'}
roots = {'/Users/a112233/Desktop', '/Users/a112233/Desktop/Rw权益项目', '/Users/a112233/Desktop/Jasper工作文档（不含EA项目）', '/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/项目工作区', '/Users/a112233/Desktop/流程架构项目_jasper'}
targets = roots | {p for p, r in pm.items() if decision(r) in approved | containers}
failures, signals, scanned, skipped = [], [], [], []
observations = 0

def open_dir(path):
    fd = os.open('/', os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in Path(path).parts[1:]:
            nxt = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            if os.fstat(nxt).st_dev != os.fstat(fd).st_dev:
                os.close(nxt)
                raise OSError('mount boundary rejected')
            os.close(fd)
            fd = nxt
        return fd
    except Exception:
        os.close(fd)
        raise

def excluded(path):
    parts = Path(path).parts
    return any(x.startswith('.') or x.lower() in {'node_modules', 'venv', '__pycache__', 'scratch', 'tmp', 'ob', 'eg'} or any(t in x.lower() for t in ['p&l', 'eg-', 'fixture', 'ob知识库', '工程', '测试']) for x in parts[4:])

for path in sorted(targets):
    if excluded(path):
        skipped.append({'path': path, 'reason': 'excluded path component'})
        continue
    # Explicit child approval may exist beneath a container, but never beneath isolation.
    blocked = [str(p) for p in [Path(path), *Path(path).parents] for mapping in (pm, fm) if str(p) in mapping and (hard_boundary(mapping[str(p)]) or (str(p) not in roots and '待核' in decision(mapping[str(p)])))]
    if blocked:
        skipped.append({'path': path, 'reason': 'ancestor boundary', 'ancestors': blocked})
        continue
    try:
        fd = open_dir(path)
    except OSError as e:
        failures.append({'path': path, 'error': str(e)})
        continue
    try:
        try:
            children = sorted(os.listdir(fd))
        except OSError as e:
            failures.append({'path': path, 'error': str(e), 'stage': 'listdir'})
            continue
        scanned.append(path)
        present = {str(Path(path) / name) for name in children}
        for known in sorted((set(pm) | set(fm)) - present):
            if str(Path(known).parent) == path:
                missing = {'checked': NOW.isoformat(), 'signal': 'not_observed_in_direct_listing', 'source_body_read': False, 'meaning': 'not proof of deletion; prior admission retained as historical only'}
                for mapping in (pm, fm):
                    if known in mapping:
                        mapping[known]['daily_presence'] = missing
                signals.append({'path': known, **missing})
        for name in children:
            p = str(Path(path) / name)
            try:
                s = os.stat(name, dir_fd=fd, follow_symlinks=False)
            except OSError as e:
                failures.append({'path': p, 'error': str(e)})
                continue
            observations += 1
            kind = 'link' if stat.S_ISLNK(s.st_mode) else 'directory' if stat.S_ISDIR(s.st_mode) else 'file'
            obs = {'checked': NOW.isoformat(), 'kind': kind, 'size': s.st_size, 'mtime_ns': str(s.st_mtime_ns), 'mtime': dt.datetime.fromtimestamp(s.st_mtime, NOW.tzinfo).isoformat(), 'source_body_read': False}
            existing = fm.get(p) or pm.get(p)
            if existing:
                previous = next((existing[k] for k in ('daily_metadata', 'stat_after', 'stat_before', 'stat_inventory', 'stat') if isinstance(existing.get(k), dict) and existing[k].get('mtime_ns') is not None and existing[k].get('size') is not None), existing)
                previous = dict(previous)
                prior_kind = existing.get('daily_metadata', {}).get('kind') or existing.get('kind')
                if prior_kind in {'file', 'directory', 'link'}:
                    previous['kind'] = prior_kind
                obs['signal'] = compare_metadata(previous, obs)
                for mapping in (pm, fm):
                    if p in mapping:
                        mapping[p]['daily_metadata'] = obs
                        mapping[p]['daily_presence'] = {'checked': NOW.isoformat(), 'signal': 'observed'}
                if obs['signal'] != 'metadata_unchanged' and not excluded(p):
                    signals.append({'path': p, 'signal': obs['signal'], 'admission': 'requires type/window recheck; not body authorization'})
                continue
            blocked_type = excluded(p) or kind == 'link'
            admitted_parent = decision(pm.get(path, {})) in approved
            ext = Path(p).suffix.lower()
            d = '排除' if blocked_type else '待核不递归'
            if kind == 'file' and admitted_parent and not blocked_type:
                d = '待核内容类型' if ext in {'.md', '.html', '.htm'} else '仅引用' if ext in {'.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'} else '排除分析类型'
                if d == '待核内容类型' and not LOW.timestamp() <= s.st_mtime <= NOW.timestamp():
                    d = '不读正文:增量窗口外'
            row = {'path': p, 'decision': d, 'reason': '每日直接子项元数据发现；新项目不自动准入', 'discovered': NOW.isoformat(), 'checked': NOW.isoformat(), 'content_read_allowed': False, 'review_status': '待独立核查', 'daily_metadata': obs, 'window': {'start': LOW.isoformat(), 'end': NOW.isoformat()}}
            if kind == 'file' and admitted_parent:
                files.append(row)
                fm[p] = row
            else:
                projects.append(row)
                pm[p] = row
            signals.append({'path': p, 'signal': 'new_inventory_entry', 'decision': d})
    finally:
        os.close(fd)

summary = {'checked': NOW.isoformat(), 'timezone': 'America/Chicago', 'window': {'start': LOW.isoformat(), 'end': NOW.isoformat()}, 'scope': 'Existing explicitly admitted directories and scope containers, direct children only; new directories not traversed; no source bodies', 'directories_checked': len(scanned), 'scanned_directories': scanned, 'metadata_observations': observations, 'skipped_boundaries': skipped, 'failures': failures, 'signals': signals, 'project_rows': len(projects), 'file_rows': len(files), 'source_body_bytes': 0, 'actual_tokens': None, 'unknown_subtree_file_count': None, 'local_acceptance': False, 'review_status': 'pending independent review', 'remaining': 'Skipped boundaries, failed paths and newly discovered scopes remain separate; this is not whole-local acceptance'}
coverage = json.loads(original[names[2]])
if 'daily_increment' in coverage:
    coverage.setdefault('daily_increment_history', []).append(coverage['daily_increment'])
coverage['daily_increment'] = summary
if any((OUT / n).read_bytes() != original[n] for n in names):
    raise RuntimeError('Concurrent governance update; no output committed')
# Publish one complete proposal instead of partially replacing live queues.
# Promotion must revalidate base hashes and preserve newer review-layer changes.
proposal = {'status': 'pending_review_not_applied', 'checked': NOW.isoformat(), 'base_sha256': {n: hashlib.sha256(original[n]).hexdigest() for n in names}, 'outputs': dict(zip(names, (projects, files, coverage)))}
target = OUT / ('daily_proposal_' + NOW.strftime('%Y%m%dT%H%M%S%f') + '.json')
with target.with_suffix('.tmp').open('x') as f:
    json.dump(proposal, f, ensure_ascii=False, indent=2)
    f.write('\n')
os.replace(target.with_suffix('.tmp'), target)
print('STAGED ONLY; canonical queues unchanged:', target.name)
print(json.dumps({k: v for k, v in summary.items() if k not in {'scanned_directories', 'signals', 'skipped_boundaries'}}, ensure_ascii=False))
print('signals', len(signals), 'skipped', len(skipped))
