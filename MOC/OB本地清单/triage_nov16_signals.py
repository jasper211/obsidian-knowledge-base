"""Record bounded disposition of the nine November 16 metadata signals."""
import json
from pathlib import Path

B = Path(__file__).resolve().parent
coverage = json.loads((B / '扫描覆盖.json').read_text())
daily = coverage['daily_increment']
assert daily['checked'] == '2026-11-16T13:58:09.355059-06:00'
assert len(daily['signals']) == 9
rows = []
for signal in daily['signals']:
    p = signal['path']
    r = {'path': p, 'original_signal': signal, 'content_read_allowed': False, 'source_read_bytes': 0}
    if signal['signal'] == 'new_inventory_entry':
        r.update(status='项目归属待核', reason='桌面截图未获项目准入；不解析图片，不因文件新增摄入')
    elif signal['signal'] == 'not_observed_in_direct_listing':
        r.update(status='未见信号保留', reason='只说明直接列表未见，不证明删除；隐藏同步临时不摄入，缺失项目入口不自行判作废')
    elif p.endswith('Agent运行仪表盘.md'):
        r.update(status='沿用工程OB排除', reason='E021/G014既有范围处置不因mtime变化解除；不重读正文')
    elif p.endswith('Agent健康报告.md'):
        r.update(status='范围待核', reason='未获业务项目/类型准入，不凭邻近仪表盘推断或读取')
    elif p.endswith('Jasper AI协同经验引擎'):
        r.update(status='容器信号处置', reason='目录mtime变化不说明子项目在用；不继承正文准入')
    else:
        assert p.endswith('蓝象合规引擎项目工作区/README.md')
        r.update(status='治理片段识别后暂缓', reason='E065限定历史设计/观点用途；必要入口出现待确认股权安排即停止，不跟链接，不作现行批准或业务条款结论', source_read_bytes=768, source_read_locator='UTF-8 byte range [0,768), incomplete trailing character ignored', observed_at='2026-11-16T19:35:10.100619-06:00', mtime_ns='1794808416040092551', size=36709, stat_stable=True, declared_business_date='frontmatter updated 2026-11-05; source declaration only', source_claim='合作筹备、存在待确认事项；非当前状态独立核验', continuation='仅取得可分离、非敏感业务片段范围证据后继续；不自动读取链接目标')
    rows.append(r)
report = {'batch': '2026-11-16-nine-signals', 'scan_checked': daily['checked'], 'processed_signals': 9, 'records': rows, 'source_body_bytes': 768, 'source_files_read': 1, 'new_business_analyses': 0, 'actual_tokens': None, 'review_status': 'pending independent boundary review', 'local_acceptance': False, 'remaining': 'Scope and safe-content gaps retained; signal disposition does not resolve them'}
out = B / '20261116增量信号处置.json'
with out.open('x') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
    f.write('\n')
print('9 signal dispositions; 1 source prefix / 768 bytes; 0 new business analyses')
