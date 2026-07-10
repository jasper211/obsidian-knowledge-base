---
type: 项目笔记
source: 03_发布成果-交付物/权威数据/规则数据
synced: 2026-06-15
tags: [项目]
---

# T3 · signal_leads · 数据字典

> 任务包：TASK-M4W10-102
> 产出日期：2026-06-11
> 对应CSV：T3_signal_leads_PAY域_v2.1.csv
> 来源：PAY域_价值节点信号提取基线_v1.9.md · Step4 B类·规则线索（整合v1.1地图+v4.1工具包）
> 补充来源：PAY域_第二层_访谈工具包_四岗位合一_v4.1.md · B/C路径5维度问题

---

## 字段定义

| 列号 | 字段名 | 数据类型 | 来源 | 枚举值/格式 | 说明 |
|---|---|---|---|---|---|
| 1 | lead_id | TEXT | 自编 | S3-PAY[NN]-[NNN] | 主键，B类规则线索唯一标识 |
| 2 | node_id | TEXT | v1.9 MD Step4 B类节点列 | VN-PAY-XX | 外键→T1.node_id |
| 3 | content | TEXT | v1.9 MD Step4 B类信号内容列 | 原文 | 规则线索内容 |
| 4 | source | TEXT | v1.9 MD Step4 B类来源列 | SheetX·RowX | 来源定位 |
| 5 | confidence | TEXT | v1.9 MD Step4 B类确认程度列 | 明确/推断/待确认 | 确认程度 |
| 6 | target_rule_type | TEXT | v1.9 MD Step4 B类转化后规则类型列 | 合规约束规则/计算推导规则/流程触发规则/数据结构规则 | 访谈后可能转化的规则类型 |
| 7 | interview_priority | TEXT | v1.9 MD Step4 B类访谈优先级列 | P0/P1/P2 | 访谈优先级 |
| 8 | l_layer | TEXT | v1.9 MD Step4 B类L层定位列 | L3层/L4层/数据架构层/治理层 | 架构层定位 |
| 9 | status | TEXT | 固定初始值 | 待访谈 | 处理状态 |
| 10 | gap_description | TEXT | v1.9 MD Step4 B类gap_description列 / v1.1地图E列 | 原文/待补充 | 规则空白具体描述 |
| 11 | gap_impact | TEXT | v1.9 MD Step4 B类gap_impact列 / v1.1地图E列 | 原文/待补充 | 规则空白影响 |
| 12 | expected_output | TEXT | v1.9 MD Step4 B类expected_output列 / v4.1沟通区 | 原文/待补充 | 访谈期望产出 |
| 13 | target_interviewee | TEXT | v1.9 MD Step4 B类target_interviewee列 | 岗位族/待补充 | 目标访谈对象 |
| 14 | background | TEXT | v1.9 MD Step4 B类background列 / v4.1沟通区 | 原文/待补充 | 访谈背景信息 |
| 15 | answer_format | TEXT | v1.9 MD Step4 B类answer_format列 / v4.1沟通区 | 原文/待补充 | 期望回答格式 |
| 16 | interview_result | TEXT | 固定初始值 | 待访谈 | 访谈结果 |
| 17 | converted_rule | TEXT | 固定初始值 | 待确认 | 转化后的规则ID（访谈后填写） |
| 18 | b_scope_correction | TEXT | 访谈时受访者填写 | 空字符串/原文 | 环节范围校正：实际负责范围与背景描述不符时填写 |
| 19 | b_owner_correction | TEXT | 访谈时受访者填写 | 空字符串/岗位族 | 责任归属校正：实际执行岗位与背景描述不符时填写 |
| 20 | b_trigger_correction | TEXT | 访谈时受访者填写 | 空字符串/原文 | 触发条件校正：实际触发条件与背景描述不符时填写 |
| 21 | b_output_correction | TEXT | 访谈时受访者填写 | 空字符串/原文 | 产出物校正：实际产出物与背景描述不符时填写 |
| 22 | b_validity_judgment | TEXT | 基于B路径校正后判断 | 仍然成立/需重定义/不成立/空字符串 | 原规则空白成立性判断 |
| 23 | c_existence_check | TEXT | 访谈时受访者判断 | 完全不存在/存在但形态不同/空字符串 | 环节存在性判断（C路径） |
| 24 | c_actual_owner | TEXT | 访谈时受访者填写 | 空字符串/岗位族 | 实际职责承担：类似职责目前由哪个岗位/团队承担 |
| 25 | c_actual_boundary | TEXT | 访谈时受访者填写 | 空字符串/原文 | 真实边界：实际的起点/终点/频率 |
| 26 | c_main_problem | TEXT | 访谈时受访者填写 | 空字符串/原文 | 当前最大问题：该环节目前最大的管理问题 |
| 27 | c_feedback_target | TEXT | 基于C路径分析后判断 | 价值节点清单/L3蓝图/岗位归口/其他/空字符串 | 来源反哺定位：C路径触发后问题来源指向哪里 |

---

## 枚举值规范

- **lead_id**: S3-PAY[节点后两位]-[三位序号]，例：S3-PAY02-001
- **target_rule_type**: 合规约束规则 / 计算推导规则 / 流程触发规则 / 数据结构规则
- **interview_priority**: P0 / P1 / P2
- **confidence**: 明确 / 推断 / 待确认
- **l_layer**: L3层 / L4层 / 数据架构层 / 治理层
- **status**: 待访谈（初始值，访谈后更新）
- **interview_result**: 待访谈（初始值）/ 已完成·已转化 / 已完成·未转化 / 部分转化
- **converted_rule**: 待确认（初始值）/ S2-PAYxx-xxx（转化后填写）
- **b_validity_judgment**: 仍然成立 / 需重定义 / 不成立 / 空字符串（初始值）
- **c_existence_check**: 完全不存在 / 存在但形态不同 / 空字符串（初始值）
- **c_feedback_target**: 价值节点清单 / L3蓝图 / 岗位归口 / 其他 / 空字符串（初始值）

