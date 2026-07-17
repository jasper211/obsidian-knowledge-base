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
entity_ref: CLUSTER-dim_process.agentifiability字段不可信
extracted_at: 2026-07-16T11:45:23
---

# DIM_AGENT字段校验规则

DIM_AGENT各字段有严格校验规则，例如：agent_code格式为agent-[a-z-]+；agent_type枚举值为Auto/Aug/Hybrid（不含Human）；agent_status枚举值为已上线/开发中/规划中/已停用。

## 关联概念

- [[DIM_AGENT维度表]]
