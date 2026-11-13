import json, os, hashlib, collections
from pathlib import Path
from shard0_process import BASE, EXCLUDED, signature

# These findings were written after reading the numbered source text, not keyword extraction.
FINDINGS = {
    28: ('礼宾履约与服务边界', ['T14-T19', 'T28-T57', 'T72-T83'],
         'V0.9评审稿把受理、资格核验、风险确认、资源匹配、行前准备、现场执行、异常升级、客户结单串为八步；前台经纪运营与履约团队分工，项目经理承接高风险升级。首批建议四项低风险服务，价格、次数、资源与退款权限尚未确认。',
         '静态正文只呈现15项服务的栏目标题，分项内容不可见；未执行脚本，不声称已读15项完整SOP。'),
    36: ('客户生命周期与运营节奏', ['T3-T25', 'T26-T42'],
         '三阶段派生快照自述进入46、链接42、融入37项，折扣数12→4→0，服务重心从落地响应转向周期维护、再转事件捕捉；档案从建档、归集到冲刺交付贯穿全旅程。这是业务结构设计，不是交付完成率。',
         '125项数量、市场实证、保费档位、监管奖金与竞争判断均仅为源文自述；未读取SSOT、kill_log或外部证据，不确认其真实性和当前有效性。'),
    40: ('口碑运营与非销售角色', ['T10-T20', 'T21-T30'],
         '荣誉大使设计由客户里程碑邀请、月季活动、自然线索登记、24小时内专业承接和季度复盘构成；记录活动NPS与承接时效而不设转化考核。活动成本与转介奖励被区分，机制独立运营。',
         '仅记录历史设计；源文零金钱即合规、获客成本更低等推论未验证，不作为合规结论；身份绑定有效保单的安排亦未获本次批准。'),
    48: ('事件触发与证据交付', ['L20-L28', 'L40-L58', 'L90-L108', 'L136-L144'],
         '融入期SOP将事件捕捉作为入口；档案冲刺交付包括终检、缺口倒排、成套档案与封存，缺失证据不得制造。家庭决策记录驱动后续事项，资产清单逐项核销；年度与事件检视采用双轨，并由不同专业角色承担判断。',
         '只纳入流程设计；离港天数、身份/税务/联考条件、时点及保单权益均未核实，不作为执行规则。自动引擎是文稿设计，不证明已实现。'),
    52: ('进入期需求路由与闭环', ['L10-L18', 'L20-L38', 'L70-L92', 'L100-L108'],
         '进入期以管家首通为统一路由：需求盘点形成行动单，围绕身份证、住址、银行、电话卡推进，每周跟进后转月度。选区输出衔接房源与教育；材料清单、倒排表、核对单和触点记录让服务结果可交接。档案建档并入首次沟通，未响应归集由人工跟进。',
         'T+0/T+1/T+2及响应指标是历史设计目标，不是实际SLA达成；开户、学校政策与牌照情况不纳为当前事实，引用的产品卡未跟读。'),
    64: ('TOI产品定义与证据层', ['L3-L20', 'L22-L47', 'L59-L79'],
         '产品卡先说明为保司解决的问题，再把权益项、交付形态、证据与Gate绑定；运营链限定为触发、准备、执行、验收、复盘五步。价值证明只接受有证据的匿名指标；产品卡模板不等于已可外发产品。',
         'L0-L5是本版旧模型字段，不能推定仍为现行分类；审批解锁条件仅记录源文，不刷新当前Gate。'),
    68: ('TOI产品定义与证据层', ['L3-L17', 'L19-L29', 'L31-L57', 'L71-L83'],
         '升级建议把TOI从案例/报告导向改为可装配能力商品：价值链、经纪能力缺口、成熟度决定产品，证据作为交付后的审计层。A层内部原子、B层定价、C层对外货架分工；旧产品卡模板可保留但需改字段，而非把案例直接变为对外价值。',
         '文首明确待拍板；119原子、25 SKU、8个外部SKU是所述不同粒度，不相加，未读其引用表且不确认升级已执行。'),
    80: ('购买结果与业务验收', ['L3-L18', 'L27-L39', 'L41-L80', 'L99-L111'],
         '混合交付先看购买对象和验收锚点，再做删除测试，而不是数文档。单主交付允许替代辅助工具；双核心须两种结果均验收但覆盖只计一个原子；组合方案按阶段、整体结果与非加总计价管理。文稿指出活动需完成/复盘签收、课程需最终标准课程包，不能用更多模板掩盖结果缺口。',
         '15/5/3与Accepted为该文历史自述；本次未核批准记录、原子主表和回写状态，不代表启动或验收授权。'),
    136: ('保司价值证明的计量边界', ['L5-L7', 'L18-L35', 'L37-L41'],
         '价值证明指标须区别激活量、使用率和完成率：使用率依赖冻结基数，完成率要求已完成且有验收证据，并把第三方未履约单列。报告以匿名聚合、流程改善与机构反馈为主体，不能用客户明细或投保承诺替代运营证据。',
         '源文自述正式报表源缺失，因此只支持指标框架；不推定今天仍缺源或已经补齐，未跟随合同/PDF引用。'),
    140: ('保司价值证明的计量边界', ['L3-L18', 'L35-L44', 'L71-L79'],
         '内部模板把正式源路径、hash、期间与指标值均保留待补，并区分source_absent与source_found；从框架变正式报告候选还需源验收及多角色确认。空值是证据状态，不应填零或用估计业绩替代。',
         '不可外发是本模板历史状态；本次未核当前审批，既不解除也不推定新的外发授权。'),
    168: ('服务场景与交付深度', ['T1-T18', 'T19-T100', 'T101-T114'],
         '生活状态分落地安顿、家庭安居、城市体验三层，场景分类与交付深度另设维度。信息指引解决不知道，协办陪同解决协调难，专属统筹解决复杂事务；同一事项可有不同深度，不能把25项目等同25种统一交付规格。',
         '仅设计架构，不证明资源可售或25项已交付；长幼照护服务安排是协调，不自动授权管家亲自照护。'),
    176: ('人才能力与履约组织', ['T24-T85', 'T192-T207', 'T246-T304', 'T324-T333'],
         '人才方案不要求一人专业执行25项，而用主责管家、专项资源、专业伙伴、项目经理共同闭环。招聘以具体服务动作和实操评分验证；边界红线独立通过，不能被总分抵消。四周试用从规则、跟岗、低风险独立到综合统筹，晋升还看复杂案件与带教，不以交易量替代服务质量。',
         '为招聘候选稿；牌照适用性未核、不纳为法律知识，职级薪酬排班SLA与人数仍为文内待确认，未实施招聘。'),
}

