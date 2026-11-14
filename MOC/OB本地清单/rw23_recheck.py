"""Exclusive RW23 review: bounded unbuffered prefixes, no full source hashes."""
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import stat
import sys
import codecs
import os
import subprocess
from html.parser import HTMLParser

BASE=Path(__file__).resolve().parent
OUT=BASE/'RW23再核定.json'
LEDGER=BASE/'295项处置明细.json'
ROOT='/Users/a112233/Desktop/Rw权益项目/'
EXTRA=ROOT+'03_AMANDA/荻邦香港-TOC权益包/续签档案/TOC续签证据完整字段映射图-V5.html'

def safe_open(p):
    mounts=subprocess.check_output(['/sbin/mount'],text=True)
    for line in mounts.splitlines():
        m=re.match(r'.+ on (.+) \((.+)\)$',line)
        if m and (str(p)==m[1] or str(p).startswith(m[1].rstrip('/')+'/')):
            assert 'local' in m[2].split(', '), 'Nonlocal mount boundary'
    fd=os.open('/',os.O_RDONLY|os.O_DIRECTORY)
    try:
        for component in p.parts[1:-1]:
            nxt=os.open(component,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW,dir_fd=fd)
            os.close(fd)
            fd=nxt
        leaf=os.open(p.name,os.O_RDONLY|os.O_NOFOLLOW,dir_fd=fd)
        assert stat.S_ISREG(os.fstat(leaf).st_mode)
        return os.fdopen(leaf,'rb',buffering=0)
    finally:
        os.close(fd)

def st(p):
    s=p.lstat()
    return dict(dev=s.st_dev,ino=s.st_ino,size=s.st_size,mode=s.st_mode,
                mtime_ns=str(s.st_mtime_ns),ctime_ns=str(s.st_ctime_ns),
                mtime_utc=dt.datetime.fromtimestamp(s.st_mtime,dt.timezone.utc).isoformat())

def save(d):
    OUT.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def probe(r,cap=650,max_lines=8):
    assert not r['requires_user'] and r['project_admitted_for_type_probe']
    p=Path(r['path'])
    before=st(p)
    assert stat.S_ISREG(before['mode']) and not p.is_symlink()
    assert p.suffix.lower() in {'.md','.html'}
    assert 1778389200000000000<=int(before['mtime_ns'])<1794376800000000000
    offset=r['fragments'][-1]['byte_end_exclusive'] if r['fragments'] else 0
    start=r['fragments'][-1]['line_end']+1 if r['fragments'] else 1
    raw=bytearray()
    # Unbuffered byte streaming prevents hidden read-ahead into later content.
    with safe_open(p) as f:
        f.seek(offset)
        while len(raw)<cap and raw.count(b'\n')<max_lines and offset+len(raw)<before['size']-1:
            b=f.read(1)
            if not b:
                break
            raw.extend(b)
    # Retain complete lines only; count consumed trailing bytes separately.
    end=raw.rfind(b'\n')+1
    kept=bytes(raw[:end])
    text=kept.decode('utf-8')
    after=st(p)
    f=dict(byte_start=offset,byte_end_exclusive=offset+len(kept),line_start=start,
           line_end=start+kept.count(b'\n')-1,read_bytes=len(raw),read_chars=len(text),
           fragment_sha256=hashlib.sha256(kept).hexdigest() if kept else None,
           hash_scope='仅实际保留前缀字节，非完整文件hash',text=text,
           stat_before=before,stat_after=after,stable=before==after)
    r['fragments'].append(f)
    r['read_bytes']+=len(raw)
    r['read_chars']+=len(text)
    r['content_read']=bool(kept)
    r['stability']='stable' if before==after and before==r['stat_before'] else 'changed_pending_review'
    r['stat_after']=after
    r['locators']=[f"L{x['line_start']}-L{x['line_end']}; bytes[{x['byte_start']},{x['byte_end_exclusive']})" for x in r['fragments'] if x['text']]

