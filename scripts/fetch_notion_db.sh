#!/bin/bash
# Fetch ALL pages from a Notion database with pagination
# Usage: ./fetch_notion_db.sh <db_id> <output_file>
TOKEN="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"
DB_ID="$1"
OUTPUT="$2"
PAGE=0
CURSOR=""
ALL_RESULTS="[]"

echo "Fetching DB: $DB_ID" >&2

while true; do
  PAGE=$((PAGE+1))
  if [ -z "$CURSOR" ]; then
    BODY='{"page_size":100}'
  else
    BODY="{\"page_size\":100,\"start_cursor\":\"$CURSOR\"}"
  fi
  
  RESPONSE=$(curl -s --retry 2 \
    -X POST \
    -H "Authorization: Bearer $TOKEN" \
    -H "Notion-Version: 2022-06-28" \
    -H "Content-Type: application/json" \
    -d "$BODY" \
    "https://api.notion.com/v1/databases/${DB_ID}/query")
  
  COUNT=$(echo "$RESPONSE" | python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d.get('results',[])))" 2>/dev/null)
  HAS_MORE=$(echo "$RESPONSE" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('has_more',False))" 2>/dev/null)
  CURSOR=$(echo "$RESPONSE" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('next_cursor','') or '')" 2>/dev/null)
  
  echo "  Page $PAGE: $COUNT entries, has_more=$HAS_MORE" >&2
  
  # Append results to output file
  echo "$RESPONSE" >> "${OUTPUT}.pages"
  
  if [ "$HAS_MORE" != "True" ] || [ -z "$CURSOR" ]; then
    break
  fi
done

# Merge all pages into single JSON
python3 - <<'PYEOF'
import json, os, sys

output = sys.argv[1] if len(sys.argv) > 1 else "/tmp/notion_out.json"
pages_file = output + ".pages"

all_results = []
with open(pages_file) as f:
    content = f.read()

# Split by newlines and parse each JSON object
decoder = json.JSONDecoder()
pos = 0
while pos < len(content):
    content_strip = content[pos:].lstrip()
    if not content_strip:
        break
    try:
        obj, offset = decoder.raw_decode(content_strip)
        all_results.extend(obj.get("results", []))
        pos += len(content) - len(content_strip) + offset
    except:
        break

with open(output, 'w') as f:
    json.dump({"total": len(all_results), "results": all_results}, f, indent=2, ensure_ascii=False)

print(f"Total merged: {len(all_results)} entries -> {output}")
PYEOF
