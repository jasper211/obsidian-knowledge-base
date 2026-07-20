---
type: concept_atom
concept_type: 经验教训
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/AI_PLATFORM_GUIDE.md
extracted_at: 2026-07-20T12:29:39
---

# PTA--sync需人工确认

agent.py 的 --sync 参数会真实执行 git push 到共享仓库，因此必须由人工明确要求才能使用。如果让其他 AI 无人值守运行 PTA，务必确保它不会自动添加 --sync 参数，以避免意外推送。

## 关联概念

- [[PTA统一入口]]
