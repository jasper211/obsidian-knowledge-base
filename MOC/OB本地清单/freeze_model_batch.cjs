const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const p = path.join(__dirname, '非RW_模型EA核定.json');
const bytes = fs.readFileSync(p);
const data = JSON.parse(bytes);
const rows = data.file_decisions.filter(x => x.status === '已准入待正文核定');
if (rows.length !== 338) throw new Error('Model cohort changed');
const grouped = {A: [], B: [], C: []};
for (const row of rows) {
  const s = row.path.split('/业务模型/')[1];
  if (!s) throw new Error('Unexpected root');
  const group = /^(00_总控|10_标准与基线)\//.test(s) ? 'B'
    : /^20_工作包\/D09P(02|03|04|05|08|09|10)_/.test(s) ? 'A' : 'C';
  grouped[group].push(row);
}
if (grouped.A.length !== 79 || grouped.B.length !== 107 || grouped.C.length !== 152) {
  throw new Error('Unexpected cohort partitions');
}
const out = {created_utc: new Date().toISOString(), source_ledger: p,
  source_ledger_hash: crypto.createHash('sha256').update(bytes).digest('hex'),
  project_state: data.project_state, window: data.window,
  counts: {A: 79, B: 107, C: 152, total: 338}, groups: grouped,
  note: 'Metadata ledger only. Type recheck required before any eligible source body read.'};
fs.writeFileSync(path.join(__dirname, '模型338续批冻结输入.json'), JSON.stringify(out, null, 2) + '\n', {flag: 'wx'});
console.log(JSON.stringify(out.counts));
