---
type: 项目笔记
source: 04_Skill库/report_generator
synced: 2026-06-15
tags: [项目]
---

# report_generator — Mark V3.0 调研报告生成器

> **定位**: 读取调研 Excel → 按 Mark V3.0 方法论收敛到价值节点 → 生成 D1-D5 标准交付物
> **上游**: 调研 Excel（L3-L4 流程调研 + 交付物调研）
> **下游**: Carrie（数据底座层）/ 袁林（RACI 矩阵）/ 赵琦（规则治理层）

---

## 一、快速开始

### 1.1 环境要求

- Python 3.9+
- pandas
- openpyxl

```bash
pip install pandas openpyxl
```

### 1.2 运行命令

```bash
python main.py \
    --payment-flow "调研_付款流程_V1.0.xlsx" \
    --l4-deliverable "调研_L4交付物_含付款流程_V1.0.xlsx" \
    --output-dir "./output"
```

### 1.3 输出文件

| 交付物 | 文件名 | 格式 | 消费方 |
|--------|--------|------|--------|
| D1 | `D1_修正版L4清单_V1.0_YYYYMMDD.xlsx` | Excel | Carrie / 袁林 / 赵琦 |
| D2 | `D2_L4偏差分析报告_V1.0_YYYYMMDD.md` | Markdown | Mark / Carrie |
| D3 | `D3_L3架构重构方案_V1.0_YYYYMMDD.md` | Markdown | Mark / 王总 |
| D4 | `D4_Mark裁定清单_V1.0_YYYYMMDD.md` | Markdown | Mark |
| D5 | `D5_Excel整改清单_V1.0_YYYYMMDD.md` | Markdown | Terresa |

---

## 二、V3.0 方法论核心

### 2.1 与 V2.0 的区别

| 维度 | V2.0（旧版） | V3.0（Mark 要求） |
|------|-------------|------------------|
| **起点** | 从 L4 反向抽产出物 | 从 M0-M8 识别 L3 端到端闭环 |
| **单元** | 物理交付物（N 个） | L3 闭环价值节点（收敛后） |
| **字段** | 2 状态（凭证性+数据可用性） | 4 硬性属性 + 3 重验证 gate + M 锚定 + KPI 锚定 |
| **熔断** | 无机制 | 任一 gate FAIL → 强制熔断，不计入交付 |

### 2.2 价值节点（示例）

价值节点是 L3 端到端流程中可被独立交付、验证、度量的最小价值单元。不同业务领域有不同的价值节点集合。

当前默认配置涵盖以下领域（在 `config.py` 中定义）：
- **财务支付** (VN-PAY-01~09) — 9 个价值节点
- 可扩展至：资金管理 (VN-BAM-01, VN-CFM-01)、经代业务、HR、保司合作等

### 2.3 三个致命反例（通用检测）

| 反例 | 问题 | V3.0 整改 |
|------|------|----------|
| ① 服务类 L3 三件套化 | N 个服务商 L3 被切成过多条 L4，违反「不能拦腰斩断 L3」 | 收敛到单个价值节点 |
| ② 执行流程被切碎 | 申请→审核→授权→执行→归档被切成过多独立交付物 | 收敛到单个价值节点 |
| ③ 空交付物立为产出 | L4 交付物为空/未跑过数据，却列为交付物 | 强制熔断 |

---

## 三、程序架构

```
main.py                          # CLI 入口
    ├── excel_reader.py          # 读取调研 Excel，标准化为 L4Record / Scenario
    ├── value_node_mapper.py     # L4 → 价值节点映射，检测反例
    ├── gate_validator.py        # 4 硬性属性 + 3 重 Gate 评分，熔断判定
    ├── deviation_analyzer.py    # 结构/状态/责任 三分类偏差分析
    ├── report_generator.py      # 生成 D1-D5 交付物
    └── config.py                # V3.0 方法论配置（价值节点/Gate规则/裁定模板）

meeting_survey_generator/        # 子模块：会议录音 → 调研采集表
    ├── main.py
    ├── transcript_reader.py
    └── survey_generator.py

archive/                         # 历史业务脚本（按领域归档）
    ├── generate_*_survey.py     # 各业务领域调研生成
    ├── generate_*_d1_d4.py      # 各业务领域报告生成
    ├── update_*.py              # 数据更新脚本
    ├── read_*.py                # 数据读取/验证脚本
    └── audit_*.py               # 审计检查脚本
```

### 3.1 数据处理流程

```
调研 Excel (L3-L4流程 + 交付物调研)
    ↓ excel_reader.py
标准化 L4Record[] + Scenario[]
    ↓ value_node_mapper.py
价值节点 ValueNode[]（L4 收敛到价值节点）
    ↓ gate_validator.py
4属性+3gate评分 → 综合得分 + 熔断判定
    ↓ deviation_analyzer.py
结构/状态/责任 偏差矩阵 + 五大洞察
    ↓ report_generator.py
D1 Excel + D2/D3/D4/D5 Markdown
```

---

## 四、输入 Excel 格式要求

### 4.1 调研 Excel（流程调研）

**Sheet 列表**（示例）：
- `业务需求调研` — N 条业务场景
- `员工报销调研` — 报销流程
- `主体差异调研` — 审批链/合规差异

