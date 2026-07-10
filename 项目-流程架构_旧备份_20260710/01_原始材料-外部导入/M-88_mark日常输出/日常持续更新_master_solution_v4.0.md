---
type: 项目笔记
source: 01_原始材料-外部导入/M-88_mark日常输出
synced: 2026-06-15
tags: [项目]
---

# Mark 经验机构化系统｜独立项目方案 v4.0

**版本**：v4.0（独立项目级架构 - 2026-04-26 定稿）
**关键升级**：从 insurance-analytics-v2 子模块 → **独立基础设施级项目**

---

# 1. 重大架构判断（你的判断 = 完全正确）

## 1.1 之前的错误定位

```
v3.0 方案（错误）：
  experience_library/ 作为 insurance-analytics-v2 项目的子目录
  
问题：
  ✗ Playbook 被锁死在保险业务的上下文里
  ✗ 跨项目复用需要 fork 整个保险项目
  ✗ 经验库的版本与保险业务版本耦合
  ✗ 估值逻辑（基础设施 8-15x）无法物理隔离
```

## 1.2 v4.0 的正确定位

```
v4.0 方案（正确）：
  经验机构化系统 = 独立的基础设施级项目
  与 insurance-analytics-v2 平级
  作为"行业 OS"的核心引擎
  其他业务项目（保险/新动力/未来扩展）都来集成它
```

## 1.3 这个判断的战略意义

```
战略层面：
  ✓ 与 L1_02 "AI 数据组织认知升级"完全对齐
  ✓ 与 L0_02 "运营合伙人定位"的"行业基础设施"叙事完全对齐
  ✓ 估值倍数 8-15x 找到了物理证据（独立资产）
  ✓ Phase 4 跨保司迁移的基础设施已就位（不是未来才建）

工程层面：
  ✓ 三层产出物（A/B/C）作为独立资产管理
  ✓ 版本独立于业务项目
  ✓ API 化暴露给所有项目消费
  ✓ 本身可作为产品对外销售（SaaS 化前提）

组织层面：
  ✓ 显式表达"我们是基础设施公司"
  ✓ 团队心智从"做保险的"升级为"做行业 OS 的"
  ✓ 经验库本身就是公司核心资产
```

---

# 2. 新的项目架构

## 2.1 整体架构

```
~/projects/
├── experience-engine/                  ← 🆕 新建独立项目
│   ├── 这就是经验机构化系统的家
│   └── 是其他项目的"上游基础设施"
│
├── insurance-analytics-v2/             ← 现有项目
│   ├── 保险业务的 generate_insights.py
│   └── 集成 experience-engine（消费方）
│
├── 新动力 (未来项目)                    ← 未来项目
│   └── 集成 experience-engine（消费方）
│
└── 跨保司迁移 (未来项目)                ← Phase 4 的项目
    └── 集成 experience-engine（消费方）
```

## 2.2 experience-engine 项目的内部结构

