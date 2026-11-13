import json
from collections import Counter
from pathlib import Path

BASE = Path(__file__).parent
current = BASE/'分片1_处置.json'
if current.exists() and any(r.get('recheck_reads') for r in json.loads(current.read_text())):
    raise SystemExit('Historical first-pass writer disabled: use shard1_recheck_finalize.py after scope clarification')
d = json.loads((BASE/'分片1_读取证据.json').read_text())
rows = d['rows']
by = {r['index']: r for r in rows}
# These are manually authored observations from the displayed source text.
notes = {
13: ('L30-L57;L59-L113', '研学产品包装依赖课程大纲、用餐、人员配置、物料及品牌授权先行确认；报价正文区分课程预约/讲座与交通/午餐，不宜把“全包”直接当全行程报价。', '2026-05-26会议AI总结自述，不确认学校排名、授权或活动已落地。'),
25: ('L5-L19;L148-L216;L220-L296;L357-L359', '三产品方案把续签档案列第一优先；官方材料、个案补充和长期生活证据应分层，完备度不等于审批概率；管家时效先试点再形成对外SLA，身份终局只做访谈、画像、路由而不替家庭决策。', '推进方案及设计假设，不证明案例收集、试点或上线完成。'),
33: ('T20-T93;T113-T119', '旧档案卡设计了建档、季度归集、年度体检、续签前六个月冲刺及本人递交五步；其14项归集与成功率KPI须与三产品方案的分层和非概率边界并列，不能当官方统一清单。', '历史产品卡，政策及合规断言未核验，不据此执行。'),
37: ('T14-T55;T65-T79', '管家卡把身份证、住址、银行、电话卡串为统一行动单，并在首通同步启动证据档案；基础与尊享在人户配比、陪办和响应上区分，但尊享门槛仍待定价。', '历史服务设计，T+1/4h/21天等是卡内指标，不是已验证承诺。'),
41: ('T24-T63;T71-T86', '教育陪跑以子女画像、三线选校简报、窗口倒排、材料协办和年度复检连接落地与后续阶段；就读证明回流档案，搬迁需求另走房源路由，培训由第三方承担。', '产品卡设计；统计、年龄窗口、考试政策及本地生资格不作为当前事实。'),
45: ('T25-T52;T58-T70', '陪读家长支持把就业/创业意愿访谈、资源导航、月度社群和季度回访连成持续服务；社群无销售区，线索仅记录，岗位不做配对或收费的设计边界与口碑机制衔接。', '历史产品设计；“市场空白”和续保预测关系未经本次证实。'),
49: ('L8-L25;L34-L55', '口碑机制区分候选复核、本人确认、荣誉授予和线索承接；登记须被介绍人同意，随后由持牌方承接且不向大使同步销售细节；观测承接时效与留任，不考核成交额或人均转介。', 'v1.0内部机制设计；零金钱规则是源内边界，不等于法律合规认证。'),
53: ('L3-L7;L31-L59;L101-L139;L146-L167', '链接期将险企内嵌权益的交付主体与管家激活协办角色分开；保单周年、税季、教育节点及季度档案归集共用运营节奏。档案未响应14天转人工跟进，仍未响应记录而不强求；使用率与续保仅作观测。', '历史SOP v1.1；条款尚待正式落定，14项加权规则与三产品分层方案有差异，不能视为现行部署。'),
69: ('L15-L37;L43-L58;L91-L108', 'TOI框架区分模型层、原子能力底账、采购包、价格、服务设计与证据；文内98存量=97交付+1度量，119候选中的21新增须单独变更，8采购包不因装配而自动可售或可外发。', '2026-07-12内部框架自称当前；仅陈述当时分层，不认定2026-11-12仍为现行SSOT，也未读取其引用表格。'),
169: ('L3-L18;L20-L25', '25项服务标准卡被用于反推人才画像，而非先定万能岗位再拼服务；README明确服务范围、资源、时效、价格、次数、取消规则和对客话术未全部冻结。', '内部讨论稿README，仅分析本页目标和边界；未读取25张卡或Office附件。'),
173: ('L5-L22;L31-L33', '主责管家由专项资源池、专业伙伴和项目经理支持，岗位价值不是成交或供应商回扣；招聘标准须经过HR、业务、运营确认职级薪酬排班SLA和人数才可升级。', 'v0.1招聘候选README；不表示实际招聘获批。'),
177: ('L5-L22', 'v0.3把单一专业锚点调整为分阶段互补资格组合：基础安全训练、首个锚点、跨场景组合到带教与组织建设；强调个人资质和公司经营许可分管，不能用证书数量替代服务能力。', '招聘培养候选README；触发条件仍待按真实动作与经营模式复核，不是法律意见。'),
181: ('L5-L18;L24-L26', '服务介绍回答对象和价值，服务内容回答客户可感知的模块，服务流程回答体验路径，核对发送留痕等动作留给内部SOP；本次修改仅内容列，不把模块确认误当资源价格上线批准。', 'v0.5候选README自述；未打开工作簿验证列保留或专业确认。'),
}
reasons = {
1:'审计报告属于治理核查材料',5:'业务系统调整、数据管理及AI落地备忘录涉及技术和经营数据',9:'团队管理规则和财务体系会议涉及治理与敏感经营信息',17:'高净值客户合作对接涉及潜在敏感客户及商业信息',57:'资料基线与引用清单属于治理导航',61:'负责人介入地图属于职责治理',65:'模型结构化读取报告属于处理与模型治理证据',73:'模型变更规范属于治理',77:'REVIEW批次排序属于复核治理',81:'原子交付架构ADR涉及技术架构决策',85:'Owner与MARK裁定事项属于未决治理',89:'判定回复属于人员裁定记录',93:'个人任务跟踪台账属于过程治理',97:'内部交付台账机制属于治理记录',101:'内部合规清洗底稿涉及合规风险',105:'GL25合理性评估涉及法律合规判断',109:'Owner确认记录属于治理证据',113:'佣金迁出合规意见涉及法律及敏感商业安排',117:'WFOE设立建议涉及法律及公司结构安排',121:'经营板块核算口径涉及内部敏感财务治理',125:'冻结候选与Gate清单属于治理',129:'GL25原则机制涉及法律合规判断',133:'运营场景穿透盘点结果属于状态核查证据',137:'正式匿名报表源补齐结果属于证据治理',141:'字段冻结回写说明属于变更治理',145:'站会检查单属于过程治理',149:'收件箱复核属于证据治理',153:'工作文件夹交叉比对属于治理核查',157:'核心流程模板验收属于验收记录',161:'只挂资产可下放清单属于授权治理',
}
for i,r in by.items():
    r['source_hash_algorithm']='sha256' if r['source_hash'] else None
    r['hash_missing_reason']=None if r['source_hash'] else '未准入正文；不为补hash额外读取源文件'
    r['semantic_review']='未读正文，仅用途风险分流'
    r['knowledge']=[]
    if i in notes:
        loc,knowledge,boundary=notes[i]
        r.update(status='已分析',reason='实际阅读必要业务文本，形成可定位业务知识；不构成当前执行确认',locators=loc.split(';'),knowledge=[knowledge],source_state=boundary,semantic_review='全文阅读提取文本；HTML不执行脚本')
    elif i in reasons:
        r['reason']=reasons[i]+'；仅依据用途风险隔离，未读正文，不作内容结论'
    elif i==21:
        r.update(reason='正文L1标题写永明，L2-L58多处写永英，L60起又写永明；同时含对接人员态度与权限叙述。实体歧义及潜在敏感内容隔离，不统一纠正或分析',locators=['L1-L90'],semantic_review='仅实际阅读前90行后隔离；程序已读取全文件并hash，read_chars为提取字符数非全文语义已读')
    elif i==165:
        r.update(reason='阅读全文确认只是模型/HTML总入口和权威声明；属于导航治理，不跟随引用，不将125实例等自述升为事实',locators=['L7-L18'],semantic_review='全文阅读后治理隔离')
    elif i==29:
        assert r['source_hash']==by[25]['source_hash'] and r['stat_stable']
        r.update(status='重复',reason='与索引25实际读取的原始字节SHA256完全相同，不按名称判重',duplicate_of=by[25]['path'],locators=['SHA256:'+r['source_hash']],semantic_review='已稳定读字节验证同hash；语义分析复用索引25')

out=BASE/'分片1_处置.json'
out.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
assert len(rows)==46 and len({r['path'] for r in rows})==46
assert all(r['reason'] and r['status'] in ('已分析','重复','排除','待核') for r in rows)
assert all(r['knowledge'] and r['locators'] and r['stat_stable'] for r in rows if r['status']=='已分析')
print(json.dumps({'total':len(rows),'counts':dict(Counter(r['status'] for r in rows)),'read_chars':sum(r['read_chars'] for r in rows),'read_bytes':sum(r['read_bytes'] for r in rows)},ensure_ascii=False))
