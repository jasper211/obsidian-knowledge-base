---
type: concept_atom
concept_type: 规则
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/03_规划项目结构_Plan_Project_Structure/README.md
extracted_at: 2026-07-20T12:30:56
---

# sys.path配置

调用方（如agents/agent.py）需要将每个编号文件夹加入sys.path（而非项目根目录），才能正确解析from skills.xxx import等语句。具体实现见04_定义Agent_Define_Agent/agents/agent.py开头的sys.path.insert代码。

## 关联概念

- [[编号文件夹嵌套]]
- [[项目目录结构规范]]
