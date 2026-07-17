---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 01_原始材料-外部导入/M-88_mark日常输出/Mark_第三轮决策回复_M4-W10_20260529.md
authority_layer: 01_原始
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-29
entity_type: 待聚类
entity_ref: （无）
extracted_at: 2026-07-16T12:46:45
---

# v_fact_sales_activity多事件升级

接受 v2.2 多事件升级，将 v1 单一 event_type (POLICY_SIGN) 扩展为 5 个事件类型 (RESERVATION/POLICY_SIGN/SUBMISSION/APPROVAL/CANCEL)，行数从 2,918 增至 11,253。功能无损：P1 视图加 WHERE event_type='POLICY_SIGN' 仍可维持一保单一行聚合；额外收益包括全生命周期洞察；回退成本极低。风险：多事件导致行数膨胀，BI 不做过滤会重复计算，已在文档中显式警告。

## 关联概念

（暂无）
