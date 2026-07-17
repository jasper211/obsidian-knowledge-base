---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 01_原始材料-外部导入/M-88_mark日常输出/Mark_第三轮决策回复_M4-W10_20260529.md
authority_layer: 01_原始
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-29
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-FCT_PRODUCT拆两张
extracted_at: 2026-07-16T12:46:44
---

# FCT_CHANNEL拆两张

FCT_CHANNEL 表拆分为 FCT_CHANNEL_partner 和 FCT_CHANNEL_ka 两张视图，因为 partner 和 ka 的主键、JOIN 路径、字段集不同，合并会增加消费侧查询复杂度。拆开零成本，消费侧无需 WHERE discriminator。

## 关联概念

- [[FCT_PRODUCT拆两张]]
