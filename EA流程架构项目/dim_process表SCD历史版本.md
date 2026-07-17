---
type: concept_atom
concept_type: 背景说明
project: EA流程架构项目
source: 02_过程成果-工作产出/规则分析（Jasper）/汇报与方法论/[RPT]_周五汇报初稿_规则分析方法论v3.0范式转换_v0.4.md
authority_layer: 02_草稿
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
extracted_at: 2026-07-16T15:18:04
---

# dim_process表SCD历史版本

dim_process表是SCD历史版本表，包含version/valid_from/valid_to/is_current字段。物理726行中，368条为当前版（is_current=TRUE），358条为历史版本。当前版L4的agentifiability分级已100%覆盖，无缺失脏值，但该字段与dim_agent存在矛盾分级，可信度存疑。

## 关联概念

- [[Agent评估数据可信度不足]]
- [[数据源同步滞后]]
