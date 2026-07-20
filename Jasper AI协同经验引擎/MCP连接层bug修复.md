---
type: concept_atom
concept_type: 经验教训
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/OB/README.md
extracted_at: 2026-07-20T12:26:21
---

# MCP连接层bug修复

在检索服务校准过程中，发现 tools.mjs 中存在一个连接层 bug：7个工具收到组合对象却按 vaultIndex 直接访问。该 bug 已通过真实 MCP 连接验证，8 个工具全部恢复正常。

## 关联概念

- [[检索服务]]
