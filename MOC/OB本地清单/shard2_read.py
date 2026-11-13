import json, os, stat, hashlib
from pathlib import Path
from html.parser import HTMLParser

BASE = Path(__file__).parent
EXCLUDED = {'45_TOB服务目录与验收口径_v0.2.md', '45_TOI价值证明框架与报表模板_v0.2.md', '45_SHARED权益资产字段冻结与变更规则_v0.2.md'}
BUSINESS = set(range(2, 182, 4))
SENSITIVE = {6, 18, 66, 94, 102, 114, 130}
TECHNICAL = {26, 30, 34, 110, 146}

class TextHTML(HTMLParser):
    def __init__(self):
        super().__init__(); self.skip = 0; self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'template'): self.skip += 1
        if not self.skip and tag in ('p','div','li','h1','h2','h3','h4','tr','section','br'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script','style','template'): self.skip = max(0, self.skip - 1)
        if not self.skip and tag in ('p','div','li','h1','h2','h3','h4','tr','section'): self.parts.append('\n')
    def handle_data(self, data):
        if not self.skip: self.parts.append(data)

def snapshot(s):
    return dict(dev=s.st_dev, ino=s.st_ino, size=s.st_size, mtime_ns=s.st_mtime_ns, ctime_ns=s.st_ctime_ns)

def run():
    raw = (BASE/'295项处置明细.json').read_bytes()
    source = json.loads(raw)
    rows = sorted((r for r in source if r['status']=='业务候选待内容核定' and Path(r['path']).name not in EXCLUDED), key=lambda r:r['path'])
    result=[]; texts={}; hashes={}
    for i, original in enumerate(rows):
        if i % 4 != 2: continue
        p=Path(original['path'])
        r=dict(path=str(p), index=i, status='待核', reason='', source_hash=None, mtime=None, locators=[], read_chars=0, read_bytes=0, token_count=None, token_proxy_chars_div4=0, project_evidence='项目入口队列.json: /Users/a112233/Desktop/Rw权益项目 限定保留；本项在其下。非当前业务有效性证明', source_kind='未读隔离')
        result.append(r)
        if not str(p).startswith('/Users/a112233/Desktop/Rw权益项目/'):
            r['reason']='项目归属未证实'; continue
        if i not in BUSINESS:
            r['reason']=('敏感财务/合同/保单/合规台账材料，隔离不读正文' if i in SENSITIVE else '技术/资料接入或工作台筛选材料，隔离不作业务分析' if i in TECHNICAL else '治理/审阅/决策/验收/导航过程材料，隔离不作业务分析')
        try:
            if any(stat.S_ISLNK(os.lstat(q).st_mode) for q in [*reversed(p.parents),p]):
                r.update(status='排除', reason='路径含符号链接，拒绝跟随'); continue
            before=os.lstat(p); r['stat_before']=snapshot(before); r['mtime']=before.st_mtime
            if not stat.S_ISREG(before.st_mode):
                r.update(status='排除',reason='非普通文件'); continue
            if p.suffix.lower() not in ('.md','.html'):
                r.update(status='排除',reason='非MD/HTML'); continue
            if not 1778389200 <= before.st_mtime < 1794376800:
                r.update(status='排除',reason='首次stat不在指定mtime窗口'); continue
            if i not in BUSINESS: continue
            fd=os.open(p,os.O_RDONLY|os.O_NOFOLLOW)
            with os.fdopen(fd,'rb') as f:
                opened=os.fstat(f.fileno()); data=f.read(); afterfd=os.fstat(f.fileno())
            after=os.lstat(p); r['stat_after']=snapshot(after)
            r['read_bytes']=len(data); r['source_hash']=hashlib.sha256(data).hexdigest()
            r['stat_stable']=snapshot(before)==snapshot(opened)==snapshot(afterfd)==snapshot(after)
            if not r['stat_stable']:
                r['reason']='读取前后stat不稳定，不分析'; continue
            text=data.decode('utf-8-sig')
            if p.suffix.lower()=='.html':
                parser=TextHTML(); parser.feed(text)
                text='\n'.join(s.strip() for s in ''.join(parser.parts).splitlines() if s.strip())
                r['locator_kind']='清洗HTML文本行T（剔除script/style/template；不执行）'
            else: r['locator_kind']='原始Markdown行L'
            r['read_chars']=len(text); r['token_proxy_chars_div4']=(len(text)+3)//4
            r['source_kind']='历史业务设计/纪要，非当前执行核验'
            if r['source_hash'] in hashes:
                r.update(status='重复',reason='与本分片已读取源字节SHA-256相同',duplicate_of=hashes[r['source_hash']]); continue
            hashes[r['source_hash']]=str(p)
            r['reason']='已稳定提取全文，待本轮逐文语义分析'
            texts[str(i)]=text
        except (OSError, UnicodeError) as exc:
            r['reason']='读取异常，隔离: '+str(exc)
    return result,texts,hashlib.sha256(raw).hexdigest()

if __name__=='__main__':
    import sys
    rows,texts,h=run()
    if sys.argv[1:]==['--finalize']:
        from collections import Counter
        from datetime import datetime, timezone
        analyses={
            2: (['L71-L92','L101-L122','L130-L153'], ['研学内容与资源确认'], '历史AI纪要将儿童两日课程、家长讲座、学校分享大纲列为宣发前置；品牌露出不等于学校盖章认证，午餐和场地尚需日期锁定后确认。1:8仅为当时口述配比，非本轮验证的安全标准。'),
            22: (['T24-T85','T88-T149','T199-T214','T253-T340'], ['管家服务组织','人才成长与招聘'], 'v0.3提出先招服务与学习能力，再按服务半径培养1+N+1复合资质；区分个人牌照和组织资格，晋升依服务案例、复杂度、诚信与带教而非销售额；公司SLA、排班、薪酬和人数仍待确认。'),
            38: (['T5-T21','T23-T31'], ['税务服务与持续档案'], '历史PC-09把年度报税提醒、年度居民身份评估、身份事件复评、文档留存串联；CPA独立委聘收费，RW承担节奏和档案，非保险附带税务结论。法规和市场证据评级未经本轮核验。'),
            42: (['T5-T22','T24-T32'], ['医疗权益激活与专业分工'], '历史PC-03把已含权益激活与自营引荐补位分开，按周年和健康事件触发协办；管家不解读报告或承诺医疗结果，授权先于健康档案。使用率到续保率是待验证经营假设，不是已证因果。'),
            46: (['T3-T14','T15-T67','T68-T73'], ['家庭生命周期产品结构'], '历史融入阶段37项由4货币、21服务、0第三方折扣、12信息组成，重心转为身份、传承及事件触发；不能把第三方折扣为零理解为保费礼遇消失，源文仍在货币类列二代保单折扣。'),
            50: (['L3-L19','L31-L40','L52-L59','L69-L101','L105-L107'], ['客户沟通与转介边界'], '十卡以客户问题组织开场、问答、红线应答，保单问题转持牌同事；医疗未达档不顺推加保、社群场外转办、证据缺口不造假。文中硬窗口、比例、费用、时效与法律断言不是本轮确认事实。'),
            170: (['L9-L33','L68-L103','L105-L125'], ['管家服务组织','岗位能力与上岗'], '主责管家是需求诊断到结单的单一接口，不要求独自专业执行25项；八维能力配合情景和实操考核，四周按规则学习、跟岗、低风险独立、多事项统筹递进。权重及通过线为建议，未证明已有人员达标。'),
            174: (['T21-T82','T119-T177','T196-T205'], ['招聘评估与试点'], 'v0.1将岗位画像转成六环节招聘流程、至少两名面试官独立评分及四种实操作品；红线单独否决，建议先招一名资深负责人跑真实服务单，未确认排班、SLA及招聘数量，不是已发布招聘。'),
        }
        quarantined={
            10: ('L16-L17;L40-L42;L79-L108', '全文含可识别人员评价、业绩管理及技术/法律判断，混合敏感与未知内容，整件隔离；不传播其中人员断言，不把规避工具公开审查的建议当知识。'),
            14: ('L1-L63', '开篇内容辨识发现AI研发投入、算力和技术预算自述，且不限RW业务；仅人工审阅前63行后停止语义分析，整件技术混合待核。全文曾由提取器读入，不声称全文人工读完。'),
            62: ('L4-L16;L18-L35;L47-L88', '正文确认是Phase0交付标准建议、Gate与owner治理材料；已读以辨识类型，不作为业务主题分析完成。'),
            70: ('L9-L31;L50-L108', '正文确认是模型业务确认/变更控制/候选处置记录，属治理材料；Accepted为历史自述，不验证SSOT或授权。'),
            78: ('L3-L16;L99-L122', '正文确认是待MARK审阅的分类轴修订建议，属模型治理；119/635/1020为原文统计自述，不跟随读取被引Office核验。'),
            82: ('L18-L30;L165-L218', '正文确认是原子规范、权限、Gate及机器验收治理文件；Active为原文历史状态，不等于当前有效规范或119项完成。'),
        }
        for r in rows:
            i=r['index']; t=texts.get(str(i),'')
            r['inventory_sha256']=h
            r['read_metric_scope']='单次最终取证快照；read_chars为安全提取的字符量，非累计I/O或真实token'
            r['hash_algorithm']='SHA-256' if r['source_hash'] else None
            r['hash_unavailable_reason']=None if r['source_hash'] else '正文未准入，未为计算hash而额外读取'
            r['analysis_completed']=False
            r['model_review_chars']=0
            r['stat_after']=r.get('stat_after')
            r['stat_stable']=r.get('stat_stable')
            r['external_verification']=False
            if i in analyses and r.get('stat_stable'):
                loc,themes,note=analyses[i]
                r.update(status='已分析',reason='稳定阅读全文并完成逐文语义分析；仅历史资料理解，不代表执行/批准/外发',locators=loc,themes=themes,knowledge=note,analysis_completed=True,model_review_chars=len(t),model_review_lines=f'1-{len(t.splitlines())}')
            elif i in quarantined and r.get('stat_stable'):
                loc,reason=quarantined[i]
                reviewed=t if i!=14 else '\n'.join(t.splitlines()[:63])
                r.update(status='待核',reason=reason,locators=loc.split(';'),model_review_chars=len(reviewed),model_review_lines=f'1-{63 if i==14 else len(t.splitlines())}')
            elif r['status']=='重复':
                r['locators']=['SHA-256全文件字节一致；业务定位承接index=22']
            else:
                r['reason']+='；仅入口/名称风险分流，非正文已核定'
        from shard2_clarified import apply_decisions
        rows=apply_decisions(rows,texts)
        for r in rows:
            r['extracted_chars']=r['read_chars']
            r['read_metric_scope']='单次最终取证快照；read_bytes为hash读取字节，read_chars/extracted_chars为解析文本字符，model_review_chars为实际审阅片段字符；非累计I/O或真实token'
        assert len(rows)==45 and len({r['path'] for r in rows})==45
        assert all(r['index']%4==2 for r in rows)
        for r in rows:
            if r['status']=='重复':
                target=next(x for x in rows if x['path']==r['duplicate_of'])
                assert target['source_hash']==r['source_hash'] and target['status']=='已分析'
            if r['status']=='已分析':
                assert r['knowledge'] and r['locators'] and 0<r['model_review_chars']<=r['read_chars'] and r['stat_stable']
        # This is a generated evidence ledger, not a hand-edited source artifact.
        (BASE/'分片2_处置.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps(dict(total=len(rows),counts=dict(Counter(r['status'] for r in rows)),snapshot_read_chars=sum(r['read_chars'] for r in rows),analyzed_chars=sum(r['read_chars'] for r in rows if r['status']=='已分析'),inventory_sha256=h,generated_at=datetime.now(timezone.utc).isoformat()),ensure_ascii=False))
    elif sys.argv[1:2]==['--slice']:
        start,end=int(sys.argv[2]),int(sys.argv[3])
        for key in sys.argv[4:]:
            t=texts.get(key,'[未提取/重复]')
            print('\n=== INDEX '+key+' | lines='+str(len(t.splitlines()))+' chars='+str(len(t))+' ===')
            print('\n'.join(f'{j}: {s}' for j,s in enumerate(t.splitlines(),1) if start<=j<=end))
    elif len(sys.argv)>1:
        for key in sys.argv[1:]:
            print('\n=== INDEX '+key+' ===')
            print('\n'.join(f'{j}: {s}' for j,s in enumerate(texts.get(key,'[未提取/重复]').splitlines(),1)))
    else:
        print(json.dumps([dict(index=r['index'],status=r['status'],reason=r['reason'],read_chars=r['read_chars']) for r in rows],ensure_ascii=False,indent=2))
