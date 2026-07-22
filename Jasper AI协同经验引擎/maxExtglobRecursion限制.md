---
type: concept_atom
concept_type: 规则
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/12_任务看板_Task_Dashboard/web/node_modules/tinyglobby/node_modules/picomatch/README.md
authority_layer: 02_草稿
confidence: HIGH
confidence_reason: 选项表格中明确描述
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
status: 生效
extracted_at: 2026-07-22T03:14:18
---

# maxExtglobRecursion限制

为避免性能问题，嵌套量化的 extglob 和其他危险重复 extglob 形式有递归限制（默认 0）。超过限制时，extglob 会被当作字面量字符串，而非编译为正则。可设为 `false` 禁用此保护。

## 关联概念

（暂无）
