---
type: concept_atom
concept_type: 经验教训
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/OB/10_部署与运行_Deploy_and_Run/README.md
extracted_at: 2026-07-20T12:26:44
---

# 旧plist未更新

`com.jasper.ob-sync-agent.plist` 是从旧游离目录迁移过来的 launchd 模板，内容尚未更新，仍指向旧的部署路径，而非迁移后的新入口 `04_定义Agent_Define_Agent/agents/agent.py --sync-check`。当前实际运行的是旧部署副本，迁移新代码不影响该任务继续按原样每小时运行。

## 关联概念

- [[launchd任务切换]]
