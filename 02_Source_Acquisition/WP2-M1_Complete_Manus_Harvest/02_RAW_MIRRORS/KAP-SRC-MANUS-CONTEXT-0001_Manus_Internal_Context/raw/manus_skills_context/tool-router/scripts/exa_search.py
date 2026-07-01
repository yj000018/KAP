#!/usr/bin/env python3
"""
Exa Search API Wrapper — Y-OS
Usage: python3 exa_search.py "query" [--type search|news|research] [--n 10]
Auto-reads EXA_API_KEY from environment.
"""

import os
import sys
import json
import argparse
import requests
from datetime import datetime, timedelta

EXA_API_KEY = os.environ.get("EXA_API_KEY", "")
BASE_URL = "https://api.exa.ai"


def search(query: str, num_results: int = 10, search_type: str = "auto",
           highlights: bool = True, use_autoprompt: bool = True,
           start_published_date: str = None) -> dict:
    """Standard Exa search — optimal parameters for Y-OS."""
    if not EXA_API_KEY:
        return {"error": "EXA_API_KEY not set in environment"}

    payload = {
        "query": query,
        "numResults": num_results,
        "type": search_type,
        "highlights": highlights,
        "useAutoprompt": use_autoprompt,
        "contents": {
            "highlights": {"numSentences": 3, "highlightsPerUrl": 2},
            "summary": {"query": query}
        }
    }
    if start_published_date:
        payload["startPublishedDate"] = start_published_date

    headers = {
        "x-api-key": EXA_API_KEY,
        "Content-Type": "application/json"
    }

    resp = requests.post(f"{BASE_URL}/search", json=payload, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()


def news(query: str, num_results: int = 10, days_back: int = 7) -> dict:
    """Recent news search — last N days."""
    start_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%dT00:00:00Z")
    return search(query, num_results, search_type="news", start_published_date=start_date)


def research(query: str, num_results: int = 10) -> dict:
    """Academic/research search — optimized for papers and reports."""
    return search(query, num_results, search_type="neural", use_autoprompt=True)


def find_similar(url: str, num_results: int = 10) -> dict:
    """Find pages similar to a given URL."""
    if not EXA_API_KEY:
        return {"error": "EXA_API_KEY not set in environment"}

    payload = {"url": url, "numResults": num_results, "highlights": True}
    headers = {"x-api-key": EXA_API_KEY, "Content-Type": "application/json"}
    resp = requests.post(f"{BASE_URL}/findSimilar", json=payload, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()


def format_results(data: dict) -> str:
    """Format results for readable output."""
    if "error" in data:
        return f"ERROR: {data['error']}"

    results = data.get("results", [])
    if not results:
        return "No results found."

    output = []
    for i, r in enumerate(results, 1):
        title = r.get("title", "No title")
        url = r.get("url", "")
        score = r.get("score", 0)
        published = r.get("publishedDate", "")[:10] if r.get("publishedDate") else ""

        output.append(f"\n[{i}] {title}")
        output.append(f"    URL: {url}")
        if published:
            output.append(f"    Date: {published} | Score: {score:.3f}")

        # Highlights
        highlights = r.get("highlights", [])
        if highlights:
            output.append(f"    → {highlights[0]}")

        # Summary
        summary = r.get("summary", "")
        if summary:
            output.append(f"    Summary: {summary[:200]}...")

    return "\n".join(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Exa Search — Y-OS wrapper")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--type", choices=["search", "news", "research", "similar"],
                        default="search", help="Search type")
    parser.add_argument("--n", type=int, default=10, help="Number of results")
    parser.add_argument("--days", type=int, default=7, help="Days back for news")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    if args.type == "news":
        data = news(args.query, args.n, args.days)
    elif args.type == "research":
        data = research(args.query, args.n)
    elif args.type == "similar":
        data = find_similar(args.query, args.n)
    else:
        data = search(args.query, args.n)

    if args.json:
        print(json.dumps(data, indent=2))
    else:
        print(format_results(data))
