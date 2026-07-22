---
type: concept_atom
concept_type: 背景说明
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/12_任务看板_Task_Dashboard/web/node_modules/queue-microtask/README.md
authority_layer: 02_草稿
confidence: HIGH
confidence_reason: 原文明确说明等价性和标准化差异
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
status: 生效
extracted_at: 2026-07-22T03:13:13
---

# queueMicrotask与nextTick

在 Node.js 中，queueMicrotask 与 process.nextTick 基本等价，只有细微差别；queueMicrotask 是标准化版本，可在浏览器中运行，无需 shim process。

## 关联概念

- [[queueMicrotask定义]]
- [[process.nextTick]]
