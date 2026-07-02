import os
import sys
import requests
import json

API_KEY = "sk-TEKENLb_4FM1xUD0skvl7Y5bxdg_ZwSBn93f4UyT3obza8szuxS1v4AFcs5iokvaLur6obq0SlG80yIIr-Zu_rKeVdze"
BASE_URL = "https://api.manus.im/v2"
HEADERS = {"x-manus-api-key": API_KEY, "Content-Type": "application/json"}

def update_session(uid: str):
    print(f"Updating session {uid} in Manus...")
    
    # Add footer message
    footer_text = "========\nARCHIVED\n========"
    chat_url = f"{BASE_URL}/task.sendMessage"
    chat_payload = {
        "task_id": uid,
        "message": {
            "content": footer_text
        }
    }
    
    try:
        res = requests.post(chat_url, headers=HEADERS, json=chat_payload, timeout=10)
        if res.status_code == 200:
            print(f"✓ Footer added to session")
        else:
            print(f"Error adding footer: {res.status_code} - {res.text}")
    except Exception as e:
        print(f"Request Error (footer): {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 04_mark_archived_in_manus.py <uid>")
        sys.exit(1)
    update_session(sys.argv[1])
