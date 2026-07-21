---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/校验与上下文/数据溯源_任务包_溯源校验_v3.md
extracted_at: 2026-07-20T22:17:07
---

# dim_value_stream分层抽样

dim_value_stream表采用分层抽样，每个VS（VS-1到VS-5）各取20行，共100行。校验字段vs_code、stage_code、activity_code、stage_name需与S3完全一致，且activity_code必须存在于dim_l3。

## 关联概念

- [[旧概念分组码]]
