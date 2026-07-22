---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/规则分析（Jasper）/02_信号提取基线/提取合集校准/PAY域_价值节点信号提取基线_v1.0.md
authority_layer: 02_草稿
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 非正式主题
entity_ref: 续保Shortage规则
extracted_at: 2026-07-16T18:31:41
status: 待裁定
conflict_group: 续保Shortage规则
---

# Shortage仅续保适用边界规则

VN-PAY-07节点规则：Shortage不追索严格限定于续保业务，新单不适用。

## 关联概念

- [[银行权益活动费对账单]]

## 所属枢纽

- [[续保Shortage规则]]

## ⚠️ 待裁定：entity_ref矛盾（续保Shortage规则）

与同组原子存在冲突：[[Shortage处理规则]]、[[超限Shortage上报]]、[[续保小额差异不追索规则]]、[[新单保费不足处理]]

冲突说明：冲突点：续保Shortage金额超过100港币时，是否必须上报？'Shortage处理规则'说'不设固定罚则与金额阈值'，暗示无上报要求；而'超限Shortage上报'明确要求超过100港币必须上报财务总监和运营总监审批。涉及标题：'Shortage处理规则'与'超限Shortage上报'。

（标记时间：2026-07-21T20:56:43）
