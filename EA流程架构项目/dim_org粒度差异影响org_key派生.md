---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/任务状态/致Terresa_fact_card字典澄清_M4-W10_20260528.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-28
entity_type: 非正式主题
entity_ref: org_key处理
extracted_at: 2026-07-16T12:07:22
---

# dim_org粒度差异影响org_key派生

字典声明dim_org粒度为岗位级（每人一行），但实测仅8行（岗位族级）。派生fact_card.org_key时，需确定如何将保单的partner_code映射到org_key：按L4所属族取8选1，或Phase 1全部NULL等待GAP-01完成。

## 关联概念

- [[dim_org表]]
- [[org_key]]
- [[fact_card表]]

## 所属枢纽

- [[org_key处理]]
