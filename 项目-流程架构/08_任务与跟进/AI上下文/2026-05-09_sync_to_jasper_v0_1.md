---
type: 项目笔记
source: 08_任务与跟进/AI上下文
synced: 2026-06-15
tags: [项目]
---

# experience-engine 最小同步包（致 Jasper · 用于替换 v0.1 旧版认知）

> 来源：Mark · experience-engine 项目当前状态（5-9 实测）
> 用途：替换 Jasper《信号架构设计_经验引擎_v0.1》第 1.1/1.2 节 + 补充阶段2 接入前置
> 范围：仅给到 Jasper 阶段0 → 阶段2 接入所需的最小信息，不是 experience-engine 全貌

---

## 0 · TL;DR

你 v0.1 第 1.1/1.2 节描述的 experience-engine 状态（117 entries / 4 字段：business_framework / causal_logic / root_cause / cross_layer_links）是 **v1.0.0 旧版快照**。5-8 系统性 prompt audit 之后已升到 v2.1，结构、规模、规则都变了。本同步包给你 5 件事：

1. **新数据结构**：7 段（a-g）+ 11 元数据（替换你的 4 字段表）
2. **新基线规模**：332 entries / A 103 + B 81 + C 127 + D 21（不是 117）
3. **双轨架构**：V3 / V3.1 并存，接入时必须区分
4. **§28 业务实战主导锁定**：你的"节点6 行动生成"程序需要据此调整
5. **阶段2 接入前置**：除你自己列的"L3↔entry_id 对照表"外，还有三项

---

## 1 · entry 数据结构（替换你 v0.1 第 1.2 节"四字段结构"表）

### 1.1 7 段结构（a-g）

| 段 | 段头 | 字数 | 子段格式 |
|---|---|---|---|
| a | business_framework | 100-200 字 | 业务场景 / 核心命题 / 适用条件 |
| b | causal_logic | 100-200 字 | 显性因果链 A→B→C→结果 |
| c | root_cause | 100-200 字 | 底层原理 / 元层判断 |
| d | quantitative_thresholds | 50-100 字 | 数字阈值 |
| e | application_scenarios | 100-200 字 | `- B2B:` / `- B2A:` list 子段 |
| f | **do_and_dont** | 100-200 字 | `- 能做:` / `- 不能做:` list 子段 |
| g | **risks_and_mitigations** | 100-200 字 | `- 风险:` / `- 缓释:` list 子段 |

**与你 v0.1 4 字段的对应**：
- 你的 business_framework / causal_logic / root_cause = a/b/c（保留）
- 你的 cross_layer_links → 已**降级为元数据**（不再是独立段，详见 1.2）
- **新增 d/e/f/g 4 段** = quantitative_thresholds + application_scenarios + do_and_dont + risks_and_mitigations
- f/g 是 5-9 Mark 业务实战版段头（不是理论版的 inversion_or_boundary / decision_support）

### 1.2 11 元数据（5-9 锁定）

| 元数据 | 取值 | 5-9 新增？ |
|---|---|---|
| 类型 | principle / business_playbook / mechanism_playbook / decision_framework / strategic_framework / agent_config | 否 |
| 业务领域 | NGP / BIB / 永明 / ... | 否 |
| 关键词 | list[str] | 否 |
| 判断主体 | Mark / 团队 / ... | 否 |
| 数字事实 | list[str] | 否 |
| 原话引用 | str | 否 |
| **confidence_level** | HIGH / MEDIUM / LOW | ✅ 5-9 新增 |
| **urgency** | P0 / P1 / P2 | ✅ 5-9 新增 |
| **scope** | single_carrier / multi_carrier / cross_business / enterprise_wide | ✅ 5-9 新增 |
| **business_line** | NGP / BIB / 永明 / 天领 / 跨线 / ... | ✅ 5-9 新增 |
| **target_audience** | B2B / B2A / B2B+B2A | ✅ 5-9 新增 |

### 1.3 你 v0.1 阶段2 设计的影响

- 你的洞察"模块3 经验参照"原设计是 `[entry_id 原则名称]` 一行简略 → 这样会丢 90% 经验密度
- 推荐改为引用 a/c/f 三段（business_framework + root_cause + do_and_dont），约 300-500 字
- target_audience 元数据可以直接用来过滤"给 B2B 还是 B2A"

---

## 2 · A/B/C/D 4 类基线（替换你 v0.1 第 1.1 节统计）

### 2.1 5-9 实测数量（不是 117）

| 类 | 路径 | 数量 | 性质 |
|---|---|---|---|
| A · 原理库 | `core/A_principle_library/` | **103** | Mark 底层判断原则 |
| B · 机制 playbook | `core/B_mechanism_playbooks/` | **81** | 组织/运营机制设计 |
| C · 业务流程 | `domains/{insurance, _shared, 新动力}/` | **127** | 具体业务场景操作逻辑 |
| D · agent 运行时 | `core/D_agent_runtime_config/` | **21** | AI 协作行为规范与协议 |
| **总计** | — | **332** | mark_verified=true |

注意：C 类在 `domains/` 下不在 `core/`，按业务线分子目录（insurance / 新动力 / _shared 跨线）。

### 2.2 §29 关键认知（5-9 锁定）

