import os
import shutil
import sys

RULES = {
    ".jpg": "图片",
    ".png": "图片",
    ".gif": "图片",
    ".mp4": "视频",
    ".mov": "视频",
    ".mp3": "音乐",
    ".txt": "文档",
    ".md": "文档",
    ".pdf": "文档",
}

def organize(folder, root=None):
    if root is None:
        root = folder
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if name in list(RULES.values()) + ["其他"]:
            continue
        if os.path.isdir(path):
            organize(path, root)
            continue
        if os.path.abspath(path) == os.path.abspath(__file__):
            continue
        
        ext = os.path.splitext(name)[1].lower()
        target = RULES.get(ext, "其他")
        dest_dir = os.path.join(root, target)
        os.makedirs(dest_dir, exist_ok = True)

        base, exit2 = os.path.splitext(name)
        new_name = name
        i = 2
        while os.path.exists(os.path.join(dest_dir, new_name)):
            new_name = f"{base} {i}{exit2}"
            i += 1
    
        shutil.move(path, os.path.join(dest_dir, new_name))
        print(f"移动{name} -> {target}")

if len(sys.argv) < 2:
    print("用法: python organize.py <文件夹路径>")
else:
    organize(sys.argv[1])