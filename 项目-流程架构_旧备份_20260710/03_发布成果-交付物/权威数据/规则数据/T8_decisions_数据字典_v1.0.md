---
type: 项目笔记
source: 03_发布成果-交付物/权威数据/规则数据
synced: 2026-06-15
tags: [项目]
---

# T8 · decisions · 数据字典

> 任务包：TASK-M4W10-099
> 产出日期：2026-06-11
> 对应CSV：T8_decisions_PAY域_v1.0.csv
> 来源：PAY域_熔断节点_补建清单+裁定工具包_v1.1.md

---

## 字段定义

| 列号 | 字段名 | 数据类型 | 来源 | 枚举值/格式 | 说明 |
|---|---|---|---|---|---|
| 1 | decision_id | TEXT | 自编 | D8-PAY[NN]-[NNN] | 主键，Mark裁定事项唯一标识 |
| 2 | node_id | TEXT | 裁定事项关联节点 | VN-PAY-XX | 外键→T1.node_id，标识该裁定所属熔断节点 |
| 3 | action_id | TEXT | 关联T4行动项 | S4-PAY[NN]-[NNN] / null | 有对应C类行动项时填S4编号，无对应填null |
| 4 | question | TEXT | 裁定事项标题摘要 | 1句话描述 | Mark需要裁定的核心问题 |
| 5 | options | TEXT | 裁定事项【选项】 | A.选项1,B.选项2,C.选项3 | 所有可选方案，逗号分隔 |
| 6 | recommend | TEXT | 裁定事项【推荐】 | A/B/C | 分析师推荐的选项编号 |
| 7 | recommend_reason | TEXT | 裁定事项【理由】 | 1-2句原文 | 推荐理由摘要 |
| 8 | risk_note | TEXT | 裁定事项【风险提示】 | 1-2句原文 | 各选项风险摘要 |
| 9 | status | TEXT | 固定初始值 | 待裁定 | 裁定状态：待裁定→已裁定 |
| 10 | result | TEXT | Mark拍板后填入 | A/B/C / null | 最终裁定结果，初始null |
| 11 | decided_by | TEXT | Mark拍板后填入 | Mark / null | 裁定人，初始null |
| 12 | decided_date | TEXT | Mark拍板后填入 | YYYY-MM-DD / null | 裁定日期，初始null |

---

## 枚举值规范

- **decision_id**: D8-PAY[节点后两位]-[三位序号]，例：D8-PAY04-001
- **node_id**: VN-PAY-04 / VN-PAY-06 / VN-PAY-08 / VN-PAY-09（仅限熔断节点）
- **action_id**: S4-PAYxx-xxx（有对应C类时）/ null（无对应时）
- **recommend**: A / B / C
- **result**: A / B / C / null（待裁定）
- **status**: 待裁定（初始） / 已裁定
- **decided_by**: Mark / null

---

## 版本记录

| 版本 | 日期 | 变更内容 |
|---|---|---|
| v1.0 | 2026-06-11 | 初始产出，7项Mark裁定事项，来自熔断节点补建清单+裁定工具包v1.1 |

---

## 扩展说明

### ID编号规则
decision_id = D8-PAY + 节点编号（VN-PAY-后两位）+ 三位递增序号
同一节点内按裁定事项原始顺序递增

### 7项裁定事项对应关系
| 裁定事项 | decision_id | node_id | action_id | 问题 |
|---|---|---|---|---|
| 01 IA合规负责人 | D8-PAY04-001 | VN-PAY-04 | S4-PAY04-002 | IA合规负责人归属 |
| 02 FPG-05归属 | D8-PAY06-001 | VN-PAY-06 | S4-PAY06-002 | 协议参数中心化归属 |
| 03 报销SaaS选型 | D8-PAY08-001 | VN-PAY-08 | null | 报销数字化方案选型 |
| 04 P1后置确认 | D8-PAY08-002 | VN-PAY-08 | null | 报销节点优先级确认 |
| 05 37.2M归口 | D8-PAY09-001 | VN-PAY-09 | S4-PAY09-002 | 体系外资金归口部门 |
| 06 建表方案 | D8-PAY09-002 | VN-PAY-09 | S4-PAY09-003 | fact_offsystem_flow建表方案 |
| 07 历史补录优先级 | D8-PAY09-003 | VN-PAY-09 | null | 历史数据补录优先级 |

### 与T4的关系
- action_id字段建立T8→T4的引用关系
- 有对应C类的裁定事项（01/02/05/06）可直接关联T4行动项
- 无对应C类的裁定事项（03/04/07）action_id填null，待T4补录后更新

### 与T1的关系
- node_id字段建立T8→T1的引用关系
- 仅限熔断节点（VN-PAY-04/06/08/09）

---

## 自检声明

| # | Done Criteria | 自检结果 |
|---|---|---|
| 1 | CSV文件产出，7行×12列 | ✅ |
| 2 | decision_id唯一无重复 | ✅ |
| 3 | 所有node_id在T1熔断节点范围内 | ✅ VN-PAY-04/06/08/09 |
| 4 | status全部=待裁定 | ✅ |
| 5 | result/decided_by/decided_date全部=null | ✅ |
| 6 | action_id：有对应填S4，无对应填null | ✅ 4条有S4，3条null |
| 7 | recommend枚举值规范 | ✅ A/B/C |
| 8 | 字段来源标注清晰 | ✅ 全部来自裁定工具包v1.1 |
| 9 | 数据字典格式统一 | ✅ |
| 10 | 自检声明已逐项自检 | ✅ |

---

> 产出文件路径：03_发布成果-交付物/权威数据/规则数据/T8_decisions_数据字典_v1.0.md
