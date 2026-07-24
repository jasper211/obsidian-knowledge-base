---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/规则分析（Jasper）/05_SOP/SOP_VN-PAY-01_市场佣金制作产出包_v0.2.md
authority_layer: 02_定稿
domain: PAY
confidence: HIGH
confidence_reason: 原文在必检项中用'立即发消息询问，禁止继续'明确限定
decision_status: UNSTATED
as_of: 未知
entity_type: SOP
entity_ref: （无）
status: 生效
extracted_at: 2026-07-24T10:26:14
---

# 产品ID有效性检查

开始处理前必须验证涉及的Product_ID已存在于DIM_Product_ID表中，若查询为空则立即停止并询问，禁止继续后续步骤，以避免无效数据写入。

## 关联概念

- [[前置检查]]
- [[DIM_Product_ID]]
- [[佣金数据录入岗]]
