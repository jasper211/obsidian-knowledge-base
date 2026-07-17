---
type: concept_atom
concept_type: 经验教训
project: EA流程架构项目
source: 01_原始材料-外部导入/M-88_mark日常输出/任务安排相关文档_P2-2_Agent框架学习笔记.md
authority_layer: 01_原始
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
extracted_at: 2026-07-16T12:48:52
---

# 试跑Agg1失败原因

Agg1源头佣金宽表Agent试跑失败，原因是依赖FACT1的输出目录未链接（Mac环境需手动链接etl/agg/source_data/到FACT1的output）。Windows上已配好，Mac需手动操作。

## 关联概念

- [[Agg1_source_commission_wide]]
- [[FACT1_commission_rate]]
