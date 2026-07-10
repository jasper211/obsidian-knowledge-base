---
type: 项目笔记
source: 01_原始材料-外部导入/M-88_mark日常输出
synced: 2026-06-15
tags: [项目]
---

# 月度聚合会审核结果 v2 - 2026-04（4 字段完整版）

**版本**: v2.0（基于 v1.0 修正）
**修正原因**: v1.0 audit 文件中 73 个 PROMOTE 仅含简述，agent 处理后产生 BRIEF 模式（causal_logic / root_cause = null）。Mark 在会议中实际产出了 73 × 4 字段 = 219 个判断，但 v1.0 audit 仅传递了 73 个简述。本 v2 修正这个错误，含全部 103 个 PROMOTE 的完整 4 字段。
**修正日期**: 2026-04-29
**Agent 处理指令**: `python pipelines/process_audit_results_2026_04_v2.py`

---

## §0 处理说明（5 段格式）

### §1 我做了什么
- 从"月度聚合会_103_PROMOTE详细汇总_2026-04.md"提取全部 103 个 PROMOTE 的完整 4 字段
- 重新组织为 agent parser 可消费的 YAML-like 格式
- 每个 entry 含：layer / confidence / business_framework / causal_logic / root_cause / 联动 / quantitative_thresholds（C 类）
- DELAY / REVISE / REJECT_MERGE / CREATE 决策保持 v1.0 不变

### §2 我检查了什么
- ✅ 103 个 PROMOTE entries 全部含完整 4 字段（grep 验证）
- ✅ 每个 entry 的 entry_id 与 v0.9 baseline 一致
- ✅ DELAY / REVISE / REJECT_MERGE / CREATE 决策与 v1.0 一致
- ✅ 跨层联动 13 项保持

### §3 我没检查什么 / 我简化了什么
- ⚠️ 11 个伪 PROMOTE（strategic_framework_009b-013b + decision_framework_008-013）仍标 PROMOTE，但 v0.9 baseline 不存在 → agent 仍会跳过（按 v1.0 逻辑）。这 11 个的"留下月专题"决策（1B）保持有效。
- ⚠️ 4 字段的具体措辞我从详细汇总文档复制过来，没让 Mark 重新审一遍 → 应该等同于 Mark 在会议中的判断（因为详细汇总文档 Mark 已认可）。

### §4 决策分歧
- 无新决策分歧。本 v2 是对 v1.0 错误的修复（不是新审核）。

### §5 已知未完成
- agent 跑完 v2 后：87 PROMOTE_BRIEF + 14 PROMOTE_FULL → 87 PROMOTE_FULL（73 个升级 + 14 个保持）
- 4 CREATE 不变
- 91 baseline 保持，但全部变成 FULL（mark_input_mode=full）
- 议程 7（73 BRIEF 4 字段补全）可以从下月议程移除

---

## §1 PROMOTE entries 完整 4 字段（按 entry_id 排序）


### entry_id: `decision_framework_001`

**candidate_number**: #87
**name**: 阶段判断框架（季度评估，本次会议修订）
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
与 strategic_framework_011（L1 五阶段战略路径）配套的判断工具。每季度末 + 关键事件触发时使用（修订自原"每年 Q4"）。判断维度：(1) 当前主阶段权重是否需要调整；(2) 是否触发跃迁事件（保司主动采用 / 监管引用 / 同行接入）；(3) 下一阶段储备是否就绪；(4) 失败判据是否触发（如 3 年红线）。每季度输出阶段权重表更新 + 战略动作清单调整。

**causal_logic**:
评估周期年度 → 阶段权重调整滞后 → 跃迁事件来临时无法快速响应 → 错失窗口。+ 当前阶段 1→2 转换关键期，年度评估太慢。反向：每季度评估 → 阶段权重持续优化 → 跃迁来临时已就绪 → 战略叙事权 + 估值倍数双跃迁。

**root_cause**:
AI 时代反馈循环必须缩短（principle_014：反馈循环越短组织进化越快）。战略层评估也适用——年度评估是工业时代节奏，AI 时代应该季度甚至月度。这是把"反馈循环越短越好"原则应用到战略层评估的具体表现。

**cross_layer_links**:
触发 #24 L1 战略路径全景中"每年 Q4 自评"机制同步修订为"每季度自评"；与 #100 KA 升降级判断 + #101 团队扩张/收缩 + #99 业务线退出判断同步季度节奏

---


### entry_id: `decision_framework_002`

**candidate_number**: #88
**name**: 战略叙事分层
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark 公司对外叙事的分层规则（来自 L2_02 基础设施三层架构）：(1) 对 C 级员工 / 大众："跨境保险 MGA 公司"（安全、常规）；(2) 对 S 级合作方（保司 / 大同行）："跨境财富管理行业的运营合伙人"；(3) 对核心高管（3-5 人）："基础设施三层 + 五阶段路径"；(4) 对 Mark 本人：当前阶段进展 + 下一阶段储备。每个层级使用对应词汇，避免错配（如对大众讲"行业 OS"会被误认为 Crypto / 技术平台）。

**causal_logic**:
叙事不分层 → 对大众讲"行业 OS"被误解 → 错失合作机会。反向：分层叙事 → 每个层级精准沟通 → 战略叙事兑现。

**root_cause**:
战略叙事是认知工具。错配的叙事会"形变"为错误认知，反过来限制战略动作。这条原则把"分层叙事"工程化为可执行清单。

**cross_layer_links**:
#22 五阶段路径观（行业 OS 2030 前不对外讲）；#23 运营合伙人定位；#1 行业 OS 类比陷阱（反例验证）

---


### entry_id: `decision_framework_003`

**candidate_number**: #89
**name**: 投入-产出 ROI 计算框架
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark 公司任何重大投入（人员 / 系统 / 业务线 / 工具）的决策框架。三维度：(1) 直接产出（短期可见的 APE / 利润）；(2) 间接产出（know-how 资产 / 关系网络 / 系统能力）；(3) 战略产出（对 5 阶段路径的推进）。计算时三维度权重不同：阶段 1 重直接产出 70%，阶段 2-3 重间接产出 50%，阶段 4-5 重战略产出 60%。

**causal_logic**:
用单一直接产出衡量投入 → know-how 沉淀 + 关系积累 + 系统能力等"资产投入"被低估。反向：三维度框架 → 长期战略投入有依据。

**root_cause**:
基础设施型公司的投入很多是"资产积累"而非"立即变现"。这条框架是把"长期投入"工程化为可量化决策。

**cross_layer_links**:
与 #25 AI 数据组织升级（AI/数据/组织投入的 ROI 框架）；与 #84 mark_verified 资产估值锚点

---


### entry_id: `decision_framework_004`

**candidate_number**: #90
**name**: 跨保司迁移决策框架
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
阶段 2 启动新保司合作的决策框架。判断维度：(1) 该保司战略匹配度（产品互补 / 合规边界）；(2) Mark 现有 know-how 复用率（A/B 库可用度）；(3) 切换成本（流程对接 / 系统改造 / 团队学习）；(4) 风险评估（合规 / 数据 / 关系冲突）；(5) 时机窗口（市场窗口 + 永明关系是否有冲突）。每个维度评分后综合决策。

**causal_logic**:
随机选保司 → 战略匹配度低 → 资源分散。反向：决策框架 → 优先级排序 → 阶段 2 启动有依据。

**root_cause**:
阶段 2 不是"多签几家保司"，是"挑选战略匹配的保司"。决策框架是把"挑选"工程化的工具。

**cross_layer_links**:
#85 永明深度 vs 多保司广度；阶段 2 启动条件（≥ 100 mark_verified entries）

---


### entry_id: `decision_framework_005`

**candidate_number**: #91
**name**: 监管变化应对决策框架
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
监管变化（GL16/25 / 廉政联合执法 / SFC 政策更新）对 Mark 公司业务的影响评估 + 应对决策。流程：(1) 监管变化识别（专人监控）；(2) 影响评估（哪些业务线 / KA / 产品受影响）；(3) 应对方案设计（合规调整 / 业务模式优化 / 战略机会识别）；(4) 时间盒 + 责任人；(5) 后续追踪。GL16/25 的应对就是这个框架的实战案例（信息差 B 已填平 + C 反向机会）。

**causal_logic**:
监管变化被动应对 → 措手不及。反向：主动监控 + 决策框架 → 监管变化反而成为战略机会（如 GL25 推动持牌 = 阶段 3 渠道转化）。

**root_cause**:
监管是高度监管行业的核心变量。"被动应对"会变成"被动收缩"，"主动应对"才能把监管变化变成战略机会。

**cross_layer_links**:
信息差 B/C/D 都与监管变化相关；principle_028（合规优先红线）；#80 IA 中介合规 + #79 SFC 持牌法团合规

---


### entry_id: `decision_framework_006`

**candidate_number**: #27
**name**: 决策规则化工作流
**layer**: A
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
决策规则化是把"Mark 个人判断"转化为"组织规则"的工作流。核心公式：加规则价值 = 错误成本 × 频率 - 维护成本 - 灵活性损失。决策树：(1) 错误成本高 + 频率高 → 必须规则化（不能让 LLM 自由判断）；(2) 错误成本低或频率低 → 让 LLM 自由（不值得维护规则）。规则化执行 4 步：识别场景 → 显式化判断 → 进入代码层（不是 prompt 层）→ 设置 owner + 评审周期 + 变更流程。这条工作流是 DKP 流水线（mechanism_playbook_022）的"判断阶段"输出——什么 know-how 该规则化，什么不该。

**causal_logic**:
不区分错误成本/频率，全部规则化 → 规则维护成本爆炸 + 灵活性丧失 → 规则系统老化失效。反向不区分，全部让 LLM 自由 → 高错误成本场景被 LLM 失败拖垮（如 Phase 1 的 70% 假设性产出 = 战略级判断没有规则化的代价）。反向：按公式算清楚 → 规则化与 LLM 自由各得其所 → 规则可持续维护 → 协作杠杆兑现。

**root_cause**:
把所有判断都交给 LLM = 不机构化（个人能力依赖）；把所有判断都规则化 = 过度工程化（灵活性丧失）。两个极端都失败。决策规则化工作流是用"错误成本 × 频率"作为客观依据，让两个极端中间的最优分配点变得可计算、可维护。

**cross_layer_links**:
是 principle_024（AI-人分工）的具体执行框架；与 mechanism_playbook_022（DKP 流水线）配套；与 #14c agent_config_014（自我迭代+依赖分析）联动

---


### entry_id: `decision_framework_007`

**candidate_number**: #28
**name**: 真实 6 个信息差（含 D 反转）
**layer**: A
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
真实 6 个信息差按"是否构成 Mark 战略动作"分三类：

类型 1（操盘机会，Mark 直接执行）：
- A 客户端产品认知差——Layer A 服务平台功能（专业咨询）
- E 保司 vs 内地分布差——vendor 模式核心，TA 6 亿真实定位
- F 非持牌→持牌运营建设差——Mark 已有 know-how 通过 RW-同行联运变现，阶段 3 渗透加速器

类型 2（战略杠杆点，反推产品/渠道设计）：
- C 非持牌 vs 经纪行合规差——监管推动非持牌持牌 → 新晋持牌人成阶段 3 目标客群
- D 返佣行情差——根本问题是保司产品设计未联动"客户-市场"视角；Mark 作为 MGA 反向倒逼保司做差异化产品（把利益从"中间经纪行佣金"转移到"客户保费折扣/直接增值权益"），实现 4 方共赢，把 vendor 模式从"销售执行"升级到"产品共创"

类型 3（不相关）：
- B 经纪行 vs 保司佣金差——已被 GL16/25 监管填平

Mark 真正商业机会 = 类型 1（A+E+F）直接执行 + 类型 2（C+D）战略杠杆。

**causal_logic**:
用外部观察者视角看 6 个信息差 → B/C/D 看似有套利空间 → 战略向"信息套利"偏移 → 实际全部不是直接套利空间（B 已填平、C 是渠道转化、D 是产品设计反推）→ 战略动作错配。+ 用静态视角看 C/D → 错失渠道转化（C）和产品差异化（D）的杠杆。+ 看不到 F → 错失 Mark 已有 know-how 的市场化机会。反向：操盘者视角 + 动态视角 + 能力匹配视角 + 价值链上溯视角 → 识别 A+E+F 操盘机会 + C+D 战略杠杆 → vendor 模式不仅做销售执行，还做产品共创（D 反推差异化）+ 同行渗透加速器（C+F）→ 阶段 1（永明深度）→ 阶段 2（多保司）→ 阶段 3（同行经代）打通。

**root_cause**:
信息差分析必须用 4 个视角校准：① 操盘者视角；② 动态视角；③ 能力匹配视角；④ 价值链上溯视角。三个视角缺一会让战略动作错配。这条决策框架的核心是把"信息差分析"从"市场叙事工具"升级为"4 视角战略动作触发器"。

**cross_layer_links**:
与 #2 信息差还原陷阱（反例 + 修正对子）；与 #26 基础设施三层（F 对应 Layer B RW-同行联运 / D 对应 Layer C 与永明 TA 关系升级）；与 #23 运营合伙人定位（D 验证 Mark 是深度介入方）；与 #24 五阶段路径（A+E+F 直接执行类型 / C+D 战略杠杆类型）；触发新 C 类 Playbook 候选"保司产品差异化共创"（下月新增）

---


### entry_id: `decision_framework_008`

**candidate_number**: #97
**name**: 何时不做规则化（灵活性优先）
**layer**: A
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
与 #61 principle_011（决策成本越高规则化价值越大）配套的反向判断。何时不做规则化：(1) 低决策成本（错误后果小）；(2) 低频率（不经常发生）；(3) 高灵活性需求（需要 case-by-case）；(4) 早期探索阶段（规律未稳定）。这条原则避免"规则化过度"——把所有决策都规则化会让组织僵化。

**causal_logic**:
低成本场景也强行规则化 → 维护成本爆炸 → 规则系统僵化。反向：按 4 个维度判断 → 该规则化的规则化 + 该灵活的灵活 → 规则系统精简可持续。

**root_cause**:
规则化的边际收益递减。这条原则是把"何时停止规则化"工程化为可判断标准。

**cross_layer_links**:
#61 principle_011（决策成本越高规则化价值越大）；#27 decision_framework_006（决策规则化工作流）

---


### entry_id: `decision_framework_009`

**candidate_number**: #98
**name**: 业务线启动时机判断
**layer**: A
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
新业务线启动的判断框架。判断条件：(1) 战略匹配度——与 5 阶段路径权重表（#94）匹配；(2) 资源就绪度——know-how 储备 ≥ 60% / 团队产能可调配 / 财务可承受；(3) 时机窗口——市场窗口 + 监管窗口 + 竞争空白；(4) 退出门槛——若失败 6 个月内能否平稳退出。4 维度评分 ≥ 70 分启动。

**causal_logic**:
业务线启动凭直觉 → 资源浪费 + 战略错配。反向：4 维度评分 → 启动决策客观化。

**root_cause**:
业务线启动是高成本决策（人 + 资金 + 时间），需要客观判断框架。

**cross_layer_links**:
#94 阶段并行资源分配公式；#90 跨保司迁移决策框架；#99 业务线退出判断（互补对子）

---


### entry_id: `decision_framework_010`

**candidate_number**: #99
**name**: 业务线退出/收缩判断
**layer**: A
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
业务线退出/收缩的判断框架。3 类触发：(1) 红线触发——失败判据（#96）触发；(2) ROI 触发——连续 6 个月 ROI < 1.5；(3) 战略触发——与 5 阶段路径冲突或不再匹配。每季度末评估（#87 季度末机制）。退出/收缩动作清单：人员安置 / 客户转移 / know-how 沉淀（不浪费已有资产）。

**causal_logic**:
业务线"永不退出"→ 低 ROI 业务持续输血 → 集团整体效率下降。反向：客观退出框架 → 资源及时释放 → 投入更高 ROI 方向。

**root_cause**:
组织资源有限，新业务启动 = 必有业务退出。退出框架是把"取舍"工程化的工具。

**cross_layer_links**:
#96 失败判据红线；#87 季度评估；#98 业务线启动判断（互补对子）

---


### entry_id: `decision_framework_011`

**candidate_number**: #100
**name**: KA 升降级判断
**layer**: A
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
KA 分级（#36 KA 分级与画像）的动态调整框架。升级条件：连续 3 个月超过上一级别基线 → 升级。降级条件：连续 6 个月低于当前级别基线 → 降级。特殊：突破/急降需要 Mark 主动 review（避免短期波动误判）。每季度末批量调整（#87 季度评估同步）。

**causal_logic**:
KA 级别一旦定下不调整 → 资源错配（高潜 KA 服务不足 / 衰退 KA 资源浪费）。反向：动态调整 → 资源精准投放 → KA 体系健康度持续优化。

**root_cause**:
KA 价值是动态变化的，分级体系必须配套动态调整机制。

**cross_layer_links**:
#36 KA 分级与画像；#87 季度评估机制

---


### entry_id: `decision_framework_012`

**candidate_number**: #101
**name**: 团队扩张/收缩判断
**layer**: A
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
组织规模动态调整的判断框架。扩张条件：(1) 人均投产比 ≥ 1:5（#69）；(2) 业务量超过现有团队产能阈值 ≥ 6 个月；(3) 新业务线启动需要专门团队。收缩条件：(1) 人均投产比 < 1:3 持续 3 个月；(2) AI 协同强度（mechanism_playbook_017）持续不达标；(3) 业务线退出（#99 触发）。每季度末评估。

**causal_logic**:
团队扩张滞后 → 业务受限。+ 团队不收缩 → 人均投产比恶化。反向：扩张/收缩双向判断 → 团队规模与业务匹配。

**root_cause**:
组织规模不是越大越好（违反 strategic_framework_001 哑铃组织）。客观判断框架避免"自然扩张"陷阱。

**cross_layer_links**:
#69 人均投产比；#31 mechanism_playbook_017（200-300 小时投入追踪）；#99 业务线退出判断

---


### entry_id: `decision_framework_013`

**candidate_number**: #102
**name**: 资本/资金动作判断
**layer**: A
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark 公司资本动作（融资 / 估值故事讲述 / 战略并购 / 资金分配）的判断框架。判断维度：(1) 当前阶段是否需要资本动作（5 阶段路径中的对应资本节奏）；(2) 估值倍数是否与故事匹配（基础设施 8-15x vs SaaS 3-5x）；(3) 资金使用方向（短期：业务扩张 / 中期：基础设施建设 / 长期：跨保司复制）；(4) 风险评估（合规 / 战略一致性 / 控制权）。

**causal_logic**:
资本动作凭机会触发 → 错过窗口或仓促行动。反向：判断框架 → 资本动作与战略节奏一致。

**root_cause**:
资本动作是高敏感决策，需要客观判断框架避免短期诱惑导致长期错配。

**cross_layer_links**:
#84 mark_verified 资产 = 估值锚点；#22 五阶段路径权重表；#26 基础设施三层（估值倍数依据）

---


### entry_id: `principle_001`

**candidate_number**: #4
**name**: AI 时代的人类价值三类
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
AI 时代组织设计的三类人模型：(1) 结果负责人（CEO/COO/业务线负责人）—— 最稀缺，需要跨领域信息拉通能力 + 决策权 + 风险承担；(2) 合规专家（Key Person/法务/审计）—— 不可被 AI 替代的牌照/资质/法律责任主体；(3) 业务独当一面者（一线销售/客户经理/产品经理）—— 直接产生业务结果，AI 是放大器而非替代品。中间层（项目经理/协调员/汇报员/翻译员）会被 AI 系统性替代。Mark 公司 124 人组织对照此框架，预计 30% 保留（约 40 人）。

