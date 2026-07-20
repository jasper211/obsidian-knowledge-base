---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/11_监控与优化_Monitor_and_Optimize/README.md
extracted_at: 2026-07-20T12:32:15
---

# 通用版与Rw版数据模型分离

PTA-INTEL 通用版和 PTA-INTEL-RW 专用版虽然表面同构（analyze/query/cross 三模式），但数据模型完全不同：通用版猜 Markdown/CSV 结构（TaskItem），Rw 版精确读固定台账 CSV 列名（TrackItem）。迁移时保留两套解析器/分析器，通过自动探测目标项目目录下是否有 Rw 固定台账 CSV 文件名来选择后端。

## 关联概念

- [[项目智能分析器]]
- [[数据模型]]
