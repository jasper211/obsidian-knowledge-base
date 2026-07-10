---
type: project_note
project: 流程架构
layer: "04_Skill库"
layer_tag: Skill
subdir: "report_generator"
tags: [Skill]
---

## 🧭 导航
⬆️ [[04_Skill库]] · ⬆️ [[report_generator]] · 🏠 [[流程架构项目MOC]]

---

# SKILL: report_generator

## 概述

基于 Mark V3.0 方法论的企业架构调研报告生成器。将 L3-L4 流程调研 Excel 自动收敛到价值节点，经过 4 属性 + 3 Gate 验证，输出 D1-D5 标准交付物。

## 能力范围

- **输入**: 调研 Excel（L3-L4 流程 + 交付物调研）
- **输出**: D1(修正版L4清单) / D2(偏差分析) / D3(架构重构) / D4(裁定清单) / D5(整改清单)
- **方法论**: Mark V3.0（端到端价值节点、4HA+3Gate、熔断机制）

## 快速使用

```bash
python main.py \
    --payment-flow "调研_流程_V1.0.xlsx" \
    --l4-deliverable "调研_L4交付物_V1.0.xlsx" \
    --output-dir "./output"
```

## 领域扩展

当前默认配置为财务支付领域（VN-PAY-01~09）。扩展至新领域：

1. 编辑 `config.py` → `VALUE_NODES` 列表添加新领域价值节点
2. 编辑 `config.py` → `DECISION_ITEMS_TEMPLATE` 添加裁定项模板
3. 如需自定义 Excel 列映射，修改 `excel_reader.py`
4. 参考 `archive/` 中各业务领域的历史脚本

## 核心模块

| 模块 | 职责 |
|------|------|
| `main.py` | CLI 入口，编排全流程 |
| `excel_reader.py` | 标准化读取调研 Excel |
| `value_node_mapper.py` | L4 → 价值节点映射，反例检测 |
| `gate_validator.py` | 4 硬性属性 + 3 Gate 评分 |
| `deviation_analyzer.py` | 结构/状态/责任 偏差分析 |
| `report_generator.py` | D1-D5 交付物生成 |
| `config.py` | 价值节点定义、Gate 规则、方法论配置 |

## 子模块

- `meeting_survey_generator/` — 会议录音/纪要 → 调研采集表

## 归档脚本

`archive/` 目录包含已整理的历史业务脚本，按业务领域分类：
- KA 业务、经代业务、HR、保司合作、同行合作、VS-01 端到端等

## 依赖

- Python 3.9+
- pandas
- openpyxl

