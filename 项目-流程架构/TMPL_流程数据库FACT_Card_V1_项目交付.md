---
type: project_note
project: 流程架构
layer: "02_过程成果-工作产出"
layer_tag: 过程
subdir: "数据库"
tags: [过程, 数据]
---

## 🧭 导航
⬆️ [[02_过程成果-工作产出]] · ⬆️ [[数据库]] · 🏠 [[流程架构项目MOC]]

---

# 流程数据库 FACT_Card 模板 V1.1

> 模板用途: 基于流程星型模型的标准分析卡，支持二维/三维流程运行分析与EA改进Insight产出
> 版本: V1.1 (2026-04-23)
> 所属: 流程团队主要交付成果 · 报告类型二
> 数据源: L3流程注册表 · L4活动清单 · Metabase数据平台
> 方法论依据: 流程数据库星型模型 (Star Schema for Process Analytics)
> 数据标准依据: DICT_流程数据库数据字典_V1.md（冲突时以数据字典为准）

---

## 一、流程数据库星型模型设计

### 1.1 模型总览

```
                        ┌──────────────────┐
                        │ DIM_M_STRATEGY   │
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
   │  VS-1~5+横切 │    │  (流程运行事实表)  │   │  YYYYMMDD整数键 │
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
                        │ DIM_DELIVERABLE  │◄───────────┘
                        │  (交付物维度)     │
                        │  物理交付物类型   │
                        └──────────────────┘
```

**设计要点**:
- 所有维度外键均使用**代理键**（Surrogate Key），避免自然键变更导致事实表历史数据失准
- `FACT_CARD` 保留少量自然键冗余字段（`l3_code`, `l4_code`, `vs_code`, `position_family`, `agentifiability`），支持无 JOIN 快速聚合
- `DIM_PROCESS` 采用 SCD Type 2（缓慢变化维），保留 L4 定义的历史版本
- 时间维度主键为 `INT` 类型的 `YYYYMMDD` 格式（如 20260423），便于分区与跨系统对齐

---

### 1.2 核心事实表: FACT_CARD

> 每一行 = 一次 L4 活动的完整执行实例记录
> schema: `process_analytics.FACT_CARD`

```sql
-- FACT_CARD 字段定义（与数据字典 FC-001 ~ FC-037 对齐）
CREATE TABLE FACT_CARD (
    -- 主键
    fact_id             UUID          NOT NULL DEFAULT gen_random_uuid(),
    record_date         DATE          NOT NULL,
    
    -- 维度代理键外键（星型模型标准做法）
    process_key         INT           NOT NULL,  -- FK → DIM_PROCESS(process_key)
    vs_key              INT           NOT NULL,  -- FK → DIM_VS(vs_key)
    org_key             INT,                     -- FK → DIM_ORG(org_key), NULLABLE(GAP-01过渡期)
    time_key            INT           NOT NULL,  -- FK → DIM_TIME(time_key), YYYYMMDD格式
    agent_key           INT,                     -- FK → DIM_AGENT(agent_key), NULLABLE
    strategy_key        INT,                     -- FK → DIM_M_STRATEGY(strategy_key), NULLABLE
    kpi_key             INT,                     -- FK → DIM_KPI(kpi_key), NULLABLE(Phase1/2)
    deliverable_key     INT,                     -- FK → DIM_DELIVERABLE(deliverable_key), NULLABLE
    
    -- 自然键冗余字段（用于无JOIN聚合与校验）
    l3_code             VARCHAR(20)   NOT NULL,  -- 格式: ^L3-[A-Z]{2,6}$
    l4_code             VARCHAR(20)   NOT NULL,  -- 格式: ^L4-[A-Z]{2,6}-\d{2}[a-z]?$
    vs_code             VARCHAR(10)   NOT NULL,  -- VS-1~VS-5 / L1-05
    position_family     VARCHAR(5),              -- A/B/C/D/E/F/G/职能, NULLABLE(GAP-01过渡期)
    agentifiability     VARCHAR(10)   NOT NULL,  -- Auto/Aug/Hybrid/Human
    
    -- 执行度量 (Measures)
    execution_status    VARCHAR(20)   NOT NULL,  -- 完成/进行中/阻断/逾期
    start_date          DATE,                    -- 实际开始日期
    end_date            DATE,                    -- 实际完成日期
    duration_hours      FLOAT       CHECK (duration_hours > 0),  -- 实际耗时(小时)
    sla_hours_actual    FLOAT,                   -- 写入时从DIM_PROCESS复制的SLA标准（防历史失真）
    sla_breach_flag     BOOLEAN     GENERATED ALWAYS AS (
                            CASE 
                                WHEN duration_hours IS NULL OR sla_hours_actual IS NULL THEN NULL
                                WHEN duration_hours > sla_hours_actual THEN TRUE
                                ELSE FALSE
                            END
                        ) STORED,
    rework_count        SMALLINT    DEFAULT 0 CHECK (rework_count >= 0),   -- 返工次数
    handoff_count       SMALLINT    DEFAULT 0 CHECK (handoff_count >= 0),  -- 交接次数
    
    -- 质量度量
    error_flag          BOOLEAN     DEFAULT FALSE,
    error_description   TEXT,                    -- error_flag=TRUE时必填, ≤500字符
    escalation_flag     BOOLEAN     DEFAULT FALSE,
    escalation_reason   TEXT,                    -- escalation_flag=TRUE时必填
    
    -- Agent介入度量
    agent_assist_flag   BOOLEAN     DEFAULT FALSE,
    agent_assist_hours  FLOAT       CHECK (agent_assist_hours >= 0),  -- Agent实际介入时长
    agent_save_hours    FLOAT,                   -- 节省人工时估算(=sla_hours_actual-duration_hours)
    human_override_flag BOOLEAN     DEFAULT FALSE,  -- 人工是否推翻Agent决策
    
    -- 价值度量
    ape_contribution    FLOAT       CHECK (ape_contribution >= 0),  -- 对APE的贡献(元)
    efficiency_score    FLOAT       CHECK (efficiency_score BETWEEN 0 AND 100),  -- 人效得分
    
    -- 审计字段
    data_source         VARCHAR(20) NOT NULL DEFAULT '手工录入',  -- 手工录入/Agent日志/系统自动/批量导入
    entry_by            VARCHAR(50),             -- 录入人账号
    created_at          TIMESTAMP   NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMP   NOT NULL DEFAULT NOW(),
    
    PRIMARY KEY (fact_id)
);
```

