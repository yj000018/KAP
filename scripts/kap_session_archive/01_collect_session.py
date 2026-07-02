import os
import sys
import json
import requests

API_KEY = "sk-TEKENLb_4FM1xUD0skvl7Y5bxdg_ZwSBn93f4UyT3obza8szuxS1v4AFcs5iokvaLur6obq0SlG80yIIr-Zu_rKeVdze"
BASE_URL = "https://api.manus.im/v2"
HEADERS = {"x-manus-api-key": API_KEY}
EXPORT_DIR = "/home/ubuntu/KAP/03_Archived_Sessions/raw_json"

os.makedirs(EXPORT_DIR, exist_ok=True)

def fetch_session_verbatim(uid: str):
    print(f"Fetching verbatim for UID: {uid}")
    messages = []
    has_more = True
    last_id = None
    page = 0
    seen_ids = set()
    
    while has_more and page < 100:
        page += 1
        url = f"{BASE_URL}/task.listMessages?task_id={uid}&page_size=100"
        if last_id:
            url += f"&last_id={last_id}"
        
        print(f"Fetching page {page}...")
        try:
            res = requests.get(url, headers=HEADERS, timeout=10)
            if res.status_code == 200:
                data = res.json()
                page_msgs = data.get("messages", [])
                
                # Check for duplicates to prevent infinite loop
                new_msgs = []
                for m in page_msgs:
                    if m.get("id") not in seen_ids:
                        seen_ids.add(m.get("id"))
                        new_msgs.append(m)
                
                messages.extend(new_msgs)
                has_more = data.get("has_more", False)
                
                if new_msgs:
                    last_id = new_msgs[-1].get("id")
                else:
                    has_more = False
                    
            else:
                print(f"HTTP Error: {res.status_code} - {res.text}")
                return None
        except Exception as e:
            print(f"Request Error: {e}")
            return None
            
    # Reverse to get chronological order (API returns newest first)
    messages.reverse()
    return messages

def main(uid: str):
    messages = fetch_session_verbatim(uid)
    if not messages:
        print(f"Failed to fetch {uid}")
        sys.exit(1)
        
    out_path = os.path.join(EXPORT_DIR, f"{uid}_verbatim.json")
    with open(out_path, "w") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)
    print(f"✓ Saved raw verbatim to {out_path} ({len(messages)} messages)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 01_collect_session.py <uid>")
        sys.exit(1)
    main(sys.argv[1])
