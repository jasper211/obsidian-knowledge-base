"""Merge vault ledgers only. No source-path stat, content read or traversal."""
import copy
import fcntl
import hashlib
import json
import os
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QUEUE = ROOT / '文件准入队列.json'
REPORT = ROOT / '文件队列整合核对.json'
SPECS = [('非RW_模型EA核定.json', 'file_decisions', 2784, 'first_window'),
         ('非RW_Jasper核定.json', 'file_decisions', 943, 'first_window'),
         ('Jasper16增量核定.json', 'records', 16, 'incremental')]
ANALYZED = {'已分析', '业务片段已分析_候选'}

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def read_local(path):
    if path.parent != ROOT or path.is_symlink():
        raise RuntimeError(f'Unsafe ledger path: {path}')
    return path.read_bytes()

def rows_check(rows, label):
    if not isinstance(rows, list):
        raise TypeError(f'{label}: expected array')
    seen = set()
    for r in rows:
        if not isinstance(r, dict) or not isinstance(r.get('path'), str):
            raise TypeError(f'{label}: non-object or missing string path')
        if not r['path'].startswith('/') or r['path'] in seen:
            raise ValueError(f'{label}: nonabsolute/duplicate path: {r["path"]}')
        seen.add(r['path'])

def status(r):
    return r.get('status', r.get('review_status', r.get('decision', '未声明')))

def stringify_ns(obj):
    # Only imported review snapshots change representation; old queue stays exact.
    if isinstance(obj, dict):
        return {k: str(v) if k.endswith('_ns') and v is not None else stringify_ns(v)
                for k, v in obj.items()}
    if isinstance(obj, list):
        return [stringify_ns(v) for v in obj]
    return obj

def encode(obj):
    return (json.dumps(obj, ensure_ascii=False, indent=2) + '\n').encode()

def atomic_replace(path, raw):
    fd, tmp = tempfile.mkstemp(prefix='.admission-merge-', dir=ROOT)
    try:
        with os.fdopen(fd, 'wb') as f:
            f.write(raw)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)

