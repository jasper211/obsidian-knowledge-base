---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 01_原始材料-外部导入/M-88_mark日常输出/上下文报告_SSOT防御SPOF_v1.docx
authority_layer: 01_原始
confidence: UNSTATED
decision_status: UNSTATED
as_of: 未知
entity_type: 非正式主题
entity_ref: 二次硬编码Fail_Loud_二次硬编码Fail_Loud误伤风险
extracted_at: 2026-07-16T12:51:37
---

# 二次硬编码Fail Loud

下游层Override上游SSOT即二次硬编码，属于L0禁令。架构CI扫描检测到任一Override立即触发Fail Loud熔断，不允许沉默处理。GO标准为所有下游层完全消费SSOT，0 Override。

## 关联概念

- [[SSOT定义]]

## 所属枢纽

- [[二次硬编码Fail_Loud_二次硬编码Fail_Loud误伤风险]]
