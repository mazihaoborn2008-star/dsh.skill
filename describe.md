---
name: describe
description: When user ask for read a/some photo or recognize what exactly show of a photo
---

# 识图

当用户要求识别图片内容时：
1. 运行 `scripts/.venv/bin/python scripts/describe.py` 识别图片内容：脚本会自动读取当前会话中用户最新一条消息里的**所有图片**（一次全发给 MIMO），然后返回识图结果。
2. 你需要将得到的内容返回给用户。
3. 该 skill 仅适用于你无法识别的图片，因为你不是多模态模型。
4. 如果用户上传的是文件（比如 word 文档），则不使用该 skill。
5. 参数都可省略：只发图片直接跑脚本即可；指定图片传路径（`describe.py <路径> [问题]`）；自动找图时传自定义问题用 `describe.py --question "问题"`。
6. 不管用户提不提问，你都需要根据 MIMO 识别后返回的结果进行第二次判断，而不是单纯搬运输出。如果 MIMO 输出是报错，根据报错内容提供解决办法；普通图片则正常回答用户。
7. 脚本依赖 `zstd` 命令解压会话日志，缺失时提示安装（macOS: `brew install zstd`）。
