---
type: 项目笔记
source: 03_发布成果-交付物/权威数据/规则数据
synced: 2026-06-15
tags: [项目]
---

# T3 · signal_leads · 数据字典

> 任务包：TASK-M4W10-105
> 产出日期：2026-06-12
> 对应CSV：T3_signal_leads_PAY域_v3.0.csv
> 来源：PAY域_价值节点信号提取基线_v1.9.md · Step4 B类·规则线索（整合v1.1地图+v4.1工具包）
> 补充来源1：PAY域_第二层_访谈工具包_四岗位合一_v4.1.md · B/C路径5维度问题
> 补充来源2：T2_signals_PAY域_v2.0.md · 重分类移入的16条规则草稿

---

## 字段定义

| 列号 | 字段名 | 数据类型 | 来源 | 枚举值/格式 | 说明 |
|---|---|---|---|---|---|
| 1 | lead_id | TEXT | 自编 | S3-PAY[NN]-[NNN] | 主键，B类规则线索唯一标识 |
| 2 | node_id | TEXT | v1.9 MD Step4 B类节点列 / T2重分类 | VN-PAY-XX | 外键→T1.node_id |
| 3 | content | TEXT | v1.9 MD Step4 B类信号内容列 / T2重分类 | 原文 | 规则线索内容 |
| 4 | source | TEXT | v1.9 MD Step4 B类来源列 / T2重分类 | SheetX·RowX | 来源定位 |
| 5 | confidence | TEXT | v1.9 MD Step4 B类确认程度列 / T2重分类 | 明确/推断/待确认 | 确认程度 |
| 6 | target_rule_type | TEXT | v1.9 MD Step4 B类转化后规则类型列 / T2.rule_subtype | 合规约束规则/计算推导规则/流程触发规则/数据结构规则 | 访谈后可能转化的规则类型 |
| 7 | interview_priority | TEXT | v1.9 MD Step4 B类访谈优先级列 / 按l_layer推断 | P0/P1/P2 | 访谈优先级 |
| 8 | l_layer | TEXT | v1.9 MD Step4 B类L层定位列 / T2重分类 | L3层/L4层/数据架构层/治理层 | 架构层定位 |
| 9 | status | TEXT | 固定初始值 | 待访谈 | 处理状态 |
| 10 | gap_description | TEXT | v1.9 MD Step4 B类gap_description列 / T2.content原文 | 原文/待补充 | 规则空白具体描述 |
| 11 | gap_impact | TEXT | v1.9 MD Step4 B类gap_impact列 / 基于T2内容推断 | 原文/待补充 | 规则空白影响 |
| 12 | expected_output | TEXT | v1.9 MD Step4 B类expected_output列 / 基于T2缺失字段推断 | 原文/待补充 | 访谈期望产出 |
| 13 | target_interviewee | TEXT | v1.9 MD Step4 B类target_interviewee列 / T2.rule_owner | 岗位族/待补充 | 目标访谈对象 |
| 14 | background | TEXT | v1.9 MD Step4 B类background列 / v4.1沟通区 / 基于T2已知字段组织 | 原文/待补充 | 访谈背景信息 |
| 15 | answer_format | TEXT | v1.9 MD Step4 B类answer_format列 / v4.1沟通区 / 按target_rule_type推断 | 原文/待补充 | 期望回答格式 |
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
| v3.0 | 2026-06-12 | TASK-M4W10-105：T2重分类移入16条规则草稿。原T2 v2.0中不符合严格A类定义的16条（completeness≠完整或子字段含「待访谈」占位符）全部归入T3，作为B类规则线索等待访谈补全。T3从11行扩展至27行 |

---

## 扩展说明

### ID编号规则
lead_id = S3-PAY + 节点编号（VN-PAY-后两位）+ 三位递增序号
同一节点内按Step4 B类表格原始顺序递增，重分类移入条目接续同节点最大编号

### T3构成（v3.0）
| 来源 | 数量 | 说明 |
|---|---|---|
| 原T3 v2.1（Step4 B类） | 11条 | 来自v1.9 Step4 B类表格，保留不变 |
| T2 v2.0重分类移入 | 16条 | 原T2中不符合v3.2严格A类定义的条目，降级为B类规则线索 |
| **合计** | **27条** | — |

### 重分类移入16条的字段生成规则
对于从T2移入的16条规则草稿，T3字段按以下规则填充：

| T3字段 | 生成规则 |
|---|---|
| lead_id | 按node_id分组，接续该节点当前最大序号 |
| node_id/content/source/confidence/l_layer | 直接从T2对应字段继承 |
| target_rule_type | 直接继承T2的rule_subtype |
| interview_priority | 按l_layer推断：治理层→P0，数据架构层/L4层→P1，L3层→P2 |
| gap_description | 直接复制T2的content原文 |
| gap_impact | 基于T2 content推断：「[content]尚未完整定义，导致[执行风险/问题]」 |
| expected_output | 基于T2缺失子字段推断：「补全[缺失字段]，明确[具体标准内容]」 |
| target_interviewee | 继承T2的rule_owner |
| background | 基于T2已知子字段组织：「目前[rule_action]已在执行（执行岗位：[rule_owner]），但[缺失标准]尚未有明确标准」 |
| answer_format | 按target_rule_type推断：数据结构规则→格式2+数据框，流程触发规则→格式3+流程框，计算推导规则→格式3+计算框，合规约束规则→格式2+合规框 |
| interview_result/converted_rule/status | 固定填「待访谈」/「待访谈」/「待访谈」 |
| B/C路径10个字段 | 全部填空字符串 |

