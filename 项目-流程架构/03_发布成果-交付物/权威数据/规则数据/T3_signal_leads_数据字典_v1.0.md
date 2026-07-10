---
type: 项目笔记
source: 03_发布成果-交付物/权威数据/规则数据
synced: 2026-06-15
tags: [项目]
---

# T3 · signal_leads · 数据字典

> 任务包：TASK-M4W10-095
> 产出日期：2026-06-11
> 对应CSV：T3_signal_leads_PAY域_v1.0.csv
> 来源：PAY域_价值节点信号提取基线_v1.8.md · Step4 B类·规则线索

---

## 字段定义

| 列号 | 字段名 | 数据类型 | 来源 | 枚举值/格式 | 说明 |
|---|---|---|---|---|---|
| 1 | lead_id | TEXT | 自编 | S3-PAY[NN]-[NNN] | 主键，B类规则线索唯一标识 |
| 2 | node_id | TEXT | v1.8 MD Step4 B类节点列 | VN-PAY-XX | 外键→T1.node_id |
| 3 | content | TEXT | v1.8 MD Step4 B类信号内容列 | 原文 | 规则线索内容 |
| 4 | source | TEXT | v1.8 MD Step4 B类来源列 | SheetX·RowX | 来源定位 |
| 5 | confidence | TEXT | v1.8 MD Step4 B类确认程度列 | 明确/推断/待确认 | 确认程度 |
| 6 | target_rule_type | TEXT | v1.8 MD Step4 B类转化后规则类型列 | 合规约束规则/计算推导规则/流程触发规则/数据结构规则 | 访谈后可能转化的规则类型 |
| 7 | interview_priority | TEXT | v1.8 MD Step4 B类访谈优先级列 | P0/P1/P2 | 访谈优先级 |
| 8 | l_layer | TEXT | v1.8 MD Step4 B类L层定位列 | L3层/L4层/数据架构层/治理层 | 架构层定位 |
| 9 | status | TEXT | 固定初始值 | 待访谈 | 处理状态 |

---

## 枚举值规范

- **lead_id**: S3-PAY[节点后两位]-[三位序号]，例：S3-PAY02-001
- **target_rule_type**: 合规约束规则 / 计算推导规则 / 流程触发规则 / 数据结构规则
- **interview_priority**: P0 / P1 / P2
- **confidence**: 明确 / 推断 / 待确认
- **l_layer**: L3层 / L4层 / 数据架构层 / 治理层
- **status**: 待访谈（初始值，访谈后更新）

---

## 版本记录

| 版本 | 日期 | 变更内容 |
|---|---|---|
| v1.0 | 2026-06-11 | 初始产出，11条B类规则线索 |

---

## 扩展说明

### ID编号规则
lead_id = S3-PAY + 节点编号（VN-PAY-后两位）+ 三位递增序号
同一节点内按Step4 B类表格原始顺序递增

### 与T2/T5的关系
- T3是待访谈确认的规则线索
- 访谈确认后可升级为T2（已确立规则）或T5（规则库）
- status字段随访谈流程推进更新

---

## 自检声明

| # | Done Criteria | 自检结果 |
|---|---|---|
| 1 | CSV文件产出，11行×9列 | ✅ |
| 2 | lead_id唯一无重复 | ✅ |
| 3 | 所有node_id在T1范围内 | ✅ |
| 4 | status全部=待访谈 | ✅ |
| 5 | interview_priority枚举值规范 | ✅ P0×7 / P1×4 |
| 6 | target_rule_type枚举值规范 | ✅ |
| 7 | 字段来源标注清晰 | ✅ 全部来自v1.8 Step4 B类 |
| 8 | 数据字典格式统一 | ✅ |
| 9 | 自检声明已逐项自检 | ✅ |

---

> 产出文件路径：03_发布成果-交付物/权威数据/规则数据/T3_signal_leads_数据字典_v1.0.md
