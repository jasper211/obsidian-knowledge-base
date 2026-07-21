---
type: concept_atom
concept_type: 背景说明
project: EA流程架构项目
source: 02_过程成果-工作产出/校验与上下文/上下文_三链合并_链ABC_v1.0_20260513.md
extracted_at: 2026-07-20T23:07:24
---

# EA数据底座现状

活跃数据库为ea_knowledge_base_t1.db，包含4张核心表：dim_l3（82个L3流程编码）、dim_value_stream（价值流全量表V3，360行）、dim_l4_activity（L3→L4映射，400行）、dim_agent_capability（Agent能力维度，400行）。验收状态为TASK-EEP-007全部通过（13个子项0失败）。Agent化分布基线：Hybrid 44.0%、Aug 27.0%、Auto 19.3%、Human 9.8%。

## 关联概念

- [[dim_l3]]
- [[dim_value_stream]]
- [[dim_l4_activity]]
- [[dim_agent_capability]]
