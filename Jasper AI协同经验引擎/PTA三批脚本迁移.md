---
type: concept_atom
concept_type: 经验教训
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/三大主Agent体系架构_v1.2.md
extracted_at: 2026-07-20T12:22:40
---

# PTA三批脚本迁移

PTA将原有6个独立扁平脚本（DASH/EXT/DISCOVER/SCAN/INTEL/INTEL-RW）按风险递增分三批全部迁移进skills/tools包，原脚本移入_retired_flat_structure/。迁移过程中发现并修复多个真实bug：批1修复EXT目录排除不完整（漏排node_modules）；批2修复SCAN改用sha256、删除忙等循环、DISCOVER去重文件未记入增量状态；批3修复新引入的read_content_truncated共享助手漏了utf-8-sig BOM处理。

## 关联概念

- [[PTA]]
- [[skills/tools]]


---
⚠️ **待复核**：源文档「05_Agent库/草稿/三大主Agent体系架构_v1.2.md」已被删除（标记时间：2026-07-21T02:00:44）