```
experience-engine/                       ← 项目根
├── README.md                           ← 项目说明
├── CHANGELOG.md                        ← 版本历史
├── ARCHITECTURE.md                     ← 架构设计文档
│
├── core/                               ← 核心引擎（与业务无关）
│   ├── A_principle_library/            ← A 思维体系库
│   │   ├── 00_index.md
│   │   ├── core_principles/            ← 23 条核心原则
│   │   ├── strategic_frameworks/       ← 8 个战略框架
│   │   └── decision_frameworks/        ← 5 个决策框架
│   │
│   ├── B_mechanism_playbooks/          ← B 机制设计 Playbook
│   │   ├── 00_index.md
│   │   ├── organizational/             ← 6 个组织机制
│   │   ├── ai_collaboration/           ← 5 个 AI 协作机制
│   │   ├── data_infrastructure/        ← 4 个数据机制
│   │   └── talent_learning/            ← 5 个人才/学习机制
│   │
│   └── _meta/
│       ├── cross_layer_dependencies.yaml
│       ├── version_log.md
│       └── schemas/                    ← Schema 定义
│           ├── principle_schema.yaml
│           ├── mechanism_schema.yaml
│           └── playbook_schema.yaml
│
├── domains/                            ← 领域特定的 C 类（业务诊断）
│   ├── insurance/                      ← 保险领域
│   │   ├── 00_index.md
│   │   ├── v1.0_legacy/                ← 原 50 条快照
│   │   ├── v1.1_current/               ← 当前版本（含本次新增 10 + 修订 24）
│   │   └── changelog.md
│   │
│   ├── 新动力/                          ← 未来领域（培训/内容）
│   │   └── （等待新动力项目启动时建立）
│   │
│   └── _shared/                        ← 跨领域共享的 C 类
│       └── （Phase 3 后才会有内容）
│
├── extractors/                         ← 经验卡识别系统
│   ├── extractor.py                    ← 主识别脚本
│   ├── classification_rules.yaml       ← 5 类识别器规则（v2.0 标准）
│   ├── classifier.py                   ← 三层分类器
│   ├── test_cases/                     ← 测试用例（20+ 标注片段）
│   └── README.md
│
├── pipelines/                          ← 数据流水线
│   ├── ingest_meeting_transcript.py    ← 会议逐字稿入口
│   ├── ingest_feedback_log.py          ← 反馈日志入口
│   ├── prepare_aggregation.py          ← 月度聚合会准备
│   └── sync_to_consumers.py            ← 通知消费方更新
│
├── api/                                ← 对外 API（其他项目集成用）
│   ├── server.py                       ← API 服务器
│   ├── client_examples/                ← 客户端集成示例
│   │   ├── python_client.py
│   │   ├── insurance_integration.py    ← insurance-analytics-v2 怎么用
│   │   └── README.md
│   └── openapi.yaml                    ← OpenAPI 规范
│
├── agents/                             ← Agent 标准加载逻辑
│   ├── load_principles.py
│   ├── load_mechanisms.py
│   ├── load_playbooks.py
│   ├── agent_initialization.py         ← Agent 启动时调用
│   └── README.md
│
├── governance/                         ← 治理与监督
│   ├── consistency_checker.py          ← 跨层依赖检查
│   ├── version_manager.py              ← 版本管理工具
│   ├── monthly_aggregation_sop.md      ← 月度聚合会 SOP
│   └── change_review_process.md        ← 变更评审流程
│
├── data/                               ← 输入输出数据
│   ├── input/
│   │   ├── transcripts/                ← 会议逐字稿（来自外部）
│   │   ├── feedback_logs/              ← 执行反馈日志
│   │   └── manual_cards/               ← 手工录入的经验卡
│   │
│   ├── candidates/                     ← 候选池（待审核）
│   │   ├── A_principle_drafts/         ← A 库草案（v0.x）
│   │   ├── B_mechanism_drafts/         ← B 库草案
│   │   └── C_playbook_drafts/          ← C 库草案
│   │
│   └── archive/                        ← 历史归档
│       └── monthly_aggregations/       ← 历次聚合会记录
│
├── tests/                              ← 测试
│   ├── test_extractor.py
│   ├── test_classifier.py
│   ├── test_consistency.py
│   └── test_api.py
│
└── docs/                               ← 文档
    ├── getting_started.md              ← 快速上手
    ├── for_consumers.md                ← 消费方集成指南
    ├── for_contributors.md             ← 贡献者指南（如何新增产出物）
    └── architecture/                   ← 架构设计文档
```

## 2.3 核心设计原则

### 原则 1：业务中立的核心 + 领域特定的扩展

```
core/ 目录（业务中立）：
  - A 思维体系库：跨业务通用
  - B 机制设计：80% 跨业务通用
  → 这是估值 8-15x 的核心资产

domains/ 目录（业务特定）：
  - C 业务诊断：每个业务领域一份
  - 保险、新动力、未来扩展各占一个子目录
  → 这是业务执行的工具
```

### 原则 2：API 优先（API-First）

