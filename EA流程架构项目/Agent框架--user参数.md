---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 01_原始材料-外部导入/M-88_mark日常输出/任务安排相关文档_20260415-流程团队上手任务执行记录.md
authority_layer: 01_原始
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-04-15
entity_type: 待聚类
entity_ref: （无）
extracted_at: 2026-07-16T12:40:05
---

# Agent框架--user参数

在Agent框架中加入--user参数，使控制台和企业微信告警均显示执行人姓名（如terresa），以支持多人同时执行时区分告警来源。修改文件包括agents/base.py、agents/commission_agents.py、agents/performance_agents.py。

