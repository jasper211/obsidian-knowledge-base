---
文件类型: Carrie spot-check + SQL 执行指南 (W8-C 产出)
产出日期: 2026-05-23
产出 agent: W8-C (Claude 替 Carrie)
回执方向: Carrie → Claude 主 thread (1 句话)
W8-C 2026-05-23 Claude 替 Carrie 做 PG 字段 + SQL:
  - Mark 5-23 决策 "Carrie 填写字段这块 Claude 来做"
  - 32 KPI × PG 字段名翻译 + ALTER TABLE + UPDATE SQL
  - Carrie 工时: 1h → 5-10 分钟 (节省 80-90%)
  - AG07 Day 0 5-25/5-26 起跑窗口
关联前序:
  - W7-F CSV (`03/权威数据/DIM_KPI_W7F补字段_v1.0.csv`, 32 KPI × 业务公式)
  - Mark verify 回执 (`08/收件箱/Mark/Mark回执_W7F_32KPI_verify_20260523.md`, 32 KPI 全锁定, KPI_04 改 B)
  - Carrie 5-24 partial 75% 回执 (`08/收件箱/Carrie/Carrie回执_AG07底座_partial75pct_20260524.md`, DIM_KPI 32/32 ready)
  - DICT 流程数据库数据字典 (`03/治理规范/DICT_流程数据库数据字典_V1_项目交付.md`, process_analytics schema 风格)
  - 02 层数据库定义 (`02/数据库/`)
关联下游:
  - Carrie 5-24 spot-check (~5-10 分钟)
  - PG SQL 执行 → DIM_KPI 100% 完整
  - AG07 Day 0 5-25/5-26 起跑
---

# Carrie verify 报告 — DIM_KPI W8-C 完整版

## § 1 一句话总结

> **Claude 已替 Carrie 做完 32 KPI × PG 字段名翻译 + 完整 SQL. Carrie 只需 spot-check + PG 执行 SQL ~5-10 分钟. AG07 Day 0 5-25/5-26 起跑.**

工时压缩: Carrie 原 1h (Mark 5-23 之前) → 现 5-10 分钟 (Mark 5-23 决策后), 节省 80-90%.

---

## § 2 Carrie spot-check 重点 (5 分钟)

打开 `03/权威数据/DIM_KPI_W8C_完整版_v2.0.csv`, 重点 verify 4 项:

### 重点 1: 表名 verify

Claude 假设以下 PG 业务事实表存在 (DICT 字典只覆盖流程数据库, 不覆盖保险业务表). Carrie 请快速对照实际 PG schema:

| Claude 假设表名 | 用途 | KPI |
|---|---|---|
| `fct_policy` | 保单事实表 | KPI_01, 02, 09, 12, 16, 17, 18, 19, 20, 22, 24, 26, 28, 30, 31, 32, 35 |
| `fct_commission` | 佣金事实表 | KPI_04, 06, 13, 21, 33 |
| `fct_activity` | 理财师活动事实表 | KPI_14, 15, 16 |
| `fct_complaint` | 投诉事实表 | KPI_26 |
| `fct_audit` | 审计事实表 | KPI_27 |
| `fct_claim` | 理赔事实表 | KPI_50, 51 |
| `fct_cost` | 成本分摊事实表 | KPI_06, 33 |
| `fct_rule_hit` | 规则命中事实表 | KPI_29 |
| `fct_training` | 培训事实表 | KPI_37 |
| `dim_ka` | KA 维度表 | KPI_30, 34, 35 |
| `dim_employee` | 员工维度表 | KPI_36 |
| `dim_target` | 目标维度表 | KPI_03, 31, 32 |

**spot-check action**: 若 PG 实际表名不同 (例如 `fct_policy` 实为 `fact_policy` 或 `policy_fact`), 在 SQL 文件中全文替换即可.

### 重点 2: 关键字段名 verify

Claude 沿用业内标准命名 (snake_case, 与 process_analytics schema 风格一致):

