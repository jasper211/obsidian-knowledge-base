import os, re, json, stat, hashlib
from pathlib import Path
from datetime import datetime, timezone

# Disabled: historical reader acquired full bytes before content type review.
raise SystemExit('Disabled after audit: do not reread sources; use recorded C batch evidence.')

V=Path(__file__).resolve().parents[2]
Q=V/'MOC/OB本地清单/模型338续批冻结输入.json'
raw=Q.read_bytes(); queue=json.loads(raw)
prefix='/Users/a112233/Desktop/业务模型/20_工作包/'
items=sorted(queue['groups']['C'],key=lambda x:x['path'])
assert len(items)==152,len(items)

def snap(p):
    for a in list(Path(p).parents)[::-1]+[Path(p)]:
        if stat.S_ISLNK(os.lstat(a).st_mode): raise ValueError('link rejected')
    s=os.lstat(p)
    if not stat.S_ISREG(s.st_mode): raise ValueError('not regular file')
    return dict(dev=s.st_dev,ino=s.st_ino,size=s.st_size,mtime=s.st_mtime,mtime_ns=str(s.st_mtime_ns),ctime_ns=str(s.st_ctime_ns))

rows=[]; seen={}
for i,x in enumerate(items):
    p=x['path']; n=Path(p).name
    r=dict(id=f'C{i+1:03}',path=p,project_state='在用业务项目（历史执行证据），不等于现实验收',status='待内容复审',reason='',source_hash=None,fragment_hash=None,mtime=None,read_bytes=0,read_chars=0,locators=[],stable=None,token_count=None,analysis_performed=False)
    if any(t in p for t in ['RO邮件草稿','受限确认邮件','三名TR公开','天誉人员名单','客户外键候选源','签署页受控回读']):
        r.update(status='敏感隔离',reason='邮件/个人名单或客户关联/受控签署页边界；不打开，不为hash读取')
    elif any(t in n for t in ['技术确认','技术规则','建表方案','系统Owner确认','KYC_SIGNED来源登记']):
        r.update(status='技术排除',reason='工程技术实现或系统来源登记线索；类型复筛排除，未读取正文')
    elif Path(p).suffix.lower()!='.md':
        r.update(status='类型待核',reason='本批仅实现安全MD读取；其他类型不自动打开')
    try:
        s=snap(p);r.update(mtime=s['mtime'],stat_before=s,mtime_utc=datetime.fromtimestamp(s['mtime'],timezone.utc).isoformat())
    except Exception as e:
        r.update(status='待核',reason=str(e)); rows.append(r);continue
    if r['status']!='待内容复审':
        r.update(hash_scope='未读，hash缺失',stable=None);rows.append(r);continue
    if not 1778389200<=s['mtime']<1794376800:
        r.update(status='窗口排除',reason='固定首次窗口外，不读取正文',hash_scope='未读');rows.append(r);continue
    fd=os.open(p,os.O_RDONLY|os.O_NOFOLLOW)
    try:
        fs=os.fstat(fd);assert fs.st_ino==s['ino'] and fs.st_dev==s['dev']
        chunks=[]
        while True:
            b=os.read(fd,65536)
            if not b:break
            chunks.append(b)
        data=b''.join(chunks)
    finally:os.close(fd)
    after=snap(p);r.update(stat_after=after,stable=s==after,read_bytes=len(data),source_hash=hashlib.sha256(data).hexdigest(),hash_scope='完整源字节SHA256；仅限定文本片段用于语义复审')
    if not r['stable']:
        r.update(status='待核',reason='读取前后stat不稳定');rows.append(r);continue
    txt=data.decode('utf-8-sig',errors='strict');lines=txt.splitlines();parts=[];count=0;fence=False
    for ln,line in enumerate(lines,1):
        if line.lstrip().startswith(('```','~~~')):fence=not fence;continue
        if fence:continue
        if count>=1900 or ln>65:break
        take=line[:1900-count];parts.append([ln,take]);count+=len(take)
    r.update(decoded_chars=len(txt),line_count=len(lines),read_chars=count,locators=[{'line':ln,'chars':len(t)} for ln,t in parts],preview=parts)
    if r['source_hash'] in seen:
        r.update(status='重复',reason='完整源字节SHA256相同',duplicate_of=seen[r['source_hash']])
    else:seen[r['source_hash']]=p
    rows.append(r)
print(json.dumps(dict(queue_hash=hashlib.sha256(raw).hexdigest(),project_state=queue['project_state']['业务模型'],rows=rows),ensure_ascii=False))
