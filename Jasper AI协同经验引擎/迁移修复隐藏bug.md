---
type: concept_atom
concept_type: 经验教训
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/11_监控与优化_Monitor_and_Optimize/README.md
extracted_at: 2026-07-20T12:32:09
---

# 迁移修复隐藏bug

原 PTA-EXT 外部项目分析器只排除隐藏目录，未排除 node_modules 等非隐藏但应跳过的目录，导致误统计。迁移时修复了此 bug。

## 关联概念

- [[外部项目分析器]]
- [[目录扫描]]