A/B/C/D **4 套 Playbook 都用同一套 7 段 v2.0 标准**（不是只有个人 entry 用 7 段）。
B 和 C 已经从旧 schema 升到 7 段，layer_hint 半自动分流决定一条 entry 入 A/B/C/D 哪一类。

→ 你阶段2 建对照表时，映射粒度应该是 **L3 编码 ↔ A/B/C/D 中具体某条 entry**，而不是"L3 ↔ 任意 entry_id"。映射时 layer_hint 元数据是关键过滤字段。

---

## 3 · 双轨架构 V3 / V3.1（你 v0.1 完全没提）

### 3.1 两条轨道

| 轨道 | raw 来源 | 处理器 | 4-28 保险市场实测 | 可信度 |
|---|---|---|---|---|
| V3 | v1 raw 关键词识别 | 旧 signal_converter | 47 candidates | **root_cause 89.2% fallback 模板**（不可信） |
| V3.1 | v2/v2.1 raw 段落 split | `_candidate_v3_1_paragraph_splitter.py` | 27 candidates | 0 fallback / 100% citations / 100% paragraph_split / 100% substance |

V3 现存数据**不能直接拿来当 experience-engine 内容**，72/74 条已被 fallback marker 标记。

### 3.2 §30 关键认知（5-9 锁定）

**v2.1 raw → entry 必经聚合阶段**（不是 1:1 直扩）。raw 段落数 ≠ 最终 entry 数。如果你阶段2 接入想消费 candidates，要消费 V3.1 的**已聚合后的 entry**，不要消费 raw split 出来的 candidates。

### 3.3 对你阶段2 接入的硬要求

- 接入入口必须明确轨道：`source: V3 (含 fallback)` 或 `source: V3.1 (clean)`
- V3 数据要先看 `fallback_marker` 字段，标记为 fallback_template 的 root_cause 不能用
- 不能消费 raw candidates，只消费已聚合 entry

---

## 4 · §28 业务实战主导锁定（影响你节点6 行动生成程序）

### 4.1 §28 五条规则（5-9 永久锁定）

1. prompt 段头由 Mark 业务实战主导，agent 不主动推断扩展
2. 实战版段头优先于理论完美段头（do_and_dont 优于 inversion_or_boundary）
3. V3.1 转换器升级必须按 Mark 实测产出格式
4. prompt 升级后第一次实测必须 5 类型抽样验证
5. 录音工具 LLM 上游污染过滤逻辑保留作兜底

### 4.2 对你 v0.1 节点6 "Step C 行动生成" 的张力

你设计：节点6 由 Claude 自动生成"建议行动选项 A/B/C"输出给 Mark 决策。
§28 精神：经验类内容的段头 / 框架 / 行动选项语言由 Mark 业务实战主导，不接受 agent 推断扩展。

**调和方案（推荐）**：
- 节点6 Step C 不输出 A/B/C 选项，改为输出 **audit 锚点**（"这条信号涉及 9 问题中的 Q3/Q5/Q7" + 引用 experience-engine 中相关 do_and_dont/risks_and_mitigations 段原文）
- 让 Mark 看 audit 锚点 + 经验原文后自己拍 A/B/C
- 这同时减轻你 v0.1 第七章问题3"洞察消费者颗粒度"的压力——Mark 战略级用 audit 锚点，岗位负责人用经验原文 + L4 标准

---

## 5 · 阶段2 接入前置清单（扩展你 v0.1 第七章问题1）

你 v0.1 提到要建"L3 编码 ↔ entry_id 对照表"。实际接入还需要三项：

| 前置 | 内容 | Owner |
|---|---|---|
| 1 你已列 | L3 编码 ↔ entry_id 对照表（含 layer_hint 过滤） | Jasper 主导 / Mark agent 辅助 |
| 2 新增 | 接入接口区分 V3 / V3.1 轨道（source + fallback_marker 字段） | Mark agent |
| 3 新增 | 经验引用粒度从"一行 entry_id"升到"a+c+f 三段" | Jasper（节点6 模板调整） |
| 4 新增 | 节点6 Step C 改为输出 audit 锚点 + 经验原文（§28 调和） | Jasper（推理程序调整） |

---

## 6 · 不在本同步包内的（边界声明）

以下你阶段0 / 阶段2 接入**不需要**，等阶段2 真接入前再深 sync：

- governance/phase3/ 详细产出（5-8 audit 报告 / 5-9 v2.1 实测 raw / cross_layer map）
- §21-§27 工程纪律（议题成熟度 / prompt audit / V3.1 转换器标准 / fallback 透明化 / agent 启动预检 / 一次性修订）
- patch_log §1-§30 完整版
- 5-15 Session 2 入库 24 entries / 5-19 Session 3 决策节奏

---

## 7 · 一句话边界

**experience-engine 是"会议→经验"的生产引擎；你的"信号架构设计 v0.1"是把 experience-engine 当下游燃料的"信号→洞察"消费引擎。本同步包给你的是燃料的真实规格（容量、油号、双轨），不是发动机原理。**

---

*版本：v1.0 / 2026-05-09 / Mark 起草*
*来源依据：experience-engine repo 5-9 实测 + governance/framework_patch_log/2026-05.md §28-§30*