def init():
    raw=LEDGER.read_bytes()
    queue=[r for r in json.loads(raw) if r['status']=='技术风险隔离']
    assert len(queue)==23
    d=dict(batch_id='RW23再核定',schema_version='1.0',created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
           input_ledger=str(LEDGER),input_ledger_sha256=hashlib.sha256(raw).hexdigest(),
           window=['2026-05-10T05:00:00Z','2026-11-11T06:00:00Z'],records=[],additional_records=[],
           governance=['MOC/OB执行与独立核查协议_2026-11-10.md',
                       'MOC/OB本地清单/项目入口队列.json:decision=保留筛类型;reason=既有RW准入目录',
                       'MOC/RW业务主题_批量1.md:主题一与主题二',
                       'MOC/RW规则与交付治理MOC_2026-08-13.md:L39-L95',
                       'MOC/RW风险升级与复核MOC_2026-08-13.md:L44-L88'])
    for i,old in enumerate(queue,1):
        r=dict(id=f'R{i:02}',path=old['path'],old_status=old['status'],new_status='待逐项类型复核',
               reason='',evidence_locator=[],requires_user=False,question=None,analysis_needed=False,
               analysis_completed=False,project_admitted_for_type_probe=True,
               source_hash=None,read_bytes=0,read_chars=0,content_read=False,fragments=[],locators=[],
               token_count=None,token_estimate=None,old_mtime=old['mtime'])
        r['stat_before']=st(Path(r['path']))
        r['project_scope']='RW既有准入目录内；本次仅授权安全类型复核，不继承旧content_read_allowed=false为语义判定'
        if i in {3,4}:
            r.update(new_status='项目归属待核_未读正文',requires_user=True,project_admitted_for_type_probe=False,
                     reason='vault已有荻邦三产品业务项目证据，但未证明嵌套荻邦项目工作台codex是该业务交付副本还是独立实验/工程项目；不能仅据目录名定技术',
                     question='荻邦项目工作台codex中的outputs及project-workbench属于在用荻邦业务交付副本，还是独立实验/工程工作台？请给出项目归属/状态依据。',
                     evidence_locator=['MOC/RW业务主题_批量1.md:L23-L29','MOC/OB本地清单/项目入口队列.json:03_AMANDA仅父目录准入'])
        elif not 1778389200000000000<=int(r['stat_before']['mtime_ns'])<1794376800000000000:
            r.update(new_status='窗口外_未读正文',reason='本轮首次mtime不在固定半开窗口内')
        else:
            probe(r)
        d['records'].append(r)
    d['additional_records'].append(dict(id='A01',path=EXTRA,old_status='类型证据不足待核（原分片3为待核）',
        new_status='类型与敏感边界证据不足_保持隔离',reason='vault旧记录明确未读正文，仅由名称提出技术/个人证据字段可能；不足以断言技术或证明无个人实例，不能为了辨型打开潜在个人字段。',
        evidence_locator=['MOC/OB本地清单/分片3_处置.json:index=23;semantic_review;project_scope;read_bytes=0;source_hash=null',
                          'MOC/RW业务主题_批量3.md:L86;L136-L138','MOC/RW业务主题_批量1.md:主题二的客户画像/证据分层'],
        requires_user=True,question='V5是否仅含脱敏字段定义/业务流程而完全不含真实个人实例、证件/联系方式或客户材料？请由保管人提供安全说明或独立脱敏类型摘要，并确认它归属荻邦续签业务设计而非另一个未准入系统项目。',
        analysis_needed=False,analysis_completed=False,content_read=False,read_bytes=0,read_chars=0,
        locators=[],source_hash=None,fragments=[],token_count=None,token_estimate=None,
        stability='not_probed_sensitivity_boundary_unresolved',mtime_source='仅旧vault元数据，未stat或打开源',
        historical_mtime_ns='1787413880262485718',historical_size=42380,
        project_scope='RW父目录归属已知，具体文档用途及无个人实例边界未证明；不自动准入',
        next_condition='保管人提供安全类型/脱敏证据后再评估必要最小片段；其余旧17项未触碰'))
    save(d)
    show(d,1,23)

