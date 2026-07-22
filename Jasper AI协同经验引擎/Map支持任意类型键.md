---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/12_任务看板_Task_Dashboard/web/node_modules/@alloc/quick-lru/readme.md
authority_layer: 02_草稿
confidence: HIGH
confidence_reason: 文档明确陈述设计决策和理由。
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
status: 生效
extracted_at: 2026-07-22T03:14:40
---

# Map支持任意类型键

quick-lru 受 hashlru 算法启发，但改用 Map 实现，以支持任意类型的键（不只是字符串），并且值可以为 undefined。

## 关联概念

- [[LRU缓存]]
- [[hashlru]]
- [[Map数据结构]]
