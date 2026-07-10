---
type: 项目笔记
source: 02_过程成果-工作产出/_归档
synced: 2026-06-15
tags: [项目]
---

# A族数据分布报告

执行日期：2026-04-22

---

## 一、总览

| 项目 | 数量 |
|---|---|
| A族活动总行数（fact_activity JOIN bridge_l4_job） | 8 |
| 来自 L3流程库（有l5_activity） | 0 |
| 来自 Agent评分（有agent_score_total） | 8 |
| 两者均有数据的 L3 数量 | 0 |

## 二、来自 L3流程库 的 A族活动

（字段：l3_code / l3_name / l4_code / l4_name / l5_activity）

_无数据_

## 三、来自 Agent评分 的 A族活动

（字段：l3_code / l3_name / l4_code / l4_name / agent_tier / agent_score_total / D1~D6）

| l3_code   | l3_name     | l4_code   | l4_name       | agent_tier   |   agent_score_total |
|:----------|:------------|:----------|:--------------|:-------------|--------------------:|
| L3-IMF    | 保司市场反馈与数据回流 | L4-01     | 数据采集与质量校验     | Auto         |                  16 |
| L3-IMF    | 保司市场反馈与数据回流 | L4-02     | 分析模型运行与洞察     | Auto         |                  16 |
| L3-IMF    | 保司市场反馈与数据回流 | L4-06     | 实时数据接入看板      | Auto         |                  16 |
| L3-IMF    | 保司市场反馈与数据回流 | L4-09     | 预测分析          | Auto         |                  16 |
| L3-IMF    | 保司市场反馈与数据回流 | L4-10     | 异常事件紧急通报      | Auto         |                  16 |
| L3-IMF    | 保司市场反馈与数据回流 | L4-11     | 数据安全与监管合规     | Auto         |                  16 |
| L3-MSE    | 策略执行与评估     | KN6       | 持续战略执行追踪(持续型) | Auto         |                  15 |
| L3-MSI    | 市场洞察与策略设计   | KN6       | 竞品动态监控(持续型)   | Auto         |                  16 |

## 四、L3 级关联分析

| 类别 | L3编码列表 |
|---|---|
| 仅在流程库中出现 | （无） |
| 仅在Agent评分中出现 | L3-IMF, L3-MSE, L3-MSI |
| 两表均有 | （无） |

### 说明

- A族（保司资源投放 VS-1）的 L3 节点主要来自 **Agent评分** 表（L3-IAO/IAC/IPI/IMF/IRR 等），因为这些流程尚未录入 L3流程库 CSV。
- L3流程库 覆盖 KA上架/经代/权益 类 L3，与 A族 JD 存在交叉（通过 bridge_l4_job 桥接）。
- 两表 L3 无重叠时，Query3（Value Stream ↔ fact_activity）需依赖 l3_mapping 字段而非直接 JOIN。

## 五、A族 L3 分布（行数统计）

| l3_code   | l3_name     | data_source   |   行数 |
|:----------|:------------|:--------------|-----:|
| L3-IMF    | 保司市场反馈与数据回流 | Agent评分       |    6 |
| L3-MSE    | 策略执行与评估     | Agent评分       |    1 |
| L3-MSI    | 市场洞察与策略设计   | Agent评分       |    1 |

## 六、A族 Agent Tier 分布

| agent_tier   |   行数 |
|:-------------|-----:|
| Auto         |    8 |

---

*本报告由 Claude Code 自动生成（Phase 4-3），数据来源：ea_knowledge_base.db*
