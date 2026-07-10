---
type: 项目笔记
source: 08_任务与跟进/项目规划
synced: 2026-06-15
tags: [项目]
---

# 流程数据库 FACT_Card 模板 V1.0

> 模板用途: 基于流程星型模型的标准分析卡，支持二维/三维流程运行分析与EA改进Insight产出
> 版本: V1.0 (2026-04-21)
> 所属: 流程团队主要交付成果 · 报告类型二
> 数据源: L3流程注册表 · L4活动清单 · Metabase数据平台
> 方法论依据: 流程数据库星型模型 (Star Schema for Process Analytics)

---

## 一、流程数据库星型模型设计

### 1.1 模型总览

```
                        ┌──────────────────┐
                        │  DIM_STRATEGY    │
                        │  (战略维度)       │
                        │  M0-M8战略层级   │
                        └────────┬─────────┘
                                 │
   ┌──────────────┐              │              ┌──────────────────┐
   │  DIM_PROCESS │              │              │  DIM_ORG         │
   │  (流程维度)  │              │              │  (组织维度)       │
   │  L1-L5层级   ├──────────────┤              │  岗位族/岗位/人   │
   └──────────────┘              │              └────────┬─────────┘
                                 │                       │
   ┌──────────────┐    ┌─────────▼─────────┐   ┌────────┴─────────┐
   │  DIM_VS      │    │                   │   │  DIM_TIME        │
   │  (价值流维度) ├────►  FACT_CARD        ◄───┤  (时间维度)       │
   │  VS-1~5+横切 │    │  (流程运行事实表)  │   │  日/周/月/季/年   │
   └──────────────┘    │                   │   └──────────────────┘
                       └─────────┬─────────┘
                                 │
   ┌──────────────┐              │              ┌──────────────────┐
   │  DIM_KPI     │              │              │  DIM_AGENT       │
   │  (KPI维度)   ◄──────────────┤              │  (Agent维度)      │
   │  企业/岗位KPI│              │              │  Auto/Aug/Hybrid │
   └──────────────┘              │              └────────┬─────────┘
                                 │                       │
                        ┌────────▼─────────┐            │
                        │  DIM_DELIVERABLE │◄───────────┘
                        │  (交付物维度)     │
                        │  物理交付物类型   │
                        └──────────────────┘
```

---

### 1.2 核心事实表: FACT_CARD

> 每一行 = 一次流程活动的运行记录（可以是L3级别或L4级别）

```sql
-- FACT_CARD 字段定义
CREATE TABLE FACT_CARD (
    -- 主键
    fact_id             VARCHAR(32)   NOT NULL,  -- 唯一运行ID
    record_date         DATE          NOT NULL,  -- 记录日期
    
    -- 流程维度外键
    l1_code             VARCHAR(10),   -- L1节点编码 (L1-01~05)
    l2_code             VARCHAR(10),   -- L2业务能力编码
    l3_code             VARCHAR(20),   -- L3流程编码 (如: L3-IAO)
    l4_code             VARCHAR(20),   -- L4活动编码
    l5_step             VARCHAR(50),   -- L5步骤描述 (可选)
    
    -- 价值流维度外键
    vs_code             VARCHAR(10),   -- VS-1~VS-5 或 L1-05
    vs_stage            VARCHAR(20),   -- 价值阶段 (如: VS1-S1)
    
    -- 组织维度外键
    position_family     VARCHAR(5),    -- 岗位族 (A/B/C/D/E/F/G/职能)
    position_code       VARCHAR(20),   -- 岗位编码
    executor_id         VARCHAR(20),   -- 执行人ID
    
    -- 时间维度外键
    year                INT,
    quarter             INT,
    month               INT,
    week                INT,
    
    -- Agent维度外键
    agent_code          VARCHAR(30),   -- 配套Agent编码
    agent_type          VARCHAR(10),   -- Auto/Aug/Hybrid/Human
    
    -- 战略维度外键
    strategy_level      VARCHAR(5),    -- M0-M8
    
    -- KPI维度外键
    kpi_code            VARCHAR(20),   -- 关联KPI编码
    
    -- 交付物维度外键
    deliverable_type    VARCHAR(30),   -- 交付物类型
    deliverable_id      VARCHAR(50),   -- 交付物唯一标识
    
    -- 度量字段 (Measures)
    execution_status    VARCHAR(20),   -- 执行状态: 完成/进行中/阻断/逾期
    duration_hours      FLOAT,         -- 实际耗时(小时)
    sla_hours           FLOAT,         -- SLA标准时限(小时)
    sla_breach_flag     BOOLEAN,       -- 是否SLA违反
    rework_count        INT,           -- 返工次数
    handoff_count       INT,           -- 交接次数(协同复杂度)
    error_flag          BOOLEAN,       -- 是否有质量问题
    escalation_flag     BOOLEAN,       -- 是否升级至Mark
    agent_assist_flag   BOOLEAN,       -- 是否有Agent介入
    agent_save_hours    FLOAT,         -- Agent节省人工时(估算)
    
    -- 价值度量
    ape_contribution    FLOAT,         -- 对APE的贡献(元, 可为NULL)
    efficiency_score    FLOAT,         -- 人效得分 (0-100)
    
    -- 审计字段
    created_at          TIMESTAMP,
    updated_at          TIMESTAMP,
    source_system       VARCHAR(30)    -- 数据来源系统
);
```

