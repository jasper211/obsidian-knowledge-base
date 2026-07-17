---
type: concept_atom
concept_type: 背景说明
project: EA流程架构项目
source: 01_原始材料-外部导入/M-02_架构全景/02_架构全景_C_数据架构_C1_数据字典_50张表关联逻辑分析报告.docx
authority_layer: 01_原始
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-意向到签约平均周期
extracted_at: 2026-07-16T12:57:45
---

# KPI生成链路

贯穿五层的核心数据链路之一，描述管理层在KPI看板上看到的数字如何从原始数据计算而来。环节：数据采集（FACT_POLICY等）→维度关联→目标对齐→漏斗计算→业绩聚合→佣金聚合→目标追踪→报表输出。

## 关联概念

- [[FACT_POLICY]]
- [[FACT_SALES_AGG]]
- [[FACT_COMMISSION_AGG]]
- [[业绩报表]]
