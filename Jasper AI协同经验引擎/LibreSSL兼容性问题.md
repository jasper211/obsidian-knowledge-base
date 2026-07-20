---
type: concept_atom
concept_type: 经验教训
project: Jasper AI协同经验引擎
source: 02_decisions/D-20260702-001_GitHub推送协议选择.md
extracted_at: 2026-07-20T12:22:07
---

# LibreSSL兼容性问题

macOS自带的LibreSSL与部分网络环境或服务端TLS配置存在兼容性问题，遇到SSL_ERROR_SYSCALL时优先尝试SSH而非切换OpenSSL后端，因为后者未根本解决网络层不稳定问题。

## 关联概念

- [[SSH优于HTTPS连接GitHub]]
- [[OpenSSL后端切换]]