---

### 1.3 维度表定义

#### DIM_PROCESS (流程维度)

```sql
CREATE TABLE DIM_PROCESS (
    process_key         SERIAL PRIMARY KEY,
    l1_code             VARCHAR(10),
    l1_name             VARCHAR(50),
    l2_code             VARCHAR(10),
    l2_name             VARCHAR(80),
    l3_code             VARCHAR(20),
    l3_name             VARCHAR(100),
    l3_vs_code          VARCHAR(10),      -- 归属价值流
    l3_trigger          TEXT,             -- 触发事件
    l3_deliverable      TEXT,             -- 标准交付物
    l4_code             VARCHAR(20),
    l4_name             VARCHAR(100),
    l4_agentifiability  VARCHAR(10),      -- Auto/Aug/Hybrid/Human
    l4_agent_score      INT,              -- 6维评分总分(0-18)
    is_active           BOOLEAN DEFAULT TRUE,
    valid_from          DATE,
    valid_to            DATE
);
```

#### DIM_VS (价值流维度)

```sql
CREATE TABLE DIM_VS (
    vs_key              SERIAL PRIMARY KEY,
    vs_code             VARCHAR(10),   -- VS-1~5, L1-05
    vs_name             VARCHAR(80),
    vs_stakeholder      VARCHAR(50),   -- 外部利益相关者
    s2b2a_layer         VARCHAR(10),   -- S/B/A/C/横切
    stage_code          VARCHAR(20),   -- VS1-S1 等
    stage_name          VARCHAR(80),
    stage_sequence      INT,
    coverage_status     VARCHAR(10)    -- OK/PARTIAL/GAP
);
```

#### DIM_ORG (组织维度)

```sql
CREATE TABLE DIM_ORG (
    org_key             SERIAL PRIMARY KEY,
    position_family     VARCHAR(5),
    position_family_name VARCHAR(50),
    position_code       VARCHAR(20),
    position_name       VARCHAR(80),
    position_nature     VARCHAR(20),  -- 执行/战略/专业
    headcount_target    INT,
    executor_id         VARCHAR(20),
    executor_name       VARCHAR(50),
    reports_to          VARCHAR(20),
    is_active           BOOLEAN DEFAULT TRUE
);
```

#### DIM_KPI (KPI维度)

