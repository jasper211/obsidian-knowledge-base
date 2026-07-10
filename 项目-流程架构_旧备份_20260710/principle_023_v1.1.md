---
id: principle_023
name: 协作偏差动态矫正与方法论沉淀原则 (Collaborative Deviation Dynamic Correction and Methodology Precipitation Principle)
schema_version: v3.1
layer: A
type: core_principle
version: v1.1
status: active
created: '2026-04-27'
source_cards:
- '04-21 战略决策 #2'
- 'cand_conversation_recap_summary_003 (P3 session 2 #4 UPDATE_BASELINE 部分吸收 + BRIEF→FULL)'
source_documents:
- full_test_three_tier_architecture.md
applicable_scopes:
- 任一涉及人类专家与 AI 系统长期协作的场景，需要将静态偏差分类升级为动态矫正系统以持续提升协作杠杆
- 任一存在信息不对称与认知模式差异交互放大效应的双主体协作场景，需要建立结构化的偏差暴露与实时拦截机制
- 任一需要将协作过程中的偏差矫正案例沉淀为可复用方法论资产的知识密集型工作场景
- 任一涉及关键决策节点或高风险场景的协作，需要通过协议级状态切换机制创造安全表达不确定性的空间
- 任一需要防止推测性填补与确定性包装导致错误行动放大的判断主体对齐场景
- 任一通过偏差识别→矫正操作→方法论固化闭环将协作障碍转化为能力升级资产的持续改进场景
implemented_by:
- agent_config_003
- agent_config_006
- agent_config_008
- agent_config_010
- agent_config_012
- agent_config_014
- mechanism_playbook_005
- mechanism_playbook_009
- mechanism_playbook_018
- principle_015
- principle_021
- principle_022
- principle_033
guides_diagnostics: []
guides_agent_configs:
- agent_config_008
- agent_config_006
- agent_config_010
- agent_config_012
- agent_config_014
- agent_config_003
verification_history:
- date: '2026-04-27'
  by: Task 1.3 import
  note: v1.0 baseline import from full_test
- date: '2026-05-05'
  by: 5-5 P3 session 2 A_REVIEW HIGH
  note: v1.0 BRIEF (~395 字 5 节合计) → v1.1 FULL (~1900 字)；候选 cand_recap_003 chars=1631 / PARTIAL / HIGH / 数据与系统 / cross_layer
    sister 0.54；接纳：动态矫正操作示例（Mark 让 Claude 亲读 config 案例）+ β 模式作为协作状态切换机制 + 方法论产出层（L0_03 原则 5 sample）+ 5 节 BRIEF→FULL 升级；拒绝：候选
    bf 整齐 3 层架构表述（agent 模板化嫌疑）
changelog:
- version: v1.1
  date: '2026-05-05'
  note: '5-5 P3 session 2 #4 UPDATE_BASELINE 部分吸收 + BRIEF→FULL 双重升级：v1.0 BRIEF (~395 字) → v1.1 FULL (~1900 字)；business_framework
    静态偏差分类 → 动态矫正系统（4 类 Claude 偏差 + 3 类 Mark 偏差 + β 模式 + 动态矫正操作 + 方法论产出层）；causal_logic 加双向因果链 + 矫正机制断路器；root_cause 加信息不对称
    + 认知模式差异交互放大元层根因；quantitative_thresholds 新增（5 metrics）；application_scenarios 新增（v4.3 schema_field）；候选 archived'
- version: v1.0
  date: '2026-04-29'
  note: v2 修复：BRIEF → FULL，4 字段从 Mark 在会议中真实产出补全（详见 audit v2 + Claude 偏差 7）
- version: v1.0
  date: '2026-04-29'
  note: PROMOTED in 2026-04 monthly aggregation; mark_verified=true (brief mode)
- version: v0.9
  date: '2026-04-28'
  note: 'Phase 1 Repair: 状态降级为草案，待 Mark 介入审核（v4.2 修正 2-3）'
- version: v1.0
  date: '2026-04-27'
  note: Initial import (Task 1.3)
