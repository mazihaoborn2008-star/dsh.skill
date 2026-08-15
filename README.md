# xiaojiji-dance 技能包

小击击的技能集合：跳舞 🕺、整理文件 📁、识图 🖼️

## 包含的技能

| 技能 | 说明 | 入口 |
|---|---|---|
| `SKILL.md` | 技能总入口（跳舞 + 识图 + 整理） | `scripts/dance.py` / `scripts/describe.py` / `scripts/organize.py` |
| `describe.md` | 调用 MIMO 模型识图（多图一起识别） | `scripts/describe.py` |
| `organize.md` | 按扩展名整理文件 | `scripts/organize.py` |

## 安装（新机器）

```sh
# 1. 克隆到 dsh 技能目录
git clone <你的仓库地址> ~/.dsh/skills/xiaojiji-dance

# 2. 创建虚拟环境并装依赖
cd ~/.dsh/skills/xiaojiji-dance
python3 -m venv scripts/.venv
scripts/.venv/bin/pip install -r requirements.txt

# 3. 配置 API Key（MIMO 识图需要）
cp .env.example scripts/.env
# 编辑 scripts/.env 填入 MIMO_API_KEY

# 4. 安装 zstd（识图脚本解压会话日志需要）
brew install zstd
```

## 使用

```sh
# 跳舞
scripts/.venv/bin/python scripts/dance.py

# 整理文件（<文件夹路径> 换成目标目录）
scripts/.venv/bin/python scripts/organize.py <文件夹路径>

# 识图：自动读取当前会话最新上传的图片（多张一起识别）
scripts/.venv/bin/python scripts/describe.py

# 识图：指定图片和问题
scripts/.venv/bin/python scripts/describe.py <图片路径> [问题]

# 识图：自动找图 + 自定义问题
scripts/.venv/bin/python scripts/describe.py --question "图片里有什么"
```

> 所有脚本都通过 `scripts/.venv/bin/python` 运行——系统 Python 可能没有 `requests` 等依赖，venv 里装好了。

> 识图需要本机装有 `zstd` 命令（macOS: `brew install zstd`），脚本用它解压 DSH 会话日志来定位上传的图片。
