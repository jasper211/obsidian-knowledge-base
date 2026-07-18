---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 08_任务与跟进/任务状态/Terresa_回函_fact_card字典澄清_M4-W10_20260529.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-29
entity_type: 非正式主题
entity_ref: time_key派生口径_time_key派生口径
extracted_at: 2026-07-16T13:52:26
---

# time_key派生口径

time_key按优先级fallback：1. start_date；2. start_date缺失则取record_date；3. 都不存在则不允许（FC-006校验隐含NOT NULL）。Phase 1批量回填用record_date作为fallback安全，因dim_time已覆盖2024-2027。

## 关联概念

- [[time_key]]
- [[dim_time]]
- [[fact_card]]

## 所属枢纽

- [[time_key派生口径]]

## 关联原子（同话题聚类）

- [[time_key_派生规则]]
- [[time_key派生口径]]
- [[time_key派生口径未定]]
