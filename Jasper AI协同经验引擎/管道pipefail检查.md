---
type: concept_atom
concept_type: 规则
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/Agent验证标准清单_v1.0.md
extracted_at: 2026-07-20T12:25:21
---

# 管道pipefail检查

脚本中凡是使用管道（如 `cmd | tail/grep/head`）的地方，必须开启 `set -eo pipefail`，否则管道退出码可能掩盖前序命令的失败。若使用 `grep -q` 并检查 `$?`，应改为 `if pipeline; then` 直接判断，避免提前终止。

## 关联概念

- [[Agent验证四原则]]
- [[确定性检查优先]]
