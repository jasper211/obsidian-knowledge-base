---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 00_治理与元模型/命名编码规范/00_治理与元模型_人机协作执行规范.md
authority_layer: 00_治理
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类(已归入非正式簇)
entity_ref: CLUSTER-第一期产出清单
extracted_at: 2026-07-16T11:15:25
---

# Spec先于实现

在修改任何L3定义、RACI或岗位方案之前，必须先更新对应的schema（如doc-meta-schema.yaml、L3-definition-schema.yaml），再修改内容，最后运行验证脚本。Pipeline项目经验表明，跳过spec直接实现会导致4轮返工约8小时，而spec-driven重启可在1小时内发现20个bug。

## 关联概念

- [[知识库4件套]]
- [[quality-gate.yaml]]
