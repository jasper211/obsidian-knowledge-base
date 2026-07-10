---
type: project_note
project: 流程架构
layer: "02_过程成果-工作产出"
layer_tag: 过程
subdir: "校验与上下文"
tags: [过程, 校验]
---

## 🧭 导航
⬆️ [[02_过程成果-工作产出]] · ⬆️ [[校验与上下文]] · 🏠 [[流程架构项目MOC]]

---

# 数据质量报告

生成日期：2026-04-22

## 一、VS-1 至 VS-5 清洗结果

| VS | 清洗后行数 | 字段完整度 | 主要空值字段 |
|---|---|---|---|
| VS-1 | 20 | 80.0% | l1_mapping(20)、l3_mapping(20) |
| VS-2 | 45 | 70.0% | vs_description(45)、l1_mapping(45)、l3_mapping(45) |
| VS-3 | 36 | 80.0% | l1_mapping(36)、l3_mapping(36) |
| VS-4 | 27 | 80.0% | l1_mapping(27)、l3_mapping(27) |
| VS-5 | 37 | 82.4% | vs_description(37)、l3_mapping(25)、l1_mapping(3) |

## 二、fact_activity JOIN 质量

| 指标 | 值 |
|---|---|
| L3流程库原始行数 | 403 |
| Agent评分表行数 | 253 |
| Bridge表行数 | 80 |
| JOIN后总行数 | ? |
| Agent字段JOIN成功率 | 0.0% |
| 无Agent评分的行数 | ? |
| 平均字段完整度 | 67.0% |

## 三、已知数据缺口（需后续补录）

1. **VS-1 L5经营活动缺失**：VS-1的7个L3流程(IAO/IAC/IRI/IBE/IPI/IMF/IRR)在L3流程库CSV中无对应L5活动数据，需从txt框架文档中提取补录
2. **VS-5 L1/L3 mapping部分为空**：只有部分行标注了l1_mapping和l3_mapping
3. **dim_job_family字段依赖正则提取**：从Markdown提取，job_title_en/job_nature等字段匹配质量依赖原文格式规范度
4. **bridge_l4_job.responsibility_type未细化**：当前统一填'主导'，需对照RACI矩阵更新为主导/支持/监控

