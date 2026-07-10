---
type: 项目笔记
source: 02_过程成果-工作产出/岗位族设计
synced: 2026-06-15
tags: [项目]
---

# 岗位架构分析报告 · 渲染指令

> 版本: v1.0 | 2026-04-21
> 数据底座: ea_knowledge_base.db (9张表)
> 输出物: job_report_{A~G}_v2.html (7份)

---

## 一、数据表单清单与关系

### 1.1 九张数据表

| 序号 | 表名 | 行数 | 角色 | 核心字段 |
|------|------|------|------|---------|
| T1 | fact_activity | 652 | 事实表 | activity_id, l3_code, l3_name, l4_code, l4_name, l5_sequence, l5_activity, agent_tier, physical_deliverable, vs_mapping, stage_mapping |
| T2 | dim_value_stream | 168 | 维度表 | vs_id, vs_name, value_item, value_stage, value_activity, l3_mapping, stage_l3_mapping |
| T3 | dim_agent_capability | 284 | 维度表 | l3_code, l4_code, l4_name, agent_tier, automation_readiness, bottleneck_dimension, priority_for_m4, notes, physical_deliverable |
| T4 | bridge_l4_job | 80 | 桥接表 | l3_code, l4_code, value_stream, job_family_code, job_family_name, supervisor, responsibility_type |
| T5 | mapping_kpi_l3 | 235 | 映射表 | kpi_id, kpi_name, kpi_domain, l3_code, l3_name, vs_mapping, weight, contribution_logic, data_availability |
| T6 | mapping_jd_kpi_l3 | 302 | 映射表 | job_family, jd_kpi_name, enterprise_kpi_id, enterprise_kpi_name, l3_code, l3_name, vs_mapping, l3_weight, contribution_logic |
| T7 | dim_job_family | 6 | 维度表 | job_id, job_family_code, job_title_cn, job_title_en, job_level, headcount, supervisor, vs_primary, kpi_1, kpi_2, kpi_3 |
| T8 | matrix_job_m0m8 | 63 | 矩阵表 | job_family_code, dimension_code, dimension_name, score, tier, rationale |
| T9 | insight_job | 23 | 洞察表 | job_family_code, insight_type, insight_title, insight_content, severity, action_suggestion |

### 1.2 表间关系

```
dim_job_family (T7) ──1:N──> matrix_job_m0m8 (T8)     [job_family_code]
dim_job_family (T7) ──1:N──> insight_job (T9)          [job_family_code]
dim_job_family (T7) ──1:N──> bridge_l4_job (T4)        [job_family_code]
dim_job_family (T7) ──1:N──> mapping_jd_kpi_l3 (T6)    [job_family ↔ job_family]

fact_activity (T1) ──N:1──> dim_value_stream (T2)      [l3_code → l3_mapping]
fact_activity (T1) ──1:1──> dim_agent_capability (T3)   [l4_code]
fact_activity (T1) ──1:1──> bridge_l4_job (T4)          [l4_code]

mapping_kpi_l3 (T5) ──N:1──> fact_activity (T1)         [l3_code]
mapping_jd_kpi_l3 (T6) ──N:1──> mapping_kpi_l3 (T5)     [enterprise_kpi_id → kpi_id]
mapping_jd_kpi_l3 (T6) ──N:1──> fact_activity (T1)       [l3_code]
```

---

## 二、报告参数

渲染前需指定岗位族代码（job_family_code），取值范围：A/B/C/D/E/F/G

---

## 三、各章节渲染指令

### J-01 岗位战略坐标

**回答问题**: 这个岗位在公司整体战略中处于什么位置？

**数据源**: T7(dim_job_family) + T8(matrix_job_m0m8) + T4(bridge_l4_job)

**渲染逻辑**:

```
1. 读 T7 WHERE job_family_code='{族码}'
   → 岗位名称(job_title_cn/en)、等级(job_level)、编制(headcount)
   → 汇报对象(supervisor)、归属VS(vs_primary)

2. 读 T8 WHERE job_family_code='{族码}' ORDER BY score DESC
   → M0-M8评分矩阵 → 雷达图(SVG)
   → 分级标签: score=5→Core, 4→High, 3→Mid, 1~2→Low
   → rationale 作为评分说明

3. 读 T4 WHERE job_family_code='{族码}' AND responsibility_type='lead'
   → COUNT → 核心工作介入点数

4. 计算CEO减负贡献:
   → 统计 T4 WHERE job_family_code='{族码}' AND supervisor='Mark'
   → 计算总EP数 × 该族lead占比 → 减负百分比
```

