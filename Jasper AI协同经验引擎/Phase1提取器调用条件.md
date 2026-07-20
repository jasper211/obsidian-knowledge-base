---
type: concept_atom
concept_type: 规则
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/VNW/01_初始化项目_Initialize_Project/需求定义.md
extracted_at: 2026-07-20T12:28:13
---

# Phase1提取器调用条件

仅在SHA-256检出内容变化后，才调用Phase1已验证提取器。提取器成功执行后才推进状态；失败则不污染状态。

## 关联概念

- [[SHA-256变化检测]]
- [[VNW首批范围]]
