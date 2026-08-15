# xiaojiji-dance 技能包

小击击的技能集合：跳舞 🕺、整理文件 📁、识图 🖼️

## 包含的技能

| 技能 | 说明 | 入口 |
|---|---|---|
| `SKILL.md` | 跳舞（小击击之舞） | `scripts/dance.py` |
| `organize.md` | 按扩展名整理文件 | `scripts/organize.py` |
| `describe.md` | 调用 MIMO 模型识图 | `scripts/describe.py` |

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
```

## 使用

```sh
# 跳舞
scripts/.venv/bin/python scripts/dance.py

# 整理文件（<文件夹路径> 换成目标目录）
scripts/.venv/bin/python scripts/organize.py <文件夹路径>

# 识图（<图片路径> 换成图片，[问题] 可省略）
scripts/.venv/bin/python scripts/describe.py <图片路径> [问题]
```

> 所有脚本都通过 `scripts/.venv/bin/python` 运行——系统 Python 可能没有 `requests` 等依赖，venv 里装好了。
