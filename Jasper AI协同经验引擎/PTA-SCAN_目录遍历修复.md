---
type: concept_atom
concept_type: 经验教训
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/_retired_flat_structure/README_v1.md
extracted_at: 2026-07-20T12:31:53
---

# PTA-SCAN 目录遍历修复

v1.5.1 修复 PTA-SCAN 目录遍历 bug：原只检查文件名是否以 . 开头，未排除 .git/node_modules 目录本身，导致 .git 内部文件被误扫；改用 os.walk + 目录剪枝修复。

## 关联概念

- [[增量扫描机制]]
