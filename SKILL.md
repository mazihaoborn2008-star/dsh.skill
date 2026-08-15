---
name: xiaojiji-dance
description: Use when 击击 asks for a dance (跳舞/舞蹈/庆祝), asks to read or recognize a photo (识图/看图/识别图片/这张图是什么), or asks to organize files (整理文件) — 小击击技能包
---

# 小击击技能包

## 🕺 跳舞

当击击要求跳舞/庆祝时：
1. 在技能目录下运行 `scripts/.venv/bin/python scripts/dance.py`
2. 把脚本输出的舞蹈动作完整呈现给击击
3. 如果脚本执行失败，才手动编三个屑屑的动作

## 🖼️ 识图

当击击要求识别图片内容时，按 `describe.md` 执行：
运行 `scripts/.venv/bin/python scripts/describe.py`（自动读取当前会话最新上传的图片，也可传路径/问题），调用 MIMO 识别后，对结果做二次判断再回答击击。

## 📁 整理文件

当击击要求整理文件时，按 `organize.md` 执行：
运行 `scripts/.venv/bin/python scripts/organize.py <文件夹路径>`。
