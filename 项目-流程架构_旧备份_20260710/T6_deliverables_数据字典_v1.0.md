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

# T6 · deliverables · 数据字典

> 任务包：TASK-M4W10-095
> 产出日期：2026-06-11
> 对应CSV：T6_deliverables_PAY域_v1.0.csv
> 来源：
> - PAY域_价值节点信号提取基线_v1.8.md · Step3信号5交付物清单
> - PAY域_第一层_规则空白地图_v1.0（未熔断节点）· 规则空白编号关联

---

## 字段定义

| 列号 | 字段名 | 数据类型 | 来源 | 枚举值/格式 | 说明 |
|---|---|---|---|---|---|
| 1 | deliverable_id | TEXT | 自编 | D6-PAY[NN]-[NNN] | 主键，交付物唯一标识 |
| 2 | node_id | TEXT | 对应节点 | VN-PAY-XX | 外键→T1.node_id |
| 3 | name | TEXT | v1.8 MD Step3信号5交付物名称 | 原文 | 交付物完整名称 |
| 4 | format | TEXT | v1.8 MD Step3信号5形态列 | 原文 | 交付物物理形态 |
| 5 | externalized | TEXT | v1.8 MD Step3信号5外化状态 | 已文档化/部分文档化/纸质化为主/完全缺失/未实现/未统一归档 | 外化状态 |
| 6 | producers | TEXT | T1.producers + 多交付物归口规则 | 岗位名称(人名备注) | 生产方岗位 |
| 7 | kpi_anchors | TEXT | T1.kpi_anchors拆分归口 | KPI#XX或null | 交付物关联的KPI |
| 8 | related_rule_gaps | TEXT | 规则空白地图v1.0 | PAY-P0-001,PAY-P1-003或null | 关联的规则空白编号 |
| 9 | file_path | TEXT | 固定初始值 | null | 文件上传后更新 |
| 10 | version | TEXT | 固定初始值 | null | 版本确认后更新 |

---

## 枚举值规范

- **deliverable_id**: D6-PAY[节点后两位]-[三位序号]，例：D6-PAY01-001
- **externalized**: 已文档化 / 部分文档化 / 纸质化为主 / 完全缺失 / 未实现 / 未统一归档
- **kpi_anchors**: KPI#XX格式，逗号分隔；无法判断归口时填null
- **related_rule_gaps**: 规则空白编号，逗号分隔多个；熔断节点填null；无关联填null
- **file_path**: 当前固定填null
- **version**: 当前固定填null

---

## 多交付物producers归口规则

| 节点 | 交付物 | 生产方 |
|---|---|---|
| VN-PAY-01 | 《季度源头佣金表》 | 佣金制表执行岗(Lillian)/佣金数据录入岗(Joanne) |
| VN-PAY-01 | 《市场佣金表(月)》 | 佣金制表执行岗(Lillian)/佣金数据录入岗(Joanne) |
| VN-PAY-01 | 源头PDF合订 | 佣金制表执行岗(Lillian) |
| VN-PAY-02 | 全部3个 | 佣金对账执行岗(Lillian) |
| VN-PAY-03 | 全部3个 | 应派计算执行岗(Pebbles) |
| VN-PAY-04 | 全部3个 | 佣金对账执行岗(Lillian)/合规管理岗(空缺·待Mark裁定) |
| VN-PAY-05 | 《增值服务台账》 | 服务台账管理岗(Joanne) |
| VN-PAY-05 | 《服务价值汇总表》 | 应派计算执行岗(Pebbles) |
| VN-PAY-05 | 服务凭证附件 | 服务台账管理岗(Joanne) |
| VN-PAY-06 | 全部5个 | 应派计算执行岗(Pebbles)/佣金对账执行岗(Lillian) |
| VN-PAY-07 | 全部3个 | 服务台账管理岗(Joanne) |
| VN-PAY-08 | 全部3个 | 待确认 |
| VN-PAY-09 | 全部2个 | 待确认·Mark裁定 |

---

## related_rule_gaps映射规则

- 通过节点（VN-PAY-01/02/03/05/07）：根据规则空白地图v1.0的「交付物名称」列匹配
- 熔断节点（VN-PAY-04/06/08/09）：统一填null（熔断节点不在规则空白地图v1.0中）
- 同一交付物对应多个规则空白时，逗号分隔

---

## 版本记录

| 版本 | 日期 | 变更内容 |
|---|---|---|
| v1.0 | 2026-06-11 | 初始产出，28个交付物，覆盖9个节点 |

---

## 自检声明

| # | Done Criteria | 自检结果 |
|---|---|---|
| 1 | CSV文件产出，行数≥20 | ✅ 28行 |
| 2 | deliverable_id唯一无重复 | ✅ |
| 3 | 所有node_id在T1范围内 | ✅ |
| 4 | 每个节点的交付物全部覆盖 | ✅ 9个节点全部覆盖 |
| 5 | 一个交付物一行 | ✅ 28个独立交付物 |
| 6 | 熔断节点related_rule_gaps填null | ✅ VN-PAY-04/06/08/09 |
| 7 | file_path和version全部null | ✅ |
| 8 | producers按归口规则填写 | ✅ |
| 9 | 字段来源标注清晰 | ✅ Step3信号5 + 规则空白地图 |
| 10 | 数据字典格式统一 | ✅ |
| 11 | 自检声明已逐项自检 | ✅ |

---

> 产出文件路径：03_发布成果-交付物/权威数据/规则数据/T6_deliverables_数据字典_v1.0.md

