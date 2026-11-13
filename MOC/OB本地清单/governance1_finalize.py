import hashlib
import json
import os
import re
from collections import Counter
from pathlib import Path
from governance1_read import no_links, snap

BASE=Path(__file__).parent
OUT=BASE/'治理1_处置.json'
# Manual judgments grounded in displayed source passages, not keyword summaries.
ANALYZED={
10: ('L8-L31;L123-L156;L158-L187','四对象视图将主标签、辅标签和REVIEW分开；多标签复制不能形成多个独立证据，SHARED不应吸收所有商业背景，视图仅检索而非SSOT。源内分数阈值只是历史分流规则，不证明语义正确。','业务分类治理任务的必要段；不分析目录生成或评分算法，不执行任务书。'),
13: ('L3-L26;L28-L47','财务确认需按类型读：运营服务按项目核算、治理项不适用或内部管理，TOI报表源仍blocked，全部对外承诺仍no；财务回填不能自动解除客户外发、正式报告源或合同主体确认。','2026-07-08完成日报自述；标题“全部16确认”仅可理解为均有处置，不能覆盖表内13 confirmed、2不适用、1blocked。'),
19: ('L10-L25;L61-L71;L115-L122;L148-L180','重构计划把119原子作为目标范围、8个C包作为目标SKU、旧25簇保留迁移；存量/新建是来源状态，不等于已建成或获准外发。U080由旧度量定位改作目标交付能力，组合与下层组件不能按数量累加报价。','历史v3.3候选任务，不能从Ready for execution推导已经完成或现行有效；仅分析业务模型和状态分层，不处理工程实现。'),
22: ('L3-L24;L30-L37;L40-L53;L57-L80','机构流程复核区分历史参考和基线候选：合同范围、寻源、上架、交付蓝图、生命周期与RACI可提供补洞思路，但旧流程必须与当前权威版本和Owner对照；该报告自承工作簿仅结构/表头/关键行阅读，不足以证明冻结基线。','二级复核报告的历史业务观点；未读取所引Office，不接受路径或文件名独自证明内容正确。'),
25: ('L9-L11;L33-L42;L54-L85;L87-L103;L120-L128','交付物应按最终可观察成品、交接和验收本质分类：空白表不是真实执行凭证，课程含流程不自动变制度，问卷用于诊断不自动变报告；不确定项降置信并留精确缺口，原子层裁定不能直接覆盖每个组件。','历史定向语义任务；不运行标准化、修改ID或制造artifact，不把任务通过等同Current发布。'),
43: ('L3-L21;L119-L145','客户口径复核把版本树、客户承诺字段、图片源稿、候选MVP和旧版禁用分别处理；PDF导出与PPT源稿不独立计权，Final不是批准。复核报告自身只是治理证据，清洗后的客户材料仍需多方确认。','历史B5复核自述，未验证37原件及图片；同名详版关系不当作本批hash重复。'),
46: ('L3-L30;L32-L47;L60-L71','清洗需要唯一候选源稿和作废范围、可编辑图片源、服务次数/对象/触发条件/第三方/除外责任字段清单，以及内部术语和客户话术分栏；清洗完成仍是候选，不自动形成客户承诺或MVP正式字段。','历史执行清单，未执行任何源稿清洗或审批；实际物料可用性未核。'),
49: ('L3-L11;L25-L32;L48-L54','正式匿名汇总源应包含汇总维度、指标定义、期间、来源、刷新和Owner，且明确可用与禁用字段；搜索无结果应留source_absent和补源字段，不能用模板伪造数值或将结算内容转成价值承诺。','补源任务要求而非搜索结果，不声称当前有源或无源；不执行其Office搜索指令。'),
55: ('L3-L14;L16-L43','TOB运营证据可分批补：需求、方案排除项、供应/SLA、合同范围、培训、执行异常、验收分别收件，财务口径另归财务确认；站会检查已入箱、缺Owner/来源和升级阻塞，不直接冻结财务或外发。','2026-07-04补证任务，不把待补表当今天进度；保留草稿与正式证据的区别。'),
64: ('L3-L14;L16-L40','站会按九节点短报，真正需要停下的是风险和待决动作；出行B层SLA部分冻结不覆盖B4长期保留，合同模板残留第三方法人名称需签约前重写，RO接口确认不等于收款开票或客户外发批准。','2026-07-13议程中的完成/风险自述，未验证会议召开、SLA签署、机构身份、模板实际残留或Gate当前值。'),
70: ('L3-L30','25项服务形成卡片后，还需逐项确定首发范围、服务深度、预约时长地域、超时派单、供应覆盖、事故赔偿权限；招聘能力分为主责管家具备与资源池补齐，未确认不得上线。','v0.1定稿前业务问题清单，法律/授权/医疗和儿童资料问题仍只是待确认事项，不输出法律结论。'),
76: ('L3-L27','人才培养需把专业资质、公司许可、委任关系、续牌与持续进修分别管理，并与P0影随到P3主责的授权矩阵相配；牌照培训预算和费用、服务自营/外包划分、利益冲突及异常责任都需业务与HR运营共同确定。','v0.2候选确认清单；不判断具体动作是否触发牌照，不将优先专业锚点建议当已批准培养计划。'),
}
LOW={
1: ('L1-L75','文件仅复制/跳过计数和Office等路径索引；不能从路径产生业务知识，不跟随引用。'),
4: ('L1-L24','仅对话导出与文件复制回执，没有续签业务内容；不按目录名制造主题，也不执行记录里的文件操作。'),
7: ('L1-L49','TOC文件清单及复制数量，仅提供导航；不分析其引用业务资产，不计为hash重复。'),
16: ('L3-L19;L21-L60','早期SSOT落地验收回执；数量、渲染和镜像通过均为源自述，持续控制项未关闭。只供版本追溯，不重复生成产品模型知识。'),
28: ('L3-L24','仅一处血缘算术勘误：119+535+1020+754=2428，不能为原错数2528补造100行；保留勘误定位，不独立造原子。'),
37: ('L3-L44','索引扩展完成回执，仅称补hash及内部/audit边界；不证明候选材料获业务采用，不延伸技术分析。'),
52: ('L1-L35;L37-L62;L64-L92','并非纯空模板：预填启动结论和Owner，同时保留空确认栏、会后待补与占位人员；仅溯源，不将预填内容当真实会议决议。'),
58: ('L3-L34','共享底座候选映射及当时财务等待快照，规则与本批补证/字段主题重复，无独立新增业务原子；不是同hash重复。'),
61: ('L3-L39','24份工作副本物理归类回执；复制入箱不是业务采用或外发批准，只留来源组织与后续Owner确认线索。'),
67: ('L3-L19','架构图文件/视觉自验回执，未认证价格、供应商或法律审查；不重读图或造业务原子。'),
73: ('L3-L32','招聘稿文档及网页质检回执，描述环境字体限制和候选边界；排版通过不等于人力制度获批，仅溯源，不做渲染工程分析。'),
79: ('L3-L18','服务表结构化改写自验回执，保留旧版与候选状态；未核所引工作簿，不把公式无错当专业资源或对客批准。'),
82: ('L1-L7','简短角色确认清单，与本批服务上线确认主题相同但非字节重复；仅记录专业、供应资源、交付规格和品牌尚待确认，不另造原子。'),
}
TECH={
31: ('L3-L22;L24-L46;L78-L80','主体为工作簿整合依赖、机器验收与代表范围渲染的工程自验报告；只辨识类型及candidate边界，不分析实现或技术指标为业务知识。'),
34: ('L3-L42','正文明确仅数据/技术预备件：入库结构、权限检查、索引模板；按技术工程排除，不执行DB预设计。业务/合规/外发仍另需确认仅作为边界记录。'),
40: ('L3-L38;L40-L57','seed数据包与入库规则校验工程回执；不分析数据实现、不创建数据库、不把校验通过当真实入库或业务采用。'),
}