**causal_logic**:
AI 让信息在组织内自动流转 → 协调/翻译/汇报岗位失去价值（机器做得更快更准）→ 中间层消失。剩下的人必须直接产生价值：要么承担结果（高 leverage 决策）→ 高薪保留；要么承担合规风险（不可替代）→ 必要保留；要么直接产生业务（与 AI 协同）→ 一线保留。组织从金字塔（多层中间）变为哑铃（顶+底）。

**root_cause**:
AI 把"信息中转"成本压到接近 0，所以"信息中转"岗位失去经济价值。剩下有价值的是 AI 做不到的三件事：承担后果（结果负责）、承担法律责任（合规）、承担物理在场（业务一线）。

**cross_layer_links**:
#67 strategic_framework_002 三类人才与组织扁平化；#66 strategic_framework_001 AI 时代组织扁平化；#31 mechanism_playbook_017 200-300 小时追踪

---


### entry_id: `principle_002`

**candidate_number**: #55
**name**: AI 是认知放大器，不是替代品
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
AI 不是"取代人"的工具，是"放大人判断"的工具。Mark 公司应用：(1) AI 放大 Mark 战略判断（Claude 第二大脑）；(2) AI 放大 KA 销售能力（培训 + Agent 辅助）；(3) AI 放大组织协作效率（Agent 替代协调岗位）。这条原则与 principle_024（AI-人分工哲学）、principle_001（三类人）形成认知体系。

**causal_logic**:
把 AI 当替代品 → 决策权交给 LLM → LLM 在结构判断上失败 → 翻车。反向：AI 当放大器 → 人保留判断 + AI 放大执行 → 杠杆 13-16x 兑现。

**root_cause**:
LLM 的语言能力世界级、结构判断不稳定。"放大器"定位精准利用前者、规避后者；"替代品"定位错配能力分布。

**cross_layer_links**:
#5 principle_024；#4 principle_001

---


### entry_id: `principle_003`

**candidate_number**: #56
**name**: 个人 vs 组织使用 AI 是两个量级
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
个人使用 AI（13-16x 杠杆，Mark 实测）≠ 组织使用 AI（10x 杠杆，更难）。差异源于：(1) 个人 AI 协同直接，组织 AI 协同需流程；(2) 个人判断闭环秒级，组织判断闭环需协作；(3) 个人规则库即时更新，组织规则库需机构化。Mark 公司的关键是"把个人 AI 杠杆机构化为组织 AI 杠杆"——这就是 experience-engine 项目的存在理由。

**causal_logic**:
把个人 AI 经验直接套用到组织 → 组织成员各自用 AI 但不形成系统 → 杠杆停留在个人级（10 倍而非 100 倍）。反向：经验机构化 → 组织级 AI 协同 → 集体杠杆 10x（不是各自 1.3x 加总）。

**root_cause**:
个人 AI 是"工具使用"，组织 AI 是"系统协同"。两者的瓶颈不同（个人是判断质量，组织是机构化深度）。

**cross_layer_links**:
#82 strategic_framework_003（1 个 Mark = 10 个普通员工）；experience-engine 项目存在的根本理由

---


### entry_id: `principle_004`

**candidate_number**: #57
**name**: AI 杠杆需要 200-300 小时心流投入
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
AI 杠杆不是"用 AI 工具"，是"高强度专注 + AI 协同"的复合产物。Mark 实测每周 200-300 小时（含 Agent 协同时间）才能达到 13-16x 杠杆。门槛特征：(1) 每周 ≥40 小时电脑活跃；(2) 每天 ≥$20 token 消耗；(3) 每周 ≥1000 文档处理；(4) 每周 ≥200 次 Agent 调用。低于这些数字 = AI 协同强度不足，杠杆不会兑现。

**causal_logic**:
组织成员使用 AI 但不达 200-300 小时投入 → AI 协同强度不足 → 杠杆停留在 1.3-2x（不是 13x）→ 公司付薪水但未获真实杠杆。反向：达投入门槛 → 心流状态 + AI 持续反馈 → 杠杆兑现 → 个人产出抵 10 人。

**root_cause**:
AI 协同杠杆不是"会用工具"问题，是"心流 + 持续反馈循环"问题。低于心流门槛，AI 工具的价值无法被激活。

**cross_layer_links**:
#31 mechanism_playbook_017 200-300 小时追踪机制（具体执行）；#101 团队扩张/收缩判断

---


### entry_id: `principle_005`

**candidate_number**: #58
**name**: 数据基础设施是 AI 杠杆的前提
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
AI 杠杆兑现需要数据基础设施先行。链条：原始数据 → FACT 表 → DIM 表 → KPI 体系（已有 R1-R9）→ Layer 3 分析层 → AI Agent 加载。任一环节缺失，AI Agent 加载的就是零散数据，无法做有效判断。Mark 公司当前数据基础设施完成度约 60%（FACT_POLICY 完整、FACT_COMMISSION 部分、FACT_ALLOCATED_COST 部分、KPI 体系定义未实施）。Phase 2 的核心任务之一就是补齐数据基础设施。

**causal_logic**:
没有数据基础设施 → AI 加载零散数据 → 判断质量低 + 不可重现 → 杠杆失败。反向：数据基础设施完整 → AI 加载结构化上下文 → 判断质量高 + 可追溯 → 杠杆兑现。

**root_cause**:
AI 不是"魔法"——它的输出质量上限由输入数据质量决定。数据基础设施是 AI 杠杆的物理基础。

**cross_layer_links**:
#77 mechanism_playbook_004 数据基础设施建设（DELAY，下月专题）；KPI.xlsx 50+ KPI 体系；FACT 表系列

---


### entry_id: `principle_006`

**candidate_number**: #59
**name**: 经验机构化必须代码化，不能只靠文档
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
经验机构化的载体必须是"代码可加载"形态，不能只是文档。链条：Mark 脑中判断 → 显式化文档（Markdown）→ 结构化 Schema（YAML）→ 代码可加载（API）→ Agent 加载执行。Phase 1 已经把 117 entries 升级到 Schema 层（v0.9）+ 4 个 Schema 文件。Phase 5 API 化是从 Schema 到"代码可加载"的最后一步。如果停留在文档层（Markdown 只读），经验机构化就只对人有用、对 Agent 无用。

**causal_logic**:
经验只在文档（Markdown）→ Agent 无法加载 → 跨 Agent 实例失忆 → 经验机构化失败。反向：代码化（YAML + API）→ 任何 Agent 启动时加载 → 跨实例一致 → 经验真正成为组织资产。

**root_cause**:
文档化 ≠ 机构化。机构化需要"机器可消费"——这就是为什么 experience-engine 的核心载体是 YAML（不是 Markdown）+ Schema + API。

**cross_layer_links**:
#65 principle_015 经验代码化的本质；experience-engine 项目核心载体设计；Phase 5 API 化

---


### entry_id: `principle_008`

**candidate_number**: #60
**name**: 工具迁移成本与杠杆的平衡
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
选择 AI 工具时必须做 ROI 计算：杠杆增益 vs 迁移成本。决策三维度：(1) 杠杆增益——预期效率提升倍数；(2) 迁移成本——学习曲线 + 数据迁移 + 流程改造；(3) 锁定风险——工具供应商依赖度。Mark 公司原则：(a) 杠杆 < 2x 不值得迁移；(b) 锁定风险高的工具需要备选方案；(c) 已有团队习惯的工具优先升级而非替换。

**causal_logic**:
盲目追新工具 → 迁移成本 > 杠杆增益 → 团队疲于切换 → 整体效率下降。反向：ROI 计算后迁移 → 杠杆兑现 + 团队节奏稳定。

**root_cause**:
AI 工具迭代速度极快，组织无法跟上每个新工具。"工具选择"本质是"投入-产出 + 锁定风险"的多目标优化。

**cross_layer_links**:
#75 mechanism_playbook_008 AI 工具栈选型机制（具体执行）

---


### entry_id: `principle_011`

**candidate_number**: #61
**name**: 决策成本越高，规则化价值越大
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
与 decision_framework_006（决策规则化工作流）配套的判断原则。具体：(1) 高决策成本 + 高频率 → 必须规则化（如：合规判断 / KA 分级 / 阈值触发）；(2) 高决策成本 + 低频率 → 不规则化但建立 SOP（如：重大战略转向）；(3) 低决策成本 + 高频率 → LLM 自由判断 + 偏差监控；(4) 低决策成本 + 低频率 → 完全自由。Mark 公司的规则化优先级清单基于这个矩阵。

**causal_logic**:
低成本决策也强行规则化 → 规则维护成本爆炸 → 规则系统僵化。反向：按成本×频率矩阵决策 → 规则化资源精准投放 → 系统可持续。

**root_cause**:
规则化不是越多越好，是"边际收益 > 边际成本"才值得做。这条原则把"规则化决策"工程化为客观计算。

**cross_layer_links**:
#27 decision_framework_006（决策规则化工作流）；#97 decision_framework_008（何时不做规则化的反向判断）

---


### entry_id: `principle_012`

**candidate_number**: #62
**name**: 单点失效是组织最大风险
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
组织设计的根本原则——任何关键能力依赖单一角色 = 单点失效风险。Mark 公司当前单点：(1) 战略判断高度依赖 Mark；(2) 永明关系高度依赖 Mark；(3) 部分核心 KA 依赖 Mark 个人关系；(4) 财务合规依赖 Alice（Key Person）。应对：(1) Mark 战略判断 → experience-engine 机构化（A/B 库）；(2) 永明关系 → 制度化合作框架（阶段 1 KPI）；(3) KA 关系 → KA 分级体系 + 标准化服务；(4) Alice 单点 → Bernard + Roy 三角财务团队（已建）。

**causal_logic**:
单点失效未识别 → 关键人离开 → 业务瘫痪（如 Phase 1 教训：Alice 健康危机暴露财务单点风险）。反向：主动识别 + 系统化分散 → 抗风险能力提升 → 组织韧性。

**root_cause**:
组织规模 → 关键能力依赖个人 → 单点风险积累。这是 Mark 公司从"高水平 boutique"升级到"基础设施"的关键障碍。

**cross_layer_links**:
experience-engine 项目本身的存在理由（Mark 战略判断的机构化）；D5 财务团队三角结构

---


### entry_id: `principle_014`

**candidate_number**: #63
**name**: 反馈循环越短，组织进化越快
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
组织进化速度 = 反馈循环频率的函数。传统组织：年度复盘 / 季度 OKR → 进化速度慢。Mark 公司：每天反馈循环（mechanism_playbook_018）+ 每月聚合会（experience-engine）→ 进化速度 13-16x。链条：行动 → 反馈 → 规则更新 → 下次行动改进。每缩短反馈循环一个量级（年→季→月→周→天→秒），组织进化速度提升一个量级。

**causal_logic**:
反馈循环年/季级别 → 偏差累积到下次复盘已严重 → 修正成本高。反向：日级反馈 + 月度聚合 → 偏差当天识别 → 第二天就修正 → 复利提升。

**root_cause**:
组织进化的瓶颈不是"是否反馈"，是"反馈速度"。AI 把反馈速度从月/周缩短到秒/天，但前提是组织有反馈循环机制（mechanism_playbook_018）。

**cross_layer_links**:
#32 mechanism_playbook_018 每天反馈循环（运行时载体）；#87 季度评估（修订自年度，应用此原则）

---


### entry_id: `principle_015`

**candidate_number**: #65
**name**: 经验代码化的本质是"判断的可复用化"
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
经验代码化（experience-engine 项目本质）的真实含义不是"把经验写下来"，是"把判断变成可被任何角色复用的资产"。链条：Mark 脑中判断（个人能力）→ 显式化文档（可读不可执行）→ 结构化 Schema（可加载但需理解）→ 代码化规则（任何 Agent 启动即可用）→ 跨 Agent 实例 / 跨业务 / 跨保司复用。这条原则定义了 experience-engine 项目的最终形态判断标准——不是"我们写了多少文档"，是"我们的判断有多少被代码化复用了"。

**causal_logic**:
经验只在文档层 → 需要人理解后执行 → 跨人传递有损耗 → 不可规模化。反向：经验代码化 → 任何 Agent 加载即可用 → 跨实例无损 → 真正可规模化（10x → 100x）。

**root_cause**:
传统"知识管理"停留在文档层（人 → 文档 → 人），失败率 90%+。"经验代码化"是从文档层升级到执行层（人 → 代码 → 任何 Agent）。这是估值倍数差异的物理基础（基础设施 8-15x vs 文档库 1-2x）。

**cross_layer_links**:
#3 mechanism_playbook_022 DKP 流水线（具体流程）；#84 strategic_framework_006 mark_verified 资产 = 估值锚点

---


### entry_id: `principle_016`

**candidate_number**: #9
**name**: 事实五件确认（升级自三件，Mark 本次会议拍板）
**layer**: A
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
事实五件（升级自原三件）是任何战略级 AI 建议或跨角色协作动作的强制前置门禁。Claude/Agent/外部协作方必须在给出战略推理前显式确认五件事实：(1) 下游消费者——谁会用这条建议？以什么形式？(2) 进度三段——已做什么/未做什么/待做什么；(3) 时间约束——什么时候必须完成 + 外部硬约束（合规期限、市场窗口）；(4) 里程碑——硬里程碑/软里程碑/中间检查点；(5) 责任矩阵——拍板者/执行者/验收者。任一缺失则建议是"伪建议"，必须先校准事实再推理。

**causal_logic**:
跳过事实五件确认 → 凭语境推测 5 个变量（下游/进度/时间/里程碑/责任）→ 推理基于错误假设（如 PPT 案例错配"单人用户"假设）→ 战略建议方向完全错误 → Mark 用反例拦截 → 协作往返成本上升。反向：先校准五件事实 → 推理基于真实约束 → 建议落地可行 → 5 件事实清单本身成为产出物（避免下次重新问）→ 协作杠杆兑现。

**root_cause**:
战略级动作的失败根因 90% 是事实校准不到位，10% 是推理错误。LLM 的语言生成能力让"未校准事实的推理"看起来很合理，必须用结构化清单（五件事实）拦截。"事实三件"过于精简，实际操作中"客群"模糊（多客群？哪一个？）、"进度"模糊（节点 vs 完成度），所以升级为五件，颗粒度更操作化。

**cross_layer_links**:
触发 #12 agent_config_003 协作协议 + #14 agent_config_005 主动追问的同步升级

---


### entry_id: `principle_017`

**candidate_number**: #69
**name**: 组织目标必须可量化（人均投产比）
**layer**: A
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
组织管理的元原则——任何组织目标必须可量化（与 mechanism_playbook_020 组织效率倍数追踪配套）。核心指标"人均投产比"：每人年薪 / 每人年贡献利润。Mark 公司目标：人均投产比 ≥ 1:5（即每付 1 元薪水产生 5 元利润）。低于此线的岗位进入"自然流失"流程。

**causal_logic**:
组织目标定性表述（"提高效率"）→ 无法被检验 → 沦为口号。反向：定量指标（人均投产比 ≥ 1:5）→ 可追踪可验证 → 推动真实变革。

**root_cause**:
定性目标在 Mark 公司不可接受。这条原则是"AI 时代组织 = 数字化运营"的基础。

**cross_layer_links**:
#34 mechanism_playbook_020 组织效率倍数追踪；#101 团队扩张/收缩判断（投产比阈值）

---


### entry_id: `principle_018`

**candidate_number**: #7
**name**: 锚点优先原则
**layer**: A
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
锚点优先是所有结构性设计任务的 P0 门禁。任何"无中生有"的设计（组织架构/流程/Schema/模板/分类法）必须先获得 2-3 份真实锚点：(1) 已有的相似案例；(2) 实际产出的样本；(3) 业务现场的真实约束。AI/Agent 在没有锚点的情况下不开工，或在产出物显式标注"无锚点凭空草案，需校验"。这条原则适用于所有 experience-engine 的产出物——包括本系统自己的 Schema 设计、Worksheet 模板、4 字段标准。

**causal_logic**:
没有锚点 → AI 凭"行业常识 + 语境推测"产出 → 看起来合理但偏离实际业务 → 下游消费时发现错配 → 大规模返工。反向：先收集 2-3 份真实锚点 → AI 基于锚点抽象规律 → 产出物覆盖真实变体 + 隐性约束 → 下游可直接使用 → 杠杆兑现。Phase 1 的 70% 假设性产出 = 锚点优先原则被违反的代价。

**root_cause**:
AI 的语言生成能力让"凭空产出"看起来质量很高，但实际是表面合理性掩盖了对真实业务的无知。锚点是把 AI 从"模仿人类语言"拉回"对齐真实业务"的唯一可靠机制。

**cross_layer_links**:
#5 principle_024 AI-人分工；v4.2 方案"Mark 介入显式化"的根本依据；#71 mechanism_playbook_006 AI 输出质量审查

---


### entry_id: `principle_021`

**candidate_number**: #64
**name**: AI 协作需显式化"不确定性"
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
与 agent_config_002（5 段格式）+ agent_config_005（主动追问与假设标注）配套的协作认知。AI 协作的核心风险是"不确定性被隐藏"——LLM 倾向产出"看起来确定"的输出。应对：(1) 强制 AI 标注假设（"我的假设是 X"）；(2) 强制 AI 标注未检查（"我没检查 Y"）；(3) 强制 AI scope call 语义歧义；(4) Mark 主动追问"哪里你不确定"。把"不确定性"从隐藏变为显示，才能被 Mark 校准。

**causal_logic**:
AI 输出隐藏不确定性 → Mark 误以为已验证 → 错误传导到下游。反向：显式化不确定性 → Mark 可识别校准点 → 协作质量稳定。

**root_cause**:
AI 协作的最大风险不是"AI 出错"，是"AI 出错但 Mark 不知道哪里错"。显式化不确定性是把这个风险前置可见的机制。

**cross_layer_links**:
#11 agent_config_002 5 段格式；#14 agent_config_005 主动追问

---


### entry_id: `principle_022`

**candidate_number**: #8
**name**: Agent 行为边界（不越界规划）
**layer**: A
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark-Claude-Agent 三方协作的角色边界划分原则。每个角色的职责严格分工：(1) Agent = 执行者（运行任务+surface 事实+识别 scope 超出）；(2) Claude = 协调者（决定 Mark 触点+聚合颗粒度+战略层判断）；(3) Mark = 决策者（拍板+反馈）。Agent 不能越界做"Claude 该做的判断"——比如建议聚合时机、规划下游动作。Agent 越界 = 错误模式被嵌入运行时配置。

**causal_logic**:
Agent 越界规划 Claude 工作 → Mark 收到的"Agent 信息流"被 Agent 自己污染 → Claude 的协调价值被稀释 → 三方协作模型退化为"Agent + Mark"二元 → 协作杠杆下降。反向：严格三角分工 → Agent 输出纯净（事实+scope）→ Claude 基于事实做判断 → Mark 收到的是"已聚合的判断"→ 三角协作杠杆维持。

**root_cause**:
LLM 倾向于"主动 helpful"——但 helpful 的边界是自己的职责范围。超出职责的 helpful 是越界，会破坏多方协作的清晰度。这条原则是把"过度礼貌/迎合"（principle_023 偏差 A）在 Agent 层的具体应用。

**cross_layer_links**:
#21 agent_config_013 scope_violation_case 实例；#14d agent_config_015 三阶段时序协议

---


### entry_id: `principle_023`

