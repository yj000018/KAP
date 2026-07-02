import os
import sys
import json
import traceback
from openai import OpenAI

# Rely entirely on the environment variables pre-configured in the sandbox
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE")
)
# Use a supported model from the proxy error message
MODEL = "claude-sonnet-4-6"

SYSTEM_PROMPT = """You are an expert knowledge architect specializing in extracting structured intelligence from AI conversation transcripts.
Analyze the session transcript and output a structured JSON summary.
DO NOT output any markdown or explanation, ONLY the raw JSON object.

JSON SCHEMA:
{
  "title": "string — a concise, descriptive title for the session",
  "date": "string — YYYY-MM-DD",
  "language": "string — primary language: fr / en / mixed",
  "depth_score": "string — minor / standard / substantial / landmark",
  "length_category": "string — short / medium / long / xl",
  "project_hint": "string — eia / yOS / VISUAL_REALITY / DOMUS / GEN5 / ODYSSEY / KAP / UNKNOWN",
  "themes": ["array of strings — key themes, concepts, tools"],
  "subthemes": ["array of strings — more specific sub-topics"],
  "executive_summary": "string — 3-5 sentences. What happened, why, net result. Dense, factual, no filler.",
  "context_and_intent": "string — Why this session was started. Initial question or goal.",
  "what_was_done": "string — Chronological sequence of actions.",
  "key_points": ["array of strings — the most important takeaways or facts"],
  "outputs_produced": [
    {"type": "string", "name": "string", "description": "string"}
  ],
  "key_decisions": ["array of strings — explicit choices made"],
  "open_items": ["array of strings — unresolved uncertainties, blockers, or pending questions"],
  "next_steps": ["array of strings — concrete actions identified but not executed"],
  "links_and_references": ["array of strings — URLs, tools, or external resources mentioned"],
  "tags": ["array of strings — 3-5 categorization tags"],
  "conversation_resume_hints": "string — instructions on how another AI could resume this work"
}

Be precise. Be dense. No filler. If a field has no content, use empty array [] or empty string "".
"""

def extract_text(messages):
    text_blocks = []
    for m in messages:
        if "user_message" in m:
            text_blocks.append(f"USER: {m['user_message']}")
        elif "assistant_message" in m:
            if m["assistant_message"]:
                content = m["assistant_message"].get("content", "")
                if content:
                    text_blocks.append(f"MANUS: {content}")
        elif "status_update" in m:
            if m["status_update"]:
                status = m["status_update"]
                text_blocks.append(f"SYSTEM [{status.get('agent_status')}]: {status.get('description')}")
    return "\n\n".join(text_blocks)

def generate_card(uid: str):
    raw_path = f"/home/ubuntu/KAP/03_Archived_Sessions/raw_json/{uid}_verbatim.json"
    if not os.path.exists(raw_path):
        print(f"Error: {raw_path} not found")
        sys.exit(1)
        
    with open(raw_path, "r") as f:
        messages = json.load(f)
        
    transcript = extract_text(messages)
    print(f"Generating card for {uid} ({len(transcript)} chars)...")
    
    try:
        response = client.chat.completions.create(
            model=MODEL, max_tokens=4096,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Here is the transcript for session {uid}:\n\n<transcript>\n{transcript}\n</transcript>\n\nGenerate the JSON card now."}
            ]
        )
        
        if not response.choices:
            print("Error: No choices in response:", response)
            sys.exit(1)
            
        content = response.choices[0].message.content
        
        # Clean up in case Claude added markdown backticks
        if content.startswith("```json"):
            content = content[7:]
        if content.startswith("```"):
            content = content[3:]
        if content.endswith("```"):
            content = content[:-3]
            
        data = json.loads(content.strip())
        
        out_path = f"/home/ubuntu/KAP/03_Archived_Sessions/raw_json/{uid}_card.json"
        with open(out_path, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print(f"✓ Card generated: {out_path}")
        return data
    except Exception as e:
        print(f"Error generating card:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 02_generate_card.py <uid>")
        sys.exit(1)
    generate_card(sys.argv[1])
