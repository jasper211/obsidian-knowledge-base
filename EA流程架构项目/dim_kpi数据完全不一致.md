---
type: concept_atom
concept_type: 经验教训
project: EA流程架构项目
source: 02_过程成果-工作产出/数据库/compare_local_db_report.txt
extracted_at: 2026-07-21T00:56:04
---

# dim_kpi数据完全不一致

dim_kpi表文件与数据库无共同记录：文件有43条（kpi_code为'内部-PI-14'等），数据库有1条（kpi_code为NULL），且文件中的kpi_code与数据库中的kpi_code完全不同，表明两套数据源使用了不同的编码体系。

## 关联概念

- [[数据同步检查]]