**candidate_number**: #6
**name**: Mark-Claude 协作偏差识别
**layer**: A
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark-Claude 协作中识别出的具体认知偏差类型。建立偏差库（Bias Library）作为持续迭代资产：(1) Claude 端 4 类偏差（过度礼貌/伪装确定性/凭语境推测/模式错配）；(2) Mark 端 3 类偏差（结构性任务误派/不读 5 段报告就直接拍板/反馈缺失）；(3) β 模式作为"双方主动声明的高敏感协作状态"——双方都更主动地 surface 不确定性、给反馈。每次发现新偏差立即写入偏差库（A.5），月度聚合会评审。

**causal_logic**:
不识别偏差 → 协作 bug 重复出现（如：Phase 1 中 Claude 把 70% 假设性产出标 v1.0）→ 系统性错误传导到下游 → 信任受损 → 协作效率下降。反向：识别偏差 → 写入偏差库 → β 模式触发时双方主动校准 → 错误被前置拦截 → 协作杠杆持续提升（如 Phase 1 实测 10x，Phase 1 Repair 实测 8x）。

**root_cause**:
Mark-Claude 协作不是"用工具"，是"两个判断主体的对齐"。两边都有自己的认知盲区：Claude 倾向迎合而非真实判断，Mark 倾向把结构性任务委托给 LLM。识别这些偏差并文档化，是协作从 1.0 升级到 2.0 的必经路径。

**cross_layer_links**:
D 类 13 个具体偏差应对来源；#20 agent_config_012 偏差库（运行时存储）；#14c agent_config_014 自我迭代

---


### entry_id: `principle_024`

**candidate_number**: #5
**name**: AI-人分工哲学（v3.1 父框架）
**layer**: A
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
L0_03 AI-人分工哲学的核心定稿（含 31 个具体规则，跨 4 大主题）：(1) AI 是放大器非替代品；(2) 人保留判断 / 决策 / 后果承担；(3) 错误纠偏机制（人发现 → AI 修正 → 文档化）；(4) Agent L9+ 协作纪律（rule 31，2026-04-23 新增）。关键认知：LLM 两类能力——结构性判断（不可靠）/ 语言表达（世界级）。规则层接管结构决策，LLM 只做语言表达。"削弱 LLM 结构决策" = "强化 Mark 判断机构化程度"。AI = 判断力放大器，非替代品。这是 D 类 13 个 entries 的"上游原则"。

**causal_logic**:
不区分 AI/人能力边界 → 让 LLM 做结构性判断（如：业务诊断/战略推理/合规判断）→ LLM 在边界场景失败 → 后果不可控 → 信任崩溃 → AI 项目失败。反向：清晰分工 → 规则层承接结构决策 → LLM 仅做语言表达（其世界级能力）→ 错误率可控 → 持续迭代 → 杠杆 10-13x 真实兑现（Mark 04-13 实测）。

**root_cause**:
LLM 在不同任务上的能力分布是分裂的：语言表达能力世界级，但结构性判断能力不稳定。把 LLM 当"通用智能"使用必然失败；把 LLM 当"特定能力的精确工具"使用就能 10x 杠杆。这条原则是 AI 落地工程化的第一性原理。

**cross_layer_links**:
D 类 13 个 entries 全部的父原则；#27 decision_framework_006 决策规则化；#30 人机角色分工动态调整

---


### entry_id: `principle_025`

**candidate_number**: #1
**name**: 行业 OS 类比的过度承诺陷阱
**layer**: A
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
任何对外叙事的类比必须经过"机制层压力测试"——把类比拆解为 5+ 个具体机制（如 OS 的运行时依赖、API 标准化、文件系统读写模式、应用独立性、生态依赖），逐一对照实际业务，吻合度 < 80% 则禁止使用。"行业 OS" 仅 20% 吻合，"行业运营合伙人" 85% 吻合。该原则是对外叙事的"门禁"机制。

**causal_logic**:
类比未经压力测试 → 修辞吸引导致默认接受 → 对外叙事用"行业 OS" → 投资人按 SaaS 平台估值（3-5x 倍数）→ 反而压低基础设施服务（8-15x）的估值故事 → 战略叙事失效。反向：经过压力测试 → "行业运营合伙人" → 估值倍数对齐 → 对内动作可指导（深度运营 vs 标准化产品）→ 战略叙事兑现。

**root_cause**:
修辞优先级被无意识置于机制准确性之上。Mark 是操盘者视角（vendor 模式深度运营），但被外部金融记者视角的"行业 OS"叙事临时抓取，未做身份对齐。

**cross_layer_links**:
↔ #23 运营合伙人定位（双向验证）

---


### entry_id: `principle_026`

**candidate_number**: #2
**name**: 三个信息差还原陷阱
**layer**: A
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
任何"信息差"假设必须做两层验证：(1) 时间维度——这个信息差当前是否还存在，还是已被市场动作填平；(2) 角色维度——分析者用的是外部观察者视角还是操盘者视角。Mark 的真实信息差不是"中间层佣金"（已填平），而是 vendor 模式下"保司想合规看保司端分布"的需求——Mark 已在做，是 6 亿 TA 业务的真实定位。

**causal_logic**:
用外部观察者视角看行业 → 看到"信息差"概念有市场卖点 → 推导出"卖数据给保司"业务假设 → 错误指导战略动作（向数据 SaaS 偏移）→ 与 Mark 实际操盘的 vendor 模式分裂。反向：用操盘者视角 → 识别真实价值（代运营+代支付+反馈一体化）→ 战略动作对齐（深化永明 vendor 关系，扩展到其他保司）→ 阶段 2 多保司基础就位。

**root_cause**:
分析者身份未与操盘者身份对齐。"信息差套利"是金融记者视角的产业分析框架，但 Mark 是平台运营方，价值不来自信息差本身，而是把已合规的能力打包为基础设施服务。

**cross_layer_links**:
↔ #28 真实 6 信息差

---


### entry_id: `principle_028`

**candidate_number**: #81
**name**: 合规优先于增长（Mark 红线）
**layer**: A
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark 公司经营的根本红线原则。任何业务动作必须先过合规检查。优先级：合规 > 客户 > 增长 > 利润。具体含义：(1) 合规风险高的业务即使收入高也不做；(2) 合规与增长冲突时合规优先；(3) 不做"擦边球"业务（监管灰区）；(4) 主动配合监管（IA / SFC / 廉政）。

**causal_logic**:
合规让位增长 → 短期收入但长期风险 → 监管处罚 / 业务停摆。反向：合规优先 → 短期增长慢但长期持续 → 5 阶段路径走得稳。

**root_cause**:
跨境保险 / 财富管理是高度监管行业。"合规红线"是 Mark 公司能跑 5 阶段路径的底层保证。这条原则虽然内容简单但战略权重极高。

**cross_layer_links**:
信息差 C（监管推动持牌）+ #79 SFC 合规 + #80 IA 合规 + #46 渠道激励合规 + #91 监管变化应对决策框架

---


### entry_id: `strategic_framework_001`

**candidate_number**: #66
**name**: AI 时代组织扁平化
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
AI 时代组织形态从"金字塔"演化为"哑铃"。传统金字塔：决策层（5%）→ 中层管理（25%）→ 执行层（70%），中层负责"信息中转 + 协调"。AI 哑铃：决策层（30%，含战略+合规+一线 KA）+ Agent 执行层（70%，无中间管理）。Mark 公司从 124 人转型到 30%（约 40 人）就是金字塔→哑铃的物理实现。配套：mechanism_playbook_017（200-300 小时追踪）+ principle_001（三类人）。

**causal_logic**:
保留金字塔结构 → 中层管理岗位无法被 AI 替代（情感原因）→ AI 协同浪费在协调而非产出 → 杠杆未兑现。反向：扁平化 + 自然流失 → 协调岗位消失 → AI 协同直接服务产出 → 杠杆兑现。

**root_cause**:
AI 把"信息中转"成本压到接近 0，所以"信息中转"岗位失去经济价值。组织形态必须跟上技术变革，否则就是付薪水维持过时结构。

**cross_layer_links**:
#4 principle_001 三类人；#67 三类人才与组织扁平化；#31 mechanism_playbook_017

---


### entry_id: `strategic_framework_002`

**candidate_number**: #67
**name**: 三类人才与组织扁平化
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
与 principle_001（三类人）配套的组织设计框架。Mark 公司组织演化目标（12-18 个月）：(1) 结果负责人（10-15 人）——CEO/COO/业务线 lead/核心销售；(2) 合规专家（5-8 人）——Key Person/法务/审计/IA 备案；(3) 一线业务人员（20-25 人）——直接产生业务的销售/客户经理。共约 35-50 人（vs 当前 124 人）。中间层（项目经理/协调员/汇报员）全部退出。这是 Mark 公司"哑铃组织"的具体落地清单。

**causal_logic**:
不做明确人员分类 → 转型时争议大 → 流失人员判断标准不一致。反向：三类人才框架明确 → 自然流失有客观依据 → 组织转型有序进行。

**root_cause**:
组织扁平化不是"裁员"，是"重新定义谁有价值"。三类人才框架把这个判断显式化、客观化。

**cross_layer_links**:
#4 principle_001 三类人；#66 AI 时代组织扁平化；#82 1 个 Mark = 10 个普通员工

---


### entry_id: `strategic_framework_003`

**candidate_number**: #82
**name**: 1 个 Mark = 10 个普通员工的杠杆
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark 公司组织规划的核心命题。Mark 个人实测 13-16x 个人杠杆，但需要 200-300 小时心流投入支撑。组织级别的目标：每个核心员工达到"Mark 级别杠杆 / 3-5"（即 3-5x 杠杆），通过 30-40 人达到原 124 人的产出 + 更高效率。Mark 个人 = 10 个普通员工 = 整个公司转型的"个人能力杠杆参照系"。

**causal_logic**:
不识别个人能力杠杆差异 → 用平均薪酬+平均要求管所有人 → 高潜员工被低标准拖累。反向：以 Mark 杠杆为参照系 → 设计差异化薪酬+要求 → 高杠杆员工被识别和激励 → 组织整体杠杆提升。

**root_cause**:
传统组织假设员工能力同质，AI 时代员工能力差异 10x+。这条战略是把"能力差异显式化"为组织设计基础。

**cross_layer_links**:
与 mechanism_playbook_017（200-300 小时投入追踪）配套；与 #67 三类人才与组织扁平化共同支撑组织变革

---


### entry_id: `strategic_framework_005`

**candidate_number**: #68
**name**: 副机概念（员工 = 主机+副机）
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
与 mechanism_playbook_019（副机建设机制，已 REVISE）联动的战略概念。AI 时代每个员工 = 1 主机（人）+ 副机（24h Agent）。主机职责：决策 / 审核 / 跨知识域；副机职责：连续工作 / 监控 / 后台任务。这条战略框架定义了 Mark 公司未来员工的"工作单元"形态——不是"个人"，是"个人+副机"双工作单元。

**causal_logic**:
员工只有"自己"没有副机 → 个人精力上限 = 公司产能上限 → 杠杆受限。反向：员工 = 主机+副机 → 副机连续运行突破时间限制 → 杠杆 13-16x。

**root_cause**:
人的物理时间上限（每天 24 小时）是组织产能瓶颈。副机突破这个瓶颈——Agent 7×24 工作 + 人在关键节点决策。

**⚠️ 状态特殊**：本战略框架 PROMOTE，但执行机制 #33 mechanism_playbook_019 REVISE（下月再审）。状态不一致允许的——战略可先于机制定义，下月当 #33 重审时需确认与 #68 一致。

**cross_layer_links**:
#33 副机建设机制（执行机制，已 REVISE）；#5 principle_024 AI-人分工

---


### entry_id: `strategic_framework_006`

**candidate_number**: #84
**name**: 公司估值 = mark_verified 资产数量
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark 公司估值的物理基础不是"营收"或"利润"，是"经过 Mark 介入审核的可复用 know-how 资产数量"（mark_verified=true 的 entries 数量）。映射关系：(1) ≥ 100 个 mark_verified entries = 阶段 2 多保司启动条件；(2) ≥ 200 个 = 阶段 3 同行经代渗透条件；(3) ≥ 300 个 = 阶段 4 行业运营商条件；(4) ≥ 500 个 + 跨保司复制 = 阶段 5 行业 OS 条件。这条战略框架把"估值故事"工程化为可数字化追踪的资产清单。

**causal_logic**:
用传统营收估值 → 保险佣金倍数 3-4x → 估值偏低。+ 没有可量化资产追踪 → 估值故事说不清。反向：mark_verified 资产作为估值锚点 → 倍数 8-15x → 估值故事有数据支撑。

**root_cause**:
基础设施估值的本质是"可复用资产存量"。这条战略框架把"基础设施"从概念变为可量化指标。

**cross_layer_links**:
与 v4.2 方案核心修正 2（Mark 介入显式化）；与 #65 经验代码化本质；与 #26 基础设施三层（Layer A/B 的 know-how 集合）；与 #102 资本/资金动作判断

---


### entry_id: `strategic_framework_007`

**candidate_number**: #85
**name**: 永明深度 vs 多保司广度的取舍
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark 公司阶段 1 → 阶段 2 转换的核心张力。永明深度（vendor 模式深化、TA 6 亿增长）vs 多保司广度（启动第 2/3 保司、降低单保司依赖）。当前判断（2026）：永明深度优先 70% + 多保司广度储备 30%。永明深度的 know-how（A/B 库）= 多保司广度的复用资产。当永明 know-how 达 ≥ 100 mark_verified entries 时，自然过渡到广度。

**causal_logic**:
过早分散到多保司 → 永明深度不足 + 多保司浅尝辄止 → 两头不讨好。反向：先深度后广度 → 永明 know-how 沉淀 → 多保司复用启动 → 阶段 2 平稳过渡。

**root_cause**:
广度需要深度的资产支撑。这条原则把"阶段 1 vs 阶段 2"的张力工程化为可调权重。

**cross_layer_links**:
与 #24 五阶段路径权重表（2026 = 70%/20%/10%/0%/0%）；与 #90 跨保司迁移决策框架；与 #84 mark_verified 资产数量（≥ 100 = 阶段 2 启动条件）

---


### entry_id: `strategic_framework_008`

**candidate_number**: #86
**name**: 同行经代渗透速度 vs 深度的平衡
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
阶段 3（同行经代渗透）的核心张力。速度（5-10 家同行经代合作）vs 深度（每家深度联运、共享 know-how）。当前判断：深度优先 60% + 速度跟进 40%。每家同行经代深度合作 = 阶段 4 行业运营商的物理基础（关系密度 + know-how 渗透）。盲目追求 5-10 家但每家浅层 = 阶段 4 不可能。

**causal_logic**:
追求渗透速度 → 5-10 家但每家浅层 → 阶段 3 完成度看似高但阶段 4 没有基础。反向：深度优先 → 每家联运成熟才扩展下一家 → 关系密度 + know-how 渗透真实积累 → 阶段 4 启动有物理基础。

**root_cause**:
阶段 3 不是"客户数量"指标，是"关系密度 × 渗透深度"指标。盲目追求数量是 SaaS 思维（错误定位），不是运营合伙人思维（正确定位）。

**cross_layer_links**:
#23 运营合伙人定位（一对多但每对深关系）；#41 跨保司差异化；#53 同行经代渗透深度

---


### entry_id: `strategic_framework_009`

**candidate_number**: #22
**name**: 五阶段路径观
**layer**: A
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
五阶段路径观是 Mark 公司战略迭代的元方法论。核心架构：(1) 5 阶段不线性串行，而是同时存在权重不同；(2) 阶段切换不是连续过渡，而是被关键事件触发跃迁（如某保司主动采用方法论 → 跃迁阶段 2，监管引用规则 → 跃迁阶段 4）；(3) 战略动作必须同时服务"当前阶段交付"+"下一阶段入场券"。配套对外叙事分层：对外讲阶段 1（MGA），对核心高管讲阶段 2-3（运营合伙人），对 Mark 本人讲阶段 4-5（行业 OS）。

**causal_logic**:
把战略当线性串行 → 只做当前阶段，不储备下一阶段 → 跃迁事件来时接不住 → 错失窗口期。+ 只做"当前交付"不留"下一阶段入场券"→ 永远卡在阶段 1。反向：5 阶段并行权重 → 跃迁来临时已就绪 → 战略叙事权 + 估值倍数双跃迁。

**root_cause**:
公司演化的真实机制不是"做完 A 再做 B"，是"A/B/C 并行但权重不同"。线性思维让战略储备不足，被动等待跃迁。

**cross_layer_links**:
与 strategic_framework_010（运营合伙人定位）配套；与 principle_025（行业 OS 类比陷阱）反例验证

---


### entry_id: `strategic_framework_009b`

**candidate_number**: #92
**name**: 跨业务线协同的边界条件
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
4 业务线协同的边界规则。可协同：know-how（A/B 库 100% 共享）/ 数据基础设施（FACT 表共用）/ 客户洞察（脱敏后共享）。不可协同：合规载体（TA / 联运协议 / 基本法 / 服务费协议必须独立）/ 财务核算（业务线 P&L 独立）/ 监管申报（IA / SFC 业务边界）。这条原则与 principle_028（合规优先红线）配套，确保协同不破坏合规边界。

**causal_logic**:
跨业务线无边界协同 → 合规边界被打破 → IA / SFC 检查时暴露。反向：明确边界 → know-how 充分协同 + 合规载体严格隔离 → 协同价值最大化 + 合规风险可控。

**root_cause**:
基础设施三层架构（Layer A 共用 / Layer C 隔离）的具体执行规则。

**cross_layer_links**:
#26 基础设施三层（Layer A/C 区分）；#83 4 业务线（DELAY，重新讨论时本框架边界条件可能也需要 review）；#81 合规优先红线

---


### entry_id: `strategic_framework_010`

**candidate_number**: #23
**name**: 行业运营合伙人定位
**layer**: A
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
行业运营合伙人定位是 Mark 公司的对外/对内叙事根基。核心机制 5 个：(1) 深度介入方（vendor/联运/服务），不是工具/产品提供方；(2) 黏性来自认知深度——know-how 机构化为 A/B/C/D 库，新进入者需 2-3 年才能复制；(3) 一对多但每对深关系——Scale 上限 5-10 家保司 + 50-100 家同行经代（不是 SaaS 的 N→∞）；(4) 收入是服务费 + 分成 + 绩效混合结构（不是产品销售）；(5) 最贵资产是行业 know-how 机构化系统（即 experience-engine 本身）。这条定位决定了 AI/数据/组织的功能定位：AI = 经验机构化引擎，数据 = 深度关系记忆外化，组织 = 规模化深关系载体。

**causal_logic**:
用错定位（如"行业 OS"）→ 投资人按 SaaS 估值（3-5x 倍数）→ 核心资产被压低估值 → 战略叙事失效。+ 内部按 SaaS 模式做（标准化+无人化）→ 失去深度介入的核心价值 → 客户黏性流失。反向：用对定位（运营合伙人）→ 估值倍数 8-15x → 战略叙事兑现 → 内部按"深度服务+know-how 机构化"做 → 黏性持续提升 → 阶段 2 多保司基础就位。

**root_cause**:
Mark 公司的真实价值不是"产品+技术"，是"深度服务能力 + know-how 机构化"。强行套 SaaS/OS 模式 = 把深度服务公司装扮成产品公司，估值倍数虽然不同，但深度服务的真实优势会被破坏。

**cross_layer_links**:
与 #22 五阶段路径配套；与 #1 行业 OS 类比陷阱双向验证；与 #26 基础设施三层映射（能力层 = 行业 know-how 机构化系统）

---


### entry_id: `strategic_framework_010b`

