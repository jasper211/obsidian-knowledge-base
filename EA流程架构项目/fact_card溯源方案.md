---
type: concept_atom
concept_type: 决策
project: EA流程架构项目
source: 08_任务与跟进/任务状态/Terresa_回函_fact_card字典澄清_M4-W10_20260529.md
authority_layer: 08_任务跟进
confidence: UNSTATED
decision_status: UNSTATED
as_of: 2026-05-29
entity_type: 非正式主题
entity_ref: fact_card溯源
extracted_at: 2026-07-16T13:52:29
status: 待裁定
conflict_group: fact_card溯源
---

# fact_card溯源方案

不使用source_notes字段，而是用batch_id关联etl_batch_detail辅助表实现溯源。etl_batch_detail包含batch_id、target_table、target_card_id、source_table、source_key、etl_time字段。避免事实表膨胀。

## 关联概念

- [[fact_card]]
- [[batch_id]]
- [[etl_batch_detail]]

## 所属枢纽

- [[fact_card溯源]]

## ⚠️ 待裁定：entity_ref矛盾（fact_card溯源）

与同组原子存在冲突：[[数据来源枚举]]、[[fact_card_不新增_source_notes]]、[[fact_card缺少source_ref字段]]

冲突说明：原子1要求data_source不允许为空，原子4指出fact_card缺少source_ref字段，但原子3明确Phase 1不新增source_notes字段，而原子2建议用batch_id关联辅助表实现溯源，原子4则提出多个选项（包括新增source_ref字段），这些在是否新增字段上存在冲突。

（标记时间：2026-07-21T20:56:43）