---

### 1.3 维度表定义

#### DIM_PROCESS — 流程维度

> 覆盖 L1→L2→L3→L4→L5 完整层级，含 Agent 化6维评分
> SCD Type 2：L4 定义随里程碑迭代，保留历史版本

```sql
CREATE TABLE DIM_PROCESS (
    process_key         SERIAL PRIMARY KEY,
    
    -- L1-L3 层级
    l1_code             VARCHAR(10)   NOT NULL,  -- L1-01~L1-05
    l1_name             VARCHAR(50),
    l2_code             VARCHAR(10),             -- 业务能力编码
    l2_name             VARCHAR(80),
    l3_code             VARCHAR(20)   NOT NULL,  -- SSOT主键, 如 L3-IAO
    l3_name             VARCHAR(100)  NOT NULL,
    l3_domain           VARCHAR(20)   NOT NULL,  -- KA/权益/经代/代理人/佣金/MGA/设计细分/经代联合/跨域
    l3_status           VARCHAR(10)   NOT NULL DEFAULT 'active',  -- active/draft/retired/merged
    l3_trigger          TEXT,                    -- 外部触发事件
    l3_exit_condition   TEXT,                    -- 可视化完成标志
    
    -- L4-L5 层级
    l4_code             VARCHAR(20)   NOT NULL,  -- 如 L4-COM-03 / L4-BME-05a
    l4_name             VARCHAR(100)  NOT NULL,  -- 动宾结构
    l4_deliverable      TEXT          NOT NULL,  -- 唯一物理交付物（禁止行为描述）
    l4_deliverable_type VARCHAR(30),             -- 报告/合同/凭证/数据表/决议/方案/系统记录/签字文件
    l4_accountable_role VARCHAR(80),             -- RACI中的A责任人岗位
    l4_accountable_family VARCHAR(5),            -- A责任人岗位族 A/B/C/D/E/F/G/职能/Mark
    l5_step             VARCHAR(200),            -- L5步骤描述（空率36.7%）
    
    -- Agent化评估（6维评分）
    agentifiability     VARCHAR(10)   NOT NULL,  -- Auto/Aug/Hybrid/Human
    agent_human_touchpoint TEXT,                 -- 人工介入点描述
    agent_d1_input_struct SMALLINT  CHECK (agent_d1_input_struct BETWEEN 0 AND 3),
    agent_d2_rule_clear   SMALLINT  CHECK (agent_d2_rule_clear BETWEEN 0 AND 3),
    agent_d3_output_verify SMALLINT CHECK (agent_d3_output_verify BETWEEN 0 AND 3),
    agent_d4_api_reach    SMALLINT  CHECK (agent_d4_api_reach BETWEEN 0 AND 3),
    agent_d5_fallback     SMALLINT  CHECK (agent_d5_fallback BETWEEN 0 AND 3),
    agent_d6_compliance   SMALLINT  CHECK (agent_d6_compliance BETWEEN 0 AND 3),
    agent_score_total     SMALLINT  CHECK (agent_score_total BETWEEN 0 AND 18),
    
    -- SLA与版本控制
    sla_hours           FLOAT       CHECK (sla_hours > 0),
    sla_source          VARCHAR(100),            -- 协同框架文件名+段落
    version             SMALLINT    NOT NULL DEFAULT 1,  -- SCD Type 2版本号
    valid_from          DATE        NOT NULL DEFAULT CURRENT_DATE,
    valid_to            DATE,                    -- NULL表示当前版本
    is_current          BOOLEAN     NOT NULL DEFAULT TRUE,  -- 每l4_code仅一条TRUE
    source_notes        TEXT                     -- 历史溯源备注（如G3-1/原BMC-01）
);
```