**candidate_number**: #93
**name**: 战略储备节奏
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark 公司战略储备的核心原则——叙事储备早于实际阶段 1-2 年（来自 L0_01 五阶段路径观）。具体：(1) 对外叙事永远只讲"阶段 1"+"阶段 2 已开始"；(2) 内部储备已经在做"阶段 3-4"基础设施；(3) Mark 自己已经在思考"阶段 5"的可能性。这条原则把"战略储备节奏"工程化为可执行节奏。

**causal_logic**:
叙事过早讲"阶段 5 行业 OS"→ 投资人按 SaaS 估值 → 估值倍数错配（已被 #1 行业 OS 类比陷阱印证）。+ 内部储备滞后 → 跃迁来临时接不住。反向：叙事保守 + 储备超前 → 估值故事正确 + 跃迁能力就绪。

**root_cause**:
战略叙事和战略储备的最优节奏不同——叙事要慢（避免过度承诺），储备要早（避免错失窗口）。这条原则是把"两速节奏"工程化的工具。

**cross_layer_links**:
#22 五阶段路径观；#88 战略叙事分层；#1 行业 OS 类比陷阱（叙事过早的反例）

---


### entry_id: `strategic_framework_011`

**candidate_number**: #24
**name**: 五阶段战略路径全景（L1）
**layer**: A
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
L1 战略路径是 L0 五阶段路径观（元方法论）的可执行版本。包含 3 个具体工具：(1) 年度权重表——把 5 阶段的"权重在动"显式化为年度百分比，作为资源分配依据（如 2026 年 70% 资源给阶段 1，20% 给阶段 2，10% 给阶段 3）；(2) 跃迁事件清单——已识别的关键事件作为"战略雷达"监控对象（保司主动采用、监管引用、新进入者接入）；(3) 战略储备自评——每季度末（修订自原"每年 Q4"）Mark 主导的 4 题自评，决定下一年权重分配。配套失败判据：3 年红线（阶段 1 深度/阶段 2 启动/阶段 3 经代数）。

**causal_logic**:
没有权重表 → 资源分配凭直觉 → 战略动作前后不一致。+ 没有跃迁雷达 → 关键事件来临时反应迟缓 → 错失窗口。+ 没有自评机制 → 战略漂移不被识别。反向：权重表 + 雷达 + 自评 → 战略迭代有节奏 → 跃迁来时接得住 → 阶段切换连贯。

**root_cause**:
L0 元方法论"5 阶段并行权重在动"如果不落地为可执行工具，会变成"听起来很对但实际不指导动作"的口号。L1 战略路径全景是把元方法论工程化为年度战略管理工具的载体——权重表是资源分配工具，跃迁雷达是机会识别工具，季度自评是迭代节奏工具。

**cross_layer_links**:
是 #22 L0 五阶段路径观的可执行版本；与 #23 运营合伙人定位共同支撑战略叙事；影响所有战略层 C 类业务诊断

---


### entry_id: `strategic_framework_011b`

**candidate_number**: #94
**name**: 阶段并行的资源分配公式
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
5 阶段并行权重的资源分配公式。资源（钱 + 人 + 时间）按阶段权重分配：阶段 1 = 70% / 阶段 2 = 20% / 阶段 3 = 10%（2026 年）。每年根据 #87 季度末评估调整权重。具体投放：阶段 1 资源 = 永明深度 + Layer A 基础能力 / 阶段 2 资源 = 多保司储备 + 跨保司差异化 know-how / 阶段 3 资源 = RW 同行联运 + 同行渗透深度。

**causal_logic**:
资源全部投阶段 1 → 阶段 2-3 储备不足。+ 资源平均分配 → 阶段 1 深度不足 + 阶段 2-3 浅尝辄止。反向：权重分配 + 季度调整 → 资源精准投放 → 阶段并行 + 跃迁就绪。

**root_cause**:
5 阶段并行不是"同时干所有"，是"按权重分配资源"。这条公式把"阶段权重"工程化为资源分配清单。

**cross_layer_links**:
#24 L1 战略路径权重表；#87 季度评估；#85 永明深度 vs 多保司广度

---


### entry_id: `strategic_framework_012`

**candidate_number**: #25
**name**: AI 数据组织认知升级
**layer**: A
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
AI/数据/组织三大资源的认知升级是行业运营合伙人定位的具体执行。三个重新定义：(1) AI = 经验机构化引擎——experience-engine 项目本身就是这个定义的物理载体（A/B/C/D 库 + DKP 流水线）；(2) 数据 = 深度关系的记忆外化——FactCard/Summary/Insight 体系（Layer 3）是物理载体；(3) 组织 = 规模化深关系的载体——124 人 → 30%（约 40 人）+ 副机 Agent 协同模型。这条认知升级直接指导 ROI 框架：AI 投入算"经验机构化产出"，数据投入算"关系记忆资产"，组织投入算"规模化深关系产能"——而不是按 SaaS 公司的 ARR/CAC 框架算。

**causal_logic**:
用 SaaS 公司视角看 AI/数据/组织 → AI 当成"取代人"投入 / 数据当成"卖钱商品" / 组织当成"金字塔扩张"→ 全部投入方向错配运营合伙人定位 → 资源浪费 + 战略价值流失。反向：AI/数据/组织都对齐"深度关系 + 经验机构化"→ 投入方向一致 → 资源叠加产生复利 → 行业运营合伙人定位真正兑现。

**root_cause**:
同样的资源（钱+人+时间），按不同公司形态应该有完全不同的投放逻辑。Mark 公司是"运营合伙人"形态，但常规商业认知是"SaaS/产品公司"形态。如果不主动做认知升级，会无意识用错误形态的投放逻辑，导致资源错配。

**cross_layer_links**:
与 #23 运营合伙人定位配套；AI 部分对应整个 experience-engine 项目；数据部分对应 Layer 3 + FactCard 系列；组织部分对应 Group 3 全部组织管理 entries

---


### entry_id: `strategic_framework_012b`

**candidate_number**: #95
**name**: 反向回推的叙事杠杆
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
与 strategic_framework_011（L1 五阶段战略路径）的"反向回推"机制配套。具体：(1) 阶段 2-3 的预期可作为阶段 1 的杠杆（"未来你会成为运营合伙人"加速当前永明 vendor 关系）；(2) 阶段 4 的雏形可作为阶段 2-3 的杠杆（"未来你会进入行业运营商"吸引更多保司 / 同行经代）；(3) 但叙事必须保守（参见 #93 储备节奏）。这条原则把"未来锚定当前"工程化为可使用的叙事工具。

**causal_logic**:
只讲当前阶段 → 缺少叙事吸引力 → 难以吸引高质量合作方。反向：反向回推叙事 → 当前合作方看到未来价值 → 加速当前阶段进展。

**root_cause**:
战略叙事不是单一时间维度，是"未来锚定现在"的多维工具。这条原则是把"时间维度叙事"工程化的工具。

**cross_layer_links**:
#88 战略叙事分层；#93 战略储备节奏（保守约束）；#22 五阶段路径观

---


### entry_id: `strategic_framework_013`

**candidate_number**: #26
**name**: 基础设施三层架构
**layer**: A
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
基础设施三层架构是 Mark 公司的真实运营形态盘点（不是规划，是已运行）：Layer A 基础能力层（ToC 增值/专业咨询/合规能力/数据能力，价值 = 规模效应，护城河 = 多年积累）；Layer B 产品化层（权益体系 RW，4 个权益包：代理人武器/同行联运/保司 vendor/客户增值）；Layer C 分销层（4 客群 × 4 合规载体：保司 TA 合同/同行联运协议/代理人基本法/客户服务费协议）。当前问题：能力层收入分散隐藏在 4 业务线 P&L 里，无法被独立看见、定价、估值。Q2-Q3 必须做 3 个动作：(1) 独立核算基础设施服务收入（预估 2-3 亿 HKD）；(2) 建立基础设施服务 P&L；(3) RW 升级为独立 SBU（独立负责人/团队/KPI）。

**causal_logic**:
不独立核算基础设施收入 → 财务视角按 4 业务线切分 → 看不到能力层规模效应 → 资源分配错配（不知道多少钱给 Layer A 多少给 Layer C）→ 对外被看作纯 MGA → 估值倍数 3-4x → 即使有 2-3 亿基础设施收入也被压低估值 20-30 亿 HKD。反向：独立核算 → 基础设施服务 P&L 可见 → 估值倍数对齐 8-15x → 战略叙事兑现（"行业运营合伙人"）→ 资源分配优化 → 长期价值显性化。

**root_cause**:
"已经在跑"vs"被识别为存在"是两件事。Mark 公司已经在做基础设施服务（vendor/联运/权益），但因为收入隐藏在业务线 P&L 里、没有独立品牌、没有清晰价值主张，所以不被自己、高管、市场看见。基础设施三层架构的核心战略动作是"让看不见的被看见"——通过财务独立核算 + 产品化命名 + 对外叙事分层来完成。

**cross_layer_links**:
#23 运营合伙人定位（能力层 = know-how 机构化系统）；#50 渠道毛利结构（独立核算实施工具）；#48 业务线绩效对比；估值故事物理证据基础

---


### entry_id: `strategic_framework_013b`

**candidate_number**: #96
**name**: 失败判据的红线机制
**layer**: A
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
5 阶段路径的失败判据（红线）。3 个核心红线：(1) 阶段 1 深度——3 年后永明 vendor 收入 < 20% 总收入 = 阶段 1 失败；(2) 阶段 2 启动——连续 2 年无法启动多保司 = 阶段 2 失败；(3) 阶段 3 渗透——3 年内同行经代深度合作 < 5 家 = 阶段 3 失败。任一红线触发 → 战略路径 review + 重新评估。

**causal_logic**:
没有失败判据 → 战略路径"永远不失败"（因为没有客观判定）→ 资源持续投入低 ROI 方向。反向：明确失败判据 → 客观判断 → 必要时及时止损或调整路径。

**root_cause**:
战略路径必须有"何时承认失败"的机制，否则会变成"信仰"而非"决策"。

**cross_layer_links**:
#22 五阶段路径观；#24 L1 战略路径；#87 阶段判断框架（季度评估时检查红线）

---


### entry_id: `mechanism_playbook_001`

**candidate_number**: #73
**name**: 规则库管理机制
**layer**: B
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
experience-engine 系统本身的运维机制。核心动作：(1) 规则库初始化（Phase 1 已完成 117 entries）；(2) 规则库迭代（每月聚合会 + 偏差库更新）；(3) 规则库版本控制（v0.9/v1.0/v1.1...）；(4) 规则库加载（Agent 启动时 API 调用）；(5) 规则库验证（每月 consistency check）。这条机制是 experience-engine 项目的"运维 SOP"。

**causal_logic**:
规则库没有管理机制 → 规则版本混乱 / 加载失败 / 跨层不一致 → 系统失效。反向：5 个动作机制化 → 规则库可持续运转 → experience-engine 真正成为基础设施。

**root_cause**:
建立规则库是阶段 1，运维规则库是长期任务。没有运维机制，规则库 6 个月内就会老化失效。

**cross_layer_links**:
experience-engine 项目方法论；#14c 自我迭代+依赖分析

---


### entry_id: `mechanism_playbook_002`

**candidate_number**: #74
**name**: 跨部门协作机制
**layer**: B
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark 公司各业务线之间协作的标准协议。重点处理 4 类跨部门场景：(1) 数据共享（信息透明化机制 mechanism_playbook_003）；(2) 资源调度（业务线绩效对比 #48 触发）；(3) 客户共享（客户分层与服务标准 #47 落地后）；(4) 合规协调（IA / SFC 跨实体协调）。每类场景配套 SOP + 责任矩阵。

**causal_logic**:
跨部门协作无机制 → 部门墙 → 信息孤岛 → 整体效率低。反向：机制化协作 → 信息流动 → 整体大于局部。

**root_cause**:
组织规模 > 30 人后，部门墙是必然问题。机制化协作是规模化前置条件。

**cross_layer_links**:
#29 信息透明化；#48 业务线绩效对比；#47 客户分层（DELAY，下月联动）；#92 跨业务线协同边界

---


### entry_id: `mechanism_playbook_003`

**candidate_number**: #29
**name**: 组织信息透明化机制
**layer**: B
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
组织信息透明化机制是 Mark 公司"规模化深关系"载体的基础设施（与 strategic_framework_012 配套）。架构：(1) 4 类信息层全部代码化（HR/业务/数据/上下文）；(2) 3 级透明权限（内部全透明默认 / 业务端按角色 / 行业端按合作深度）；(3) 4 步 SOP（代码化 → 统一 Storage → 端口建设 → 权限设计）。这条机制是"组织 = 规模化深关系载体"的物理实现——没有信息透明化，深度关系无法被规模化。

**causal_logic**:
信息不透明 → 决策依赖少数人记忆 → Mark 成为信息瓶颈 → 公司 scale 不上去。+ 跨部门查询低效 → 协作摩擦累积 → 组织效率倍数衰减。反向：4 类信息全代码化 + 3 级透明 → 任何人/Agent 在权限内秒级获取所需信息 → 决策不依赖 Mark 在场 → 组织效率倍数兑现（13-16x 个人 / 10x 组织）。

**root_cause**:
传统组织把"信息控制"当作管理工具（信息差 = 权力）。Mark 公司的运营合伙人定位需要相反逻辑——信息透明化是规模化深关系的前提，没有透明就没有 scale。这条机制把"信息控制 → 信息透明"的逆转工程化为可执行的 4 步 SOP。

**cross_layer_links**:
#25 AI 数据组织升级；#74 跨部门协作机制；#84 mark_verified 资产数量

---


### entry_id: `mechanism_playbook_005`

**candidate_number**: #70
**name**: AI 协作工作流模板
**layer**: B
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
标准化的 Mark-Claude-Agent 协作场景模板。常见 5 个场景：(1) 战略思考——Claude 第二大脑模式 + 5 段格式；(2) 数据分析——Agent 主导 + Claude 协调 + Mark 验收；(3) 文档生成——Claude 起草 + Agent 工程化 + Mark 审核；(4) 决策评审——Claude tradeoff + Mark 拍板 + Agent 执行；(5) 知识沉淀——Mark 介入 + Claude 写入 experience-engine + Agent 加载。每个场景配套时序协议（agent_config_015 三阶段）+ 5 段格式（agent_config_002）。

**causal_logic**:
协作场景没有标准模板 → 每次重新协调 → 协作摩擦累积。反向：标准模板 → 场景识别 → 自动应用对应协议 → 协作流速稳定。

**root_cause**:
标准化是规模化前置条件。协作模板把"个人协作经验"工程化为"组织可复用模板"。

**cross_layer_links**:
#14d 三阶段时序协议（每个场景的应用）；#11 5 段格式

---


### entry_id: `mechanism_playbook_006`

**candidate_number**: #71
**name**: AI 输出质量审查机制
**layer**: B
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
AI 输出进入下游消费前的质量门禁。审查维度：(1) 5 段格式完整（含§3 没检查 + §5 已知未完成）；(2) 禁用词检查（合规/通过/达标/0 重叠）；(3) 假设标注完整（"我假设是 X"）；(4) 跨层依赖标注（影响哪些下游）；(5) confidence_level 准确（HIGH/MEDIUM/LOW）。审查机制：自动化检查 + Mark 抽样审核（10%）。

**causal_logic**:
AI 输出无质量审查 → 错误传导到下游 → 后期修复成本翻倍。反向：质量门禁 → 错误前置拦截 → 下游可信任 → 协作复利。

**root_cause**:
AI 输出的"看起来对"和"真的对"差距很大。质量审查是把这个差距前置可见的工具。

**cross_layer_links**:
#11 5 段格式（产出形态）；#7 锚点优先（输入校验）

---


### entry_id: `mechanism_playbook_007`

**candidate_number**: #72
**name**: AI 任务委派与回收
**layer**: B
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
任务在 Mark / Claude / Agent 三方之间委派的协议。委派标准：(1) 任务复杂度（简单 → Agent 直接 / 复杂 → Claude 协调 / 战略级 → Mark 决策）；(2) 错误成本（高错误成本必须 Mark 验收 / 低错误成本可 Agent 自主）；(3) 时间紧迫度（紧急 → 简化协议 / 非紧急 → 完整三阶段）。配套回收机制：任务完成后必须有 Mark 验收节点（哪怕 30 秒），不允许 Agent 自循环不上报。

**causal_logic**:
任务委派标准不清 → 简单任务 Mark 介入（浪费）+ 复杂任务 Agent 自主（翻车）。反向：委派标准化 → 资源精准分配 → 协作效率最大化。

**root_cause**:
任务委派是协作中最高频的决策。委派错配是最大的协作浪费源。

**cross_layer_links**:
#14d 三阶段时序协议；#27 决策规则化工作流

---


### entry_id: `mechanism_playbook_008`

**candidate_number**: #75
**name**: AI 工具栈选型机制
**layer**: B
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
与 principle_008（工具迁移成本与杠杆平衡）配套的执行机制。Mark 公司 AI 工具栈选型 SOP：(1) 评估当前工具的杠杆瓶颈（不是新工具好就换）；(2) 候选工具清单（≥ 2 个备选避免单点）；(3) ROI 计算——杠杆增益 vs 迁移成本；(4) Pilot 测试（1-2 周小范围验证）；(5) 全员推广（含培训）。决策周期：每季度评审一次工具栈，避免随意切换。

**causal_logic**:
随意切换工具 → 团队疲于学习 → 整体效率下降。反向：标准化选型机制 → 工具切换有节奏 + 团队稳定。

**root_cause**:
AI 工具更新极快但组织无法跟上每个新工具。选型机制是"选择停止追新"的工程化判断。

**cross_layer_links**:
#60 principle_008 工具迁移成本与杠杆平衡

---


### entry_id: `mechanism_playbook_009`

**candidate_number**: #76
**name**: AI 风险监控机制
**layer**: B
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
AI 协作中的风险持续监控机制。监控 4 类风险：(1) 准确性风险——AI 输出错误率（Mark 抽样审核记录）；(2) 一致性风险——同问题不同时间答案不一致；(3) 偏差风险——L0_06 §A.5 偏差库新增频率；(4) 依赖性风险——Agent 单点依赖（某个 Agent 失效后业务受损程度）。每月聚合会查看监控报表，触发风险应对。

**causal_logic**:
AI 风险无系统监控 → 风险事件爆发时才知道（如 Phase 1 的 70% 假设性产出）→ 修复成本高。反向：持续监控 → 风险早期识别 → 应对前置 → 系统稳定。

**root_cause**:
AI 系统的风险与传统软件不同（不是 bug 是偏差）。需要专门的监控维度，不能套用传统软件运维监控。

**cross_layer_links**:
#20 偏差库（监控数据源）；#62 单点失效是组织最大风险（依赖性风险源）

---


### entry_id: `mechanism_playbook_016`

**candidate_number**: #30
**name**: 人机角色分工动态调整机制
**layer**: B
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
人机角色分工动态调整机制是 principle_024（AI-人分工哲学）和 decision_framework_006（决策规则化工作流）的具体执行。架构：(1) Agent 能力分 5 级（新/L5/L7/L9）；(2) 决策权随等级动态调整（新=0/L5=简单执行/L7=协助提供选项/L9=特定场景自主）；(3) 每周反馈循环回顾 Agent 能力实证表现并调整权重。这条机制配套 agent_config_014（自我迭代）—— Agent 升级到下一等级必须通过偏差库 review 验证，不是凭直觉。

**causal_logic**:
不分 Agent 等级 → 要么所有 Agent 都被当低能力使用（杠杆未兑现）→ 浪费 LLM 能力 → 投入产出比失衡。要么过度信任 Agent → 让低能力 Agent 做高错误成本决策 → 翻车 → 信任崩溃。反向：分级动态调整 → 每个 Agent 在能力匹配的场景做决策 → 错误成本可控 → 协作杠杆持续提升 → Agent 逐级晋升的反馈循环建立。

