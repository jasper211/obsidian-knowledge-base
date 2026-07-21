---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/校验与上下文/校验报告_数据库层_TASK-EEP-004B.md
extracted_at: 2026-07-20T23:01:42
---

# agent_type与m2_tier完全相同

dim_agent_capability表中agent_type与m2_tier字段数值完全一致（Aug 108, Auto 77, Human 39, Hybrid 176），但infer_tier分布存在系统性差异（Aug 108→196, Auto 77→111, Hybrid 176→54, Human 39不变）。需评估哪个字段为权威来源，m2_tier是Mark确认值还是系统推导值，infer_tier的推导逻辑是否有依据文档。

## 关联概念

- [[dim_agent_capability]]
- [[agent_type]]
- [[m2_tier]]
- [[infer_tier]]