#### DIM_VS — 价值流维度

> 粒度：VS × Stage（每个价值流的每个阶段一行）

```sql
CREATE TABLE DIM_VS (
    vs_key              SERIAL PRIMARY KEY,
    vs_code             VARCHAR(10)   NOT NULL,  -- VS-1~VS-5 / L1-05
    vs_name             VARCHAR(80)   NOT NULL,
    vs_stakeholder      VARCHAR(50)   NOT NULL,  -- 外部利益相关者（禁止内部角色）
    s2b2a_layer         VARCHAR(5)    NOT NULL,  -- S/B/A/C/横切
    vs_trigger          TEXT,                    -- 价值流整体触发条件（仅stage_sequence=1时填写）
    stage_code          VARCHAR(10)   NOT NULL,  -- S1/S2/S7...
    stage_name          VARCHAR(80)   NOT NULL,
    stage_sequence      SMALLINT      NOT NULL CHECK (stage_sequence > 0),
    stage_exit_condition TEXT,                   -- 可视化完成标志
    l3_primary          VARCHAR(20),             -- 直属主要L3编码（可多，逗号分隔）
    l1_05_consumed      TEXT,                    -- 消费的L1-05能力JSON数组 ["L3-SRA",...]
    stage_deliverable   VARCHAR(200),            -- VS-*.csv第11列（可选）
    stage_kpi           VARCHAR(200),            -- VS-*.csv第12列（可选）
    coverage_status     VARCHAR(10)   NOT NULL DEFAULT 'PARTIAL'  -- OK/PARTIAL/GAP
);
```

#### DIM_ORG — 组织维度

> 粒度：岗位级（同一岗位族内可有多个岗位；同一岗位可有多个执行人，每人一行）

```sql
CREATE TABLE DIM_ORG (
    org_key             SERIAL PRIMARY KEY,
    position_family     VARCHAR(5)    NOT NULL,  -- A/B/C/D/E/F/G/职能
    position_family_name VARCHAR(50)  NOT NULL,
    position_code       VARCHAR(20),             -- 如 A-01
    position_name       VARCHAR(80),             -- 保司交付规则执行器
    position_nature     VARCHAR(10),             -- 执行/战略/专业
    ep_count            SMALLINT    CHECK (ep_count >= 0),   -- 核心介入点数量
    headcount_target_min SMALLINT   CHECK (headcount_target_min >= 0),
    headcount_target_max SMALLINT   CHECK (headcount_target_max >= 0),
    mark_retained       BOOLEAN     NOT NULL DEFAULT FALSE,   -- Mark保留决策
    executor_id         VARCHAR(20),             -- 工号
    executor_name       VARCHAR(50),
    reports_to_family   VARCHAR(5),              -- 汇报线岗位族
    is_active           BOOLEAN     NOT NULL DEFAULT TRUE,
    effective_date      DATE                     -- 岗位生效日期
);
```

#### DIM_TIME — 时间维度

> 脚本生成，覆盖 2024-01-01 至 2027-12-31

```sql
CREATE TABLE DIM_TIME (
    time_key            INT PRIMARY KEY,         -- YYYYMMDD，如 20260423
    full_date           DATE          NOT NULL UNIQUE,
    year                SMALLINT      NOT NULL,
    quarter             SMALLINT      NOT NULL CHECK (quarter BETWEEN 1 AND 4),
    month               SMALLINT      NOT NULL CHECK (month BETWEEN 1 AND 12),
    week                SMALLINT      NOT NULL CHECK (week BETWEEN 1 AND 53),  -- ISO周数
    day_of_week         SMALLINT      NOT NULL CHECK (day_of_week BETWEEN 1 AND 7),  -- 1=周一
    day_of_year         SMALLINT      NOT NULL CHECK (day_of_year BETWEEN 1 AND 366),
    is_weekday          BOOLEAN       NOT NULL   -- 周一至周五（不处理节假日）
);
```

