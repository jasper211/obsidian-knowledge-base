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
entity_ref: 拆表操作
extracted_at: 2026-07-16T12:46:44
---

# FCT_PRODUCT拆两张

FCT_PRODUCT 表拆分为 FCT_PRODUCT_id 和 FCT_PRODUCT_sku 两张视图，因为 product_id 和 sku 的业务粒度不同，拆开可降低消费侧复杂度。

## 关联概念

- [[FCT_CHANNEL拆两张]]

## 所属枢纽

- [[拆表操作]]