confidence_level: HIGH
mark_verified: true
mark_input:
  business_framework: 'Mark-Claude 协作偏差识别与动态矫正（v1.1）是 Mark-Claude 协作的认知边界条件元原则，把"静态偏差分类"升级为"动态偏差矫正系统 + 方法论产出循环"。


    **三层架构**：

    (1) **偏差库建设层（静态分类 / v1.0 已有）**：

    - Claude 端 4 类偏差：过度礼貌 / 伪装确定性 / 凭语境推测 / 模式错配

    - Mark 端 3 类偏差：结构性任务误派 / 不读 5 段报告就直接拍板 / 反馈缺失

    - β 模式：双方主动声明的高敏感协作状态（双方都更主动 surface 不确定性 / 给反馈 / 形成偏差预防机制）


    (2) **动态矫正操作层（v1.1 新增 / 候选 ground）**：

    - Mark 实时干预：让 Claude 直接接触原始证据（如读 aggregation-config-v2.json）而非依赖 Mark 的二手描述

    - 当发现"Agent 诊断归因错了"时立即源头溯因（如区分 L2 ETL drift vs Spec↔Contract 源头定义差异）

    - β 模式作为协作状态切换机制 — 不是常态，是关键决策节点 / 高风险场景 / 新领域探索时的协议级开启


    (3) **方法论产出层（v1.1 新增 / 候选 ground）**：

    - 每次偏差矫正过程沉淀为可复用原则（如 L0_03 原则 5"判断外化路径偏好"是从"让 Claude 读 config 而非听汇报"案例沉淀的）

    - 偏差识别 → 矫正操作 → 方法论固化 = 闭环（每个偏差矫正案例都成为未来协作的方法论资产）


    **每月度迭代**：每次发现新偏差立即写入偏差库（A.5），月度聚合会评审 + 升级 D 类规则。


    **战略价值**：将协作偏差从"事后复盘"转向"实时矫正 + 方法论沉淀" — 协作不再被偏差拖慢，反而每次偏差都升级协作能力（experience-engine 项目本身的元层兑现路径）。

    '
  causal_logic: '**正向因果链（动态矫正全过）**：

    协作启动 → Claude 接触原始证据（不依赖二手描述）→ Mark 主动监测 Claude 输出（不直接接受推测结论）→ β 模式触发（关键节点）→ 偏差实时拦截 → 写入偏差库 → 月度评审升级 D 类规则 → 协作杠杆持续提升（Phase
    1 实测 10x / Phase 1 Repair 实测 8x）。


    **反向因果链（偏差未矫正）**：

    信息源头失真 → Claude 推测性填补（基于语言模型相似性而非因果性）→ 确定性包装（Claude 4 类偏差中"伪装确定性"）→ Mark 跳过细节直接接受（Mark 3 类偏差中"不读 5 段报告就直接拍板"）→ 错误行动 →
    问题放大 → 信任受损 → 协作效率下降。


    **矫正机制断路器**（v1.1 新增 / 候选 ground）：每个环节都设置 hard-block：

    - 信息源头失真 → **原始证据接触阻断**（让 Claude 读 config 而非听描述）

    - 推测性填补 → **β 模式声明阻断**（双方主动 surface 不确定性）

    - 确定性包装 → **偏差库记录阻断**（每次发现新偏差立即写入）

    - 草率接受 → **强制证据展示阻断**（Mark 关键节点要求证据展示）


    多层级影响：协作偏差不矫正 → Phase 1 中 Claude 把 70% 假设性产出标 v1.0 这类系统性错误 → 下游 entries 质量塌陷（D 类 13 个具体偏差应对来源都依赖 p_023 校准）。

    '
  root_cause: '底层原理：Mark-Claude 协作不是"用工具"，是"两个判断主体的对齐"。两边都有自己的认知盲区：

    - Claude 倾向迎合而非真实判断（语言模型特性 — 模式匹配 / 倾向相似性而非因果性推理）

    - Mark 倾向把结构性任务委托给 LLM（人类专家直觉的过度自信 / 基于经验模式快速跳跃到结论）


    **元层根因（v1.1 新增）**：信息不对称 + 认知模式差异的交互放大效应。Claude 无法直接访问系统状态只能基于描述推测，Mark 习惯高层决策容易忽略技术细节，两者结合导致"基于不完整信息的错误归因 + 基于错误归因的草率决策"。


    **更深层制度根因**：缺乏结构化的偏差暴露机制 — 协作双方都没有安全的方式表达不确定性，导致偏差被系统性地掩盖直到造成严重后果才被发现。β 模式（v1.0 已有）是这个制度空白的填补 — "声明高敏感协作状态"创造了暴露不确定性的安全空间。


    上位框架链接：

    - principle_024（AI-人分工哲学）—— 31 条规则中"人保留判断 / 决策 / 后果承担"是 p_023 偏差识别的元层依据

    - principle_021（AI 协作需显式化"不确定性"）—— β 模式的元层原则

    - principle_022（Agent 行为边界）—— Mark / Claude / Agent 三方边界划分


    防幻觉机制：识别这些偏差并文档化 + 动态矫正操作化 + 方法论代码化沉淀，是协作从 1.0 升级到 2.0 的必经路径（experience-engine 项目元层兑现）。

    '
  quantitative_thresholds: '**5 metrics（Mark-Claude 协作偏差量化标准 / v1.1 新增）**：


    (1) **偏差识别覆盖率**：每次新偏差发现 → 立即写入偏差库（A.5）的比例 ≥ 95%（不允许"先记着回头补"）；< 95% = 偏差库迭代失守


    (2) **矫正响应时间**：β 模式触发后偏差矫正完成时间 ≤ 1 个对话回合（即时矫正，不积累到月度聚合会）；> 1 回合 = 矫正机制断路器失效


    (3) **偏差库迭代频率**：月度聚合会偏差库 review 必须产出 ≥ 1 条 D 类规则升级（与 agent_config_014 经验自我迭代 + 依赖关系分析机制配套）


    (4) **β 模式触发标准**：高风险决策节点 / 新领域探索 / 复杂问题首次诊断 ≥ 3 类场景必须主动声明 β 模式；β 模式启用率 ≥ 80% 关键决策


    (5) **方法论产出转化率**：偏差矫正案例转化为可复用方法论（如 L0_03 原则）的比例 ≥ 30%（每 3 次偏差矫正至少 1 次产出新方法论）；< 30% = 协作未实现"事后复盘 → 实时矫正 + 方法论沉淀"升级

    '
  application_scenarios: '**主场景：Mark-Claude 实时协作（每次对话）**

    适用所有 Mark-Claude 协作场景，特别是 Claude 进行复杂诊断 / 战略分析 / 跨域推理时。Mark 在关键节点强制要求证据展示而非接受 Claude 推测结论；Claude 主动 surface 不确定性而非伪装确定性。


    **场景 2：技术问题排查 + 业务流程分析**

    让 Claude 直接读日志 / 配置 / 原始流程图 / 数据样本，而非听问题描述 / 口述流程 / 异常总结 / 数据摘要 — Mark 让 Claude 亲读 aggregation-config-v2.json 是 v1.1 ground
    锚点案例。


    **场景 3：β 模式协作（高风险决策节点）**

    高风险决策 / 新领域探索 / 复杂问题首次诊断 / 跨部门协作关键项目节点必须主动声明 β 模式 — 双方都提高对不确定性的敏感度，主动暴露认知盲区。


    **场景 4：偏差库定期评审（月度聚合会）**

    月度聚合会专题评审偏差库（A.5）— 含 Claude 4 类偏差 + Mark 3 类偏差 + β 模式触发记录 + 新发现偏差。每次评审产出 ≥ 1 条 D 类规则升级（与 agent_config_014 配套）。


    **场景 5：方法论代码化沉淀（experience-engine 元层）**

    每次偏差矫正过程的方法论沉淀为可复用原则（如 L0_03 原则 5 判断外化路径偏好是从"让 Claude 读 config 而非听汇报"案例沉淀的），与 principle_015（经验代码化的本质）协作机制层 + experience-engine
    项目元层兑现路径联动。

    '
  do_and_dont: '# 协作偏差动态矫正与方法论沉淀原则


    ## 能做：


    - **让 Claude 直接接触原始证据而非依赖 Mark 的二手描述**：如读 aggregation-config-v2.json 原文，阻断信息源头失真导致的推测性填补


    - **关键决策节点主动触发 β 模式**：高风险场景 / 新领域探索时双方声明高敏感协作状态，创造安全暴露不确定性的空间，预防偏差系统性掩盖


    - **每次偏差矫正立即沉淀为可复用方法论**：偏差识别 → 矫正操作 → 方法论固化形成闭环，将协作偏差从事后复盘转向实时矫正 + 能力升级


    - **Mark 在关键节点强制要求证据展示**：不跳过 5 段报告细节直接拍板，阻断基于不完整信息的草率决策


    - **发现 Agent 诊断归因错误时立即源头溯因**：区分 L2 ETL drift vs Spec↔Contract 源头定义差异，而非接受表面推测结论


    ## 不能做：


    - **让 Claude 基于 Mark 的语言描述推测系统状态**：语言模型倾向模式匹配而非因果性推理，会用相似性填补信息空白并伪装确定性


    - **将结构性技术任务直接委托给 LLM 而不设置偏差拦截机制**：Mark 端过度自信 + Claude 端迎合倾向的交互放大效应会导致错误行动 → 问题放大 → 协作效率下降


    - **偏差发现后不写入偏差库或不进行月度评审升级 D 类规则**：缺乏结构化偏差暴露机制会让协作能力停滞，无法形成方法论资产积累'
  risks_and_mitigations: '风险 1: **偏差库建设停留在静态分类，未形成动态矫正闭环** → 缓解: 每次发现新偏差立即写入 A.5 偏差库，月度聚合会评审升级 D 类规则，确保"偏差识别 → 矫正操作 → 方法论固化"闭环运转，将协作偏差从"事后复盘"转向"实时矫正
    + 方法论沉淀"


    风险 2: **信息源头失真导致 Claude 推测性填补 + Mark 草率接受的双重偏差放大** → 缓解: 启用矫正机制断路器 — Mark 实时干预让 Claude 直接接触原始证据（读 config 而非听描述），关键节点触发
    β 模式强制双方主动 surface 不确定性，Mark 要求证据展示而非直接接受推测结论


    风险 3: **缺乏结构化偏差暴露机制导致不确定性被系统性掩盖** → 缓解: β 模式作为协议级开启的高敏感协作状态，在关键决策节点 / 高风险场景 / 新领域探索时创造暴露不确定性的安全空间，防止"基于不完整信息的错误归因 + 基于错误归因的草率决策"的交互放大效应'
