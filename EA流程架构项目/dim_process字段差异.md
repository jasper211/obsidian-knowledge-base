---
type: concept_atom
concept_type: 经验教训
project: EA流程架构项目
source: 02_过程成果-工作产出/数据库/compare_local_db_report.txt
extracted_at: 2026-07-21T00:55:50
---

# dim_process字段差异

dim_process表中文件与数据库存在285条字段差异，主要涉及l4_deliverable和agent_score_total字段，如L4-ASD-01的交付物名称不一致、agent_score_total类型差异（文件为整数，库为浮点数）。

## 关联概念

- [[dim_deliverable一致性]]
- [[数据同步检查]]
