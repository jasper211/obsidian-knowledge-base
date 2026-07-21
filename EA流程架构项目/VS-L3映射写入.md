---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/价值流建模/写入日志_VS_L3写入日志.txt
extracted_at: 2026-07-21T00:52:42
---

# VS-L3映射写入

将CSV中的VS-L3映射关系写入dim_value_stream和fact_activity表，写入前需跳过L3-ISD孤立记录，并新增vs_l3_mapping、stage_l3_mapping、l3_confidence等字段。

## 关联概念

- [[dim_value_stream]]
- [[fact_activity]]
- [[L3-ISD孤立记录]]
