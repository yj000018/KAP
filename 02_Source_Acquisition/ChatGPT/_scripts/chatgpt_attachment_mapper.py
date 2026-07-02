#!/usr/bin/env python3
"""ChatGPT Attachment Mapper — CONN-OAI-01. Maps file attachments in conversations.json."""
import json, os, argparse, datetime

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_dry_runs")

def map_attachments(filepath=None):
    if not filepath or not os.path.exists(filepath):
        print("[SKIP] No conversations.json provided"); return
    with open(filepath) as f: data = json.load(f)
    convs = data if isinstance(data, list) else data.get("conversations", [])
    attachments = []
    for c in convs:
        for node in c.get("mapping", {}).values():
            msg = node.get("message") or {}
            content = msg.get("content") or {}
            for part in content.get("parts", []):
                if isinstance(part, dict) and part.get("content_type") in ["image_asset_pointer","file_asset_pointer"]:
                    attachments.append({"conv_id": c.get("id",""), "conv_title": c.get("title",""),
                                        "type": part.get("content_type"), "asset_id": part.get("asset_pointer","")})
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out = os.path.join(OUTPUT_DIR, f"chatgpt_attachments_{datetime.date.today()}.json")
    with open(out, "w") as f: json.dump({"total": len(attachments), "items": attachments}, f, indent=2)
    print(f"[OK] {len(attachments)} attachments mapped | Saved: {out}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("--file"); p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(); map_attachments(args.file)
