---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/规则分析（Jasper）/05_SOP/SOP_VN-PAY-01_市场佣金制作产出包_v0.2.md
authority_layer: 草稿
source_checked_at: 2026-08-30
source_review_status: 已核v0.2草稿声明，未逐条复核正文或当前业务状态
authority_review_note: 待Terresa审核及Mark校准；历史缺口和角色描述不代表当前事实，原as_of保留
domain: PAY
confidence: HIGH
confidence_reason: 原文在必检项中用'立即发消息询问，禁止继续'明确限定
decision_status: UNSTATED
as_of: 未知
entity_type: SOP
entity_ref: （无）
status: 草稿
extracted_at: 2026-07-24T10:26:14
---

# 产品ID有效性检查

开始处理前必须验证涉及的Product_ID已存在于DIM_Product_ID表中，若查询为空则立即停止并询问，禁止继续后续步骤，以避免无效数据写入。

## 关联概念

- [[前置检查]]
- [[DIM_Product_ID]]
- [[佣金数据录入岗]]
