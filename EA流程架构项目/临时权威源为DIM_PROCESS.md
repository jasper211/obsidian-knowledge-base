---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 08_任务与跟进/任务状态/EA业务能力SSOT确认回执_v1.0.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
extracted_at: 2026-07-16T12:15:46
---

# 临时权威源为DIM_PROCESS

IE可直接从DIM_PROCESS中取数，使用l1_code（5条L1价值链）作为临时权威源，无需标记provisional。SQL查询：SELECT DISTINCT l1_code, l1_name FROM process_analytics.DIM_PROCESS WHERE is_current = true ORDER BY l1_code;

## 关联概念

- [[L1价值链]]
- [[DIM_PROCESS]]
