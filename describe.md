---
name: describe
description: When user ask for read a/some photo or recognize what exactly show of a photo
---

# 识图

当用户要求识别图片内容时：
1. 在当前文件夹运行'scripts/.venv/bin/python scripts/describe.py <用户上传的图片路径> <用户描述的问题>'来识别图片内容，该脚本会调用MIMO模型来识别图片然后给你返回识图结果。
2. 你需要将得到的内容返回给用户。
3. 该skill仅适用于你无法识别的图片，因为你不是多模态模型。
4. 如果用户上传的是文件，比如word文档，则不使用该skill。
5. 如果用户只发了图片，问题可以省略，省略会默认为描述该图片。
6. 不管用户提不提问，你都需要根据MIMO识别图片后返回的结果进行第二次判断，而不是单纯搬运输出。如果MIMO输出是报错，你需要根据报错内容提供解决办法，如果只是普通图片则正常回答用户