ISOLATED_READ = {
    0: ('审计/治理混合材料，不作为业务知识准入；已读后仅保存历史口径冲突定位', ['L93-L104', 'L345-L369']),
    44: ('身份政策和税费等具体断言未核：涉及印花税比较、受养人同步与年龄硬窗口，隔离整卡，不将其转为现行服务承诺', ['T7-T17', 'T19-T33']),
    132: ('战略修正与执行安排属治理材料，隔离；自述TOB/TOI优先不等于本次核实当前执行', ['L3-L16', 'L26-L50']),
}

PENDING = {
    4:'多区域机构业务跟进纪要，潜在客户/机构经营信息未定',
    8:'财务对账及公司运营财务纪要，商业敏感范围未定',
    12:'亲子研学核心事项与安排纪要，家庭/参与人信息范围未定',
    16:'经纪收益、合规及账务纪要，商业/法律敏感范围未定',
    20:'人员管理与业务推进推理笔记，人员/经营敏感范围未定',
    24:'产品卡开发进度与分工报告，过程治理',
    32:'不透明artifact文件名，内容类型未知',
    56:'风险与决策登记册，治理证据',
    60:'owner-agent-loop任务卡，技术执行/治理模板',
    72:'架构决策记录ADR，技术/治理',
    76:'业务模型架构决策ADR，技术/治理',
    84:'佣金合规与保司渠道复核，法律及商业敏感未核',
    88:'任务跟踪台账，治理证据',
    92:'字段确认任务说明书，治理证据',
    96:'内部交付台账机制说明，治理证据',
    100:'GL25/IA诱因服务分层研究，法律解释未核',
    104:'GL25及操守守则补查报告，法律解释未核',
    108:'业财拉通待办分配，治理及财务边界',
    112:'外发合规边界确认，审批治理',
    116:'PDPO数据管控确认，隐私合规治理',
    120:'经营板块与核算口径，经营/财务敏感未知',
    124:'Phase1准入Gate刷新，治理状态',
    128:'战略拍板确认单，审批治理',
    144:'每日站会记录，过程治理',
    148:'候选证据检查纪要，核查治理',
    152:'grep结果与候选证据归档，检索命中不构成业务事实',
    156:'owner确认表使用说明，治理操作',
    160:'合同模板PwC残留风险项，法律/主体边界未核',
    164:'组织补位待办，治理及人员信息边界',
    172:'README入口，未读且不跟随外宣正文引用',
    180:'README入口，未读且不跟随确认版正文引用',
}

