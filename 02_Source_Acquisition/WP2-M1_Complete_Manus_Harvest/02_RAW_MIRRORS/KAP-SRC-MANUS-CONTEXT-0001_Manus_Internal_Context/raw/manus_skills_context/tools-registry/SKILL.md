---
name: tools-registry
description: "Y-OS Tools Registry manager. Use when user asks to list tools, find a tool by name or use case, update the registry, add a new tool, create a factsheet, or says 'Tools Registry', 'mets a jour le Tools Registry', 'quel outil pour X', 'ajoute cet outil au registry'. Provides a quick menu and executes registry operations against the Notion database (DS: 76236561-0572-46bd-861b-636e61898921)."
---

# Y-OS Tools Registry Skill

## Registry Location

- **Notion DB:** `🗂️ Y-OS Tools Registry v2`
- **URL:** https://app.notion.com/p/85f89b4e847d4cbea9310ffdf11b60f2
- **Data Source ID:** `76236561-0572-46bd-861b-636e61898921`
- **MCP Server:** `notion`
- **Query tool:** `notion-query-data-sources`
- **Write tool:** `notion-create-pages` (insert) / `notion-update-page` (update)

## DB Schema (key fields)

| Field | Type | Notes |
|---|---|---|
| Tool Name | TITLE | Primary key |
| Category | SELECT | 18 options |
| Tool Type | SELECT | MCP Connector / REST API / CLI Tool / Script Python / Skill Y-OS / Browser Automation |
| Source Type | SELECT | Officiel / Communauté / Custom Y-OS |
| Source URL | URL | Official doc or GitHub repo |
| Auth Credentials | SELECT | OAuth MCP / API Key Env Var / 1Password Item / Session Cookie / No Auth |
| Business Value | RICH_TEXT | What problem it solves in Y-OS |
| Capabilities | RICH_TEXT | What it CAN do |
| Known Limits and Bugs | RICH_TEXT | What it CANNOT do + known bugs |
| Workarounds and Lessons | RICH_TEXT | Live-tested solutions by Manus |
| Pricing | SELECT | Free / Freemium / Payant / Pay-as-you-go / Inclus Y-OS |
| Dependencies | RICH_TEXT | Env vars, devices, prerequisite tools |
| Factsheet URL | URL | Link to detailed factsheet if exists |
| Status | SELECT | Production / Experimental / A tester / Deprecated |
| Tool ID | AUTO | YOT-001… |

**⚠️ Tags field:** MULTI_SELECT exists in schema but `notion-create-pages` rejects array values — causes "Invalid input". Set tags manually in Notion UI or skip.

## Quick Menu

When invoked without a specific command, display this menu and wait for selection:

```
🗂️ Y-OS Tools Registry — Quick Menu

1️⃣  List all tools by Category
2️⃣  Find tool (name or use case)
3️⃣  Update Registry (add / edit tool)
4️⃣  Create Factsheet for a tool
5️⃣  Show tools by Status
6️⃣  Show tools missing Factsheet
```

## Workflows

### 1️⃣ List all tools by Category

```sql
SELECT "Tool Name", "Category", "Status", "Factsheet URL"
FROM "collection://76236561-0572-46bd-861b-636e61898921"
ORDER BY "Category", "Tool Name"
```

Format as grouped table per category. Status emoji: 🟢 Production / 🟡 Experimental / ⚪ À tester / 🔴 Deprecated.

### 2️⃣ Find tool (name or use case)

Search by name via `notion-search`. Search by use case: query DB filtering by relevant Category or scan Business Value field. Return top 3–5 matches with Business Value snippet.

### 3️⃣ Update Registry

**Add new tool:** Collect all fields, then:
```python
manus-mcp-cli tool call notion-create-pages --server notion \
  --input '{"parent": {"data_source_id": "76236561-0572-46bd-861b-636e61898921"}, "pages": [{"properties": {...}}]}'
```

**Edit existing tool:** Query to get page URL, then call `notion-update-page` with updated properties.

**Do NOT pass Tags as a property** — causes "Invalid input" error.

After any write: confirm with Notion page URL.

### 4️⃣ Create Factsheet

1. Fetch official docs via `firecrawl` or `webpage_extract`
2. Check if live test exists (Workarounds and Lessons field)
3. Write factsheet using template in `references/factsheet_template.md`
4. Push to Notion under parent `31435e218cf881b0a484ea8b0099c5f0` (Architecture Hub)
5. Update tool's `Factsheet URL` + `Status` in Registry

### 5️⃣ Show tools by Status

```sql
SELECT "Tool Name", "Category", "Factsheet URL"
FROM "collection://76236561-0572-46bd-861b-636e61898921"
WHERE "Status" = '<Production|Experimental|A tester|Deprecated>'
```

### 6️⃣ Show tools missing Factsheet

```sql
SELECT "Tool Name", "Category", "Status"
FROM "collection://76236561-0572-46bd-861b-636e61898921"
WHERE "Factsheet URL" IS NULL
ORDER BY "Status", "Category"
```

Present as prioritized list (Production first).

## Update Protocol ("mets à jour le Tools Registry")

1. Query current DB state
2. Compare with active MCP connectors (system prompt `<mcp_integration>` section)
3. Identify: new tools not in DB / outdated Status / missing fields
4. Propose diff to user before writing
5. Execute approved changes

## Key Rules

- **Never invent capabilities** — only document what was tested or is in official docs
- **Source discipline:** Workarounds field must include `Source: test live [date]` or `Source: doc officielle`
- **Status = Production** only after end-to-end live test by Manus
- **Lessons Learned are gold** — always capture API quirks, 404 endpoints, auth gotchas
