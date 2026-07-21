---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/校验与上下文/数据溯源_任务包_溯源校验_v3.md
extracted_at: 2026-07-20T22:17:13
---

# dim_l4_activity分组抽样

dim_l4_activity表按l3_code分组，每组取3条，约240条样本。校验字段l4_code、l4_name、l3_code需与S4完全一致，且l3_code必须存在于dim_l3。

## 关联概念

- [[dim_l3]]
