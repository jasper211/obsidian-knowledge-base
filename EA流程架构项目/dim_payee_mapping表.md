---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 01_原始材料-外部导入/M-77_跨部门输入/数据模型设计v2.2.md
authority_layer: 01_原始
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-DIM_PAYEE_MAPPING
extracted_at: 2026-07-16T12:37:08
---

# dim_payee_mapping表

dim_payee_mapping是v2.2新增的维度表，用于存储人员姓名到实际收款方的映射关系，包括特殊业务约定（如吴竞→白博文）。在V1到V3转换时，先通过此表将原人名重映射为实际人名，再按实际收款方分组。

## 关联概念

- [[收款人合并规则]]
- [[V1到V3转换]]
