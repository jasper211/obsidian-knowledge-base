---
type: concept_atom
concept_type: 规则
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/VNW/03_规划项目结构_Plan_Project_Structure/流程设计.md
extracted_at: 2026-07-20T12:28:21
---

# VNW最小闭环流程

VNW v0.1 的最小闭环流程为：发现最新清单 → SHA-256 与成功状态比对 → 有变化则调用 Phase1 信号提取器 → 校验 Markdown 产物存在 → 原子写入状态。失败发生在状态提交之前，因此下一次运行仍会重试。源清单只读，状态和产物只进入 .vnw_workspace/ 或用户指定的 --workspace。

## 关联概念

- [[SHA-256比对]]
- [[Phase1信号提取器]]
- [[原子写入状态]]
