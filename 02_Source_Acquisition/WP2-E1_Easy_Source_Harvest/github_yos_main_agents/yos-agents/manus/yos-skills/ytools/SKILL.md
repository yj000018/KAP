---
name: ytools
description: "Y-OS unified tool intelligence system. Search existing tools, discover new MCP/API/GitHub/Chrome extensions, monitor for updates and novelties, add tools to Registry, and audit Y-OS capability gaps. Use when user asks: 'find a tool for X', 'what tools do I have for Y', 'any new MCP for Z', 'add this tool to Registry', 'audit my tools', 'monitor new connectors', '/yTools', or via /yMenu → Tools."
---

# yTools — Y-OS Tool Intelligence System

Single entry point for all tool operations in Y-OS: search, discover, audit, monitor, register.

## Commands

| Command | Action |
|---|---|
| `/yTools search [query]` | Search existing Y-OS tools (skills + connectors + CLI + libs) |
| `/yTools discover [category]` | Find new tools not yet in Y-OS (MCP, API, GitHub, Chrome ext) |
| `/yTools audit` | Full capability gap analysis |
| `/yTools add [tool]` | Add tool to Notion Registry with factsheet |
| `/yTools monitor` | Check for new notable tools (weekly cadence) |
| `/yTools status` | Health check all active connectors |

---

## 1. Search Existing Tools (`/yTools search`)

**Sources to search in order:**
1. Skills: `/home/ubuntu/skills/` — 57 skills
2. Connectors: `~/.manus/config/config.json` — 80 active
3. CLI tools: `manus-*` commands + Python libs
4. Notion Registry: `85f89b4e-847d-4cbe-a931-0ffdf11b60f2`

**Search method:**
```bash
# Quick local search
ls /home/ubuntu/skills/ | grep -i [query]
cat ~/.manus/config/config.json | python3 -c "import json,sys; d=json.load(sys.stdin); [print(c['name']) for c in d.get('connectors',[]) if '[query]' in c['name'].lower()]"
# Notion Registry search
manus-mcp-cli tool call notion-search --server notion --input '{"query": "[query]"}'
```

**Output format:**
```
🔍 Results for "[query]":
  🧠 Skills: [list]
  🔌 Connectors: [list]  
  🛠️  CLI/Libs: [list]
  📋 Registry: [links]
```

---

## 2. Discover New Tools (`/yTools discover`)

**Categories to scan:**
- `mcp` → MCP servers (Smithery, Glama, GitHub MCP repos)
- `api` → REST/GraphQL APIs
- `github` → GitHub repos (stars > 1k, recent activity)
- `chrome` → Chrome extensions for productivity/AI
- `native` → Manus native connectors not yet enabled

