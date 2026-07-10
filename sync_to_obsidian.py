#!/usr/bin/env python3
"""v3.0 - 保留目录结构"""
import os, sys, datetime

SOURCE = "/Users/zhaoqitrenda.cn/Desktop/流程架构项目_jasper"
VAULT  = "/Users/zhaoqitrenda.cn/ObsidianVault"
PROJ   = os.path.join(VAULT, "项目-流程架构")

DRY_RUN = "--dry-run" in sys.argv
EXCLUDE_DIRS = {".stfolder", ".git", ".git_backup", ".obsidian", ".claude", "node_modules", "__pycache__"}
EXCLUDE_FILES = {"CLAUDE.md"}
ATTACH_EXTS = {".csv", ".xlsx", ".json", ".py", ".html", ".sql", ".txt", ".docx", ".pdf", ".pptx"}

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f: return f.read()
    except UnicodeDecodeError:
        with open(path, "r", encoding="utf-8", errors="replace") as f: return f.read()

def count_lines(path):
    try:
        with open(path, "r", encoding="utf-8") as f: return sum(1 for _ in f) - 1
    except: return 0

def sync_md(src, rel):
    fname = os.path.basename(src)
    if fname in EXCLUDE_FILES: return None
    d = os.path.join(PROJ, os.path.dirname(rel))
    dp = os.path.join(d, fname)
    if os.path.exists(dp) and os.path.getmtime(src) <= os.path.getmtime(dp): return None
    os.makedirs(d, exist_ok=True)
    c = read_file(src)
    y = "" if c.startswith("---") else f"---\ntype: 项目笔记\nsource: {os.path.dirname(rel)}\nsynced: {datetime.date.today().isoformat()}\ntags: [项目]\n---\n\n"
    if DRY_RUN: print(f"  [MD] {rel}"); return fname
    with open(dp, "w", encoding="utf-8") as f: f.write(y + c)
    return fname

def sync_att(src, rel):
    fname = os.path.basename(src)
    ad = os.path.join(PROJ, os.path.dirname(rel), "_附件")
    cn = fname.rsplit(".", 1)[0] + ".md"
    cp = os.path.join(ad, cn)
    if os.path.exists(cp) and os.path.getmtime(src) <= os.path.getmtime(cp): return None
    os.makedirs(ad, exist_ok=True)
    ext = os.path.splitext(fname)[1]
    fs = os.path.getsize(src)
    fh = f"{fs/1024:.1f}KB" if fs > 1024 else f"{fs}B"
    rows = count_lines(src) if ext == ".csv" else 0
    card = f"---\ntype: 附件索引卡\nformat: {ext[1:]}\nsource: {os.path.dirname(rel)}\nsize: {fh}\nsynced: {datetime.date.today().isoformat()}\ntags: [附件, {ext[1:]}]\n---\n\n# {fname}\n\n- 格式: {ext[1:].upper()}\n- 大小: {fh}\n"
    if rows > 0: card += f"- 数据行: {rows}\n"
    card += f"- 来源: {os.path.dirname(rel)}/\n"
    if DRY_RUN: print(f"  [{ext[1:].upper()}] {rel}"); return fname
    with open(cp, "w", encoding="utf-8") as f: f.write(card)
    return fname

def main():
    mc = ac = sc = ec = 0
    for root, dirs, files in os.walk(SOURCE):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for fn in files:
            if fn.startswith("."): continue
            sp = os.path.join(root, fn)
            rp = os.path.relpath(sp, SOURCE)
            try:
                if fn.endswith(".md"):
                    r = sync_md(sp, rp)
                    if r: mc += 1
                    else: sc += 1
                elif any(fn.endswith(e) for e in ATTACH_EXTS):
                    r = sync_att(sp, rp)
                    if r: ac += 1
                    else: sc += 1
            except Exception as e:
                ec += 1
                if not DRY_RUN: print(f"  ERR {rp}: {e}")
    a = "将同步" if DRY_RUN else "已同步"
    print(f"{a}: {mc} MD + {ac} 附件 ({sc} 跳过)" + (f" + {ec} 错误" if ec else ""))

if __name__ == "__main__": main()
