import random
import sys

actions = [
    "屑屑摇摆：屁股一扭一扭，尾巴翘上天",
    "鬼脸蹦迪：吐舌头翻白眼",
    "黄金右脚：华丽转身假摔收尾",
    "太空步：原地滑行假装在月球",
    "翅膀扑棱：起飞失败，假装在扇风",
]

count = 3

try:
    if len(sys.argv) > 1:
        count = int(sys.argv[1])
except ValueError as e:
    print(e)
    sys.exit()

print("小击击开始跳舞啦！")
for i in range(count):
    print(f"动作{i + 1}: {random.choice(actions)}")

print("跳完啦，给击击比个心❤️")