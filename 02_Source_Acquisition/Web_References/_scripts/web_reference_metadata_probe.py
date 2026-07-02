#!/usr/bin/env python3
"""
Web Reference Metadata Probe — CONN-WEB-01
Fetches title, description, and metadata from a list of URLs. No full text dump.
Usage: python3 web_reference_metadata_probe.py [--urls url1 url2 ...] [--dry-run]
"""
import os, json, argparse, datetime

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_dry_runs")
SAMPLE_URLS = ["https://manus.im", "https://notion.so", "https://obsidian.md"]

def probe(urls=None):
    if not urls: urls = SAMPLE_URLS
    try:
        import requests
        from html.parser import HTMLParser
        class TitleParser(HTMLParser):
            def __init__(self):
                super().__init__(); self.title = ""; self._in_title = False
            def handle_starttag(self, tag, attrs):
                if tag == "title": self._in_title = True
            def handle_data(self, data):
                if self._in_title: self.title += data
            def handle_endtag(self, tag):
                if tag == "title": self._in_title = False
        results = []
        for url in urls:
            try:
                r = requests.get(url, timeout=8, headers={"User-Agent": "KAP-Connector/1.0"})
                p = TitleParser(); p.feed(r.text[:5000])
                results.append({"url": url, "status": r.status_code, "title": p.title.strip()[:100]})
            except Exception as e:
                results.append({"url": url, "status": "error", "title": str(e)[:80]})
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        out = os.path.join(OUTPUT_DIR, f"web_probe_{datetime.date.today()}.json")
        with open(out, "w") as f: json.dump({"total": len(results), "items": results}, f, indent=2)
        print(f"[OK] {len(results)} URLs probed | Saved: {out}")
    except ImportError: print("[FAIL] requests not installed")

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("--urls", nargs="+"); p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(); probe(args.urls)
