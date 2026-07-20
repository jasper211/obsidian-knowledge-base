---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 01_execution/P1-04_访谈规则继承/任务执行记录.md
extracted_at: 2026-07-20T12:20:10
---

# 解析策略：字符串find+局部正则

解析手工基线Markdown表格时，采用字符串find()定位信号4标题，再使用局部正则提取表格行，避免贪婪匹配导致跨节点污染。

## 关联概念

- [[信号4访谈规则继承]]