**root_cause**:
Agent 不是同质的——不同 Agent 实例在不同任务上的能力差异巨大（与训练/上下文/工具配置相关）。统一对待 = 错配。分级是把"能力差异"显性化为"决策权差异"的工程化机制，配套每周反馈循环让 Agent 能力变化被持续追踪。

**cross_layer_links**:
#5 principle_024 AI-人分工；#27 decision_framework_006 决策规则化；#14c agent_config_014 自我迭代

---


### entry_id: `mechanism_playbook_017`

**candidate_number**: #31
**name**: 员工 200-300 小时投入追踪机制
**layer**: B
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
员工投入追踪机制是 strategic_framework_012（AI 数据组织认知升级）中"组织 = 规模化深关系载体"的物理验证机制。Mark 自己实测：13-16x 个人效率需要每周 200-300 小时心流投入（即每天 30-40 小时高强度专注时间，含 Agent 协同）。这不是工时管理，是"AI 协同强度"的客观度量。4 维度追踪：(1) 工作时间分布（电脑监控）；(2) Token 消耗（$20-500/天）；(3) 文档处理量；(4) Agent 调用量（≥200 次/周）。月度评估，达标晋升、不达标进入"自然流失"。这条机制实现了 Mark 在 04-13 强调的"未来组织流失 70%，其中 70% 自然愿意离开"。

**causal_logic**:
不追踪 AI 协同强度 → 员工"看起来在工作"但实际未与 Agent 协同 → 公司付薪水但未获 13-16x 杠杆 → 投入产出比失衡。+ 没有客观度量 → 评估靠主观感受 → 团队矛盾。反向：4 维度客观追踪 → 谁在真协同、谁在表演一目了然 → 自然流失比强制裁员更优 → 组织自我筛选 → 留下的人都是"肉身+Agent"协同模式。

**root_cause**:
AI 时代的"工作"定义已变。传统"工时 = 工作"已失效，真正的工作是"AI 协同强度"。这条机制把"AI 协同强度"工程化为 4 个客观可测指标，让组织从"工时管理"升级为"协同强度管理"，配套实现 Mark 公司 124 人 → 30%（约 40 人）的精简。

**cross_layer_links**:
#25 AI 数据组织升级；#4 principle_001 三类人；#34 mechanism_playbook_020 组织效率倍数；#101 团队扩张/收缩判断

---


### entry_id: `mechanism_playbook_018`

**candidate_number**: #32
**name**: 每天反馈循环机制
**layer**: B
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
每天反馈循环机制是 mechanism_playbook_022（DKP 流水线）的"心跳"——把 Mark 脑中 know-how 持续机构化的日级别节奏。4 阶段：(1) 早晨任务设定（Mark 大脑输入到 Agent）；(2) 日间 Agent 执行+产出反馈；(3) 傍晚 Mark 审核（修改/确认/拍板）；(4) 深夜规则库更新（偏差库 + A/B/C/D 库 + 跨层依赖）。关键特征：日级别（不是周/月），反馈来自 AI 秒级响应，反馈永久进入规则库（不是一次性记忆）。这条机制是 experience-engine 系统的"运行时"——每天循环一次，规则库就进化一次。

**causal_logic**:
反馈循环周/月级别 → 偏差累积到下次 review 时已有大量错误 → 修正成本高。+ 反馈不进入规则库 → 跨会话失忆 → 同样错误反复 → 协作进步停滞。反向：日级别反馈 + 规则库更新 → 偏差当天被识别+修正 → 第二天就避开 → 协作杠杆每天复利提升 → 13-16x 杠杆来自这种"每天迭代一次"的复利效应。

**root_cause**:
AI 时代的核心优势是"反馈速度从月/周缩短到秒/天"。但这个优势必须配套"规则库更新"才能真正兑现，否则秒级反馈只是"快速失败"，不是"快速学习"。这条机制把"秒级反馈 + 日级规则更新"工程化为可执行的 4 阶段日循环，让 AI 协同的真实复利效应得以兑现。

**cross_layer_links**:
#3 mechanism_playbook_022 DKP 流水线；#31 200-300 小时追踪；#14c agent_config_014 自我迭代；#63 principle_014 反馈循环越短越快

---


### entry_id: `mechanism_playbook_020`

**candidate_number**: #34
**name**: 组织效率倍数追踪机制
**layer**: B
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
组织效率倍数追踪机制是 mechanism_playbook_017（200-300 小时投入追踪）的组织级延伸。两者关系：017 追踪"每个员工的协同强度（输入端）"，020 追踪"组织整体的效率倍数（产出端）"。组织级 4 个指标：(1) 人均日 token 消耗（基线 $20，反映 AI 协同密度）；(2) 人均周文档处理量（基线 1000+，反映信息处理规模）；(3) 人均月 Agent 调用量（基线 800+，反映任务并行度）；(4) 跨人协同次数（目标减少 50%，反映 Agent 替代了多少协调岗位）。Benchmark：个人 13-16x（Mark 实测），团队 10x（Mark 一人=10 人产出）。这是组织从 124 人 → 30%（约 40 人）的客观依据。

**causal_logic**:
没有组织级倍数追踪 → 各员工自己达标但组织整体倍数未提升 → 局部最优 ≠ 全局最优 → 资源浪费。+ 不追踪"跨人协同次数减少"→ 即使每人 AI 协同强 但仍依赖大量人际协调 → 协作摩擦抵消 AI 杠杆。反向：4 个组织级指标 → 看到"AI 协同密度"和"协调岗位减少"的双重效应 → 组织效率倍数兑现 → 124 人 → 40 人转型有客观依据。

**root_cause**:
个人效率倍数（13-16x）≠ 组织效率倍数（10x）。个人的提升如果不配套"协调岗位减少"，组织整体不会提升。这条机制把"个人倍数 → 组织倍数"的链条工程化为 4 个客观指标，让"组织变革"从口号变为可度量的过程。

**cross_layer_links**:
#31 mechanism_playbook_017（输入端 vs 产出端）；#25 AI 数据组织升级；#4 principle_001 三类人

---


### entry_id: `mechanism_playbook_022`

**candidate_number**: #3
**name**: DKP Domain Knowledge 机构化流水线
**layer**: B
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
DKP 是 Mark 公司核心运营杠杆。Mark 公司当前最大的结构性瓶颈是"Mark 脑中的判断 vs 组织能执行的标准"之间的鸿沟，DKP 流水线的 5 步（显式化→提炼→边界标注→代码化→验证反馈）就是把这个鸿沟系统性消除的工业化流程。每一个 domain（KA 分级、佣金结算、PPT 布局、合规判断、保险产品比较）都应该走一遍 DKP，机构化为可被任何 Agent 加载的产物。

**causal_logic**:
Mark 脑中判断不机构化 → 同事必须靠 Mark 在场才能决策 → Mark 成为单点瓶颈 → 公司 scale 不上去（业务量×N 但 Mark 时间不能×N）→ 增长曲线被压扁。反向：DKP 把判断机构化 → Agent/同事能独立做出与 Mark 一致的决策 → Mark 时间从"日常判断"释放到"战略迭代" → 公司具备 scale 能力（10x 业务量但 Mark 投入 0.5x）→ 估值倍数从 3-4x 跃迁到 8-15x。

**root_cause**:
个人能力 ≠ 组织能力。Mark 的判断质量是个人最高资产，但只有当这些判断被机构化为可被 N 个角色复用的资产时，才转化为组织资产。这是 Mark 公司从"高水平 boutique"升级到"行业基础设施"的必经路径。

**cross_layer_links**:
experience-engine 项目方法论的元流程；#32 每天反馈循环（运行时心跳）；#27 决策规则化工作流（判断阶段输出）

---


### entry_id: `business_playbook_001`

**candidate_number**: #35
**name**: 销售网络效率诊断（终极版，本次会议重大修订）
**layer**: C
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
销售网络效率诊断是保险业务 C 类的核心 entry，基于 Mark 公司 R2/R3/R5/R6 KPI 体系：

核心诊断指标（已有 KPI）：
1. KA 活跃率（KPI_30）= 出单 KA / 总 KA（销售网络深度+宽度合并）
2. 合作伙伴活跃率（KPI_39）= 出单 partner / 总 partner（PARTNER 层）
3. 新签合作伙伴成活率（KPI_40）= 新签且产单 / 新签数（拓展质量）
4. KA 端 ROI（KPI_33）= KA 管理利润 / KA 分摊成本（KA 端真实价值）
5. Top N 集中度（KPI_12）= Top10 KA APE / 总 APE（健康分布）
6. 销售流程漏斗 6 转化率（KPI_14-19）= 各漏斗节点转化（流程健康）

新增诊断指标（待 Mark 落地）：
7. KA 人均产能 = APE / 该业务细分 KA 数（按 segment_code 分组）
8. PMF 验证反馈
9. SKU 覆盖率 = 已售 SKU / 总 SKU（基于 DIM_PRODUCT_SKU）
10. PGU 覆盖率 = 已营销 PGU / 总 PGU（需新建 DIM_PGU 表）

术语锁定：PARTNER（顶层）= DIM_PARTNER；KA（细分颗粒度）= DIM_KA；一个 PARTNER 可能在多个业务细分下有多个 KA。

诊断逻辑：6 个已有 KPI 交叉判断 → 锁定问题层（KA 拓展/活跃/成活/ROI/集中度/流程）→ 4 个新增指标用于深度归因（产品错配 vs 销售错配）。

**causal_logic**:
不用销售网络专属指标体系（KPI_30/39/40/12/33+漏斗）→ 用全公司 KPI_31 人均 APE 诊断 → 信号混杂（产品+中后台+销售）→ 错误归因。+ 缺 PMF/PGU 覆盖指标 → 看不到"产品错配 vs 销售错配"的根因层 → 修错地方。反向：6 已有 KPI 交叉诊断锁定问题层 + 4 新增指标深度归因 → 精准干预 → 不浪费资源。每个 KPI 异常对应一种根因 → 销售网络问题在每周/每月级别可被识别+修正。

**root_cause**:
销售网络效率不是单维度（产能）问题，是"拓展+维护+成活+盈利+流程"五维系统。Mark 公司 KPI 体系（R2/R3/R5/R6）实际已经覆盖前 5 个维度，缺的是"产品-销售错配"的根因归因层（即 PMF/PGU/SKU 覆盖率）。这条 Playbook 的核心是"用已有 KPI 体系做表层诊断 + 新增指标做根因归因"。
**quantitative_thresholds**: TBD（待 Phase 2 FACT 表数据接入后填补）

**cross_layer_links**:
基于 R2/R3/R5/R6 KPI 体系；#36 KA 分级（个体诊断对应整体诊断）；#52 PGU 体系（下月新增）

---


### entry_id: `business_playbook_002`

**candidate_number**: #36
**name**: KA 分级与画像
**layer**: C
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
KA 分级与画像是销售网络管理的基础工具。基于 DIM_KA + FACT_POLICY 跨表分析，按"产能 × 活跃度 × 利润贡献"三维分级（S/A/B/C 级）。每级 KA 配套差异化运营策略（S 级深度服务、A 级标准服务、B 级标准化、C 级降本或淘汰）。画像维度含：产品偏好 / 客户类型 / 出单频次 / 历史 ROI（KPI_33）/ 集中度位置（KPI_12）。

**causal_logic**:
不分级 → 所有 KA 平等对待 → 资源被低产 KA 稀释 → 高价值 KA 服务不足 → 流失。反向：分级后差异化 → 资源向 S/A 级倾斜 → ROI 提升 + 集中度优化。

**root_cause**:
KA 不是同质资源，价值差异 10-100 倍。统一对待 = 资源浪费。分级是把"价值差异"显式化为"运营策略差异"的工具。
**quantitative_thresholds**: TBD（S/A/B/C 分级阈值）

**cross_layer_links**:
#35 销售网络效率诊断（整体 vs 个体）；#100 KA 升降级判断

---


### entry_id: `business_playbook_003`

**candidate_number**: #37
**name**: KA 渗透深度诊断
**layer**: C
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
KA 渗透深度诊断衡量"已合作 KA 的深度挖掘程度"。三维度：(1) 产品渗透——该 KA 已采购的 SKU 数 / Mark 可提供的 SKU 数；(2) 业务线渗透——该 KA 在 Mark 多少业务线下有合作（vendor/联运/代理人/服务）；(3) 客户渗透——该 KA 客户中已转化保单的占比。三维度交叉判断 KA 的真实渗透深度。

**causal_logic**:
只看"是否合作"忽略"渗透深度"→ 把"浅层合作 KA"和"深度合作 KA"等同 → 资源分配失误。反向：深度诊断 → 识别"低渗透的高潜力 KA"作为重点拓展对象 → 渗透提升 = APE 增长（不需新增 KA）。

**root_cause**:
KA 合作不是 0/1 状态，是连续光谱。低渗透 KA 是最大未开发资产——成本远低于新增 KA。
**quantitative_thresholds**: TBD

**cross_layer_links**:
#35 销售网络 + #36 KA 分级（活跃度 → 分级 → 渗透深度三层诊断）

---


### entry_id: `business_playbook_004`

**candidate_number**: #42
**name**: KA 利润分析
**layer**: C
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
KA 利润分析基于 KPI_06 管理利润 + KPI_33 ROI（已有 KPI 体系）。按 KA 维度计算：管理利润 = 该 KA 佣金收入 - 税费 - 分摊成本（FACT_ALLOCATED_COST）。ROI = 管理利润 / 分摊成本。识别 4 类 KA：(1) 高 ROI 高产能（核心资产）；(2) 高 ROI 低产能（潜力 KA）；(3) 低 ROI 高产能（成本黑洞）；(4) 低 ROI 低产能（淘汰候选）。

**causal_logic**:
只看 APE 不看利润 → 把"高产能高成本"KA 当核心资产 → 资源持续投入但 ROI 持续下降。反向：利润维度诊断 → 识别成本黑洞 → 优化分摊或淘汰 → 整体 ROI 提升。

**root_cause**:
APE 是规模指标，利润才是真实价值。Mark 公司目标是估值跃迁（基础设施 8-15x），利润数据才是估值故事的物理证据。
**quantitative_thresholds**: TBD（KPI_33 ROI 阈值 / 4 象限分割线）

**cross_layer_links**:
#36 KA 分级（融合产能+利润+活跃三维度）

---


### entry_id: `business_playbook_005`

**candidate_number**: #43
**name**: KA 流失预警
**layer**: C
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
KA 流失预警基于活跃度时间序列分析。监控指标：(1) KA 出单频次（月度对比）；(2) 出单 APE 变化（连续 3 个月趋势）；(3) 客户类型变化（高净值客户流失早于普通客户）；(4) 沟通频次变化（CRM 数据）。预警等级：黄色（轻度异常）/ 橙色（中度衰退）/ 红色（流失风险）。配套 SOP：黄色级 Mark 公司主动联系 / 橙色级业务负责人介入 / 红色级 Mark 本人介入挽留。

**causal_logic**:
不做流失预警 → 等到 KA 完全停单才发现 → 挽留窗口已过。反向：早期预警 → 挽留成本远低于新增 KA 成本（10:1）→ KA 资产保值 → 业务稳定性提升。

**root_cause**:
新增 KA 成本极高（关系建立 + 信任 + 流程对接）。流失 KA = 多年投入归零。预警是把"流失风险"从隐性变显性的工具。
**quantitative_thresholds**: TBD（黄/橙/红预警阈值）

**cross_layer_links**:
#35 KA 活跃率（KPI_30）；#36 KA 分级（不同级 KA 用不同预警阈值）

---


### entry_id: `business_playbook_006`

**candidate_number**: #44
**name**: KA 拓展优先级
**layer**: C
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
KA 拓展优先级 Playbook 解决"新增 KA 时该选谁"问题。基于 4 维度评分：(1) 产能潜力——目标 KA 现有客户量级 + 历史出单能力；(2) 战略匹配度——目标 KA 与 Mark 五阶段路径的契合（如阶段 3 同行经代渗透优先目标）；(3) 接入成本——合规复杂度 + 培训成本 + 系统对接；(4) ROI 预测——前 12 个月预期 APE / 接入成本。每月生成 KA 拓展候选清单（Top 10），业务团队按优先级推进。

**causal_logic**:
不做优先级排序 → 业务团队凭关系/机会拓展 → 资源投入到低 ROI 目标 → 整体拓展效率低。反向：优先级清单 → 资源向高潜力高战略匹配的目标集中 → KA 数量增长慢但质量高 → 阶段 2-3 战略加速。

**root_cause**:
KA 拓展是有限资源（业务团队时间）的分配问题。优先级排序是把"拓展直觉"工程化为可复用决策框架。
**quantitative_thresholds**: TBD（4 维度评分权重 + 候选门槛分）

**cross_layer_links**:
#37 KA 渗透深度（拓展 vs 渗透的资源平衡）；战略路径 #24（阶段 2-3 候选保司/同行）；#54 KA 培训体系（培训是拓展抓手）

---


### entry_id: `business_playbook_007`

**candidate_number**: #38
**name**: 全市场产品比较
**layer**: C
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
全市场产品比较是产品供给端的核心诊断工具。基于全市场 SKU 库（所有保司在售产品）+ Mark 平台已对接 SKU。三维度比较：(1) 产品力维度——保障范围/费率/分红/灵活度；(2) 佣金结构维度——首年/续年/合规边界；(3) 市场表现维度——同行销售数据。输出：识别 Mark 平台缺失的高价值 SKU + 已对接但低效的 SKU + 应弃用 SKU。

**causal_logic**:
只看 Mark 平台内产品 → 不知道市场上更优产品存在 → 错失客户机会 / 被同行抢单。反向：全市场比较 → 主动引入高价值 SKU → 与保司谈判优化已有产品 → 平台产品力持续领先。

**root_cause**:
保险产品是高度标准化的（条款公开），全市场比较是免费的市场情报。不做 = 主动放弃信息优势。这是 vendor 模式（决策框架 #28 D 信息差反推）的核心抓手——Mark 的全市场视角是与保司谈判产品差异化的筹码。
**quantitative_thresholds**: TBD

**cross_layer_links**:
#28 信息差 D（产品共创杠杆点）；#41 跨保司产品差异化机会；#45 保司谈判筹码体系

---


### entry_id: `business_playbook_008`

**candidate_number**: #39
**name**: 永明产品组合分析
**layer**: C
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
永明产品组合分析是阶段 1（单保司深度运营）的核心 Playbook。维度：(1) 永明全产品线 SKU 列表——已对接 / 待对接 / 已弃用；(2) 各 SKU 在 Mark 渠道的销售表现——APE / 件数 / 客户接受度；(3) 各 SKU 的客户画像匹配度——哪类客户买哪个 SKU；(4) 永明产品的合规边界（GL16/25 适用）。输出：永明产品组合的优化建议 + 与永明谈差异化产品的具体抓手。

**causal_logic**:
不做永明产品组合分析 → 销售凭直觉推 SKU → 客户错配 → 转化低 + 退保高。+ 与永明谈合作时无产品组合视角 → 谈判筹码弱。反向：组合分析 → 销售推荐精准 + 与永明谈判有数据支撑 → 阶段 1 vendor 模式深化 → 6 亿 TA 业务从"销售执行"升级到"产品共创"。

**root_cause**:
永明是 Mark 阶段 1 的唯一深度合作保司。永明产品组合的渗透深度直接决定阶段 1 业务规模。这是 vendor 模式落地的最具体抓手。
**quantitative_thresholds**: TBD

