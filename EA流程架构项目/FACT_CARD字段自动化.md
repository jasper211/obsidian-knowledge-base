---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/AI上下文/上下文_METHOD_流程架构落地工作方法论_V1.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-FACT_CARD字段数据来源
extracted_at: 2026-07-16T11:50:23
---

# FACT_CARD字段自动化

FACT_CARD各字段的自动化填充来源：fact_id/record_date等系统生成（100%），process_key/l4_code等来自DIM_PROCESS lookup（100%），time_key/end_date来自触发事件时间戳（100%），execution_status默认'完成'，sla_hours_actual来自DIM_PROCESS快照，start_date/duration_hours有源字段时填充，org_key依赖DIM_ORG映射，rework_count/handoff_count默认0，error_flag/escalation_flag默认FALSE需人工确认，agent_assist_flag当前全FALSE。

## 关联概念

- [[路径B自动写入FACT_CARD]]
- [[CONFIG_PROCESS_EVENT_TRIGGER]]
