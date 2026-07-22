---
type: concept_atom
concept_type: 经验教训
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/12_任务看板_Task_Dashboard/web/node_modules/queue-microtask/README.md
authority_layer: 02_草稿
confidence: HIGH
confidence_reason: 原文明确陈述 setTimeout 的问题和性能影响
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
status: 生效
extracted_at: 2026-07-22T03:13:13
---

# 避免setTimeout微任务

使用 setTimeout(fn, 0) 作为微任务回退不可取，现代浏览器节流定时器导致至少4ms延迟，后台标签页更严重，大量调用会严重降低性能。

## 关联概念

- [[queueMicrotask定义]]
- [[微任务]]
