---
type: 项目笔记
source: 04_Skill库/草稿
synced: 2026-06-15
tags: [项目]
---

# A1-S08 — VS-L3 映射写入

**Skill ID**：A1-S08
**版本**：V1.0
**归属 Agent**：A1（EA数据库维护）
**创建日期**：2026-04-28
**状态**：可用

---

## 一、这个 Skill 做什么

从 `L3与价值流全量分析汇总表.csv` 读取 L3→VS 映射规则，幂等写入数据库
`bridge_l3_vs` 表（首次执行自动建表），并输出结构化日志。

**核心特性**：
- 覆盖 82 个 L3 的 VS 映射（VS级 66条 + 非VS级 16条）
- **非VS级16条同等写入**，不跳过；`vs_l3_mapping = "非VS级"`，`stage_l3_mapping` = L1层标注
- 幂等保护：默认不重复写入；`force_overwrite=True` 可强制覆盖
- 自动建表：`bridge_l3_vs` 不存在时自动创建
- 日志：每次执行输出 VS分布统计 + 非VS级明细

**理论依据**：价值流-L3映射分析逻辑与标准.md（同目录相邻文件）

---

## 二、输入文件

| 文件 | 路径 | 说明 |
|------|------|------|
| L3与价值流全量分析汇总表.csv | `output/output(Claude)/validation/` | 主输入，83行（含表头） |
| mapping_rules_vs.json | `skills/A1-S08/` | 由CSV预生成，可校验用 |
| ea_knowledge_base.db | `output(Claude)/` | 目标数据库 |

---

## 三、输出表结构（bridge_l3_vs）

| 字段 | 类型 | 说明 |
|------|------|------|
| l3_code | TEXT PK | L3 编码 |
| l3_name | TEXT | L3 名称 |
| vs_l3_mapping | TEXT | VS-1/VS-2/VS-3/VS-4/VS-5 或 "非VS级" |
| stage_l3_mapping | TEXT | 价值流阶段码（如VS2-S3）或L1层标注（如"战略赋能层(L1-01)"） |
| confidence | TEXT | 高/中/低 |
| evidence | TEXT | 证据来源 |
| notes | TEXT | 备注 |
| is_non_vs | INTEGER | 1=非VS级，0=VS级 |
| source_file | TEXT | 来源CSV名称 |
| last_updated | TEXT | 写入日期 |

---

## 四、函数签名

```python
from skill_A1_S08 import write_vs_mappings, query_vs_for_l3, export_mapping_csv

# 主写入函数
result = write_vs_mappings(
    db_path         = "path/to/ea_knowledge_base.db",
    csv_path        = "path/to/L3与价值流全量分析汇总表.csv",
    rules_json_path = "path/to/mapping_rules_vs.json",
    log_path        = "path/to/logs/A1_S08_run.txt",  # 可选
    force_overwrite = False,   # True = 先清空再写入
)

# 查询单个L3的VS映射
entry = query_vs_for_l3(db_path, "L3-FLM")
# → {"l3_code": "L3-FLM", "vs_l3_mapping": "VS-4", "stage_l3_mapping": "VS4-S1", ...}

# 导出完整映射CSV
export_mapping_csv(db_path, "output/bridge_l3_vs.csv")
```

### 返回值

```python
{
    "status":        "inserted" | "skipped" | "error",
    "rows_inserted": int,     # 实际写入行数
    "rows_skipped":  int,     # 幂等跳过的已有行数
    "rows_non_vs":   int,     # 非VS级写入行数
    "log_lines":     list[str],
    "log_path":      str      # 仅当传入log_path时
}
```

---

## 五、典型调用示例

```python
from skill_A1_S08 import write_vs_mappings

BASE = "/Users/zhaoqitrenda.cn/Desktop/企业架构与岗位分析项目"

result = write_vs_mappings(
    db_path         = f"{BASE}/output(Claude)/ea_knowledge_base.db",
    csv_path        = f"{BASE}/output/output(Claude)/validation/L3与价值流全量分析汇总表.csv",
    rules_json_path = f"{BASE}/output(Claude)/skills/A1-S08/mapping_rules_vs.json",
    log_path        = f"{BASE}/output(Claude)/skills/A1-S08/logs/run.txt",
)
print(result["status"], result["rows_inserted"])
```

---

## 六、非VS级16条说明

这16条L3不属于任何价值流（没有外部利益相关者旅程），但仍需写入：

| 类别 | L3编码 | stage_l3_mapping |
|------|--------|-----------------|
| 战略赋能层 | CAS / MED / MEI / MIO / SFC / SPE / SRE / VPV | 战略赋能层(L1-01) |
| 佣金合规层 | CBD / CMU / COM / CVI | 佣金合规层(L1-04) |
| 权益中台横切层 | EO / RSD / SLCM / SLM | 权益中台横切层(L1-05) |

---

## 七、与其他 Skill 的关系

| Skill | 关系 |
|-------|------|
| A1-S09（L1-L3映射） | 并行：两套独立映射体系，互不覆盖 |
| A1-S03（推导补录） | 上游：A1-S03 补录数据后，A1-S08 补充VS维度 |

---

## 八、命令行运行

```bash
python skill_A1_S08.py --db /path/ea_knowledge_base.db \
    --csv /path/L3与价值流全量分析汇总表.csv \
    --rules /path/mapping_rules_vs.json \
    --out /path/output \
    [--force]  # 覆盖已有数据
```

---

*本文档由 Claude Code 自动生成，需架构小组审核后正式入库。*
