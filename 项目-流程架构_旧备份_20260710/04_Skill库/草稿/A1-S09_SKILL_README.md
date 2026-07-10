---
type: 项目笔记
source: 04_Skill库/草稿
synced: 2026-06-15
tags: [项目]
---

# A1-S09 — L1-L3 归属验证与写入

**Skill ID**：A1-S09
**版本**：V1.0
**归属 Agent**：A1（EA数据库维护）
**创建日期**：2026-04-28
**状态**：可用

---

## 一、这个 Skill 做什么

以**硬编码的 `L1_NAMES`** 为唯一权威定义，从 `L1_L3映射表_最终版.csv` 读取 L3→L1
映射关系，幂等校验并修正 `fact_activity` 表中的 `l1_code` / `l1_name` 字段。

**核心特性**：
- `L1_NAMES` 硬编码于 `skill_A1_S09.py`，**不允许从外部文件读取覆盖**（权威防护）
- 每次执行输出校验报告：已正确数 / 修正数 / 异常项
- 支持 `dry_run` 预检模式（只校验不写入）
- 提供 `get_l1_for_l3()` 工具函数，可无数据库直接查询映射

**理论依据**：L1-L3映射分析逻辑与标准.md / 价值流与价值链方法论纠偏.md 第四节 4.1（Mark裁定）

---

## 二、权威L1定义（硬编码，不可覆盖）

```python
L1_NAMES = {
    "L1-01": "资源获取与产品整合",
    "L1-02": "市场设计与合作伙伴发展",
    "L1-03": "运营反馈与路由决策",
    "L1-04": "能力赋能与增长驱动",
    "L1-05": "价值增值与生态绑定",
}
```

任何与此不符的 `l1_name` 字段值均视为错误，执行时自动修正。

---

## 三、输入文件

| 文件 | 路径 | 说明 |
|------|------|------|
| L1_L3映射表_最终版.csv | `output(Claude)/validation/` | 主输入，83行（含表头） |
| l1_mapping_table.json | `skills/A1-S09/` | 预生成的JSON映射（含L1_NAMES） |
| ea_knowledge_base.db | `output(Claude)/` | 目标数据库（fact_activity表） |

---

## 四、函数签名

```python
from skill_A1_S09 import validate_and_apply_l1_mapping, get_l1_for_l3

# 主校验+写入函数
result = validate_and_apply_l1_mapping(
    db_path  = "path/to/ea_knowledge_base.db",
    csv_path = "path/to/L1_L3映射表_最终版.csv",
    log_path = "path/to/logs/A1_S09_run.txt",  # 可选
    dry_run  = False,  # True = 只校验不写入
)

# 轻量查询（不依赖数据库）
entry = get_l1_for_l3("L3-FLM")
# → {"l3_name": "理财师线索挖掘与招募", "l1_code": "L1-03", "l1_name": "运营反馈与路由决策"}
```

### 返回值

```python
{
    "status":      "ok" | "error",
    "l3_checked":  int,         # 校验的唯一L3数量
    "rows_updated": int,        # 实际修正的L3数量
    "rows_ok":     int,         # 已符合权威定义的L3数量
    "anomalies":   list[dict],  # 不在CSV中的L3（异常项）
    "log_lines":   list[str],
    "log_path":    str          # 仅当传入log_path时
}
```

---

## 五、典型调用示例

### 预检（dry_run）

```python
from skill_A1_S09 import validate_and_apply_l1_mapping

BASE = "/Users/zhaoqitrenda.cn/Desktop/企业架构与岗位分析项目"

# 先预检，确认修正范围
result = validate_and_apply_l1_mapping(
    db_path  = f"{BASE}/output(Claude)/ea_knowledge_base.db",
    csv_path = f"{BASE}/output(Claude)/validation/L1_L3映射表_最终版.csv",
    dry_run  = True,
)
print(f"需修正：{result['rows_updated']}个（dry_run，未写入）")
```

### 正式写入

```python
result = validate_and_apply_l1_mapping(
    db_path  = f"{BASE}/output(Claude)/ea_knowledge_base.db",
    csv_path = f"{BASE}/output(Claude)/validation/L1_L3映射表_最终版.csv",
    log_path = f"{BASE}/output(Claude)/skills/A1-S09/logs/run.txt",
    dry_run  = False,
)
print(f"修正：{result['rows_updated']}个L3 | 已正确：{result['rows_ok']}个")
```

### 查询单个L3（无需数据库）

```python
from skill_A1_S09 import get_l1_for_l3

entry = get_l1_for_l3("L3-COM")
# → {"l3_name": "佣金全链路管理", "l1_code": "L1-03", "l1_name": "运营反馈与路由决策"}
```

---

## 六、边界与限制

| 场景 | 行为 |
|------|------|
| l3_code 不在CSV中 | 记录为 anomaly，不报错，不修改该L3 |
| CSV中的l1_code不在L1_NAMES中 | 跳过该行，日志警告 |
| l1_name 与L1_NAMES不一致 | 自动以L1_NAMES覆盖（CSV中的名称不可信） |
| dry_run=True | 只读校验，不执行UPDATE |
| fact_activity中有placeholder行（TBD） | 正常校验，有映射的会被修正 |

---

## 七、与其他 Skill 的关系

| Skill | 关系 |
|-------|------|
| A1-S08（VS-L3映射） | 并行：两套映射维度，A1-S09管L1归属，A1-S08管VS归属 |
| A1-S03（推导补录） | 上游：新增L3行后应重新运行A1-S09确保l1字段正确 |

---

## 八、命令行运行

```bash
python skill_A1_S09.py \
    --db  /path/ea_knowledge_base.db \
    --csv /path/L1_L3映射表_最终版.csv \
    --out /path/output \
    [--dry-run]   # 只校验不写入
```

---

*本文档由 Claude Code 自动生成，需架构小组审核后正式入库。*
