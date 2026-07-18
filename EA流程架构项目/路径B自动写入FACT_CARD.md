---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/AI上下文/上下文_METHOD_流程架构落地工作方法论_V1.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 非正式主题
entity_ref: FACT_CARD字段
extracted_at: 2026-07-16T11:50:22
---

# 路径B自动写入FACT_CARD

路径B通过数据表写入/更新事件自动生成FACT_CARD记录。核心思想：数据表事件=某个L4活动已完成的信号。三个关键约束：批次粒度（用batch_key_fields控制，防止一行一条记录）、幂等性（用l4_code+batch_key+record_date做唯一性检查）、维度表就绪（写入前必须能lookup到process_key和vs_key，否则写入失败并记录错误日志）。

## 关联概念

- [[CONFIG_PROCESS_EVENT_TRIGGER]]
- [[FACT_CARD字段自动化]]

## 所属枢纽

- [[FACT_CARD字段]]