**输出卡片**:
- 3个统计卡: 核心介入点数 / CEO减负项数 / 减负百分比
- M0-M8雷达图 + 9行评分条(名称+进度条+分数+等级标签)

---

### J-02 价值流穿透

**回答问题**: 这个岗位在公司业务流程中负责哪些环节？

**数据源**: T4(bridge_l4_job) + T1(fact_activity) + T2(dim_value_stream)

**渲染逻辑**:

```
1. 读 T4 WHERE job_family_code='{族码}'
   → 获取该族涉及的 value_stream 列表
   → 按 value_stream 分组

2. 读 T2 WHERE vs_id IN (该族涉及的VS)
   → 获取每个VS的阶段(value_stage)和L3映射(l3_mapping)
   → 按 vs_id + value_stage 排序

3. 读 T1 WHERE l3_code IN (该族涉及的L3) AND vs_mapping IN (该族VS)
   → 获取 L4 活动列表
   → 按 l3_code + l4_code 排序

4. 对每个VS阶段:
   → 主导L3 = T4 WHERE responsibility_type='lead' 的 l3_code
   → 支持L3 = T4 WHERE responsibility_type='support' 的 l3_code
   → EP数 = COUNT(T1的l4_code)

5. 27个关键介入点清单:
   → 读 T1 + T4 关联
   → responsibility_type=lead → 主导标签
   → responsibility_type=support → 支持标签
   → responsibility_type=watch → 监控标签
```

**输出卡片**:
- VS阶段路径条(5个阶段，点击展开L3列表)
- 阶段主导流程集中度热力图(橙色=主导, 蓝色=支持)
- EP完整清单(主导/支持/监控三色标签)

---

### J-03 工作活动清单

**回答问题**: 这个岗位每天/每周/每月具体做什么？完成之后产出什么？

**数据源**: T4(bridge_l4_job) + T1(fact_activity) + T3(dim_agent_capability)

**渲染逻辑**:

```
1. 读 T4 WHERE job_family_code='{族码}'
   → 获取该族关联的 l3_code + l4_code 列表

2. 读 T1 WHERE l4_code IN (该族L4列表)
   → 按 l3_code 分组
   → 每组内按 l4_code 排序
   → 字段: l4_code, l4_name, l5_activity, physical_deliverable, agent_tier

3. 统计:
   → 工作活动总数 = COUNT(DISTINCT l4_code)
   → 核心交付物数 = COUNT(DISTINCT physical_deliverable) WHERE physical_deliverable != ''

4. AI辅助类型映射:
   → agent_tier='Aug' → 全自动(绿色标签)
   → agent_tier='Assist' → 人机协作(蓝色标签)  
   → agent_tier='Human' → 纯人工(红色标签)
```

**输出卡片**:
- 2个统计卡: 工作活动总数 / 核心交付物数
- 按L3分组的活动表(L4编号+名称+交付物+AI类型标签)

---

### J-04 AI自动化分析

**回答问题**: 哪些可以AI做、哪些需要人机配合、哪些必须人工？

**数据源**: T3(dim_agent_capability) + T4(bridge_l4_job)

**渲染逻辑**:

```
1. 读 T3 + T4 关联 WHERE job_family_code='{族码}'
   → 按 automation_readiness 分组统计:
     - 全自动(Auto) = COUNT WHERE automation_readiness='全自动' 或 agent_tier='Aug'
     - 人机协作(Assist) = COUNT WHERE automation_readiness='人机协作' 或 agent_tier='Assist'
     - 纯人工(Human) = COUNT WHERE automation_readiness='纯人工' 或 agent_tier='Human'

2. AI可介入率 = (Auto + Assist) / Total × 100%

3. 必人工清单 = T3 WHERE agent_tier='Human' (或 automation_readiness='纯人工')
   → 展示: l4_code, l4_name, 必须人工原因(notes字段), 频率(priority_for_m4)
```

**输出卡片**:
- 3个统计卡: 全自动数/人机协作数/纯人工数(带占比)
- 必人工节点表(编号+名称+原因+频率)

---

### J-05 KPI绩效结构

**回答问题**: 这个岗位如何被考核？指标背后支撑了哪些业务目标？

**数据源**: T6(mapping_jd_kpi_l3) + T5(mapping_kpi_l3) + T7(dim_job_family)

**渲染逻辑**:

