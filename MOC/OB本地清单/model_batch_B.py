"""Bounded, local-only fragment review for the frozen B queue."""
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
from html.parser import HTMLParser

BASE = Path(__file__).resolve().parent
INPUT = BASE / '模型338续批冻结输入.json'
OUTPUT = BASE / '模型续批_B.json'
POLICY = BASE.parent / 'OB执行与独立核查协议_2026-11-10.md'

def sha(b):
    return hashlib.sha256(b).hexdigest()

def stamp(s):
    return dict(dev=s.st_dev, ino=s.st_ino, size=s.st_size,
                mtime_ns=s.st_mtime_ns, ctime_ns=s.st_ctime_ns,
                mtime_utc=dt.datetime.fromtimestamp(s.st_mtime, dt.timezone.utc).isoformat())

class Visible(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.lines = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        hidden = (tag in {'script', 'style', 'template', 'noscript', 'head'} or
                  'hidden' in a or a.get('aria-hidden') == 'true' or
                  re.search(r'display\s*:\s*none|visibility\s*:\s*hidden', a.get('style', '')))
        if tag not in {'meta','link','br','hr','img','input','source','wbr'}:
            self.stack.append((tag, bool(hidden)))
    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break
    def handle_data(self, data):
        if not any(x[1] for x in self.stack) and data.strip():
            self.lines.append((self.getpos()[0], data.strip()))

def display_md(raw, start_line):
    lines = []
    fenced = False
    comment = False
    for i, line in enumerate(raw.decode('utf-8').splitlines(), start_line):
        if line.lstrip().startswith(('```', '~~~')):
            fenced = not fenced
            continue
        if '<!--' in line:
            comment = True
        if '-->' in line:
            comment = False
            continue
        if not fenced and not comment and line.strip():
            lines.append((i, line))
    return lines

def fragment(record, offset=0, cap=2800, start_line=1):
    p = Path(record['path'])
    before = stamp(p.stat())
    # Every read is independently gated, including supplements.
    assert 1778389200000000000 <= before['mtime_ns'] < 1794376800000000000
    assert p.suffix.lower() in {'.md', '.html', '.htm'}
    assert not p.is_symlink()
    with p.open('rb') as f:
        f.seek(offset)
        fetched = f.read(cap)
    raw = fetched if offset + len(fetched) == before['size'] else fetched[:fetched.rfind(b'\n')+1]
    after = stamp(p.stat())
    if p.suffix.lower() in {'.html', '.htm'}:
        parser = Visible()
        parser.feed(raw.decode('utf-8'))
        visible = parser.lines
    else:
        visible = display_md(raw, start_line)
    frag = dict(byte_range_half_open=[offset, offset+len(raw)],
                line_range=[start_line,start_line+raw.count(b'\n')+int(bool(raw) and not raw.endswith(b'\n'))-1],
                sha256=sha(raw), hash_scope='exact raw bytes in byte_range_half_open',
                fetched_bytes=len(fetched), retained_bytes=len(raw),
                visible_chars=sum(len(t) for _,t in visible),
                visible_lines=visible, stat_before=before, stat_after=after,
                stable=before == after)
    record['fragments'].append(frag)
    record['read_bytes'] += len(fetched)
    record['read_chars'] += frag['visible_chars']
    record['content_read'] = bool(visible)
    record['stability'] = 'stable' if all(f['stable'] for f in record['fragments']) and before == record['stat_before'] else 'changed_pending_review'
    record['stat_after'] = after
    return frag

def save(data):
    OUTPUT.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def init():
    raw = INPUT.read_bytes()
    frozen = json.loads(raw)
    queue = frozen['groups']['B']
    assert len(queue) == 107 and len({r['path'] for r in queue}) == 107
    data = dict(schema_version='model-B-1.0', batch_id='模型338续批_B',
                created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                frozen_input=str(INPUT), frozen_input_sha256=sha(raw),
                governance=dict(protocol=str(POLICY), protocol_sha256=sha(POLICY.read_bytes()),
                                project_state=frozen['project_state']),
                window=frozen['window'], independent_review='pending_not_self_certified',
                file_decisions=[])
    for i, old in enumerate(queue,1):
        p = Path(old['path'])
        assert '/业务模型/00_总控/' in str(p) or '/业务模型/10_标准与基线/' in str(p)
        r = dict(id=f'B{i:03}', path=str(p), baseline_mtime=old['mtime_utc'],
                 baseline_stat=old['stat'], source_hash=None, content_read=False,
                 business_analyzed=False, read_bytes=0, read_chars=0, token_count=None,
                 fragments=[], status='片段待语义复核', reason='', stability='not_read')
        if i in {9,27}:
            r.update(type_screen='工程技术排除', status='技术排除_未读正文',
                     reason='双发布引擎handoff/执行单属于软件发布工程；仅按文件类型定位排除，不分析技术正文')
        else:
            r['type_screen'] = 'MD/HTML业务治理候选；先按路径文档类型复筛，片段继续甄别混合内容'
        try:
            s = p.lstat()
            r['stat_before'] = stamp(s)
            r['mtime_utc'] = r['stat_before']['mtime_utc']
            r['baseline_stability'] = ('matches_with_serialization_tolerance' if
                s.st_size == old['stat']['size'] and abs(s.st_mtime_ns-old['stat']['mtime_ns']) <= 1000
                and s.st_ino == old['stat']['ino'] else 'changed_since_frozen_queue')
            if stat.S_ISLNK(s.st_mode) or not stat.S_ISREG(s.st_mode):
                r.update(status='类型隔离_未读正文',reason='非普通文件或符号链接，不跟随')
            elif not 1778389200000000000 <= s.st_mtime_ns < 1794376800000000000:
                r.update(status='窗口外_未读正文',reason='首次本轮mtime不在固定半开窗口内')
            elif p.suffix.lower() not in {'.md','.html','.htm'}:
                r.update(status='类型排除_未读正文',reason='非MD/HTML；Office/JSON等源不解析')
            elif r['baseline_stability'] != 'matches_with_serialization_tolerance':
                r.update(status='源变更待复核_未读正文',reason='与冻结队列元数据不一致，不自动晋升')
            elif i not in {9,27}:
                fragment(r, cap=18000 if p.suffix == '.html' else 2800)
            r['stat_after'] = stamp(p.stat())
            if not r['fragments']:
                r['stability'] = 'metadata_stable_body_unread' if r['stat_before'] == r['stat_after'] else 'changed_pending_review'
        except (OSError, AssertionError, UnicodeError) as e:
            r.update(status='读取受阻待复核',reason=str(e))
        data['file_decisions'].append(r)
    save(data)
    print(json.dumps(dict(total=len(data['file_decisions']),read=sum(r['content_read'] for r in data['file_decisions']),bytes=sum(r['read_bytes'] for r in data['file_decisions'])),ensure_ascii=False))

def show(start, end):
    data = json.loads(OUTPUT.read_text())
    seen = {}
    for r in data['file_decisions']:
        if not start <= int(r['id'][1:]) <= end:
            continue
        print('\n###',r['id'],r['path'].split('/业务模型/')[1],r['status'])
        for f in r['fragments']:
            if f['sha256'] in seen:
                print('相同片段:',seen[f['sha256']])
            else:
                print('\n'.join(f'L{n}: {t}' for n,t in f['visible_lines']))
                seen[f['sha256']] = r['id']

# Human-reviewed dispositions, not keyword-generated summaries. Ranges refer only
# to business prose actually exposed for review; excluded payloads never qualify.
REVIEW = {
1: ('A','T01','总控表将来源扫描与验收分开；3/18等仅2026-08-21源文快照，不作当前状态','7-29'),
2: ('S','','定位到公司法定登记标识和逐主体名单；本轮保守隔离，不摄入登记明细或据此确认主体资格','1-24'),
3: ('M','','主体关系业务与生产库结构核验混合；识别片段后停止，不分析生产聚合数据或工程结论','1-16'),
4: ('M','','产品业务与生产表、代理键及结构检查混合；识别后停止，不据工程结果形成产品事实','1-13'),
5: ('A','T03','联合任务单区分转介、服务、产品授权及牌照权限，受控材料不意味着业务激活','3-29;40-54'),
6: ('A','T04','任务单明确事件、费率、应付实付与损益不能替代；PACK_COMPLETE不等于验真','3-30;48-50'),
7: ('A','T05','合规权限任务区分KYC签署事件和适当性通过；岗位、账户、动作与专业责任需分开','3-31;48-48'),
8: ('L','','交付副本阅读入口与2026-08-22快照说明，低复用；仅溯源，不另立SSOT','3-5;55-61'),
9: ('T','','文件名明确insight_engine_dual_publish_handoff：软件引擎双发布交接工程，正文未读；不为hash打开',''),
10: ('D','','与B001已读原始前缀逐字节hash相同；只归并相同片段，未证整文件相同','1-36'),
11: ('L','','字典层确认回执仅作历史自述溯源；不确认回执签名、生产发布或实际生效','1-6;30-39'),
12: ('M','','正文定位为TECHNICAL_READBACK_PASS及三方引擎回读候选，工程与治理混合；停止业务分析','1-17'),
13: ('A','T04','历史裁决区分服务框架与已签计价事实、双边生效证据；不复核合同或采用争议金额','3-21;29-31'),
14: ('S','','与B002识别片段相同，含法定登记标识；保守隔离，不因副本重复而摄入主体明细','1-24'),
15: ('M','','预扫描主要为生产表聚合和字段缺口技术核对；仅类型识别，不作主体核验或技术分析','1-11;30-42'),
16: ('A','T02','身份规则裁定保留稳定身份与独立资格/法域/角色版本；正文明确未验证全部主体','3-16;33-39'),
17: ('D','','与B003已读片段hash相同，继承混合隔离，不分析副本或声称全文重复','1-16'),
18: ('A','T02','历史线下规格区分母单元、细分桥及九要素评估主体；线下确认不等于自动放行','3-7;24-47'),
19: ('D','','与B004已读片段hash相同，继承混合隔离；不重复提炼生产统计','1-13'),
20: ('A','T03','只提炼五类业务证据不能相互替代的历史边界；合同/PDF/牌照引用未读且未经本轮核实','3-6;28-32'),
21: ('D','','与B005已读片段hash相同，归并授权业务主题；无独立新增分析','1-56'),
22: ('A','T04','仅采用文内财务分层控制原则，不采用生产数值；来源存在和沙箱运行不等于生产闭环','6-7;17-17;30-30'),
23: ('D','','与B006已读片段hash相同，归并财务边界；未校验未读尾部','1-54'),
24: ('A','T05','仅提炼隐私及场景适用边界，纯内部不适用也须有依据，不能由空值或事件量推定通过','6-7;30-36'),
25: ('D','','与B007已读片段hash相同，归并权限合规主题；不算新业务分析','1-55'),
26: ('A','T01','基线关闭规则禁止以测试/字段/口头确认替代来源验真，新增要求须独立变更批准','3-10;24-34'),
27: ('T','','文件名明确insight-engine双发布执行单：软件引擎发布工程；正文未读，不为hash打开',''),
28: ('M','','数据中台数字标准、系统表/API和业务治理混合；仅识别后停止，不摄入工程建设规范','3-30'),
29: ('M','','正文是物理对象/API/发布环境执行模板，业务分类与系统发布混合；空发布栏非发布事实','3-7;33-47'),
30: ('M','','文内三方生产回读、SQL和引擎校验混合；识别后停止，不分析或复算工程结果','3-19'),
31: ('D','','与B028已读片段hash相同，继承中台工程混合隔离，不声称全文已分析','1-30'),
32: ('A','T01','统一验收明确来源/标准检查与全量真实数据、经营损益、正式运营分界；审查非Mark签署','3-28'),
33: ('L','','逐包审查意见依赖未读Office及专业记录；本轮只保留审查定位，不重判包级验收','1-15'),
34: ('L','','路径与Office哈希清单，低复用，仅溯源；文内哈希未对被引Office复算','1-9'),
35: ('A','T06','P14历史主责变更明确交易事实、数据治理与财务期间分工；旧决定保留，不作为现任名单','3-20;33-38'),
36: ('A','T06','P02专业授权按主体×法律角色×有效期间限定；Mark知会Note为非阻断监督，不跨专业代签','3-25;36-50'),
37: ('A','T06','历史统筹方案区分唯一接口与多专业确认人；后续主责变更另行串联，不照抄旧人名执行','3-6;14-24;45-58'),
38: ('A','T06','临时代收口与正式唯一主责分开；临时替代不自动改永久责任','3-13;24-41'),
39: ('A','T03 T06','P12范围裁定将永明TA与联合运营分子域，合同服务证据不代替P11可售权或P13监管权限','3-45'),
40: ('A','T06','P14主责变更仅改变整包统筹，不扩大为全量数据、佣金或P&L验收；专业判断仍分开','3-31;37-43'),
41: ('A','T06','P15正式主责替代临时代收口，但来源Owner、保管人及专业确认人不随包级主责机械改写','3-45'),
42: ('L','','每日数字看板为2026-08-29进度快照，数字和完成标志仅文内声称，低复用仅溯源','3-18'),
43: ('L','','2026-08-30看板与后续人员更新混时点，不能按mtime推定全部数字当前有效；仅溯源','3-18'),
44: ('L','','仅读取HTML可见项目总览，脚本样式隐藏内容排除；进度比例为静态历史自述，不分析实时交付','30-57;85-102'),
45: ('A','T01','进度台账明确草案、来源Owner确认、专业签署与独立核验分开；不采用历史完成比例','3-9;17-23'),
46: ('L','','进度表为空白/历史投影并引用旧JSON真源，后续指引已降级该真源；仅保留历史定位','3-7;20-25'),
47: ('A','T07 T04','归属调整建议明确不是裁定；经济义务/结算腿与期间核算分层，采用证据另见B050','3-20;27-41'),
48: ('A','T07','需求粒度为实名提交人可定位的最小事实单元；来源线索及证据副本不能冒充真实来源','3-33'),
49: ('A','T07','需求增量保持原ID及标题；范围扩充、提法变更、新增、关闭、降级分别登记，不能自批关闭','3-5;26-46;57-57'),
50: ('A','T07 T04','后续补丁正文称采纳归属调整但不新增/关闭需求；派生来源与工作包责任不能混为一列','3-20;24-49'),
51: ('A','T06 T07','原始来源行与后续包级责任覆盖分开，预填非确认，候选降级须裁定；不把快照状态当前化','3-8;41-44'),
52: ('M','','对象/字段机器比对与业务作业权威混合；只作类型识别，不分析工程建模差异','3-16;20-37'),
53: ('L','','单纯Office基线SHA清单，低复用仅溯源；被引文件未打开，列示hash不是本轮实算','1-10'),
54: ('L','','交Mark核验准备清单，不是实际送达或Mark验收；下游Office未读，历史交付只溯源','1-10'),
55: ('L','','范围受限签署登记回执，仅记录历史声称和限制，不验证电子确认人或升级状态','3-24'),
56: ('L','','历史目录迁移执行记录，不核实移动结果；FINAL_PACKAGE字样不证明当前正式交付','3-5;37-42'),
57: ('L','','目录整理日志含技术清理与迁移自述，低复用，仅定位其旧JSON降历史的文本，不执行整理动作','3-7;42-49'),
58: ('A','T01 T07','项目计划区分来源节点与完整交付，先范围与分母再身份版本再取料；历史执行比例不作当前事实','3-11;26-33'),
59: ('A','T07','待裁定判据区分列语义/枚举不明、范围可能变化、纯改名和已有数据整改；治理复用而非实施字段','3-22'),
60: ('M','','字段增删/结构落地与业务裁定混合，停止工程分析；文内硬阻塞清零不作实际发布或专业签署证明','3-26'),
61: ('L','','归档增量派单与未读Office定位，历史任务只溯源，不重派完成动作或代签','3-20'),
62: ('L','','归档待办快照，已含多次日期更新和状态自述；不将旧待办恢复为当前任务','1-14'),
63: ('L','','归档README入口快照，所称当前版本仅历史定位，不跟随Office/JSON引用','1-17'),
64: ('L','','归档S1待办视图，预验收/送Mark与例外仍分开；低复用，仅溯源不刷新状态','3-24'),
65: ('L','','归档v10入口，与后续v11入口有明确版本差异；不按同名README自动覆盖','1-17'),
66: ('L','','派单记录仅说明PMO/数据治理职责与当时任务，未读所链工作包，不称任务执行已核实','3-12'),
67: ('A','T01 T04','六组计划明确机械封包一致非整批验收，部分来源不为清零晋升，实际金额/全量对账仍后置','3-20'),
68: ('A','T04','财务范围受限预验收只能带明确例外送审，不确认真实金额、全期间核销及整包闭环','3-17'),
69: ('M','','路径/公式/哈希重绑工程执行与状态治理混合；最小定位后停止，不分析技术修正','3-18'),
70: ('A','T03 T08','只采用S1范围说明：新增四分类未采用，不成为门槛；路由身份不变，执行回写不等于验收','3-9'),
71: ('A','T04 T08','核对意见说明字节一致非内容成立，财务例外按覆盖拆分，高权批准不能被代理；不采技术检查数字','3-15'),
72: ('L','','基线确认和派单自述，不代表六组实质工作完成；只定位历史协作入口','3-9;16-20'),
73: ('A','T01','源文明示同一助手代执行再PMO复核，不冒充独立人工；通过仅S1增量，整批与真实数据未通过','3-13'),
74: ('M','','哈希/公式/字段回写封包变更表，工程与业务状态混合；停止分析，只留识别片段指纹','1-5'),
75: ('M','','公式修复、Office字节变化及封包清单，工程混合；不验证哈希变化成因，不做业务分析','1-14'),
76: ('L','','v10封包历史快照，未建表未造真实ID未发送的自述仅溯源；不据哈希清单认定验收','1-23'),
77: ('L','','v11封包正文给出v10继承关系和D09 v2.24，作为版本定位；未核实Office或验收','1-13'),
78: ('M','','v3工程封包增量、上游哈希重绑与PMO记录混合，停止分析；不采完成声明','1-5;15-25'),
79: ('M','','v4工程字段及哈希修正记录，混合类型识别即止，不复算或判断完成','1-21'),
80: ('M','','v5技术遗漏修复/字典单元格回写与业务规则混合，不作业务知识依据','1-20'),
81: ('M','','v6建模、逻辑对象和封包哈希混合，停止分析；例外关闭自述不晋升','1-24'),
82: ('M','','v7字段族/依赖/封包修正与例外拆分混合，仅溯源，不分析工程实现','1-22'),
83: ('M','','v8字段取值/版本绑定与封包技术变更混合，不把初拟值域当批准基线','1-20'),
84: ('M','','v9表头重生/判重及日志工程变更混合，仅类型识别，完成自述不视为执行验证','1-19'),
85: ('A','T08','预验收退回单列出同文件规则/状态冲突；返修应定点处理而非重做证据或重复追签','3-27'),
86: ('L','','共同回执只有Carrie部分，Teresa栏留空；仅历史溯源，不称共同预验收完成','1-23'),
87: ('M','','逐单元格原值新值、公式与版本工程修正混合，识别后停止，不采执行完成结论','1-16'),
88: ('L','','UA版本与Office SHA清单v1，低复用仅溯源；未读附件不验证声明哈希','1-10'),
89: ('L','','UA版本与Office SHA清单v2，历史封包索引，不以清单/公式自述判定交付成立','1-9;31-31'),
90: ('A','T08','仅提炼授权代执行、旧新版本及原回执范围不倒改边界；不分析工作簿技术改动或认定已验收','3-7;18-20'),
91: ('A','T01','数据结果、局部预填、来源规则回填分三类，文件名已回填不证明业务数据完成；不采用历史数量','3-15'),
92: ('A','T08','追加历史与阅读投影来自同一事实，实际执行/发送/回读分开，缺旧快照不得造差异或旧hash','3-13;19-32'),
93: ('L','','待发送说明兼含渠道故障细节，识别后不分析技术信息；仅保留待发送非送达性质','1-3;21-23'),
94: ('L','','可用业务文字只有协作回读性质，主要载荷在代码围栏中按协议排除；不称空回执或已核实回读','1-3;32-32'),
95: ('L','','资料合并与引用勘误完成自述，专业待签和实际P&L仍未确认；低复用仅溯源','3-4;23-29'),
96: ('L','','回复草稿与安排，不证明已发送/收件/完成；不跟随其文件清单','1-16;26-28'),
97: ('A','T07','初步识别区分真实来源与证据副本；不能从来源类别猜目录，历史PASS不代表本轮验收','3-15'),
98: ('L','','就绪报告只是提交条件自述，非独立核验通过；历史包数量不作为当前业务事实','3-23'),
99: ('L','','日总结属回填/进度自述，明确预填非来源确认；不将汇报数量当验证','3-27'),
100: ('L','','日总结/待办历史快照，未跟随专业回执，不据完成措辞晋升签署或验收','1-20'),
101: ('L','','收盘总结含完成与日期覆盖自述，低复用，仅保留定位，不核实回执数量及样本','1-4;27-50'),
102: ('L','','修正完成回收位置清单，仍列专业待确认；仅历史线索，不重开或关闭任务','1-8;17-28'),
103: ('M','','P06 binding落库/seed与发布时点工程待裁定单；识别后停止，不分析部署或解除RELEASE_HOLD','1-13'),
104: ('L','','归档团队指引与B106同主题但入口不同；不声称全文重复，仅历史版本溯源','1-13;35-51'),
105: ('M','','归档作业指引混合旧JSON投影与工程回读语境；识别后停止，入口已被后续明确降历史','1-17'),
106: ('A','T01 T06','团队业务指引界定来源责任/位置/版本及单总表多回执，敏感原件不汇集；旧任务节奏非现行派单','1-2;17-25;35-80;82-107;122-122'),
107: ('M','','首段按治理指引识别，定点补读发现生产表统计、引擎回读与业务方法混合后停止；不作业务主题依据、不全读取hash','1-40;46-74;128-148'),
}

def finalize():
    data=json.loads(OUTPUT.read_text())
    assert set(REVIEW)==set(range(1,108))
    assert sha(INPUT.read_bytes())==data['frozen_input_sha256']
    statuses={'A':'业务片段已分析_候选','L':'低复用仅溯源_未作业务分析',
              'M':'工程混合隔离_仅类型识别','T':'技术排除_未读正文',
              'S':'敏感标识隔离_未作业务分析','D':'重复片段仅溯源_未新增分析'}
    records=data.pop('file_decisions')
    seen={}
    for r in records:
        i=int(r['id'][1:])
        mode,topic,reason,ranges=REVIEW[i]
        r['status']=statuses[mode]
        r['reason']=reason
        r['type_screen_final']={'A':'业务治理正文','L':'低复用业务过程/索引','M':'工程或工程业务混合','T':'工程技术','S':'保守敏感隔离','D':'片段重复，继承代表路径的类型边界'}[mode]
        r['business_analyzed']=mode=='A'
        r['analysis_scope']='仅列示必要业务片段；不是全文分析' if mode=='A' else '未作业务分析'
        r['themes']=topic.split()
        r['semantic_locators']=['L'+s.replace('-','-L') for s in ranges.split(';') if s]
        r['locators']=[f"L{f['line_range'][0]}-L{f['line_range'][1]}; bytes[{f['byte_range_half_open'][0]},{f['byte_range_half_open'][1]})" for f in r['fragments']]
        r['business_date_evidence']=[]
        for f in r['fragments']:
            for line,text in f['visible_lines']:
                if line<=12 and re.search(r'日期|时间|更新|基准|基线日期|发布日|裁定日|生效日|生成|打包',text):
                    dates=re.findall(r'20\d{2}[-/]\d{2}[-/]\d{2}(?:[ T]\d{2}:\d{2}(?::\d{2})?)?',text)
                    if dates:
                        r['business_date_evidence'].append(dict(locator=f'L{line}',values=list(dict.fromkeys(dates)),scope='源文历史日期，不是mtime或现行生效证明'))
        r['date_caution']='未出现独立业务日期时保留未知，不从文件名或mtime推定'
        r['duplicate_fragments']=[]
        for f in r['fragments']:
            key=(tuple(f['byte_range_half_open']),f['sha256'])
            if key in seen:
                r['duplicate_fragments'].append(dict(representative=seen[key],sha256=f['sha256'],scope='仅此原始字节片段相同，非整文件重复'))
            else:
                seen[key]=r['id']
            # Do not persist company registration lists, technical dumps, or
            # unnecessary copied prose. Fingerprints and ranges suffice.
            f.pop('visible_lines')
        r['stat_final']=stamp(Path(r['path']).stat())
        if r['stat_final'] != r['stat_before']:
            r.update(stability='changed_pending_review',status='源变更待复核',business_analyzed=False,themes=[])
        else:
            r['stability']='stable_pre_post_final' if r['fragments'] else 'metadata_stable_body_unread'
        r['evidence_level']='源文自述/历史设计；非现行执行或独立验收'
        r['source_hash']=None
        r['hash_policy']='未全文件读hash；仅fragments内已读原始片段SHA-256；未读项无hash'
    from collections import Counter
    counts=Counter(r['status'] for r in records)
    data['records']=records
    data['counts']=dict(expected=107,processed=len(records),unique_paths=len({r['path'] for r in records}),
                        missing=0,duplicate_paths=0,by_status=dict(counts),
                        business_analyzed=sum(r['business_analyzed'] for r in records),
                        content_read_files=sum(r['content_read'] for r in records),
                        unread_files=sum(not r['content_read'] for r in records),
                        duplicate_fragment_paths=sum(bool(r['duplicate_fragments']) for r in records),
                        changed_sources=sum(r['stability']=='changed_pending_review' for r in records))
    data['read_metrics']=dict(source_file_reads=sum(len(r['fragments']) for r in records),
                            read_bytes=sum(r['read_bytes'] for r in records),
                            read_chars=sum(r['read_chars'] for r in records),
                            hashed_fragment_bytes=sum(f['retained_bytes'] for r in records for f in r['fragments']),
                            token_count=None,token_estimate=None,
                            byte_definition='实际从业务MD/HTML读取的原始字节，包括解析时剔除的代码/样式及末行截断；补读重叠尾部按实际读取计入',
                            char_definition='业务MD/HTML抽取的非空可见文本字符数，包含类型识别/隔离片段，不等于已分析字符；代码围栏及HTML脚本样式隐藏区不计',
                            full_file_hash_reads=0,
                            administrative_inputs='协议、原核定JSON的project_state与队列元数据、冻结输入及本轮输出复查另计为治理读取，不计业务源读量')
    data['boundaries']=dict(local_only=True,server_reads=0,office_source_reads=0,json_business_source_reads=0,
                           rw_pending_17_touched=False,source_writes=0,unified_ledger_writes=0,
                           references_followed=False,production_acceptance=False,
                           note='只读冻结B队列的MD/HTML必要片段。工程/混合/敏感识别片段不进入主题知识；完成自述不视为执行。')
    data['verification']=dict(scope='执行者自检，非独立核查',queue_coverage='107/107 exact path set',
                              input_hash_unchanged=True,all_required_fields=True,
                              sole_next_step='主线程按冻结338全集合并并做独立核查；本批不自行晋升统一清单')
    # JSON numbers cannot faithfully carry nanoseconds in JavaScript consumers.
    def string_times(obj):
        if isinstance(obj,dict):
            return {k:str(v) if k.endswith('_ns') and isinstance(v,int) else string_times(v) for k,v in obj.items()}
        if isinstance(obj,list):
            return [string_times(v) for v in obj]
        return obj
    save(string_times(data))
    print(json.dumps(dict(counts=data['counts'],read_metrics=data['read_metrics']),ensure_ascii=False,indent=2))

def verify_and_index():
    data=json.loads(OUTPUT.read_text())
    frozen=json.loads(INPUT.read_bytes())
    records=data['records']
    # These EOF lines were displayed in the original review. The initial line
    # counter omitted the last line of files without a trailing newline.
    for r in records:
        if r['id'] in {'B086','B089'}:
            final_line={'B086':23,'B089':31}[r['id']]
            r['fragments'][-1]['line_range'][1]=final_line
            r['locators']=[f"L{f['line_range'][0]}-L{f['line_range'][1]}; bytes[{f['byte_range_half_open'][0]},{f['byte_range_half_open'][1]})" for f in r['fragments']]
    data['verification']['locator_correction']='B086/B089原末行无换行；依据已显示片段修正终止行号，不新增源读取'
    expected={r['path'] for r in frozen['groups']['B']}
    assert len(records)==107 and {r['path'] for r in records}==expected
    assert len({r['path'] for r in records})==107
    assert sha(INPUT.read_bytes())==data['frozen_input_sha256']
    errors=[]
    for r in records:
        assert all(k in r for k in ('path','status','reason','locators','read_chars','read_bytes','stability'))
        for stat_key in ('stat_before','stat_after','stat_final','baseline_stat'):
            assert isinstance(r[stat_key]['mtime_ns'],str)
            assert isinstance(r[stat_key]['ctime_ns'],str)
        s=stamp(Path(r['path']).stat())
        assert str(s['mtime_ns'])==r['stat_before']['mtime_ns']
        assert str(s['ctime_ns'])==r['stat_before']['ctime_ns']
        assert s['ino']==r['stat_before']['ino'] and s['size']==r['stat_before']['size']
        assert 1778389200000000000<=int(r['stat_before']['mtime_ns'])<1794376800000000000
        assert r['read_bytes']==sum(f['fetched_bytes'] for f in r['fragments'])
        assert r['read_chars']==sum(f['visible_chars'] for f in r['fragments'])
        if not r['content_read']:
            assert not r['business_analyzed'] and not r['locators'] and r['source_hash'] is None
        for loc in r['semantic_locators']:
            a,b=map(int,re.findall(r'\d+',loc))
            if any(not any(f['line_range'][0]<=n<=f['line_range'][1] for f in r['fragments']) for n in range(a,b+1)):
                errors.append((r['id'],loc,'semantic locator beyond retained fragment'))
    assert not errors,errors
    assert sum(data['counts']['by_status'].values())==107
    assert data['read_metrics']['read_bytes']==sum(r['read_bytes'] for r in records)
    assert data['read_metrics']['read_chars']==sum(r['read_chars'] for r in records)
    save(data)
    page=BASE.parent/'模型业务主题_B.md'
    text=page.read_text()
    marker='<!-- B_SOURCE_INDEX -->'
    text=text.split(marker)[0].rstrip()+'\n\n'+marker+'\n\n'
    text+='| ID | 真实源路径 | 业务证据定位 | mtime（UTC） |\n| --- | --- | --- | --- |\n'
    for r in records:
        if r['business_analyzed']:
            path=r['path']
            rel=path.split('/业务模型/',1)[1]
            text+=f"| {r['id']} | [{rel}](<{path}>) | {'; '.join(r['semantic_locators'])} | {r['mtime_utc']} |\n"
    page.write_text(text,encoding='utf-8')
    print(json.dumps(dict(queue_coverage='107/107',missing=0,duplicate_paths=0,required_fields='PASS',
                          nanosecond_strings='PASS',source_final_stat='107/107 stable',
                          semantic_locator_bounds='PASS',read_metric_sums='PASS',
                          independent_review='pending',json_sha256=sha(OUTPUT.read_bytes()),
                          topic_sha256=sha(page.read_bytes())),ensure_ascii=False,indent=2))

if __name__ == '__main__':
    if sys.argv[1] == 'init':
        init()
    elif sys.argv[1] == 'show':
        show(int(sys.argv[2]),int(sys.argv[3]))
    elif sys.argv[1] == 'supplement':
        data=json.loads(OUTPUT.read_text())
        r=data['file_decisions'][int(sys.argv[2])-1]
        previous=r['fragments'][-1]
        fragment(r, previous['byte_range_half_open'][1], int(sys.argv[3]), previous['line_range'][1]+1)
        save(data)
        show(int(sys.argv[2]),int(sys.argv[2]))
    elif sys.argv[1] == 'finalize':
        finalize()
    elif sys.argv[1] == 'verify':
        verify_and_index()
