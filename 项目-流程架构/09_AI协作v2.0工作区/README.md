---
type: 项目笔记
source: 09_AI协作v2.0工作区
synced: 2026-06-15
tags: [项目]
---

# JASPER-AI-OP v2.0 工作区
> 建立日期：2026-06-09 | 当前阶段：Phase 0

## 架构概览
| 层级 | 角色 | 承担者 | 工具 |
|------|------|--------|------|
| 战略层 | 参谋长 | Claude Chat | 桌面端 |
| 战术层 | 军事 | Claude Code | VSCode内置 |
| 规划层 | 主指挥 | Kimi Code | VSCode扩展 |
| 执行层 | 任务执行 | OpenCode | DeepSeek |
| 执行层 | 文件执行 | Qoder | DeepSeek |
| 决策层 | 总司令 | Jasper | 人类 |

## 目录说明
- 00_项目看板/：实时状态，每次任务变更后更新
- 01_军事指挥对话/：Kimi Code↔Claude Code共识文件
- 02_指挥执行指令/：Kimi Code→执行终端的任务包
- 03_执行产出/：OpenCode/Qoder的产出文件
- 04_决策日志/：所有决策、共识、抽检、时间审计记录
- 05_规范文件/：F2协作规范、各角色手册
- 06_数据库脚本/：Phase 2自动化脚本（待开发）
- 07_模板库/：标准任务包模板

## 紧急覆盖权
Jasper可在任何时候声明"紧急覆盖"，直接向任意终端下指令，
不经过Kimi Code，不需要共识。紧急覆盖后须补记decision_log。
