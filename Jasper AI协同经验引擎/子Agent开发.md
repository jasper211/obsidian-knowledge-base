---
type: concept_atom
concept_type: 规则
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/Agent搭建SOP_v1.2.md
extracted_at: 2026-07-20T12:24:03
---

# 子Agent开发

第4步每个skill/tool需满足：清晰docstring（含来源和迁移决策）、不直接读写memory.workspace状态文件（接收状态dict返回更新后dict）、有错误处理（明确异常类型）、有返回值（结构化dict/dataclass）、LLM调用提示词放独立prompts文件、外部项目路径物理隔离。

## 关联概念

- [[Agent搭建六步法]]
- [[skills/tools模块化]]