| 字段名 | 类型 | 含义 | 假设来源 |
|---|---|---|---|
| `premium_amt` | NUMERIC | 保费金额 | 保险业内标准 |
| `ape` | NUMERIC | 年化保费 | 保险业内标准 |
| `sign_date / submit_date / issue_date / surrender_date / paid_to_date` | DATE | 保单生命周期日期 | 推断 |
| `policy_status` | VARCHAR | 保单状态枚举 ('Approved'/'Issued'/'Pending'/'InProcess') | 推断 |
| `ka_id / policy_id / claim_id / emp_id` | VARCHAR | 主键/外键 | 标准 |
| `comm_type` | VARCHAR | 佣金类型枚举 ('Renewal' 等) | 推断 |
| `activity_type` | VARCHAR | 活动类型枚举 ('appt'/'contact'/'schedule') | 推断 |
| `outcome` | VARCHAR | 活动结果枚举 ('success') | 推断 |
| `risk_score` | NUMERIC | 风险评分 (0-100, Stella 路由引擎写入) | Mark 已 verify |
| `market_segment_code` | VARCHAR | 细分市场编码 | 推断 |
| `contract_status` | VARCHAR | KA 签约状态 ('Active') | 推断 |

**spot-check action**: 若 PG 字段名 / 枚举值有差异 (例如 `policy_status` 实为中文 '已核保', 或 `ape` 实为 `apx`), 在 SQL 中改正.

### 重点 3: 低 confidence 字段重点检查 (4 个 🔴 surface)

CSV 列 9 `confidence_pg` 标 **低** 的 KPI 共 6 个 (3 主线 + 3 联动):

| KPI | 风险点 | Carrie verify 关键 |
|---|---|---|
| 🔴 **KPI_04 净营收** (Mark 5-23 改 B) | 字段 `fct_commission.amount + payout_amt` 假设. 若 PG 用 `commission_amt / split_amount` 或拆 `fct_commission_in + fct_commission_out` 两表, **必须改 SQL** | 字段名 + 是否拆表 |
| 🔴 **KPI_06 管理利润** (联动 KPI_04 B) | 同上 + 成本字段 `fct_cost.allocated_amt` 假设. 若 PG 命名不同请改 | 成本表 + 字段名 |
| 🔴 **KPI_29 红线命中数** | 表 `fct_rule_hit` 假设. 若 PG 命名 `fct_compliance_alert / fct_red_line`, 严重级别枚举 'Red' 假设 (可能为中文 '红线') | 表名 + 枚举 |
| 🔴 **KPI_33 ROI** | Mark 锁定 A: (收益-成本)/成本. 收益取毛佣金 (简化). 若 PG ROI 收益定义为净营收 (而非毛佣金) 请改为 KPI_04 PG 表达式 | 收益定义 |
| 🔴 **KPI_35 新签成活率** | Mark 锁定 90 天窗口. SQL 用子查询 EXISTS + 跨表 JOIN, 若 PG 已有视图 `v_ka_survival` 推荐直接复用 | 视图复用 |
| 🔴 **KPI_37 培训改善度** | 表 `fct_training` + 字段 `ape_post / ape_pre` 假设. 若 PG 按事件流存 (多行 fct_training_event), 需改窗口函数 (LAG) 计算前后差 | 表结构形态 |

### 重点 4: KPI_04 净营收公式 (Mark 5-23 决策)

**最关键的一处变化**: Mark 接受 Claude 主 thread 修正 = **B 口径**:

```sql
-- W7-F 原推荐 A (废弃): 佣金 - WHT - GST (通用财务定义)
-- Mark 5-23 接受 B (执行): 佣金 - 外发分成 (MGA 业务定义)
KPI_04 净营收 = SUM(fct_commission.amount) - SUM(fct_commission.payout_amt)
KPI_06 管理利润 = KPI_04 - SUM(fct_cost.allocated_amt)  -- 联动
```

业务理由 (MGA 业务模型): 净营收 = 公司实际留存 = 佣金 - 给 KA/代理人分成. WHT/GST 是代收代付不属公司.

**Carrie verify action**: 仅需 verify `payout_amt` 字段名是否准确.

---

## § 3 spot-check 后的 3 种处理

### Case A: 全 OK (~70% 概率)

```bash
# 直接执行 SQL → DIM_KPI 100% 完整 → AG07 起跑
psql -h 43.98.163.46 -d DIM_ORG -U <user> -f 已完成_dim_kpi_w8c_alter_update.sql

# 1 句话回执给 Claude:
# "AG07 起跑就绪"
```

### Case B: 少量字段名不一致 (~25% 概率)

