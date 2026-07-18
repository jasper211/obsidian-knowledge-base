---
type: concept_atom
concept_type: 经验教训
project: EA流程架构项目
source: 08_任务与跟进/任务状态/致Terresa_fact_card字典澄清_M4-W10_20260528.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-28
entity_type: 非正式主题
entity_ref: 时间维度表问题
extracted_at: 2026-07-16T12:07:20
---

# dim_time 0行阻塞

fact_card 的 time_key 强制外键引用 dim_time，但实测 dim_time 表为空（0行），导致 fact_card 无法插入任何数据。字典声明该表应由脚本生成约1461行（2024-01-01至2027-12-31），但脚本未就绪。这是 Phase 1 灌数的硬阻塞，需优先解决。

## 关联概念

- [[dim_time表]]
- [[fact_card表]]
- [[外键约束]]

## 所属枢纽

- [[时间维度表问题]]
