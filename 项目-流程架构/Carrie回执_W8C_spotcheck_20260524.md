---
文件类型: Carrie spot-check 回执（最终版）
产出日期: 2026-05-24
回执方向: Carrie → 主 thread Claude
关联文件: 06_Scripts库/草稿/已完成_dim_kpi_w8c_alter_update.sql
graph_layer: "08_任务与跟进"
graph_tag: 任务
graph_subdir: "任务状态"
tags: [任务]
---

## 🧭 导航
⬆️ [[08_任务与跟进]] · ⬆️ [[任务状态]] · 🏠 [[流程架构项目MOC]]

---

# Carrie W8-C Spot-Check 回执 (2026-05-24) — 最终版

## 结论

[差距 FCT_表缺失，DIM_KPI 本身已 ready] DIM_KPI 32/32 行补字段完成，4 字段全填满，验证通过。
FCT_ 事实表在 PG 中均不存在（已确认非 schema 问题），AG07 实际出数依赖 ETL 建表，待主 thread 确认 ETA。

---

## Step 0 备份

✅ `process_analytics.DIM_KPI_backup_20260524` 已建立

---

## Step 2 SQL 执行结果

✅ ALTER TABLE + 32 × UPDATE 执行成功，0 报错

---

## Step 4 验证结果

### 验证 1：32 行全部更新，4 字段无空值

```
 total_kpi | l1_filled | l3_filled | num_filled | den_filled
-----------+-----------+-----------+------------+------------
        32 |        32 |        32 |         32 |         32
```
✅ 全部符合预期

### 验证 2：l1_code 分布

```
 l1_code | cnt
---------+-----
 L1-01   |   5
 L1-02   |   8
 L1-03   |   7
 L1-04   |   7
 L1-05   |   5
```
✅ 全部符合预期（合计 32）

### 验证 4：KPI_04 B 口径确认

```
 kpi_code | formula_numerator
----------+-------------------------------------------------------------------------------------------
 KPI_04   | 期内佣金收入 - 外发分成 SUM(amount) - SUM(payout_to_carrier_or_ka_amt) [Mark 5-23 B 口径]
```
✅ B 口径确认

---

## 表名差异修正记录（已写入 formula 文本）

| W8-C 假设表名 | PG 数据字典实际表名 |
|---|---|
| `fct_commission` | `FCT_COMMISSION` |
| `fct_cost` | `FCT_ALLOCATED_COST` |
| `fct_rule_hit` | `FCT_RISK` |
| `fct_complaint` / `fct_audit` | `FCT_SERVICE_RECORD` |
| `fct_claim` | `FCT_CLAIMS` |
| `fct_activity` | `FCT_SALES_ACTIVITY` |
| `fct_training` | ❌ 数据字典无此表，KPI_37 改用 FCT_POLICY |

---

## 阻塞项：FCT_ 事实表不存在

- PG 所有 schema 均无 FCT_ 开头事实表（已全面确认）
- **DIM_KPI 补字段本身已 100% 完成**
- **AG07 实际计算 KPI 时需要 FCT_ 表，目前无法出数**

待主 thread 确认：FCT_ 事实表 ETL 建表计划 ETA？

---

*Carrie 5-24 最终回执. DIM_KPI 补字段 ✅ 完成. FCT_ 表缺失为独立阻塞项，待主 thread 协调.*

