---
type: project_note
project: 流程架构
layer: "08_任务与跟进"
layer_tag: 任务
subdir: "AI上下文"
tags: [任务, AI]
---

## 🧭 导航
⬆️ [[08_任务与跟进]] · ⬆️ [[AI上下文]] · 🏠 [[流程架构项目MOC]]

---

# 流程架构落地工作方法论 V1.0

> 文档类型：工作方法论
> 版本：V1.0（2026-05-19）
> 负责人：Terresa
> 适用范围：EA项目 M4 阶段，L1-L4 流程架构向流程数据库的落地实施
> 依赖文档：
> - `DICT_流程数据库数据字典_V1_架构知识库.md`（字段规范权威来源）
> - `调研_付款流程_V1.0.xlsx`（L3现状调研）
> - `调研_L4交付物_含付款流程_V1.0.xlsx`（L4交付物调研）

---

## 一、方法论概述

### 1.1 核心问题

L1-L4 流程架构已完成设计（M1~M3 产出），但架构本身是静态的"应然"描述。
要让架构产生管理价值，必须回答一个问题：

> **"企业流程实际执行情况"如何持续、低成本地进入流程数据库，并支撑人效分析和 Agent 监督？**

### 1.2 核心判断

调研数据（付款流程调研、L4交付物调研）揭示了三个关键事实：

1. **现状与架构存在偏差**：大量 L4 的交付物"目前没有"或与 DIM_PROCESS 定义不符，
   说明维度表本身还有缺口，不能直接开始记录事实数据。

2. **数据表覆盖率低**：在调研的 79 条 L4 中，只有 L4-COM-01/02 有明确关联的
   数据库表，其余大多数 L4 的交付物仍是 Excel、邮件或口头确认。

3. **执行粒度不统一**：有的 L4 每天执行（如日常对账），有的每月执行一次
   （如佣金外发），不能用同一种触发机制处理。

### 1.3 方法论结构

基于以上判断，落地工作分为**三条并行路径**：

```
调研数据（现状）
│
├─ 路径 A：补全维度表 ──────────────────────────────────────────────────┐
│   调研 → DIM_PROCESS（角色/SLA）+ DIM_ORG（执行人）                    │
│                                                                        ▼
├─ 路径 B：系统自动记录 ─────────────────────────────────────────────► FACT_CARD
│   数据表写入事件 → CONFIG_PROCESS_EVENT_TRIGGER → 触发器 → 自动写入     ▲
│                                                                        │
└─ 路径 C：手工录入 ─────────────────────────────────────────────────────┘
    无数据表的 L4 → 标准录入表单 → 人工填写后批量导入
```

三条路径不是顺序执行，而是**同时推进**：
- 路径 A 是路径 B/C 的前提（维度表不完整，外键无法写入）
- 路径 B 覆盖有数据表的 L4（当前约 3%，M4.1 后逐步扩大）
- 路径 C 覆盖其余所有 L4（当前约 97%）

---

## 二、路径 A：调研数据 → 补全维度表

### 2.1 目标字段清单

调研数据能直接填充或辅助判断的维度表字段：

