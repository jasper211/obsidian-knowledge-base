---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/12_任务看板_Task_Dashboard/web/node_modules/queue-microtask/README.md
authority_layer: 02_草稿
confidence: HIGH
confidence_reason: 原文明确给出包大小比较和适用场景
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
status: 生效
extracted_at: 2026-07-22T03:13:13
---

# 选择queue-microtask原因

当优先考虑小 JS 包体积而非旧浏览器最优性能时，可选择 queue-microtask，它比 immediate 小四倍，比 asap 小两倍，且在支持 Promise 的环境获得最优性能。

## 关联概念

- [[queueMicrotask定义]]
- [[immediate库]]
- [[asap库]]
