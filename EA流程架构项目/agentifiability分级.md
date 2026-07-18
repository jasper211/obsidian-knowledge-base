---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 03_发布成果-交付物/治理规范/DICT_流程数据库数据字典_V2_项目交付.md
authority_layer: 03_已锁定
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 非正式主题
entity_ref: Agent维度表问题
extracted_at: 2026-07-16T11:41:39
---

# agentifiability分级

agentifiability是L4活动的Agent化分级，枚举值为Auto（全自动）、Aug（增强）、Hybrid（人机协同）、Human（人工）。该字段在DIM_PROCESS中记录，并冗余到FACT_CARD。分级依据为Agent化6维评分总分，Auto通常≥14分，Human通常≤4分。

## 关联概念

- [[Agent化6维评分]]
- [[DIM_PROCESS维度表]]

## 所属枢纽

- [[Agent维度表问题]]
