---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 03_reviews/第1周_Phase0启动_周报复盘.md
extracted_at: 2026-07-20T12:18:33
---

# GitHub推送协议选择

当GitHub HTTPS推送因LibreSSL兼容性失败时，应改用SSH协议；若SSH 22端口被封锁，可在~/.ssh/config中配置使用ssh.github.com:443作为fallback，因为443端口通常被防火墙放行。

## 关联概念

- [[SSH网络排错]]
