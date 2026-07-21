---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/校验与上下文/数据整合_任务包_Qoder_DB整合_v1.md
extracted_at: 2026-07-20T22:09:27
---

# confirmation_status保留规则

写入数据库时，confirmation_status保持源数据中的值；若源数据无此字段则默认'draft'；不得修改已有confirmation_status=mark_locked的记录。

## 关联概念

- [[dim_l3]]
- [[dim_agent_capability]]
- [[dim_kpi]]
- [[bridge_job_kpi]]
