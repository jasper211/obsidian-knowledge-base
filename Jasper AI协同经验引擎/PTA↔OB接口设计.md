---
type: concept_atom
concept_type: 决策
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/三大主Agent体系架构_v1.2.md
extracted_at: 2026-07-20T12:22:32
---

# PTA↔OB接口设计

PTA与Obsidian巡检Agent（OB）采用client-service划分：OB拥有知识图谱（概念笔记+关系），提供检索（返回相关上下文包）和写入（接收发现并组织成新原子）能力；PTA作为薄客户端，只负责“什么时候该问”和“问完怎么用”，不重新实现图遍历或原子切分。当前阶段两者都不动，需等待Jasper其他AI终端先搭建完概念笔记网络（向量层），再下达明确指令后按Agent搭建SOP重新搭建OB。

## 关联概念

- [[PTA]]
- [[Obsidian巡检Agent]]
- [[知识图谱]]
