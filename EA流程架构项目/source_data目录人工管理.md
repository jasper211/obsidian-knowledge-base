---
type: concept_atom
concept_type: 经验教训
project: EA流程架构项目
source: 01_原始材料-外部导入/M-88_mark日常输出/任务安排相关文档_20260415-流程团队上手任务执行记录.md
authority_layer: 01_原始
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-04-15
entity_type: 待聚类
entity_ref: （无）
extracted_at: 2026-07-16T12:40:06
---

# source_data目录人工管理

佣金链和业绩链共用etl/agg/source_data/目录，每次运行前需人工确认目录内只有当前链路所需文件，否则会读错文件导致ETL失败。

## 关联概念

- [[佣金链Agent管线]]
- [[业绩链Agent管线]]
