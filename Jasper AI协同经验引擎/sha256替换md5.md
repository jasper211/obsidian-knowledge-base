---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/11_监控与优化_Monitor_and_Optimize/README.md
extracted_at: 2026-07-20T12:32:10
---

# sha256替换md5

PTA-SCAN 迁移时改用 tools/file_diff.py 的 snapshot_dir/diff_snapshots（基于 sha256），替代原脚本自维护的 md5 哈希/快照逻辑，旧快照因此失效，首次运行会重扫。

## 关联概念

- [[文件哈希]]
- [[快照]]