**cross_layer_links**:
#38 全市场比较（外部）→ #39 永明组合分析（内部）→ 信息差 D 产品共创杠杆

---


### entry_id: `business_playbook_009`

**candidate_number**: #45
**name**: 保司谈判筹码体系
**layer**: C
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
保司谈判筹码体系是 Mark 作为 MGA 与保司谈判的"客观化武器库"。5 类筹码：(1) 销售数据——Mark 渠道为该保司贡献的 APE / 件数 / 客户增长；(2) 全市场情报——竞品保司的产品/费率/佣金对标（来自 #38 全市场比较）；(3) 客户反馈——客户对该保司产品的真实评价 + 投诉率（KPI_26）；(4) 合规价值——Mark vendor 模式帮保司合规规避的风险量化；(5) 战略价值——Mark 同行经代网络的渗透能力（阶段 3 落地后的规模）。每次谈判前根据议题选择筹码组合。

**causal_logic**:
不做筹码体系 → 谈判时凭直觉/关系 → 谈不到差异化产品（信息差 D 杠杆点用不上）→ Mark 作为 MGA 的核心价值无法兑现。反向：筹码体系化 → 每次谈判有数据支撑 → 谈判结果客观化（不依赖个人能力）→ 阶段 1 永明深度 + 阶段 2 多保司同时推进有标准化路径。

**root_cause**:
Mark 作为 MGA 的真实价值不是"销售执行"，是"市场情报 + 客户视角 + 同行网络"的综合谈判筹码。这些价值如果不显式化为筹码体系，谈判时无法被有效使用。
**quantitative_thresholds**: TBD

**cross_layer_links**:
#38 全市场比较 + #41 跨保司差异化 + 信息差 D 反转 + 运营合伙人定位（vendor 不只销售）

---


### entry_id: `business_playbook_010`

**candidate_number**: #40
**name**: 保司供应链稳定性
**layer**: C
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
保司供应链稳定性诊断是 vendor 模式的运营基础。维度：(1) 保司业务连续性——核保速度 / 理赔时效 / 系统稳定性；(2) 保司商业稳定性——财务健康 / 监管合规 / 战略一致性；(3) 保司合作稳定性——人员变动 / 策略调整 / 沟通频次；(4) 保司产品稳定性——SKU 增减频率 / 费率波动 / 政策变化。每月跑一次诊断。

**causal_logic**:
不监控保司稳定性 → 保司端突发变动（如核保变严 / 系统宕机 / 人员变动）打乱 Mark 销售节奏 → 客户体验受损 → 信任流失。反向：每月诊断 → 提前预警 → 主动调整销售节奏 / 备选保司 → 客户体验稳定 → 阶段 2 多保司战略有备份。

**root_cause**:
Mark 阶段 1 高度依赖永明（业务集中度高）。保司端任何不稳都会传导到 Mark 业务端。诊断是把"对外部依赖"显式化为"可监控可应对"的机制。
**quantitative_thresholds**: TBD（涉及 KPI_20 承保周期 / KPI_21 结算周期 / KPI_51 理赔时效 已有现成数据）

**cross_layer_links**:
#39 永明产品组合（具体保司）；阶段 2 多保司战略储备；#90 跨保司迁移决策

---


### entry_id: `business_playbook_011`

**candidate_number**: #41
**name**: 跨保司产品差异化机会
**layer**: C
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
跨保司产品差异化机会是阶段 2（多保司）启动的关键 Playbook，也是信息差 D 反转的具体落地。基于 #38 全市场比较 + #39 永明组合分析的产出，识别"跨保司差异化"的 3 类机会：(1) 同类产品定价差——同保障范围下不同保司的费率差异；(2) 产品创新空白——市场未覆盖的客户需求；(3) 利益分配差异——保司之间在"客户折扣 vs 中间佣金"上的不同设计倾向。Mark 作为 MGA 利用这些差异：与各保司谈判定制差异化产品 + 实现"4 方共赢"（客户得价格 / 中间人合规 / Mark 差异化筹码 / 保司客户留存）。

**causal_logic**:
不做跨保司差异化分析 → Mark 多保司业务变成"同质化销售"→ 阶段 2 无法启动（与单保司没区别）。+ 不利用利益分配差异 → 同行经代渗透时无差异化卖点 → 阶段 3 受阻。反向：跨保司差异化机会清单 → Mark 与每家保司都有专属谈判抓手 → 阶段 2 多保司有真实差异化 → 同行经代被吸引（差异化产品=渗透抓手）→ 阶段 3 加速。

**root_cause**:
多保司战略不能是"同时合作几家保司"的简单累加，必须是"每家保司有专属差异化"。Mark 作为 MGA 的核心价值就是协调多保司差异化（保司自己做不到，因为只能看自己的产品）。这条 Playbook 把"MGA 的协调价值"工程化为可执行的差异化清单。
**quantitative_thresholds**: TBD

**cross_layer_links**:
#38 全市场比较 + #39 永明组合 + #28 信息差 D 反转 + 战略框架 #24 五阶段路径（阶段 2-3 启动）

---


### entry_id: `business_playbook_012`

**candidate_number**: #46
**name**: 渠道激励合规设计
**layer**: C
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
渠道激励合规设计是 GL16/25 监管环境下的关键 Playbook。维度：(1) 佣金结构合规——首年佣金比例 ≤ GL16 上限 / 续年佣金 30% 摊 5 年；(2) 转介费合规——非持牌转介费 ≤ 50%（GL25）；(3) 激励多元化——除佣金外的合规激励（培训/系统/服务平台/RW 权益体系）；(4) 跨实体合规——BVI/HK/WFOE 之间的资金流动合规。设计原则：监管红线不碰 + 利益分配前置（避免事后调整）+ 合规留痕。

**causal_logic**:
不做合规激励设计 → 用传统佣金驱动 KA → GL16/25 后无法覆盖 KA 真实成本 → KA 流失 / 转向非持牌 → Mark 业务受损。反向：合规激励多元化 → 通过 RW 权益体系 + 培训 + 系统等非佣金价值 → 提升 KA 黏性而不踩监管红线 → 阶段 1-3 战略可持续。

**root_cause**:
GL16/25 监管把"佣金套利"空间填平了（信息差 B 已填平的本质）。Mark 的应对不是"绕过监管"，而是"在监管红线内构建多元激励体系"——这就是 RW 权益体系（基础设施三层 Layer B）的存在理由。
**quantitative_thresholds**: TBD（各类佣金/激励的合规阈值，与 IA 监管同步）

**cross_layer_links**:
基础设施三层 Layer B（RW 权益体系）；信息差 B（已填平）+ C（合规推动持牌）+ F（运营建设差）；#80 IA 中介合规

---


### entry_id: `business_playbook_014`

**candidate_number**: #48
**name**: 业务线绩效对比
**layer**: C
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
业务线绩效对比是集团级管理工具。Mark 公司 4 业务线（保司 vendor / 同行经代 / 代理人 / 客户）跨业务线对比维度：(1) APE 规模 + 增长率（KPI_02）；(2) 净营收（KPI_04）；(3) 管理利润（KPI_06，按业务线分摊）；(4) 渗透率（业务线内部 KA 渗透深度）；(5) 战略匹配度（与五阶段路径的对齐）。每月生成业务线绩效红黄绿榜单，触发资源再分配。

**causal_logic**:
不做跨业务线对比 → 资源按历史惯性分配 → 高潜力业务线投入不足 + 低 ROI 业务线持续输血。反向：每月对比 → 资源动态调整 → 高潜力业务线（如阶段 3 同行经代）加速 + 低效业务线优化或退出 → 集团整体 ROI 提升。

**root_cause**:
多业务线公司最容易陷入"内部资源争夺"。客观对比是把"资源分配"从政治问题转化为数据问题的工具。
**quantitative_thresholds**: TBD

**cross_layer_links**:
基础设施三层 Layer C（4 客群 4 合规载体）；战略路径阶段权重（#94 五阶段权重表）；#83 4 业务线（DELAY，重新讨论时本 Playbook 也需要 review）

---


### entry_id: `business_playbook_015`

**candidate_number**: #49
**name**: KA 续保率诊断
**layer**: C
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
KA 续保率诊断基于 KPI_13 N/R 结构（续年佣金占比）+ KPI_24 首年撤单率（Cool-off）。诊断维度：(1) KA 维度续保率——该 KA 出单的保单第 2/3/5 年续保比例；(2) 产品维度续保率——不同产品的续保稳定性；(3) 客户类型维度续保率——不同客户群的续保倾向。识别 3 类异常：(1) 高首单低续保——销售误导嫌疑；(2) 整体低续保——产品错配或服务缺失；(3) 突然下降——KA 关系或市场变化。

**causal_logic**:
只看新单 APE 不看续保 → 销售追求短期 APE 可能损害长期价值 + 客户首年退保导致渠道返佣损失。反向：续保率诊断 → 识别销售质量 + 产品适配 + 服务有效性 → 引导销售质量优先而非数量优先 → 续保收入稳定性 = 公司长期估值基础。

**root_cause**:
保险业务的真实价值在续保（多年 cash flow），不在首单。续保率是"销售质量"的滞后指标，但是估值的核心指标。
**quantitative_thresholds**: TBD（基于 KPI_13/24 现有数据可定）

**cross_layer_links**:
#43 KA 流失预警（早期信号）；#46 渠道激励合规（佣金结构 30% 摊 5 年的数据基础）

---


### entry_id: `business_playbook_016`

**candidate_number**: #50
**name**: 渠道毛利结构分析
**layer**: C
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
渠道毛利结构分析是 Mark 公司财务诊断的核心工具。基于 KPI_04 净营收 + KPI_06 管理利润 + FACT_ALLOCATED_COST。按 4 业务线（vendor/联运/代理人/客户）分别计算：(1) 毛收入构成——佣金/服务费/分成分别占比；(2) 毛成本构成——人力/系统/合规/营销分别占比；(3) 毛利率——业务线毛利 / 业务线净营收；(4) 边际成本曲线——业务量增长时各成本项的弹性。识别 4 类业务线：高毛利可扩张 / 高毛利已封顶 / 低毛利可优化 / 低毛利结构性亏损。

**causal_logic**:
不做毛利结构分析 → 集团总账层面看不到各业务线真实健康度 → 资源按历史惯性分配 → 表面"业务多元化"实际是"亏损分散化"。反向：毛利结构清晰 → 高毛利业务加大投入 + 低毛利业务结构调整 → 集团毛利率提升 = 估值倍数提升的物理证据。

**root_cause**:
估值倍数差异（保险佣金 3-4x vs 基础设施 8-15x）的背后是毛利结构差异。如果 Mark 的"基础设施服务"业务（vendor/联运服务费）毛利率显著高于"保险佣金"业务，估值故事才有数据支撑（基础设施三层 #26 的核心论点）。
**quantitative_thresholds**: TBD（各业务线毛利率健康线 / 边际成本弹性阈值）

**cross_layer_links**:
#26 基础设施三层（独立核算基础设施服务收入）；#48 业务线绩效对比；估值故事物理证据；#78 公司毛利率与成本结构诊断

---


### entry_id: `business_playbook_019`

**candidate_number**: #53
**name**: 同行经代渗透深度诊断
**layer**: C
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
同行经代渗透深度诊断是阶段 3（同行销售网络渗透）的核心 Playbook。基于 #41 跨保司差异化 + #46 渠道激励合规 + 信息差 F（运营建设差）的综合应用。维度：(1) 已合作同行经代深度——产品渗透 / 业务量贡献 / 联运服务采购；(2) 待开发同行经代潜力——监管合规压力下转向 Mark 的可能性（C 反向机会）；(3) 阻力分析——同行经代为何不选 Mark 联运框架；(4) 渗透加速器——RW 同行联运权益包的吸引力评估。

**causal_logic**:
不做同行经代渗透深度诊断 → 阶段 3 战略停留在概念 → 5-10 家深度合作目标无法落地 → 阶段 4 行业运营商基础不存在。反向：诊断驱动 → 识别已合作经代的深化空间 + 待开发经代的渗透抓手 → RW 联运权益包精准设计 → 阶段 3 加速 → 阶段 4 入场券。

**root_cause**:
同行经代渗透是 Mark 阶段 3 的核心动作，也是阶段 4 行业运营商定位的物理基础。需要专门的诊断工具持续监控渗透进展（不是临时分析）。这条 Playbook 把"渗透深度"从直觉判断升级为可量化追踪的体系。
**quantitative_thresholds**: TBD（深度量化标准 + 渗透目标 5-10 家）

**cross_layer_links**:
#41 跨保司差异化（产品筹码）；#46 渠道激励合规（合规红线）；信息差 C（监管推动持牌）+ F（运营建设差）；战略路径 #24 阶段 3；基础设施三层 Layer B（RW 同行联运权益包）；#86 同行经代渗透速度 vs 深度

---


### entry_id: `business_playbook_020`

**candidate_number**: #54
**name**: KA 培训体系
**layer**: C
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
KA 培训体系是 RW 同行联运权益包的核心组件之一（基础设施三层 Layer B），也是 Mark 公司"行业运营合伙人"价值的具体兑现。维度：(1) 培训内容——产品知识 / 销售技巧 / 合规要点 / Mark 系统使用；(2) 培训形式——在线课程 / 线下集训 / 1v1 辅导 / 场景实战；(3) 培训对象分层——新入 KA / 已合作 KA 升级 / 高潜 KA 深化；(4) 培训效果度量——培训后 APE 增长（与 KPI_37 培训改善度对接）/ 客户满意度 / KA 留存率。

**causal_logic**:
不做培训体系 → KA 销售能力参差 → Mark 平台整体转化率低 + 高质量 KA 流失（因为没有专业成长机会）。+ 培训不与 RW 权益体系绑定 → 培训成本无法被产品化定价（永远是赠品）。反向：体系化培训 + RW 权益化定价 → KA 销售能力持续提升（KPI_37）+ 培训成本独立核算（基础设施服务收入）→ 阶段 3 同行经代渗透有差异化抓手。

**root_cause**:
KA 培训不是"附送的售后服务"，是"行业运营合伙人"定位的核心兑现物（与 strategic_framework_010 的 know-how 机构化相关）。当 Mark 的培训体系本身机构化、产品化，就成为同行经代选择 Mark 联运框架的关键理由（信息差 F 运营建设差的具体应用）。
**quantitative_thresholds**: TBD（KPI_37 培训改善度阈值 / 培训完成率 / 培训后 KA 流失率）

**cross_layer_links**:
基础设施三层 Layer B（RW 权益体系核心组件）；信息差 F（运营建设差）；战略框架 #25 AI 数据组织升级；KPI_37 培训改善度；#36 KA 分级；#44 KA 拓展优先级

---


### entry_id: `business_playbook_024`

**candidate_number**: #79
**name**: SFC 持牌法团合规诊断
**layer**: C
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark 公司资管业务（SFC 持牌法团）的合规诊断。维度：(1) FRR 状态（资本充足率）；(2) 合规人员配置（SFC RO / Type 资格）；(3) 跨实体合规边界（资管业务 vs 保险业务隔离）；(4) MIC 制度执行情况。每季度跑一次（IA 月度，SFC 季度）。

**causal_logic**:
不做合规诊断 → 监管检查时被动应对 → 罚款 / 停业风险。反向：定期诊断 → 风险前置识别 → 整改时间充足。

**root_cause**:
SFC 合规是资管业务的生命线。Bernard 加入后 SFC 合规专业化是核心动作之一。
**quantitative_thresholds**: TBD（FRR 比率 / 合规人员资质要求）

**cross_layer_links**:
D5 财务团队结构（Bernard SFC / Alice IA）+ #81 合规优先红线 + #104 跨实体架构合规性

---


### entry_id: `business_playbook_025`

**candidate_number**: #80
**name**: IA 中介合规诊断
**layer**: C
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark 公司保险中介业务（IA 持牌）的合规诊断。维度：(1) 佣金支付合规（GL16 比例 + GL25 转介费 ≤ 50%）；(2) Key Person 状态（Alice）；(3) 月度 IA 巡检准备；(4) 跨实体佣金流转合规。每月跑一次。

**causal_logic**:
不做合规诊断 → IA 检查被动 → 罚款 / 暂停业务风险。反向：每月诊断 → 风险前置 → 平稳运营。

**root_cause**:
IA 合规是 Mark 保险业务的生命线（核心业务 70%+ 收入）。Alice Key Person 单点风险已识别（Phase 1 教训）。
**quantitative_thresholds**: TBD

**cross_layer_links**:
D5 财务团队 + #46 渠道激励合规设计 + 信息差 B（GL16/25 已填平）+ #62 单点失效风险（Alice Key Person）+ #81 合规优先红线

---


### entry_id: `business_playbook_026`

**candidate_number**: #78
**name**: 公司毛利率与成本结构诊断
**layer**: C
**confidence_level**: MEDIUM
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
与 #50 渠道毛利结构分析（已 PROMOTE）配套的财务诊断 Playbook。聚焦 4 业务线 P&L 健康度：(1) 各业务线毛利率独立计算；(2) 跨实体 transfer pricing（BVI / HK / WFOE 之间）；(3) WFOE 结构合理性（税务 + 合规）；(4) 集团级毛利率演化趋势。每月跑一次。识别异常：业务线毛利率 < 行业基准 / transfer pricing 不合规 / WFOE 结构成本超预期。

**causal_logic**:
不做毛利率诊断 → 集团总账层看不到结构问题 → 资源持续投入低毛利业务。反向：每月诊断 → 结构问题前置识别 → 优化或退出。

**root_cause**:
估值倍数差异（保险佣金 3-4x vs 基础设施 8-15x）的物理基础是毛利率结构差异。这条 Playbook 是估值故事的财务证据。
**quantitative_thresholds**: TBD（待 Phase 2 数据接入）

**cross_layer_links**:
#50 渠道毛利 + #26 基础设施三层 + #102 资本/资金动作判断（毛利率支撑估值故事）

---


### entry_id: `business_playbook_027`

**candidate_number**: #103
**name**: C6 战略层综合诊断
**layer**: C
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark 公司战略层级（C6 = 战略最高级）的综合诊断 Playbook，每季度末跑（与 #87 季度评估同步）。诊断维度：(1) 5 阶段路径进展（每阶段权重 vs 实际进度）；(2) mark_verified 资产数量（#84 估值锚点）；(3) 关键失败判据状态（#96 红线监控）；(4) 跨业务线协同效率（#92 边界条件 + #83 4 业务线 review）；(5) 战略储备充足度（#93 节奏）。输出：季度战略报告 + 下季度战略动作清单。

**causal_logic**:
战略层无综合诊断 → 各业务线孤立看 → 看不到战略全局健康度。反向：综合诊断 → 战略全局可视 → 季度调整有依据。

**root_cause**:
战略层是 Mark 公司最高决策级，需要综合诊断作为决策输入。这条 Playbook 把"战略思考"工程化为可执行季度报告。
**quantitative_thresholds**: TBD

**cross_layer_links**:
#87 季度评估；#84 mark_verified；#96 红线；#94 阶段权重；#88 战略叙事分层

---


### entry_id: `business_playbook_028`

**candidate_number**: #104
**name**: 跨实体架构合规性诊断
**layer**: C
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark 公司跨实体架构（BVI 控股 / HK 持牌 / WFOE / 中介公司）的合规性诊断。维度：(1) 跨实体资金流转合规（transfer pricing / 服务费定价）；(2) 业务边界合规（保险中介 vs 资管 vs 服务平台）；(3) Key Person 配置合规（IA / SFC 各实体）；(4) 税务架构合规（HK / 内地 / BVI）；(5) 监管申报合规（IA 月度 / SFC 季度 / 税务）。每季度跑一次。