```
不是文件复制，而是 API 调用：

insurance-analytics-v2/generate_insights.py
  ↓ HTTP/gRPC 调用
experience-engine/api/server.py
  ↓ 加载相关产出物
返回结构化数据

好处：
  ✓ 经验库版本升级不需要重启业务项目
  ✓ 多个项目共享同一份经验库
  ✓ 跨保司迁移时，新项目直接调用 API
```

### 原则 3：版本独立

```
experience-engine 自己的版本号：
  v1.0.0 - 初版（含 90 个产出物）
  v1.1.0 - 第一次月度升级
  v2.0.0 - 重大架构调整

业务项目集成时声明依赖版本：
  insurance-analytics-v2 依赖 experience-engine ^1.0.0
  新动力项目 依赖 experience-engine ^1.5.0
```

### 原则 4：贡献者机制

```
任何业务项目都可以贡献回核心：
  - 在保险领域发现的"通用机制" → 升级到 core/B_mechanism_playbooks/
  - 在新动力发现的"原则" → 升级到 core/A_principle_library/
  
贡献流程：
  1. 业务项目发现新经验
  2. 提交到 core/data/candidates/
  3. 月度聚合会评审
  4. Mark 拍板是否合并到 core/
```

---

# 3. 与现有项目的关系

## 3.1 与 insurance-analytics-v2 的关系

### 现状

```
insurance-analytics-v2 现在的样子：
  - generate_insights.py 自己包含逻辑
  - playbook 散落在项目内部
  - 与 Mark 的经验深度耦合
```

### 改造后

```
insurance-analytics-v2 改造后：
  - generate_insights.py 调用 experience-engine API
  - 加载相关 A 库原则 + B 库机制 + 保险领域的 C 库
  - 业务逻辑保持不变，只是经验来源外部化

具体变化：
  原代码：
    principles = hardcoded_principles
    playbooks = local_yaml_files
    
  新代码：
    from experience_engine_client import ExperienceEngine
    engine = ExperienceEngine(version="^1.0.0")
    principles = engine.load_principles()
    playbooks = engine.load_playbooks(domain="insurance")
```

### 迁移路径

```
Phase 0（当前）: insurance-analytics-v2 完全独立
  ↓
Phase 1（4 周）: experience-engine 项目建立
  experience-engine 已有完整内容（90 个产出物）
  insurance-analytics-v2 暂未集成
  ↓
Phase 2（6 周）: 双轨运行
  insurance-analytics-v2 仍用本地 playbook（保底）
  同时引入 experience-engine API（试运行）
  对比两者输出
  ↓
Phase 3（8 周）: 切换主干
  insurance-analytics-v2 切换到 experience-engine 为主
  本地 playbook 作为 fallback
  ↓
Phase 4（12 周）: 完全集成
  insurance-analytics-v2 删除本地 playbook
  完全依赖 experience-engine
```

## 3.2 与 L0/L1/L2 文档生态的关系

```
现有文档生态（在 /mnt/project/）：

L0 经营哲学层（Mark 的核心信仰）
  - L0_01 五阶段路径观
  - L0_02 运营合伙人定位
  - L0_03 AI-人分工哲学 v3.1
  - L0_05 架构保险丝 SOP
  - L0_06 Mark-Claude 协作手册

L1 战略架构层
  - L1_01 五阶段战略路径
  - L1_02 AI 数据组织认知升级

L2 机制设计层
  - L2_01 真实 5 个信息差
  - L2_02 基础设施三层架构

experience-engine 的关系：
  
  L0/L1/L2 文档 = 这些产出物的"种子"
                 = 历史已沉淀的经验
                 ↓ 导入
  experience-engine/core/ = 这些产出物的"工业化版本"
                           = 可被 Agent 加载的形式
                           = 可被新项目复用的形式

具体映射：
  L0_01 五阶段路径观 → core/A_principle_library/strategic_frameworks/
  L0_02 运营合伙人定位 → core/A_principle_library/strategic_frameworks/
  L0_03 AI-人分工哲学 → core/A_principle_library/core_principles/
  L0_05 架构保险丝 → core/B_mechanism_playbooks/organizational/
  L0_06 Mark-Claude 协作 → core/B_mechanism_playbooks/ai_collaboration/
  L1_02 AI 数据组织 → core/A_principle_library/strategic_frameworks/
  L2_01 信息差 → core/A_principle_library/decision_frameworks/
  L2_02 基础设施三层 → core/A_principle_library/strategic_frameworks/
```

