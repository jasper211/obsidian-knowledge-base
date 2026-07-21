---
type: concept_atom
concept_type: 经验教训
project: EA流程架构项目
source: 02_过程成果-工作产出/数据库/compare_local_db_report.txt
extracted_at: 2026-07-21T00:56:09
---

# dim_vs文件多余记录

dim_vs表文件中存在24条记录（如VS-1/S8等）未在数据库中出现，且34条共同记录的stage_name字段不一致（如VS-1/S2文件为'授权与合同'，库为'授权与合作框架'）。

## 关联概念

- [[bridge_l3_vs_stage数据不一致]]
- [[数据同步检查]]