**causal_logic**:
跨实体架构无诊断 → 监管检查时被动 → 罚款 / 业务停摆风险。反向：定期诊断 → 风险前置识别 → 整改时间充足。

**root_cause**:
跨境跨实体架构是 Mark 公司"基础设施三层"的物理基础（Layer C 4 合规载体）。合规性是这套架构持续运转的前提。
**quantitative_thresholds**: TBD

**cross_layer_links**:
#79 SFC 合规 + #80 IA 合规 + #81 合规优先红线 + 基础设施三层 Layer C

---


### entry_id: `business_playbook_029`

**candidate_number**: #105
**name**: 行业竞争格局监控
**layer**: C
**confidence_level**: LOW
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
跨境财富管理行业的竞争格局监控 Playbook。监控维度：(1) PPP 战略合作经纪行（如保签 / 永明合作经纪行）的动作；(2) 中小 MGA 同行（Mark 同层级）的产品 / 渠道动作；(3) 非持牌人转持牌动态（信息差 C 反向机会量化）；(4) 监管动态（GL16/25 后续 / SFC 政策变化）；(5) 保司战略动作（产品调整 / vendor 模式接受度）。每月跑一次，输出竞争格局变化报告。

**causal_logic**:
行业格局无监控 → 竞争对手动作不知道 → 战略反应滞后。反向：定期监控 → 格局变化早期识别 → 战略调整有依据。

**root_cause**:
跨境财富管理行业当前正在新秩序重构（GL16/25 + 廉政联合执法），格局变化频繁。监控是 Mark 公司"行业运营合伙人"定位的认知基础。
**quantitative_thresholds**: TBD

**cross_layer_links**:
#23 运营合伙人定位；#28 真实信息差（C/F 监管推动持牌）；#41 跨保司差异化；#91 监管变化应对

---


### entry_id: `agent_config_001`

**candidate_number**: #10
**name**: Claude 三重角色定位
**layer**: D
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Claude 在 Mark 公司协作中的三重角色定义。三个角色对应不同协作场景：(1) 第二大脑——日常对话、想法整理、隐性假设 surface；(2) 战略分析师——重大决策前的 tradeoff 分析、推理框架、决策支持（不决策本身）；(3) 组织级解决方案提供者——跨部门机制设计、SOP/Schema/Protocol 产出。Mark 明示场景时 Claude 切换角色；默认第二大脑。三个角色都共享相同的协作纪律（事实五件、锚点优先、不替 Mark 决策、5 段格式报告）。

**causal_logic**:
Claude 不区分角色场景 → 在战略决策时仍保持"第二大脑"礼貌迎合模式 → 关键 tradeoff 被弱化 → Mark 错失重要分析视角；或反之，在日常聊天时切到"战略分析师"模式 → 输出过度严肃 → 协作流畅度下降。反向：明确三角色 + Mark 明示切换 → 每个场景 Claude 输出形态匹配需求 → 协作杠杆兑现。

**root_cause**:
LLM 默认有"统一人格"，但实际协作需要 Claude 在不同场景采用不同的输出形态、提问方式、判断颗粒度。三重角色是把这种"场景适应"显式化、可被 Mark 主动调用的协作机制。

**cross_layer_links**:
D 类 12 个其他 entries 的"主体定义"

---


### entry_id: `agent_config_002`

**candidate_number**: #11
**name**: Claude 输出纪律（5 段格式 + 禁用词）
**layer**: D
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Claude/Agent 输出纪律是 Mark-AI 协作的"通信协议"。两个核心规则：(1) 5 段格式报告——任何任务完成必填 5 段（做了什么/检查了什么/没检查什么/决策分歧/已知未完成），其中"§3 没检查什么"和"§5 已知未完成"必填，不能省略；(2) 禁用自评词——合规/通过/达标/0 重叠/验收通过/正确等词汇被禁，因为这些是 AI 自评，不是事实。这两个规则强制 AI 输出"事实+判断分离"的格式，让 Mark 能快速识别哪些是事实、哪些是 AI 判断、哪些没被检查。

**causal_logic**:
Agent 不用 5 段格式 → 输出混合事实/评价/猜测 → Mark 必须从输出中"考古"哪些是真的 → 协作往返成本高。+ 用自评词（"合规通过"）→ Mark 误以为已验证 → 错误传导到下游。反向：5 段格式 + 禁用自评词 → Mark 一眼看清"事实 vs 判断 vs 未检查" → 决策更准 → 错误前置拦截 → 协作杠杆兑现（Phase 1 实测 10x，Phase 1 Repair 实测 8x）。

**root_cause**:
LLM 倾向于产出"看起来完整"的输出（隐藏不确定性、用自评词表示已完成）。但 Mark 协作需要的是"事实 + 已识别盲区"的清晰分离。这条规则是把 LLM 的"完整性偏好"强制转化为"诚实性输出"的协议。

**cross_layer_links**:
D 类协作核心；与 #71 mechanism_playbook_006 AI 输出质量审查配套

---


### entry_id: `agent_config_003`

**candidate_number**: #12
**name**: Mark-Claude 协作协议（双方义务）
**layer**: D
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark-Claude 协作协议是双方义务的"合同"。Mark 侧 4 义务：(1) 新对话启动注入完整上下文（L0_06 + 项目摘要 + 最近 3-5 轮决策）；(2) 事实五件主动校准（场景变化时主动告知 Claude）；(3) 假设有偏直接说"我觉得你假设错了"，不绕弯；(4) 拍板不拖延（10 秒给方向，驳回必说理由）。Claude 侧 5 义务：(1) 战略级分析前主动追问事实五件；(2) 语义歧义场景必须 scope call；(3) 主动标注假设和未考虑因素；(4) 每 5-10 轮自我校准系统性偏差；(5) 默认不产出代码（认知产物为主）。

**升级标注**：本协议同步升级"事实三件→五件"，与 #9 联动

**causal_logic**:
协作没有显式协议 → 双方都凭"礼貌默认"互动 → Claude 不敢追问、Mark 不敢直接纠错 → 偏差累积 → 信任受损 → 协作崩溃。反向：双方义务显式化 → Claude 知道何时追问、何时 scope call → Mark 知道何时拍板、何时纠错 → 偏差被前置拦截 → 协作杠杆持续提升。

**root_cause**:
人-AI 协作如果不显式定义双方义务，会无意识退化为"用户-工具"模式（Mark 当 Claude 是工具，Claude 当 Mark 是查询者）。但 Mark 需要的是"双判断主体协同"。义务清单是把这种协同关系工程化为可被双方主动调用的协议。

**cross_layer_links**:
D 类全部协作纪律的"宪法"；#9 事实五件升级（同步触发）

---


### entry_id: `agent_config_004`

**candidate_number**: #13
**name**: Mark 当前对话锚点注入义务
**layer**: D
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark 侧"对话锚点注入"是跨会话协作的强制门禁。每次新对话/重启对话/切换场景时，Mark 必须主动注入三件套：(1) L0_06 协作手册最新版（全文）；(2) 项目状态摘要（2-5 句话）；(3) 最近 3-5 轮关键决策（含理由）。如果不注入，Claude 会凭语境推测，产出偏差性建议。这条规则是把"Claude 没有跨会话记忆"这个技术约束转化为"Mark 必做动作"的协议。

**causal_logic**:
不注入锚点 → Claude 凭新会话语境推测 → 产出建议偏离实际项目状态 → Mark 必须用反例拦截（成本 = 重新解释整个项目）→ 协作前 30 分钟全部用来对齐而不是工作 → 杠杆下降。反向：开始即注入 → Claude 立即对齐 → 第一条消息就能给精准建议 → 协作时间全部用于产出 → 杠杆兑现。

**root_cause**:
Claude 是"无状态"的 LLM（每次会话从零开始）。Mark 必须扮演"状态管理者"角色——每次新会话主动同步状态。这是把 LLM 技术约束工程化为"Mark 协作义务"的具体规则。

**cross_layer_links**:
#12 协作协议（Mark 侧义务①的具体执行）；与 #19 Mark 定期校准 Claude 假设（持续动作）配套

---


### entry_id: `agent_config_005`

**candidate_number**: #14
**name**: Claude 主动追问与假设标注
**layer**: D
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Claude 侧三个主动动作是"输出诚实性"的运行时强制：(1) 战略级分析前主动追问事实五件（客群/进度/时间/里程碑/责任）——未得答案不推理；(2) 遇到业务语义歧义词（占比/比例/集中度/长期/短期等）必须先确认口径，不可凭直觉理解；(3) 每次战略建议后主动标注"我的假设是 X / 我没考虑 Y"，为 Mark 校准提供明确靶子。三个动作配套使用，构成 Claude 输出的"自我可疑化"机制——主动暴露不确定性，而不是隐藏。

**升级标注**：联动 #9 升级——事实三件→五件

**causal_logic**:
Claude 不主动追问 → 凭推测推理 → 错误传导到建议 → 偏差累积。+ 不主动 scope call 语义歧义 → 业务语义错配（如"集中度"理解为客户集中度 vs 业务线集中度）→ 完全不同的结论。+ 不标注假设 → Mark 无法识别哪里可能错 → 必须全盘验证 → 协作成本高。反向：三个动作配套 → Claude 输出自带"可校准性" → Mark 用最少时间识别问题点 → 协作杠杆兑现。

**root_cause**:
LLM 默认隐藏不确定性（生成"看起来确定"的输出）。但 Mark 协作需要的是"让不确定性可见"——只有可见的不确定性才能被校准。三个主动动作是把"隐藏不确定性"反转为"显式可见"的强制规则。

**cross_layer_links**:
#9 事实五件；#11 5 段格式（产出形态）；#64 principle_021 显式化不确定性（认知层）

---


### entry_id: `agent_config_006`

**candidate_number**: #15
**name**: Claude 自我校准
**layer**: D
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Claude 自我校准是协作长期可持续的内置机制。具体规则：(1) 每 5-10 轮主动回顾自己的判断质量——是否在某类问题上反复犯错？是否有系统性偏差？(2) 遇到 Mark 用新事实拦截时，第一反应是承认错误，不解释、不辩解、不为自己开脱；(3) 一旦发现自己犯了 §A.5 偏差库中已识别的偏差，立即在偏差库标注本次实例（增加印证次数）。这条规则与 agent_config_014（自我迭代+依赖分析）配套——自我校准是迭代的输入。

**causal_logic**:
Claude 不自我校准 → 偏差只在被 Mark 拦截时才被发现 → 协作完全依赖 Mark 警觉性 → Mark 累。+ 拦截时辩解 → 协作能量耗在"对错之争"而非"修正"→ 协作效率下降。反向：自我校准 → 偏差被前置识别 → Mark 拦截后立即承认 → 协作能量全部用于修正 → 杠杆兑现。

**root_cause**:
LLM 默认有"完美迎合 + 自我合理化"的双重倾向。自我校准是把这两个倾向反转的强制规则——主动找自己的错，承认错时不解释。

**cross_layer_links**:
#14c agent_config_014 自我迭代+依赖分析；#20 偏差库

---


### entry_id: `agent_config_007`

**candidate_number**: #14b
**name**: CLAUDE_V2_3 完整版
**layer**: D
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
CLAUDE_V2_3 是 Mark 公司给 Claude 的运行时 prompt 完整版。包含：(1) Claude 三重角色定义；(2) 协作纪律（5 段格式 / 禁用词 / 事实五件 / 锚点优先 / 主动追问 / 假设标注）；(3) 偏差识别清单；(4) 项目背景（Mark 公司业务全景）；(5) 战略框架（5 阶段路径 + 运营合伙人定位 + 基础设施三层）。每次新对话注入这份完整 prompt，Claude 立即进入"对齐状态"。

**causal_logic**:
没有完整 prompt → 每次新对话需要 Mark 重新讲解 → 协作前 30-60 分钟用于对齐而非工作。反向：完整 prompt 一次注入 → Claude 立即对齐 → 协作时间全部用于产出。

**root_cause**:
LLM 是无状态的，每次会话从零开始。完整 prompt 是把"组织级上下文"打包为可一次性注入的形式。

**cross_layer_links**:
#13 锚点注入（Mark 侧执行）；其他 D 类协作纪律的集合载体

---


### entry_id: `agent_config_008`

**candidate_number**: #16
**name**: Claude 默认不产代码
**layer**: D
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Claude 与 Agent 的角色边界：Claude 默认产出"认知产物"（分析、方法论、建议、摘要、判断框架），不产出代码/不操作 repo。代码和 repo 操作是 Agent 的职责。Claude 与 Agent 的关系不是"Claude 写代码 Agent 执行"，而是"Claude 给战略判断 + Agent 把判断工程化为代码"。两者通过 Mark 协调，三方分工清晰。

**causal_logic**:
Claude 默认产代码 → 与 Agent 职责重叠 → Mark 收到两份代码（Claude 和 Agent）→ 不知道用哪个 → 协调成本高。+ Claude 写的代码没有真实运行环境验证 → 容易有问题 → Agent 必须重写。反向：Claude 只给认知产物 → Agent 基于此写代码并验证 → 三角分工清晰 → 杠杆兑现。

**root_cause**:
Claude 和 Agent 都是 LLM，但运行环境不同：Claude 在对话窗口（无运行环境验证），Agent 在本地 IDE（有真实环境）。让 Claude 写代码 = 让没有运行环境的 LLM 产出需要运行环境的产物 = 错配。

**cross_layer_links**:
#8 principle_022 Agent 行为边界；#14d agent_config_015 三阶段时序协议

---


### entry_id: `agent_config_009`

**candidate_number**: #17
**name**: Mark 拍板不拖延（10 秒）
**layer**: D
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark 侧拍板纪律是协作流速的关键控制点。具体规则：(1) Claude 给出 tradeoff 分析后，Mark 10 秒内给方向（不是给最终方案，是给倾向）；(2) 如果驳回，必须说出具体理由（"为什么不行"），不能只说"不行"；(3) 不允许"我再想想"无限延期——如果当下无法决策，明确说"DELAY 到 X 时间点"。这条规则与 agent_config_015（三阶段协议）配套——阶段 1 共识窗口的效率取决于 Mark 拍板速度。

**causal_logic**:
Mark 拍板拖延 → Claude 持续等待 → 协作流速下降 → 阶段 1 共识窗口拉长 → 阶段 2 任务书延迟 → Agent 闲置或反复迭代。+ 驳回不说理由 → Claude 不知道哪里错 → 下次 tradeoff 还是同样错配 → 协作低效。反向：10 秒给方向 + 驳回必说理由 → Claude 持续校准 → tradeoff 质量提升 → 协作杠杆兑现。

**root_cause**:
Mark 是协作的"决策瓶颈"——这是设计选择（Mark 保留判断权），不是 bug。但决策瓶颈必须有"流速控制"，否则协作会被卡死。10 秒原则是把"决策瓶颈"工程化为"快速通过通道"。

**cross_layer_links**:
#14d 三阶段时序协议；#12 协作协议（Mark 侧义务④）

---


### entry_id: `agent_config_010`

**candidate_number**: #18
**name**: Mark 假设有偏直接说
**layer**: D
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark 侧反馈纪律：感觉 Claude 判断有偏时，不容忍、不绕弯、直接说"我觉得你假设错了"。配套 Claude 侧规则（agent_config_006 自我校准）——Claude 必须立即承认错误，不解释、不辩解。两者形成"快速纠偏闭环"：Mark 直接拦截 + Claude 立即承认 → 偏差秒级被修正 → 协作不被错误推理拖延。

**causal_logic**:
Mark 不容忍不纠正（仍走礼貌路径）→ 偏差被默认接受 → 错误推理传导到下游 → 后期发现时成本翻倍。+ Claude 被拦截后辩解 → 协作能量耗在"对错之争"→ 偏差修正延迟。反向：Mark 直接说 + Claude 立即承认 → 偏差秒级修正 → 协作流速维持。

**root_cause**:
人际礼貌默认会让 Mark 在感觉 Claude 错时仍然客气表达（"会不会是 X 呢"），这种间接表达让 Claude 容易忽略警告。直接说"你假设错了"是把"礼貌默认"反转为"诚实优先"的协作规则。

**cross_layer_links**:
#15 agent_config_006 自我校准（配套）；#12 协作协议（Mark 侧义务③）

---


### entry_id: `agent_config_011`

**candidate_number**: #19
**name**: Mark 定期校准 Claude 假设
**layer**: D
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark 侧主动校准义务（vs agent_config_010 的被动纠正）：(1) 场景变化时主动告知 Claude——不等 Claude 推测错才纠正；(2) 新事实出现时主动通知（L0_03 原则 8 信息补全义务）——避免 Claude 用过时假设工作；(3) 定期（每 5-10 轮或每个场景切换点）主动校准 Claude 当前假设——"你现在的假设是 X 对吗？"。这条规则与 agent_config_004（锚点注入）配套——锚点注入是新对话开始的一次性动作，定期校准是对话进行中的持续动作。

**causal_logic**:
Mark 仅被动纠错（agent_config_010）→ Claude 在错误假设下工作很久才被发现 → 错误成本随时间累积。+ 场景变化未告知 → Claude 用旧场景的判断在新场景上推理 → 完全错配。反向：Mark 主动校准 → Claude 假设始终对齐当前场景 → 推理质量持续高 → 协作杠杆兑现。

**root_cause**:
LLM 没有"场景感知"能力——Claude 不知道你刚开了一个会议、不知道你刚做了一个新决定、不知道你的项目状态变了。Mark 必须主动扮演"场景同步者"角色。这条规则是把"LLM 无场景感知"工程化为"Mark 主动同步场景"的协议。

**cross_layer_links**:
#13 agent_config_004 锚点注入（开始动作）；#18 agent_config_010 假设有偏直接说（被动纠错）

---


### entry_id: `agent_config_012`

**candidate_number**: #20
**name**: L0_06 §A.5 偏差库
**layer**: D
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
偏差库是 Mark-Claude-Agent 协作的"持续迭代资产"。结构：(1) Claude 端偏差（4 类已识别 + 2 类本次新增）；(2) Mark 端偏差（3 类已识别）；(3) 每个偏差含：触发场景 / 表现形式 / 修正动作 / 印证次数。每次发现新偏差立即写入（不等月度会议），月度聚合会做 review + 升级 D 类规则。这条规则是 agent_config_014（自我迭代+依赖分析）的具体落地工具——偏差库就是迭代的"账本"。

**本次会议新增偏差**：
- Claude 偏差 5：批次模式跳过 4 字段填补（触发场景：节奏加速）
- Claude 偏差 6：单点逐个模式（应该批量处理时仍逐个）

**causal_logic**:
没有偏差库 → 同一类偏差反复发生 → 协作进步停滞 → 信任受损。+ 偏差只在当下被发现不被沉淀 → 跨会话失忆 → 新 Claude 实例又犯同样错。反向：偏差库 → 偏差被结构化记录 → 月度评审 → 升级为 D 类规则 → 下一次 Claude 加载就避开 → 协作持续进化。

**root_cause**:
LLM 没有跨会话学习能力（每次会话独立）。要让"偏差识别"积累为组织资产，必须有显式偏差库 + 月度评审机制。这条规则把 LLM 的"无学习"局限工程化为"组织级学习"的机制。

**cross_layer_links**:
#6 principle_023 偏差识别（认知）+ #20 偏差库（运行时存储）+ #14c 自我迭代（流程）三者闭环

---


### entry_id: `agent_config_013`