**必填列**:
| 列名 | 说明 | 示例 |
|------|------|------|
| 类型 | 场景名称 | 佣金转介费 |
| 走款主体 | 付款方 | 各牌照主体 |
| 付款对象 | 收款方 | KA、塞尔斯 |
| 频率 | 周期 | 1月2次 |
| 执行人 | 谁执行 | JorJor(Chaya) |
| 审批链 | 审批路径 | 业务端→财务负责人 |
| SOP | 是否有SOP | 无SOP，有台账 |
| 关联L3 | 对应L3编码 | L3-COM |
| 关联L4 | 对应L4编码 | L4-COM-10~13 |
| 状态 | 标准化状态 | 存在 / 部分 / 缺失 / 待调研 |

### 4.2 调研 Excel（L4 交付物调研）

**必填列**:
| 列名 | 说明 | 示例 |
|------|------|------|
| L3编码 | L3流程编码 | L3-COM |
| L3名称 | L3流程名称 | 佣金全链路管理 |
| L4编码 | L4交付物编码 | L4-COM-10 |
| L4名称 | L4交付物名称 | 保单信息整合与应收核算 |
| 状态 | 调研状态 | 存在 |
| 状态说明 | 详细描述 | Cici录入→JoJo手工匹配 |
| 交付物 | 物理产出物 | 应收核算表 |
| 责任人(数据库) | dim_process标注 | 财务-各牌照财务 |
| 责任人(实际) | 调研确认 | 中台支持-蔡依娜 |
| 数据表关联 | 关联的数据表 | FACT_COMMISSION_RATE |

---

## 五、输出说明

### 5.1 D1 · 修正版 L4 清单（Excel）

**6 个 Sheet**:

| Sheet | 内容 |
|-------|------|
| 0_方法论与说明 | V2.0 vs V3.0 对比、4属性定义、3gate定义、M0-M8定义、熔断规则 |
| 1_价值节点总览 | 价值节点汇总（存在/部分/缺失统计 + gate 状态 + 综合判定） |
| 2_节点详情卡 | 完整属性卡（L3/L4/M锚/KPI锚/4属性/3gate/Next动作） |
| 3_四属性三重验证矩阵 | 双层表头 + gate 着色 + 综合判定公式 |
| 4_L4映射明细 | 全部 L4 的映射与偏差记录（L3→VN→状态→偏差类型→责任人） |

### 5.2 D2 · L4 偏差分析报告（MD）

**章节**:
1. 报告目的
2. 偏差分析框架
3. 结构性偏差
4. 状态性偏差（数据库标存在实际缺失/部分的L4清单）
5. 责任性偏差（跨部门错位清单）
6. 五大结构性洞察
7. 偏差消除建议（责任方+时点）
8. 附录：致命反例

### 5.3 D3 · L3-L1 架构重构方案（MD）

**章节**:
1. 决策原则（端到端 + L3 完整性）
2. L3 架构变更总览（变更前后对比表 + 架构重构图）
3. 各 L3 变更详情
4. L1-L3 归属统计变化
5. 流转规则
6. 依赖与前置条件
7. 向上汇报建议
8. 边界声明

### 5.4 D4 · Mark 裁定清单（MD）

每项含：背景 / 问题 / 建议方案（A/B/C）/ 影响范围 / 签字栏

### 5.5 D5 · Excel 整改清单（MD）

含具体整改动作 + 工时 + 时点 + 验收标准

---

## 六、扩展至新领域

### 6.1 新增业务领域价值节点

编辑 `config.py` 中 `VALUE_NODES` 列表，按模板添加：

```python
{
    "code": "VN-XXX-01",
    "name": "价值节点名称",
    "description": "描述",
    "related_l3s": ["L3-XXX"],
    "related_l4s": ["L4-XXX-01"],
    "hard_attributes": {
        "物理载体": "...",
        "数据属性": "...",
        "业务锚点": "...",
        "责任人": "..."
    },
    "gates": {
        "gate_1_凭证性": "...",
        "gate_2_数据闭环": "...",
        "gate_3_权责清晰": "..."
    },
    "priority": "P0-规范化",
    "kpi_anchor": "..."
}
```

### 6.2 调整 Gate 评分规则

编辑 `config.py` 中 `GATES` 和 `HARD_ATTRIBUTES` 列表。

### 6.3 新增裁定项

编辑 `config.py` 中 `DECISION_ITEMS_TEMPLATE` 列表。

### 6.4 自定义报告模板

编辑 `report_generator.py` 中对应 `generate_dX` 方法。

### 6.5 参考历史脚本

`archive/` 目录包含已归档的各业务领域脚本：
- `generate_ka_*.py` — KA 业务领域
- `generate_jingdai_*.py` — 经代业务领域
- `generate_hr_*.py` — HR 业务领域
- `generate_ins_*.py` — 保司合作领域
- `generate_tongxing_*.py` — 同行合作领域
- `generate_vs01_*.py` — VS-01 端到端领域
- `update_*.py` — 各类权威数据更新脚本

---

## 七、子模块

### meeting_survey_generator

将会议录音/纪要转换为结构化调研采集表的子模块。

用法：
```bash
cd meeting_survey_generator
python main.py --audio "会议录音.mp3" --output "调研采集表.xlsx"
```

---

## 八、版本记录

| 版本 | 日期 | 说明 |
|------|------|------|
| V1.0 | 2026-05-22 | 初始版本，财务支付板块 |
| V1.1 | 2026-06-01 | 重构为通用 report_generator，支持多领域扩展 |
