const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const base = __dirname;
const hash = value => crypto.createHash('sha256').update(value).digest('hex');
const read = name => JSON.parse(fs.readFileSync(path.join(base, name), 'utf8'));
const files = [0, 1, 2, 3].map(i => `分片${i}_处置.json`)
  .concat([0, 1, 2].map(i => `治理${i}_处置.json`));
const pending = files.flatMap(name => read(name)
  .filter(row => row.status === '待核')
  .map(row => ({path: row.path, status: row.status, reason: row.reason,
    ledger: name, record_hash: hash(JSON.stringify(row))})));
const result = {
  checked_utc: new Date().toISOString(),
  timezone: 'America/Chicago',
  purpose: 'Existing RW unresolved records only; no source access or promotion.',
  count: pending.length,
  pending,
  token_usage: null,
  proxy: {vault_ledgers_read: files.length, source_files_read: 0},
};
const target = path.join(base, '17项RW待核保留核对.json');
if (fs.existsSync(target)) {
  const old = JSON.parse(fs.readFileSync(target, 'utf8'));
  const before = old.pending.map(x => `${x.path}\t${x.record_hash}`).sort();
  const after = pending.map(x => `${x.path}\t${x.record_hash}`).sort();
  if (JSON.stringify(before) !== JSON.stringify(after)) {
    throw new Error('RW pending records changed; investigate without overwriting baseline');
  }
  console.log(JSON.stringify({pending_count: pending.length, unchanged: true}));
} else {
  if (pending.length !== 17) throw new Error('Unexpected pending count');
  fs.writeFileSync(target, JSON.stringify(result, null, 2) + '\n');
  console.log(JSON.stringify({pending_count: pending.length, baseline_created: true}));
}
