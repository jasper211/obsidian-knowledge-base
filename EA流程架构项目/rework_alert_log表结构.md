---
type: concept_atom
concept_type: 定义
project: EA流程架构项目
source: 08_任务与跟进/任务状态/Terresa_回函_fact_card字典澄清_M4-W10_20260529.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-29
entity_type: 非正式主题
entity_ref: 返工预警表
extracted_at: 2026-07-16T13:52:25
status: 待裁定
conflict_group: 返工预警表
---

# rework_alert_log表结构

rework_alert_log表包含alert_id（主键）、card_id（引用fact_card）、alert_time、rework_count、alert_level（WARNING/CRITICAL）、resolved（布尔）字段。触发器trg_rework_alert在fact_card插入或更新且rework_count>=3时触发，行级触发器，幂等设计。

## 关联概念

- [[fact_card]]
- [[trg_rework_alert]]
- [[rework_count]]

## 所属枢纽

- [[返工预警表]]

## ⚠️ 待裁定：entity_ref矛盾（返工预警表）

与同组原子存在冲突：[[rework_alert_log_触发器]]、[[返工次数预警]]、[[rework_alert_log表schema缺失]]

冲突说明：原子'rework_alert_log 触发器'指出触发器非幂等，而原子'rework_alert_log表结构'声称幂等设计，两者关于幂等性描述矛盾。

（标记时间：2026-07-21T20:56:43）
