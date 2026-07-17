---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/任务状态/致Terresa_fact_card字典澄清_M4-W10_20260528.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-28
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-真KPI目标待定
extracted_at: 2026-07-16T12:07:23
---

# dim_kpi重构后kpi_key派生规则

实测dim_kpi已从旧体系（33行）重构为新体系（32行企业级KPI），但字典V1.0仍描述旧体系。需要确认新32行KPI是否稳定可用，以及关联规则（按vs_code、strategy_level还是l3_code）。Mark D1说Phase 1 kpi_key全NULL，与新体系是否矛盾需评估。

## 关联概念

- [[dim_kpi表]]
- [[kpi_key]]
- [[fact_card表]]