#### DIM_AGENT — Agent维度

```sql
CREATE TABLE DIM_AGENT (
    agent_key           SERIAL PRIMARY KEY,
    agent_code          VARCHAR(30)   NOT NULL UNIQUE,  -- agent-[a-z-]+
    agent_name          VARCHAR(100)  NOT NULL,
    agent_type          VARCHAR(10)   NOT NULL,  -- Auto/Aug/Hybrid（不含Human）
    agent_status        VARCHAR(20)   NOT NULL,  -- 已上线/开发中/规划中/已停用
    l3_primary          VARCHAR(20),             -- 主覆盖L3编码
    l4_codes_json       TEXT,                    -- JSON数组 ["L4-COM-03",...]
    l4_count_covered    SMALLINT    CHECK (l4_count_covered >= 0),  -- 自动计算
    tech_stack          VARCHAR(100),            -- Claude API + PostgreSQL...
    platform_path       VARCHAR(200),            -- mga-data-platform相对路径
    owner_position_family VARCHAR(5),            -- 负责岗位族
    m4_priority         VARCHAR(5),              -- P0/P1/P2
    go_live_date        DATE,                    -- 上线日期
    baseline_accuracy   FLOAT     CHECK (baseline_accuracy BETWEEN 0 AND 1),
    baseline_throughput INT       CHECK (baseline_throughput >= 0)  -- 日均处理量(条/天)
);
```

#### DIM_M_STRATEGY — 战略维度

> 9行静态数据（M0~M8），Week 3 一次性录入

```sql
CREATE TABLE DIM_M_STRATEGY (
    strategy_key        SERIAL PRIMARY KEY,
    strategy_level      VARCHAR(5)    NOT NULL UNIQUE,  -- M0~M8
    strategy_name       VARCHAR(80)   NOT NULL,         -- 市场定位/价值主张...
    strategy_description TEXT,                         -- 业务含义
    claude_v2_domain    VARCHAR(20),                   -- 关联CLAUDE_V2域
    sequence            SMALLINT      NOT NULL CHECK (sequence BETWEEN 0 AND 8)
);
```

#### DIM_KPI — KPI维度

> 当前建空表，Week 6 KPI穿透矩阵完成后批量导入

```sql
CREATE TABLE DIM_KPI (
    kpi_key             SERIAL PRIMARY KEY,
    kpi_code            VARCHAR(20)   NOT NULL UNIQUE,
    kpi_name            VARCHAR(100)  NOT NULL,
    kpi_type            VARCHAR(20)   NOT NULL,  -- 企业KPI/岗位KPI/流程KPI
    kpi_level           VARCHAR(10)   NOT NULL,  -- 企业/L2/L3/岗位
    kpi_formula         TEXT,                    -- 计算公式文字描述
    kpi_target          FLOAT,                   -- 目标值
    kpi_unit            VARCHAR(20),             -- 万元/%/次/小时...
    measurement_cycle   VARCHAR(10)   NOT NULL,  -- 日/周/月/季/年
    vs_code             VARCHAR(10),             -- 关联价值流
    position_family     VARCHAR(5),              -- 关联岗位族
    strategy_level      VARCHAR(5),              -- 关联战略层级
    is_mark_kpi         BOOLEAN     NOT NULL DEFAULT FALSE  -- Mark保留顶层KPI
);
```

#### DIM_DELIVERABLE — 交付物维度

> 一个 L4 = 一个物理交付物 = 一行（L4唯一物理交付物原则）

```sql
CREATE TABLE DIM_DELIVERABLE (
    deliverable_key     SERIAL PRIMARY KEY,
    deliverable_name    TEXT          NOT NULL,  -- 与DIM_PROCESS.l4_deliverable完全一致
    deliverable_type    VARCHAR(30)   NOT NULL,  -- 报告/合同/凭证/数据表/决议/方案/系统记录/签字文件
    deliverable_category VARCHAR(20)  NOT NULL,  -- 文档/签约文件/数字产物/决策产物
    l4_code             VARCHAR(20)   NOT NULL UNIQUE,  -- 1:1关系
    l3_code             VARCHAR(20)   NOT NULL,
    vs_code             VARCHAR(10),             -- 主价值流
    agentifiability     VARCHAR(10)   NOT NULL   -- 冗余，用于交付物维度Agent分析
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
*数据模型与 DICT_流程数据库数据字典_V1.md 须保持字段级一致，冲突时以数据字典为准。*
*Insight产出是流程团队向Mark汇报的核心载体，格式不可随意修改。*

