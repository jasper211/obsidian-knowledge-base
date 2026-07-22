---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 02_过程成果-工作产出/规则分析（Jasper）/05_SOP/SOP_VN-PAY-01_市场佣金制作产出包_v0.2.md
authority_layer: 02_草稿
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
extracted_at: 2026-07-16T19:14:18
---

# Fact表校验规则

从Fact_Commission_Rate提取FYC/RYC数据，与本表计算Total做减法，若不为零则立即逐行排查；若误差极小（≤0.0001）且符合四舍五入规则，则备注说明。

