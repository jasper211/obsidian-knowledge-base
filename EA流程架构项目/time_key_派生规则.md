---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/任务状态/Terresa_回函_fact_card字典澄清_M4-W10_20260529_修正版.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-29
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-time_key派生口径
extracted_at: 2026-07-16T12:13:49
---

# time_key 派生规则

fact_card 的 time_key 按以下优先级派生：1) 使用 start_date 转换；2) 若 start_date 缺失，使用 record_date（自动取当前日期）；3) 若两者都不存在则不允许，因为 time_key 隐含 NOT NULL。Phase 1 批量回填时 record_date 作为 fallback 是安全的。

## 关联概念

- [[fact_card]]
- [[dim_time]]
