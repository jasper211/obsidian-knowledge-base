---
type: concept_atom
concept_type: 经验教训
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/11_监控与优化_Monitor_and_Optimize/README.md
extracted_at: 2026-07-20T12:32:19
---

# BOM剥离修复

迁移到共享的 read_content_truncated 时发现原 PTA-SCAN/PTA-INTEL-RW 显式处理了 utf-8-sig BOM，但批2迁移 SCAN 时改用的共享函数未覆盖，导致回归。统一在共享函数中做了 BOM 剥离修复。

## 关联概念

- [[文件读取]]
- [[BOM]]
