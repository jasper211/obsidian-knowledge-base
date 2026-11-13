import os, stat, json, hashlib, sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from html.parser import HTMLParser

BASE = Path(__file__).parent
ROOT = Path('/Users/a112233/Desktop/Rw权益项目')
EXCLUDED = {'45_TOB服务目录与验收口径_v0.2.md', '45_TOI价值证明框架与报表模板_v0.2.md', '45_SHARED权益资产字段冻结与变更规则_v0.2.md'}
# Explicit triage decisions, not keyword-based content summaries.
BUSINESS = {3,7,11,35,39,43,47,51,63,71,95,103,127,131,135,155,171}
TECH = {15,23,31,107,159}
BUSINESS.update(set(range(3,182,4))-TECH)
BUSINESS.update({15,31,107,159})
SENSITIVE = {19,67,163}

class Visible(HTMLParser):
    def __init__(self):
        super().__init__(); self.skip=0; self.parts=[]
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style','noscript','template'): self.skip+=1
        if not self.skip and tag in ('p','div','br','li','tr','h1','h2','h3','section'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script','style','noscript','template') and self.skip: self.skip-=1
        if not self.skip and tag in ('p','div','li','tr','h1','h2','h3','section'): self.parts.append('\n')
    def handle_data(self, data):
        if not self.skip: self.parts.append(data)

def signature(s):
    return [s.st_dev,s.st_ino,s.st_mode,s.st_size,s.st_mtime_ns,s.st_ctime_ns]

def scan():
    items=json.loads((BASE/'295项处置明细.json').read_text())
    candidates=sorted([r for r in items if r['status']=='业务候选待内容核定' and Path(r['path']).name not in EXCLUDED],key=lambda r:r['path'])
    assert len([r for r in items if r['status']=='业务候选待内容核定'])==185
    assert len(candidates)==182
    rows=[]; texts={}
    for i,r in enumerate(candidates):
        if i%4!=3: continue
        p=Path(r['path'])
        row=dict(index=i,path=str(p),status='待核',reason='',source_hash=None,mtime=None,locators=[],read_chars=0,read_bytes=0,project_scope='RW限定根内；非正文批准',stat_before=None,stat_after=None,stat_stable=None,token_count=None,token_proxy=None)
        rows.append(row)
        try:
            p.relative_to(ROOT)
            for part in [*reversed(p.parents),p]:
                if stat.S_ISLNK(part.lstat().st_mode): raise ValueError('拒绝链接路径')
            kind='业务文本候选' if i in BUSINESS else ('技术内容隔离' if i in TECH else ('经营财务或合同主体敏感待核' if i in SENSITIVE else '治理/任务/索引或资料筛选记录隔离'))
            row['content_triage']=kind
            before=p.lstat(); row['stat_before']=signature(before); row['mtime']=before.st_mtime
            if not stat.S_ISREG(before.st_mode): raise ValueError('非普通文件')
            if not 1778389200<=before.st_mtime<1794376800:
                row.update(status='排除',reason='首次stat不在指定半开时间窗口'); continue
            if p.suffix.lower() not in ('.md','.html'):
                row.update(status='排除',reason='非MD/HTML'); continue
            if i not in BUSINESS:
                row['reason']=kind+'；未读取正文，不作业务分析'; continue
            fd=os.open(p,os.O_RDONLY|os.O_NOFOLLOW)
            with os.fdopen(fd,'rb') as f:
                opened=os.fstat(f.fileno())
                if signature(opened)!=signature(before): raise ValueError('打开前stat变化')
                data=f.read(); after_fd=os.fstat(f.fileno())
            after=p.lstat(); row['stat_after']=signature(after)
            row['stat_stable']=signature(before)==signature(after)==signature(after_fd)
            row.update(read_bytes=len(data),source_hash=hashlib.sha256(data).hexdigest())
            if not row['stat_stable']: raise ValueError('读取前后stat不稳定')
            content=data.decode('utf-8-sig')
            if p.suffix.lower()=='.html':
                parser=Visible(); parser.feed(content); content='\n'.join(x.strip() for x in ''.join(parser.parts).splitlines() if x.strip())
                row['locator_type']='HTML清理后非空文本行T；不执行脚本、不取外链'
            else: row['locator_type']='MD原文行L'
            texts[str(i)]=content
            row.update(read_chars=len(content),token_proxy={'method':'ceil(visible_chars/2), not tokenizer','value':(len(content)+1)//2},reason='已安全读取；等待本轮逐文人工语义核定')
        except Exception as e: row['reason']=str(e)
    return rows,texts

# Manually authored conclusions after reading; no regex summarization.
ANALYSIS = {
35: ('83588a7a64459667f4b079a622389c44c37dced0b444e0945bef4cdf95a9c65e', [(3,9),(83,96)], '权益分类与阶段变化', '历史设计把价值类型与战略角色作为两主轴，载体降为派生标签，只有服务保留多载体选择；交付方、价值锚和绑定条件另作运营字段。页首46项与页尾40项、10/12与11/12格、货币3与4项、核心10与8项互相冲突，数量不采用，不据此重算SSOT。'),
39: ('21a3f88dbec671782a37318e579d219aabbe0ff4aea56093a9febca3b6868212', [(3,5),(10,27)], '企业主年度证据服务', 'PC-06把公司登记指引、CPA委聘、合规日历、月度凭证和年度归档串成服务链。客户与CPA直接签约收费，RW定位日历与归档；文中T+14及申报率100%仅为产品卡设计指标。拒绝买生意续签撮合，不把营运证据叙事转成续签保证；真实营运必要条件及保单绑定合法性未核。'),
43: ('0d21429eb1b69a819111c1dd698ccb81b70c8665e0c4824b4698f201b84f02f9', [(3,16),(17,32)], '财富传承服务分工', 'PC-08设计内嵌激活与独立引荐两通道，由年度及身份事件后的受益人架构检视识别需求；独立引荐要求至少两家受托人供选、客户直接委聘，专业意见由律师/CPA/受托人出具，保单动作归JF。家庭会议、二代教育与慈善资讯仍列C级候补。保费档、服务商、证据等级及退保条款均为源卡自述，未复核，不当作当前权益承诺。'),
47: ('85039d8a617d6b15e7daa8037beca63d519ce2275e1a0b7a1ca4005ec181e2aa', [(3,12),(73,82)], '权益分类与阶段变化', '链接香港设计把持续服务转为年度与事件触发：报税、体检、MPF为周期，就医、插班、开业为事件。服务允许独立、内嵌、第三方三种载体；折扣在本页只用于引流，服务不做引流。42项、7个A级内嵌服务及高端档位仅是本页历史声明，未追读外部证据；与进入阶段比较可形成设计假说，不是现行业务统计。'),
63: ('1efebb33ae9a4b51f4f24641ca93415f1a18cb11321a48d409428a444865b18a', [(3,24),(26,38),(49,80),(84,93)], 'TOI产品化层次与状态分离', '2026-07-07规划稿认为案例直接跳报告会缺失权益项原料池和产品卡规划；权益项承载原料、SOP承载执行、产品卡包装价值、报告证明结果。TOC按客户旅程，TOI按渠道赋能、权益激活、资源运营及匿名价值证明表达，可共用底层资产但不能混用包装。L0-L5和六张卡是派生草案，不是正式SSOT，PC-TOI-05受当时OB-G7限制。'),
71: ('6c3bc6a0a33a2d8485ebc77385161c2d1732c098014e53e89820206e008cf10f', [(3,30),(32,47),(49,84),(88,104)], 'TOI产品化层次与状态分离', '2026-07-12内部下游记录列目标119原子、当前98存量、21新建按3/9/9波建设，C层八包包括持牌开业、数据经营、履约、产品认知、营销、销售培训、顾问展业、增员。缺证据产生建设任务，不据此删除目标能力；model/build/evidence/external四状态分开。C6优先及design_ready是当时记录，不证明今天整包可交付。依赖共享财务口径不改变TOI归属，报价和外发另需审批。'),
135: ('f64d8e74798ddade0423b53ac4ea4ec4747b993b449f0bd77842fe2d57dd1c1a', [(5,22),(24,59)], 'TOB机构服务交付闭环', 'TOB包的对象是机构服务范围、上架、培训和验收，而非客户无条件权益。六步业务链为需求诊断、寻源上架、合同范围确认、宣导培训、执行异常处理、验收归档；每步须有对应证据。第三方还缺准入/SLA/异常机制，价格成本毛利待财务；RACI在合同和验收行存在多个A/R，不能擅自归并成单一最终负责人的已定规则。'),
171: ('f60d1947298688a2bafdd595af51e85c13fb33f3c46f63288129db323ebad873', [(1,24),(54,116),(134,216),(224,306),(310,312)], '香港管家交付与责任边界', '内部讨论稿以服务介绍、内容、流程、边界四字段定义25项服务，覆盖落地安顿、家庭安居、城市体验；信息指引、协办陪同、专属统筹是介入深度而非客户身份档位。八步流程以建单开始、客户确认及结单留痕结束。开户由客户回答KYC和签署；就医仅做流程协助不解释报告；儿童活动不由管家单独监护。上线前仍须冻结费用、取消、补偿权限、数据期限、SLA和责任人，未具备正式对客承诺条件。'),
}
ISOLATED_READ = {
3: ('正文跨经验引擎、EA、数据与组织改造，混入技术能力断言及具体人员/股权安排；位于RW根不证明其中跨项目结论归属RW，无法据必要片段划清RW业务事实范围，隔离；不是因治理或人员裁定主题名称拒读', [(4,11),(29,41),(130,159)], '部分正文语义审阅后隔离'),
7: ('纪要混入个人评价、签约结算与跨境支付细节；整件敏感隔离，不复述或验证人事指控', [(6,14),(17,35)], '全文语义核定后隔离'),
11: ('纪要混入人事指控、经营财务与渠道结算信息；不将其中培训采购或收费自述转为当前事实', [(11,30),(70,84)], '全文语义核定后隔离'),
51: ('文本以市场惯例直接推导低风险及合法性，涉及回佣、转介与监管豁免；未核法源，合规未知单列，不作业务安全性结论', [(3,17),(22,46)], '全文语义核定后隔离'),
95: ('付款条款建议含跨境支付及税务责任断言；法务财务待核，不读取其引用的Office合同，不作为可执行条款', [(15,29),(33,43)], '全文语义核定后隔离'),
103: ('风险提请及合规治理记录；自身明确非合规结论，涉及既往外部敞口；不采纳法律定性，也不据自述四份相同认定重复', [(9,15),(27,43),(79,95)], '全文语义核定后隔离'),
127: ('上位定位及项目治理建议，引用EE材料和未经本轮复核的扫描结论；非正式拍板记录，单列治理待核', [(3,24),(97,120),(154,162)], '全文语义核定后隔离'),
131: ('内控交付留痕模板，明确待法务合规审定后进入系统；不将空白模板当成客户授权、审批或真实交付证据', [(3,16),(136,149)], '全文语义核定后隔离'),
155: ('案例口径纠正与Gate治理记录；自身仍为候选线索，不证明正式交付；不追读证据收件箱', [(3,9),(19,33)], '全文语义核定后隔离'),
}
UNREAD_REASONS = {
15:'系统调整、数据管理与AI落地工作备忘录，技术/治理信号',19:'银行业务、团队管理与财务体系会议，经营财务敏感信号',23:'续签证据完整字段映射图，数据结构/技术且可能含个人证据字段',27:'战略资料筛选报告，二次筛选治理而非原始业务内容',31:'系统PRD，技术产品需求规格',55:'MVP Backlog，开发与项目任务治理',59:'owner每日跟进与介入机制，过程治理',67:'合同主体矩阵草案，主体责任及合同敏感口径未核',75:'模型变更管理规范，模型治理',79:'REVIEW批次及agent边界复核，复核治理',83:'语义例外复核清单，质量治理',87:'正式发布决定与切换记录，发布治理不等于当前执行',91:'个人任务说明书及字段确认，任务/数据治理',99:'CR映射提请，变更治理',107:'业财拉通自动化方案，技术与财务交叉',111:'个人主动认领边界清单，任务治理',115:'外部承诺合规分级规则，合规治理口径待核',119:'请求评审会，会议过程治理',123:'0周立项决策包，立项治理',139:'正式启动留痕，过程证据',143:'等待期推进清单，过程治理',147:'下一次检查单，复核治理',151:'外发Gate与source_absent说明，证据治理',159:'任务面板生成记录，技术/生成过程',163:'财务字段口径确认交接，敏感财务治理',167:'架构图目录README，仅入口与内容性质未知',175:'招聘画像目录README，仅入口与潜在人员信息未知',179:'服务结构化确认版README，仅入口；不据目录或确认版名称推断正文已确认',
}

# Additional minimal business passages reviewed after the user's scope clarification.
EXTRA = {
7: ([(15,20),(26,35)], '培训产品与专业资源组织', '历史洽谈把高客课程与专家资源两种供给分开：课程需要导师分层、报价及签约安排，专家陪谈按小时调用，机构一次性服务另设合作路径。这里只提炼供给组织方式；人事评价、具名利益关系、费用实数及跨境安排不采纳，不认定合同路径现行有效。'),
11: ([(3,9),(37,43),(54,69),(85,91)], '培训产品与专业资源组织', '历史纪要按入职、6至12个月、12个月后分培训阶段，后期分专业进阶和组织发展；服务菜单区分整体咨询、指定模块和高客专项培训。专项培训草案将财务/事务/税务/法务课程、案例实操、认证后陪谈资源和KYC评分门槛连接。门槛及采购确认仅为纪要自述，不采用人事指控、结算渠道、个体评判或对外收费承诺。'),
15: ([(17,33),(50,66)], '数据口径与业务证据', '历史备忘录把新旧订单编号对照、表头校验列为跨表统计前置条件，并指出排期、预约、签单、批核、撤销需要分别定义业务映射。批核日期非空只是临时方案，取消后日期是否保留未确认，不能凭单字段产生正式业务报表。仅分析业务口径，不分析代码、系统改造或约800状态的真实性。'),
19: ([(35,67)], '执行治理与分阶段授权', '该纪要的企业决策体系片段要求统一术语和SSOT，内部反馈同时提交判断、理由及风险；对外沟通与突发应急不套用同一格式规则。现有/目标规则数量是自述，且有效期同时写长期与Q3末，期限不采用。银行退票段中的实体及交易细节不作归并或分析。'),
27: ([(3,17),(54,71)], '权益产品范围与证据质量', '筛选报告主张先做续签档案、落地管家和身份终局规划三个MVP，先还原线下SOP再系统化；区分保险公司潜在买单方、持牌入口与家庭使用方。其材料错位和重复结论未追查，不能替代本轮hash；源文14项证据与会议13项冲突保留，商业闭环是历史建议。'),
31: ([(3,19),(21,31)], '行政服务与专业责任分离', 'PRD业务使命为新港人长期行政服务；需求要求有上游SOP来源，无来源功能不入v1.0。业务权限设计把JF限于转办和服务摘要、CPA限于相关委聘分区，保单只保留服务所需派生标志。仅分析使命与责任边界；后续模块、触发器、数据模型及技术实现不纳入知识，法律保证性表述不采用。'),
51: ([(4,17),(22,36),(37,46)], '历史合规意见与产品风险', '历史矩阵把缴费方式、续期、健康行为等奖励归入险企定价场景，把付费转介单列高风险，试图区分介绍客户与推介产品、自然口碑与付费奖励。其绿色评级、合法/违法判断及监管豁免均未经本轮法源验证，只记录历史分类意见；不能作为客户话术、合法性或上线批准。'),
55: ([(3,14),(36,65)], '权益产品范围与证据质量', '启动Backlog将资产治理、TOB规范化和TOI价值证明列P0，TOC列成熟度准备。业务验收要求SKU有对象/版本/owner，供应有准入/SLA/退出，机构服务有范围及验收，TOI报告要能追溯成本、来源和交付证据。仅分析业务用户故事，不把开发需求或P0标记当已实现。'),
59: ([(18,53),(55,73)], '执行治理与分阶段授权', '每日更新采用完成事项、证据、灯号、阻塞、介入需求、下一步和更新时间七字段；无证据的完成不算完成。历史机制规定P0超过24小时无更新或同一阻塞超过一个工作日升级，财务/外发事项依各自owner处理；明确证据充分但排版不美观不应触发决策人介入。'),
75: ([(8,37),(39,72)], 'TOI产品化层次与状态分离', '模型规范规定证据不能决定能力是否存在，按权威输入分层管理原子、SKU、产品包及价格研究；四种状态分别回答模型归属、建设进度、证明程度、外用权限。C0至C4区分格式、状态、结构、边界及紧急风险变更，紧急冻结只能收紧不得放宽；新能力先建任务再演练试点。Active为历史文件标签。'),
79: ([(7,11),(28,34),(65,75)], '权益产品范围与证据质量', '历史复核任务把机构合同主体、上架、RACI与资源入驻作为可参考范围，排除本批TOC交付。旧版/冲突版只能历史参考，不能未经有效性证明直接进基线；输出区分纳入、历史参考、继续REVIEW和不可用。这里只记录复核规则，没有执行文中指令或读取24件Office引用。'),
83: ([(7,11),(63,73)], '服务产物语义与可追溯性', '语义复核不是一律回退分类：要求逐件决定保留、回退、另分或拆合，同时说明可观察对象、交接方式和验收证据。对同名工具功能点要求按输入、检索、生成、复核、导出区分，或证明可合并；不能以父级优先代替产物判断。65异常与1020mention等为原清单统计，未复验。'),
87: ([(9,35),(37,44)], 'TOI产品化层次与状态分离', '发布决定自述批准v3.3.1作为内部Current，但生效仍要求候选一致性验收、台账同步和发布闭环；失败保持旧Current，旧版保留不覆盖。754待决项不得随发布关闭，119项模型发布不代表全部可交付/报价/外发。本轮未读取工作簿或验收报告，因此不确认实际切换已完成。'),
91: ([(10,39),(43,63)], '数据口径与业务证据', '字段确认任务区分数据owner与JF关系接口人；历史清单允许状态、档位、周年月等最小镜像，禁止保费、佣金及条款。关键问题是可提供字段、更新频率及无法提供的原因；可存不等于实际可获取，缺字段须走降级。这里只分析数据业务约束，无个人保单值、无实现分析。'),
95: ([(5,11),(15,29),(33,43)], '业务财务与付款边界', '付款修订建议将商业发票和双方签署验收单作为支付前置，约定无法接受指定支付方式时另行书面约定，并声明不承诺最低采购量。CNH支付、税务自理及无需代扣等仅为历史条款建议，不作为现行法律/税务结论；[30]工作日及第X条仍为模板占位。未打开所引DOCX。'),
99: ([(11,13),(23,36),(54,75)], '服务产物语义与可追溯性', '变更提请区分钱台账、服务原子主表和文件资产册的记录对象，认为补三行文件不能解决服务编号映射。建议asset_id对多个atom_ids并记合同/流程/价值证明等关系类型及无对应原因。其全库无映射断言未经本轮复查，映射仍待裁定，收入数字不进入知识。'),
103: ([(15,25),(27,43),(79,95)], '历史合规意见与产品风险', '风险提请关注续签档案销售叙事与不得暗示买保单更易续签的内部冲突，以及保单绑定、价值锚、续保奖金联动。提请要求明确判断销售用语、补评估、清洗客户物料并检查既往传播敞口；源文明确不是合规结论。四副本相同仅为源文自述，不用于本轮重复标记。'),
107: ([(8,26),(30,38),(64,75)], '业务财务与付款边界', '业财方案历史修订把佣金移出RW、关联交易独立反映、收入成本时点匹配和内部人力分摊列为业务控制；框架额度只记上限，实际执行单触发消耗，财务满足后仍待合规放行。仅取业务修订说明，不分析SQL、自动化实现，也不把已修视为已投产或现行会计政策。'),
111: ([(20,39),(50,69)], '数据口径与业务证据', '认领清单把G7前段业务事实/源/指标/合规冻结与后段结构化分开；数据owner可做后段准备，但不替业务找原始课件、付款证明，不代判外发叙事或代签审批。仅分析责任边界，DB、ETL及加密实现不纳入。carrier与Carrie的对应仅据源文自述，不拓展到其他实体。'),
115: ([(15,36),(60,75),(79,120)], '历史合规意见与产品风险', '2026-07-29内部规则将对外承诺权与文件存在、财务确认区分：缺源blocked，共享底座不适用，其余经财务与合规链路。合规层分允许、条件允许、待上游决策、禁止；条件包括匿名化、授权、摘要改写及口径冻结。法律引文不验证、不输出法律结论；代码和字段枚举实现不分析。'),
119: ([(9,21),(25,47),(68,75)], '业务财务与付款边界', '一页式请求把业财方案、关联定价、人力标准成本率、WFOE并列方案及尽调交给Mark决策；后续先补定价与合规意见再实施。正文称材料齐备但T-02仍待定价，属于有前置条件的可评审，不等于可执行；第53行关系链文字损坏隔离，不修复推断。所有价格及资本为当时建议。'),
123: ([(3,24),(26,51)], '执行治理与分阶段授权', '决策包将战略定位单人拍板与0周执行会承接区分；默认P0为资产、TOB、TOI，TOC后置，JF先人工镜像，缺匿名汇总源只做报告框架不冻结正式报告。本文是会前收口稿，默认决议不是已经追认；历史(1)不独立计权规则不替代本轮同hash去重。'),
127: ([(3,5),(26,36),(61,95),(97,107)], '权益产品范围与证据质量', '定位建议将权益部门作为Layer B产品化事业线，而非普通客服或CRM；Layer A供基础能力、B管SKU/成本/供应链/证据、C向四对象分发。客户交付MVP保留但不代表整个项目，P0优先已有TOB/TOI场景，TOC补资源与授权后再启动。属于上位建议，不等于战略批准，EE引用未跟读。'),
131: ([(3,16),(43,56),(58,103),(136,149)], '行政服务与专业责任分离', '专家咨询模板把客户授权、服务边界、第三方委聘、事实摘要、专业意见路径和转办承接组成最小留痕链。原记录不可删改，纠错追加；转办需记录RW是否停止实质讨论、承接及客户通知。空白模板是待审内控设计，不证明真实授权、资质或咨询发生。'),
139: ([(3,18),(51,67)], '执行治理与分阶段授权', '启动留痕自述项目进入带Gate限制的Phase0，资产治理及TOB/TOI框架先行；配置验收与执行包就绪转绿，同时客户外发与正式保司报告仍红。该记录不能单独证明用户批准、业务已经交付或所有owner实体已消歧；与会前决策包应分版本时间解释，不简单覆盖。'),
143: ([(3,25),(28,41)], '执行治理与分阶段授权', '等待财务确认不等于全项目暂停：站会、证据登记、内部模板及阻塞跟踪可继续，价格成本毛利、预算归因、正式外发及自动结算不推进。成功标准是每条流程有状态、有应查证据和明确依赖，不新增财务或客户承诺。历史等待状态不推定今天仍未确认。'),
147: ([(3,23),(25,36)], '数据口径与业务证据', '检查单分别看内部叙事、受限背景、合作提案清洗及正式源缺口，SHARED则看字段可见性与变更留痕。非财务规则可继续，财务冻结待确认；发现源后必须重新补源验收，不因发现一个文件直接转绿。是检查规则，不是检查已完成结果。'),
151: ([(3,24),(26,41)], '数据口径与业务证据', 'source_absent只指缺少支撑正式外发报告的匿名汇总源，不否定真实业务可能存在。内部可做案例证据化、指标字典和pending_source占位；外发需源、期间、分子分母及排除项、匿名化、owner和审批齐备，策划机会不得当完成交付。文中业务存在是源文自述，未另核。'),
155: ([(3,9),(19,33)], '数据口径与业务证据', '案例纠正记录将CASE-001名称改为太保香港课程服务，并列议程课件、需求确认、执行签到/录屏、结算及外发确认等证据缺口。名称纠正不等于交付凭证，本文当时仍为候选线索且G7红。本轮不消歧公司法律实体、不追读课件或付款原件。'),
159: ([(7,16),(28,39)], '执行治理与分阶段授权', '面板生成记录明确Phase0显示执行快照，而Phase1至3仅展示目标及进入条件；静态面板不自动读取CSV，源台账变化须刷新。不因界面有未来阶段就认定已执行，也不把生成记录等同实时状态；不分析HTML实现。'),
163: ([(13,34),(36,42)], '业务财务与付款边界', '交接说明把含税收入、成本与费用分界、毛利/净利公式、应收实收及应付实付、汇率和入账粒度列为待Roy确认问题；对公/个人终点及法人收付款开票链仍开放。v0.1发出不等于v0.2补发，回填未完成不能自动结算。开放项文字写3项实际列4项，保留不改；未读台账XLSX。'),
167: ([(3,15)], '香港管家交付与责任边界', '架构README直接说明三服务层、十类、25项和三级介入深度，管家做需求、策划、协调、陪同、跟进，专业判断及签署归专业机构。它自述产品讨论逐项确认，但仍是内部视觉稿，不自动批准价格、上线或对客承诺；未跟读PNG/HTML。'),
175: ([(3,17),(27,36)], '管家招聘与培养', '人才设计先招服务底盘再培养专业资质，采用一项基础安全资质、一个专业锚点和一项运营能力；职业路径从学员到主责家庭管家再分专家/管理。薪酬按资质、复杂度、质量与带教贡献，不设交易或转介佣金。个人牌照不等于机构资格，正式招聘仍需合规、HR、业务、运营确认。'),
179: ([(3,12),(18,20)], '香港管家交付与责任边界', '服务内容结构化调整把25项服务统一成三项服务模块，说明客户具体获得什么，不重复流程、不扩大专业边界。源文明确为外宣及移民公司确认候选稿、待逐项确认；文件名含确认版不代表已确认，未读取所引XLSX。'),
}

def finalize():
    rows,texts=scan()
    now=datetime.now(timezone.utc).isoformat()
    for r in rows:
        i=r['index']; r['checked_at']=now
        r['metrics_scope']='本次最终读取快照；read_chars为解码/清理文本字符，不等于模型token或累计I/O；未读为0'
        r['hash_algorithm']='sha256' if r['source_hash'] else None
        r['hash_unavailable_reason']=None if r['source_hash'] else '正文准入前隔离，未为hash另读内容'
        r['semantic_review']='未读正文，仅元数据及文件名保守隔离'
        if i in EXTRA and r['stat_stable']:
            ranges,theme,knowledge=EXTRA[i]
            r.update(status='已分析',reason='按用户澄清核定最小业务片段；仅历史规则/设计/意见，不验证法规、不认定当前执行',theme=theme,knowledge=knowledge,semantic_review='实际阅读所列业务片段；非全文语义完成',current_execution_verified=False)
        elif i==67 and r['stat_stable']:
            ranges=[(1,8),(16,22),(63,75)]
            r.update(reason='真实版本及T8裁定冲突：标题v0.6、状态v0.7待评审与T8已结案并存；源文主体/责任链不能据此唯一确定，隔离不擅自裁决',semantic_review='最小业务片段核定后保留冲突待核')
        elif i in ANALYSIS and r['stat_stable']:
            expected,ranges,theme,knowledge=ANALYSIS[i]
            if r['source_hash']!=expected:
                r['reason']='与本轮实际审阅快照hash不同，隔离'; continue
            r.update(status='已分析',reason='已实际阅读业务文本并形成逐文知识；历史设计/自述，不等于当前执行或批准',theme=theme,knowledge=knowledge,semantic_review='全文阅读并手工语义分析',current_execution_verified=False)
        elif i in ISOLATED_READ and r['stat_stable']:
            reason,ranges,review=ISOLATED_READ[i]
            r.update(reason=reason,semantic_review=review)
        else:
            if r['status']=='待核' and i in UNREAD_REASONS: r['reason']=UNREAD_REASONS[i]+'；不读正文、不假分析，隔离即本轮处置完成'
            continue
        prefix='T' if Path(r['path']).suffix.lower()=='.html' else 'L'
        lines=texts[str(i)].splitlines()
        r['locators']=[{'range':f'{prefix}{start}-{prefix}{end}','start_line':start,'end_line':end,'anchor':lines[start-1][:100]} for start,end in ranges]
        r['reviewed_fragment_chars']=sum(len('\n'.join(lines[start-1:end])) for start,end in ranges)
        for start,end in ranges: assert 1<=start<=end<=len(lines)
    seen={}
    for r in rows:
        if r['status']=='已分析':
            h=r['source_hash']
            if h in seen:
                r.update(status='重复',reason='本分片已准入业务文本完整原始字节SHA256相同',duplicate_of=seen[h])
            else: seen[h]=r['path']
    assert len(rows)==45 and len({r['path'] for r in rows})==45
    assert all(r['index']%4==3 for r in rows)
    assert all(r['source_hash'] and r['stat_stable'] and r['locators'] and r['knowledge'] for r in rows if r['status']=='已分析')
    assert all(not r['read_chars'] for r in rows if not r['source_hash'])
    out=BASE/'分片3_处置.json'
    out.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    report=BASE.parent/'RW业务主题_批量3.md'
    if report.exists():
        marker='<!-- GENERATED_SOURCE_REGISTER -->'
        main=report.read_text().split(marker)[0].rstrip()
        register=[marker,'','## 逐项来源与处置索引','','S编号是排除三文件后Unicode排序的全局零基索引，不是文件编号。MD用L行，HTML用剔除脚本/样式后的非空T行。完整SHA256、stat、知识条目及阅读指标见JSON。','']
        for r in rows:
            ranges='、'.join(x['range'] for x in r['locators']) or '未读正文，无内容定位'
            register.extend([f"### S{r['index']:03d} · {r['status']}",f"来源：[{Path(r['path']).name}](<{r['path']}>)",f"定位：{ranges}。原始字节SHA256：`{r['source_hash'] or 'null（准入前隔离）'}`。",f"处置：{r['reason']}"])
            if r.get('knowledge'): register.append('知识：'+r['knowledge'])
            register.append('')
        report.write_text(main+'\n\n'+'\n'.join(register)+'\n')
    print(json.dumps({'total':len(rows),'status':dict(Counter(r['status'] for r in rows)),'read_files':sum(bool(r['read_bytes']) for r in rows),'snapshot_read_bytes':sum(r['read_bytes'] for r in rows),'snapshot_read_chars':sum(r['read_chars'] for r in rows),'analyzed_chars':sum(r['read_chars'] for r in rows if r['status']=='已分析'),'sha256_duplicates_in_read_set':len([r for r in rows if r['source_hash']])-len({r['source_hash'] for r in rows if r['source_hash']}),'output':str(out)},ensure_ascii=False))

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='finalize':
        finalize(); sys.exit()
    rows,texts=scan()
    if len(sys.argv)>1 and sys.argv[1]=='read':
        wanted=set(map(int,sys.argv[2:]))
        for r in rows:
            if r['index'] in wanted:
                print('\n###',r['index'],r['path'],r['reason'])
                for n,line in enumerate(texts.get(str(r['index']),'').splitlines(),1):
                    if os.environ.get('SHARD3_MINIMAL') and n>75: break
                    print(f'{n}: {line}')
    else:
        print(json.dumps(rows,ensure_ascii=False,indent=2))
