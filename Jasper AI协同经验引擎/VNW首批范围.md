---
type: concept_atom
concept_type: 定义
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/VNW/01_初始化项目_Initialize_Project/需求定义.md
extracted_at: 2026-07-20T12:28:09
---

# VNW首批范围

VNW首批解决价值节点清单内容变化后可靠产生新信号基线且不重复处理的问题。输入为用户授权目录中的标准化清单Excel，输出写入VNW专属工作区，不修改源项目。成功标准：SHA-256检出变化后调用Phase1已验证提取器，成功后才推进状态；未变化跳过，失败不污染状态。

## 关联概念

- [[SHA-256变化检测]]
- [[Phase1提取器]]
