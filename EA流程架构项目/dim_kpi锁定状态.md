---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 02_过程成果-工作产出/KPI穿透/KPI数据全链路更新同步_SOP_v1.md
extracted_at: 2026-07-20T21:55:53
---

# dim_kpi锁定状态

dim_kpi的authority_status字段有两个状态：'LOCKED-部分字段待补'和'LOCKED'。回填Mark裁定后，更新为'LOCKED'并清空pending_decision。

## 关联概念

- [[dim_kpi]]
- [[Mark裁定清单]]
