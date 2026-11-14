import json, os, stat, hashlib
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
from nonrw_model_ea import BASE, OUT, ROOTS, LOW, HIGH, check, snap

# Human-authored semantic judgments; no keyword-generated knowledge summaries.
NOTES = {
 'README_目录说明.md': ('治理识别已读', [[1,18],[125,139],[190,201]], 'G1', '正文给出D09 v2.24/v11执行入口及独立核验未完成；核定为有执行记录的在用业务项目，不等于全部数据投入生产。'),
 'D09_TeresaPMO_v11差异定向复核回执_20260914.md': ('治理识别已读', [[3,11],[44,52]], 'G1', '记录09-14差异复核及下一步提交Mark；明确同一助手实施与复核，不冒充独立人工审计，未发送、未登记Mark通过。'),
 'D09_Mark复验后当前未完成事项清单_v1_20260911.md': ('治理识别已读', [[1,24]], 'G1', 'v11清单仍列定向复核，随后同日回执明确补记完成；15条PARTIAL_SOURCE保留，不能重派已完成确认或称整批验收。'),
 'D09交付包形态与收口流程对齐说明_v1_20260830.md': ('已分析', [[10,54],[69,73]], 'T1', '七类交付内容可归集或指向共享材料，不要求105份新文档；定位精确到文件/页签，法律身份不拥有商业关系、场所、分销或牌照。原文是请求确认的历史方案。'),
 'D09主责协作指引_v1.0_20260826.md': ('已分析', [[15,65],[77,94],[132,147],[171,224]], 'T1', '按系统预填/完整台账/缺列台账/无台账/上游派生分流；无台账先签分母，未知不冒充不适用；来源绑定、标准化和数据内容分轴。'),
 'D09来源收口执行路径_v2.0_20260826.md': ('已分析', [[11,27],[66,89]], 'T1', '批次按键依赖而非整条数据完备链排列；既有数据用于预填但不继承完成标签。预填比例正文62%、表合计63%且分母说明不一，不能复用为统一完成率。'),
 'README_工作包规范.md': ('已分析', [[10,18],[50,82],[96,120],[124,139]], 'T1', '在途不等于定稿；12项最低内容已收敛为7类DOC，受控索引替代平行登记表；结构自查不等于外部独立核验。历史未封包状态不可覆盖后续记录。'),
 '[CONFIRM]_P03_partner_role角色定义_MOMO回岗复核_20260902.md': ('已分析', [[18,34]], 'T2', 'IFA角色依GTD/SLC、牌照挂接及其他上下文分别定义；角色语义确认不补齐Party锚、生命周期或协议真值。'),
 '[PMO_RECORD]_P04五合作场所确认责任与既有Amanda回执采用_20260908.md': ('已分析', [[8,31]], 'T2', '19项拆为11物理场所与8地域容器；合作非实控仍为真实场所，不能变成实控或地域容器。包负责人不能替实际业务责任人签署。'),
 'P05-MIN-EVIDENCE_派生标准与上游引用_20260902.md': ('已分析', [[4,16]], 'T2', '销售节点、KA实例和覆盖桥来自受控派生标准与上游，不存在独立原始业务台账；证明规则可追溯不等于实例已物化。'),
 '[SIGNED]_P05_MOMO回岗复核与电子签署回执_20260902.md': ('已分析', [[19,38]], 'T2', 'sales_node按角色×网络实体派生，KA按业务细分和母单元，覆盖依有效Partner-KA关系；签署保留五项例外及PILOT_PENDING。'),
 '[SIGNED]_P08_连亮晴_版本变化不影响产品身份_限定确认_20260907.md': ('已分析', [[8,40]], 'T3', '文件签署/缺口措辞改变不等于产品身份改变，但P10须重新绑定真实哈希；身份确认不证明费率条款或可售性。'),
 '[SIGNED]_P09_连亮晴_PGU身份规则产品含义确认_20260911.md': ('已分析', [[9,54],[61,89],[106,112]], 'T3', 'PGU以业务用途为身份锚，运营场景/客群/准入性质改变与名称或成员调整不同；明确不划不等于未知，禁止虚构PGU承载。单产品用途消失须考虑整体退役。'),
 'P10-MIN-EVIDENCE_ProductRoute派生与上游引用_20260902.md': ('已分析', [[4,13]], 'T4', 'Route无独立原始表，依P08/P09/P11/P12/P13受控输入派生；来源可查不代替组合与产品侧可售确认。'),
 'P10_supply_chain_id引用对象与版本规则_裁定说明_v1.0_20260911.md': ('已分析', [[6,23],[38,45],[59,59],[81,120]], 'T4', '开头补记明确采用S1具体供给安排，后文未批准仅历史；稳定Route身份与供给版本分开，不能用经纪合同、保司代码或文件哈希替供给身份；规则采用不证明安排实例存在。'),
 'P12_P10跨包边界确认意见_v1.0_20260907.md': ('已分析', [[8,43]], 'T4', 'MGA运营、培训、履约不证明产品授权/Binder或Route可售；旧签署中等待P12的文字保留历史，由新边界说明纠偏而非倒改签署。'),
 'P11_Teresa专业批准及增量预验收回执_20260911.md': ('已分析', [[3,24],[37,41]], 'T4', '批准限当期关系登记快照；关系存在不等于KA产品可售权，历史生效日空值不得用is_current补证；Mark签署仍空。'),
 '[REPLY]_P15_P16_财务材料采用范围_Roy确认_20260911.md': ('已分析', [[1,77]], 'T5', '按财务负责人明确页签/期间采用，不猜最后页签；保单号与订单号不足以唯一标识付款；原记录键与派生ID分开，历史研究及模板不等于现实损益。'),
 '[REPLY]_P15_P16_财务材料采用范围_Chaya确认_20260911.md': ('已分析', [[5,89]], 'T5', '按本人主体、页签、块和字段限定采用V6；中台入账依据不等于MYOB总账，副本不造新源；缺失月份及既往入账不同步保留，非全量财务真实性结论。'),
 '价值链L1建模_V0_待补清单.md': ('已分析', [[20,36],[52,76],[119,157]], 'T6', '正式价值链名称与战略飞轮内部简称分开；历史RSJD归属调整是当时裁定自述，不能只凭名称为当前节点重判。'),
 '价值流定义_ACC002_P4_价值流L3映射分析逻辑与标准_v1.1正式发布稿.md': ('已分析', [[18,37],[75,88]], 'T7', '02稿元数据published与正文未发布冲突；业务上区分单属外部价值流、被消费、内部能力，不能混用空值。后续03 v1.2已明确纠正发布表达。'),
 '价值流定义_ACC002_75码价值流差异与安全处置_v0.1.md': ('已分析', [[15,49],[70,81]], 'T7', '75码差异稿把57归属、12被消费、6拟内部能力显式分开；旧82与67+16不闭合，不能反推现行集合。数据库与脚本段不入知识。'),
 '价值流定义_ACC001_D1价值节点清单修订说明_v0.1.md': ('技术排除', [[1,12],[55,63]], None, '最小辨识发现主体为整改候选生成与工程验证；虽已整文件读取，不将测试通过/代码回归转作业务知识。'),
 '价值流定义_价值节点清单_消歧版_V4.0.md': ('混合范围隔离', [[18,38],[562,576]], None, '标题虽为价值节点，实质混有旧财务支付流程、工程实现与未经核实法规断言；此次读取范围过宽，整份不产主题原子，不能以目录名放行。'),
 '[VS-L3]_价值流-L3映射分析逻辑与标准_v1.2.md': ('已分析', [[24,69]], 'T7', '正文明确08-26发布并修复旧02措辞；五条外部旅程归属与横切消费分离，分类不代表流程成熟或数据库授权。仅作为该源发布自述。'),
 '[L1L3]_L1-L3映射分析逻辑与标准_v1.2.md': ('已分析', [[1,23],[34,98]], 'T6', '价值链5层节点、19能力与75注册流程分层；主归属唯一不妨碍多价值流消费；锁定架构不等于现实成熟，valid_until已过，当前续期未知。'),
}