def show(d,start,end):
    for r in d['records']:
        if start<=int(r['id'][1:])<=end:
            print('\n###',r['id'],Path(r['path']).name,r['new_status'])
            for f in r['fragments']:
                if 'visible_nodes' in f:
                    print('\n'.join(f'L{n}: {t}' for n,t in f['visible_nodes']))
                else:
                    fenced=False
                    for n,t in enumerate(f['text'].splitlines(),f['line_start']):
                        if t.strip().startswith(('```','~~~')):
                            fenced=not fenced
                            continue
                        if not fenced:
                            print(f'L{n}: {t}')

def html_probe():
    d=json.loads(OUT.read_text())
    r=d['records'][4]
    p=Path(r['path'])
    before=st(p)
    assert before==r['stat_before']
    class P(HTMLParser):
        def __init__(self):
            super().__init__()
            self.hidden=[]
            self.nodes=[]
        def handle_starttag(self,tag,attrs):
            a=dict(attrs)
            hide=(tag in {'head','style','script','template','noscript'} or 'hidden' in a or a.get('aria-hidden')=='true' or
                  bool(re.search(r'display\s*:\s*none|visibility\s*:\s*hidden',a.get('style',''))))
            if tag not in {'meta','link','br','hr','img','input','wbr','source'}:
                self.hidden.append((tag,hide))
        def handle_endtag(self,tag):
            for n in range(len(self.hidden)-1,-1,-1):
                if self.hidden[n][0]==tag:
                    del self.hidden[n:]
                    break
        def handle_data(self,t):
            if not any(h for _,h in self.hidden) and t.strip():
                self.nodes.append((self.getpos()[0],t.strip()))
    parser=P()
    decoder=codecs.getincrementaldecoder('utf-8')()
    raw=bytearray()
    with safe_open(p) as f:
        while len(raw)<min(10000,before['size']-1):
            b=f.read(1)
            if not b:
                break
            raw.extend(b)
            ch=decoder.decode(b)
            parser.feed(ch)
            if sum(len(t) for _,t in parser.nodes)>=650 and ch=='>':
                break
    after=st(p)
    # Byte-wise parsing can split text nodes. Coalesce adjacent source lines.
    nodes=[]
    for line,t in parser.nodes:
        if nodes and nodes[-1][0]==line:
            nodes[-1][1]+=t
        else:
            nodes.append([line,t])
    frag=dict(byte_start=0,byte_end_exclusive=len(raw),line_start=1,line_end=raw.count(b'\n')+1,
              read_bytes=len(raw),read_chars=sum(len(t) for _,t in nodes),visible_nodes=nodes,
              fragment_sha256=hashlib.sha256(raw).hexdigest(),hash_scope='流式HTML前缀，非全文件；脚本样式隐藏区不作依据',
              stat_before=before,stat_after=after,stable=before==after,text='')
    r['fragments'].append(frag)
    r['read_bytes']+=len(raw)
    r['read_chars']+=frag['read_chars']
    r['stat_after']=after
    r['stability']='stable' if before==after else 'changed_pending_review'
    r['locators'].append(f"HTML可见文本L{nodes[0][0]}-L{nodes[-1][0]}; raw bytes[0,{len(raw)})" if nodes else f'仅HTML前缀bytes[0,{len(raw)})，未获得可见业务正文')
    save(d)
    print(json.dumps(dict(read_bytes=len(raw),visible_nodes=nodes),ensure_ascii=False,indent=2))

