"""Chinese TL;DR generator via any OpenAI-compatible Chat Completions endpoint.

This module is intentionally backend-agnostic. You configure where the calls go
via environment variables; the script itself contains NO hard-coded endpoints,
keys, or model names. Set in your CI secrets:

    OPENAI_BASE_URL   e.g. https://api.deepseek.com/v1  or  https://api.openai.com/v1
    OPENAI_API_KEY    your key
    OPENAI_MODEL      e.g. deepseek-chat / gpt-4o-mini / moonshot-v1-8k / ...

If any of them is missing, the function is a no-op and returns an empty string
so the pipeline keeps working without LLM enrichment.

Design notes:
- Persisted cache `data/tldr.json` (arxiv_id -> tldr) avoids regenerating.
- One paper per request keeps prompts short and failures isolated.
- Hard timeout + small retry, never blocks the daily job.
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from typing import Optional

import requests

ROOT = Path(__file__).resolve().parent.parent
CACHE_FILE = ROOT / "data" / "tldr.json"

REQUEST_TIMEOUT = 30
MAX_RETRIES = 2
SLEEP_BETWEEN = 0.6
MAX_ABSTRACT_CHARS = 1800  # truncate very long abstracts to keep prompt small

SYSTEM_PROMPT = (
    "你是一名计算机视觉/图形学方向的资深科研助理，专注于 Gaussian Splatting (3DGS/4DGS) 相关论文。"
    "请用一句**简体中文**总结给定论文，要求："
    "(1) 不超过 60 字；"
    "(2) 点出问题、方法关键词与主要贡献；"
    "(3) 不要复述标题，不要加 'TL;DR'/'本文' 等冗余前缀；"
    "(4) 直接输出一句话，不要使用引号、Markdown 或换行。"
)


def _load_cache() -> dict:
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def _save_cache(cache: dict) -> None:
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def _llm_available() -> bool:
    return bool(os.environ.get("OPENAI_BASE_URL") and os.environ.get("OPENAI_API_KEY") and os.environ.get("OPENAI_MODEL"))


def _call_llm(title: str, abstract: str) -> str:
    base_url = os.environ["OPENAI_BASE_URL"].rstrip("/")
    api_key = os.environ["OPENAI_API_KEY"]
    model = os.environ["OPENAI_MODEL"]

    url = f"{base_url}/chat/completions"
    abstract = abstract[:MAX_ABSTRACT_CHARS]
    user_prompt = f"标题: {title}\n\n摘要: {abstract}\n\n请输出一句中文 TL;DR。"

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.3,
        "max_tokens": 200,
        "stream": False,
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    last_err: Optional[str] = None
    for attempt in range(MAX_RETRIES + 1):
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=REQUEST_TIMEOUT)
            if resp.status_code >= 400:
                last_err = f"HTTP {resp.status_code}: {resp.text[:200]}"
            else:
                data = resp.json()
                content = (
                    data.get("choices", [{}])[0]
                    .get("message", {})
                    .get("content", "")
                    .strip()
                )
                # Strip any wrapping quotes/asterisks the model might add
                content = content.strip("`\"' \n")
                # Single line only
                content = content.split("\n")[0].strip()
                if content:
                    return content
                last_err = "empty content"
        except Exception as e:
            last_err = str(e)
        time.sleep(SLEEP_BETWEEN * (attempt + 1))

    print(f"[tldr] failed after retries: {last_err}", file=sys.stderr)
    return ""


def enrich(papers: list[dict]) -> None:
    """Mutate each paper dict in place by adding a `tldr_zh` field.

    Skips silently if LLM env vars are unset (so the pipeline still works).
    """
    cache = _load_cache()
    available = _llm_available()
    if not available:
        print("[tldr] OPENAI_* env vars not set, skip LLM enrichment.")

    for p in papers:
        arxiv_id = p["id"]
        if arxiv_id in cache and cache[arxiv_id]:
            p["tldr_zh"] = cache[arxiv_id]
            continue
        if not available:
            p["tldr_zh"] = ""
            continue
        try:
            tldr = _call_llm(p["title"], p.get("summary", ""))
        except Exception as e:
            print(f"[tldr] unexpected error on {arxiv_id}: {e}", file=sys.stderr)
            tldr = ""
        p["tldr_zh"] = tldr
        if tldr:
            cache[arxiv_id] = tldr
            # Persist incrementally so a mid-run failure doesn't lose progress.
            _save_cache(cache)
        time.sleep(SLEEP_BETWEEN)

    _save_cache(cache)
