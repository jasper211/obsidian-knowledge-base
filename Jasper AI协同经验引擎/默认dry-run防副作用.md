---
type: concept_atom
concept_type: 规则
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/08_设计提示词_Design_Prompts/prompts/system.md
extracted_at: 2026-07-20T12:32:57
---

# 默认dry-run防副作用

不确定某个指令是否该有真实副作用时，默认以dry-run模式执行，让用户显式加--execute确认后才真正执行。

## 关联概念

- [[安全边界]]
- [[git push仅由doc_sync触发]]
