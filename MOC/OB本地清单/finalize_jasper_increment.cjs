const fs = require('fs');
const path = require('path');
const target = path.join(__dirname, 'Jasper16增量核定.json');
const data = JSON.parse(fs.readFileSync(target));
const decisions = [
  ['已分析', '项目受控启动需共同事实、责任、主账、证据与阶段门；合作方自述只能形成验证任务。仅文中方法论，不认证来源所称发布权限。', ['L15-L52']],
  ['已分析', '续保发送按白名单组合条件；项目方确认与我方补充须分开标识。仅摘业务筛选R1-R4，不提炼字段实现、不执行发信；发送数为历史自述。', ['L3-L4','L14-L16','L27-L34']],
  ['低复用仅溯源', '进度前缀仅为11月2日自述，测试草稿和测试邮件不是客户真实发送；未读后续台账，不称当前整体进度。', ['L5-L24']],
  ['低复用仅溯源', '变更记录保留旧新状态及来源；本次只读早期记录，不能凭mtime断言已读取11月最新变更。', ['L3-L10','L22-L39']],
  ['低复用仅溯源', '只读DEC-001至011历史段，含待签和后期对齐；不推断后续决策或执行、不跟随服务器与附件。', ['L3-L17']],
  ['已分析', '11月11日纪要区分对方单方时间估计与我方驻场规划；核名预审不等于公司设立，ODI一个月估计被后续不确定表述修正。未核截图。', ['L3-L10','L16-L35']],
  ['低复用仅溯源', '展示材料索引只作版本定位；不依源文删除、生成或运行任何文件，发布/归档自述不当现实验收。', ['L3-L16']],
  ['技术排除', '构建脚本目录的README，未读取正文。', []],
  ['已分析', '阶段小结明确区分转述、单方规划、执行层一致和双方共识；合作与出资条件均为内部历史表述，不是签约事实。', ['L219-L227']],
  ['已分析', '合作框架为供修改草案；股权/实缴与成本分担分红是不同维度，收入示例非签约，报价与收入条件非已批准付款义务。', ['L34-L41','L55-L60','L70-L85']],
  ['已有分析关联', 'v0.9与给Mark草稿的已读片段高度重合，关联INC09；未比较全文不判整文件重复或替代，保留内部/对方版本边界。', ['L34-L41','L55-L60','L70-L85']],
  ['已分析', '待确认清单把合作框架、首单保司/签约/回款与驻场环境保留为确认项，300万只是举例；源声称服务器同步未独立验证也未访问。', ['L7-L15','L20-L27']],
  ['已分析', '驻场试用是M1之前演练，不等于M1验收；四角色任务与跨部门协同为业务交付设计，开始日期/范围仍待对齐，不涉及实现代码。', ['L32-L43','L46-L59']],
  ['已有分析关联', '沟通草稿关联INC12的角色试用主题，但目标读者不同；稿件明确我方建议、对方待调整，不能当双方确认排期或外发授权。', ['L29-L55']],
  ['已分析', '近期台账将核名/ODI/驻场不确定性与规则来源分层并列；内审手册规则不等于外部监管规则，未核准手册及个案裁决不能直接通用化。只作源文历史内部观点。', ['L3-L9']],
  ['待核', 'README头部status仍为30/70待确认，正文导航称34/66的新阶段；同文件口径不一单列，不用mtime自动裁定或发布统一结论。', ['L5-L6','L15-L18']],
];
if (data.records.length !== decisions.length) throw new Error('Increment cohort changed');
data.records.forEach((r,i) => {
  if (r.stable === false || /源变化|窗口待/.test(r.status)) throw new Error('Unstable increment source');
  [r.status,r.reason,r.locators] = decisions[i];
  r.record_id = `INC${String(i).padStart(2,'0')}`;
  r.semantic_scope = '仅登记定位的必要片段，未宣称全文分析或当前执行验证';
  r.independent_review = '待核查';
  r.associated_with = i===10?'INC09':i===13?'INC12':null;
  // Keep provenance and analysis rather than a prefix-text mirror of the source.
  delete r.excerpts;
});
data.counts = {};
for (const r of data.records) data.counts[r.status]=(data.counts[r.status]||0)+1;
data.read_metrics={files_read:data.records.filter(x=>x.read_bytes>0).length,
  bytes_acquired:data.records.reduce((s,x)=>s+x.read_bytes,0),
  visible_chars_extracted:data.records.reduce((s,x)=>s+x.read_chars,0),
  note:'首次工具展示截断后仅从vault补看INC06-11，未再次读取源；不是token或全文语义字数'};
data.unprocessed=0;
data.finalized_utc=new Date().toISOString();
fs.writeFileSync(target,JSON.stringify(data,null,2)+'\n');
console.log(JSON.stringify({counts:data.counts,metrics:data.read_metrics},null,2));