**关键认识**：experience-engine 不是替代这些 L0/L1/L2 文档，而是**让它们工业化、可执行、可复用**。

## 3.3 与 Project Knowledge 的关系

```
Project Knowledge（Mark 的 Claude Project 中）：
  - 用途：与 Claude 对话时的上下文
  - 形式：散落的文档
  - 维护：手工

experience-engine：
  - 用途：经验的工业化、API 化、可执行化
  - 形式：结构化的产出物 + API
  - 维护：自动化（识别器+月度聚合会）

关系：
  Project Knowledge = "Mark 的私人书房"
  experience-engine = "公司的中央图书馆 + 知识引擎"
  
  两者并存：
    - Mark 个人对话仍用 Project Knowledge
    - 业务项目集成 experience-engine
```

---

# 4. 项目分阶段建设方案

## 4.1 总体规划

```
启动到成熟，4 个阶段，12 周完成：

Phase 1: 项目骨架（Week 1-2）
  目标：项目结构 + 90 个产出物入库 + 基础脚本
  
Phase 2: 自动化能力（Week 3-4）
  目标：识别器代码化 + 月度聚合 SOP + 一致性检查
  
Phase 3: API 化（Week 5-8）
  目标：API 服务器 + insurance-analytics-v2 集成
  
Phase 4: 跨项目集成（Week 9-12）
  目标：双轨运行 → 切换主干 → 完全集成
```

## 4.2 Phase 1: 项目骨架（Week 1-2）

### Week 1：项目建立

#### Task 1.1：创建独立项目
**Owner**: Agent
**时间盒**: 1 小时

**产出**:
- 创建 `~/projects/experience-engine/` 目录
- 初始化 Git repo
- 创建完整的目录结构（如上述 2.2 所示）
- README.md / ARCHITECTURE.md / CHANGELOG.md

#### Task 1.2：导入 Schema 定义
**Owner**: Agent
**时间盒**: 2 小时

**产出**:
- core/_meta/schemas/principle_schema.yaml
- core/_meta/schemas/mechanism_schema.yaml
- core/_meta/schemas/playbook_schema.yaml

#### Task 1.3：导入 90 个产出物
**Owner**: Agent
**时间盒**: 4 小时

**输入**:
- `/mnt/user-data/outputs/full_test_three_tier_architecture.md`

**产出**:
- A 库：36 个 .md 文件
- B 库：20 个 .yaml 文件
- 保险领域 C 库：34 个 .yaml 文件

#### Task 1.4：建立跨层依赖矩阵
**Owner**: Agent
**时间盒**: 3 小时

**产出**:
- core/_meta/cross_layer_dependencies.yaml
- 73 个依赖关系全部录入

### Week 2：种子内容补充

#### Task 1.5：从现有 L0/L1/L2 文档导入"种子"
**Owner**: Agent
**时间盒**: 1 周

**任务**：
- 扫描 /mnt/project/ 中的 L0/L1/L2 文档
- 提取核心原则、机制、框架
- 与本次 90 个产出物对比、合并、去重
- 形成 v1.0.0 的完整核心库

**预期产出**：
- A 库扩展到 50+ 条（基于 L0/L1/L2 文档的提取）
- B 库扩展到 30+ 个
- 完整的 v1.0.0 release notes

#### Task 1.6：版本发布 v1.0.0
**Owner**: Agent + Mark
**时间盒**: 1 天

**产出**:
- experience-engine v1.0.0 正式发布
- CHANGELOG.md 记录初版内容
- 文档站点上线（docs/）

## 4.3 Phase 2: 自动化能力（Week 3-4）

