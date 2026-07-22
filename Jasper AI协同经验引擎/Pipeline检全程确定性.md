---
type: concept_atom
concept_type: 规则
project: Jasper AI协同经验引擎
source: 05_Agent库/草稿/PTA/README.md
authority_layer: 02_草稿
confidence: HIGH
confidence_reason: 原文用'全部是确定性检查...不调用LLM'的肯定陈述
decision_status: UNSTATED
as_of: 未知
entity_type: 待聚类
entity_ref: （无）
status: 生效
extracted_at: 2026-07-22T03:11:53
---

# Pipeline检全程确定性

Pipeline健康检测所有检查项均为确定性操作（文件存在性/测试exit code/字段读取/mtime），不调用LLM，不做主观判断，只展示差异供人决策。

## 关联概念

- [[Pipeline差距矩阵]]
- [[检测记录]]