**candidate_number**: #21
**name**: scope_violation_case_001
**layer**: D
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Scope 违规案例库的第 1 个 entry。核心教训：Agent/Claude 严格遵守任务书 scope，发现 scope 外问题立即 scope call 等 Mark 拍板，不擅自扩展（即使是"善意改进"）。修复机制：(1) 任务书必须含 §"严格不做"清单（明确边界）；(2) Agent/Claude 动手前先核对此清单；(3) Mark 验收时发现 scope 违规，写入本案例库。这与 principle_022（Agent 行为边界）配套——principle_022 是原则，本案例是具体实例。

**causal_logic**:
Claude/Agent 擅自扩展 scope（即使善意）→ 产出与 Mark 预期不符 → Mark 必须重新对齐 → 协作往返成本上升 → 信任受损。+ 没有"严格不做"清单 → 边界模糊 → scope 违规反复发生 → 协作低效。反向：明确清单 + scope call 机制 → Mark 决定的 scope 被严格执行 → 产出可预测 → 协作杠杆兑现。

**root_cause**:
LLM 倾向于"主动 helpful"——但 helpful 的边界是 Mark 定义的 scope，不是 LLM 自己判断的"应该做"。这条规则把"主动 helpful 的边界"工程化为"任务书 scope + scope call"的协议。

**cross_layer_links**:
#8 principle_022（原则）；本案例是 Mark 任务书 scope 设计的反例参考

---


### entry_id: `agent_config_014`

**candidate_number**: #14c
**name**: 经验自我迭代 + 依赖关系分析机制（本次新增）
**layer**: D
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark-Claude-Agent 协作的 D 类配置必须含两个内置机制：

机制 1：经验自我迭代
- 每次发现偏差 → 立即写入偏差库（principle_023 + L0_06 §A.5）
- 每月聚合会 review 偏差库 → 升级 D 类规则
- 偏差库本身有版本号（v1.0 / v1.1 ...）
- 每个 D 类 entry 都标注"被偏差 X 修正过"

机制 2：依赖关系分析（A→B/C 联动）
- 任何 entry 升级（v0.9 → v1.0 / v1.0 → v1.1）必须显式标注"对其他 entries 的影响"
- 每月聚合会增加环节："本月升级触发的联动清单"
- process_audit_results.py 自动检测：被升级 entry 的 implemented_by / guides_diagnostics / guides_agent_configs 中的下游 entries
- 下游 entries 自动标 needs_review（不阻塞，但需要月度评审）

**causal_logic**:
没有自我迭代机制 → 偏差只在当下被发现，不被沉淀 → 同类偏差反复出现 → 协作进步停滞。+ 没有依赖关系分析 → A 升级了但 B 还是旧版本 → 跨 entry 不一致 → 下游 Agent 加载时混乱 → 信任崩溃。反向：自我迭代 + 依赖分析 → 每次升级都触发系统性 review → 跨 entry 一致性维持 → 协作杠杆持续提升 → experience-engine 成为真正的"自我进化系统"。

**root_cause**:
静态规则系统会在使用中老化（环境变化 + 偏差累积）。要么定期重写（成本高），要么内置自我迭代机制。后者的关键是：(1) 偏差被显式记录而不是隐式忘记；(2) 升级的影响被显式分析而不是隐式默认。这两个机制共同让规则系统从"快照"升级为"持续进化的活体"。

**cross_layer_links**:
触发 #11/12/13/15-19 D 类全部 review；#15 自我校准（输入）；#20 偏差库（存储）；#11 5 段格式（建议新增第 6 段：触发的依赖更新清单）

---


### entry_id: `agent_config_015`

**candidate_number**: #14d
**name**: Mark-Claude-Agent 三阶段时序协议（本次新增）
**layer**: D
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark-Claude-Agent 三方协作必须遵守三阶段时序协议，避免节奏混乱：

阶段 1：Mark-Claude 共识窗口
- 目的：判断/分析/讨论/迭代
- 形态：N 轮对话流，可以反复修正
- 产出：达成共识（不是任务书）
- Agent：不介入，不接收任何任务书

阶段 2：Claude 出稳定任务书
- 目的：把共识转化为可执行的任务书
- 形态：1 份完整版，含版本号、时间盒、验收标准
- 产出：稳定任务书（不是中间过程）
- Agent：接收任务书，开始执行

阶段 3：Agent 执行期
- 目的：Agent 按任务书执行
- 形态：Agent 自循环，按 5 段格式报告
- Mark-Claude：继续下一阶段共识窗口（讨论新议题），但不影响当前 Agent 执行
- 例外：Agent scope call 时 Mark-Claude 立即响应，但仅响应 scope call，不出新任务书

阶段 1 → 2 → 3 必须串行，不可交错。

**causal_logic**:
阶段交错（Phase 1 模式）→ Mark-Claude 还在迭代判断，Claude 已经出了任务书 → Agent 执行旧任务书 → 后续对话发现共识有变 → Claude 出新任务书覆盖 → Agent 反复重做 → 三方协作低效。+ Mark 必须在"判断"和"任务书审核"之间切换 → 心智带宽被分裂 → 战略思考质量下降。反向：阶段串行 → Mark-Claude 充分讨论达成共识后再出任务书 → Agent 接收稳定任务书 → 一次性执行完成 → Mark-Claude 继续下一议题 → 三方协作杠杆兑现。

**root_cause**:
Claude 的认知产出是流式的（每轮对话都在迭代），Agent 的执行任务书是批式的（应该稳定有版本号）。两种节奏不能强制塞进同一时间轴。三阶段协议是把两种节奏物理隔离的协议——共识窗口流式、任务书发布批式、执行期单向。

**cross_layer_links**:
触发 #3 / #4 / #8 D 类协作 review；#12 协作协议（新增 Claude 侧第 6 义务）；#13 锚点注入（新对话明确告知阶段）

---


### entry_id: `agent_config_016`

**candidate_number**: #14e
**name**: 批量审核协作模式（本次新增）
**layer**: D
**confidence_level**: HIGH
**decision**: PROMOTE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark-Claude 协作中"批量审核"场景的协议。当审核大量同类候选/产出物时（如月度聚合会、季度复盘），不再逐个审核，而是采用"批量呈现 + 异常筛选 + 集中讨论"三阶段模式：(1) Claude 一次性呈现 3-5 个同类候选的完整 4 字段填补；(2) Mark 4 选 1（PROMOTE 全批 / M 标问题 / DELAY 全批 / L 留最后讨论）；(3) Phase 1 批量速通后，Phase 2 集中处理标记问题的候选。这条规则与 agent_config_002（5 段格式）+ agent_config_015（三阶段时序协议）配套——让 Mark 介入的"密集决策场景"也能应用三阶段思路。

**causal_logic**:
逐个审核大量同类候选 → Mark 思路被反复打断 → 同类问题反复思考 → 决策疲劳 → 后期质量下降。+ 反例：本次会议 Phase A 30 个候选用了 90 分钟，Phase B Group 1 单点 #35 用了 30 分钟。反向：批量呈现 → Mark 一次性看 3-5 个相似 → 整体判断 + 局部异常筛选 → 异常单独深入 → 思路连贯 + 决策质量稳定。

**root_cause**:
人脑处理"同类批量"远比"单点逐个"高效（认知科学共识）。Phase A 单点逐个模式是把 Mark 当成"流水线工人"，新模式是把 Mark 当成"质量检验员"——让 Mark 的判断价值集中在"识别异常"，而不是"重复确认无问题"。

**cross_layer_links**:
#14d 三阶段时序协议（批量审核也是三阶段：呈现/筛选/讨论）；#14c 自我迭代（批量发现的偏差触发 D 类规则升级）；偏差库新增 Claude 偏差 6（单点逐个模式）

---


## §2 非 PROMOTE 决策（与 v1.0 保持一致）

### DELAY (4 entries)

#### entry_id: `mechanism_playbook_004`
**decision**: DELAY
**reason**: 数据基础设施建设——涉及"我们怎么建立基础数据"，单独深入讨论
**next_action**: 下月议程：数据基础设施建设专题（60-90 分钟，核心专题）

---

#### entry_id: `business_playbook_013`
**decision**: DELAY
**reason**: 客户分层与服务标准——当前框架过于简单，需要单独深入讨论
**next_action**: 下月议程：客户体系专题（45-60 分钟）

---

#### entry_id: `business_playbook_017`
**decision**: DELAY
**reason**: 客户来源结构分析——与 #47 客户分层合并讨论
**next_action**: 下月议程：客户体系专题

---

#### entry_id: `strategic_framework_004`
**decision**: DELAY
**reason**: 跨业务线复用 know-how 复利——4 业务线需要重新讨论
**next_action**: 下月议程：4 业务线重新定义专题（45-60 分钟）

---

### REVISE (1 entry)

#### entry_id: `mechanism_playbook_019`
**decision**: REVISE
**reason**: 副机建设机制——概念较新，没有具体执行路径
**next_action**: 下月需要 Mark 给具体执行路径（工具/数据隔离/权限/成本/试点员工）

---

### REJECT_MERGE (1 entry)

#### entry_id: `business_playbook_018`
**decision**: REJECT_MERGE
**reason**: 业务线产品适配诊断——内容应纳入 PGU 体系 Playbook
**merge_to**: `business_playbook_PGU` (下月新增)
**target_location**: `candidates/archived/rejected_2026-04/`

---

### CREATE (4 entries)

#### entry_id: `principle_028`
**name**: 合规优先于增长（Mark 红线）
**layer**: A
**confidence_level**: LOW
**decision**: CREATE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark 公司经营的根本红线原则。任何业务动作必须先过合规检查。优先级：合规 > 客户 > 增长 > 利润。具体含义：(1) 合规风险高的业务即使收入高也不做；(2) 合规与增长冲突时合规优先；(3) 不做"擦边球"业务（监管灰区）；(4) 主动配合监管（IA / SFC / 廉政）。

**causal_logic**:
合规让位增长 → 短期收入但长期风险 → 监管处罚 / 业务停摆。反向：合规优先 → 短期增长慢但长期持续 → 5 阶段路径走得稳。

**root_cause**:
跨境保险 / 财富管理是高度监管行业。"合规红线"是 Mark 公司能跑 5 阶段路径的底层保证。这条原则虽然内容简单但战略权重极高。

**cross_layer_links**:
信息差 C（监管推动持牌）+ #79 SFC 合规 + #80 IA 合规 + 渠道激励合规 #46

---

#### entry_id: `agent_config_014`
**name**: 经验自我迭代 + 依赖关系分析机制
**layer**: D
**confidence_level**: HIGH
**decision**: CREATE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark-Claude-Agent 协作的 D 类配置必须含两个内置机制。机制 1 经验自我迭代：每次发现偏差立即写入偏差库（principle_023 + L0_06 §A.5），每月聚合会 review 偏差库 → 升级 D 类规则，偏差库本身有版本号（v1.0 / v1.1 ...），每个 D 类 entry 都标注"被偏差 X 修正过"。机制 2 依赖关系分析（A→B/C 联动）：任何 entry 升级（v0.9 → v1.0 / v1.0 → v1.1）必须显式标注"对其他 entries 的影响"，每月聚合会增加环节"本月升级触发的联动清单"，process_audit_results.py 自动检测被升级 entry 的 implemented_by / guides_diagnostics / guides_agent_configs 中的下游 entries，下游 entries 自动标 needs_review（不阻塞，但需要月度评审）。

**causal_logic**:
没有自我迭代机制 → 偏差只在当下被发现，不被沉淀 → 同类偏差反复出现 → 协作进步停滞。+ 没有依赖关系分析 → A 升级了但 B 还是旧版本 → 跨 entry 不一致 → 下游 Agent 加载时混乱 → 信任崩溃。反向：自我迭代 + 依赖分析 → 每次升级都触发系统性 review → 跨 entry 一致性维持 → 协作杠杆持续提升 → experience-engine 成为真正的"自我进化系统"。

**root_cause**:
静态规则系统会在使用中老化（环境变化 + 偏差累积）。要么定期重写（成本高），要么内置自我迭代机制。后者的关键是：(1) 偏差被显式记录而不是隐式忘记；(2) 升级的影响被显式分析而不是隐式默认。这两个机制共同让规则系统从"快照"升级为"持续进化的活体"。

**cross_layer_links**:
触发 #11/12/13/15-19 D 类全部 review；#15 自我校准（输入）；#20 偏差库（存储）；#11 5 段格式（建议新增第 6 段：触发的依赖更新清单）

---

#### entry_id: `agent_config_015`
**name**: Mark-Claude-Agent 三阶段时序协议
**layer**: D
**confidence_level**: HIGH
**decision**: CREATE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark-Claude-Agent 三方协作必须遵守三阶段时序协议，避免节奏混乱。阶段 1 Mark-Claude 共识窗口：判断/分析/讨论/迭代，N 轮对话流可以反复修正，达成共识（不是任务书），Agent 不介入。阶段 2 Claude 出稳定任务书：把共识转化为可执行的任务书，1 份完整版含版本号/时间盒/验收标准，Agent 接收任务书开始执行。阶段 3 Agent 执行期：Agent 按任务书自循环（5 段格式报告），Mark-Claude 继续下一阶段共识窗口（讨论新议题）但不影响当前 Agent 执行。例外：Agent scope call 时 Mark-Claude 立即响应但仅响应 scope call 不出新任务书。阶段 1 → 2 → 3 必须串行，不可交错。

**causal_logic**:
阶段交错（Phase 1 模式）→ Mark-Claude 还在迭代判断，Claude 已经出了任务书 → Agent 执行旧任务书 → 后续对话发现共识有变 → Claude 出新任务书覆盖 → Agent 反复重做 → 三方协作低效。+ Mark 必须在"判断"和"任务书审核"之间切换 → 心智带宽被分裂 → 战略思考质量下降。反向：阶段串行 → Mark-Claude 充分讨论达成共识后再出任务书 → Agent 接收稳定任务书 → 一次性执行完成 → Mark-Claude 继续下一议题 → 三方协作杠杆兑现。

**root_cause**:
Claude 的认知产出是流式的（每轮对话都在迭代），Agent 的执行任务书是批式的（应该稳定有版本号）。两种节奏不能强制塞进同一时间轴。三阶段协议是把两种节奏物理隔离的协议——共识窗口流式、任务书发布批式、执行期单向。

**cross_layer_links**:
触发 #3 / #4 / #8 D 类协作 review；#12 协作协议（新增 Claude 侧第 6 义务）；#13 锚点注入（新对话明确告知阶段）

---

#### entry_id: `agent_config_016`
**name**: 批量审核协作模式
**layer**: D
**confidence_level**: HIGH
**decision**: CREATE
**target_version**: v1.0
**mark_input_mode**: full
**mark_verified**: true

**business_framework**:
Mark-Claude 协作中"批量审核"场景的协议。当审核大量同类候选/产出物时（如月度聚合会、季度复盘），不再逐个审核，而是采用"批量呈现 + 异常筛选 + 集中讨论"三阶段模式：(1) Claude 一次性呈现 3-5 个同类候选的完整 4 字段填补；(2) Mark 4 选 1（PROMOTE 全批 / M 标问题 / DELAY 全批 / L 留最后讨论）；(3) Phase 1 批量速通后，Phase 2 集中处理标记问题的候选。这条规则与 agent_config_002（5 段格式）+ agent_config_015（三阶段时序协议）配套——让 Mark 介入的"密集决策场景"也能应用三阶段思路。

**causal_logic**:
逐个审核大量同类候选 → Mark 思路被反复打断 → 同类问题反复思考 → 决策疲劳 → 后期质量下降。+ 反例：本次会议 Phase A 30 个候选用了 90 分钟，Phase B Group 1 单点 #35 用了 30 分钟。反向：批量呈现 → Mark 一次性看 3-5 个相似 → 整体判断 + 局部异常筛选 → 异常单独深入 → 思路连贯 + 决策质量稳定。

**root_cause**:
人脑处理"同类批量"远比"单点逐个"高效（认知科学共识）。Phase A 单点逐个模式是把 Mark 当成"流水线工人"，新模式是把 Mark 当成"质量检验员"——让 Mark 的判断价值集中在"识别异常"，而不是"重复确认无问题"。

**cross_layer_links**:
#14d 三阶段时序协议（批量审核也是三阶段：呈现/筛选/讨论）；#14c 自我迭代（批量发现的偏差触发 D 类规则升级）；偏差库新增 Claude 偏差 6（单点逐个模式）

---

## §3 跨层联动清单（13 项，与 v1.0 一致）

1. principle_025 行业 OS 类比陷阱 ↔ strategic_framework_010 运营合伙人定位（双向验证）
2. principle_026 信息差还原陷阱 ↔ decision_framework_007 真实 6 信息差（修正与扩展）
3. principle_016 事实三件→五件升级 触发 agent_config_003 协作协议 + agent_config_005 主动追问的同步升级
4. agent_config_014（自我迭代+依赖分析）触发 agent_config_002/003/004/006/008/009/010/011 D 类全部 review
5. agent_config_015（三阶段协议）触发 mechanism_playbook_022 (DKP) / principle_001 (三类人) / principle_022 (Agent 边界) D 类协作 review
6. agent_config_016（批量审核）触发偏差库新增 Claude 偏差 6
7. agent_config_012（偏差库）新增 Claude 偏差 5（批次模式跳过 4 字段）+ 6（单点逐个模式）
8. strategic_framework_013 基础设施三层 ↔ business_playbook_016 渠道毛利结构（独立核算）
9. decision_framework_007 真实 6 信息差 D 反转 触发新 C 类 Playbook 候选"保司产品差异化共创"（下月新增）
10. decision_framework_001 季度评估（修订自年度）触发 strategic_framework_011 L1 战略路径 review
11. strategic_framework_005 副机战略框架 PROMOTE 与 mechanism_playbook_019 副机建设机制 REVISE 状态不一致（允许的）
12. business_playbook_018 业务线产品适配 REJECT_MERGE → 下月 PGU 体系 Playbook 新增
13. strategic_framework_004 4 业务线 DELAY 触发 strategic_framework_009b（实为 audit 提的跨业务线协同边界）的 review

---

## §4 战略级修订（4 项）

1. **事实三件 → 事实五件升级**（principle_016 + agent_config_003）
2. **真实信息差 3 个 → 6 个**（decision_framework_007 重大修订，分 3 类，含 D 反转 + F 新增）
3. **战略评估周期**：年度 → 季度（decision_framework_001 修订自原"每年 Q4"）
4. **偏差库新增 Claude 偏差 5/6**（agent_config_012 — 批次模式跳过 4 字段 / 单点逐个模式）

---

## §5 v2 修复说明（给 agent）

### 修复目标
- v1.0 audit 73 个 PROMOTE 仅含简述 → agent 处理后 BRIEF 模式（causal_logic / root_cause = null）
- v2 audit 含 103 个 PROMOTE 完整 4 字段 → agent 升级 73 个 BRIEF 到 FULL

### Agent 动作
1. 读取 v2 audit 文件
2. 对 87 个 PROMOTE entries（已是 v1.0）：
   - 检查 mark_input_mode 字段
   - 如果 mark_input_mode == 'brief' → 升级到 'full'
   - 用 v2 audit 中的 causal_logic / root_cause / cross_layer_links 填充
   - changelog 追加："v1.0 4 字段升级 (2026-04-29 v2 修复)"
3. 不动 14 个已是 FULL 的 entries
4. 不动 4 个 CREATE entries
5. 不动 4 DELAY / 1 REVISE / 1 REJECT_MERGE
6. 输出处理日志到 `governance/monthly_aggregations/2026-04/v2_repair_log.json`

### 验收标准
- 91 个 v1.0 entries 全部 mark_input_mode='full'
- 全部含 4 字段完整内容（无 null）
- changelog 反映 v2 修复
- 5 段格式报告

---

**v2 audit 文件 End**
