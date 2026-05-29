"""Feishu (Lark) custom bot webhook notifier.

Reads webhook URL from env var FEISHU_WEBHOOK. If empty, the call is a no-op so
local runs and forks without secrets still succeed. Optional FEISHU_SECRET
enables signed requests.
"""
from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import time
from typing import Optional

import requests

REQUEST_TIMEOUT = 15


def _sign(secret: str, timestamp: int) -> str:
    string_to_sign = f"{timestamp}\n{secret}"
    h = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256)
    return base64.b64encode(h.digest()).decode("utf-8")


def _escape_md(s: str) -> str:
    return s.replace("[", "\\[").replace("]", "\\]")


def _build_card(date_str: str, total: int, grouped: dict, repo_url: str) -> dict:
    elements: list[dict] = [
        {
            "tag": "div",
            "text": {
                "tag": "lark_md",
                "content": f"**📅 Date (UTC):** {date_str}\n**📚 New papers:** {total}",
            },
        },
        {"tag": "hr"},
    ]

    for topic, papers in grouped.items():
        if not papers:
            continue
        shown = papers[:5]
        lines = [f"**{topic}** ({len(papers)})"]
        for p in shown:
            title = _escape_md(p["title"])
            authors = p["authors"]
            if len(authors) > 80:
                authors = authors[:77] + "..."
            lines.append(f"• [{title}]({p['link']})")
            tldr = p.get("tldr_zh", "").strip()
            if tldr:
                lines.append(f"  💡 {tldr}")
            lines.append(f"  _{authors}_")
        if len(papers) > 5:
            lines.append(f"_... and {len(papers) - 5} more_")
        elements.append({
            "tag": "div",
            "text": {"tag": "lark_md", "content": "\n".join(lines)},
        })

    elements.append({"tag": "hr"})
    elements.append({
        "tag": "action",
        "actions": [
            {
                "tag": "button",
                "text": {"tag": "plain_text", "content": "View full README on GitHub"},
                "type": "primary",
                "url": repo_url,
            }
        ],
    })

    return {
        "msg_type": "interactive",
        "card": {
            "config": {"wide_screen_mode": True},
            "header": {
                "template": "blue",
                "title": {
                    "tag": "plain_text",
                    "content": f"🌟 Awesome Gaussian Splatting — {total} new paper(s)",
                },
            },
            "elements": elements,
        },
    }


def notify(date_str: str, total: int, grouped: dict, repo_url: str) -> bool:
    webhook: Optional[str] = os.environ.get("FEISHU_WEBHOOK", "").strip()
    if not webhook:
        print("[feishu] FEISHU_WEBHOOK not set, skip notification.")
        return False
    if total == 0:
        print("[feishu] zero new papers, skip notification.")
        return False

    payload = _build_card(date_str, total, grouped, repo_url)

    secret = os.environ.get("FEISHU_SECRET", "").strip()
    if secret:
        ts = int(time.time())
        payload["timestamp"] = str(ts)
        payload["sign"] = _sign(secret, ts)

    try:
        resp = requests.post(
            webhook,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"},
            timeout=REQUEST_TIMEOUT,
        )
        body = resp.text
        print(f"[feishu] status={resp.status_code} body={body[:200]}")
        return resp.ok and '"code":0' in body
    except Exception as e:
        print(f"[feishu] notify failed: {e}")
        return False