def main():
    started = datetime.now(timezone.utc).isoformat()
    raw_queue = read_local(QUEUE)
    queue = json.loads(raw_queue)
    rows_check(queue, QUEUE.name)
    original = copy.deepcopy(queue)
    by_path = {r['path']: r for r in queue}
    originals = set(by_path)
    raw_inputs = {QUEUE: raw_queue}
    report_before = read_local(REPORT) if REPORT.exists() else None
    inputs = []
    excluded = []
    touched = set()
    appended = set()
    skipped = 0
    layer_counts = Counter()
    input_counts = {}
    for name, field, expected, layer in SPECS:
        p = ROOT / name
        raw = read_local(p)
        source_digest = digest(raw)
        raw_inputs[p] = raw
        doc = json.loads(raw)
        if not isinstance(doc, dict):
            raise TypeError(f'{name}: expected object')
        records = doc.get(field)
        rows_check(records, name + '.' + field)
        if len(records) != expected:
            raise ValueError(f'{name}: expected {expected}, got {len(records)}; inspect before updating')
        input_counts[name] = {'field': field, 'records': len(records),
                              'statuses': dict(Counter(status(r) for r in records))}
        inputs.append({'file': str(p), 'sha256': source_digest, 'field': field})
        for r in records:
            kind = r.get('kind')
            if kind not in (None, 'file') or r.get('type') in ('other', 'directory', 'dir'):
                excluded.append({'source': name, 'path': r['path'], 'kind': kind,
                                 'type': r.get('type'), 'reason': '非文件记录不入文件队列'})
                continue
            path = r['path']
            if layer == 'incremental' and path not in by_path:
                raise ValueError(f'Increment lacks first-window record: {path}')
            if path not in by_path:
                # No invented root status: preserve imported first-window fields.
                item = copy.deepcopy(r)
                if 'admission_review' in item:
                    raise ValueError('Source owns reserved admission_review field')
                queue.append(item)
                by_path[path] = item
                appended.add(path)
            item = by_path[path]
            if 'admission_review' not in item:
                item['admission_review'] = {'schema_version': 'dated-admission-review-v1', 'history': []}
            review = item['admission_review']
            if not isinstance(review, dict) or review.get('schema_version') != 'dated-admission-review-v1' or not isinstance(review.get('history'), list):
                raise ValueError(f'Existing admission_review schema conflict; preserve and stop: {path}')
            identity = {'source_file': name, 'source_sha256': source_digest, 'source_array': field, 'layer': layer}
            if any(all(h.get(k) == v for k, v in identity.items()) for h in review['history']):
                skipped += 1
                continue
            snapshot = stringify_ns(copy.deepcopy(r))
            # Preserve missing/null/false/true and every read metric independently.
            # Isolation status never implies that a source was unread.
            for key in ('content_read', 'read_bytes', 'read_chars', 'read_events', 'read_purpose'):
                if key in r:
                    assert snapshot[key] == stringify_ns(r[key])
                else:
                    assert key not in snapshot
            review['history'].append({**identity, 'reviewed_at': started, 'record': snapshot})
            review['latest_review_index'] = len(review['history']) - 1
            review['updated_at'] = started
            touched.add(path)
            layer_counts[layer] += 1
    # Old fields and RW records are retained, not reclassified by this merge.
    for old in original:
        now = by_path[old['path']]
        for k, v in old.items():
            if k != 'admission_review' and now[k] != v:
                raise AssertionError(f'Old field changed: {old["path"]} {k}')
        if old['path'] not in touched:
            assert old == now
        elif 'admission_review' in old:
            hist = old['admission_review']['history']
            assert now['admission_review']['history'][:len(hist)] == hist
    rows_check(queue, 'output')
    effective = []
    analyzed = []
    for item in queue:
        rev = item.get('admission_review')
        record = rev['history'][rev['latest_review_index']]['record'] if rev else item
        s = status(record)
        effective.append(s)
        if s in ANALYZED:
            analyzed.append({'path': item['path'], 'status': s,
                             'locators': record.get('locators', []),
                             'source_file': rev['history'][rev['latest_review_index']]['source_file'] if rev else QUEUE.name,
                             'admission_review_index': rev['latest_review_index'] if rev else None,
                             'read_chars': record.get('read_chars'), 'read_bytes': record.get('read_bytes')})
    output = encode(queue)
    report = {'schema_version': 'file-admission-merge-audit-v1', 'checked_at': started,
              'scope': '仅vault JSON记录整合，无源正文或源路径stat，无目录展开',
              'input_queue_sha256': digest(raw_queue), 'inputs': inputs,
              'output_queue_sha256': digest(output), 'input_counts': input_counts,
              'counts': {'before_records': len(original), 'before_unique_paths': len(originals),
                         'after_records': len(queue), 'after_unique_paths': len(by_path),
                         'appended_paths': len(appended), 'updated_existing_paths': len(touched & originals),
                         'unchanged_existing_paths': len(originals - touched),
                         'paths_reviewed': len(touched), 'review_layers_appended': sum(layer_counts.values()),
                         'layers_by_window': dict(layer_counts), 'already_present_layers': skipped,
                         'excluded_nonfile_records': len(excluded), 'analyzed_records': len(analyzed)},
              'statuses_latest_review_else_original': dict(Counter(effective)),
              'statuses_original_top_level_after_merge': dict(Counter(status(r) for r in queue)),
              'analyzed_status_definition': sorted(ANALYZED), 'analyzed_records': analyzed,
              'excluded_nonfile_records': excluded,
              'preservation': {'old_nonreview_fields_equal': True, 'old_unreviewed_records_equal': True,
                               'first_window_layers_retained': True, 'source_ledgers_unchanged': True},
              'concurrency': {'strategy': 'queue advisory exclusive lock + all-input SHA256 recheck immediately before atomic replacement',
                              'limitation': '非协作写入者在最后检查与rename之间的竞争不能由普通文件系统CAS完全消除；检测到变化则停止，不自动覆盖'},
              'notes': ['新复核放admission_review.history；latest_review_index选择最新层，不重写既有decision/status。',
                        '首窗和增量独立保存；后期增量不是重新纳入首窗。',
                        '导入复核快照的ns转字符串只保留已有数值，不恢复历史number可能损失的精度。',
                        '读取状态缺字段/null/false/true分别原样保留；已读后隔离不改作未读，不从隔离状态推断读取标志。',
                        '未从entry_decisions/new_entries/其他核定目录入口导入记录。',
                        '统计为账本自述，不是源文复读、独立核查或验收通过。']}
    with QUEUE.open('rb') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        for p, raw in raw_inputs.items():
            if digest(read_local(p)) != digest(raw):
                raise RuntimeError(f'Concurrent modification, abort: {p.name}')
        current_report = read_local(REPORT) if REPORT.exists() else None
        if current_report != report_before:
            raise RuntimeError('Concurrent report modification, abort')
        report['concurrency']['prewrite_all_hashes_match'] = True
        atomic_replace(QUEUE, output)
        if read_local(QUEUE) != output:
            raise RuntimeError('Queue postwrite changed; do not claim successful merge')
        report['concurrency']['postwrite_queue_hash_match'] = True
        report['concurrency']['postwrite_input_hashes_match'] = all(
            read_local(p) == raw for p, raw in raw_inputs.items() if p != QUEUE)
        atomic_replace(REPORT, encode(report))
    print(json.dumps(report['counts'], ensure_ascii=False))
    print(json.dumps(report['statuses_latest_review_else_original'], ensure_ascii=False))

if __name__ == '__main__':
    main()