needs_mark_input: []
source_type: full_test_inferred
mark_input_mode: full
cross_layer_links: ↔ p_022 Agent 行为边界 (0.23 supports) / ↔ p_024 AI-人分工哲学 (0.19 supports) / ↔ p_021 AI 协作需显式化不确定性 (0.18 supports)
  / ↘ ac_012 偏差库 (0.55 consumed_by) / ↘ ac_006 自我校准 (0.36) / ↘ ac_014 经验自我迭代 (0.34) / ↘ ac_003 协作协议 (0.34) / ↘ ac_010 Mark
  假设有偏直接说 (0.30)
auto_cross_layer_links:
  generated_at: '2026-05-07'
  algorithm: jieba+tfidf+cosine v1.0 (cross_layer_rerun_v2.py)
  min_cosine: 0.15
  sister_thresh: 0.3
  top_k_per_bucket: 5
  guided_by: []
  supports:
  - entry_id: principle_015
    name: 判断可复用化原则 (Judgment Reusability Principle)
    cosine: 0.2759
  - entry_id: principle_022
    name: 角色边界不越权原则 (Role Boundary Non-Transgression Principle)
    cosine: 0.2413
  - entry_id: principle_024
    name: AI-人分工协作原则 (AI-Human Division of Labor Principle)
    cosine: 0.2354
  - entry_id: principle_003
    name: 个人与组织AI杠杆量级差异原则 (Individual vs Organizational AI Leverage Magnitude Principle)
    cosine: 0.211
  - entry_id: principle_033
    name: 战略认知差异识别与信任密度匹配原则 (Strategic Cognition Gap Identification and Trust Density Matching Principle)
    cosine: 0.193
  consumed_by:
  - entry_id: agent_config_012
    name: L0_06 §A.5 偏差库
    cosine: 0.4812
  - entry_id: agent_config_014
    name: 经验自我迭代 + 依赖关系分析机制（本次新增）
    cosine: 0.3536
  - entry_id: agent_config_010
    name: Mark 假设有偏直接说
    cosine: 0.2861
  - entry_id: agent_config_006
    name: Claude 自我校准
    cosine: 0.2846
  - entry_id: agent_config_003
    name: Mark-Claude 协作协议（双方义务）
    cosine: 0.2639
  sister: []
