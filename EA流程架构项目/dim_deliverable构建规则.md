---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/L3流程库/dim_delieverable_构建说明.md
extracted_at: 2026-07-20T21:19:12
---

# dim_deliverable构建规则

构建dim_deliverable维度表时，同一l4_code出现多次的去重规则：优先保留版本号更高的蓝图（如V1.1 > V1.0），优先保留主L3而非子流程L3（如L3-IAC优先于L3-IAC-AUTH），优先保留有Agent分级信息的记录。

## 关联概念

- [[dim_deliverable]]
- [[L4编码]]
- [[流程蓝图]]
