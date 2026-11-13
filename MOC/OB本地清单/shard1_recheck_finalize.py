import hashlib
import json
import os
import re
from collections import Counter
from pathlib import Path
from shard1_audit import no_links, snapshot

BASE = Path(__file__).parent
OUT = BASE/'分片1_处置.json'
# Manually written after reading the specified business excerpts.
NOTES = {
1: ('L3-L40', '审计建议以三阶段客户旅程组织权益运营，以服务交付、档案、权益激活和渠道价值证明作为产出；其立项建议明确限定为受控MVP，不等于37个SOP可全量生产。', '2026-07-04审计建议自述；可行性评分与被引用材料未重验，后续S57将TOB/TOI优先列为修正口径。'),
5: ('L10-L13;L29-L59', '备忘录将权益使用从预约起计量，区分已签单、批核、生效和结算；实际发生费用不因保单未生效而漏记，迁移先服务价值订单后全台账。它同时保留取消后批核日期是否保留、状态映射未定等缺口。', '2026-05-27会议总结中的业务统计规则，不作为现行结算办法；函数、系统实现及AI实现段不分析。'),
9: ('L13-L40;L44-L62', '会议自述以财务SSOT防止单点失效；反馈需含判断、依据和风险，任务小组在明确边界内推进。营销费用管理强调资金打款四锚点留痕，但此片段未给四锚点定义，不补造定义。', '历史会议规则及组织设想；不把效率目标或机制完成自述视为实际成效，不展开银行单笔事项。'),
17: ('L28-L56;L89-L116;L118-L145', '洽谈摘要提出按小时采购专家陪访/咨询以便跨合作场景复用，并要求合同、付款、交付可追溯；同文对香港直签要求与内地对公供应商例外分别叙述，不能抽成唯一签约路径。', 'AI会议总结；仅采用服务采购与流程设计，不采用人员矛盾、动机、报价、利润推断或法律有效性结论。新动力与RW实体关系不自行合并。'),
57: ('L14-L21;L77-L96;L104-L125;L127-L144', '基线清单将旧v3的25聚合簇记为迁移来源，将193记为内部Current，21新增进入目标模型和开发任务；发布仍保留754开放项。它明确把119框架和125变更规范列作历史或被替代输入，导航和派生视图不改变源权威。', '读取的是版本登记自述，不是被引用工作簿的当前验证；本批S69与S73不再被误用作现行基线。'),
61: ('L10-L40;L43-L61', '负责人介入分三层：方向/Gate/财务和跨owner争议需亲自裁定，给口径后可授权的事项短介入，模板维护与每日汇总只看结果；业务采用、财务字段、外发脱敏各自有责任归属。', '2026-07-06介入建议和当时红黄灯快照；不据此宣告今日任务未完成。'),
65: ('L9-L17;L28-L41;L50-L84;L86-L121', '读取报告把内部能力底账、对保司采购货架、定价阶梯与服务设计分开：底账管资源成本与归属，货架用采购语言，服务设计回答怎么交付而非怎么报价；两个同名v2候选当时需Owner确认。', '早期模型重构输入，S57后来将25簇降为迁移来源；23文件读取与内部数量均为源报告自述，未重复验证。'),
73: ('L10-L37;L39-L62;L92-L120', '变更规范要求CR、影响分析、审批、候选、验证、发布、登记闭环；紧急机制只可收紧不可放宽，前序与错误版本保留追溯。人工验收与批准发布不能被机器检查或文件名Final替代。', 'v1.0历史规则，S57 L122明确记为superseded；不执行其4合并1删除等首次应用方案。'),
77: ('L7-L38;L40-L59', '复核排序先合同主体与机构流程、佣金渠道和培训对象，再客户MVP，避免早固化客户承诺；复核通过只产候选与需确认，不自动释放基线。表内B5原42与说明中调整后的37属于不同统计阶段。', '2026-07-04复核流程及进度自述，不据文件名或表内数量替代当前完成状态。'),
81: ('L9-L25;L27-L42;L44-L72', '原子保留服务定义、内容模块、交付物结构、经纪行使用流程及CII五要素；八种形态只描述最终交付物，不是SKU。U046不能缩成课程，组合解决方案须分阶段及整体验收、非加总计数，不能按组件数累加覆盖或报价。', 'Accepted业务交付架构决定自述；不读取或实现Schema、Agent任务、软件功能，数量不当成交付成熟度。'),
85: ('L7-L9;L24-L52', '结构整合不关闭建设、证据、价格和合规缺口；Accepted family缺口只能补真实可追溯产物或走CR/ADR修改，不能靠模板、栏位、标签凑数；定价与非加总规则须一起确认。', '754项开放事项的历史汇总而非逐行关闭证据；不替Owner代签或判断今天是否已闭环。'),
89: ('L11-L31', 'Amanda反对把RW直签作为所有大陆TP单的唯一默认：自找供应商与银行指定且不收CNH的供应商分别处理；供应商盘点要先于唯一默认决策，新增合同付款仍走三方人工审批。', '2026-07-14业务判定回复，保留对合规方案A的异议，不认定方案B当前合法或已获最终放行。'),
93: ('L5-L6;L17-L28;L31-L40', '个人任务台账只记录本人完成事项，识别问题但未授权修正写identified_not_executed；数据标准化接手以业务口径、合规及审批先确定为前提，候选源有hash和机器校验不等于敏感性人工复核或正式源。', '台账自述含后续更新；本批仅分析职责及证据状态，未打开DB、数据字典或保单源，不验证completed标签。'),
97: ('L17-L68;L100-L145;L177-L188;L217-L280', '台账记录服务事实而非财务：服务后T+1记、真人验收、证据空白不计指标；合同每单时限替代统一SLA档。保司购买者与TOI→TOB受益路径分开，钱/服务/文件三种底账分别管理，服务场次挂U原子而非ASSET文件编号；使用率分母及投诉另需机制。', '机制含07-17启用和07-20纠偏自述；建台账不解锁OB-G7，不把数据0行启用等同服务交付或报告就绪。'),
101: ('L1-L8;L30-L77;L97-L104;L110-L169', '清洗底稿将销售因果叙事从客户卡移出而保留内部改动证据，服务本体与KPI未一并重构；同义扩改需复核，找不到ILAS客户材料不能等于无需剥离。测算应先明确服务挂档模型、再定阈值、后算比例与复核，清洗不解除外发Gate。', '内部历史清洗记录，保留禁止客户可见边界；不复述被移出话术用于外宣，不确认实际四份源卡或合规通过。'),
105: ('L13-L22;L30-L41;L49-L84;L88-L114;L142-L173;L177-L201', '历史评估把服务分层、销售场景话术、价值奖金流向、产品卡改写及转介结构分案；分层结论带Conditional，价值/保费测算仍Amber，不能用一个Pass覆盖整个体系。Class C处理属于源内另列限制，产品卡改写后仍需复核。', 'Teresa于2026-07-17的内部意见，源称非法律意见；不验证GL25条款、产品类别或输出当前法律结论。'),
109: ('L7-L39', '确认保单数据归口、SaaS来源及周年月按生效日，并不等于承接完整OB-G7补源责任；source_absent指正式匿名汇总报告源缺，不代表没有保单数据或真实业务，数据owner不能代定指标、合规和外发。', '2026-07-20职责与业务口径确认记录；只分析责任边界，不实施字段派生或数据接入。'),
113: ('L13-L15;L46-L54;L76-L93', '历史意见支持把RW权益服务结算与JF佣金结算分开，并要求JF→RW服务费有独立定价及真实服务实质，不能只换名称；意见明确不覆盖JF本身义务、大陆TP路径和未来主体变化。', 'Teresa历史合规意见而非本批法律判断；不采纳“删除字段即可切断风险”的充分性推断，不验证迁移已实施或实体牌照状态。'),
117: ('L3-L17;L19-L55', '设立建议把短期境内供应商签约、人民币收付、发票需求，与长期AI服务承载主体分为两层目的，提出前海优先选址；这只是待审批草案，题头“最终优化完整版”不使其成为已批准方案。', '文件名07-20、正文修订日期07-31均保留；政策优惠、车牌、税率、奖补与可落地性不核验不采用为现实事实，未展开技术实现。'),
121: ('L3-L14;L33-L42;L55-L89;L101-L144;L160-L168', '核算草案将市场分类、细分、主体、经营板块、收入和成本六维分开；权益服务按验收与回款分离、扣直接交付成本，佣金线另核；共享成本与人力分别按收入和工时分摊，IFA及定价仍待补。', '2026-08-06财务草案，未被本批认作正式会计政策；不传播原文经营金额、毛利率或验证HKFRS结论。'),
125: ('L3-L17;L34-L63;L65-L81', 'REVIEW报告可作为治理证据但源文件不自动升级基线；阶段Gate分别控制范围、财务、合同、授权、运营与外宣，TOB/TOI配置或启动不等于TOC可交付，未满足时可降级为内部试点或模板。', 'Phase0历史状态快照；同文“核心TOC资料冻结”与“TOC后置”需按冻结用途区分，未替源修改口径。'),
129: ('L3-L10;L33-L72;L74-L80', '内部专家咨询方案将行政资讯、专业咨询、险企内嵌、保险事项和暂停项分路由；专业主体具名、独立委聘、场景隔离、客户授权与全链留痕共同构成上线条件，不能只看有无专家名单。', '2026-07-04内控底稿待签批；分类和Gate按源文历史方案总结，不将GL25引述或适用范围当当前法规结论。'),
133: ('L5-L19;L38-L52', '场景盘点把TOB合同范围、上架验收、机构培训、RACI和供应资源拆成运营证据任务，TOI区分价值证明、渠道背景、提案与缺失报表源；标题“已运营”不使目录命中或文件数变成当前业务验收。', '盘点报告自述；154文件112hash等未经本次再扫，不能据路径和关键词推定所引Office正文。'),
137: ('L3-L25;L100-L131', '正式汇总源须有期间、汇总维度、分子分母、来源、刷新、owner、匿名化、使用边界、批准及hash；有指标模板不等于存在数值源。报告写source_absent时仍允许框架设计，不允许冻结数值或外发。', '2026-07-04搜索结论限当时范围，后续S97已描述内部交付台账路径；未重做其214文件搜索。'),
141: ('L3-L38', '回写预备件称财务确认已交付但未合入冻结表，13confirmed、2不适用与1缺正式报表源分开；机械合并不等于签署，source_absent不应误记为财务owner未交付，16行对外承诺仍no。', '2026-07-15回写说明自述，不验证两CSV连接或替Roy/PMO将Gate转绿。'),
145: ('L3-L5;L13-L40', '15分钟站会逐项检查需求、范围、供应/SLA、合同、培训、执行、验收和内部价值证明证据，争议按业务/财务/合规升级；会议只更新证据和任务状态，不能现场冻结价格或放行外发。', '历史站会检查规则，不代表会议已召开或条目通过。'),
149: ('L5-L5;L11-L50', '需求确认的流程、SOP、收集表与确认模板只能提供可执行结构；真实机构需求、会议邮件签收、最终确认清单及触发的专业确认齐备后，才可能成为正式证据。', '历史收件箱复核结论；未验证六份文件存在或真实实例后来是否补齐。'),
153: ('L14-L30;L42-L59', '新增源池可改变补证路径：财务从单点等回复转为业务底账加财务确认，TOB从模板转真实活动实例，TOI从少量线索转候选案例池；扫描命中与候选增强仍不等于匿名正式报表源齐备。', '2026-07-05初步交叉比对自述；未扫描共享盘，不传播经营数字，不将其实体更正推广至S21的不同歧义。'),
157: ('L12-L36;L38-L60', '标准证据箱检查说明、流程、SOP、边界、台账、Gate与owner模板，真实案例包另可补轻量README/采用判定/脱敏记录；标准箱通过与真实案例证据化不是同一验收。', '2026-07-06验收报告自述；后续S141对财务等待状态有修正，不认定当前所有箱已通过。'),
161: ('L3-L5;L11-L31', '运营执行职责可下放而业务owner保留，候选岗位和人员必须经确认再回填RACI；把业务把控与日常运营分开可降低单点集中，建议分派效果不等于已完成分工。', '2026-07-07建议清单，未核实站会点名或人员实际承接，不转述人员能力评价。'),
165: ('L7-L18', '导航将TOI内部Current入口、TOC原始材料、内部草案和派生阅读视图区分；入口提供检索不改写源，TOC续签档案仍受客户上线Gate控制，汇总导航不产生发布权。', '2026-08-06README自述；未打开193或导航HTML，125实例不作为本次扫描统计。'),
}