### Week 3：识别器代码化

#### Task 2.1：经验卡识别器实现
**Owner**: Agent
**时间盒**: 1 周

**输入**:
- v2.0 识别标准库
- 7 个会议逐字稿作为测试集

**产出**:
- extractors/extractor.py
- extractors/classification_rules.yaml
- extractors/classifier.py
- 单元测试（覆盖率 ≥ 80%）

**Acceptance**:
- 在 7 个会议上识别准确率 ≥ 85%
- 输出格式与 Schema 一致

#### Task 2.2：一致性检查工具
**Owner**: Agent
**时间盒**: 3 天

**产出**:
- governance/consistency_checker.py
- 跨层依赖循环检测
- 版本一致性检查
- 孤儿条目检测

### Week 4：月度聚合系统

#### Task 2.3：月度聚合 SOP 文档化
**Owner**: Agent + Claude
**时间盒**: 2 天

**产出**:
- governance/monthly_aggregation_sop.md
- governance/aggregation_template.md

#### Task 2.4：月度聚合自动准备脚本
**Owner**: Agent
**时间盒**: 3 天

**产出**:
- pipelines/prepare_aggregation.py
- 自动收集本月经验卡 / 反馈日志 / 升级建议
- 生成会议输入物

#### Task 2.5：第一次月度聚合会试运行
**Owner**: Mark + Claude
**时间盒**: 3 小时

**产出**:
- 第一次聚合会的 3 份输出文件（patch log / proposal queue / data plan）
- v1.1.0 升级清单

## 4.4 Phase 3: API 化（Week 5-8）

### Week 5-6：API 服务器

#### Task 3.1：API 服务器开发
**Owner**: Agent
**时间盒**: 2 周

**产出**:
- api/server.py（基于 FastAPI 或类似框架）
- api/openapi.yaml（OpenAPI 规范）
- 核心端点：
  - GET /principles（加载所有 A 库原则）
  - GET /mechanisms?context=xxx（加载相关 B 机制）
  - GET /playbooks?domain=insurance（加载领域 C 库）
  - GET /dependencies（加载跨层依赖图）
  - POST /feedback（接收执行反馈）

#### Task 3.2：客户端 SDK
**Owner**: Agent
**时间盒**: 1 周

**产出**:
- api/client_examples/python_client.py
- api/client_examples/insurance_integration.py
- 使用文档

### Week 7-8：insurance-analytics-v2 集成

#### Task 3.3：插入 experience-engine 到 generate_insights.py
**Owner**: Agent
**时间盒**: 1 周

**改造方式**：
```python
# 旧版（v3.0 之前）
def generate_insights(data):
    principles = HARDCODED_PRINCIPLES
    playbooks = load_local_playbooks()
    # ...

# 新版（集成 experience-engine）
def generate_insights(data):
    from experience_engine_client import ExperienceEngine
    engine = ExperienceEngine(version="^1.0.0")
    
    principles = engine.load_principles()
    playbooks = engine.load_playbooks(domain="insurance")
    # ...
    
    # 执行后反馈
    engine.submit_feedback(feedback_log)
```

#### Task 3.4：双轨运行验证
**Owner**: Agent
**时间盒**: 1 周

**任务**：
- 同样输入跑两个版本
- 对比输出差异
- 验证新版本输出质量不低于旧版本

## 4.5 Phase 4: 完全集成（Week 9-12）

### Week 9-10：切换主干

- insurance-analytics-v2 切换到 experience-engine 为主
- 本地 playbook 作为 fallback
- 监控 1 周

### Week 11-12：完全集成

- 删除 insurance-analytics-v2 的本地 playbook
- 完全依赖 experience-engine
- 准备其他项目（新动力）的集成方案

---

# 5. 启动决策点（4 个，Mark 拍板）

### 决策点 1：项目位置

**问题**：experience-engine 项目放在哪？

| Option | 说明 |
|---|---|
| A | 与 insurance-analytics-v2 同级，新建独立 Git repo |
| B | 在某个 monorepo 下作为独立模块 |
| C | 单独的 GitHub organization 下 |

