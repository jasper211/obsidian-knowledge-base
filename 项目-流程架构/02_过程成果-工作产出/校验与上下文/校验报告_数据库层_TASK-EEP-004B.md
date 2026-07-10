---
type: 项目笔记
source: 02_过程成果-工作产出/校验与上下文
synced: 2026-06-15
tags: [项目]
---

# 质检报告：数据库层
**任务包**：TASK-EEP-004B · EA数据底座数据库层质检
**执行日期**：2026-05-09
**执行终端**：Claude Code（只读查询，无数据修改）
**溯源**：02_过程成果-工作产出/数据库/数据库_知识库_T1活跃版.db

---

## 一、数据库连接确认

| 项目 | 值 |
|------|-----|
| **数据库路径** | `/Users/zhaoqitrenda.cn/Desktop/流程架构项目_jasper/02_过程成果-工作产出/数据库/数据库_知识库_T1活跃版.db` |
| **SQLite版本** | 3.37.0 |
| **表名列表** | dim_l3 / dim_value_stream / dim_l4_activity / dim_agent_capability / dim_agent_capability_backup |

> 注：任务包指定的4张核心表全部存在，另有1张备份表 `dim_agent_capability_backup`（本次不纳入统计）。

---

## 二、各表行数摘要

| 表名 | 实际行数 | 备注 |
|------|---------|------|
| dim_l3 | **82** | L3流程编码主表 |
| dim_value_stream | **359** | 价值流活动明细表（非VS维度表，含重复vs_code） |
| dim_l4_activity | **400** | L4活动表 |
| dim_agent_capability | **400** | Agent能力评估表 |

> 注：`dim_value_stream` 实际存储的是价值流活动全量明细（359条活动记录），每条 vs_code 出现多次（如 VS-2 出现 223 次），不是仅含5行的VS维度码表。

---

## 三、dim_l3 详细摘要

### 3.1 总行数
**82条**（L3流程编码全量）

### 3.2 L1分布

| l1_code | L3数量 |
|---------|--------|
| L1-01 | 9 |
| L1-02 | 14 |
| L1-03 | 19 |
| L1-04 | 12 |
| L1-05 | 28 |
| **合计** | **82** |

### 3.3 VS分布

| vs_code | L3数量 | 说明 |
|---------|--------|------|
| （空值） | 17 | ⚠️ 无VS映射 |
| VS-1 | 7 | |
| VS-2 | 26 | |
| VS-3 | 7 | |
| VS-4 | 6 | |
| VS-5 | 19 | |
| **合计** | **82** | |

### 3.4 空值统计

| 字段 | 空值数 | 状态 |
|------|--------|------|
| l3_code | 0 | ✅ 无空值 |
| vs_code | **17** | ⚠️ 17条无VS映射 |

**vs_code为空的17条L3清单（按L1分组）**：

| l3_code | l3_name | l1_code |
|---------|---------|---------|
| L3-CAS | 竞争与获客策略制定流程 | L1-01 |
| L3-MED | 市场进入模式设计流程 | L1-01 |
| L3-MEI | 市场进入策略整合流程 | L1-01 |
| L3-MIO | 市场洞察与机会识别流程 | L1-01 |
| L3-SDSA | 市场数据分析与决策支持 | L1-01 |
| L3-SFC | 策略可行性评估与沟通流程 | L1-01 |
| L3-SPE | 战略目标与绩效体系建立流程 | L1-01 |
| L3-SRE | 战略风险评价流程 | L1-01 |
| L3-VPV | 价值主张设计与验证流程 | L1-01 |
| L3-CBD | 永明源头佣金向细分市场差异化拆解与合规验证 | L1-03 |
| L3-CMU | 永明保司佣金政策接收校准与标准化分发 | L1-03 |
| L3-COM | 佣金全链路管理 | L1-03 |
| L3-CVI | 永明与非永明佣金多源整合全链路验证与标准化外发 | L1-03 |
| L3-EO | 理财师权益分级与绩效监控 | L1-05 |
| L3-RSD | 权益方案框架设计 | L1-05 |
| L3-SLCM | 权益服务生命周期管理 | L1-05 |
| L3-SLM | 权益上市推广 | L1-05 |

> 规律：L1-01（战略类）9条中9条无VS映射，L1-03（佣金类）4条无VS映射，L1-05（权益类）4条无VS映射。

