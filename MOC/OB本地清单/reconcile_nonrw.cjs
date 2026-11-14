const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const base = __dirname;
const read = name => JSON.parse(fs.readFileSync(path.join(base, name), 'utf8'));
const digest = name => crypto.createHash('sha256').update(fs.readFileSync(path.join(base, name))).digest('hex');
const names = ['非RW_Jasper核定.json', '非RW_模型EA核定.json', '非RW_其他核定.json'];
const sourceName = '项目入口队列.json';
const sourceHash = digest(sourceName);
const projects = read(sourceName);
const baselineName = '20261112T201040873141_项目入口队列.json';
const expected = read(baselineName).filter(x => !x.path.startsWith('/Users/a112233/Desktop/Rw权益项目'));
const entries = names.flatMap(name => {
  const data = read(name);
  if (!Array.isArray(data.entry_decisions)) throw new Error(`${name}: missing entry_decisions`);
  return data.entry_decisions.concat(data.new_entry_decisions || data.new_entries || data.new_subprojects || [])
    .map(row => ({...row, ledger: name, ledger_hash: digest(name)}));
});
const index = new Map();
const duplicates = [];
for (const row of entries) {
  if (!row.path || !row.decision || !row.reason) throw new Error('Incomplete entry adjudication');
  if (index.has(row.path)) duplicates.push(row.path);
  index.set(row.path, row);
}
const missing = expected.filter(row => !index.has(row.path)).map(row => row.path);
const expectedPaths = new Set(expected.map(row => row.path));
const extra = entries.filter(row => !expectedPaths.has(row.path)).map(row => row.path);
const counts = {};
for (const row of entries) counts[row.decision] = (counts[row.decision] || 0) + 1;
const report = {
  checked_utc: new Date().toISOString(), timezone: 'America/Chicago',
  original_entry_count: expected.length, adjudication_entry_count: entries.length,
  matched_original_entries: expected.length - missing.length,
  missing, duplicates, additional_entries: extra, decision_counts: counts,
  complete_original_entry_mapping: missing.length === 0 && duplicates.length === 0,
  source_queue_hash_before: sourceHash,
  input_ledgers: names.map(name => ({name, sha256: digest(name)})),
  note: 'Entry mapping is not complete local file coverage or current business acceptance.',
};
console.log(JSON.stringify({...report, additional_entries: extra.length}, null, 2));
if (process.argv.includes('--apply')) {
  if (!report.complete_original_entry_mapping) throw new Error('Incomplete mapping; not applied');
  if (digest(sourceName) !== sourceHash) throw new Error('Concurrent queue modification');
  // Preserve original scan fields; adjudication is a separate dated evidence layer.
  for (const row of projects) {
    const adjudication = index.get(row.path);
    if (!adjudication) continue;
    if (row.admission_review && JSON.stringify(row.admission_review) !== JSON.stringify(adjudication)) {
      row.admission_history = [...(row.admission_history || []), row.admission_review];
    }
    row.admission_review = adjudication;
    row.manual_decision = adjudication.decision;
  }
  const currentPaths = new Set(projects.map(row => row.path));
  for (const p of extra.filter(p => !currentPaths.has(p))) {
    const adjudication = index.get(p);
    projects.push({path: p, decision: '待核', reason: 'New entry; dated adjudication in admission_review',
      checked: report.checked_utc, discovered: report.checked_utc, content_read_allowed: false,
      review_status: '待独立核查', manual_decision: adjudication.decision, admission_review: adjudication});
  }
  const temp = path.join(base, `.nonrw-${Date.now()}.tmp`);
  if (fs.lstatSync(path.join(base, sourceName)).isSymbolicLink()) throw new Error('Unsafe target');
  fs.writeFileSync(temp, JSON.stringify(projects, null, 2) + '\n', {flag: 'wx'});
  if (digest(sourceName) !== sourceHash) throw new Error('Concurrent queue modification');
  fs.renameSync(temp, path.join(base, sourceName));
  report.source_queue_hash_after = digest(sourceName);
  fs.writeFileSync(path.join(base, '非RW覆盖汇总.json'), JSON.stringify(report, null, 2) + '\n');
}