```sql
CREATE TABLE DIM_KPI (
    kpi_key             SERIAL PRIMARY KEY,
    kpi_code            VARCHAR(20),
    kpi_name            VARCHAR(100),
    kpi_type            VARCHAR(20),   -- 企业KPI/岗位KPI/流程KPI
    kpi_level           VARCHAR(10),   -- L1/L2/L3/岗位
    kpi_formula         TEXT,
    kpi_target          FLOAT,
    kpi_unit            VARCHAR(20),
    measurement_cycle   VARCHAR(10),   -- 日/周/月/季/年
    vs_code             VARCHAR(10),   -- 关联价值流
    position_family     VARCHAR(5)     -- 关联岗位族
);
```

#### DIM_AGENT (Agent维度)

```sql
CREATE TABLE DIM_AGENT (
    agent_key           SERIAL PRIMARY KEY,
    agent_code          VARCHAR(30),
    agent_name          VARCHAR(100),
    agent_type          VARCHAR(10),   -- Auto/Aug/Hybrid
    agent_status        VARCHAR(20),   -- 已上线/开发中/规划中
    l4_codes            TEXT,          -- 覆盖的L4编码列表(JSON)
    tech_stack          VARCHAR(100),
    owner_position      VARCHAR(20),   -- 负责岗位
    go_live_date        DATE,
    m4_priority         VARCHAR(5)     -- P0/P1/P2
);
```

---

## 二、FACT_Card 单张分析卡

> 以下为单条流程分析的标准化卡片格式，支持Agent自动填写或人工填写。
> 每张FACT_Card对应一个L3流程在特定时间周期内的运行快照。

---

### FACT_Card 标准格式

```yaml
# ====================================================
# FACT_Card — 流程运行分析卡
# ====================================================
card_id: FC-[L3编码]-[YYYYMM]
generated_date: YYYY-MM-DD
analysis_period: YYYY-MM ~ YYYY-MM

# 流程标识
process:
  l1: L1-0?  # 飞轮节点
  l2: ""      # 业务能力组
  l3_code: "L3-XXX"
  l3_name: ""
  vs_code: "VS-?"
  vs_stage: "VS?-S?"

# 组织负责
org:
  position_family: ""   # A/B/C/D/E/F/G
  primary_owner: ""     # 主责岗位
  collaborators:        # 协同岗位
    - ""
    - ""

# ====== 运行度量 ======
execution_metrics:
  total_cases: 0            # 分析期内执行次数
  completed: 0              # 完成数
  in_progress: 0            # 进行中数
  blocked: 0                # 阻断数
  overdue: 0                # 逾期数
  completion_rate: "0%"     # 完成率

  # 效率
  avg_duration_hours: 0     # 平均耗时(小时)
  sla_standard_hours: 0     # SLA标准时限
  sla_compliance_rate: "0%" # SLA达标率
  avg_rework_count: 0       # 平均返工次数
  avg_handoff_count: 0      # 平均交接次数

  # 质量
  error_rate: "0%"          # 错误率
  escalation_rate: "0%"     # 上升至Mark的比率

# ====== Agent介入情况 ======
agent_metrics:
  agent_code: ""            # 配套Agent
  agent_type: ""            # Auto/Aug/Hybrid/Human
  agent_assist_rate: "0%"   # Agent介入率
  agent_save_hours_total: 0 # 分析期节省总人工时
  agent_error_rate: "0%"    # Agent产出错误率
  human_override_rate: "0%" # 人工覆盖Agent决策的比率

# ====== 价值度量 ======
value_metrics:
  ape_contribution: 0       # APE贡献(元)
  efficiency_score: 0       # 人效得分(0-100)
  strategic_kpi_impact:     # 对企业KPI的影响
    - kpi: "APE达成率"
      impact_direction: "+/-/~"
      evidence: ""
    - kpi: "人效(万/人/年)"
      impact_direction: "+/-/~"
      evidence: ""

# ====== 问题与阻断 ======
issues:
  top_blockers:
    - description: ""
      frequency: 0
      root_cause: ""
      sla_impact_hours: 0
  quality_issues:
    - description: ""
      frequency: 0
      downstream_impact: ""
```

---

## 三、二维分析视图

> 二维分析 = 两个维度的交叉透视，用于识别局部瓶颈和效率洼地。

