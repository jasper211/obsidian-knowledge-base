---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 02_过程成果-工作产出/校验与上下文/数据整合_修复包_v3.md
extracted_at: 2026-07-20T22:50:35
---

# FIX-01替换价值流文件

dim_value_stream的来源文件必须从核心文档目录（非过程文档/output_旧数据/）中选取，文件名含'价值流'+'全量'或'V3'，且activity_code列的L3编码与82条标准L3完全一致。找到后清空表并重新写入，source_doc填实际文件名。

## 关联概念

- [[dim_value_stream]]
- [[L3完整清单82条]]
