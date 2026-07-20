---
type: concept_atom
concept_type: 规则
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/Agent搭建SOP_v1.0.md
extracted_at: 2026-07-20T12:23:27
---

# 子Agent开发标准

每个子Agent必须满足：有清晰docstring、argparse参数支持、输入验证（validate方法）、错误处理（try-except）、返回值（结构化dict）、状态持久化（如需）、生产环境只读。

## 关联概念

- [[Agent搭建六步法]]