| 调研来源 | 调研列 | 目标表.字段 | 映射逻辑 |
|---------|--------|------------|---------|
| L4交付物调研·列9 | 交付物由哪个角色/岗位产生 | `DIM_PROCESS.l4_accountable_role` | 取角色名称，如"中台支持-蔡依娜"→"数据运营专员" |
| L4交付物调研·列9 | 同上 | `DIM_PROCESS.l4_accountable_family` | 按岗位族枚举映射，见 §2.2 |
| L4交付物调研·列7/8 | 该交付物当前是否存在 + 当前状态 | `DIM_PROCESS.l4_deliverable`（标注） | "目前没有"→在 source_notes 标注 GAP；"现状名称与定义不符"→提 Mark 裁定后更新 |
| L4交付物调研·列10 | 该交付物是否作为付款审批的必要凭证 | `DIM_PROCESS.source_notes` | "是"→追加标注 `付款凭证: TRUE`；"否"→不标注；空→待确认 |
| L4交付物调研·列13 | 关联数据表（英文） | `DIM_PROCESS.source_notes` | 补充实际数据流向，格式：`关联表: FACT_Commission_Rates` |
| 付款调研·业务付款需求调研·列10 | 付款频率 | `DIM_PROCESS.sla_hours` | 折算规则见 §2.3 |
| 付款调研·业务付款需求调研·列14 | 审批链 | `DIM_PROCESS.l4_accountable_role` | 取链条末端 A 角色；含"Mark"→填 'Mark（CEO）' |
| 付款调研·业务付款需求调研·列12 | 当前由谁执行付款 | `DIM_ORG.executor_name` | 配合 Ivan 的 HR 基线数据补入工号 |
| 付款调研·业务付款需求调研·列15 | 是否有SOP/checklist | `DIM_VS.coverage_status` | "无"→PARTIAL；"有"→OK；"目前没有"→GAP |
| 付款调研·员工报销调研·列4 | 报销审批链 | `DIM_PROCESS.l4_accountable_role`（L4-EXP-03） | Mark审批→'Mark（CEO）'；王总/魏总→提 Mark 裁定 |
| 付款调研·员工报销调研·列5 | 报销款支付执行人 | `DIM_ORG.executor_name`（L4-EXP-04） | JORJOR/Chaya→财务职能岗；牌照财务→各牌照主体财务 |
| 付款调研·主体差异调研·列4 | 各主体审批链 | `DIM_PROCESS.l4_accountable_role` | 按主体差异覆写，管理/服务公司→王总；牌照→Mark/魏总 |
| 付款调研·主体差异调研·列6 | 特殊合规要求 | `DIM_PROCESS.source_notes` | 追加标注 `合规: IA监管` 等 |

### 2.2 角色 → 岗位族映射规则

调研中出现的角色描述需标准化为 DIM_ORG 的 `position_family` 枚举值：

| 调研中的角色描述 | position_family | 说明 |
|----------------|----------------|------|
| 中台支持-MoMo / 中台支持-蔡依娜 / 中台支持-敏然 / 中台支持-杨婷 | F（权益中台）或待定 | 需与 Ivan 确认岗位族归属 |
| 财务-各牌照财务 / NANA / Chaya / JorJor | 职能 | 财务职能岗 |
| FIONA | 职能 | 绩效/培训相关，需与 Ivan 确认 |
| SOSO / masaki | 职能 | 各主体财务执行，需与 Ivan 确认 |
| Mark / Mark审批 | Mark | 保留11条战略事务 |
| 王总 / 魏总 | Mark 或 职能 | 需 Mark 裁定归属；主体差异调研显示：管理/服务公司→王总，牌照→Mark/魏总 |
| 业务端（KA/理财师） | 外部 | 不入 DIM_ORG，在 DIM_VS 中作为利益相关者 |

**操作规则**：调研列9中出现"目前没有"或角色为空的 L4，`l4_accountable_role` 暂填 NULL，
标记为 GAP-01 待办项，不阻断其他字段录入。

### 2.3 付款频率 → SLA 折算规则

付款调研中的频率描述需折算为 `DIM_PROCESS.sla_hours`（小时）：

| 调研描述 | 折算值（小时） | 折算依据 |
|---------|-------------|---------|
| 1个月2次，15日/30日 | 360h（15天×24h）| 按日历天 |
| 每月月初 / 权益每月30日 | 720h（30天）| 自然月 |
| 每周更新 | 168h（7天）| 自然周 |
| 每天 | 24h | 自然日 |
| 实时/即时 | 1h | 业务约定 |
| 每半年 / 正常每半年做一次 | 4320h（180天）| 自然半年 |
| 绩优团队长每月预支 | 720h（30天）| 按月触发，与月度付款同频 |

**注意**：折算后须经 Mark 或业务负责人确认，写入 `sla_hours` 时同步填写 `sla_source`
（格式：`调研_付款流程_V1.0.xlsx:业务付款需求调研:行N`）。

### 2.4 路径 A 操作步骤

