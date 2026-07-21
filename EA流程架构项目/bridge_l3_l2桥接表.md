---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 02_过程成果-工作产出/数据库/dim_process_l2_update_report.md
extracted_at: 2026-07-21T00:54:42
---

# bridge_l3_l2桥接表

bridge_l3_l2桥接表用于存储L3与L2之间的多对多映射关系。当L3对应多个L2时，dim_process中的l2_code/l2_name保持为空，映射关系写入此桥接表，并在source_notes中标注异常。

## 关联概念

- [[一对多L3]]
- [[L3到L2映射关系]]