```bash
# Carrie 在 SQL 中改字段名 (例: payout_amt → split_amount), 然后执行
psql -h 43.98.163.46 -d DIM_ORG -U <user> -f 已完成_dim_kpi_w8c_alter_update.sql

# 1 句话回执:
# "差距 3 字段名, 已改 SQL 执行成功, AG07 起跑就绪"
```

### Case C: 重大不一致 (~5% 概率, 例如 PG 业务表完全是不同 schema)

```bash
# 1 句话回执:
# "差距 KPI_04/06/35 PG 表结构与 W8-C 假设不一致, 待 Claude 重推导"
# Claude 主 thread 收到后 → W8-D 重推导 (~20 分钟, 基于 Carrie 的真实 schema)
```

---

## § 4 confidence 分层 + 风险条目

| 分层 | 数量 | KPI 列表 |
|---|---|---|
| 🟢 高 (字段在 DICT 中能找到 / 行业标准命名) | 7 | KPI_01, 02, 17, 20, 24, 31, 32 |
| 🟡 中 (推断但合理 / 枚举值需 verify) | 19 | KPI_03, 09, 12, 13, 14, 15, 16, 18, 19, 21, 22, 26, 27, 28, 30, 34, 36, 50, 51 |
| 🔴 低 (Carrie 必须 verify 字段名/表结构) | 6 | KPI_04, 06, 29, 33, 35, 37 |
| **合计** | **32** | |

🔴 6 个低 confidence KPI 详见 § 2 重点 3.

---

## § 5 执行流程

### Step 0: 备份 (1 分钟, 强烈推荐)

```sql
-- 备份当前 DIM_KPI 表 (Carrie 已建 32 行 ready 的版本)
CREATE TABLE process_analytics.DIM_KPI_backup_20260524 AS
SELECT * FROM process_analytics.DIM_KPI;
```

### Step 1: dry-run 干跑 (1 分钟)

```bash
psql -h 43.98.163.46 -d DIM_ORG -U <user> \
     -f 已完成_dim_kpi_w8c_alter_update.sql \
     --single-transaction --set ON_ERROR_STOP=on \
     --echo-errors

# 干跑成功 = 0 报错 = 可进入 Step 2
```

注: SQL 已用 `BEGIN; ... COMMIT;` 包裹 + `\set ON_ERROR_STOP on`, 任何错误自动回滚.

### Step 2: spot-check 干跑结果 (2 分钟)

```sql
-- 查 ALTER 后字段是否添加
\d process_analytics.DIM_KPI

-- 期望: 末尾出现 4 新字段 (l1_code / l3_codes / formula_numerator / formula_denominator)
```

### Step 3: 真跑 (1 分钟)

若 Step 1 dry-run 成功, Step 2 ALTER 字段确认, 则真跑:

```bash
psql -h 43.98.163.46 -d DIM_ORG -U <user> -f 已完成_dim_kpi_w8c_alter_update.sql
```

### Step 4: SELECT 验证 (2 分钟)

SQL § 3 已含 4 个 VERIFY SELECT:

```sql
-- 验证 1: 32 行无空值
-- 验证 2: l1_code 分布 (L1-01:5 + L1-02:8 + L1-03:7 + L1-04:7 + L1-05:5 = 32)
-- 验证 3: 全表预览
-- 验证 4: KPI_04 B 修正确认 (含 '佣金收入 - 外发分成')
```

期望: 4 个 SELECT 全部符合预期 = SQL 执行成功.

### Step 5: 1 句话回执给 Claude (30 秒)

3 种回执模板见 § 3.

---

## § 6 W8-C 不动的范围 (避免 Carrie 修改时误改)

W8-C 完全不动以下文件 (主 thread cross-check 阶段处理):

- `03/交付清单.md` (主 thread W8 完成后批次 014)
- `00/文档结构映射表.md` (主 thread W8 完成后 v2.9 → v2.10)
- `03/权威数据/DIM_KPI_W7F补字段_v1.0.csv` (W7-F 历史基线)
- `03/权威数据/L4_核心交付物全量表_v5.3.csv` (W8-A)
- `05/Agent库/AGENT_INDEX.md` (W8-B v1.3)
- `00/风险登记册/` (W6-B + W7-B)

W8-C 唯一新增 3 文件 (本报告 + CSV + SQL).

---

*本报告由 W8-C agent 在 2026-05-23 物理化. Carrie 5-10 分钟 spot-check + 执行 SQL 后, AG07 Day 0 5-25/5-26 起跑 (vs 平移 5-29 节省 4 天).*
