---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/任务状态/T1_v2_staging_build_report.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-冲突类别：D1概览存在但验证矩阵缺失
extracted_at: 2026-07-16T12:06:38
---

# Include rows with source conflicts

即使 canonical_status=include，部分行仍携带冲突标记（如 missing_from_T1_v1、T1_raw_id_normalized），这些冲突需要在 promotion 前解决。冲突行列表见报告中的表格。

## 关联概念

- [[Promotion gate]]
- [[Synthetic rows requiring completion]]
