---
type: concept_atom
concept_type: 定义
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/VNW/VNW现状诊断与推进计划_20260720.md
extracted_at: 2026-07-21T02:00:44
---

# VNW最小闭环

VNW v0.2.0 已完成的最小闭环包括：清单变更检测（基于文件内容SHA-256）→ 信号提取（复用Phase1的signal_extractor_legacy.py）→ 状态提交。该闭环在真实数据上通过新旧两版清单验证，正确返回unchanged。

## 关联概念

- [[SHA-256变更检测]]
- [[信号提取器复用]]
