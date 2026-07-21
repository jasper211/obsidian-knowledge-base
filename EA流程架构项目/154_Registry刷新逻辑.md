---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/KPI穿透/线三_154Registry刷新报告_v2.0.md
extracted_at: 2026-07-20T21:53:02
---

# 154 Registry刷新逻辑

154 Registry刷新时，从能力问题全集提取(vn_id, kpi_name)组合，删除已废弃节点，为每个KPI生成新编码VN-{业务域简称}-{NNN}，基于业务语义建立与dim_kpi 43的多对多映射，映射关系类型包括direct_correspondence、value_chain_decomposition、process_support、driver_factor、rollup_aggregation。

## 关联概念

- [[废弃节点列表]]
- [[业务映射关系]]
