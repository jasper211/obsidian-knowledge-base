---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 01_原始材料-外部导入/M-88_mark日常输出/日常持续更新_上下文报告_SSOT防御SPOF_v1.docx
authority_layer: 01_原始
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 非正式主题
entity_ref: 二次硬编码Fail_Loud_二次硬编码Fail_Loud误伤风险
extracted_at: 2026-07-16T12:52:00
---

# 二次硬编码Fail Loud熔断

任何下游层Override上游SSOT的行为构成二次硬编码，必须立即触发Fail Loud熔断。架构CI持续扫描下游层是否Override上游SSOT，GO标准为所有下游层完全消费SSOT且0 Override，NO-GO触发即熔断。

## 关联概念

- [[SSOT定义]]
- [[架构CI Fail Loud]]

## 所属枢纽

- [[二次硬编码Fail_Loud_二次硬编码Fail_Loud误伤风险]]
