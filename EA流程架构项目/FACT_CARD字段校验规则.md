---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 03_发布成果-交付物/治理规范/DICT_流程数据库数据字典_V1_架构知识库.md
authority_layer: 03_已锁定
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-记录日期校验
extracted_at: 2026-07-16T11:45:22
---

# FACT_CARD字段校验规则

FACT_CARD各字段有严格校验规则，例如：record_date不能早于2026-01-01且不能晚于当前日期+1天；duration_hours必须>0且建议上限2000小时；rework_count>=3时自动触发预警标记等。

## 关联概念

- [[FACT_CARD事实表]]