def main():
    rows=json.loads(OUT.read_text())
    assert {r['index'] for r in rows}==set(ANALYZED)|set(LOW)|set(TECH)
    for r in rows:
        i=r['index']; r.update(pending_parts=[],candidate_cards=[],published_at=None,allowed_use='内部历史分析/溯源；不构成现行批准、法律意见、客户承诺或技术执行授权')
        if i in ANALYZED:
            loc,k,boundary=ANALYZED[i]
            r.update(status='已分析',reason='已实际阅读必要业务治理片段并提取具体可追溯知识',knowledge=[k],source_state=boundary,analysis_scope='必要业务片段，不是全文件语义终审')
        elif i in LOW:
            loc,reason=LOW[i]
            r.update(status='低复用仅溯源',reason=reason,knowledge=[],source_state='导航/预填稿/执行回执/检查清单的历史自述',analysis_scope='类型与证据边界核定，不造原子')
        else:
            loc,reason=TECH[i]
            r.update(status='技术排除',reason=reason,knowledge=[],source_state='技术工程文档，仅识别与记录使用边界',analysis_scope='不作技术工程分析')
        r['locators']=loc.split(';')
        r['existing_analysis_check']={'scope':'MOC/OB批次/OB-LOCAL-RW-*.md 与现有RW业务主题检索','result':'未发现可认定本路径已完成同源分析的记录；相关主题不冒充同源关联'}
        p=Path(r['path']); no_links(p); before=p.lstat()
        assert snap(before)==r['first_stat']
        with os.fdopen(os.open(p,os.O_RDONLY|os.O_NOFOLLOW),'rb') as f:
            assert snap(os.fstat(f.fileno()))==snap(before)
            data=f.read(); afterfd=os.fstat(f.fileno())
        no_links(p); after=p.lstat()
        assert snap(before)==snap(afterfd)==snap(after)
        assert hashlib.sha256(data).hexdigest()==r['source_hash']
        lines=data.decode('utf-8-sig').splitlines(keepends=True)
        used=set()
        for loc in r['locators']:
            m=re.fullmatch(r'L(\d+)-L(\d+)',loc); assert m,loc
            lo,hi=map(int,m.groups()); assert 1<=lo<=hi<=len(lines)
            used.update(range(lo-1,hi))
        r['reviewed_locator_chars']=sum(len(lines[j]) for j in used)
        r['analyzed_excerpt_chars']=r['reviewed_locator_chars'] if r['status']=='已分析' else 0
        r['verification_read']=dict(stat_before=snap(before),stat_after=snap(after),stat_stable=True,sha256=r['source_hash'],read_bytes=len(data))
    by={r['index']:r for r in rows}
    by[1]['read_attempt_note']='首次读取已完成stat/hash计算但打印变量错误导致未持久化；16732字节读取后重试成功，未产生语义分析。read_events仅列成功持久化调用。'
    by[13]['pending_parts']=[{'locators':['L3-L5','L18-L26','L41-L46'],'status':'待核','reason':'全部确认/完成与blocked、not_applicable共存；本批只采用明细分层，不据标题证明Gate实际放行。'}]
    by[19]['pending_parts']=[{'locators':['L18-L25','L164-L174'],'status':'待核','reason':'与G16早期25SKU/度量层口径不同；仅记录版本目标变化，当前生效版本及批准链未跟随核验。'}]
    by[43]['pending_parts']=[{'locators':['L16-L21','L125-L130'],'status':'待核','reason':'PDF/PPT及详版关系是源报告陈述；本批未读这些源，不能按同名判字节重复或独立证据权重。'}]
    by[52]['pending_parts']=[{'locators':['L3-L6','L20-L35','L39-L54'],'status':'待核','reason':'07-04预填07-06纪要且含空确认栏；真实召开、最终参会与追认不能由本文件证明。MARK/Mark等是否同人不消歧。'}]
    by[64]['pending_parts']=[{'locators':['L8-L11','L22-L32','L34-L37'],'status':'待核','reason':'B4长期保留、PwC残留重写、对外清洗和报告源仍属源内未决；“三个闭环”不能覆盖这些例外。'}]
    by[70]['pending_parts']=[{'locators':['L3-L30'],'status':'待核','reason':'首发项目、供应覆盖、时效价格、授权和岗位资源仍为待确认项，不当作完成。'}]
    by[76]['pending_parts']=[{'locators':['L3-L27'],'status':'待核','reason':'动作触发牌照/许可、委任关系、培训预算和授权矩阵均未由本批确认。'}]
    assert len({r['source_hash'] for r in rows})==28
    assert all(r['window_ok'] and r['stat_stable'] for r in rows)
    OUT.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'total':len(rows),'counts':dict(Counter(r['status'] for r in rows)),
                      'per_path_bytes':sum(r['read_bytes'] for r in rows),
                      'per_path_extracted_chars':sum(r['read_chars'] for r in rows),
                      'analyzed_excerpt_chars':sum(r['analyzed_excerpt_chars'] for r in rows),
                      'pending_part_paths':[r['index'] for r in rows if r['pending_parts']]},ensure_ascii=False))

if __name__=='__main__': main()
