---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/校验与上下文/上下文_KPI差距分析_对标锚点v0.4_v1.md
extracted_at: 2026-07-20T22:13:19
---

# S7 SSOT与治理

KPI必须存入活跃库（dim_kpi/dim_job/桥表）作为唯一权威源，并晋升03锁定。现状KPI散落6活跃+8归档+5 SQL，文档标"已入库"与事实矛盾，需建表入库并降级旧副本。

## 关联概念

- [[P0差距]]
- [[单KPI定义卡]]