### 重分类移入16条清单
| 新lead_id | 来源signal_id | node_id | target_rule_type | interview_priority |
|---|---|---|---|---|
| S3-PAY01-001 | S2-PAY01-001 | VN-PAY-01 | 数据结构规则 | P1 |
| S3-PAY01-002 | S2-PAY01-002 | VN-PAY-01 | 数据结构规则 | P1 |
| S3-PAY02-002 | S2-PAY02-001 | VN-PAY-02 | 数据结构规则 | P1 |
| S3-PAY02-003 | S2-PAY02-002 | VN-PAY-02 | 数据结构规则 | P1 |
| S3-PAY02-004 | S2-PAY02-003 | VN-PAY-02 | 流程触发规则 | P2 |
| S3-PAY03-001 | S2-PAY03-001 | VN-PAY-03 | 数据结构规则 | P1 |
| S3-PAY03-002 | S2-PAY03-002 | VN-PAY-03 | 数据结构规则 | P1 |
| S3-PAY03-003 | S2-PAY03-003 | VN-PAY-03 | 数据结构规则 | P1 |
| S3-PAY04-004 | S2-PAY04-003 | VN-PAY-04 | 数据结构规则 | P1 |
| S3-PAY05-002 | S2-PAY05-001 | VN-PAY-05 | 数据结构规则 | P1 |
| S3-PAY05-003 | S2-PAY05-002 | VN-PAY-05 | 数据结构规则 | P1 |
| S3-PAY06-002 | S2-PAY06-001 | VN-PAY-06 | 数据结构规则 | P1 |
| S3-PAY06-003 | S2-PAY06-002 | VN-PAY-06 | 数据结构规则 | P1 |
| S3-PAY07-001 | S2-PAY07-001 | VN-PAY-07 | 数据结构规则 | P1 |
| S3-PAY08-003 | S2-PAY08-001 | VN-PAY-08 | 流程触发规则 | P0 |
| S3-PAY08-004 | S2-PAY08-002 | VN-PAY-08 | 数据结构规则 | P1 |

### B类信息差异处理
- S3-PAY02-001（对应PAY-P0-002）有完整访谈工具包卡片，gap_impact来自v1.1地图，background/expected_output/answer_format来自v4.1沟通区
- 其余原10条B类因未进入访谈流程，相关字段填「待补充（熔断节点补建后）」
- 新增16条从T2重分类移入，gap_impact/background/expected_output按上述推断规则生成，answer_format按target_rule_type推断

### 与T2/T5的关系
- T3是待访谈确认的规则线索
- 访谈确认后可升级为T2（已确立规则）或T5（规则库）
- converted_rule字段记录转化后的T2/T5信号ID
- status字段随访谈流程推进更新
- v3.0新增的16条来自T2降级，访谈补全后可能重新升入T2或进入T5

---

## 自检声明

| # | Done Criteria | 自检结果 |
|---|---|---|
| 1 | CSV文件产出，27行×27列 | ✅ 原11条 + 新增16条 |
| 2 | lead_id唯一无重复 | ✅ |
| 3 | 所有node_id在T1范围内 | ✅ |
| 4 | 原11条T3内容未改动 | ✅ |
| 5 | 新增16条lead_id格式正确 | ✅ S3-PAY[NN]-[NNN] |
| 6 | 新增16条node_id/content/source/confidence/l_layer继承自T2 | ✅ |
| 7 | 新增16条target_rule_type来自原T2 rule_subtype | ✅ |
| 8 | 新增16条gap_description=原T2 content | ✅ |
| 9 | 新增16条gap_impact有实质内容 | ✅ 基于content推断 |
| 10 | 新增16条expected_output有实质内容 | ✅ 基于缺失字段推断 |
| 11 | 新增16条background有实质内容 | ✅ 基于已知字段组织 |
| 12 | 新增16条answer_format格式规范 | ✅ 格式X+YYY框 |
| 13 | 新增16条interview_result=待访谈/converted_rule=待访谈/status=待访谈 | ✅ |
| 14 | 新增16条B/C路径10字段=空字符串 | ✅ |
| 15 | 字段来源标注清晰 | ✅ v1.9 Step4 B类 + T2重分类 |
| 16 | 数据字典格式统一 | ✅ |
| 17 | 自检声明已逐项自检 | ✅ |

---

> 产出文件路径：03_发布成果-交付物/权威数据/规则数据/T3_signal_leads_数据字典_v3.0.md
