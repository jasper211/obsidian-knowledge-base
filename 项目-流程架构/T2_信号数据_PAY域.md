---
type: 数据表
table: T2
table_name: 信号数据
domain: PAY
layer: 信号层
source: 校验与上下文
created: 2026-06-15
tags: [数据表, T2, PAY]
---

## 📊 T2 · 信号数据（PAY）

> 📎 对应CSV：[[T2_信号数据_PAY域|T2_信号数据_PAY域.csv]]

**关联数据表：**
- [[T1_节点索引_全域|T1]]
- [[T3_访谈线索_PAY域|T3]]
- [[T4_访谈线索_PAY域|T4]]
- [[T5_规则清单_PAY域|T5]]
- [[T6_交付物清单_全域|T6]]
- [[T7_缺口清单_全域|T7]]
- [[T8_裁定清单_PAY域|T8]]

---

# T2 · 信号数据（PAY域）

> 总信号: 18条 | 域: PAY

| 信号ID | 节点ID | 信号内容 | 来源 |
|--------|--------|---------|------|
| S2-PAY01-001 | VN-PAY-01 | L4组成为L4-COM-01佣金政策接收与校准+L4-COM-02差异化拆解与验证 | Sheet2·Row10 |
| S2-PAY01-002 | VN-PAY-01 | 频次为季×1+月×1 | Sheet2·Row23 |
| S2-PAY02-001 | VN-PAY-02 | L4组成为L4-COM-10保单信息整合与应收核算+L4-COM-11银行到账确认与实收对账 | Sheet2·Row32 |
| S2-PAY02-002 | VN-PAY-02 | 频次为月×2(对账+复盘) | Sheet2·Row45 |
| S2-PAY02-003 | VN-PAY-02 | 月度×2刷新·跑通但效率低 | Sheet2·Row38 |
| S2-PAY03-001 | VN-PAY-03 | 争议留痕需字段化(争议ID/类型/责任方/关闭时间) | Sheet2·Row68 |
| S2-PAY03-002 | VN-PAY-03 | L4组成为L4-COM-12应派金额拆分与渠道对账+L4-COM-07佣金争议处理 | Sheet2·Row54 |
| S2-PAY03-003 | VN-PAY-03 | 频次为月×2 | Sheet2·Row67 |
| S2-PAY04-001 | VN-PAY-04 | IA硬指标：非持牌占比≤50% | Sheet1·Row8 |
| S2-PAY04-002 | VN-PAY-04 | IA硬指标：同行支付≤88% | Sheet1·Row8 |
| S2-PAY04-003 | VN-PAY-04 | 频次为月×2 | Sheet2·Row89 |
| S2-PAY05-001 | VN-PAY-05 | L4组成为L4-SSVA-01/02(服务对账/激励结算) | Sheet2·Row98 |
| S2-PAY05-002 | VN-PAY-05 | 频次为月×2 | Sheet2·Row111 |
| S2-PAY06-001 | VN-PAY-06 | L4组成为FPG-01/02/03/04+★FPG-05 | Sheet2·Row120 |
| S2-PAY06-002 | VN-PAY-06 | 频次为月×1 | Sheet2·Row133 |
| S2-PAY07-001 | VN-PAY-07 | 频次为周×1+月汇总 | Sheet2·Row155 |
| S2-PAY08-001 | VN-PAY-08 | 先解耦不阻塞P0节点（优先级P1） | Sheet2·Row178 |
| S2-PAY08-002 | VN-PAY-08 | 频次为月×1 | Sheet2·Row177 |
