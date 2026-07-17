---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 01_原始材料-外部导入/M-88_mark日常输出/Mark_第三轮决策回复_M4-W10_20260529.md
authority_layer: 01_原始
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-29
entity_type: 待聚类
entity_ref: （无）
extracted_at: 2026-07-16T12:46:45
---

# 时间粒度仅month

事实表时间粒度只做 month，quarter 和 year 可在消费侧用 DATE_TRUNC 实时聚合，无需预物化，避免视图数量膨胀。

## 关联概念

（暂无）