**Claude 推荐**：**Option A**
- 理由：简单清晰，未来需要时再迁移到 monorepo 或 organization

### 决策点 2：API 协议

**问题**：API 用什么协议？

| Option | 说明 | 优缺点 |
|---|---|---|
| A | REST + JSON | 通用，易集成 |
| B | gRPC | 性能好，但更复杂 |
| C | 直接 Python import（无 API） | 最简单，但跨语言难 |

**Claude 推荐**：**Option A（REST + JSON）**
- 理由：跨语言友好，未来如果要做对外 SaaS 直接可用

### 决策点 3：开源 vs 私有

**问题**：experience-engine 是私有项目还是部分开源？

| Option | 说明 |
|---|---|
| A | 完全私有（公司核心资产） |
| B | core/ 完全私有，extractors/api/ 部分开源 |
| C | 全部开源（社区驱动） |

**Claude 推荐**：**Option A（完全私有）**
- 理由：A 库（思维体系）是 Mark 多年经验沉淀的核心资产，是估值 8-15x 的物理证据，不应开源

### 决策点 4：种子来源

**问题**：v1.0.0 的初始内容包含什么？

| Option | 说明 |
|---|---|
| A | 仅本次提取的 90 个产出物 |
| B | 90 个产出物 + 现有 L0/L1/L2 文档的"种子" |
| C | 90 个产出物 + L0/L1/L2 + Mark 旧的会议纪要里的精华 |

**Claude 推荐**：**Option B**
- 理由：Option A 太少（只覆盖近 7 个会议），Option C 工作量爆炸（80+ 历史 Summary），Option B 平衡完整性和工作量

---

# 6. Mark 启动指令模板

## 6.1 极简启动（已决定 4 个决策点）

```
Agent，启动 experience-engine 独立项目建设。

【核心文档】
本次启动的唯一入口：
/mnt/user-data/outputs/master_solution_v4.0.md

【4 个决策点的答案】
- 决策点 1（项目位置）：[Mark 填写：A/B/C]
- 决策点 2（API 协议）：[Mark 填写：A/B/C]
- 决策点 3（开源策略）：[Mark 填写：A/B/C]
- 决策点 4（种子来源）：[Mark 填写：A/B/C]

【任务】
按照 Part 4.2 的 Phase 1 顺序执行：
1. Task 1.1：创建独立项目（1h）
2. Task 1.2：导入 Schema（2h）
3. Task 1.3：导入 90 个产出物（4h）
4. Task 1.4：建立跨层依赖（3h）

完成 Week 1 后停下来，向我报告。
不要直接开始 Week 2（L0/L1/L2 提取需要更多对齐）。

【纪律】
- 严格遵守 L0_06 协作手册
- 每个 Task 给我"5 段格式报告"
- 有疑问主动 scope call，不要脑补
- 在 CHANGELOG.md 写日志

【验收标准】
Week 1 完成后我会：
1. 检查目录结构是否符合 Part 2.2 设计
2. 抽查 5 个 A 库 / 5 个 B 库 / 5 个 C 库 entry
3. 跑 consistency_checker.py 验证依赖矩阵

开始。
```

## 6.2 分阶段启动（还在决策中）

```
Agent，启动 experience-engine 项目的"决策准备阶段"。

【目标】
完成 4 个决策点的"准备工作"，让我能在 30 分钟内拍板。

【特别要求】
针对每个决策点：
1. 列出我之前未考虑到的"长期影响"
2. 评估"如果选错的回滚成本"
3. 给一个"3 年后回看"的视角

【时间盒】
2 小时

【约束】
不要做实质性建设。
```

---

# 7. 估值故事的物理证据（重要）

## 7.1 为什么独立项目对估值至关重要