```
Step 1  整理 L4 交付物调研列9（角色）→ 生成 L4_Auto_JD_Mapping_V1.csv
        输出：l4_code, accountable_role, accountable_family（GAP-01 交付物）

Step 2  整理 L4 交付物调研列10（付款凭证标记）→ 对标注"是"的 L4 在 DIM_PROCESS.source_notes
        追加 `付款凭证: TRUE`（当前涉及：L4-COM-10/11/12）

Step 3  将 L4_Auto_JD_Mapping_V1.csv 批量 UPDATE DIM_PROCESS
        UPDATE DIM_PROCESS SET l4_accountable_role=..., l4_accountable_family=...
        WHERE l4_code=... AND is_current=TRUE;

Step 4  整理付款调研·业务付款需求调研·列10（频率）→ 折算 sla_hours → 经业务确认后 UPDATE DIM_PROCESS

Step 5  将付款调研·业务付款需求调研·列12（执行人姓名）与 Ivan 的 HR 基线数据合并
        → 补填 DIM_ORG.executor_name + executor_id

Step 6  根据付款调研·业务付款需求调研·列15（SOP状态）批量更新 DIM_VS.coverage_status

Step 7  整理付款调研·员工报销调研（新增 Sheet）→ 补填 L4-EXP-01~05 的角色与审批链
        管理/服务公司：l4_accountable_role='Mark（CEO）'
        牌照经代机构：l4_accountable_role='王总/魏总'（提 Mark 裁定）

Step 8  整理付款调研·主体差异调研（新增 Sheet）→ 在 DIM_ORG 或 DIM_PROCESS.source_notes
        按主体标注合规要求（牌照→`合规: IA监管`）
```

---

## 三、路径 B：数据表事件 → 自动写入 FACT_CARD

### 3.1 设计原则

**核心思想**：数据表的写入/更新事件 = 某个 L4 活动已完成的信号。
当实际数据流向与 DIM_PROCESS 中定义的数据流向吻合时，系统自动生成 FACT_CARD 记录。

**三个关键约束**：
1. **批次粒度**：一张表的多行数据可能属于同一次 L4 执行（如月度佣金表有 N 行，
   但只对应一次"佣金外发"执行）。必须用 `batch_key_fields` 控制粒度，防止一行一条记录。
2. **幂等性**：同一批次重复触发不能产生重复 FACT_CARD。用 `l4_code + batch_key + record_date` 做唯一性检查。
3. **维度表就绪**：触发器写入前必须能 lookup 到 `process_key`（DIM_PROCESS）和 `vs_key`（DIM_VS），
   否则写入失败并记录到错误日志，不静默丢弃。

### 3.2 三层架构

```
层1  CONFIG_PROCESS_EVENT_TRIGGER（配置表）
     ↓ 定义：哪张表 + 什么事件 → 哪个 L4 + 如何推导字段
层2  fn_auto_write_fact_card()（通用写入函数）
     ↓ 执行：lookup 维度表 → 推导字段 → 幂等检查 → INSERT FACT_CARD
层3  trg_[source_table]_to_fact（各源表触发器）
     ↓ 触发：构造 batch_key → 调用层2
```

### 3.3 CONFIG_PROCESS_EVENT_TRIGGER 配置表结构

```sql
CREATE TABLE process_analytics.CONFIG_PROCESS_EVENT_TRIGGER (
    trigger_id        SERIAL PRIMARY KEY,
    source_schema     VARCHAR(50)  NOT NULL,   -- 被监听的 schema
    source_table      VARCHAR(100) NOT NULL,   -- 被监听的表名
    trigger_event     VARCHAR(10)  NOT NULL,   -- INSERT / UPDATE
    trigger_condition TEXT,                    -- 可选 WHERE 条件（如 status='confirmed'）
    l4_code           VARCHAR(20)  NOT NULL,   -- 对应哪个 L4
    start_time_field  VARCHAR(100),            -- 源表中的开始时间字段
    end_time_field    VARCHAR(100),            -- 源表中的结束时间字段
    executor_field    VARCHAR(100),            -- 源表中的执行人字段
    batch_key_fields  TEXT[],                  -- 批次粒度字段（如 ['year_month','entity']）
    is_active         BOOLEAN DEFAULT TRUE,
    description       TEXT
);
```

### 3.4 FACT_CARD 字段自动化覆盖率

