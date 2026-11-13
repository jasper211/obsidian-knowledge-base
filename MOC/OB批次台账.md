# OB批次台账

按[[OB_P0增量作业规范_2026-11-10]]记录实际批次。无变化不追加。治理P0报告在[[OB_P0交付总览_2026-11-10]]，不是知识摄入批次。

| batch_id | root_id | window_utc | scanned_at | source_count | dispositions | candidate_cards | reviewer | review_result | receipt | published_at |
|---|---|---|---|---|---|---|---|---|---|---|
| OB-RW-P1-001 | ROOT-RW-L | 未完成窗口扫描，仅精确两路径 | 复检2026-11-11T03:26:55.697Z | 2 | hold:2 | 0 | Galileo | 有限流程通过；非知识验收 | [[OB批次/OB-RW-P1-001]] | null |
| OB-SERVER-P2-001 | ROOT-SERVER/projects | 受限逐层元数据，不推进内容cursor | 2026-11-11T03:31:38Z至03:33:36Z | 0（11项元数据） | 来源unknown隔离 | 0 | Galileo | 首批及续查回执边界通过；非知识验收 | [[OB批次/OB-SERVER-P2-001]] | null |
| OB-SERVER-P2-002 | ROOT-SERVER/projects | 精确单源片段，未完成全量窗口 | 2026-11-11T03:36:12Z至03:36:59.517331Z | 1（另14项元数据） | 历史方法候选；不晋升 | 1 | Galileo | 内容分析与候选留存终审通过 | [[OB批次/OB-SERVER-P2-002]] | null |
| OB-SERVER-P2-003 | ROOT-SERVER/产品部门知识库 | 单MD，非全量 | 2026-11-11T04:43:07.192213Z | 1 | 参数异常拒收 | 0 | Galileo | 隔离处置通过 | [[OB批次/OB-SERVER-P2-003]] | null |
| OB-SERVER-P2-004 | ROOT-SERVER/产品部门知识库 | 同ID单MD对照 | 2026-11-11T04:43:52.109872Z | 1 | 来源差异待核，不晋升 | 0 | Galileo | 隔离通过；mtime修复复核通过 | [[OB批次/OB-SERVER-P2-004]] | null |
| OB-SERVER-P2-005 | ROOT-SERVER/产品部门知识库 | 公司资料单层元数据 | 2026-11-11T04:45:47Z | 0（9PDF引用项） | citation_only:9 | 0 | Galileo | 仅引用边界通过 | [[OB批次/OB-SERVER-P2-005]] | null |
| OB-LOCAL-RW-001 | ROOT-RW-L | 首次六个月窗口内单源 | 2026-11-11T04:57:34.661Z | 1 | 候选口径分析 | 0 | Galileo | 独立核验通过 | [[OB批次/OB-LOCAL-RW-001]] | null |
| OB-LOCAL-RW-002 | ROOT-RW-L | 窗口内四主题 | 2026-11-11T05:00:45.991Z | 4 | 版本口径关联 | 0 | Galileo | 独立核验通过 | [[OB批次/OB-LOCAL-RW-002]] | null |
| OB-LOCAL-RW-003 | ROOT-RW-L | 两业务MD首段 | 2026-11-11T05:03:04.991Z | 2 | 历史设计分析 | 0 | Galileo | 片段独立核验通过 | [[OB批次/OB-LOCAL-RW-003]] | null |
| OB-LOCAL-RW-004 | ROOT-RW-L | 同两源余段，非新增2源 | 2026-11-11T05:04:33.684Z | 2续读 | 阅读闭合，不晋升 | 0 | Galileo | 必要定位核查通过 | [[OB批次/OB-LOCAL-RW-004]] | null |
| OB-LOCAL-RW-005 | ROOT-RW-L | 窗口内HTML | 2026-11-11T07:14:25.275334Z | 1 | 静态正文关联 | 0 | Galileo | 定点核查通过 | [[OB批次/OB-LOCAL-RW-005]] | null |
| OB-LOCAL-RW-006 | ROOT-RW-L | 窗口内三README | 2026-11-11T12:46:13.741Z | 3 | 历史候选与聚合分流 | 0 | James | 独立核查通过 | [[OB批次/OB-LOCAL-RW-006]] | null |
| OB-LOCAL-RW-007 | ROOT-RW-L | 招聘HTML选定片段 | 2026-11-11T15:22:40.385983Z | 1 | 历史招聘评估门槛 | 0 | James | 限定独立核查通过，非全文 | [[OB批次/OB-LOCAL-RW-007]] | null |
| OB-LOCAL-RW-008 | ROOT-RW-L | 根层12名分流、章程L1–85 | 检查截至2026-11-11T19:27:26Z | 1正文 | 历史项目定位与阶段边界 | 0 | James | 限定独立核查通过 | [[OB批次/OB-LOCAL-RW-008]] | null |
| OB-LOCAL-RW-009 | ROOT-RW-L | 同章程L86–208续读 | 检查截至2026-11-11T23:30:05Z | 1续读 | 目标、建议与审批边界 | 0 | James | 限定独立核查通过 | [[OB批次/OB-LOCAL-RW-009]] | null |
| OB-LOCAL-RW-010 | ROOT-RW-L | 会议议程L1–132 | 检查截至2026-11-12T03:31:46Z | 1 | 历史议程/空白模板，低增量 | 0 | James | 限定独立核查通过 | [[OB批次/OB-LOCAL-RW-010]] | null |
