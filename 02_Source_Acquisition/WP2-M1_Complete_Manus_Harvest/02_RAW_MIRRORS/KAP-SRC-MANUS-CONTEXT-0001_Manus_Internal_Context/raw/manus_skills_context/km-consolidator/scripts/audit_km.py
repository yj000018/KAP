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

def main():
    print("🔍 Auditing Manus Memory Hub...")
    
    # 1. Get all entries
    search_cmd = "manus-mcp-cli tool call notion-search --server notion --input '{\"query\": \"\", \"query_type\": \"internal\", \"page_url\": \"533401fa-1702-4d9d-a60e-5433cac72fe1\"}'"
    output = run_mcp(search_cmd)
    
    if not output:
        print("❌ Failed to fetch entries.")
        sys.exit(1)
        
    try:
        start_idx = output.find('{"results"')
        if start_idx == -1:
            print("❌ Could not parse JSON from output.")
            sys.exit(1)
            
        data = json.loads(output[start_idx:])
        results = data.get("results", [])
        
        print(f"\n📊 Total Entries: {len(results)}\n")
        
        entries = []
        for r in results:
            title = r.get("title", "Unknown")
            url = r.get("url", "")
            id_ = r.get("id", "")
            type_ = r.get("type", "Unknown")
            date = r.get("timestamp", "Unknown")[:10] if r.get("timestamp") else "Unknown"
            
            entries.append({
                "title": title,
                "id": id_,
                "url": url,
                "type": type_,
                "date": date
            })
            
        # Group by potential topics
        print("📑 Entries by Type:")
        types = {}
        for e in entries:
            types[e["type"]] = types.get(e["type"], 0) + 1
        for t, count in types.items():
            print(f"  - {t}: {count}")
            
        print("\n📋 Detailed List:")
        for i, e in enumerate(entries, 1):
            print(f"{i}. [{e['type']}] {e['title']} ({e['date']})")
            print(f"   ID: {e['id']}")
            
        print("\n💡 Recommendation: Look for multiple '📝 Conversation Archive' or '📝 [Date]' entries that can be merged into a single '📚 MASTER SESSION' or '🎯 Projet'.")
            
    except Exception as e:
        print(f"❌ Error processing results: {e}")

if __name__ == "__main__":
    main()
