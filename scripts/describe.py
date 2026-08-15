import os
import sys
import json
import base64
import subprocess
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

url = "https://token-plan-cn.xiaomimimo.com/v1/chat/completions"
key = os.environ["MIMO_API_KEY"]

ATTACH_DIR = Path.home() / ".dsh/attachments/v1/objects"

EXT2MIME = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
            ".gif": "image/gif", ".webp": "image/webp", ".bmp": "image/bmp"}


def current_session() -> Path:
    """当前工作区的最新会话；工作区目录不存在时全盘兜底"""
    tag = "--" + os.getcwd().replace("/", "-") + "--"
    cand = Path.home() / ".dsh/sessions" / tag
    if cand.exists():
        sessions = sorted(cand.glob("session-*"),
                          key=lambda p: p.stat().st_mtime, reverse=True)
        if sessions:
            return sessions[0]
    all_sessions = sorted((Path.home() / ".dsh/sessions").glob("*/session-*"),
                          key=lambda p: p.stat().st_mtime, reverse=True)
    if not all_sessions:
        raise FileNotFoundError("没有任何会话记录")
    return all_sessions[0]


def uploaded_image_messages(session_dir: Path | None = None) -> list[list[dict]]:
    """解析会话日志，返回每条含图用户消息的图片附件列表（按消息顺序）"""
    session_dir = session_dir or current_session()
    log = session_dir / "session.jsonl.zstd"
    raw = subprocess.run(["zstd", "-d", "-c", str(log)],
                         capture_output=True, check=True).stdout

    messages = []
    for line in raw.decode("utf-8", "replace").splitlines():
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if e.get("type") != "user/message":
            continue
        imgs = []
        for item in e.get("data", {}).get("content", []):
            if item.get("type") != "image":
                continue
            att = dict(item["attachment"])
            sha = att["attachmentId"].split(":", 1)[1]  # 去掉 sha256: 前缀
            att["path"] = Path(ATTACH_DIR) / sha[:2] / sha
            imgs.append(att)
        if imgs:
            messages.append(imgs)
    return messages


def resolve_images(path_arg: str | None) -> tuple[list[tuple[Path, str]], list[str]]:
    """返回 (图片路径, mediaType) 列表与文件名列表：传了路径用路径，否则取最新一条含图消息的全部图片"""
    if path_arg:
        p = Path(os.path.expanduser(path_arg))
        mime = EXT2MIME.get(p.suffix.lower())
        if not mime:
            sys.exit(f"不支持的图片格式{p.suffix}")
        return [(p, mime)], [p.name]
    msgs = uploaded_image_messages()
    if not msgs:
        sys.exit("会话里没找到上传的图片，请直接传图片路径")
    latest = msgs[-1]
    return [(att["path"], att["mediaType"]) for att in latest], [att["name"] for att in latest]


def parse_args() -> tuple[str | None, str | None]:
    """解析参数：`[图片路径] [问题]`，自动找图时用 `--question 问题`"""
    args = sys.argv[1:]
    if args and args[0] in ("-q", "--question"):
        return None, args[1] if len(args) > 1 else None
    if args:
        return args[0], args[1] if len(args) > 1 else None
    return None, None


path_arg, question = parse_args()
imgs, names = resolve_images(path_arg)

for p, _ in imgs:
    if not p.exists():
        sys.exit(f"文件不存在: {p}")

print(f"识别 {len(imgs)} 张图片: {', '.join(names)}")

content = [{"type": "text", "text": question or f"描述一下这{'些' if len(imgs) > 1 else '张'}图片"}]
for p, mime in imgs:
    b64 = base64.b64encode(p.read_bytes()).decode()
    content.append({"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}"}})

data = {"model": "mimo-v2.5", "messages": [{"role": "user", "content": content}]}

resp = requests.post(url,
                     headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                     json=data, timeout=(30, 300))
if resp.status_code != 200:
    print(f"请求失败: {resp.status_code}")
    print(resp.text)
    sys.exit(1)
print(resp.json()["choices"][0]["message"]["content"])