| 字段 | 自动填充 | 来源 |
|------|---------|------|
| fact_id / record_date / created_at / updated_at | ✅ 100% | 系统生成 |
| process_key / l3_code / l4_code / agentifiability | ✅ 100% | DIM_PROCESS lookup |
| vs_key / vs_code | ✅ 100% | DIM_VS lookup |
| time_key / end_date | ✅ 100% | 触发事件时间戳 |
| execution_status | ✅ 默认"完成" | 数据表有数据 = 活动已完成 |
| sla_hours_actual | ✅ 有值时 | DIM_PROCESS.sla_hours 快照 |
| start_date / duration_hours | ⚠️ 有源字段时 | 源表需有 created_at 类字段 |
| org_key / position_family | ⚠️ 有执行人字段时 | 依赖 DIM_ORG 人员映射完成 |
| rework_count / handoff_count | ⚠️ 默认 0 | 需人工确认或从版本历史推导 |
| error_flag / escalation_flag | ❌ 默认 FALSE | 必须人工补充，进入 review 队列 |
| agent_assist_flag | ✅ 当前全 FALSE | M4.1 Agent 上线后改为从日志读取 |
| kpi_key / strategy_key | ❌ NULL | 需补充 L3→战略映射表后自动化 |

### 3.5 当前可挂触发器的 L4（基于表间关系对照_V1 更新，2026-05-19）

数据来源：`02_过程成果-工作产出/映射分析/表间关系对照_数据表与L3-L4流程映射.xlsx`

共 **20 个 L4** 已有关联数据表（覆盖 79 条 L4 的约 25%），合计 **51 张表**。

| L4编码 | L4名称 | 关联数据表（英文） | 当前填写人 | batch_key_fields 建议 |
|--------|--------|-----------------|-----------|----------------------|
| L4-IPI-01 | 产品元数据录入配置 | MAPPING_PRODUCT, DIM_PRODUCT_SKU, DIM_PRODUCT_ID, fact_insurance_plan_header, fact_insurance_plan_lines, fact_insurance_plan_header_history, fact_insurance_plan_lines_history, config_product_feature_type, dim_product_feature_value, dim_product_benefit_profile | 李思齐/Mia/Carrie | ['product_id', 'carrier_code'] |
| L4-IPI-02 | 佣金政策拆解配置 | Config_Product_Commission_Formula | 刘敏然 | ['product_id', 'effective_date'] |
| L4-COM-01 | 佣金政策接收与校准 | 佣金准入表, Config_License_Carrier_Mapping, FACT_COMMISSIOM_RATE, Agg_Source_Commission_Wide_Table | 刘敏然/Momo/Carrie/敏然 | ['year_quarter', 'license_entity'] |
| L4-COM-02 | 差异化拆解与验证 | CONFIG_PARTNER_ROUTING, Product_Risk_Override, Partner_Tier_Rules, Config_Product_Exclusion_Range, Config_Commission_Table_Type, Agg_Market_Commission_Tier_Rate, 市场佣金表 | momo/Carrie | ['effective_date', 'partner_id'] |
| L4-COM-10 | 保单信息整合与应收核算 | FACT_CCOMMSSION | 未分配 | ['year_month', 'license_entity'] |
| L4-COM-12 | 应派金额拆分与渠道对账 | Agg_Commission_Payable | 廖晓希 | ['year_month', 'payee_id'] |
| L4-IAC-05 | 合同启动与进入IPI | DIM_Carrier, DIM_LICENSE | 菲菲/敏然 | ['carrier_code', 'license_code'] |
| L4-KASC-02 | 协议签订 | DIM_SEGMENTATION, DIM_PARTNER, DIM_KA, DIM_BINDER_AGREEMENT | 廖晓希 | ['partner_id', 'agreement_id'] |
| L4-KAOP-02 | 系统配置 | BRIDGE_PARTNER_KA | 廖晓希 | ['partner_id', 'ka_id'] |
| L4-KAGA-03 | 业绩复盘 | 合作伙伴全景分析报告 | Carrie | ['year_month', 'partner_id'] |
| L4-RSJD-01 | 销售执行与客户管理 | FACT_POLICY, 销售业绩报表, DIM_CUSTOMER, DIM_Client_Segment | 廖晓希/刘斯琦/敏然 | ['year_month', 'partner_id'] |
| L4-BSRV-02 | 结算与评估 | DIM_PAYEE, MAP_PARTNER_PAYEE | masaki | ['payee_id', 'effective_date'] |
| L4-OBC-02 | 设置目标 | DIM_Strategy | 马原媛 | ['strategy_id', 'year'] |
| L4-RSD-01 | 权益方案需求分析与框架设计 | DIM_Comm_Scheme, Config_Strategy_Header, Config_Strategy_Tiers, DIM_Partner_Equity, Bridge_Strategy_Routing | 马原媛 | ['scheme_id', 'effective_date'] |
| L4-SSVA-01 | 服务对账 | FACT_SERVICE_RECORD | 马原媛 | ['year_month', 'partner_id'] |
| L4-SSVA-03 | 成本测算及预算 | Config_License_Cost_Deduction | masaki | ['year', 'license_entity'] |
| L4-SPE-01 | 目标体系设计 | FACT_TARGET | 廖晓希 | ['year', 'segment_id'] |
| L4-HRD-02 | 人力资源体系建设 | DIM_EMP | 袁林 | ['emp_id', 'effective_date'] |
| L4-IMF-01 | 数据采集与质量校验 | FACT_SALES_AGG | 未分配 | ['year_month', 'carrier_code'] |
| L4-IMF-02 | 分析模型运行与洞察 | FACT_GOAL_TRACKING | 未分配 | ['year_month', 'segment_id'] |

