---
type: project_note
project: 流程架构
layer: "03_发布成果-交付物"
layer_tag: 交付
subdir: "权威数据"
tags: [交付]
---

## 🧭 导航
⬆️ [[03_发布成果-交付物]] · ⬆️ [[权威数据]] · 🏠 [[流程架构项目MOC]]

---

# T2 · signals · 数据字典

> 任务包：TASK-M4W10-101
> 产出日期：2026-06-11
> 对应CSV：T2_signals_PAY域_v2.0.csv
> 来源：PAY域_价值节点信号提取基线_v1.9.md · Step4 A类·已确立规则

---

## 字段定义

| 列号 | 字段名 | 数据类型 | 来源 | 枚举值/格式 | 说明 |
|---|---|---|---|---|---|
| 1 | signal_id | TEXT | 自编 | S2-PAY[NN]-[NNN] | 主键，A类规则唯一标识 |
| 2 | node_id | TEXT | v1.9 MD Step4 A类节点列 | VN-PAY-XX | 外键→T1.node_id |
| 3 | content | TEXT | v1.9 MD Step4 A类信号内容列 | 原文 | 规则内容描述 |
| 4 | source | TEXT | v1.9 MD Step4 A类来源列 | SheetX·RowX | 来源定位 |
| 5 | confidence | TEXT | v1.9 MD Step4 A类确认程度列 | 明确/推断/待确认 | 确认程度 |
| 6 | rule_subtype | TEXT | v1.9 MD Step4 A类规则子类列 | 合规约束规则/计算推导规则/流程触发规则/数据结构规则 | 规则子分类 |
| 7 | completeness | TEXT | v1.9 MD Step4 A类规则完整性列 | 完整/部分完整/需补充 | 规则完整性评估 |
| 8 | l_layer | TEXT | v1.9 MD Step4 A类L层定位列 | L3层/L4层/数据架构层/治理层 | 架构层定位 |
| 9 | rule_trigger | TEXT | v1.9 MD Step4 A类rule_trigger列 | 原文 | 规则触发条件 |
| 10 | rule_action | TEXT | v1.9 MD Step4 A类rule_action列 | 原文 | 规则执行动作 |
| 11 | rule_standard | TEXT | v1.9 MD Step4 A类rule_standard列 | 原文 | 规则标准/阈值 |
| 12 | rule_exception | TEXT | v1.9 MD Step4 A类rule_exception列 | 原文/待访谈 | 例外情况说明 |
| 13 | rule_owner | TEXT | v1.9 MD Step4 A类rule_owner列 | 岗位族/待访谈 | 规则责任归属 |

---

## 枚举值规范

- **signal_id**: S2-PAY[节点后两位]-[三位序号]，例：S2-PAY01-001
- **rule_subtype**: 合规约束规则 / 计算推导规则 / 流程触发规则 / 数据结构规则
- **completeness**: 完整 / 部分完整 / 需补充
- **confidence**: 明确 / 推断 / 待确认
- **l_layer**: L3层 / L4层 / 数据架构层 / 治理层
- **rule_exception**: 原文 / 待访谈（推断型规则的例外需访谈确认）
- **rule_owner**: 岗位族代码（如A-操作执行） / 待访谈

---

## 版本记录

| 版本 | 日期 | 变更内容 |
|---|---|---|
| v1.0 | 2026-06-11 | 初始产出，18条A类已确立规则，8列 |
| v2.0 | 2026-06-11 | TASK-M4W10-101：追加5个子字段列（rule_trigger/rule_action/rule_standard/rule_exception/rule_owner），扩展至13列。来源从v1.8升级至v1.9 |

---

## 扩展说明

### ID编号规则
signal_id = S2-PAY + 节点编号（VN-PAY-后两位）+ 三位递增序号
同一节点内按Step4 A类表格原始顺序递增

### 新增子字段说明（v2.0）
v1.9对A类规则进行了结构化拆解，从原始的content描述中抽取出5个子字段：
- **rule_trigger**：什么条件触发该规则（如"当单笔付款>100万"）
- **rule_action**：规则要求执行什么动作（如"需双人审批"）
- **rule_standard**：规则的标准/阈值（如">=100万人民币"）
- **rule_exception**：规则的例外情况（如推断型规则填"待访谈"）
- **rule_owner**：规则的责任归属岗位族

### 子字段数据来源策略
- content明确拆分出的：直接提取
- content未明确拆分、但上下文可推断的：标注"推断·待确认"或"待访谈"
- 完全无法推断的：标注"待访谈"

### 与T1的关系
- T2.node_id 为外键，引用 T1.node_id
- 所有node_id必须在T1.node_id范围内

### 与T5的关系
- T2是可直接进入规则库的信号
- T5（rules）由访谈后确认的规则构成，T2可批量导入T5

---

## 自检声明

| # | Done Criteria | 自检结果 |
|---|---|---|
| 1 | CSV文件产出，18行×13列 | ✅ |
| 2 | signal_id唯一无重复 | ✅ |
| 3 | 所有node_id在T1范围内 | ✅ |
| 4 | rule_subtype枚举值规范 | ✅ |
| 5 | completeness枚举值规范 | ✅ |
| 6 | 新增5个子字段非空 | ✅ rule_exception含"待访谈"占位合法 |
| 7 | 字段来源标注清晰 | ✅ 全部来自v1.9 Step4 A类 |
| 8 | 数据字典格式统一 | ✅ |
| 9 | 自检声明已逐项自检 | ✅ |

---

> 产出文件路径：03_发布成果-交付物/权威数据/规则数据/T2_signals_数据字典_v2.0.md