def finalize():
    d=json.loads(OUT.read_text())
    decisions={
      1:('业务必要片段已分析','正文定位为续签准备度管理，明确不预测成功率、不承诺审批；仅提取服务边界。','L3-L4;L12;L25-L30'),
      2:('低复用仅溯源','正文说明是用户可见对话归档；只确认档案用途，不展开对话、附件或个人材料。','L3-L6;L10-L20'),
      5:('类型证据不足待核','限量HTML前缀未获得可见业务正文；样式存在不能证明工程类型，停止扩读。','L1-L8;bytes[0,10000)'),
      6:('技术确认排除','正文指定应用连接器、触发限制及自动化命名，已足以确认技术配置；立即停止。','L3-L5'),
      7:('业务必要片段已分析','非代码围栏文字定义运行/停止治理与内外环路由；不分析围栏内容，不证明实际执行。','L2-L3;L21'),
      8:('业务必要片段已分析','非代码围栏文字定义静态产物合同、客户权益阶段及空锚点约束；不分析YAML或校准统计。','L2-L3;L22'),
      9:('技术确认排除','正文用途为Codex持续配置及工具最佳实践，非业务交付规则；停止。','L4-L8'),
      10:('业务必要片段已分析','正文是Phase0任务结果、上下文、原件保护、版本及人工确认约束，不因Agent名称排除。','L3;L13;L27-L32'),
      11:('业务必要片段已分析','仅提取候选非现行、结构检查不能替代语义标准化验收的历史结论；未核验结构统计。','L3-L13'),
      12:('业务必要片段已分析','仅提取候选与最终交付物语义验收的区分；无FAIL不等于正式接纳，未核验引用产物。','L3-L13'),
      13:('业务必要片段已分析','仅提取交付物家族与合同对齐的业务验收缺口；不将源报告自述当实测。','L3-L13'),
      14:('业务必要片段已分析','报告声称内部标准化基线接纳，但明确非现行非外发，Owner/财务/合规/证据成熟度待办仍保留。','L3-L7;L13'),
      15:('混合技术隔离','后续最小片段出现具体工具加载及产物生成实现，确认混合；停止，不提炼其工程验收或推广完成结论。','L7;L11'),
      16:('技术确认排除','必要前缀出现系统字段到数据库字段映射及落库定义，确认技术类型；未访问数据库。','L10-L16'),
      17:('技术确认排除','正文自定为技术预备/数据结构预设计，并说明不代表解锁；停止。','L4-L5'),
      18:('技术确认排除','正文明确DB预设计草案、不创建真实数据库、不代表解锁；停止。','L4-L5'),
      19:('技术确认排除','正文执行范围为DB建表及导入校验草案；completed仅文内声称，不验证执行。','L4-L5'),
      20:('业务必要片段已分析','仅提取匿名汇总内部用途、正式报表缺源、财务确认及外发门禁，不采信结构复核计数。','L34-L45'),
      21:('业务必要片段已分析','通过仅指正式报表缺源已如实记载；模板/字典工作不等于正式保司报表可外发。','L30-L32'),
      22:('业务必要片段已分析','项目配置包属于内部工作基线，source_absent及Gate仍限制客户/商业/对外使用；未复验数量。','L22;L28-L33'),
      23:('业务必要片段已分析','正文是Phase0交付治理、SSOT及任务验收约束；源AGENTS不构成本轮扩权指令。','L5-L11;L17-L27')}
    metrics={k:dict(read_bytes=0,read_chars=0,fragment_reads=0,files=[]) for k in ['type_identification','business_fragment']}
    business_second={1,7,8,10,21,22,23}
    for i,r in enumerate(d['records'],1):
        if i in decisions:
            status,reason,loc=decisions[i]
            r.update(new_status=status,reason=reason,evidence_locator=[r['path']+':'+loc])
        if i==5:
            r.update(requires_user=True,question='请提供该工作台的安全可见文本摘要，确认业务进度展示或工程日志用途；当前限量前缀不足，不继续穿透样式/脚本。')
        r['status']=r['new_status']
        r['analysis_completed']=r['new_status']=='业务必要片段已分析'
        r['analysis_needed']=r['analysis_completed']
        r['analysis_scope']='仅所列业务片段；非全文核定' if r['analysis_completed'] else '未作业务分析'
        r['read_metrics']={k:dict(read_bytes=0,read_chars=0) for k in metrics}
        for j,f in enumerate(r['fragments']):
            purpose='business_fragment' if (j>0 and i in business_second) or (i==20 and j==2) else 'type_identification'
            f['purpose']=purpose
            for key in ['read_bytes','read_chars']:
                metrics[purpose][key]+=f[key]
                r['read_metrics'][purpose][key]+=f[key]
            metrics[purpose]['fragment_reads']+=1
            if r['path'] not in metrics[purpose]['files']:
                metrics[purpose]['files'].append(r['path'])
            f.pop('text',None)
            f.pop('visible_nodes',None)
        ancestors=[]
        for ancestor in reversed(Path(r['path']).parents):
            s=ancestor.lstat()
            ancestors.append(dict(path=str(ancestor),is_symlink=stat.S_ISLNK(s.st_mode),dev=s.st_dev))
        r['path_guard_audit']=dict(ancestors=ancestors,all_ancestors_non_symlink=not any(x['is_symlink'] for x in ancestors),
            timing='事后仅元数据核查；不能追认先前读取具备dirfd防竞态保障',prior_reads_dirfd_guarded=False,
            mount_check='本轮mount显示源路径所经卷为local APFS，无网络挂载；不追读正文')
        r.setdefault('stability','not_read_project_scope_unresolved')
        if r['read_bytes']:
            after=st(Path(r['path']))
            r['final_metadata']=after
            r['stability']='stable' if after==r['stat_before'] else 'changed_pending_review'
    for r in d['additional_records']:
        r['status']=r['new_status']
        r['sidecar_only']=True
        r['old_hash_overwritten']=False
    from collections import Counter
    d['counts']=dict(records=len(d['records']),additional_records=len(d['additional_records']),
        by_status=dict(Counter(r['status'] for r in d['records'])),business_analysis_files=sum(r['analysis_completed'] for r in d['records']),
        source_read_files=sum(r['read_bytes']>0 for r in d['records']),full_source_hash_reads=0)
    for m in metrics.values():
        m['file_count']=len(m.pop('files'))
    d['read_metrics']=dict(**metrics,total_read_bytes=sum(r['read_bytes'] for r in d['records']),
        total_read_chars=sum(r['read_chars'] for r in d['records']),additional_read_bytes=0,additional_read_chars=0,
        token_count=None,scope='本轮源读取I/O；不含vault治理资料。按读取目的互斥计量，类型片段复用于业务判断不重复计费。字符为保留完整文本字符，HTML过滤扫描只计可见字符；字节含截断和重叠实读，非唯一字节数。')
    d['historical_boundary']='均为历史设计/报告文内声称；未验证现实执行、审批、财务、外发或验收；不晋升现行基线。'
    d['independent_review']=dict(reviewer='James',status='待送审_当前工具未定位接收会话',notification_sent=False)
    d['finalized_utc']=dt.datetime.now(dt.timezone.utc).isoformat()
    expected={r['path'] for r in json.loads(LEDGER.read_text()) if r['status']=='技术风险隔离'}
    assert len(expected)==23 and expected=={r['path'] for r in d['records']}
    assert len({r['path'] for r in d['records']})==23
    assert not any(r['new_status']=='待逐项类型复核' for r in d['records'])
    assert all(r['reason'] and r['evidence_locator'] for r in d['records'])
    assert all(r['stability']=='stable' for r in d['records'] if r['read_bytes'])
    assert all(r['path_guard_audit']['all_ancestors_non_symlink'] for r in d['records'])
    d['self_check']='23原队列集合相等且无重复；附项独立；字段完整；21读取项元数据稳定；无全文源hash；非独立核查'
    save(d)
    print(json.dumps(dict(counts=d['counts'],read_metrics=d['read_metrics']),ensure_ascii=False,indent=2))

if __name__=='__main__':
    if sys.argv[1]=='init':
        init()
    elif sys.argv[1]=='show':
        show(json.loads(OUT.read_text()),int(sys.argv[2]),int(sys.argv[3]))
    elif sys.argv[1]=='probe':
        d=json.loads(OUT.read_text())
        r=d['records'][int(sys.argv[2])-1]
        probe(r,int(sys.argv[3]),int(sys.argv[4]))
        save(d)
        show(d,int(sys.argv[2]),int(sys.argv[2]))
    elif sys.argv[1]=='html':
        html_probe()
    elif sys.argv[1]=='finalize':
        finalize()
