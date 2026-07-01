import sys
import json
import subprocess
import os

def run_mcp(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running MCP command: {e}")
        print(f"Stderr: {e.stderr}")
        return None

def fetch_entry(id_):
    print(f"Fetching entry {id_}...")
    cmd = f"manus-mcp-cli tool call notion-fetch --server notion --input '{{\"id\": \"{id_}\"}}'"
    output = run_mcp(cmd)
    if not output: return None
    
    try:
        start_idx = output.find('{"metadata"')
        if start_idx == -1: return None
        data = json.loads(output[start_idx:])
        return data.get("text", "")
    except Exception as e:
        print(f"Error parsing fetch result: {e}")
        return None

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 merge_entries.py <target_id> <source_id_1> [source_id_2 ...]")
        print("This script will fetch the sources, and you should use Manus to synthesize them and update the target.")
        sys.exit(1)
        
    target_id = sys.argv[1]
    source_ids = sys.argv[2:]
    
    print(f"Target Entry ID: {target_id}")
    print(f"Source Entry IDs to merge: {source_ids}")
    
    combined_content = ""
    for sid in source_ids:
        content = fetch_entry(sid)
        if content:
            combined_content += f"\n\n=== SOURCE: {sid} ===\n\n{content}"
            
    # Save combined content to a file for Manus to process
    out_file = "/tmp/combined_sources_for_merge.md"
    with open(out_file, "w") as f:
        f.write(combined_content)
        
    print(f"\n✅ Fetched all sources. Combined content saved to: {out_file}")
    print(f"Total characters: {len(combined_content)}")
    print("\nNext steps for Manus:")
    print(f"1. Read {out_file}")
    print(f"2. Synthesize and compress the content using Claude Opus")
    print(f"3. Update the target entry ({target_id}) with the synthesized content")
    print(f"4. Change the status of the source entries to 'Archivé'")

if __name__ == "__main__":
    main()
