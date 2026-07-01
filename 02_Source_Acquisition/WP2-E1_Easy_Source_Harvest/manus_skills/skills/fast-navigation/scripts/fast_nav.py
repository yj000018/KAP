#!/usr/bin/env python3
"""
fast_nav.py — Fast Navigation v2.0
Ultra-fast programmatic web toolkit for Manus sandbox.
Usage: python3 fast_nav.py <command> [args]
"""

import sys
import os
import json
import asyncio
import hashlib
import time
import sqlite3
from pathlib import Path
from datetime import datetime, timedelta

# ── Lazy imports (installed on demand) ──────────────────────────────────────

def ensure_deps():
    import subprocess
    pkgs = []
    try:
        import httpx
    except ImportError:
        pkgs.append("httpx[http2]")
    try:
        import selectolax
    except ImportError:
        pkgs.append("selectolax")
    try:
        import orjson
    except ImportError:
        pkgs.append("orjson")
    if pkgs:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--quiet"] + pkgs,
            check=True
        )

ensure_deps()

import httpx
from selectolax.parser import HTMLParser
import orjson

# ── Cache ────────────────────────────────────────────────────────────────────

CACHE_DIR = Path.home() / ".fast_nav_cache"
CACHE_DIR.mkdir(exist_ok=True)
CACHE_DB = CACHE_DIR / "cache.db"
DEFAULT_TTL = 3600  # 1 hour

def _cache_key(url: str) -> str:
    return hashlib.sha256(url.encode()).hexdigest()

def _cache_get(url: str):
    conn = sqlite3.connect(CACHE_DB)
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS cache (key TEXT PRIMARY KEY, data TEXT, expires REAL)"
    )
    c.execute("SELECT data, expires FROM cache WHERE key=?", (_cache_key(url),))
    row = c.fetchone()
    conn.close()
    if row and time.time() < row[1]:
        return row[0]
    return None

def _cache_set(url: str, data: str, ttl: int = DEFAULT_TTL):
    conn = sqlite3.connect(CACHE_DB)
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS cache (key TEXT PRIMARY KEY, data TEXT, expires REAL)"
    )
    c.execute(
        "INSERT OR REPLACE INTO cache VALUES (?,?,?)",
        (_cache_key(url), data, time.time() + ttl)
    )
    conn.commit()
    conn.close()

def cache_clear():
    if CACHE_DB.exists():
        CACHE_DB.unlink()
    print("Cache cleared.")

# ── HTTP helpers ─────────────────────────────────────────────────────────────

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

def _get_sync(url: str, cookies=None) -> httpx.Response:
    with httpx.Client(
        http2=True,
        follow_redirects=True,
        timeout=30,
        headers=HEADERS,
        cookies=cookies or {},
    ) as client:
        return client.get(url)

async def _get_async(url: str) -> tuple:
    async with httpx.AsyncClient(
        http2=True,
        follow_redirects=True,
        timeout=30,
        headers=HEADERS,
    ) as client:
        r = await client.get(url)
        return url, r

# ── HTML text extraction ─────────────────────────────────────────────────────

NOISE_TAGS = {"script", "style", "nav", "footer", "header", "aside", "noscript"}

def _extract_text(html: str, selector: str = None) -> str:
    tree = HTMLParser(html)
    if selector:
        nodes = tree.css(selector)
        return "\n".join(n.text(strip=True) for n in nodes)
    # Remove noise tags
    for tag in NOISE_TAGS:
        for node in tree.css(tag):
            node.decompose()
    body = tree.css_first("main") or tree.css_first("article") or tree.css_first("body")
    if body:
        return body.text(strip=True, separator="\n")
    return tree.body.text(strip=True, separator="\n") if tree.body else ""

# ── Cookie bridge ────────────────────────────────────────────────────────────

COOKIE_STORE = CACHE_DIR / "browser_cookies.json"

def bridge_cookies():
    """Extract cookies from Chromium profile and save to JSON."""
    import glob
    import struct

    cookie_paths = glob.glob(
        os.path.expanduser("~/.config/chromium/Default/Cookies")
    ) + glob.glob(
        os.path.expanduser("~/.config/google-chrome/Default/Cookies")
    )

    if not cookie_paths:
        print("No browser cookie store found.")
        return {}

    conn = sqlite3.connect(cookie_paths[0])
    c = conn.cursor()
    c.execute("SELECT host_key, name, value, path, expires_utc FROM cookies")
    rows = c.fetchall()
    conn.close()

    cookies = {}
    for host, name, value, path, expires in rows:
        domain = host.lstrip(".")
        if domain not in cookies:
            cookies[domain] = {}
        cookies[domain][name] = value

    COOKIE_STORE.write_text(json.dumps(cookies, indent=2))
    print(f"Bridged {sum(len(v) for v in cookies.values())} cookies from {len(cookies)} domains → {COOKIE_STORE}")
    return cookies

def _load_cookies(domain: str = None) -> dict:
    if not COOKIE_STORE.exists():
        bridge_cookies()
    if not COOKIE_STORE.exists():
        return {}
    all_cookies = json.loads(COOKIE_STORE.read_text())
    if domain:
        # Match domain and subdomains
        result = {}
        for d, cookies in all_cookies.items():
            if domain in d or d in domain:
                result.update(cookies)
        return result
    # Flatten all
    flat = {}
    for cookies in all_cookies.values():
        flat.update(cookies)
    return flat

