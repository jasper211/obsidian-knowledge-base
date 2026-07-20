---
type: concept_atom
concept_type: 规则
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/Agent搭建SOP_v1.2.md
extracted_at: 2026-07-20T12:24:10
---

# Git提交作用域纪律

Git提交前只git add该Agent目录下的文件，禁止使用git add -A或git add .，避免误提交其他Agent的改动或敏感配置文件。提交前用git diff --cached --name-only检查暂存区。

## 关联概念

- [[文档归档]]
