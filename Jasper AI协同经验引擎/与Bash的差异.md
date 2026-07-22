---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/12_任务看板_Task_Dashboard/web/node_modules/tinyglobby/node_modules/picomatch/README.md
authority_layer: 02_草稿
confidence: HIGH
confidence_reason: 文档专门章节明确陈述为设计选择
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
status: 生效
extracted_at: 2026-07-22T03:14:18
---

# 与Bash的差异

Picomatch 的匹配行为和预期结果基于 Bash 单元测试和 4.3 规范，但有例外：1) Bash 用 `*` 匹配 `foo/bar/baz`，Picomatch 只使用 `**` 匹配嵌套目录；2) Bash 在否定 extglob 中贪婪匹配（如 `!(foo)*` 匹配 `foo`），Picomatch 避免这种内存低效且认为不正确，返回 false。

## 关联概念

- [[星号不匹配路径分隔符]]
