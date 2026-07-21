---
type: concept_atom
concept_type: 经验教训
project: EA流程架构项目
source: 02_过程成果-工作产出/数据库/compare_local_db_report.txt
extracted_at: 2026-07-21T00:56:13
---

# bridge_l3_vs_stage数据不一致

bridge_l3_vs_stage表文件与数据库记录差异大：文件有29条独有记录（如L3-ACTV/VS-5/S5），数据库有51条独有记录（如L3-BSRV/VS-2/S5），共同仅14条，表明L3与VS阶段的映射关系在文件与数据库间严重不同步。

## 关联概念

- [[dim_vs文件多余记录]]
- [[数据同步检查]]
