---
type: entry
updated: 2026-07-22
status: placeholder
---

# 方法论知识库

这个文件夹是方法论Agent（Karpathy little-c compile范式，行业权威知识→
结构化Wiki）产出的独立顶层分区，跟`EA流程架构项目/`、`Jasper AI协同
经验引擎/`这两个OBagent（RAG范式）的项目原子文件夹平级、不混放。

方法论Agent由Jasper另外推动，本文件夹暂时是占位——设计已经在对话里
定下方向，详见OBagent代码仓库`03_规划项目结构_Plan_Project_Structure/
提炼标准_v1.0.md`的「与方法论Agent的接口」一节。

## 关联机制摘要（详细设计见上述文档）

- **硬关联**：方法论卡片如果能对上EA的正式编码（entity_ref），走现有
  entity_ref枢纽机制，同编码下项目原子和方法论卡片混合挂载
- **软关联**：语义相似的内容走embedding聚类（复用"非正式主题"枢纽的
  threshold=0.72+LLM连贯性判断那套，小样本先验证再全量）
- **晋升机制**：项目原子晋升到方法论卡片的候选筛选条件——
  `confidence=HIGH` 且 `status=生效` 且 `backlink数量>=N` 且未被
  entity_ref矛盾扫描标记冲突，候选清单由OBagent这边的一次性查询脚本
  产出，"怎么合并进方法论卡片"的动作归方法论Agent负责
- **冲突检测**：扩展现有entity_ref矛盾扫描逻辑到跨知识源场景——同
  entity_ref下如果既有项目原子又有方法论卡片，拿方法论卡片当标尺去
  比对项目原子

## 前提

方法论Agent产出的卡片如果想复用OBagent现有的hub/聚类/矛盾扫描机制，
frontmatter需要跟OBagent的`concept_atom`schema保持兼容（至少
`entity_type`/`entity_ref`两个字段命名和取值方式一致）——这不是OBagent
单方面能保证的，需要两边设计时对齐。
