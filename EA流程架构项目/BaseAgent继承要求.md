---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 01_原始材料-外部导入/M-88_mark日常输出/任务安排相关文档_P2-2_Agent框架学习笔记.md
authority_layer: 01_原始
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 非正式主题
entity_ref: Agent资产沉淀_Agent资产沉淀
extracted_at: 2026-07-16T12:48:50
---

# BaseAgent继承要求

自定义Agent需继承BaseAgent，必须设置name（唯一）、owner（7族代码）、l4_codes（对应L4编号）、description，并实现execute和validate方法。

## 关联概念

- [[BaseAgent]]
- [[validate方法]]
- [[7族代码]]

## 所属枢纽

- [[Agent资产沉淀]]
