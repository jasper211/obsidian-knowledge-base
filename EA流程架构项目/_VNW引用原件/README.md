# _VNW引用原件/

VNW需要引用、但性质上不该走OB白名单原子提炼的EA项目源文件——L3流程蓝图、
D1-D6打分方法论定义、D1-D6全量打分表、岗位L4映射材料。这些是项目组成员
产出的工作材料，不是"成型的方法论文档和结果文档"，跟`EA流程架构项目/`
其余文件（全部是LLM提炼出的concept_atom/entity_hub）性质不同，不要把
这个文件夹里的文件当成知识原子处理（没有`type: concept_atom`
frontmatter，不参与聚类/枢纽机制）。

## 同步机制

由`sync_vnw_reference_files.py`原样镜像，**不做任何提炼、不改内容**，只做
"存在性+最新版本"同步：
- 每天跟`ob-daily-extract`同一个定时任务一起跑，增量同步（按内容哈希，
  没变化的文件不重复写入）
- L3流程蓝图按`table_reader.py`的`group_latest_versions()`同款规则，
  同一L3编码只保留最新版本，不搬运历史版本
- 源文件路径+同步时间记录在`_manifest.json`（溯源用，不是给人读的）

## 当前收录范围（2026-07-28确认，见`sync_vnw_reference_files.py`的
`VNW_REFERENCE_SOURCES`）

1. `流程架构项目_jasper/02_过程成果-工作产出/L3流程库/流程蓝图_L3-*.md`
   （全量，按编码去重取最新版）
2. `03_发布成果-交付物/治理规范/DICT_流程数据库数据字典_V2_项目交付.md`
   （含D1-D6打分方法论定义，DP-021~DP-027）
3. `02_过程成果-工作产出/规则分析（Jasper）/Agent与Skill体系/L4两阶段复核_全量368条_合并版_v1.0.csv`
4. `HR工作材料/D_EA项目组织优化/2026-07-20_68L3岗位族归属设计_v6.1_SUBMITTED.md`
   （岗位↔L4映射权威文件，HR资料目前独立于数据库之外）

新增引用源：在`sync_vnw_reference_files.py`的`VNW_REFERENCE_SOURCES`列表
里加一条即可，不需要改同步逻辑。