### 3.5 已知问题4条查询结果

| l3_code | l3_name | vs_code | l1_code | 状态 |
|---------|---------|---------|---------|------|
| L3-CFRM | 客户反馈与权益需求再挖掘 | VS-5 | L1-05 | ✅ VS映射存在 |
| L3-SDSA | 市场数据分析与决策支持 | （空） | L1-01 | ⚠️ **VS映射缺失** |
| L3-SPD | 服务流程配置与培训 | VS-5 | L1-05 | ✅ VS映射存在 |
| L3-SRA | 服务需求诊断与分析流程 | VS-5 | L1-05 | ✅ VS映射存在 |

> 4条中仅 **L3-SDSA** 存在vs_code缺失问题，其余3条（SRA/SPD/CFRM）均已有VS映射。

---

## 四、dim_value_stream 详细摘要

### 4.1 总行数
**359条**（价值流活动明细记录，非维度码表）

### 4.2 VS分布

| vs_code | 活动条数 |
|---------|---------|
| VS-1 | 25 |
| VS-2 | 223 |
| VS-3 | 39 |
| VS-4 | 27 |
| VS-5 | 45 |
| **合计** | **359** |

### 4.3 空值统计

| 字段 | 空值数 | 状态 |
|------|--------|------|
| vs_code | 0 | ✅ 无空值 |

> 注：`dim_value_stream` 表名与内容有歧义——实际存储的是价值流下的活动明细（含L3映射、价值阶段、活动描述），不是简单的VS维度码表（VS-1~VS-5仅5行）。Claude在使用此表做跨表关联时需注意：join条件应确认使用 `vs_code` 还是行级明细字段。

---

## 五、dim_l4_activity 详细摘要

### 5.1 总行数
**400条**

### 5.2 字段结构（实际）

| 字段名 | 类型 | 说明 |
|--------|------|------|
| l4_code | TEXT (PK) | L4编码 |
| l4_name | TEXT | L4活动名称 |
| l3_code | TEXT | 关联L3编码 |
| activity_type | TEXT | 活动类型（当前全部为空） |
| source_doc | TEXT | 来源文档 |
| source_row_ref | TEXT | 来源行参考 |
| confirmation_status | TEXT | 确认状态（默认draft） |

> ⚠️ 任务包要求查询 `agent_tier` 字段，**该字段在 dim_l4_activity 中不存在**。`agent_tier` 类信息实际存在于 `dim_agent_capability` 表的 `m2_tier` / `infer_tier` 字段中。

### 5.3 activity_type 分布

| activity_type | 数量 |
|---------------|------|
| （空值） | **400** |

> ⚠️ `activity_type` 字段全部为空，该字段尚未填充。

### 5.4 confirmation_status 分布

| confirmation_status | 数量 |
|---------------------|------|
| draft | 400 |

> 全部400条均为 `draft` 状态，尚无confirmed记录。

### 5.5 L3覆盖检查

| 指标 | 数值 |
|------|------|
| dim_l4_activity中覆盖的DISTINCT L3数 | **82** |
| dim_l3总L3数 | 82 |
| 覆盖率 | **100%** |

### 5.6 孤儿L4检查（L4的L3编码在dim_l3中不存在）

**结果：无孤儿L4** ✅

### 5.7 l4_code空值统计

| 字段 | 空值数 | 状态 |
|------|--------|------|
| l4_code | 0 | ✅ 无空值 |

---

## 六、dim_agent_capability 详细摘要

### 6.1 总行数
**400条**

### 6.2 字段结构

| 字段名 | 类型 | 说明 |
|--------|------|------|
| l4_code | TEXT (PK) | 关联L4编码 |
| deliverable | TEXT | 交付物名称 |
| deliverable_type | TEXT | 交付物类型（文档/数据/签字等） |
| agent_type | TEXT | Agent类型（Auto/Aug/Hybrid/Human） |
| m2_tier | TEXT | M2层级（与agent_type一致） |
| infer_tier | TEXT | 推导Tier |
| source_doc | TEXT | 来源文档 |
| confirmation_status | TEXT | 确认状态（默认draft） |

### 6.3 Agent Type / M2 Tier分布

