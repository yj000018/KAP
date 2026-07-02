import os
import sys
import json

def json_to_md(data: dict) -> str:
    md = []
    
    # Header
    md.append(f"# {data.get('title', 'Untitled Session')}")
    md.append("")
    
    # Meta block
    md.append("## Meta")
    md.append(f"- **Date**: {data.get('date', '')}")
    md.append(f"- **Project Hint**: {data.get('project_hint', '')}")
    md.append(f"- **Language**: {data.get('language', '')}")
    md.append(f"- **Depth Score**: {data.get('depth_score', '')}")
    md.append(f"- **Length Category**: {data.get('length_category', '')}")
    md.append(f"- **Themes**: {', '.join(data.get('themes', []))}")
    md.append(f"- **Tags**: {', '.join(data.get('tags', []))}")
    md.append("")
    
    # Executive Summary
    md.append("## Executive Summary")
    md.append(data.get("executive_summary", ""))
    md.append("")
    
    # Context & Intent
    md.append("## Context & Intent")
    md.append(data.get("context_and_intent", ""))
    md.append("")
    
    # What Was Done
    md.append("## What Was Done")
    md.append(data.get("what_was_done", ""))
    md.append("")
    
    # Key Points
    md.append("## Key Points")
    for pt in data.get("key_points", []):
        md.append(f"- {pt}")
    md.append("")
    
    # Outputs Produced
    md.append("## Outputs Produced")
    outputs = data.get("outputs_produced", [])
    if outputs:
        for out in outputs:
            md.append(f"- **[{out.get('type', '')}]** {out.get('name', '')}: {out.get('description', '')}")
    else:
        md.append("None")
    md.append("")
    
    # Key Decisions
    md.append("## Key Decisions")
    for dec in data.get("key_decisions", []):
        md.append(f"- {dec}")
    md.append("")
    
    # Open Items
    md.append("## Open Items & Blockers")
    for item in data.get("open_items", []):
        md.append(f"- {item}")
    md.append("")
    
    # Next Steps
    md.append("## Next Steps")
    for step in data.get("next_steps", []):
        md.append(f"- {step}")
    md.append("")
    
    # Links & References
    md.append("## Links & References")
    for link in data.get("links_and_references", []):
        md.append(f"- {link}")
    md.append("")
    
    # Resume Hints
    md.append("## Conversation Resume Hints")
    md.append(data.get("conversation_resume_hints", ""))
    md.append("")
    
    return "\n".join(md)

def main(uid: str):
    json_path = f"/home/ubuntu/KAP/03_Archived_Sessions/raw_json/{uid}_card.json"
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found")
        sys.exit(1)
        
    with open(json_path, "r") as f:
        data = json.load(f)
        
    md_content = json_to_md(data)
    
    # Create project subfolder if available
    project = data.get("project_hint", "UNKNOWN").upper()
    if not project:
        project = "UNKNOWN"
        
    out_dir = f"/home/ubuntu/KAP/03_Archived_Sessions/{project}"
    os.makedirs(out_dir, exist_ok=True)
    
    out_path = os.path.join(out_dir, f"{uid}_session_card.md")
    with open(out_path, "w") as f:
        f.write(md_content)
        
    print(f"✓ Markdown saved to {out_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 03_save_to_kap_git.py <uid>")
        sys.exit(1)
    main(sys.argv[1])
