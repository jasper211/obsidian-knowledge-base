---
type: concept_atom
concept_type: 定义
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/12_任务看板_Task_Dashboard/web/node_modules/queue-microtask/README.md
authority_layer: 02_草稿
confidence: HIGH
confidence_reason: 原文直接明确给出定义和等价关系
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
status: 生效
extracted_at: 2026-07-22T03:13:13
---

# queueMicrotask定义

queueMicrotask 是 WHATWG 标准 API，用于将微任务排队，在当前任务完成后、控制权返回事件循环前执行，等价于 Promise.resolve().then(fn)。

## 关联概念

- [[微任务]]
- [[Promise.resolve]]
