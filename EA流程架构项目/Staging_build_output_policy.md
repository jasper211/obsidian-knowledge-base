---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/任务状态/T1_v2_staging_build_report.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
extracted_at: 2026-07-16T12:06:38
---

# Staging build output policy

T1 v2 staging build 不直接覆盖生产数据，而是根据 EA_Canonical_Value_Node_Registry_v1.csv 中的 canonical_status 字段决定输出：include 行进入 T1_nodes_全域_v2_staging.csv，hold 行仅进入 EA_Value_Node_Hold_Decision_Table_v1.csv。

## 关联概念

- [[Canonical status]]
- [[Hold decision table]]
