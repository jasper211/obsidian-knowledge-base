#!/bin/bash
# Obsidian 自动同步桥接脚本
# fswatch 监听项目目录变化 → 触发 sync_to_obsidian.py
LOG="/Users/zhaoqitrenda.cn/ObsidianVault/.sync_log"

echo "[$(date)] 同步启动" >> "$LOG"
/usr/local/bin/python3 /Users/zhaoqitrenda.cn/ObsidianVault/sync_to_obsidian.py >> "$LOG" 2>&1
echo "[$(date)] 同步完成" >> "$LOG"