```
1. 读 T7 WHERE job_family_code='{族码}'
   → kpi_1, kpi_2, kpi_3 字段提取岗位KPI名称

2. 读 T6 WHERE job_family='{族名}' AND enterprise_kpi_id != '无直接对应'
   → 按 jd_kpi_name 分组
   → 每个岗位KPI:
     - 权重(l3_weight): 取第一条记录的权重
     - 企业级KPI穿透: GROUP_CONCAT(DISTINCT enterprise_kpi_id + enterprise_kpi_name)
     - L3流程支撑: GROUP_CONCAT(DISTINCT l3_code + l3_name)

3. 反向KPI:
   → 从JD文本中提取"不考核"或"红线"条目
   → 目前硬编码在 dim_job_family 的 kpi_1/2/3 中

4. 权重条形图:
   → 每个KPI的权重 → 进度条宽度 = 权重/100 × 100%
```

**输出卡片**:
- KPI列表(权重数字+名称+企业KPI穿透+L3流程支撑+进度条)
- 反向考核指标卡

---

### J-06 洞察与建议

**回答问题**: 岗位的结构性问题、AI替代机会、协同关系

**数据源**: T9(insight_job) + T4(bridge_l4_job) + T1(fact_activity)

**渲染逻辑**:

```
1. 读 T9 WHERE job_family_code='{族码}'
   → 按 insight_type 分组渲染:
     - core_insight → 洞察卡(橙色左边框)
     - risk → 风险卡(蓝色左边框)
     - ai_opportunity → 洞察卡(橙色左边框)
     - collab → 协同卡(绿色左边框)
     - warning → 警告卡(黄色左边框)
     - work_distribution → 统计卡

2. 工作重心诊断:
   → 读 T4 WHERE job_family_code='{族码}'
   → 判断型 = COUNT WHERE responsibility_type='lead' AND l3涉及'战略/谈判/裁定'
   → 协调型 = COUNT WHERE responsibility_type='support'
   → 执行型 = COUNT WHERE responsibility_type='watch'
   (此逻辑需根据各族实际职责细化)

3. 跨岗位协同关系:
   → 读 T4 GROUP BY job_family_code, supervisor
   → 识别本族与其他族的交叉L3/L4
   → 角色标注: lead/co-lead/collaborate
```

**输出卡片**:
- 岗位重心诊断(3个统计卡: 判断型/协调型/执行型)
- 洞察/风险/AI机会/警告卡(按severity排序)
- 跨岗位协同表(对象+场景+本族角色+对方角色)

---

### J-07 数据来源

**回答问题**: 报告数据从哪来？可信度如何？

**数据源**: 全部9张表(自动统计)

**渲染逻辑**:

```
1. 数据链路总览(固定模板+动态统计):
   层级1: 价值流定义 → COUNT(DISTINCT vs_id) FROM T2
   层级2: 价值阶段 → COUNT(*) FROM T2
   层级3: L3流程库 → COUNT(DISTINCT l3_code) FROM T1
   层级4: L4活动 → COUNT(*) FROM T1
   层级5: 交付物 → COUNT(*) FROM T3
   层级6: KPI穿透 → COUNT(*) FROM T5 + COUNT(*) FROM T6

2. 各数据层来源文件清单(固定模板):
   → 每层标注: 来源文件/数据表 + 行数 + 完成状态

3. 报告版本与下一步计划(固定模板)
```

**输出卡片**:
- 数据链路流程图(6个节点+箭头)
- 数据层来源表(层级+来源+行数+状态)
- 版本与计划表

---

## 四、更新指引

### 4.1 更新数据表单

| 变更场景 | 修改哪张表 | 级联影响 |
|---------|-----------|---------|
| L3/L4编码调整 | T1 + T3 + T4 | J-02/J-03/J-04/J-07 |
| KPI体系调整 | T5 + T6 | J-05/J-07 |
| 岗位定义调整 | T7 + T8 + T9 | J-01/J-05/J-06 |
| 价值流阶段调整 | T2 | J-02/J-07 |
| 洞察/风险更新 | T9 | J-06 |

### 4.2 渲染执行

```bash
# 更新数据后，重新渲染某族的报告
python3 render_job_report.py --family A

# 全量渲染所有7族
python3 render_job_report.py --all
```

### 4.3 数据校验规则

渲染前自动校验：
1. dim_job_family 必须有7行(A~G)
2. matrix_job_m0m8 每族必须有9行(M0~M8)
3. bridge_l4_job 每族至少有1行
4. mapping_jd_kpi_l3 每族至少有1条有企业KPI映射的记录
5. fact_activity 的 vs_mapping 不能为空
