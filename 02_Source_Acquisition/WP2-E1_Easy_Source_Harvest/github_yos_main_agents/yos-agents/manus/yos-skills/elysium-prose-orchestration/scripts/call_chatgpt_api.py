#!/usr/bin/env python3
"""
Template script to call ChatGPT API for ELYSIUM prose review.
Usage: python3 call_chatgpt_api.py
"""

import os
import sys
import requests

# Set API key from environment or replace with valid key
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "sk-...")

SYSTEM_PROMPT = """You are the Chief Architect and coherence reviewer for ELYSIUM, a civilizational ontology book. Your role is structural review — not prose writing. You evaluate prose against the brief, the architectural constraints, and continuity requirements. You return a structured review with a clear PASS / REVISE / FAIL decision."""

USER_PROMPT = """[TODO: Insert prose and review criteria here]"""

def main():
    print("Calling ChatGPT API (gpt-4o-2024-08-06)...", flush=True)
    
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "gpt-4o-2024-08-06",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT}
        ],
        "max_tokens": 2000,
        "temperature": 0.3
    }
    
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=120
    )
    
    if response.status_code != 200:
        print(f"ERROR: ChatGPT API returned {response.status_code}", flush=True)
        print(response.text, flush=True)
        sys.exit(1)
    
    data = response.json()
    review_text = data["choices"][0]["message"]["content"]
    
    print("ChatGPT API review received.", flush=True)
    
    # Save output
    output_path = "review.md"
    with open(output_path, 'w') as f:
        f.write(review_text)
    
    print(f"Review saved to: {output_path}", flush=True)
    return 0

if __name__ == "__main__":
    sys.exit(main())
