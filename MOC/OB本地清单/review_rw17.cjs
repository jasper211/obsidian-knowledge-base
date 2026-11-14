const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const root = __dirname;
const names = ['分片0_处置.json','分片1_处置.json','分片2_处置.json','分片3_处置.json','治理0_处置.json','治理1_处置.json','治理2_处置.json'];
const records = [];
for (const name of names) {
  const bytes = fs.readFileSync(path.join(root,name));
  const rows = JSON.parse(bytes);
  for (const row of rows.filter(x=>x.status==='待核')) {
    let status='历史争议仅溯源', reason='现有片段已记录冲突；保留历史来源与异议，不采作现行规则，不代替实体、财务、法律或审批裁定。无需为本轮历史保留重读来源。', human=false, question=null;
    if (path.basename(row.path).startsWith('190A_') || path.basename(row.path).startsWith('22_REVIEW')) {
      status='技术审计排除'; reason='既有片段明确为依赖构建/文件抽取技术审计；按工程技术不摄入规则终结本轮知识处理，不据其自报判断业务验收。';
    } else if (path.basename(row.path).includes('字段映射图-V5')) {
      status='类型及敏感边界待核'; reason='旧依据只含标题风险且未读正文，不能宣称技术语义已确认；交RW23类型核查旁路复核，潜在个人字段不为清零展开。';
    } else if (path.basename(row.path).includes('金融垂直领域AI原生公司')) {
      status='跨项目准入待裁决'; human=true;
      reason='已有片段明确跨企业/EA/经验引擎及组织安排，RW存放位置不证明业务归属；当前已准入项目不能覆盖此综合项目。';
      question='这两份AI原生公司复盘纪要所对应的跨企业组织项目是否属于仍在推进、应纳入OB的独立业务项目？如是，请指定项目名称和业务内容边界；未明确前不展开技术、人员或股权材料。';
    }
    records.push({path:row.path,old_status:row.status,new_status:status,reason,prior_reason:row.reason,
      evidence_locator:{ledger:name,source_locators:row.locators,ledger_sha256:crypto.createHash('sha256').update(bytes).digest('hex')},
      requires_user:human,question,analysis_needed:false,new_source_reads:0,
      unresolved_truth:status==='历史争议仅溯源',current_use_allowed:false,
      original_record_sha256:crypto.createHash('sha256').update(JSON.stringify(row)).digest('hex')});
  }
}
if(records.length!==17 || new Set(records.map(x=>x.path)).size!==17)throw Error('RW17 coverage mismatch');
const counts={};for(const r of records)counts[r.new_status]=(counts[r.new_status]||0)+1;
fs.writeFileSync(path.join(root,'RW17再核定.json'),JSON.stringify({checked_at:new Date().toISOString(),timezone:'America/Chicago',scope:'既有vault证据再核定，未核验当前源',records,counts,source_reads:0,token_usage:null,unprocessed:0,review_status:'待独立核查'},null,2)+'\n');
console.log(counts);