def evidence(path, ranges, note):
    return {'path':str(path),'locators':[f'L{a}-L{b}' for a,b in ranges],'note':note}

def main():
    data=json.loads(OUT.read_text())
    reads={r['path']:r for r in data['reads']}
    queue_path=BASE/'项目入口队列.json'
    queue_raw=queue_path.read_bytes()
    queue=json.loads(queue_raw)
    old=[(i,x) for i,x in enumerate(queue) if any(x['path']==r or x['path'].startswith(r+'/') for r in ROOTS)]
    oldpaths={x['path'] for _,x in old}
    root_model=Path(ROOTS[0]); root_ea=Path(ROOTS[1])
    nodes={}; gaps=[]
    for root in (root_model,root_ea):
        check(root)
        for parent, dirs, files in os.walk(root,followlinks=False):
            p=Path(parent)
            for x in [p]+[p/n for n in dirs+files]:
                try:
                    s=x.lstat()
                    nodes[str(x)]={'path':str(x),'kind':'link' if stat.S_ISLNK(s.st_mode) else 'directory' if stat.S_ISDIR(s.st_mode) else 'file','mtime':s.st_mtime,'mtime_utc':datetime.fromtimestamp(s.st_mtime,timezone.utc).isoformat(),'stat':snap(s)}
                except OSError as exc:
                    nodes[str(x)]={'path':str(x),'kind':'unknown','stat_error':str(exc)}
            kept=[]
            for name in dirs:
                x=p/name; rel=x.relative_to(root)
                if name.startswith('.') or x.is_symlink():
                    gaps.append({'path':str(x),'kind':'隐藏或链接不展开','descendant_files':None,'requires_admission':False})
                elif root==root_ea and len(rel.parts)>=3 and not any(v in rel.parts for v in ('价值链L1建模','价值流建模')):
                    gaps.append({'path':str(x),'kind':'EA非价值链价值流子树不展开','descendant_files':None,'requires_admission':False})
                else: kept.append(name)
            dirs[:]=kept

    primary={}
    for path,r in reads.items():
        name=Path(path).name
        status,ranges,theme,note=NOTES[name]
        if '/D09P16_' in path and name.startswith('[REPLY]_P15_P16'):
            target=next(q for q in reads if '/D09P15_' in q and Path(q).name==name)
            assert r['source_hash']==reads[target]['source_hash']
            status='重复'; note='实际SHA256与P15路径完全一致；共享确认来源不重复造原子。'; r['duplicate_of']=target; ranges=[[1,6]]
        r.pop('token_proxy',None);r.pop('token_proxy_method',None)
        r.update(decision=status,status=status,reason=note,theme_id=theme,locators=[f'L{a}-L{b}' for a,b in ranges],semantic_reviewed_ranges=ranges,read_purpose='项目治理识别' if status=='治理识别已读' else '业务分析' if status=='已分析' else '类型辨识或去重',evidence=[evidence(path,ranges,note)],token_count=None)
        r['final_stat']=snap(check(path)); r['stable_at_finalize']=r['first_stat']==r['final_stat']
        assert r['stable_at_finalize'], path
        r['raw_read_chars']=r['read_chars']
        # This is an explicit evidence range, not a claim that all raw-read bytes were semantically reviewed.
        r['semantic_review_complete_file']=False
        primary[path]=r

    governance=[evidence(root_model/'README_目录说明.md',[[8,18],[135,139]],'在用业务项目的历史执行入口与PII边界'),evidence(root_model/'00_总控/07_分发与回收台账/D09_TeresaPMO_v11差异定向复核回执_20260914.md',[[3,11],[44,52]],'后续复核自述，不是独立验收')]
    def decide(n):
        p=Path(n['path']); rel=p.relative_to(root_model if str(p).startswith(ROOTS[0]) else root_ea); parts=rel.parts
        if str(p) in primary:return primary[str(p)]
        d=dict(n,source_hash=None,read_bytes=0,read_chars=0,token_count=None,locators=[],evidence=[],content_read=False)
        if n['kind']=='link': decision,reason='链接拒绝','lstat识别为链接，不跟随、不读正文'
        elif any(t.startswith('.') for t in parts): decision,reason='隐藏排除','隐藏入口仅元数据登记，目录不展开'
        elif n['kind']=='unknown':decision,reason='待核',n['stat_error']
        elif n['kind']=='directory':
            if str(p)==ROOTS[0]:decision,reason='在用业务项目准入','正文执行证据支持在用；PILOT_PENDING是数据内容轴，不等于整个项目实验'
            elif str(p)==ROOTS[1]:decision,reason='限定准入','用户仅授权价值链/价值流；其他EA正文不准入'
            elif str(p).startswith(ROOTS[0]):
                if parts[0]=='outputs':decision,reason='子树待核','README未赋予outputs权威位置；只列元数据，不能凭目录名认定在用或实验'
                elif any(t.startswith('D09P18_') for t in parts):decision,reason='敏感隔离','README L135-139明确包级PII与单独权限，未建立脱敏最小读取边界'
                else:decision,reason='业务分支准入','根README正文给出总控/标准/工作包/归档分工；准入不等于每文件已分析'
            elif any(t in parts for t in ('价值链L1建模','价值流建模')):decision,reason='限定业务分支准入','只允许价值链/价值流业务文本，工程验证和混合旧流程仍隔离'
            else:decision,reason='范围容器仅定位','EA只保留符合价值链价值流范围的具体子项；不凭此容器放行传统流程'
        elif str(p).startswith(ROOTS[1]) and not (any(t in parts for t in ('价值链L1建模','价值流建模')) or ('治理规范' in parts and any(k in p.name for k in ('[L1L3]','[VS-L3]','价值链','价值流')))):
            decision,reason='范围外不读','EA非已核定价值链/价值流业务正文；传统流程、岗位、规则分析、工程任务不展开分析'
        elif p.suffix.lower() not in ('.md','.html','.htm'):
            if p.suffix.lower() in ('.py','.mjs','.js','.ts','.sql','.yaml','.yml','.json','.jsonl'):
                decision,reason='工程或结构文件排除','类型门排除代码/配置/结构载体，未读内容也未为其计算内容hash'
            else:decision,reason='仅元数据引用','非MD/HTML；Office/PDF/图像/CSV/TXT均不解析正文、不计算内容hash'
        elif str(p).startswith(ROOTS[0]) and parts[0]=='outputs':decision,reason='归属待核','outputs未被治理入口明确纳入权威路径；不能由mtime或文件名决定实验/在用'
        elif any(t.startswith('D09P18_') for t in parts):decision,reason='敏感隔离','入口正文明确PII包级隔离，尚无脱敏片段边界，不读正文'
        elif '目标数据模型' in str(p):decision,reason='类型待核','README明确此分支含ER/主外键/字段实现，业务语义与技术工程混合；未读正文，不假作技术或业务分析'
        elif not LOW<=n['mtime']<HIGH:decision,reason='窗口外不读','项目和类型筛选后mtime不在固定首次窗口；不把mtime用作业务生效日'
        elif '映射验证_' in p.name or '项目文件夹结构与搭建指引' in p.name:decision,reason='技术排除','明确验证报告/部署搭建指引而非业务知识；正文未读'
        else:decision,reason='已准入待正文核定','项目归属及MD/HTML类型与mtime通过；本轮尚未实际语义阅读，不计已分析，不以关键词生成摘要'
        d.update(decision=decision,status=decision,reason=reason)
        if str(p).startswith(ROOTS[0]):d['evidence']=governance
        else:d['evidence']=[{'source':'用户本轮明确范围','note':'仅Desktop/流程架构项目_jasper的价值链价值流；旧传统流程不读正文'}]
        return d

    decisions={p:decide(n) for p,n in nodes.items()}
    assert set(reads)<=set(decisions)
    entries=[]
    for i,oldentry in old:
        d=decisions.get(oldentry['path'],{'path':oldentry['path'],'decision':'待核','reason':'旧路径当前不可见','evidence':[]})
        entries.append(dict(d,old_queue_index=i,old_decision=oldentry['decision'],old_queue_path=oldentry['path']))
    files=[d for p,d in sorted(decisions.items()) if nodes[p]['kind']!='directory']
    newdirs=[d for p,d in sorted(decisions.items()) if p not in oldpaths and nodes[p]['kind']=='directory']
    for d in files:d['is_new_discovery']=d['path'] not in oldpaths
    pending=[d['path'] for d in files if d['decision']=='已准入待正文核定']
    unresolved=[{'path':d['path'],'reason':d['reason'],'kind':d['decision']} for d in files if d['decision'] in ('归属待核','类型待核','敏感隔离','待核','混合范围隔离')]
    fq=json.loads((BASE/'文件准入队列.json').read_text())
    fq_local=[x for x in fq if any(x['path']==r or x['path'].startswith(r+'/') for r in ROOTS)]
    counts={'old_entry_total':len(entries),'old_entry_dispositions':dict(Counter(x['decision'] for x in entries)),
      'new_directory_total':len(newdirs),'known_file_total':len(files),'new_file_total':sum(d['is_new_discovery'] for d in files),
      'file_dispositions':dict(Counter(x['decision'] for x in files)),'old_file_queue_in_scope':len(fq_local),
      'known_admitted_file_queue_remaining':len(pending),'known_isolated_file_count':len(unresolved),
      'unadmitted_subtree_count':2,'unadmitted_subtrees_descendant_files_unknown':False,
      'unexpanded_subtree_count':len(gaps),'unexpanded_subtrees_descendant_file_count':None,
      'governance_identification_files':sum(r['decision']=='治理识别已读' for r in primary.values()),
      'business_analyzed_files':sum(r['decision']=='已分析' for r in primary.values()),
      'raw_read_files':len(primary),'raw_read_bytes':sum(r['read_bytes'] for r in primary.values()),'raw_read_chars':sum(r['read_chars'] for r in primary.values()),'token_count':None}
    result={'schema_version':'nonrw-admission-1.0','created_at':datetime.now(timezone.utc).isoformat(),'scope_roots':ROOTS,
      'window':{'start_inclusive':'2026-05-10T05:00:00Z','end_exclusive':'2026-11-11T06:00:00Z','mtime_bounds':[LOW,HIGH]},
      'queue_alignment':{'input':str(queue_path),'sha256':hashlib.sha256(queue_raw).hexdigest(),'total_shared_entries':len(queue),'scope_filter':'path == root or path starts root + slash','old_paths_covered_exactly':set(x['path'] for x in entries)==oldpaths,'no_shared_status_written':True},
      'project_state':{'业务模型':{'classification':'在用业务项目（源文历史执行证据）','evidence':governance,'production_acceptance':'未证明；Mark独立核验未完成；未判为整体实验项目'},'流程架构项目_jasper':{'classification':'价值链/价值流限定准入','current_applicability':'VS标准为源文发布自述；L1标准有效期已过，续期未知'}},
      'entry_decisions':entries,'new_entries':newdirs,'file_decisions':files,'counts':counts,
      'unresolved':unresolved,'file_queue_remaining':pending,
      'coverage_gaps':gaps+[{'path':str(root_model/'outputs'),'kind':'未准入权威归属子树','descendant_files':sum(p.startswith(str(root_model/'outputs')+'/') for p in [f['path'] for f in files]),'requires_admission':True},{'path':str(root_model/'20_工作包/D09P18_人员、组织、账户、权限、撤权与审计'),'kind':'明确PII包尚未建立脱敏读取边界','descendant_files':sum('/D09P18_' in f['path'] for f in files),'requires_admission':True}],
      'substantive_open_issues':['L1标准valid_until=2026-09-03，当前是否续期未知；不冒充现行规则','D09独立核验/实际发送未证明，PMO同助手复核不是独立审计','执行路径预填比例62%/63%及分母描述不一致，不自动算统一完成率','P15源付款组合键120/127唯一是历史源文自述，未验证余项或真实重复付款','混合价值节点文档不因目录名获准，技术和旧流程段不纳入主题'],
      'audit_notes':['实际token不可获得；只记录字节与字符，无token估算','raw_read为实际整文件读取/哈希字节，semantic_reviewed_ranges才是人工语义证据范围；输出截断部分不声称完整阅读','发现价值节点文档混合旧流程及技术段后隔离；早期整文读取范围过宽，不能声称所有读取均为最小业务片段','读取目录中发现的文件，不自动跟随正文引用；Office与服务器均未访问；未执行源代码/HTML','本轮入口逐项覆盖完成，不等于新增文件队列已全量分析；remaining数组保留真实未读工作量','独立核查尚未执行，主题为可追溯候选，不自授独立验收'],
      'reads':list(primary.values())}
    assert len({e['path'] for e in entries})==len(entries)
    assert sum(counts['file_dispositions'].values())==len(files)
    assert all(r['stable_at_finalize'] for r in primary.values())
    OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(counts,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