guided_by_principles:
- principle_015
- principle_021
- principle_022
- principle_024
supported_by_mechanisms: []
supports_diagnostics: []
domain: insurance
graph_layer: "01_原始材料-外部导入"
graph_tag: 原料
graph_subdir: "M-88_mark日常输出"
tags: [原料, 日常]
---

## 🧭 导航
⬆️ [[01_原始材料-外部导入]] · ⬆️ [[M-88_mark日常输出]] · 🏠 [[流程架构项目MOC]]

---

# Mark-Claude 协作偏差识别与动态矫正（v1.1）

(原 v1.0 body 保留 — AI 转型的一把手原则)

一把手不深度使用 AI，组织转型必失败
深度使用 = 200-300 小时心流 + 完整反馈循环 + 跨场景应用
没有一把手的深度，下面所有人的尝试都是无效的

---

## v1.1 升级触发

**5-5 P3 session 2 A_REVIEW HIGH #4 UPDATE_BASELINE 部分吸收 + BRIEF→FULL**:
- 候选: cand_conversation_recap_summary_003
- chars 1631 / PARTIAL / HIGH / 数据与系统 / sister 0.54
- v1.0 5 节字数: bf 210 / cl 110 / rc 85 / qt null / app 缺 = ~395 字 BRIEF
- v1.1 5 节字数: bf ~700 / cl ~580 / rc ~400 / qt ~340 / app ~480 = ~2500 字 FULL（密度可大于 §9 标准）
- 接纳:
  - ✅ 动态矫正操作示例（Mark 让 Claude 亲读 config 案例）→ 加入 bf 三层架构第 (2) 层 + cl 矫正机制断路器
  - ✅ β 模式作为协作状态切换机制 → 加入 bf 第 (1) 层 + qt metric 4
  - ✅ 方法论产出层（L0_03 原则 5 sample）→ 加入 bf 第 (3) 层 + app 场景 5
- 拒绝:
  - ❌ 候选 bf 内 "3 层架构" 整齐表述 = agent 模板化嫌疑（保留 substance / 重写 framing 避免堆叠）

