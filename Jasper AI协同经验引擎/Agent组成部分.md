---
type: concept_atom
concept_type: 定义
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/Agent搭建SOP_v1.2.md
extracted_at: 2026-07-20T12:23:52
---

# Agent组成部分

Agent由01-11编号骨架组成：01初始化项目、02配置项目、03规划项目结构、04定义Agent（agents/agent.py主循环入口）、05集成工具（tools/技术模块）、06开发技能（skills/业务模块）、07接入记忆（memory/workspace.py状态持久化）、08设计提示词（prompts/独立文件）、09测试与调试（tests/test_integration.py）、10部署与运行、11监控与优化。Python包名不带编号前缀，sys.path需加每个编号目录。

## 关联概念

- [[Agent定义]]
- [[skills/tools模块化]]


---
⚠️ **待复核**：源文档「05_Agent库/草稿/Agent搭建SOP_v1.0.md」已被删除（标记时间：2026-07-21T02:00:44）
