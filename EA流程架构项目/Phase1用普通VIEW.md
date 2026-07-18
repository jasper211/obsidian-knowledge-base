---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 01_原始材料-外部导入/M-88_mark日常输出/Mark_第三轮决策回复_M4-W10_20260529.md
authority_layer: 01_原始
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-29
entity_type: 非正式主题
entity_ref: 项目阶段与交付
extracted_at: 2026-07-16T12:46:44
---

# Phase1用普通VIEW

P1 四张表行量小于 3,000，实时 JOIN 毫秒级，因此 Phase 1 使用普通 VIEW 而非 MATERIALIZED VIEW，避免引入刷新延迟和运维开销。CP2 后行量暴增再评估升级。

## 关联概念

（暂无）

## 所属枢纽

- [[项目阶段与交付]]