---

## 版本记录

| 版本 | 日期 | 变更内容 |
|---|---|---|
| v1.0 | 2026-06-11 | 初始产出，11条B类规则线索，9列 |
| v2.0 | 2026-06-11 | TASK-M4W10-101：追加8个子字段列（gap_description/gap_impact/expected_output/target_interviewee/background/answer_format/interview_result/converted_rule），扩展至17列。来源从v1.8升级至v1.9（整合v1.1地图+v4.1工具包） |
| v2.1 | 2026-06-11 | TASK-M4W10-102：追加10列B/C路径访谈字段（b_scope_correction/b_owner_correction/b_trigger_correction/b_output_correction/b_validity_judgment/c_existence_check/c_actual_owner/c_actual_boundary/c_main_problem/c_feedback_target），扩展至27列。字段来源为访谈工具包v4.1的B/C路径5维度问题 |

---

## 扩展说明

### ID编号规则
lead_id = S3-PAY + 节点编号（VN-PAY-后两位）+ 三位递增序号
同一节点内按Step4 B类表格原始顺序递增

### 新增子字段说明（v2.0）
v1.9将B类规则线索与v1.1规则空白地图、v4.1访谈工具包进行了结构化整合，新增8个子字段：
- **gap_description**：规则空白/线索的具体描述（来自v1.1地图E列或v1.9内容推断）
- **gap_impact**：该空白/线索的影响描述（来自v1.1地图或v4.1工具包）
- **expected_output**：访谈后期望产出的规则内容（来自v4.1沟通区）
- **target_interviewee**：目标访谈对象岗位族
- **background**：访谈背景信息（来自v4.1沟通区）
- **answer_format**：期望的回答格式（来自v4.1沟通区）
- **interview_result**：访谈执行结果，初始为"待访谈"
- **converted_rule**：访谈后转化的规则ID，初始为"待确认"

### B类信息差异处理
- S3-PAY02-001（对应PAY-P0-002）有完整访谈工具包卡片，gap_impact来自v1.1地图，background/expected_output/answer_format来自v4.1沟通区
- 其余10条熔断节点B类因未进入访谈流程，gap_impact/background/expected_output/answer_format/target_interviewee填「待补充（熔断节点补建后）」
- 所有B类的interview_result初始为「待访谈」，converted_rule初始为「待确认」

### 与T2/T5的关系
- T3是待访谈确认的规则线索
- 访谈确认后可升级为T2（已确立规则）或T5（规则库）
- converted_rule字段记录转化后的T2/T5信号ID
- status字段随访谈流程推进更新

### B/C路径访谈字段说明（v2.1新增）
v2.1将访谈工具包v4.1中的B/C路径5维度问题固化为数据字段，供访谈时实时记录受访者反馈。

**B路径字段（情况B：部分准确）**
当受访者表示「背景基本对，但某些细节有偏差」时，记录5个维度的校正信息：
- **b_scope_correction**：实际负责范围与背景描述不符的内容
- **b_owner_correction**：实际执行岗位与背景描述不符的内容
- **b_trigger_correction**：实际触发条件与背景描述不符的内容
- **b_output_correction**：实际产出物与背景描述不符的内容
- **b_validity_judgment**：基于上述校正后，判断原规则空白是否仍然成立

**C路径字段（情况C：完全失真）**
当受访者表示「背景描述完全不对，这个环节不是这样」时，记录5个维度的重新定位信息：
- **c_existence_check**：该环节是否存在的判断（完全不存在 / 存在但形态不同）
- **c_actual_owner**：类似职责目前实际由哪个岗位/团队承担
- **c_actual_boundary**：若环节存在，实际的起点/终点/频率
- **c_main_problem**：该环节目前最大的管理问题
- **c_feedback_target**：C路径触发后，问题来源应反哺到价值节点清单/L3蓝图/岗位归口/其他

### 初始值策略
- B/C路径10个字段初始值均为**空字符串**（非null、非「待访谈」）
- 访谈时由受访者/记录人根据实际B/C路径选择填写对应字段
- 未触发B/C路径的访谈，保持空字符串

---

## 自检声明

| # | Done Criteria | 自检结果 |
|---|---|---|
| 1 | CSV文件产出，11行×17列 | ✅ |
| 2 | lead_id唯一无重复 | ✅ |
| 3 | 所有node_id在T1范围内 | ✅ |
| 4 | status全部=待访谈 | ✅ |
| 5 | interview_priority枚举值规范 | ✅ P0×7 / P1×4 |
| 6 | target_rule_type枚举值规范 | ✅ |
| 7 | 新增8个子字段已填充 | ✅ 含「待补充（熔断节点补建后）」「待访谈」「待确认」占位合法 |
| 8 | 字段来源标注清晰 | ✅ v1.9整合v1.1+v4.1 |
| 9 | 数据字典格式统一 | ✅ |
| 10 | 新增10列全部为空字符串 | ✅ 非null非待访谈 |
| 11 | 原有17列内容未改动 | ✅ |
| 12 | B/C路径字段枚举值规范 | ✅ b_validity_judgment/c_existence_check/c_feedback_target |
| 13 | 数据字典格式统一 | ✅ |
| 14 | 自检声明已逐项自检 | ✅ |

---

> 产出文件路径：03_发布成果-交付物/权威数据/规则数据/T3_signal_leads_数据字典_v2.1.md