```
v3.0 设计（子模块）：
  experience_library/ 在 insurance-analytics-v2 内
  → 投资人看到的：保险公司的工具
  → 估值倍数：3-4x（保险佣金）

v4.0 设计（独立项目）：
  experience-engine/ 是独立资产
  → 投资人看到的：行业 OS 的核心引擎
  → 估值倍数：8-15x（基础设施服务）

差异：
  10亿 HKD 收入下：
    v3.0 估值：30-40亿 HKD
    v4.0 估值：80-150亿 HKD
  
  差额：50-110亿 HKD
  
  这个差额的物理证据：
    - 独立的代码库
    - 独立的版本号
    - 独立的 API
    - 独立的客户（多个业务项目调用）
    - 独立的贡献者机制
```

## 7.2 给投资人讲的故事

```
Phase 1（当前）:
  "我们已经有了行业 OS 的核心引擎"
  证据：experience-engine v1.0.0 (90 个产出物)

Phase 2（6 个月后）:
  "我们的引擎已被多个业务消费"
  证据：insurance-analytics-v2 + 新动力 都集成了

Phase 3（12 个月后）:
  "我们的引擎可以快速适配新保司"
  证据：跨保司迁移的成功案例

Phase 4（24 个月后）:
  "我们的引擎对外 SaaS 化"
  证据：第一个外部客户付费使用
```

## 7.3 与 L1_02 v1.2 的完美对齐

```
L1_02 v1.2 描述的"AI = 经验机构化引擎"
                    "数据 = 深度关系的记忆外化"
                    "组织 = 规模化深关系的载体"

experience-engine 物理实现：
  AI 层：A/B/C 三层产出物 + Agent 加载
  数据层：跨层依赖矩阵 + 反馈日志归档
  组织层：贡献者机制 + 月度聚合会
  
完美对齐。
```

---

# 8. v4.0 vs v3.0 的关键差异总结

| 维度 | v3.0 子模块设计 | v4.0 独立项目设计 |
|---|---|---|
| **架构层级** | insurance-analytics-v2 的子目录 | 与业务项目平级的独立项目 |
| **版本管理** | 与保险业务版本耦合 | 独立版本号 |
| **复用方式** | 文件复制 | API 调用 |
| **跨项目集成** | 困难（需 fork） | 简单（API 调用） |
| **估值倍数支撑** | 弱（被埋在保险项目里） | 强（独立资产可见） |
| **战略叙事** | "保险业务的工具" | "行业 OS 的核心引擎" |
| **建设周期** | 4 周 | 12 周 |
| **未来扩展性** | 受保险业务约束 | 可对外 SaaS 化 |

**结论**：v4.0 多花 8 周，但**为下一个 5 年的估值故事打下基础**。

---

# 总结

## 你的判断 = 完全正确

✅ 经验机构化系统不应该是保险项目的子模块
✅ 应该是独立项目，与业务项目平级
✅ 应该作为基础设施被所有业务项目集成
✅ 这与 L0_02 "运营合伙人定位"、L1_02 "AI 数据组织升级"完全对齐

## 启动只需 3 件事

```
1. 拍板 4 个决策点（10 分钟）
2. 复制启动指令给 agent（1 分钟）
3. 等 Week 1 完成（4 个 Task，约 10 小时）后审核（30 分钟）

之后 12 周内：
  Week 1-2: 项目骨架 + 90 个产出物入库
  Week 3-4: 自动化能力（识别器 + 月度聚合）
  Week 5-8: API 化 + insurance-analytics-v2 集成
  Week 9-12: 完全集成，准备下一个项目
```

## 关键的 v4.0 创新点

1. **独立项目**：experience-engine 与 insurance-analytics-v2 平级
2. **业务中立的 core/ + 领域特定的 domains/**：清晰的边界
3. **API-First**：所有项目都通过 API 调用
4. **L0/L1/L2 文档导入**：现有沉淀直接成为种子
5. **估值故事的物理证据**：独立资产 = 8-15x 倍数的支撑

---

**方案版本**：v4.0（独立项目级 - 取代 v3.0）
**输出时间**：2026-04-26
**下一步动作**：Mark 拍板 4 个决策点 → 复制启动指令给 agent
