---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 08_任务与跟进/任务状态/EA_to_EEIE_Staging_Data_Contract_v1.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-Shared_audit_records
extracted_at: 2026-07-16T12:09:13
---

# Shared audit records

The shared audit table eeie_ingest_audit preserves source file, version, update date, registry evidence, decision owner, and promotion state. Its primary key is value_node_id + source_version.

## 关联概念

- [[Candidate staging tables]]
- [[EE vs IE boundary]]
