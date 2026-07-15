---
tags: [concept, 核心方法论, AI协同]
project: Jasper_AI协同经验引擎
source_type: Agent设计
created: 2026-07-15
---

# 方法论转正 Agent

## 一句话定义
方法论转正 Agent 是**验证标准统一沉淀 Agent**，负责把各 Agent 执行记录和踩坑记录转化为更新后的 SOP、定义文档和验证标准清单。

## 核心属性
- **服务对象**: 全部 Agent（含自己）
- **核心问题**: "这次踩的坑该怎么变成规则？"
- **输入**: 各 Agent 执行记录/踩坑记录
- **输出**: 更新后的 SOP/定义文档 + 验证标准清单
- **触发频率**: 每个 Agent 归档节点触发
- **当前状态**: 未启动（本次新提出）

## 相关本地文档
- [[项目-Jasper工作文档/Jasper AI协同经验引擎/AI工程能力整改项目/05_Agent库/草稿/三大主Agent体系架构_v1.2.md|三大主Agent体系架构]]
- [[项目-Jasper工作文档/Jasper AI协同经验引擎/AI工程能力整改项目/02_decisions/D-20260709-001_Agent验证方法论与方法论转正Agent.md|D-20260709-001 验证方法论决策]]

## 相关概念
- [[Jasper_AI协同经验引擎]] — 方法论转正 Agent 的项目载体
- [[AI工程能力整改项目]] — 方法论转正 Agent 的整改项目
- [[PTA]] — 项目任务协同 Agent
- [[VNW]] — 价值节点驱动工作流 Agent
- [[AIT]] — AI 协同转型咨询 Agent
- [[Obsidian巡检Agent]] — 基础设施层

## 工作流位置
```
Agent 执行 → 踩坑记录 → 方法论转正 Agent → 更新 SOP → 验证标准清单
```

## 我的思考
- 方法论转正 Agent 是**验证独立**原则的实现
- 所有 Agent 的验证环节用 Agent 完成，不用人工
- 验证标准统一维护，不各自发明
- 方法论转正 Agent 是项目的重要交付物