### 3.1 价值流 × 流程效率矩阵 (VS × SLA达标率)

| 价值流 / SLA达标率 | <60% (红色预警) | 60-80% (黄色) | 80-95% (正常) | >95% (优秀) |
|------------------|----------------|--------------|--------------|------------|
| **VS-1 保司旅程** | _(L3列表)_ | | | |
| **VS-2 机构旅程** | | | | |
| **VS-3 KA旅程** | | | | |
| **VS-4 理财师旅程** | | | | |
| **VS-5 终端客户** | | | | |
| **L1-05 权益中台** | | | | |

**解读**: 红色区域 = 流程设计或执行存在系统性问题，优先进行EA改进。

---

### 3.2 岗位族 × Agent化实际效果 (组织 × AI协作成熟度)

| 岗位族 | L4总数 | Auto实际运行占比 | Agent节省人工时/月 | 人工覆盖率 | 成熟度评级 |
|-------|-------|----------------|-----------------|----------|---------|
| A 保司交付 | | | | | ⭐⭐⭐⭐⭐ |
| B 保司关系 | | | | | |
| C 机构业务 | | | | | |
| D 代理人运营 | | | | | |
| E 理财师辅导 | | | | | |
| F 权益中台 | | | | | |
| G 佣金合规 | | | | | |

**解读**: 人工覆盖率高但Agent评级为Auto → Agent质量不足，需调优；人工覆盖率低 → AI协作成熟。

---

### 3.3 L3流程 × 返工次数 (质量热力图)

| L3 编码 | 流程名称 | 月均返工次数 | 主因类别 | 改进优先级 |
|--------|---------|-----------|---------|---------|
| | | | 数据质量/规则缺失/岗位边界模糊/系统问题 | P0/P1/P2 |
| | | | | |

**改进建议触发规则**:
- 月均返工次数 > 3次 → 触发L3协同框架重新评审
- 月均返工次数 > 5次 → 触发 Mark 裁定会议

---

### 3.4 战略层级 × 流程覆盖密度 (M0-M8 × L3数量)

| 战略层级 | L3流程数量 | Agent化覆盖率 | 覆盖薄弱区域 |
|---------|----------|-------------|-----------|
| M0 市场定位 | | | |
| M1 价值主张 | | | |
| M2 商业模式 | | | |
| M3 组织能力 | | | |
| M4 产品服务 | | | |
| M5 渠道获客 | | | |
| M6 运营流程 | | | |
| M7 数据技术 | | | |
| M8 绩效合规 | | | |

---

## 四、三维分析视图

> 三维分析 = 三个维度同时考察，产生"改进点"层级的Insight。

### 4.1 价值流 × 岗位族 × 效率 (VA-ORG-EFF立方体)

> 问题: 哪条价值流的哪个岗位族执行效率最低？

| | VS-1 | VS-2 | VS-3 | VS-4 | VS-5 | L1-05 |
|--|------|------|------|------|------|-------|
| **A族** | _(SLA达标率)_ | | | | | |
| **B族** | | | | | | |
| **C族** | | | | | | |
| **D族** | | | | | | |
| **E族** | | | | | | |
| **F族** | | | | | | |

**读法**: 找出红色格子（SLA达标率<60%）→ 该价值流 × 该岗位族 = EA改进优先介入点

---

### 4.2 Agent化类型 × 错误率 × 战略影响 (AI质量 × 战略风险)

> 问题: 哪些已上线Agent实际错误率高，且对应的流程战略影响大？

| Agent | 类型 | 实际错误率 | 对应L3战略层级 | 风险等级 |
|-------|------|---------|-------------|--------|
| | Auto | | M? | 高/中/低 |
| | Aug | | | |
| | Hybrid | | | |

**风险等级判定**: 错误率>5% + 战略层级≤M3 → 高风险，需立即人工接管并重建规则

---

### 4.3 时间 × 流程 × 质量 (趋势分析)

> 问题: 哪些L3的质量在过去N个月呈恶化趋势？

