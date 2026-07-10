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

# T4 · actions · 数据字典

> 任务包：TASK-M4W10-095
> 产出日期：2026-06-11
> 对应CSV：T4_actions_PAY域_v1.0.csv
> 来源：PAY域_价值节点信号提取基线_v1.8.md · Step4 C类·行动项 / 补建清单v1.1 · 熔断补建专项

---

## 字段定义

| 列号 | 字段名 | 数据类型 | 来源 | 枚举值/格式 | 说明 |
|---|---|---|---|---|---|
| 1 | action_id | TEXT | 自编 | S4-PAY[NN]-[NNN] | 主键，C类行动项唯一标识 |
| 2 | node_id | TEXT | v1.8 MD Step4 C类节点列 | VN-PAY-XX | 外键→T1.node_id |
| 3 | content | TEXT | v1.8 MD Step4 C类信号内容列 / 补建清单v1.1 | 原文 | 行动项内容 |
| 4 | source | TEXT | v1.8 MD Step4 C类来源列 / 补建清单v1.1 | SheetX·RowX / 补建清单v1.1·[节点] | 来源定位 |
| 5 | confidence | TEXT | v1.8 MD Step4 C类确认程度列 | 明确/推断/待确认 | 确认程度，待建项填「明确」 |
| 6 | action_subtype | TEXT | v1.8 MD Step4 C类行动子类列 / 按内容判断 | 公司行动/部门行动/岗位行动 | 行动层级分类 |
| 7 | generates_rule | TEXT | v1.8 MD Step4 C类完成后产生规则列 / 按内容判断 | 合规约束规则/计算推导规则/流程触发规则/数据结构规则 | 行动完成后产生的规则类型 |
| 8 | l_layer | TEXT | v1.8 MD Step4 C类L层定位列 / 按内容判断 | L3层/L4层/数据架构层/治理层 | 架构层定位 |
| 9 | mark_decision | TEXT | 根据action_subtype自动判断 | 是/否 | 公司行动=是，其余=否 |
| 10 | status | TEXT | 固定初始值 | 待执行 | 执行状态 |
| 11 | source_type | TEXT | 固定分类 | v1.8原有 / 熔断补建专项 | 区分两类来源：v1.8 Step4 C类原始信号 vs 熔断节点补建清单追加 |

---

## 枚举值规范

- **action_id**: S4-PAY[节点后两位]-[三位序号]，例：S4-PAY01-001
- **action_subtype**: 公司行动 / 部门行动 / 岗位行动
- **generates_rule**: 合规约束规则 / 计算推导规则 / 流程触发规则 / 数据结构规则
- **mark_decision**: 是（公司行动） / 否（部门行动/岗位行动）
- **confidence**: 明确 / 推断 / 待确认
- **l_layer**: L3层 / L4层 / 数据架构层 / 治理层
- **status**: 待执行（初始值，执行后更新）
- **source_type**: v1.8原有 / 熔断补建专项

---

## 版本记录

| 版本 | 日期 | 变更内容 |
|---|---|---|
| v1.0 | 2026-06-11 | 初始产出，20条C类行动项（v1.8 Step4）；新增source_type字段；追加10条熔断补建专项 |

---

## 扩展说明

### ID编号规则
action_id = S4-PAY + 节点编号（VN-PAY-后两位）+ 三位递增序号
同一节点内按Step4 C类表格原始顺序递增，熔断补建专项接续同节点最大编号

### mark_decision判断规则
| action_subtype | mark_decision |
|---|---|
| 公司行动 | 是 |
| 部门行动 | 否 |
| 岗位行动 | 否 |

### source_type分布
| 类型 | 数量 | 说明 |
|---|---|---|
| v1.8原有 | 20条 | 来自v1.8 Step4 C类原始调研信号 |
| 熔断补建专项 | 10条 | 来自熔断节点补建清单v1.1的细化行动 |

### 与T2/T5/T8的关系
- T4是建设和补建工作
- 行动执行完成后可能产生新的规则，进入T2或T5
- generates_rule字段标识行动完成后预期产出的规则类型
- 公司行动（mark_decision=是）同时关联T8·decisions的裁定事项

---

## 自检声明

| # | Done Criteria | 自检结果 |
|---|---|---|
| 1 | CSV文件产出，30行×11列 | ✅ 20条v1.8原有 + 10条熔断补建专项 |
| 2 | action_id唯一无重复 | ✅ |
| 3 | 所有node_id在T1范围内 | ✅ 覆盖VN-PAY-01~09 |
| 4 | status全部=待执行 | ✅ |
| 5 | mark_decision判断正确 | ✅ 公司行动×6→是，部门行动×22→否，岗位行动×2→否 |
| 6 | action_subtype枚举值规范 | ✅ |
| 7 | generates_rule枚举值规范 | ✅ |
| 8 | source_type分类正确 | ✅ 20条v1.8原有 + 10条熔断补建专项 |
| 9 | 字段来源标注清晰 | ✅ v1.8原有+补建清单v1.1 |
| 10 | 数据字典格式统一 | ✅ |
| 11 | 自检声明已逐项自检 | ✅ |

---

> 产出文件路径：03_发布成果-交付物/权威数据/规则数据/T4_actions_数据字典_v1.0.md

