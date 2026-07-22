---
type: concept_atom
concept_type: 经验教训
project: EA流程架构项目
source: 01_原始材料-外部导入/M-02_架构全景/02_架构全景_C_数据架构_C1_数据字典_50张表关联逻辑分析报告.docx
authority_layer: 01_原始
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: KPI
entity_ref: KPI_18
extracted_at: 2026-07-16T12:57:45
status: 待裁定
conflict_group: KPI_18
---

# FACT_POLICY最高风险

FACT_POLICY（保单事实表）是P1核心表，KPI_18权重57.1%，但SOP尚未制作，构成算薪体系中最大的数字可信度风险。需优先完成其SOP。

## 关联概念

- [[FACT_POLICY]]
- [[SOP]]
- [[P1节点]]

## ⚠️ 待裁定：entity_ref矛盾（KPI_18）

与同组原子存在冲突：[[中台业务交付SOP缺口]]、[[154_KPI两套目录编号撞车]]

冲突说明：第一条原子说KPI_18=57.1%且对应FCT_POLICY，第二条原子说KPI_18在EA为批核率，在CQ为对账时效，两者对KPI_18的定义不一致。

（标记时间：2026-07-21T20:56:43）