def main():
    rows=json.loads(OUT.read_text())
    for r in rows:
        i=r['index']
        if i in NOTES:
            loc, note, boundary=NOTES[i]
            r.update(status='已分析',reason='依范围澄清，实际阅读可定位业务片段；内部治理、财务、历史合规主题不再按名称隔离',
                     locators=loc.split(';'),knowledge=[note],source_state=boundary,
                     semantic_review='最小业务片段核定；仅locators范围形成知识，不声称全文语义审查',
                     analysis_scope='business_excerpt_only',pending_parts=[])
        if i==21:
            r.update(status='待核',reason='最小正文复核仍见永明/永英实体混用；无法在不跟随引用的授权范围内消歧，仅隔离实体归属与具体执行，不因人员叙述名称隔离',
                     locators=['L1-L60'],semantic_review='本轮复核L1-L60；上轮已读L1-L90，剩余不声称语义核定',
                     analysis_scope='entity_conflict_only',knowledge=[],
                     partial_knowledge=['仅可识别源内提出入口分层、6至12个月制式培养和12个月后专业/组织双路径的培训设计；不归属具体保司，不作为已决策已执行事实。'],
                     pending_parts=[{'locators':['L1-L60'],'reason':'标题永明、信号1/2与business_line永英、信号3永明；实体未知，保留原字。'}],
                     source_state='AI会议总结，实体与执行事实未核定；不以高confidence标签代替证据')
        if r.get('recheck_reads'):
            # Re-read only to verify hash/stat and measure explicitly cited text spans.
            p=Path(r['path']); no_links(p); s=p.lstat()
            with os.fdopen(os.open(p,os.O_RDONLY|os.O_NOFOLLOW),'rb') as f:
                assert snapshot(s)==snapshot(os.fstat(f.fileno()))
                data=f.read(); endfd=os.fstat(f.fileno())
            no_links(p); end=p.lstat()
            assert snapshot(s)==snapshot(endfd)==snapshot(end)
            assert hashlib.sha256(data).hexdigest()==r['source_hash']
            lines=data.decode('utf-8-sig').splitlines(keepends=True)
            used=set()
            for loc in r['locators']:
                match=re.fullmatch(r'L(\d+)-L(\d+)',loc)
                assert match,loc
                lo,hi=map(int,match.groups()); assert 1<=lo<=hi<=len(lines)
                used.update(range(lo-1,hi))
            r['analyzed_excerpt_chars']=sum(len(lines[n]) for n in used) if r['status']=='已分析' else 0
            r['reviewed_locator_chars']=sum(len(lines[n]) for n in used)
            r['final_verification']=dict(stat_before=snapshot(s),stat_after=snapshot(end),stat_stable=True,source_hash=r['source_hash'],read_bytes=len(data))
        else:
            p=Path(r['path']); no_links(p)
            assert snapshot(p.lstat())==r['stat_after'], 'Previously analyzed source metadata changed'
            r['final_metadata_unchanged']=True

    by={r['index']:r for r in rows}
    by[5]['pending_parts']=[{'locators':['L29-L37'],'reason':'旧单迁移日期/星期及录入期限有不同表述，未统一校正。'}, {'locators':['L65以后'],'reason':'函数、AI及系统技术实现不在本轮业务片段分析范围；未展开。'}]
    by[17]['pending_parts']=[{'locators':['L28-L56','L118-L145'],'reason':'香港直签原则与内地对公例外并存，具体合同实体关系及最终适用路径仍待核，不替源认定合法性。'}]
    by[93]['pending_parts']=[{'locators':['L24-L31'],'reason':'DB、权限和入库技术实现只作为任务背景，不作实现分析或执行。'}]
    by[101]['pending_parts']=[{'locators':['L110-L120'],'reason':'未找到ILAS客户材料的历史搜索不能判断不存在或已剥离。'}, {'locators':['L124-L150'],'reason':'与S105的测算派工及前置顺序存在明确意见差异，本批不裁决。'}]
    by[105]['pending_parts']=[{'locators':['L55-L84','L142-L173','L192-L201'],'reason':'阈值/数值测算、价值奖金流向、转介结构和重审未在本文全部闭环；与S101派工意见差异保留。'}]
    by[113]['pending_parts']=[{'locators':['L60-L68'],'reason':'原意见以字段删除支持风险切断，本批不据此推导实质交易合法或现实风险已消除。'}]
    by[117]['pending_parts']=[{'locators':['L57以后'],'reason':'政策优惠、资格及车牌等不验证，不转作当前决策依据；本轮只核定设立的业务目的和草案状态。'}]
    by[121]['pending_parts']=[{'locators':['L160-L168'],'reason':'IFA细分、各主体数据、佣金基准和定价/固化仍待源内所列责任方确认。'}]
    for i,addition in {69:'补充交叉来源：S57 L91/L123-L125将本框架列为历史治理输入，不再仅凭本文件“当前执行”字样视为现行。',73:'补充交叉来源：S57 L122明确本v1.0已被替代。',65:'补充交叉来源：S57 L91-L125区分早期候选模型与后续登记的内部Current。'}.items():
        if addition not in by[i]['source_state']: by[i]['source_state']+=' '+addition
    assert len(rows)==46
    assert all(r['source_hash'] and r['reason'] for r in rows)
    assert all(r['knowledge'] and r['locators'] for r in rows if r['status']=='已分析')
    assert by[25]['source_hash']==by[29]['source_hash']
    OUT.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'total':len(rows),'counts':dict(Counter(r['status'] for r in rows)),
                      'rechecked':sum(bool(r.get('recheck_reads')) for r in rows),
                      'per_path_read_bytes':sum(r['read_bytes'] for r in rows),
                      'per_path_extracted_chars':sum(r['read_chars'] for r in rows),
                      'new_business_excerpt_chars':sum(r.get('analyzed_excerpt_chars',0) for r in rows)},ensure_ascii=False))

if __name__=='__main__': main()
