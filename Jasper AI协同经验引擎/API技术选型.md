---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/12_任务看板_Task_Dashboard/README.md
authority_layer: 02_草稿
confidence: HIGH
confidence_reason: 原文明确给出了技术选型及理由。
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
status: 生效
extracted_at: 2026-07-22T03:12:45
---

# API技术选型

PTA看板API使用Python标准库http.server实现，不引入FastAPI或Flask，以保持与项目一贯的依赖习惯一致。

## 关联概念

- [[项目依赖习惯]]