**尚无 L4 映射的表（11张，需补充）**：DIM_DATE、FACT_ALLOCATED_COST、FACT_RISK、FACT_SALES_ACTIVITY、PRODUCT_SERIES_BRIDGE、DIM_ENTITY、DIM_ORG、FACT_SALES_FUNNEL、CARRIER_ENTITY_MAPPING、LICENSE_HANGING_RULES、SOP_SCORE_REPORT

其余约 59 条 L4 暂无关联数据表，走路径 C（手工录入）。

---

## 四、路径 C：手工录入（无数据表的 L4）

### 4.1 适用范围

当前数据表映射覆盖 **20 个 L4**（约占 79 条 L4 的 25%），合计关联 51 张表。
这些 L4 可接入路径 B 实现系统自动记录。其余约 59 条 L4 的交付物仍为 Excel、邮件或"目前没有"，
需通过标准录入表单由执行人事后填写。

### 4.2 标准录入字段（最小必填集）

执行人每次完成 L4 活动后，只需填写以下 6 个字段，其余由系统从维度表自动补全：

| 字段 | 说明 | 示例 |
|------|------|------|
| l4_code | 从下拉菜单选择 | L4-COM-12 |
| end_date | 完成日期 | 2026-05-15 |
| start_date | 开始日期（可选） | 2026-05-10 |
| execution_status | 完成 / 部分完成 / 未完成 | 完成 |
| rework_count | 返工次数（0起） | 1 |
| error_flag + error_description | 是否出现错误 + 简述 | TRUE, "银行流水对不上" |

系统自动补全：process_key、vs_key、agentifiability、sla_hours_actual、data_source='手工录入'。

### 4.3 录入频率要求

| L4 执行频率 | 录入截止时间 |
|------------|------------|
| 每日 | 当日 18:00 前 |
| 每周 | 周五 17:00 前 |
| 每月 | 次月 3 日前 |
| 临时/事件驱动 | 完成后 24h 内 |

### 4.4 GAP 处理规则

调研中标注"目前没有"的 L4，执行人暂时无法录入（因为该活动本身不存在）。
处理方式：
- 在 DIM_PROCESS.source_notes 标注 `GAP: 活动当前未执行`
- 不强制录入 FACT_CARD，避免产生虚假数据
- 每季度复查一次，确认 GAP 是否已被填补或需要从 L4 清单中移除

---

## 五、质量控制与审核机制

### 5.1 三类质量问题与处理规则

