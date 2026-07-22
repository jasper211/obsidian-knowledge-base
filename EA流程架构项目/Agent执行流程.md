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

# Agent执行流程

每个Agent的run方法依次执行：L1 execute（业务逻辑）→ L3 validate（校验）→ L4 失败自动告警（企业微信）→ L5 产出日志（summary）。

