---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 02_decisions/D-20260702-001_GitHub推送协议选择.md
extracted_at: 2026-07-20T12:22:05
---

# SSH优于HTTPS连接GitHub

在Phase 0中，因macOS LibreSSL与GitHub HTTPS握手失败（SSL_ERROR_SYSCALL），决定使用SSH密钥认证而非HTTPS+PAT。SSH从根本上解决了兼容性问题，一次配置长期使用，符合工程师协作标准，且能积累密钥管理经验。

## 关联概念

- [[SSH密钥生成]]
- [[GitHub远程地址设置]]