| 问题类型 | 识别方式 | 处理规则 |
|---------|---------|---------|
| **维度缺失**：FACT_CARD 写入时 process_key 为 NULL | 触发器写入失败日志 | 先补 DIM_PROCESS，再重跑触发器 |
| **字段默认值未确认**：error_flag=FALSE 但实际有错误 | V_FACT_CARD_PENDING_REVIEW 视图 | 执行人每周五前确认并更新 |
| **SLA 超时**：duration_hours > sla_hours_actual | FACT_CARD.sla_breach_flag=TRUE | 自动标记，月度 review 时由 Mark 裁定是否升级 |

### 5.2 待补充队列视图

```sql
-- 找出系统自动写入但关键字段仍为默认值、需人工确认的记录
CREATE VIEW process_analytics.V_FACT_CARD_PENDING_REVIEW AS
SELECT
    fact_id, l4_code, record_date,
    duration_hours, sla_breach_flag,
    rework_count, error_flag, escalation_flag,
    data_source,
    '请确认：rework_count / error_flag / escalation_flag 是否准确' AS review_hint
FROM process_analytics.FACT_CARD
WHERE data_source IN ('系统自动', '手工录入')
  AND record_date >= CURRENT_DATE - INTERVAL '7 days'
  AND rework_count = 0
  AND error_flag = FALSE
  AND escalation_flag = FALSE
ORDER BY record_date DESC;
```

### 5.3 月度数据质量检查清单

每月第一个工作日，Terresa 执行以下检查：

```
□ 1. 查 V_FACT_CARD_PENDING_REVIEW，推送给对应执行人补充确认
□ 2. 查 FACT_CARD WHERE process_key IS NULL，补填维度表后重跑
□ 3. 查 FACT_CARD WHERE sla_breach_flag=TRUE，整理超时清单提交 Mark review
□ 4. 查 DIM_PROCESS WHERE source_notes LIKE '%GAP%'，确认 GAP 状态是否变化
□ 5. 更新 CONFIG_PROCESS_EVENT_TRIGGER，新增上月新接入的数据表映射
```

---

## 六、分阶段实施路线图

### 阶段划分逻辑

路线图与 M4 批次对齐，每个阶段的核心目标是提升 FACT_CARD 的自动化覆盖率。

| 阶段 | 时间窗 | 核心目标 | FACT_CARD 自动化率目标 |
|------|--------|---------|----------------------|
| **Phase 0：地基** | 当前~W4 | 维度表补全 + 手工录入跑通 | 0%（全手工） |
| **Phase 1：接管数据管道** | M4.1（W1~W16）| 9条数据管道 L4 接入触发器 | ~15% |
| **Phase 2：规则引擎覆盖** | M4.2（M4.1后2~3月）| 18条规则引擎 L4 接入 | ~40% |
| **Phase 3：智能分析接入** | M4.3（M4.2后2~3月）| Agent 日志管道 + MCP/RAG | ~65% |
| **Phase 4：长尾收尾** | M4.4（M4.3后1~2月）| 剩余 6 条长尾 L4 | ~80% |

### Phase 0 具体任务（当前优先级最高）

```
Week 1
  □ 路径A：整理 L4 交付物调研列9 → 生成角色映射 CSV → UPDATE DIM_PROCESS
  □ 路径A：整理付款调研列10 → 折算 SLA → 经 Mark 确认后 UPDATE DIM_PROCESS
  □ 路径C：搭建手工录入表单（最小6字段）→ 发给付款流程执行人试填

Week 2
  □ 路径A：与 Ivan 对齐 DIM_ORG 人员数据 → 补填 executor_id
  □ 路径B：建 CONFIG_PROCESS_EVENT_TRIGGER 表 → 录入 L4-COM-01/02 规则
  □ 路径B：在 FACT_Commission_Rates 上挂触发器 → 验证自动写入链路
  □ 路径C：收集第一批手工录入数据 → 检查 V_FACT_CARD_PENDING_REVIEW

Week 3~4
  □ 修复 Phase 0 发现的维度缺口（GAP 清单）
  □ 输出第一份月度数据质量报告 → 提交 Mark review
  □ 确认 Phase 1 数据管道 L4 的源表清单 → 准备触发器开发
```

