---
tags: [concept, 核心方法论, AI协同]
project: Jasper_AI协同经验引擎
source_type: Agent设计
created: 2026-07-15
updated: 2026-08-13
---

# Obsidian 巡检 Agent

## 一句话定义
Obsidian 巡检 Agent 是**知识库基础设施 Agent**，负责知识库状态巡检、AI 工具调用准则统一，以及读取侧/写入侧治理边界的持续校准。

## 核心属性
- **服务对象**: 全部 AI 工具 + 知识库
- **核心问题**: "各 AI 调用知识库/工具的准则一致吗？"
- **输入**: 各 AI 工具调用请求 + 知识库变更
- **输出**: 知识库最新状态 + 调用日志
- **触发频率**: 持续/定期巡检
- **当前状态**: 已有实际代码，且现行口径下属于基础设施/治理层，不是独立业务产出层

## 相关本地文档
- [Jasper经验主视图导航MOC_2026-08-13](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/Jasper经验主视图导航MOC_2026-08-13.md:1)
- [[项目-Jasper工作文档/Jasper AI协同经验引擎/AI工程能力整改项目/05_Agent库/OB知识库同步巡检Agent/|OB 巡检 Agent 实现]]
- [[项目-Jasper工作文档/Jasper AI协同经验引擎/Agent运行仪表盘.md|Agent 运行仪表盘]]

## 相关概念
- [[Jasper_AI协同经验引擎]] — Obsidian 巡检 Agent 的项目载体
- [[AI工程能力整改项目]] — Obsidian 巡检 Agent 的整改项目
- [[PTA]] — 项目任务协同 Agent
- [[VNW]] — 价值节点驱动工作流 Agent
- [[AIT]] — AI 协同转型咨询 Agent
- [[方法论转正Agent]] — 验证标准统一
- [[Obsidian]] — Obsidian 知识库工具

## 工作流位置
```
AI 工具调用 → Obsidian 巡检 Agent → 知识库状态检查 → 调用日志 → 一致性报告
```

## 我的思考
- Obsidian 巡检 Agent 是**基础设施层**
- 不对应业务产出，是其他 4 个 Agent 的公共支撑
- 现行重点不是“何时启动”，而是读取侧、写入侧、文档维护责任怎样持续收口
- Obsidian 巡检 Agent 是项目的重要交付物

## 当前主入口

截至 `2026-08-13`，后续优先通过 [Jasper经验主视图导航MOC_2026-08-13](/Users/a112233/Desktop/Jasper工作文档（不含EA项目）/OB知识库_vault/MOC/Jasper经验主视图导航MOC_2026-08-13.md:1) 进入，再结合与 OB 相关的现行经验原子理解它的边界：

- `OB巡检Agent定位`
- `OB读取侧未接线`
- `OB写入侧空白`
- `OB自巡检写入理想`
- `OB写入侧项目分工`
