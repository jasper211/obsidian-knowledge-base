---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 02_过程成果-工作产出/校验与上下文/数据整合_修复包_v3.md
extracted_at: 2026-07-20T22:50:38
---

# FIX-02删除dim_kpi

dim_kpi和bridge_job_kpi表应被删除（DROP TABLE），因为KPI不纳入T1数据底座。删除后数据库应只剩4张核心表：dim_agent_capability、dim_l3、dim_l4_activity、dim_value_stream。

## 关联概念

- [[数据底座范围]]
