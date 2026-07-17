---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 01_原始材料-外部导入/M-88_mark日常输出/03_老板输出_增量_20260428.md
authority_layer: 01_原始
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-04-28
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-API优先
extracted_at: 2026-07-16T12:49:47
---

# API优先集成

experience-engine 采用 REST + JSON API 协议，业务项目通过 API 调用而非文件复制来消费经验。好处：经验库版本升级不影响业务项目，多个项目共享同一份经验，跨保司迁移时新项目直接调用 API。

## 关联概念

- [[经验机构化系统]]
- [[insurance-analytics-v2集成]]
