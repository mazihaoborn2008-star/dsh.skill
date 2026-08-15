import os
import base64
import requests
import sys
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path(__file__).parent / ".env")

url = "https://token-plan-cn.xiaomimimo.com/v1/chat/completions"
key = os.environ["MIMO_API_KEY"]

MIME = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".webp": "image/webp",
    ".bmp": "image/bmp",
}

with open(os.path.expanduser(sys.argv[1]), "rb") as f:
    image_data = f.read()

image_b64 = base64.b64encode(image_data).decode()

ext = os.path.splitext(sys.argv[1])[1].lower()
if ext not in MIME:
    print(f"不支持的图片格式{ext}")
    sys.exit(1)
mime = MIME.get(ext)
data_uri = f"data:{mime};base64,{image_b64}"

headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json",
}

question = "描述一下这个图片"
if len(sys.argv) >= 3:
    question = sys.argv[2]

data = {
    "model": "mimo-v2.5",
    "messages": [
        {"role": "user",
         "content": [
             {"type": "text",
              "text": question},
              {"type": "image_url",
               "image_url": {"url": data_uri}}
         ]}
    ]
}

resp = requests.post(url, headers=headers, json=data, timeout=(30, 300))
if resp.status_code != 200:
    print(f"请求失败: {resp.status_code}")
    print(resp.text)
    sys.exit(1)
result = resp.json()["choices"][0]["message"]["content"]
print(result)