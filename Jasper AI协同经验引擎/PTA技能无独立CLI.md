---
type: concept_atom
concept_type: 规则
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/AI_PLATFORM_GUIDE.md
extracted_at: 2026-07-20T12:29:34
---

# PTA技能无独立CLI

从 v2.0.0 开始，PTA 的五个技能（S01-S05）不再是独立可调用的脚本，而是 skills/ 下的 Python 类，只能被 agent.py 或 import 它们的代码在同进程内调用。调试单个技能应直接查看对应源码或编写测试脚本 import 调用，不再有单独的 CLI 入口。

## 关联概念

- [[PTA统一入口]]