**Discovery sources:**
- [Smithery MCP Registry](https://smithery.ai) — searchable MCP catalog
- [Glama MCP](https://glama.ai/mcp/servers) — curated MCP list
- [GitHub Awesome MCP](https://github.com/punkpeye/awesome-mcp-servers)
- [Chrome Web Store](https://chromewebstore.google.com) — extensions
- Manus config disabled connectors: `cat ~/.manus/config/config.json | python3 -c "import json,sys; d=json.load(sys.stdin); [print(c['name']) for c in d.get('connectors',[]) if not c.get('enabled',True)]"`

**Evaluation criteria:**
| Criterion | Weight |
|---|---|
| Fills a Y-OS gap | 40% |
| Free / low cost | 25% |
| Active maintenance (< 6 months) | 20% |
| Easy integration | 15% |

---

## 3. Audit Capability Gaps (`/yTools audit`)

**Y-OS capability map — check coverage:**

| Domain | Primary Tool | Backup | Gap? |
|---|---|---|---|
| LLM inference | Anthropic | OpenAI, Gemini, Grok | ✅ |
| Image generation | Flux BFL | Replicate, DALL-E | ✅ |
| Video generation | HeyGen, Higgsfield | MiniMax | ✅ |
| Audio/TTS | ElevenLabs | Hume, MiniMax | ✅ |
| Web search | Perplexity | Firecrawl, Context7 | ✅ |
| Semantic search | — | — | ⚠️ Exa/Tavily not yet added |
| Memory structured | Notion | — | ✅ |
| Memory semantic | Mem0 | — | ⚠️ Qdrant pending N100 |
| Vector DB | — | Supabase pgvector | ⚠️ Qdrant pending N100 |
| Code repos | GitHub | — | ✅ |
| Automation | Make, Zapier | n8n (N100) | ✅ |
| Browser auto | Playwright, Anchor | HARPA | ✅ |
| Email | Gmail, MailerLite | — | ✅ |
| Calendar/Scheduling | Google Cal, Cal.com | Calendly | ✅ |
| PM | Linear, Asana, ClickUp | Wrike, Monday | ✅ |
| Design | Canva, Miro | — | ✅ |
| Payments | Stripe | — | ✅ |
| Hosting | Vercel, Netlify | Cloudflare | ✅ |
| CMS | Sanity | Webflow, Wix | ✅ |
| Finance/Crypto | Alpha Vantage | CoinGecko | ✅ |
| Travel | Kiwi, Trivago | Ferryhopper | ✅ |
| Local LLM | — | — | ⚠️ Ollama pending N100 |
| Chrome extensions | — | — | ⚠️ Not inventoried |

**Known gaps to fill:**
1. **Exa Search** — semantic web search (free tier available)
2. **Tavily** — structured AI search for agents
3. **Qdrant** — vector DB (N100 when ready)
4. **Ollama** — local LLMs (N100 when ready)
5. **Chrome extensions** — inventory needed

---

## 4. Add Tool to Registry (`/yTools add`)

**Workflow:**
1. Gather tool info: name, category, auth, pricing, capabilities
2. Create factsheet at `/home/ubuntu/factsheets/[tool-name]_factsheet.md`
3. Push to Notion Registry (data_source_id: `76236561-0572-46bd-861b-636e61898921`):
   - Properties: Tool Name, Category, Status, Tool Type, Auth Credentials, Source URL, Capabilities, Business Value, Pricing, Workarounds and Lessons, Source Type
   - Valid Status: `Production` | `Experimental` | `A tester` | `Deprecated`
   - Valid Pricing: `Free` | `Freemium` | `Payant` | `Pay-as-you-go` | `Inclus Y-OS`
4. If MCP connector: enable via `manus-config config load` → edit → `manus-config config save`

---

## 5. Monitor New Tools (`/yTools monitor`)

**Weekly scan protocol:**
1. Check [Smithery new servers](https://smithery.ai) — sort by recent
2. Check [GitHub trending](https://github.com/trending) — filter: Python/TypeScript, topic: mcp
3. Check [Product Hunt AI tools](https://www.producthunt.com) — filter: AI, Developer Tools
4. Check [Chrome Web Store](https://chromewebstore.google.com/search/AI) — AI category
5. Cross-reference against current Y-OS stack — flag non-redundant tools

**Alert criteria:**
- New MCP server for uncovered domain
- GitHub repo > 500 stars in < 1 month
- Free tier available
- Not redundant with existing tools

---

## 6. Chrome Extensions Inventory

**Known Y-OS-relevant extensions (to document):**
| Extension | Purpose | Status |
|---|---|---|
| Notion Web Clipper | Save web content to Notion | Likely installed |
| HARPA AI | AI on any webpage | Configured in Y-OS |
| 1Password | Password/secret manager | Active |
| Jam | Bug recording | Active (MCP connected) |
| Loom | Screen recording | Unknown |
| Grammarly | Writing assistant | Unknown |
| uBlock Origin | Ad blocking | Unknown |

**To audit:** Ask user to list installed Chrome extensions, then document in Registry.

---

## Y-OS Inventory Summary (as of 2026-06-18)

| Layer | Count | Status |
|---|---|---|
| Skills | 58 | ✅ All documented |
| Connectors (active) | 80 | ✅ All tested + documented |
| Factsheets | 132 | ✅ In `/home/ubuntu/factsheets/` |
| Notion Registry entries | 70+ | ✅ Pushed this session |
| CLI Tools (manus-*) | 11 | ✅ Documented |
| Python libs (key) | 15+ | ✅ Installed |
| Chrome extensions | Unknown | ⚠️ Needs audit |
| Prompts | 51 | ✅ In prompt-library skill |
| N100 stack | 0 | ⏳ Pending N100 connection |
