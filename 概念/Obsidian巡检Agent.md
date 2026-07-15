---
tags: [concept, 核心方法论, AI协同]
project: Jasper_AI协同经验引擎
source_type: Agent设计
created: 2026-07-15
---

# Obsidian 巡检 Agent

## 一句话定义
Obsidian 巡检 Agent 是**知识库基础设施 Agent**，负责统一 AI 工具调用准则和知识库状态监控，确保各 AI 工具间调用规范一致。

## 核心属性
- **服务对象**: 全部 AI 工具 + 知识库
- **核心问题**: "各 AI 调用知识库/工具的准则一致吗？"
- **输入**: 各 AI 工具调用请求 + 知识库变更
- **输出**: 知识库最新状态 + 调用日志
- **触发频率**: 持续/定期巡检
- **当前状态**: 已有实际代码，需补充规范化设计

## 相关本地文档
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
- 未来定位已跟 Jasper 对齐，启动时机待明确指令
- Obsidian 巡检 Agent 是项目的重要交付物
