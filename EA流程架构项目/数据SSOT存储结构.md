---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/校验与上下文/上下文_KPI优秀体系锚点标准_v0.4.md
extracted_at: 2026-07-20T23:39:48
---

# 数据SSOT存储结构

唯一权威KPI数据存储包括：dim_kpi（20字段）、dim_job（岗位属性）、bridge_kpi_l3、bridge_job_kpi。要求一处存储、副本只读引用不复制、版本+Owner+月度评审+变更登记、文档与库一致。可算性字段禁止一律标"是"。

## 关联概念

- [[20字段强制Schema]]
- [[桥表]]
