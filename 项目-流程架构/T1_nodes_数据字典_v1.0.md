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

# T1 · nodes · 数据字典

> 任务包：TASK-M4W10-093-R1
> 产出日期：2026-06-10
> 对应CSV：T1_nodes_PAY域_v1.0.csv
> 输入材料：
> - D1_价值节点清单_V3.0.xlsx（主数据）
> - PAY域_价值节点信号提取基线_v1.8.md（补充字段）

---

## 字段定义

| 列号 | 字段名 | 数据类型 | 来源 | 枚举值/格式 | 说明 |
|---|---|---|---|---|---|
| 1 | node_id | TEXT | Excel Sheet1·节点ID列 | VN-PAY-XX | 主键，不可重复 |
| 2 | domain | TEXT | 固定值 | PAY | 本次全部填PAY，未来IBRD/FIN/EFA域另行产出 |
| 3 | value_stream | TEXT | Excel Sheet1·L3端到端闭环列 | 原文 | L3端到端闭环名称 |
| 4 | node_name | TEXT | Excel Sheet1·价值节点(物理资产)列 | 原文 | 节点的完整名称 |
| 5 | start_point | TEXT | Excel Sheet1·起点A→终点Z列（取起点） | 原文 | 起点A描述 |
| 6 | end_point | TEXT | Excel Sheet1·起点A→终点Z列（取终点） | 原文 | 终点Z描述，即ideal_state |
| 7 | frequency | TEXT | Excel Sheet2·频次行 | 如 季×1+月×1 | 执行频次 |
| 8 | gate_status | TEXT | Excel Sheet3·综合判定列 | pass / fused / force_fused | 🟢通过→pass / 🔴熔断→fused / 🔴强制熔断→force_fused |
| 9 | gate_1 | TEXT | Excel Sheet3·Gate①挂数列 | PASS / PARTIAL / FAIL | Gate①挂数评级 |
| 10 | gate_2 | TEXT | Excel Sheet3·Gate②落地列 | PASS / PARTIAL / FAIL | Gate②落地评级 |
| 11 | gate_3 | TEXT | Excel Sheet3·Gate③追溯列 | PASS / PARTIAL / FAIL | Gate③追溯评级 |
| 12 | priority | TEXT | Excel Sheet1·优先级列 | P0 / P1 / P0熔断 / P1熔断 / P0强制熔断 | 节点优先级 |
| 13 | m_anchors | TEXT | Excel Sheet4·M0-M8锚定矩阵 | M0,M7,M8（逗号分隔，无空格） | ●标记的M编号 |
| 14 | kpi_anchors | TEXT | Excel Sheet1·KPI锚定列 | KPI#15,KPI#16 | 该节点锚定的KPI编号，未定义时填null |
| 15 | strategic_note | TEXT | Excel Sheet2·业务定位/价值属性 + v1.8 MD Step3信号7 | 1-2句话 | 战略意义说明，优先取Excel，不足时从MD补充 |
| 16 | ideal_state | TEXT | Excel Sheet1·终点Z | 原文 | 完整的理想产出描述 |
| 17 | current_state | TEXT | v1.8 MD Step3信号3·Gate状态说明 | 1-2句话 | 当前执行现状总结，MD贡献字段 |
| 18 | fused_info_summary | TEXT | Excel Sheet5·熔断原因/致命缺口 | 1句话摘要 | 仅熔断节点填写，非熔断填null |
| 19 | version | TEXT | 固定值 | v1.8 | 对应的信号提取基线版本 |
| 20 | last_updated | TEXT | 固定值 | YYYY-MM-DD | 本次产出日期 |

---

## 数据来源明细