---

## 七、关键决策点与红线

### 7.1 需要 Mark 裁定的决策

以下情况不能由 Terresa 自行决定，必须提交 Mark：

| 情况 | 提交方式 | 说明 |
|------|---------|------|
| 调研角色与 DIM_PROCESS 定义不符（如"王总"应归哪个岗位族）| 月度 review 清单 | 影响 RACI 归属 |
| SLA 折算值与业务实际不符（如"1个月2次"但实际不规律）| 即时提交 | 影响 sla_breach_flag 准确性 |
| GAP 类 L4 是否需要从清单中移除 | 季度复查 | 影响 agentifiability 统计 |
| escalation_flag=TRUE 的记录 | 即时提交 | 属于 Mark 保留的11条战略事务范围 |

### 7.2 M4 阶段红线（不可逾越）

- **禁止**：基于 FACT_CARD 数量直接重组岗位（需经 Mark 战略裁定）
- **禁止**：在 Jasper 解禁前将 GAP 类 L4 写入 SOP 文档
- **禁止**：将 Agent 日志直接写入 FACT_CARD 而不经过 CONFIG_PROCESS_EVENT_TRIGGER 映射层
- **禁止**：删除 DIM_PROCESS 中的历史版本记录（只能 is_current=FALSE，不能物理删除）

---

## 八、附录

### 附录 A：调研列号速查

| 文件 | Sheet | 列号 | 含义 |
|------|-------|------|------|
| 调研_L4交付物_含付款流程_V1.0.xlsx | L4交付物调研 | 列4 | L4编码 |
| 调研_L4交付物_含付款流程_V1.0.xlsx | L4交付物调研 | 列7 | 交付物当前是否存在 |
| 调研_L4交付物_含付款流程_V1.0.xlsx | L4交付物调研 | 列8 | 当前状态描述 |
| 调研_L4交付物_含付款流程_V1.0.xlsx | L4交付物调研 | 列9 | 交付物由哪个角色产生 |
| 调研_L4交付物_含付款流程_V1.0.xlsx | L4交付物调研 | 列10 | 该交付物是否作为付款审批的必要凭证（新增）|
| 调研_L4交付物_含付款流程_V1.0.xlsx | L4交付物调研 | 列13 | 关联数据表（英文） |
| 调研_付款流程_V1.0.xlsx | 业务付款需求调研 | 列3 | L3编码 |
| 调研_付款流程_V1.0.xlsx | 业务付款需求调研 | 列10 | 付款频率 |
| 调研_付款流程_V1.0.xlsx | 业务付款需求调研 | 列12 | 当前执行人 |
| 调研_付款流程_V1.0.xlsx | 业务付款需求调研 | 列14 | 审批链 |
| 调研_付款流程_V1.0.xlsx | 业务付款需求调研 | 列15 | 是否有SOP/checklist |
| 调研_付款流程_V1.0.xlsx | 员工报销调研（新增）| 列4 | 报销审批链 → L4-EXP-03 |
| 调研_付款流程_V1.0.xlsx | 员工报销调研（新增）| 列5 | 报销款支付执行人 → L4-EXP-04 |
| 调研_付款流程_V1.0.xlsx | 主体差异调研（新增）| 列4 | 各主体审批链（按主体覆写 DIM_PROCESS）|
| 调研_付款流程_V1.0.xlsx | 主体差异调研（新增）| 列6 | 特殊合规要求（牌照→IA监管标注）|

### 附录 B：通用 FACT_CARD 写入函数（核心 DDL）