| 类别 | agent_type数量 | m2_tier数量 |
|------|---------------|-------------|
| Aug | 108 | 108 |
| Auto | 77 | 77 |
| Human | 39 | 39 |
| Hybrid | 176 | 176 |
| **合计** | **400** | **400** |

> `agent_type` 与 `m2_tier` 字段数值完全一致（即两列内容相同）。

### 6.4 infer_tier分布

| infer_tier | 数量 |
|------------|------|
| Aug | 196 |
| Auto | 111 |
| Human | 39 |
| Hybrid | 54 |
| **合计** | **400** |

> `infer_tier` 与 `m2_tier` 分布存在差异（Aug: 108→196，Auto: 77→111，Hybrid: 176→54），说明推导Tier与M2 Tier存在系统性偏差，需评估哪个为权威字段。

### 6.5 confirmation_status分布

| confirmation_status | 数量 |
|---------------------|------|
| draft | 400 |

> 全部400条均为 `draft` 状态。

---

## 七、跨表一致性结果

### 7.1 dim_l3中无L4的L3编码

**结果：无** ✅

所有82条L3编码均在 `dim_l4_activity` 中有对应L4记录，L3→L4覆盖率 **100%**。

### 7.2 dim_l3中vs_code在dim_value_stream中不存在

**结果：无** ✅

dim_l3中已填写vs_code的65条记录（VS-1~VS-5），其vs_code均可在 `dim_value_stream` 中找到对应记录。

### 7.3 dim_l4_activity与dim_agent_capability的l4_code一致性（额外验证）

| 方向 | 不一致数 | 状态 |
|------|---------|------|
| dim_agent_capability中l4_code不在dim_l4_activity | 0 | ✅ |
| dim_l4_activity中l4_code不在dim_agent_capability | 0 | ✅ |

> 两表l4_code完全对齐，400:400一一对应。

---

## 八、数据库层质检结论

**一句话结论**：数据库4张核心表结构完整、编码无孤儿、跨表l4_code完全对齐，但存在3项需重点评估的质量问题。

---

### 对Claude的提示

以下问题需要Claude重点评估：

**【问题1】dim_l3.vs_code 有17条空值（占比20.7%）**
- 空值集中在 L1-01（战略类，9/9全空）、L1-03（佣金类，4条）、L1-05（权益类，4条）
- 已知问题中 **L3-SDSA** 确认为空值，其余3条（SRA/SPD/CFRM）已有映射
- 评估方向：L1-01战略类L3是否设计上就不归属任何价值流？还是映射尚未完成？

**【问题2】dim_l4_activity.activity_type 字段全部为空（400/400）**
- 任务包原始要求的 `agent_tier` 字段在此表中不存在，`agent_tier` 类信息实际在 `dim_agent_capability` 中（字段名为 `m2_tier` / `infer_tier`）
- 评估方向：`activity_type` 是否为待填充字段？是否影响后续数据使用？

**【问题3】dim_agent_capability中 `agent_type` 与 `m2_tier` 完全相同，但与 `infer_tier` 存在系统性差异**
- m2_tier vs infer_tier对比：Aug 108→196，Auto 77→111，Hybrid 176→54（Human 39不变）
- 评估方向：哪个字段为权威来源？`m2_tier` 是Mark确认值还是系统推导值？`infer_tier` 的推导逻辑是否有依据文档？

**【问题4】全部400条L4数据的 `confirmation_status` 均为 `draft`**
- dim_l4_activity 和 dim_agent_capability 各400条全部是 draft 状态
- 评估方向：是否有待推进的确认流程？draft状态数据是否已可作为质检基准？

---

## 自检声明

已对照 TASK-EEP-004B Done Criteria 逐项自检：

- [x] 4张核心表全部查询完成，行数记录（82/359/400/400）
- [x] 已知问题4条（SRA/SPD/CFRM/SDSA）查询结果输出（见第三节3.5）
- [x] Agent Tier分布统计完成（注：字段在dim_agent_capability而非dim_l4_activity，已说明）
- [x] 孤儿L4检查完成（结果：无孤儿）
- [x] 跨表一致性2项验证完成（无L4的L3：无；VS编码不一致：无）
- [x] 质检结论包含「对Claude的提示」（4项重点评估问题）
- [x] 自检声明：已对照Done Criteria逐项自检
