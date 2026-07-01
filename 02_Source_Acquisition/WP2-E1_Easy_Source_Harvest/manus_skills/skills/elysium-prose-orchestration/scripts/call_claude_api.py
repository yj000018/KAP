#!/usr/bin/env python3
"""
Template script to call Claude API for ELYSIUM prose generation.
Usage: python3 call_claude_api.py
"""

import anthropic
import os
import sys

# Set API key from environment or replace with valid key
CLAUDE_API_KEY = os.environ.get("CLAUDE_API_KEY", "sk-ant-api03-...")

SYSTEM_PROMPT = """You are a literary prose writer for ELYSIUM, a civilizational ontology book. Your voice is civilizational, lucid, literary but not ornate, rigorous but accessible. You write in English. You produce final prose — not outlines, not drafts with commentary, not explanations. You write exactly what will appear on the page."""

USER_PROMPT = """[TODO: Insert context pack and writing brief here]"""

def main():
    client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)
    
    print("Calling Claude API (claude-opus-4-5)...", flush=True)
    
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": USER_PROMPT}
        ]
    )
    
    prose = message.content[0].text
    word_count = len(prose.split())
    
    print(f"Claude prose received. Word count: {word_count}", flush=True)
    
    # Save output
    output_path = "output.md"
    with open(output_path, 'w') as f:
        f.write(prose)
    
    print(f"Output saved to: {output_path}", flush=True)
    return 0

if __name__ == "__main__":
    sys.exit(main())
