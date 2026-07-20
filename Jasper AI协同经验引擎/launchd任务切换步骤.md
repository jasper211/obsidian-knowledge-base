---
type: concept_atom
concept_type: 规则
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/OB/10_部署与运行_Deploy_and_Run/README.md
extracted_at: 2026-07-20T12:26:45
---

# launchd任务切换步骤

切换 `com.jasper.ob-sync-agent` 任务到新代码的步骤：1. 修改 plist 的 `ProgramArguments` 为调用 `agent.py --sync-check --output <path> --auto-fix --quiet`；2. 执行 `launchctl unload`/`load` 重新加载；3. 确认新任务运行一次且输出符合预期后，再删除旧部署副本。

## 关联概念

- [[旧plist未更新]]