# ── Commands ─────────────────────────────────────────────────────────────────

def cmd_fetch(url: str) -> str:
    cached = _cache_get(url)
    if cached:
        return cached
    r = _get_sync(url)
    result = _extract_text(r.text)
    _cache_set(url, result)
    return result

def cmd_auto(url: str) -> str:
    cached = _cache_get(url)
    if cached:
        return cached
    r = _get_sync(url)
    ct = r.headers.get("content-type", "")
    if "json" in ct:
        result = json.dumps(orjson.loads(r.content), indent=2, ensure_ascii=False)
    elif "xml" in ct:
        result = r.text
    else:
        result = _extract_text(r.text)
    _cache_set(url, result)
    return result

def cmd_extract(url: str, selector: str = None) -> str:
    key = f"{url}||{selector}"
    cached = _cache_get(key)
    if cached:
        return cached
    r = _get_sync(url)
    result = _extract_text(r.text, selector)
    _cache_set(key, result)
    return result

def cmd_json(url: str) -> str:
    cached = _cache_get(url)
    if cached:
        return cached
    r = _get_sync(url)
    result = json.dumps(orjson.loads(r.content), indent=2, ensure_ascii=False)
    _cache_set(url, result)
    return result

def cmd_jsonld(url: str) -> str:
    r = _get_sync(url)
    tree = HTMLParser(r.text)
    scripts = tree.css('script[type="application/ld+json"]')
    items = []
    for s in scripts:
        try:
            items.append(orjson.loads(s.text()))
        except Exception:
            pass
    return json.dumps(items, indent=2, ensure_ascii=False)

async def _multi_async(urls: list) -> list:
    tasks = [_get_async(u) for u in urls]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    out = []
    for url, res in results:
        if isinstance(res, Exception):
            out.append({"url": url, "error": str(res)})
        else:
            out.append({"url": url, "status": res.status_code, "text": _extract_text(res.text)[:2000]})
    return out

def cmd_multi(urls: list) -> str:
    results = asyncio.run(_multi_async(urls))
    return json.dumps(results, indent=2, ensure_ascii=False)

async def _status_async(urls: list) -> list:
    tasks = [_get_async(u) for u in urls]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    out = []
    for url, res in results:
        if isinstance(res, Exception):
            out.append({"url": url, "status": "error", "detail": str(res)})
        else:
            out.append({"url": url, "status": res.status_code})
    return out

def cmd_status(urls: list) -> str:
    results = asyncio.run(_status_async(urls))
    return json.dumps(results, indent=2, ensure_ascii=False)

def cmd_auth(url: str, domain: str = None) -> str:
    if domain is None:
        from urllib.parse import urlparse
        domain = urlparse(url).netloc
    cookies = _load_cookies(domain)
    r = _get_sync(url, cookies=cookies)
    return _extract_text(r.text)

def cmd_decide(task: str) -> str:
    task_lower = task.lower()
    if any(k in task_lower for k in ["api", "json", "rest", "graphql"]):
        return "→ Use: `json <url>` or `auto <url>`"
    if any(k in task_lower for k in ["login", "auth", "session", "cookie"]):
        return "→ Use: `bridge` then `auth <url> [domain]`"
    if any(k in task_lower for k in ["multiple", "several", "list of", "batch"]):
        return "→ Use: `multi <url1> <url2> ...`"
    if any(k in task_lower for k in ["status", "check", "alive", "up"]):
        return "→ Use: `status <url1> <url2> ...`"
    if any(k in task_lower for k in ["structured", "schema", "ld+json", "seo"]):
        return "→ Use: `jsonld <url>`"
    if any(k in task_lower for k in ["css", "selector", "specific element", "table", "div"]):
        return "→ Use: `extract <url> <css_selector>`"
    return "→ Use: `auto <url>` (recommended default)"

# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)

    cmd = args[0].lower()

    if cmd == "fetch" and len(args) >= 2:
        print(cmd_fetch(args[1]))
    elif cmd == "auto" and len(args) >= 2:
        print(cmd_auto(args[1]))
    elif cmd == "extract" and len(args) >= 2:
        selector = args[2] if len(args) >= 3 else None
        print(cmd_extract(args[1], selector))
    elif cmd == "json" and len(args) >= 2:
        print(cmd_json(args[1]))
    elif cmd == "jsonld" and len(args) >= 2:
        print(cmd_jsonld(args[1]))
    elif cmd == "multi" and len(args) >= 2:
        print(cmd_multi(args[1:]))
    elif cmd == "status" and len(args) >= 2:
        print(cmd_status(args[1:]))
    elif cmd == "auth" and len(args) >= 2:
        domain = args[2] if len(args) >= 3 else None
        print(cmd_auth(args[1], domain))
    elif cmd == "bridge":
        bridge_cookies()
    elif cmd == "decide" and len(args) >= 2:
        print(cmd_decide(" ".join(args[1:])))
    elif cmd == "cache_clear":
        cache_clear()
    else:
        print(f"Unknown command or missing args: {args}")
        print("Commands: auto, fetch, extract, json, jsonld, multi, status, auth, bridge, decide, cache_clear")
        sys.exit(1)

if __name__ == "__main__":
    main()