| node_id | Sheet1行号 | Sheet2行号 | Sheet3行号 | Sheet4行号 | Sheet5行号 | MD信号3 | MD信号7 |
|---|---|---|---|---|---|---|---|
| VN-PAY-01 | Sheet1·Row5 | Sheet2·Row3-23 | Sheet3·Row5 | Sheet4·Row5 | null | v1.8 MD Step3·信号3 | v1.8 MD Step3·信号7 |
| VN-PAY-02 | Sheet1·Row6 | Sheet2·Row25-45 | Sheet3·Row6 | Sheet4·Row6 | null | v1.8 MD Step3·信号3 | v1.8 MD Step3·信号7 |
| VN-PAY-03 | Sheet1·Row7 | Sheet2·Row47-67 | Sheet3·Row7 | Sheet4·Row7 | null | v1.8 MD Step3·信号3 | v1.8 MD Step3·信号7 |
| VN-PAY-04 | Sheet1·Row8 | Sheet2·Row69-89 | Sheet3·Row8 | Sheet4·Row8 | Sheet5·Row5 | v1.8 MD Step3·信号3 | v1.8 MD Step3·信号7 |
| VN-PAY-05 | Sheet1·Row9 | Sheet2·Row91-111 | Sheet3·Row9 | Sheet4·Row9 | null | v1.8 MD Step3·信号3 | v1.8 MD Step3·信号7 |
| VN-PAY-06 | Sheet1·Row10 | Sheet2·Row113-133 | Sheet3·Row10 | Sheet4·Row10 | Sheet5·Row6 | v1.8 MD Step3·信号3 | v1.8 MD Step3·信号7 |
| VN-PAY-07 | Sheet1·Row11 | Sheet2·Row135-155 | Sheet3·Row11 | Sheet4·Row11 | null | v1.8 MD Step3·信号3 | v1.8 MD Step3·信号7 |
| VN-PAY-08 | Sheet1·Row12 | Sheet2·Row157-177 | Sheet3·Row12 | Sheet4·Row12 | Sheet5·Row7 | v1.8 MD Step3·信号3 | v1.8 MD Step3·信号7 |
| VN-PAY-09 | Sheet1·Row13 | Sheet2·Row179-199 | Sheet3·Row13 | Sheet4·Row13 | Sheet5·Row8 | v1.8 MD Step3·信号3 | v1.8 MD Step3·信号7 |

---

## 版本记录

| 版本 | 日期 | 变更内容 |
|---|---|---|
| v1.0 | 2026-06-10 | 初始产出，9个PAY域节点，基于价值节点清单V3.0.xlsx + v1.8 MD补充字段 |

---

## 扩展说明

### 新域加入规则
- 新域（如IBRD/FIN/EFA）加入时：新增对应域的CSV行，追加合并至本文件
- domain字段填写对应域编码
- node_id编码前缀跟随域变化（如VN-IBRD-XX）

### 字段修改规则
| 列范围 | 来源 | 修改权限 |
|---|---|---|
| 列1-16（Excel来源） | 价值节点清单V3.0.xlsx | **只有Mark改清单才能改** |
| 列17-18（MD来源） | v1.8+ MD迭代 | 随访谈迭代更新 |
| 列19-20（版本信息） | 固定值 | 每次更新时修改 |

### gate_status映射规则
| Excel原文 | CSV值 | 适用节点 |
|---|---|---|
| 🟢通过 | pass | VN-PAY-01/02/03/05/07 |
| 🔴熔断 | fused | VN-PAY-04/06/08 |
| 🔴强制熔断 | force_fused | VN-PAY-09 |

### 枚举值规范
- **gate_status**: pass, fused, force_fused
- **gate_1/2/3**: PASS, PARTIAL, FAIL（全大写）
- **priority**: P0, P1, P0熔断, P1熔断, P0强制熔断
- **m_anchors**: 逗号分隔，无空格，按M0→M8顺序排列
- **kpi_anchors**: 逗号分隔，无空格，保留KPI#前缀；未定义时填null
- **fused_info_summary**: 非熔断节点必须填null，不可留空

---

## 自检声明

| # | Done Criteria | 自检结果 |
|---|---|---|
| 1 | CSV文件产出，9行×20列 | ✅ 9行数据+标题行 |
| 2 | 所有Excel来源字段（列1-16）均有明确的Sheet+行号标注 | ✅ 已在数据字典"数据来源明细"表中标注 |
| 3 | gate_status枚举值正确映射 | ✅ pass×5 / fused×3 / force_fused×1 |
| 4 | gate_1/2/3枚举值正确 | ✅ PASS/PARTIAL/FAIL全大写 |
| 5 | m_anchors格式正确 | ✅ 逗号分隔，无空格 |
| 6 | kpi_anchors格式正确 | ✅ 逗号分隔，保留KPI#前缀 |
| 7 | current_state通过节点1-2句总结，熔断节点填「熔断·[核心原因]」 | ✅ 通过节点1-2句现状总结；熔断节点按格式填写 |
| 8 | fused_info_summary熔断节点已填，通过节点填null | ✅ 4个熔断节点已填，5个通过节点填null |
| 9 | 数据字典MD产出，含扩展说明 | ✅ 已产出，含新域加入规则、字段修改权限、枚举值规范 |
| 10 | 两份文件UTF-8编码 | ✅ UTF-8 |
| 11 | 自检声明已逐项自检 | ✅ 本表即为自检声明 |

---

> 产出文件路径：03_发布成果-交付物/权威数据/规则数据/T1_nodes_数据字典_v1.0.md

