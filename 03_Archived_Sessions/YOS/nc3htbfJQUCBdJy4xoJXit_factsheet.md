---
uid: nc3htbfJQUCBdJy4xoJXit
session_url: https://manus.im/app/nc3htbfJQUCBdJy4xoJXit
session_title: "Manus Share Link Extractor — Cross-Session Context Injection Fix"
date: 2026-05-07
project: "Y-OS Tooling / Manus Infrastructure"
language: fr
depth: moderate
length: short
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 15:15
referenced_sessions: ["nc3htbfJQUCBdJy4xoJXit"]
referenced_artifacts: ["/home/ubuntu/tools/manus_share_extract.py"]
referenced_urls: ["https://manus.im/share/nc3htbfJQUCBdJy4xoJXit"]
input_files: []
message_count: 20
---

# Manus Share Link Extractor — Cross-Session Context Injection Fix

> **Session:** [nc3htbfJQUCBdJy4xoJXit](https://manus.im/app/nc3htbfJQUCBdJy4xoJXit) | **Date:** 2026-05-07 | **Project:** Y-OS Tooling / Manus Infrastructure | **Language:** fr

## 📋 SESSION CARD

### 🧭 Executive Summary
Yannick needed a way to share Manus session links cross-session (to other LLMs or Manus instances), but the platform deliberately hides connector outputs in shared sessions for privacy. A Python extraction script was built and tested against a real share URL, successfully extracting ~1100 tokens of session content. The tool supports stdout, file output, compact mode, and clipboard injection.

### 🎯 Context & Intent
Yannick regularly references previous Manus sessions from other LLMs (Claude, GPT, Gemini) by pasting context. The `manus.im/share/` links were unreadable by bots/crawlers due to SPA architecture and a platform-level privacy restriction hiding connector outputs. The goal was a reliable extraction workaround enabling cross-session context injection.

### ✅ What Was Done
1. Diagnosed why `manus.im/share/` links fail to load for bots: Next.js SPA returns empty HTML skeleton, direct API returns 503
2. Identified root cause: Manus platform intentionally hides connector outputs in shared sessions (`"Connector output is hidden in shared sessions for privacy reasons"`)
3. Used Firecrawl with JS rendering to partially bypass the restriction and extract readable content
4. Built and tested `manus_share_extract.py` against the real share URL `https://manus.im/share/nc3htbfJQUCBdJy4xoJXit`
5. Validated extraction: ~1100 tokens successfully retrieved
6. Deployed script to `/home/ubuntu/tools/manus_share_extract.py` with multiple output modes

### 💡 Key Insights
- **Manus share pages are SPA (Next.js)** — raw HTML is always empty; JS rendering required
- **Platform privacy policy** is the actual blocker, not network/auth issues — connector outputs are intentionally stripped from shared sessions
- **Firecrawl with JS rendering** is the viable workaround; it can extract the human-readable portion even when the API returns 500
- **Compact mode flag** (`--compact`) is important for token budget management when injecting into other LLMs
- The script doubles as a clipboard injection tool for the paste-into-LLM workflow Yannick already uses

### 📦 Outputs Produced
- **[script]** `/home/ubuntu/tools/manus_share_extract.py`: Python CLI tool — extracts Manus share session content via Firecrawl, supports `--out`, `--compact`, `--clipboard` flags

### ⚠️ Open Items & Blockers
- Connector/tool outputs remain hidden in share links — extracted content is partial (human messages + assistant text only, no tool call results) [INCERTAIN: exact completeness of extracted content]
- `--clipboard` flag requires `xclip` — may not be available in all environments
- [INCERTAIN] Whether the 500 statusCode from Firecrawl will be consistent or flaky across sessions
- Script not yet packaged as a persistent alias/shell command for quick CLI access

### 🔁 Next Steps
1. Add a shell alias (e.g., `manus-extract`) in `.bashrc`/`.zshrc` pointing to the script for faster invocation
2. Test extraction on sessions with heavier tool-call content to benchmark how much is actually lost due to the privacy restriction
3. Consider a `--llm` flag to auto-format output for specific targets (Claude XML, GPT markdown, Gemini plain)
4. Evaluate piping output directly into a new Manus session as a system-prompt injection pattern

### 🔗 Links & References
- 🌐 `https://manus.im/share/nc3htbfJQUCBdJy4xoJXit` — test share URL used for validation
- 📁 `/home/ubuntu/tools/manus_share_extract.py` — deployed extraction script
- 🔗 session:`nc3htbfJQUCBdJy4xoJXit` — the session this card documents

### 🧠 Resume Hint
A working Manus share extractor script lives at `/home/ubuntu/tools/manus_share_extract.py`; it uses Firecrawl to bypass the SPA + privacy restrictions, extracts ~1100 tokens of readable content, and supports compact/clipboard modes for cross-LLM injection — next step is aliasing and testing on tool-heavy sessions.

### 🏷️ Tags
`cross-session-reference` `manus-tooling` `context-injection` `firecrawl` `multi-llm-workflow`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 20 messages — 2026-05-07

**[2026-05-07 00:30] USER:** Souvnt Veux partager une session manus avec manus: qui n'arrive jmais a lire... Fix

**[2026-05-07 00:30] MANUS:** Clarification rapide :

Quand tu dis "partager une session Manus avec Manus" — tu veux dire quoi exactement ?

**① Copier/exporter le contenu d'une session Manus** (historique, messages) pour l'injecter dans une nouvelle session ?

**② Partager un lien de session Manus** avec quelqu'un d'autre (ou une autre instance) qui ne peut pas le lire ?

**③ Autre chose** — ex. charger le contexte d'une session précédente dans la session courante ?

Et "qui n'arrive jamais à lire" → c'est quoi le symptôme exact ? Lien inaccessible ? Contenu vide ? Erreur ?

**[2026-05-07 00:30] USER:** Partager un lien de session Manus a manus (cross seSsion ref

**[2026-05-07 00:30] MANUS:** OK, cross-session reference via lien Manus.

Symptôme exact quand Manus essaie de lire le lien ?

① Erreur 403/401 (accès refusé)
② Page vide / contenu non chargé
③ Manus ignore le lien / ne le traite pas
④ Autre — décris

Et le lien ressemble à quoi ? `app.manus.im/share/...` ou autre format ?

**[2026-05-07 00:43] USER:** A ca https://manus.im/share/nc3htbfJQUCBdJy4xoJXit

**[2026-05-07 00:43] MANUS:** Je teste l'accès à ce lien maintenant.

**[2026-05-07 00:46] MANUS:** ## 🔍 Diagnostic — Cross-session reference via `manus.im/share/`

### Cause racine identifiée

La page `manus.im/share/...` est une **SPA React (Next.js)** qui charge le contenu **dynamiquement via JS côté client**. Quand Manus (ou n'importe quel bot/crawler) tente de la lire :

- Le HTML brut retourné = **squelette vide** (pas de contenu de session)
- L'API directe `/api/share/...` retourne **503**
- Firecrawl (avec JS rendering) récupère le contenu **mais** rencontre un `statusCode: 500` côté Manus + cette ligne critique :

> `"Connector output is hidden in shared sessions for privacy reasons"`

**→ Manus masque délibérément les outputs des outils dans les sessions partagées.** C'est une restriction de sécurité/privacy côté plateforme, pas un bug réseau.

---

### Ce que Firecrawl peut li

**[2026-05-07 00:48] USER:** Oui, injection optionnelle(dS clipboard--° parfois je pate dans autre llm

**[2026-05-07 00:48] MANUS:** Construction du script — extraction Firecrawl + copie clipboard + injection contexte.

**[2026-05-07 00:51] MANUS:** ## ✅ `manus-extract` — Script opérationnel

**Testé sur ton lien réel.** Fonctionne. ~1100 tokens extraits.

---

### 📦 Script installé

`/home/ubuntu/tools/manus_share_extract.py`

---

### 🔧 Usage

```bash
# Affichage stdout (pour coller dans Manus)
python3 ~/tools/manus_share_extract.py https://manus.im/share/XXXX

# Sauvegarde fichier
python3 ~/tools/manus_share_extract.py https://manus.im/share/XXXX --out context.md

# Format compact (moins de tokens — pour Claude/GPT/Gemini)
python3 ~/tools/manus_share_extract.py https://manus.im/share/XXXX --compact

# Clipboard (si xclip dispo — sinon affiche stdout)
python3 ~/tools/manus_share_extract.py https://manus.im/share/XXXX --clipboard

# Combiné : compact + fichier
python3 ~/tools/manus_share_extract.py https://manus.im/share/XXXX --compa
