---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 08_任务与跟进/AI上下文/Mark任务协同规则_v0_5_20260603.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-06-03
entity_type: 待聚类
entity_ref: （无）
extracted_at: 2026-07-16T11:52:15
---

# Phase F回执归档与闭环判定

触发条件为任务负责人完成验收。任务负责人按框架产出回执MD存入Partner_DB/任务状态/，Mark的AI读取。闭环判定：Boss_DB无新反馈则标注“完成-等待新任务”；有反馈则重新进入Phase A；有新任务MD则旧任务关闭。

## 关联概念

- [[六阶段协同闭环]]
- [[任务回执MD框架]]
