---
uid: XVO3HPIAGvrJiy00zR9S6m
session_url: https://manus.im/app/XVO3HPIAGvrJiy00zR9S6m
session_title: "Roberta GDrive access check — sandbox credential injection diagnostic"
date: 2026-05-07
project: "Y-OS Infrastructure / GDrive Setup"
language: mixed
depth: quick
length: short
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 15:15
referenced_sessions: []
referenced_artifacts: []
referenced_urls: []
input_files: []
message_count: 5
---

# Roberta GDrive access check — sandbox credential injection diagnostic

> **Session:** [XVO3HPIAGvrJiy00zR9S6m](https://manus.im/app/XVO3HPIAGvrJiy00zR9S6m) | **Date:** 2026-05-07 | **Project:** Y-OS Infrastructure / GDrive Setup | **Language:** mixed

## 📋 SESSION CARD

### 🧭 Executive Summary
Yannick signaled access to a new Google Drive ("Roberta GDrive") and asked Manus to confirm its visibility. Manus diagnosed the sandbox environment and found only one configured remote (`manus_google_drive`). The new drive was not yet accessible due to sandbox credential injection limitations at session start.

### 🎯 Context & Intent
Yannick had just connected a second Google Drive account (labeled "Roberta GDrive") via the Manus frontend and wanted to verify that Manus could see and interact with it within the active session.

### ✅ What Was Done
1. Checked active rclone remotes — found only `manus_google_drive`
2. Inspected Manus connector configuration — confirmed single Google Drive account
3. Checked gws CLI for multi-account config — none found
4. Diagnosed the likely cause: new credentials added frontend-side are not injected into an already-running sandbox

### 💡 Key Insights
- Manus sandbox credentials are injected **at session start** — adding a new connector mid-session does not propagate to the running environment
- Multi-GDrive access (e.g., a second account like "Roberta") requires a **fresh session** to be recognized
- No multi-account rclone config exists; each session appears scoped to a single Drive remote

### 📦 Outputs Produced
- *(None — diagnostic session only, no files or artifacts produced)*

### ⚠️ Open Items & Blockers
- ⚠️ "Roberta GDrive" is not accessible in this session — blocker for any cross-drive operations
- [INCERTAIN] It is unclear whether Manus supports true multi-GDrive in a single session even after restart
- [INCERTAIN] The exact connector name/ID assigned to Roberta's drive on the Manus frontend is unknown

### 🔁 Next Steps
1. **Start a new Manus session** to allow fresh credential injection and re-check for "Roberta GDrive"
2. Confirm in the new session that `rclone listremotes` or equivalent shows a second remote
3. If still absent, investigate Manus multi-account Drive setup documentation or support
4. Once accessible, define the intended use of Roberta GDrive (read, sync, copy, etc.)

### 🔗 Links & References
- 🔗 session:`XVO3HPIAGvrJiy00zR9S6m` — current session (GDrive access diagnostic)

### 🧠 Resume Hint
Yannick added "Roberta GDrive" as a second Google Drive connector in Manus, but it was not visible in this session's sandbox — start a fresh session and verify with `rclone listremotes` before proceeding with any cross-drive tasks.

### 🏷️ Tags
`gdrive` `multi-account` `sandbox-config` `access-diagnostic` `rclone`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 5 messages — 2026-05-07

**[2026-05-07 15:44] USER:** i git access to snother gdrive: do you se it ("roberta gdrive")

**[2026-05-07 15:44] MANUS:** Je vérifie les accès GDrive disponibles dans la session.

**[2026-05-07 15:45] MANUS:** ## 🔍 GDrive — État des accès

**Non, je ne vois pas de "Roberta GDrive"** dans la session actuelle.

### Ce que je vois

| Remote | Type | Statut |
|---|---|---|
| `manus_google_drive` | Google Drive (rclone) | ✅ Actif — ton compte principal |
| `Google Drive` connector | Manus config | ✅ Enabled (1 seul compte) |

### Diagnostic

- **rclone** → 1 seul remote configuré : `manus_google_drive`
- **Manus config** → 1 seul connecteur Google Drive (pas de multi-compte)
- **gws CLI** → pas de config multi-compte
- Aucune trace de "roberta" dans la config

### Probable cause

Le "Roberta GDrive" a été ajouté côté **Manus frontend** (nouveau connecteur), mais la session sandbox actuelle n'a pas encore reçu les credentials mis à jour. La config sandbox est injectée au démarrage de session.

### Act
