const fs=require('fs'), path=require('path'), crypto=require('crypto');
const dir=__dirname;
const load=n=>JSON.parse(fs.readFileSync(path.join(dir,n),'utf8'));
const hash=n=>crypto.createHash('sha256').update(fs.readFileSync(path.join(dir,n))).digest('hex');
const names=['RW17再核定.json','RW23再核定.json','模型98再核定.json','Jasper待核再核定.json','其他60再核定.json'];
const counts={}, all=[], extras=[],groupDecisions=[];
for(const name of names){
  const d=load(name), records=d.records;
  if(!Array.isArray(records))throw Error(name+' records missing');
  const seen=new Set();
  for(const r of records){
    if(!r.path||!r.new_status||!r.reason||seen.has(r.path))throw Error(name+' invalid/duplicate record');
    seen.add(r.path); all.push({...r,ledger:name,ledger_hash:hash(name)});
  }
  counts[name]={records:records.length,statuses:{},requires_user:records.filter(x=>x.requires_user===true).length};
  for(const r of records)counts[name].statuses[r.new_status]=(counts[name].statuses[r.new_status]||0)+1;
  for(const key of ['additional_records','scope_decisions','entry_decisions']){
    if(Array.isArray(d[key]))for(const r of d[key]){
      const target=r.path?extras:groupDecisions;
      if(!r.path&&!Array.isArray(r.record_ids))throw Error('Unmapped grouped decision');
      target.push({...r,ledger:name,ledger_hash:hash(name),record_kind:key});
    }
  }
}
const user=all.filter(x=>x.requires_user===true);
const effective=new Map(),overlaps=[];
for(const r of [...all,...extras]){
  if(!r.path||!r.new_status||!r.reason)throw Error('Incomplete review');
  const prior=effective.get(r.path);
  if(prior){
    const isHandoff=prior.ledger==='RW17再核定.json'&&r.ledger==='RW23再核定.json'&&r.record_kind==='additional_records';
    if(!isHandoff&&prior.new_status!==r.new_status)throw Error('Cross-ledger conflict: '+r.path);
    overlaps.push({path:r.path,previous_ledger:prior.ledger,adopted_ledger:r.ledger,
      reason:isHandoff?'RW17明确转交的字段图类型旁路采用RW23附项；原记录不改':'Same status; both provenance records retained in ledgers'});
  }
  effective.set(r.path,r);
}
const unfinished=all.filter(x=>/待逐项|待处理|进行中/.test(x.new_status));
if(unfinished.length)throw Error('Unfinished work records: '+unfinished.length);
const report={checked_utc:new Date().toISOString(),timezone:'America/Chicago',counts,
  record_count:all.length,unique_paths:new Set(all.map(x=>x.path)).size,
  additional_scope_records:extras,requires_user_records:user,
  grouped_decisions:groupDecisions,
  requires_user_scope_records:extras.filter(x=>x.requires_user===true),
  pending_scope_records:extras.filter(x=>/待核|待决|待补|未知|暂缓|隔离/.test(x.new_status)),
  overlap_arbitration:overlaps,effective_unique_review_paths:effective.size,
  historical_truth_unresolved:all.filter(x=>/历史争议|历史冲突/.test(x.new_status)).map(x=>x.path),
  pending_records:all.filter(x=>/待核|待裁|待决|待补|暂缓|隔离/.test(x.new_status)),
  note:'Disposition completion is not truth resolution. Entry and file rows are not additive work units.',
  source_reads_by_this_script:0,token_usage:null};
if(process.argv.includes('--apply')){
  for(const name of ['文件准入队列.json','项目入口队列.json']){
    const before=hash(name),queue=load(name),idx=effective;
    const originalFields=queue.map(({reassessment_review,reassessment_history,...rest})=>JSON.stringify(rest));
    let matched=0;const queuePaths=new Set(queue.map(x=>x.path));
    for(const r of queue){const update=idx.get(r.path);if(!update)continue;matched++;
      if(r.reassessment_review&&JSON.stringify(r.reassessment_review)!==JSON.stringify(update))r.reassessment_history=[...(r.reassessment_history||[]),r.reassessment_review];
      r.reassessment_review=update;
    }
    if(hash(name)!==before)throw Error('Concurrent modification '+name);
    for(const input of names){const r=all.find(x=>x.ledger===input);if(hash(input)!==r.ledger_hash)throw Error('Input changed '+input);}
    const temp=path.join(dir,'.reassessment-'+Date.now()+'.tmp');
    fs.writeFileSync(temp,JSON.stringify(queue,null,2)+'\n',{flag:'wx'});
    if(hash(name)!==before)throw Error('Concurrent modification '+name);
    fs.renameSync(temp,path.join(dir,name));
    const saved=load(name);
    if(saved.some(({reassessment_review,reassessment_history,...rest},i)=>JSON.stringify(rest)!==originalFields[i]))throw Error('Original fields changed');
    report[name]={matched,total:queue.length,sha256:hash(name),
      original_fields_unchanged:true,
      review_paths_not_in_this_queue:[...idx.keys()].filter(p=>!queuePaths.has(p)),
      unmatched_note:'Retained in the dedicated reassessment ledgers; file and entry queues have different scope.'};
  }
  fs.writeFileSync(path.join(dir,'待核再核定汇总.json'),JSON.stringify(report,null,2)+'\n');
}
console.log(JSON.stringify({counts,records:report.record_count,unique_paths:report.unique_paths,extra:extras.length,user:user.length},null,2));
