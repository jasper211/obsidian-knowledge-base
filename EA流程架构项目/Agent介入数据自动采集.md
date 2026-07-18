---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 03_发布成果-交付物/治理规范/DICT_流程数据库数据字典_V2_项目交付.md
authority_layer: 03_已锁定
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
extracted_at: 2026-07-16T11:41:40
---

# Agent介入数据自动采集

FACT_CARD中与Agent介入相关的字段（agent_assist_flag、agent_assist_hours、agent_save_hours、human_override_flag）优先从mga-data-platform/agents/运行日志自动写入（Week 8+启用）。agent_assist_flag与agentifiability有联动校验：Human级别时agent_assist_flag须为FALSE，Auto级别且活动完成时理论上须为TRUE。

## 关联概念

- [[FACT_CARD事实表]]
- [[agentifiability分级]]
