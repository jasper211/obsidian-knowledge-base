---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/项目规划/数据字典_流程数据库数据字典_V1.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
extracted_at: 2026-07-16T12:34:47
---

# Agent介入标记约束

FACT_CARD 中 agentifiability='Human' 时 agent_assist_flag 必须为 FALSE；agentifiability='Auto' 且活动已完成时 agent_assist_flag 理论上须为 TRUE（预警不阻断）。

## 关联概念

- [[FACT_CARD]]
- [[DIM_PROCESS]]
