---
type: concept_atom
concept_type: 规则
project: EA流程架构项目
source: 08_任务与跟进/AI上下文/任务0_密码清理_Mark端Claude同步指南_20260522.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-22
entity_type: 待聚类
entity_ref: （无）
extracted_at: 2026-07-16T11:50:43
---

# git历史暴露检查

清理明文密码后，需使用git log --all --oneline -S命令检查git历史中是否包含该密码，若存在则需进一步清理历史。

## 关联概念

- [[明文密码清理]]