```sql
CREATE OR REPLACE FUNCTION process_analytics.fn_auto_write_fact_card(
    p_l4_code         VARCHAR(20),
    p_end_time        TIMESTAMP,
    p_start_time      TIMESTAMP DEFAULT NULL,
    p_executor_name   VARCHAR(50) DEFAULT NULL,
    p_batch_key       VARCHAR(100) DEFAULT NULL
) RETURNS UUID AS $$
DECLARE
    v_fact_id         UUID;
    v_process_key     INT;
    v_vs_key          INT;
    v_l3_code         VARCHAR(20);
    v_vs_code         VARCHAR(10);
    v_agentifiability VARCHAR(10);
    v_sla_hours       FLOAT;
    v_duration_hours  FLOAT;
    v_deliverable_key INT;
    v_org_key         INT;
BEGIN
    -- 幂等检查
    IF p_batch_key IS NOT NULL AND EXISTS (
        SELECT 1 FROM process_analytics.FACT_CARD
        WHERE l4_code = p_l4_code AND data_source = '系统自动'
          AND entry_by = 'system:' || p_batch_key
    ) THEN RETURN NULL; END IF;

    -- lookup DIM_PROCESS
    SELECT process_key, l3_code, agentifiability, sla_hours
    INTO v_process_key, v_l3_code, v_agentifiability, v_sla_hours
    FROM process_analytics.DIM_PROCESS
    WHERE l4_code = p_l4_code AND is_current = TRUE LIMIT 1;

    IF v_process_key IS NULL THEN
        RAISE WARNING 'fn_auto_write_fact_card: l4_code % not in DIM_PROCESS', p_l4_code;
        RETURN NULL;
    END IF;

    -- lookup DIM_VS
    SELECT vs_key, vs_code INTO v_vs_key, v_vs_code
    FROM process_analytics.DIM_VS
    WHERE l3_primary LIKE '%' || v_l3_code || '%' LIMIT 1;

    -- lookup DIM_DELIVERABLE
    SELECT deliverable_key INTO v_deliverable_key
    FROM process_analytics.DIM_DELIVERABLE WHERE l4_code = p_l4_code LIMIT 1;

    -- lookup DIM_ORG
    IF p_executor_name IS NOT NULL THEN
        SELECT org_key INTO v_org_key FROM process_analytics.DIM_ORG
        WHERE executor_name = p_executor_name AND is_active = TRUE LIMIT 1;
    END IF;

    -- 计算耗时（合理性检查）
    IF p_start_time IS NOT NULL THEN
        v_duration_hours := EXTRACT(EPOCH FROM (p_end_time - p_start_time)) / 3600.0;
        IF v_duration_hours <= 0 OR v_duration_hours > 2000 THEN
            v_duration_hours := NULL;
        END IF;
    END IF;

    v_fact_id := gen_random_uuid();
    INSERT INTO process_analytics.FACT_CARD (
        fact_id, record_date, process_key, vs_key, org_key,
        time_key, deliverable_key, l3_code, l4_code, vs_code,
        agentifiability, execution_status, start_date, end_date,
        duration_hours, sla_hours_actual, rework_count, handoff_count,
        error_flag, escalation_flag, agent_assist_flag,
        data_source, entry_by, created_at, updated_at
    ) VALUES (
        v_fact_id, p_end_time::DATE, v_process_key, v_vs_key, v_org_key,
        CAST(TO_CHAR(p_end_time,'YYYYMMDD') AS INT), v_deliverable_key,
        v_l3_code, p_l4_code, v_vs_code,
        v_agentifiability, '完成', p_start_time::DATE, p_end_time::DATE,
        v_duration_hours, v_sla_hours, 0, 0,
        FALSE, FALSE, FALSE,
        '系统自动', COALESCE('system:'||p_batch_key,'system:auto'), NOW(), NOW()
    );
    RETURN v_fact_id;
END;
$$ LANGUAGE plpgsql;
```

### 附录 C：文档版本记录

| 版本 | 日期 | 变更说明 | 作者 |
|------|------|---------|------|
| V1.0 | 2026-05-19 | 初版，整合调研分析与事件驱动架构方案 | Terresa + Claude |
| V1.1 | 2026-05-19 | 同步表间关系对照映射更新：§3.5 可触发 L4 从 2 条扩展至 20 条（51张表），§4.1 覆盖率描述更新为 25% | Terresa + Claude |
| V1.2 | 2026-05-19 | 同步调研文件更新：§2.1 新增列10（付款凭证）及员工报销/主体差异调研映射；§2.2 补充杨婷/FIONA/SOSO等角色；§2.3 新增半年/绩优预支频率折算；§2.4 新增 Step 2/7/8；附录A 更新文件名及新增 Sheet 列号 | Terresa + Claude |

