---
name: y-menu
description: "Y-OS unified cognitive interface — single entry point to ALL Y-OS capabilities. Use when user types /yMenu, /menu, 'what can you do', 'show me tools', 'list skills', 'what's available', or wants to navigate/search Y-OS capabilities by category. Displays structured menu with drill-down into Skills, Connectors, Prompts, CLI Tools, Infrastructure. Like RayCast but for Y-OS."
---

# /yMenu — Y-OS Unified Cognitive Interface

Single entry point to everything in Y-OS. Displays structured menu with categories and drill-down navigation.

## Trigger Patterns

- `/yMenu` or `/menu` — show top-level menu
- `/yMenu [category]` — drill into category (e.g. `/yMenu skills`, `/yMenu connectors`)
- `/yMenu search [query]` — semantic search across all capabilities
- `/yMenu status` — show what's active, broken, pending auth
- "what can you do" / "show me tools" / "list capabilities" — auto-trigger top-level menu

## Top-Level Menu Output Format

When triggered, display this structure:

```
╔══════════════════════════════════════════╗
║         Y-OS  /yMenu  v2.0              ║
║    Cognitive Operating System Interface  ║
╚══════════════════════════════════════════╝

1️⃣  🧠 SKILLS          58 skills — cognitive workflows & automation
2️⃣  🔌 CONNECTORS      80 active — MCP tools & external APIs
3️⃣  📝 PROMPTS         51 prompts — 7 categories
4️⃣  🛠️  CLI & LIBS      Built-in tools & Python libraries
5️⃣  🖥️  INFRASTRUCTURE  Nodes: Sandbox / GCP / N100 (pending)
6️⃣  🔧 TOOLS           /yTools — discover, search, audit, monitor

Type /yMenu [number or name] to drill down
Type /yMenu search [query] to find anything
Type /yMenu status for health check
```

## Category Drill-Down

### 1️⃣ SKILLS (58 total)

Group skills into these categories when displaying:

| Category | Skills |
|---|---|
| 🧠 Memory & Knowledge | memoriser, hydrater, memory-manager, mem0-sync, km-consolidator, project-hydration, project-synthesis, session-synthesis, session-synthesizer, session-navigator, yos-mmm |
| 🤖 AI & LLM Routing | llm-router, tool-router, yos-optimizer, prompt-optimizer, credit-optimizer, request-optimizer |
| 🎨 Media Generation | imagegen, tts-prompter, music-prompter, video-generator, manim-animator, html-video-production |
| 💻 Code & Dev | dev, complex-webapp-builder, webapp-factory, excel-generator, github-gem-seeker, gws-best-practices, fast-navigation, persistent-computing, automation-and-scheduling, manim-animator |
| ⚙️ Y-OS System | y-menu, ytools, yos-helpdesk, yos-mac-bridge, yos-optimizer, yos-voice, yos-cleanmyapps, manus-config, manus-api, tools-registry, skill-creator, canva-mcp |
| 📝 Prompts | prompt-library, prompt-optimizer |
| 🔬 Research | stock-analysis, internet-skill-finder, harpa-grid |
| 📋 Productivity | task-manager, file-organizer, archive, summary, status, eta, back-to-chat |
| 🌐 Language | fransai-basic |

### 2️⃣ CONNECTORS (80 active)

Group by domain:

| Domain | Key Connectors |
|---|---|
| 🤖 LLM/AI | OpenAI, Anthropic, Gemini, Grok, OpenRouter, Replicate, Flux, HuggingFace, Hume, ElevenLabs, MiniMax, HeyGen, Higgsfield |
| 🧠 Memory | Notion, Notion2, Mem0, Airtable, Supabase, Dropbox, Google Drive |
| ⚡ Automation | Make, Zapier, n8n (N100), Dify, ButlerBrain |
| 📋 PM & Collab | Asana, Linear, Wrike, Monday, Todoist, ClickUp, Slack, Miro |
| 💻 Dev & Hosting | GitHub, Vercel, Netlify, Supabase, Cloudflare, Sentry, Serena, Playwright |
| 🎨 Design | Canva, Flux, Mermaid Chart, Excalidraw, Higgsfield |
| 📊 CRM & Marketing | HubSpot, Klaviyo, Stripe, MailerLite, Mailchimp |
| 🔬 Research | Perplexity, Firecrawl, Semrush⚠️, Alpha Vantage, CoinGecko, Wolfram, Context7 |
| 📅 Scheduling | Cal.com, Calendly, Google Calendar, Zoom |
| ✈️ Travel | Kiwi.com, Trivago, Ferryhopper |
| 📝 Forms | Tally⚠️, Typeform (REST only), JotForm |
| 🏗️ CMS | Sanity, Webflow, Wix |

⚠️ = needs OAuth reconnection

### 3️⃣ PROMPTS

No dedicated prompt library exists yet. When displaying this category:

```
📝 PROMPT LIBRARY — Not yet structured

Categories planned:
  ⭐ Favorites
  🎨 Multimedia (image, video, audio, TTS)
  🔬 Research & Analysis
  💻 Code & Dev
  📊 Data & Reports
  🧠 Cognitive & Memory
  ✍️ Writing & Content

→ To create prompt library: /yMenu create-prompt-library
```

### 4️⃣ CLI & LIBS

Built-in tools always available:

| Tool | Usage |
|---|---|
| `manus-render-diagram` | Render .d2/.mmd/.puml to PNG |
| `manus-md-to-pdf` | Convert Markdown to PDF |
| `manus-speech-to-text` | Transcribe audio files |
| `manus-mcp-cli` | Interact with MCP servers |
| `manus-analyze-video` | Analyze video with LLM |
| `manus-config` | Manage connectors & schedules |

Python libs installed: langchain 1.3.9, pydantic-ai 1.107.0, docling, pandas, numpy, plotly, pillow, requests, fastapi, flask, reportlab, weasyprint

### 5️⃣ INFRASTRUCTURE

| Node | Status | RAM | Role |
|---|---|---|---|
| Manus Sandbox | ✅ Active | 512MB | Dev, generation, orchestration |
| GCP Cloud Computer | ✅ Active | 955MB | Scripts légers, batches Python, traces |
| N100 Lambda | ⏳ Pending | 8-16GB | Ollama, n8n, Docker, services 24/7 |

## /yMenu status

When called, check and report:
- Count enabled connectors from config
- List connectors with AUTH_REQUIRED (Semrush, Tally)
- List connectors that FAIL (Typeform MCP → use REST API)
- Count skills with SKILL.md
- Flag thin skills (yos-mmm, yos-voice — need doc update)
- N100 status: pending connection

## /yMenu search [query]

Perform semantic matching across:
1. Skill names + descriptions
2. Connector names + capabilities
3. CLI tool descriptions
4. Infrastructure nodes

Return top 3-5 matches with category and how to use.

## /yMenu create-prompt-library

When triggered, create the prompt library skill:
1. Run `python /home/ubuntu/skills/skill-creator/scripts/init_skill.py prompt-library`
2. Create categories: favorites, multimedia, research, code, data, cognitive, writing
3. Populate with Yannick's known prompt patterns
4. Save to `/home/ubuntu/skills/prompt-library/SKILL.md`

## Routing Logic

After displaying menu, if user selects a skill → read that skill's SKILL.md and execute.
If user selects a connector → call `manus-mcp-cli tool list --server [name]` and show available tools.
If user selects infrastructure → show node status and available actions.
