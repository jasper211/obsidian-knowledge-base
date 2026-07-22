---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/规则分析（Jasper）/03_访谈准备与执行/访谈录音md/财务（二轮）-结构化信号提取（jasper版）.md
authority_layer: 02_草稿
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 非正式主题
entity_ref: 续保Shortage规则
extracted_at: 2026-07-17T01:51:09
status: 待裁定
conflict_group: 续保Shortage规则
---

# Shortage处理规则

续保保费不足（Shortage）时，缺口优先从佣金中扣回；若理财师不接受扣回，通常不追款，由公司承担（营业外支出）。新单不允许生效前不足。不足原因可能为汇率或银行手续费，不设固定罚则与金额阈值。

## 关联概念

（暂无）

## 所属枢纽

- [[续保Shortage规则]]

## ⚠️ 待裁定：entity_ref矛盾（续保Shortage规则）

与同组原子存在冲突：[[超限Shortage上报]]、[[续保小额差异不追索规则]]、[[新单保费不足处理]]、[[Shortage仅续保适用边界规则]]

冲突说明：冲突点：续保Shortage金额超过100港币时，是否必须上报？'Shortage处理规则'说'不设固定罚则与金额阈值'，暗示无上报要求；而'超限Shortage上报'明确要求超过100港币必须上报财务总监和运营总监审批。涉及标题：'Shortage处理规则'与'超限Shortage上报'。

（标记时间：2026-07-21T20:56:43）
