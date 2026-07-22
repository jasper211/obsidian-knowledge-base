---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/12_任务看板_Task_Dashboard/web/node_modules/queue-microtask/README.md
authority_layer: 02_草稿
confidence: HIGH
confidence_reason: 原文明确列出回退方案和环境条件
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
status: 生效
extracted_at: 2026-07-22T03:13:13
---

# queue-microtask回退策略

该 shim 在现代 JS 引擎使用原生 queueMicrotask，在 Node.js 10 及更早和旧浏览器中回退到 Promise.resolve().then(fn)，以确保性能最优。

## 关联概念

- [[queueMicrotask定义]]
- [[Promise.resolve]]