| L3编码 | L3名称 | M-3月SLA | M-2月SLA | M-1月SLA | 本月SLA | 趋势 | 告警 |
|-------|-------|---------|---------|---------|-------|------|------|
| | | | | | | ↑↓→ | 🔴/🟡/🟢 |
| | | | | | | | |

**告警规则**:
- 🔴 连续3个月下降且当月<70% → 触发EA改进立项
- 🟡 单月下降>10% → 流程负责人本周内分析原因
- 🟢 连续上升或稳定>90% → 记录最佳实践

---

## 五、EA改进 Insight 卡

> 每条Insight = 一个可执行的企业架构改进建议，格式标准化、优先级明确。

### Insight 标准格式

```yaml
insight_id: INS-[YYYYMM]-[序号]
insight_date: YYYY-MM-DD
insight_type: 流程优化 / Agent建设 / 组织重设计 / 规则补充 / 数据质量

title: "_(一句话说明发现)_"

# 证据链
evidence:
  data_source: FACT_CARD / 二维分析 / 三维分析
  metrics:
    - metric: ""
      value: ""
      baseline: ""
  analysis_period: ""

# 根因
root_cause:
  level: L3流程 / L4活动 / 岗位边界 / Agent质量 / 规则缺失 / 数据问题
  description: ""

# 影响范围
impact:
  vs_affected: []      # 影响的价值流
  org_affected: []     # 影响的岗位族
  kpi_affected: []     # 影响的KPI

# 改进建议
recommendation:
  action: ""           # 具体动作
  owner: ""            # 负责人（岗位）
  timeline: ""         # 完成时限
  priority: P0/P1/P2
  expected_benefit: "" # 预期收益（量化）

# 裁定状态
decision_status: 待提交 / 待Mark裁定 / 已批准 / 已实施 / 已验证
mark_decision: ""
```

---

### Insight 汇总看板 (流程小组月度产出)

| Insight ID | 类型 | 标题 | 影响VS | 优先级 | 负责人 | 状态 |
|-----------|------|------|-------|-------|-------|------|
| INS-202604-001 | | | | P0 | | 待提交 |
| INS-202604-002 | | | | | | |

**月度Insight产出目标**: ≥5条 P1以上 Insight，≥1条 P0 Insight（需提Mark裁定）

---

## 六、数据采集路径

### 6.1 现有数据来源

| 数据类型 | 来源系统 | 采集方式 | 更新频率 | 负责人 |
|--------|---------|---------|---------|-------|
| 佣金流程数据 | Metabase / PostgreSQL | 自动ETL | 日 | Carrie |
| 业绩数据 | Metabase FACT_POLICY | 自动ETL | 日 | Carrie |
| 流程SLA记录 | 手工登记 → FACT_CARD | 人工录入 / Agent抽取 | 周 | 流程团队 |
| Agent运行日志 | mga-data-platform/agents | 程序日志 | 实时 | Carrie |
| L3协同框架 | 知识库02_架构全景/A4_流程库/ | 文档解析 | 按更新 | Terresa |
| KPI数据 | Metabase看板 | SQL查询 | 月 | Carrie |

### 6.2 数据录入优先级 (流程小组建设路线)

| 阶段 | 时间 | 目标 | 输入 |
|------|------|------|------|
| 第1阶段: 试点 | Week 1-2 | 选2-3条L3跑通FACT_CARD填写 | VS-2机构旅程(覆盖最好) |
| 第2阶段: 扩展 | Week 3-4 | 覆盖所有VS-2+VS-3的L3 | 现有OK状态L3 |
| 第3阶段: 补全 | Week 5-8 | 覆盖VS-1+VS-4新建L3 | 新建L3上线后 |
| 第4阶段: 自动化 | Week 9-12 | Agent自动采集SLA+质量数据 | M4 P4.1 规则引擎 |

---

*本模板由流程团队维护，数据模型需与 Carrie 对齐 PostgreSQL 实施方案。*
*Insight产出是流程团队向Mark汇报的核心载体，格式不可随意修改。*
