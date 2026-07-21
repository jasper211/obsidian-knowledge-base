---
type: concept_atom
concept_type: 经验教训
project: EA流程架构项目
source: 02_过程成果-工作产出/数据库/compare_local_db_report.txt
extracted_at: 2026-07-21T00:55:59
---

# dim_vn_l4_bridge文件多余记录

dim_vn_l4_bridge表文件中存在5条记录（如VN-HRD-01/L4-HRD-01等）未在数据库中出现，且13条共同记录的l3_code字段不一致（如VN-INS-02的l3_code文件为L3-IAC-Neg，库为L3-IAC）。

## 关联概念

- [[dim_vn文件多余记录]]
- [[数据同步检查]]
