#!/usr/bin/env python3
"""
ChatGPT Conversation Indexer — CONN-OAI-01
Builds a metadata index from conversations.json export. No full content ingestion.
"""
import json, os, argparse, datetime

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_dry_runs")

def index(filepath=None):
    if not filepath or not os.path.exists(filepath):
        print("[SKIP] No conversations.json provided"); return
    with open(filepath) as f: data = json.load(f)
    convs = data if isinstance(data, list) else data.get("conversations", [])
    index = [{"id": c.get("id",""), "title": c.get("title",""), "created_at": c.get("create_time",""),
               "updated_at": c.get("update_time",""), "message_count": len(c.get("mapping",{}))} for c in convs]
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out = os.path.join(OUTPUT_DIR, f"chatgpt_index_{datetime.date.today()}.json")
    with open(out, "w") as f: json.dump({"total": len(index), "items": index}, f, indent=2, ensure_ascii=False)
    print(f"[OK] {len(index)} conversations indexed | Saved: {out}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("--file"); p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(); index(args.file)
