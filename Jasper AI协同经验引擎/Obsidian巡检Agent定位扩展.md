---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/三大主Agent体系架构_v1.2.md
extracted_at: 2026-07-20T12:22:34
---

# Obsidian巡检Agent定位扩展

Obsidian巡检Agent（OB）在v1.2中定位从基础设施巡检扩展为所有业务Agent（PTA/VNW/AIT）的背景记忆/认知层。其核心设计是：项目文件先做向量分析形成概念笔记/知识原子，每个原子带逻辑关系和说明（类似Graph RAG），业务Agent执行任务前从图中检索背景以“不失真”。现有MCP工具族仅支持全文关键词搜索+图遍历（只读），尚无向量语义搜索和写入能力。启动时机明确等待Jasper指令，前置条件是其他AI终端先搭完概念笔记网络。

## 关联概念

- [[Obsidian巡检Agent]]
- [[PTA]]
- [[知识图谱]]


---
⚠️ **待复核**：源文档「05_Agent库/草稿/三大主Agent体系架构_v1.2.md」已被删除（标记时间：2026-07-21T02:00:44）