from shard0_supplement import MORE, REVIEW
FINDINGS.update(MORE)
ISOLATED_READ = {}
PENDING = {}
rows = json.loads((BASE / '分片0_处置.json').read_text())
assert len(rows) == 46
seen = {}
for r in rows:
    i = r['sorted_index']
    r['record_id'] = f'S0-{i:03d}'
    r['read_metrics_scope'] = '单个唯一源快照；非多次工具调用累计I/O或模型token'
    r['current_execution_verified'] = False
    r['hash_algorithm'] = 'sha256' if r['source_hash'] else None
    r['final_stat'] = signature(os.stat(r['path'], follow_symlinks=False))
    assert r['final_stat'] == r['stat_before'], r['path']
    r['final_stat_stable'] = True
    if i in FINDINGS:
        theme, locators, knowledge, caveat = FINDINGS[i]
        assert r['read_chars'] > 0 and r['stat_stable'] and r['source_hash']
        r.update(status='已分析', reason='已实际阅读'+r['read_scope']+'；仅纳入历史设计/规则/意见，不确认现行执行',
                 themes=[theme], locators=locators, knowledge=knowledge, limitations=caveat,
                 evidence_state='历史设计/模板/文内自述，非当前事实验收')
        h = r['source_hash']
        if h in seen:
            r.update(status='重复', reason='实际读取源字节SHA256一致', duplicate_of=seen[h])
        else:
            seen[h] = r['path']
    elif i in REVIEW:
        locators, observation, conflict = REVIEW[i]
        r.update(status='待核', reason=conflict, locators=locators,
                 observed_business_fragment=observation,
                 isolation_basis='已读后发现实质冲突/实体未消歧；保留待核，不以名称隔离')
    else:
        r.update(status='待核', reason=PENDING[i]+'；仅按文件名及清单预检隔离，未读正文，不认定其真实内容。',
                 isolation_basis='预检隔离', source_hash_unavailable_reason='未读取源字节，避免为计算hash而读取非必要/敏感内容')
        r['locators'] = ['295项处置明细.json:path精确匹配', '文件准入队列.json:path精确匹配']

assert set(FINDINGS) | set(REVIEW) == {r['sorted_index'] for r in rows}
src = json.loads((BASE/'295项处置明细.json').read_text())
expected = sorted(r['path'] for r in src if r['status']=='业务候选待内容核定' and Path(r['path']).name not in EXCLUDED)[::4]
assert [r['path'] for r in rows] == expected
(BASE/'分片0_处置.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
report = BASE.parent / 'RW业务主题_批量0.md'
if report.exists():
    marker = '<!-- SHARD0_SOURCE_INDEX -->'
    body = report.read_text().split(marker)[0] + marker + '\n\n'
    body += '| ID | 状态 | 源文件（绝对路径链接） | 实读字符 | 范围 | SHA256前12位 |\n|---|---|---|---:|---|---|\n'
    for r in rows:
        p = Path(r['path'])
        body += f"| {r['record_id']} | {r['status']} | [{p.name}](<{p}>) | {r['read_chars']} | {r['locator_type']} 1-{r['text_lines']} | {r['source_hash'][:12]} |\n"
    report.write_text(body)
print(json.dumps({'total':len(rows),'counts':dict(collections.Counter(r['status'] for r in rows)),
                  'read_sources':sum(r['read_chars']>0 for r in rows),
                  'read_chars':sum(r['read_chars'] for r in rows),
                  'read_bytes':sum(r['read_bytes'] for r in rows),
                  'analyzed_chars':sum(r['read_chars'] for r in rows if r['status']=='已分析'),
                  'unique_read_hashes':len({r['source_hash'] for r in rows if r['source_hash']}),
                  'token_proxy':sum((r['token_proxy'] or {}).get('value',0) for r in rows)},ensure_ascii=False))
