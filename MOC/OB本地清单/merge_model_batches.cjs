const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const base = __dirname;
const hash = name => crypto.createHash('sha256').update(fs.readFileSync(path.join(base, name))).digest('hex');
const read = name => JSON.parse(fs.readFileSync(path.join(base, name), 'utf8'));
const frozen = read('模型338续批冻结输入.json');
const target = '非RW_模型EA核定.json';
const beforeHash = hash(target);
const data = read(target);
const merged = new Map();
const failures = [];
const shardCounts = {};
for (const group of ['A', 'B', 'C']) {
  const name = `模型续批_${group}.json`;
  const input = read(name);
  const records = Array.isArray(input) ? input : (input.records || input.file_decisions);
  if (!Array.isArray(records)) throw new Error(`${name}: missing records`);
  const expected = new Set(frozen.groups[group].map(x => x.path));
  const seen = new Set();
  shardCounts[group] = {};
  for (const row of records) {
    if (!expected.has(row.path) || seen.has(row.path) || merged.has(row.path)) failures.push(row.path);
    if (!row.status || !row.reason) failures.push(`Incomplete disposition: ${row.path}`);
    if (/待正文|待语义|已读待处置/.test(row.status || '')) failures.push(`Unprocessed: ${row.path}`);
    seen.add(row.path);
    shardCounts[group][row.status] = (shardCounts[group][row.status] || 0) + 1;
    merged.set(row.path, {...row, followup_ledger: name, followup_ledger_hash: hash(name)});
  }
  for (const p of expected) if (!seen.has(p)) failures.push(`Missing: ${p}`);
}
if (merged.size !== 338 || failures.length) throw new Error(JSON.stringify({size: merged.size, failures}));
const report = {checked_utc: new Date().toISOString(), expected: 338, processed: merged.size,
  unprocessed: 0, shard_counts: shardCounts, failures, source_ledger_before_hash: beforeHash,
  frozen_cohort_hash: hash('模型338续批冻结输入.json'),
  input_ledgers: ['A', 'B', 'C'].map(g => ({name: `模型续批_${g}.json`, sha256: hash(`模型续批_${g}.json`)})),
  source_files_read: 0, token_usage: null, check_scope: 'Vault disposition coverage only, not semantic acceptance'};
console.log(JSON.stringify(report, null, 2));
if (process.argv.includes('--apply')) {
  data.file_decisions = data.file_decisions.map(row => {
    const update = merged.get(row.path);
    if (!update) return row;
    const result = {...row, ...update, initial_decision: row.initial_decision || row.decision,
      decision: update.status};
    result.content_read = typeof update.content_read === 'boolean' ? update.content_read
      : (typeof update.read_bytes === 'number' ? update.read_bytes > 0 : null);
    if (typeof update.read_bytes !== 'number') {
      result.read_bytes = null;
      result.read_chars = null;
      result.source_hash = null;
      result.locators = [];
      result.read_metric_note = 'Restricted record minimized; absence of per-file metrics does not mean unread. See batch audit_notes.';
    }
    return result;
  });
  const counts = {};
  for (const row of data.file_decisions) counts[row.status || row.decision] = (counts[row.status || row.decision] || 0) + 1;
  data.initial_counts = data.initial_counts || data.counts;
  data.initial_unresolved = data.initial_unresolved || data.unresolved;
  data.unresolved = data.file_decisions.filter(x => /待核|隔离/.test(x.status || x.decision || ''))
    .map(x => ({path: x.path, reason: x.reason, kind: x.status || x.decision}));
  data.counts = {...data.counts, file_dispositions: counts,
    known_isolated_file_count: data.unresolved.length,
    known_admitted_file_queue_remaining: data.file_decisions.filter(x => x.status === '已准入待正文核定').length,
    business_analyzed_files: data.file_decisions.filter(x => x.status === '已分析' || /^业务片段已分析/.test(x.status || '')).length};
  for (const key of ['raw_read_files', 'raw_read_bytes', 'raw_read_chars']) {
    data.counts[`initial_${key}`] = data.initial_counts[key];
    delete data.counts[key];
  }
  data.followup_read_metrics = ['A', 'B', 'C'].map(g => {
    const x = read(`模型续批_${g}.json`);
    return {group: g, reported_metrics: x.read_metrics || null,
      note: 'Batch-specific metric definitions; do not equate byte acquisition with semantic reading or tokens.'};
  });
  data.file_queue_remaining = data.file_decisions.filter(x => x.status === '已准入待正文核定').map(x => x.path);
  data.followup_completion = report;
  if (hash(target) !== beforeHash) throw new Error('Concurrent modification');
  const temp = path.join(base, `.model-${Date.now()}.tmp`);
  if (fs.lstatSync(path.join(base, target)).isSymbolicLink()) throw new Error('Unsafe target');
  fs.writeFileSync(temp, JSON.stringify(data, null, 2) + '\n', {flag: 'wx'});
  if (hash(target) !== beforeHash) throw new Error('Concurrent modification');
  fs.renameSync(temp, path.join(base, target));
  report.source_ledger_after_hash = hash(target);
  fs.writeFileSync(path.join(base, '模型338覆盖核对.json'), JSON.stringify(report, null, 2) + '\n');
}
