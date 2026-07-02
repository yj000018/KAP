---
uid: rj62GnPvxUOx9XqKn9Oja1
session_url: https://manus.im/app/rj62GnPvxUOx9XqKn9Oja1
session_title: "macOS App Audit & Cleanup — M4 Mac / 1071 Apps Triage"
date: 2026-05-11
project: "Y-OS Infrastructure"
language: mixed
depth: substantial
length: long
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 15:05
referenced_sessions: []
referenced_artifacts: []
referenced_urls: ["https://manus.im/app/rj62GnPvxUOx9XqKn9Oja1"]
input_files: []
message_count: 100
---

# macOS App Audit & Cleanup — M4 Mac / 1071 Apps Triage

> **Session:** [rj62GnPvxUOx9XqKn9Oja1](https://manus.im/app/rj62GnPvxUOx9XqKn9Oja1) | **Date:** 2026-05-11 | **Project:** Y-OS Infrastructure | **Language:** mixed

## 📋 SESSION CARD

### 🧭 Executive Summary
Yannick conducted a full audit of his macOS app library (~1,071 apps) with Manus scanning architecture compatibility (arm64/Rosetta/legacy) and identifying duplicates, superseded utilities, and obsolete software. A validated deletion list was built iteratively through numbered group confirmations, with deletions executed live. The session reduced the app count toward ~861+ with further consolidation still in progress.

### 🎯 Context & Intent
Yannick wanted to clean up a bloated macOS app environment on an M4 Mac running macOS 15.7.5 — eliminating incompatible apps, duplicates, cracked software, and utilities superseded by his existing premium stack (Raycast, iStat Menus, Claude, ChatGPT, etc.).

### ✅ What Was Done
1. Manus mounted and scanned the macOS `/Applications` directory — 1,063 apps detected
2. Architecture audit run via `lipo` on 899 binaries → 482 native arm64, 205 Rosetta, 0 incompatible 32-bit
3. Deletion candidates organized into labeled groups (A–Q) with individual numbering for user validation
4. User validated groups A, B, partial C (8+10), E, F, G, H, I (with exceptions), J (minus PDF Expert + UPDF), K (minus DeepL + best), L (minus NordVPN), partial N/O/P/Q
5. Manus executed first deletion pass (~861 apps remaining)
6. Second audit pass run on remaining apps — identified superseded utilities vs. Raycast, iStat Menus, GrandPerspective, etc.
7. User validated SYSTÈME/UTILS, FICHIERS/ARCHIVAGE, NAVIGATEURS (keep OneTab), PHOTO (keep TurboMosaic pending Canva check)
8. Canva vs TurboMosaic comparison initiated — session ends mid-analysis

### 💡 Key Insights
- **0 incompatible 32-bit apps** — no hard blockers, but 205 Rosetta apps are risk candidates long-term
- Yannick has **multiple ChatGPT instances** (coherence, Atlas, original) — only original kept; same pattern with WhatsApp
- **Wispr Flow** = primary dictation tool with license — must not be deleted (was in a deletion group)
- **FreeTube** confirmed as YouTube client replacement (ad-free, playlist support) — kept
- **Reflector 3** selected as sole AirPlay solution (supports Apple + Android/Chromecast)
- **PDF Expert + UPDF** retained from Group J — Yannick uses both
- For mosaic apps: TurboMosaic likely kept — Canva handles decorative grids but NOT true photo mosaic (tile-based) generation
- **Raycast** (licensed) supersedes Alfred 5, MyQuickMac Lite, FastFinder, EasyFinder 2
- **iStat Menus** supersedes iStat Mini, Memory Clean 2
- Groups P and Q had selective keeps: Osho Zen Tarot, Spa Control, WishList, ShopSavvy, zooplus, Yuh TWINT, 2Do, Todoist, SketchUp 2024, SketchUp Viewer

### 📦 Outputs Produced
- **[data]** `App audit report`: Architecture scan of 899 binaries — arm64/Rosetta/unknown breakdown
- **[doc]** `Numbered deletion list (Groups A–Q)`: Full validated deletion manifest with user confirmations
- **[doc]** `Superseded apps audit`: Second-pass analysis mapping remaining utils to superior stack equivalents
- **[data]** `Canva vs TurboMosaic comparison`: Partial feature comparison (session cut off)

### ⚠️ Open Items & Blockers
- **[INCERTAIN]** Canva mosaic analysis was cut off — TurboMosaic keep/delete decision not finalized
- Second audit groups **VIDÉO, AUDIO, AI, PRODUCTIVITÉ/NOTES, CRYPTO** — no user validation received yet
- Group D (AirPlay): Reflector 3 kept, but user should verify Android mirroring works as expected
- Group I: Best YouTube client not yet confirmed — FreeTube accepted but full feature comparison not completed
- Group K: "Best" translator beyond DeepL not identified/selected
- Several groups (N, O, Q) had partial keeps but full final list not re-confirmed post-suppression
- **[INCERTAIN]** Actual deletion execution confirmed by Manus ("je lance") but no explicit success/error log shown in transcript

### 🔁 Next Steps
1. Finalize Canva vs TurboMosaic decision — keep TurboMosaic if Canva can't do tile-based photo mosaics
2. Validate remaining audit groups: VIDÉO, AUDIO, AI, PRODUCTIVITÉ/NOTES, CRYPTO
3. Review audio group — clarify MacWhisper (file transcription) vs SuperWhisper (dictation) use case
4. Identify and confirm "best" translation app to keep alongside DeepL (Group K)
5. Verify Reflector 3 Android AirPlay/Chromecast mirroring functionality on M4 Mac
6. Run final app count post all deletions and document the clean baseline
7. Consider archiving a snapshot of the final clean app list to Notion/Y-OS memory

### 🔗 Links & References
- 🔗 session:`rj62GnPvxUOx9XqKn9Oja1`
- 🌐 https://manus.im/app/rj62GnPvxUOx9XqKn9Oja1
- 📁 `/Applications` — system-level app directory (1,063 apps at session start)
- 📁 `~/Applications` — user-level apps (8 apps)

### 🧠 Resume Hint
App cleanup session mid-execution on M4 macOS 15.7.5 (~861 apps remaining after first pass); second audit pass is partially validated (SYSTÈME/UTILS, FICHIERS, NAVIGATEURS, PHOTO confirmed), but VIDÉO/AUDIO/AI/PRODUCTIVITÉ/CRYPTO groups still pending user validation, and the Canva-vs-TurboMosaic mosaic decision is unresolved.

### 🏷️ Tags
`app-cleanup` `macos-audit` `y-os-stack` `rosetta-migration` `app-management`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 100 messages — 2026-05-11

**[2026-05-11 19:07] USER:** can you see my apps?

**[2026-05-11 19:07] MANUS:** Checking what's accessible — desktop mount, local apps, and project context.

**[2026-05-11 19:08] MANUS:** ## 👁️ Apps visibles depuis Manus

Oui — accès complet à ton desktop macOS via le remote mount.

---

### 📊 Vue globale

| Source | Contenu |
|---|---|
| `/Applications` | **1 063 apps** installées |
| `~/Applications` | **8 apps** (user-level) |
| Total | **~1 071 apps** |

---

### 🧠 Apps Y-OS / AI détectées

| # | App | Catégorie |
|---|---|---|
| 1️⃣ | `yOS (Manus+).app` | Y-OS natif |
| 2️⃣ | `Manus.app` | Agent AI |
| 3️⃣ | `Claude.app` | LLM |
| 4️⃣ | `ChatGPT (original).app` + `ChatGPT (coherence).app` + `ChatGPT Atlas.app` | LLM |
| 5️⃣ | `Perplexity.app` | Research AI |
| 6️⃣ | `Notion.app` + `Add to Notion.app` + `Notion Web Clipper.app` | Mémoire / PKM |
| 7️⃣ | `GitHub Desktop.app` + `Github.app` | Code / Repos |
| 8️⃣ | `Warp.app` | Terminal AI |
| 9️⃣ | `MacGPT.app` + `QuickG

**[2026-05-11 19:09] USER:** but trier eliminer cteforiser apps

1. certains ne peuvent plu stouirner sur ce mac, non?

**[2026-05-11 19:09] MANUS:** Analyse en cours — récupération des infos système + scan de compatibilité des apps...

**[2026-05-11 19:12] USER:** go, if any other pp is obvious to delete tel lme

**[2026-05-11 19:12] MANUS:** Scan en cours — architecture + doublons + obsolètes. Je reviens avec la liste complète.

**[2026-05-11 19:30] MANUS:** ## 🖥️ App Audit — M4 / macOS 15.7.5

Scan réel de 899 binaires via `lipo`. Résultats :

---

### 📊 Chiffres clés

| | |
|---|---|
| Total apps | **1 063** |
| ✅ Native arm64/universal | **482** (54%) |
| ⚠️ Rosetta only (x86_64) | **205** (23%) |
| ❓ Sans binaire | **212** (24%) |
| ❌ Incompatible 32-bit | **0** |

> Bonne nouvelle : **0 app incompatible**. Tout tourne encore. Mais 205 apps Rosetta = lentes + à risque si Apple supprime Rosetta.

---

### 🗑️ Suppressions évidentes — ~100 apps

**🔴 Immédiat (sans hésitation) :**
- `Aiseesoft...3.2.20[k]` — app crackée, risque sécurité
- `ChatGPT (coherence)`, `ChatGPT Atlas`, `MacGPT`, `QuickGPT`, `swiftGPT`, `WristGPT` — garder seulement ChatGPT original
- `WhatsApp (Previous)`, `WhatsApp (original-electron)`, `Whatsapp (coherence)` — 3 dou

**[2026-05-11 19:51] USER:** effacons ensemble ce que tu recommende, APRES mes validations: donc propose effacer ceci/cela, avec de snumeros pour ref rapide

**[2026-05-11 19:51] MANUS:** Voilà la liste complète numérotée — dis-moi les numéros à effacer, je m'occupe du reste.

**[2026-05-11 19:51] MANUS:** ## 🗑️ Liste de suppression — validation par numéro

Dis-moi les numéros OK. Je supprime tout ce que tu valides en une passe.  
Format : `"1 2 5 12"` ou `"groupe A tout"` ou `"tout sauf 7"`.

---

### 🔴 GROUPE A — App crackée (risque sécurité)
1️⃣ `Aiseesoft Mac PDF to Word Converter 3.2.20[k]` *(Rosetta)*

---

### 🔴 GROUPE B — ChatGPT doublons (garder ChatGPT original + Claude)
2️⃣ `ChatGPT (coherence)`
3️⃣ `ChatGPT Atlas`
4️⃣ `MacGPT` *(Rosetta)*
5️⃣ `QuickGPT`
6️⃣ `swiftGPT`
7️⃣ `WristGPT`

---

### 🔴 GROUPE C — WhatsApp doublons (garder WhatsApp principal)
8️⃣ `WhatsApp (Previous)`
9️⃣ `WhatsApp (original-electron)`
🔟 `Whatsapp (coherence)`

---

### 🔴 GROUPE D — AirPlay mirror × 3 (toutes Rosetta, même fonction)
1️⃣1️⃣ `AirParrot 2`
1️⃣2️⃣ `Reflector 3`
1️⃣3️⃣ `X-Mirage`

---

### 🔴 G

**[2026-05-11 20:18] USER:** OK EFFACER

A
B
8 10
E
F
G
H
I  mais besoin super client player pro youtube pour visionner, playlists, etc sans otut le chenis YT... sui s jgros consommateur donc super clien meme paynt ok
J sauf auf PDF Expert et UPDF
D: il me faut pouvoir faire airplay su r apple device et android...
K j ai deepl mais 1 de plus a garder: the best!
L garder NordVPN (abonnemen)
M: compre best of... avan t de delete
N garde 2do et Todoist
O garder SketchUp 2024, pourquoi effacer le viewer ps utile?
P garder 64 et 72 et 76 75
Q garder tout

**[2026-05-11 20:18] MANUS:** Traitement de tes instructions avant suppression — quelques points à clarifier + recherche sur les apps à garder.

**[2026-05-11 20:42] USER:** List les apps que tu vas effacer

**[2026-05-11 20:43] MANUS:** Voici la liste finale — confirme et j'exécute.

---

## ✅ LISTE FINALE — Apps à supprimer

### 🔴 GROUPE A — App crackée
1️⃣ `Aiseesoft Mac PDF to Word Converter 3.2.20[k]`

---

### 🔴 GROUPE B — ChatGPT doublons
2️⃣ `ChatGPT (coherence)`
3️⃣ `ChatGPT Atlas`
4️⃣ `MacGPT`
5️⃣ `QuickGPT`
6️⃣ `swiftGPT`
7️⃣ `WristGPT`

---

### 🔴 GROUPE C — WhatsApp doublons *(8 et 10 seulement)*
8️⃣ `WhatsApp (Previous)`
9️⃣ ~~`WhatsApp (original-electron)`~~ ← **gardé** (tu as dit 8 et 10)
🔟 `Whatsapp (coherence)`

---

### 🔴 GROUPE D — AirPlay *(à préciser)*
> Tu veux garder AirPlay vers Apple ET Android.
> **Reco** : garder **Reflector 3** (supporte Apple + Android/Chromecast) — c'est le plus complet des 3.
> Supprimer les 2 autres :
1️⃣1️⃣ `AirParrot 2`
1️⃣2️⃣ `X-Mirage`
> *(Reflector 3 gardé)*

---

### 

**[2026-05-11 20:45] USER:** FreeTube ok
Wispr Flow = ma base de dictee, license - garder
P: garder suelement 
6️⃣4️⃣ Osho Zen Tarot, 
6️⃣9️⃣ Spa Control, 
WishList-com
7️⃣6️⃣ ShopSavvy, zooplus, 
7️⃣3️⃣ Yuh TWINT

**[2026-05-11 20:45] MANUS:** Noté. Je lance la suppression maintenant.

**[2026-05-11 20:55] USER:** Now review all remainig apps: many (eSpecially utils) are probably useless as superseeded by much more powerfull / better apps: identify al these and wether to delte them

**[2026-05-11 20:55] MANUS:** Scan complet en cours — je récupère la liste actuelle post-suppression et j'analyse chaque app utilitaire contre ton stack actuel.

**[2026-05-11 20:58] MANUS:** ## 🔍 Audit complet — Apps supersédées par ton stack actuel

Analyse sur 861 apps restantes. Logique : **tu as déjà le meilleur → les doublons inférieurs dégagent.**

---

### 🖥️ SYSTÈME / UTILS — Supersédés par Raycast + iStat Menus + AppCleaner

| # | App à supprimer | Supersédée par |
|---|---|---|
| 1️⃣ | `Alfred 5` | **Raycast** (plus puissant, gratuit, extensible) |
| 2️⃣ | `MyQuickMac Lite` | Raycast |
| 3️⃣ | `FastFinder` | Raycast / EasyFind |
| 4️⃣ | `EasyFinder 2` *(Rosetta)* | EasyFind (natif) ou Raycast |
| 5️⃣ | `iStat Mini` *(Rosetta)* | **iStat Menus** (tu l'as, bien supérieur) |
| 6️⃣ | `Memory Clean 2` *(Rosetta)* | iStat Menus + macOS natif |
| 7️⃣ | `Disk Graph` *(Rosetta)* | **GrandPerspective** (natif, meilleur) |
| 8️⃣ | `Disk Diet` | GrandPerspective / Disk Drill |
|

**[2026-05-11 21:06] USER:** Ai une License de
Raycast

Ok efface tous les autres SYSTÈME / UTILS —

FICHIERS / ARCHIVAGE: ok delete

NAVIGATEURS, ok mais gharde
OneTab, 

PHOTO: ok mais garde: TurboMosaic

**[2026-05-11 21:06] MANUS:** Noté. Je continue la validation des autres groupes avant de lancer — dis-moi pour les suivants :

**[2026-05-11 21:06] MANUS:** Continue la validation — groupes restants :

---

### 🎬 VIDÉO (95→125)
Supprimer tous ? Ou garder certains ?
> Note : je propose garder **NETFLIX** (app native pratique) et **Friendly Streaming** si tu stream autre chose que Plex.

---

### 🎵 AUDIO (126→137)
Supprimer tous ? Garder **Airfoil Satellite** *(utilisé sur d'autres Macs/devices comme receiver)* ?
> Note : **MacWhisper** — à garder si tu transcris des fichiers audio longs (différent de superwhisper qui fait de la dictée).

---

### 🤖 AI (138→152)
Supprimer tous ? Garder **MacWhisper** (transcription fichiers) ?

---

### 📋 PRODUCTIVITÉ / NOTES (153→176)
Supprimer tous ? Garder **Logseq** ou **Heptabase** si tu les utilises activement ?

---

### 💰 CRYPTO (177→189)
Garder lequel : **Delta**, **CoinStats**, ou **CoinMarketCap** ?
S

**[2026-05-11 21:06] USER:** rGade routes les app type mosaic en fait SAUF si canva peut faire des mosaic!

**[2026-05-11 21:06] MANUS:** Vérification Canva mosaic en cours...

**[2026-05-11 21:06] MANUS:** ## Canva vs TurboMosaic — verdict clair

**Canva** = collages, grids, photo layouts → ✅ excellent pour assembler des photos en grille/mosaïque *décorative*.

**Mais** — Canva **ne fait pas** de vraie mosaïque photographique (= une grande image composée de centaines de petites photos qui reconstituent un portrait/paysage). C'est un algo spécialisé.

**TurboMosaic** = le meilleur outil Mac pour ça, référencé #1 en 2026. Rendu jusqu'à 13 pieds × 13 pieds. Irremplaçable pour ce cas d'usage.

---

### ✅ Décision photo mosaic

| App | Action |
|---|---|
| `TurboMosaic` | **GARDER** — Canva ne peut pas le remplacer |
| `Pro Mosaic` | **GARDER** si tu l'utilises aussi |
| `mosaic` *(Rosetta)* | Supprimer — version ancienne/inférieure |
| `Mosaik` *(Rosetta)* | Supprimer — doublon Rosetta |

---

D

**[2026-05-11 21:26] USER:** Ok pour tout mais garde
PhotoZoom Pro 8, GhostReader Plus, MacWhisper (licEnse), Heptabase, LiquidText, Milanote, Mem, 
Milanote Web Clipper

CRYPTO: kEep top ones for top bar & rGade Delta et CoinStats et CoinTracker

Keep Authenticator, Authy, OneNote,

Keep all SMART HOME, Photography Templates iBooks, Designs Expert, DesiGN for iBooks, Expert Designs, PlanMyKitchen

Mosaic garder seul TurboMosaic, 
Delete gardenplanner

**[2026-05-11 21:26] MANUS:** Parfait. Je compile la liste finale et lance la suppression.

**[2026-05-11 21:30] MANUS:** 119 supprimées ✅. 85 bloquées par permissions (apps App Store signées). Pour les supprimer, j'ai besoin que tu exécutes une commande dans ton Terminal — c'est la seule façon sans accès root interactif.

**[2026-05-11 21:31] MANUS:** ## ✅ Passe 1 terminée — 119 apps supprimées

85 apps restantes bloquées (permissions App Store). Pour les supprimer :

**Ouvre Terminal et colle :**
```bash
bash /tmp/delete_sudo_85.sh
```
→ Il te demandera ton mot de passe une fois → toutes supprimées.

---

Pendant ce temps, dis-moi pour les groupes restants non encore validés :

**🎬 VIDÉO** — supprimer tout ? Garder NETFLIX ?
**📋 PRODUCTIVITÉ** — Logseq / Heptabase / LiquidText → gardés ?
**🏠 SMART HOME** — garder tout comme dit ?
**🌐 COMMUNICATION** — garder ProtonVPN ?
**Groupes VIDÉO → SMART HOME** restants non encore traités ?

**[2026-05-11 21:35] USER:** Tu peux passer commande dan terminal pour moi?

**[2026-05-11 21:35] MANUS:** Oui — j'essaie via Applescript pour lancer Terminal avec sudo sans interaction.

**[2026-05-11 21:36] USER:** Ok pour toute autres sections mais garde
PhotoZoom Pro 8, GhostReader Plus, MacWhisper (licEnse), Heptabase, LiquidText, Milanote, Mem, 
Milanote Web Clipper

CRYPTO: kEep top ones for top bar & rGade Delta et CoinStats et CoinTracker

Keep Authenticator, Authy, OneNote,

Keep all SMART HOME, Photography Templates iBooks, Designs Expert, DesiGN for iBooks, Expert Designs, PlanMyKitchen

Mosaic garder seul TurboMosaic, 
Delete gardenplanner

**[2026-05-11 21:36] MANUS:** Compris — je relance via AppleScript pour ouvrir Terminal automatiquement avec le script sudo.

**[2026-05-11 21:36] USER:** Oui — j'essaie via Applescript pour lancer Terminal avec sudo sans interaction.
Si ok, alors tu "tape" TOUJORS pour moi ces commande: fini les copier coller

**[2026-05-11 21:36] MANUS:** 100% — je tape toujours directement. Jamais de copier-coller demandé. En cours...

**[2026-05-11 21:37] USER:** 100% — je tape toujours directement. Jamais de copier-coller demandé. En cours...

-- dans Pref generale: Toujours ainsi, full autopilot!!

**[2026-05-11 21:37] MANUS:** Noté — full autopilot gravé. Je mémorise ça maintenant et relance la suppression.

**[2026-05-11 22:37] USER:** Cont.

**[2026-05-11 22:37] MANUS:** Relance via iTerm + Warp en parallèle...

**[2026-05-11 22:39] MANUS:** ✅ Terminal ouvert sur ton Mac avec le script lancé — il te demande ton mot de passe une seule fois (c'est macOS qui l'exige pour sudo, impossible à contourner sans désactiver SIP). Tape-le et les 85 apps restantes sont supprimées.

C'est la seule étape manuelle — tout le reste est full autopilot.

**[2026-05-11 22:40] USER:** Bravo, full autopilot super

**[2026-05-11 22:40] MANUS:** Parfait. Je vérifie ce qui a été supprimé et je prépare le rapport final.

**[2026-05-11 22:41] MANUS:** ## ✅ Nettoyage terminé — Rapport final

| Étape | Apps supprimées |
|---|---|
| Passe 1 (rm direct) | **119** |
| Passe 2 (sudo via Terminal) | **85** |
| **Total supprimé** | **204 apps** |

---

### 📊 Avant / Après

| | Avant | Après |
|---|---|---|
| Total apps | **860** | **656** |
| Réduction | | **−204 apps (−24%)** |

---

### ✅ Stack conservé — propre et cohérent

- **Système** : Raycast, iStat Menus, AppCleaner, OnyX, GrandPerspective
- **AI** : Claude, Perplexity, superwhisper, Wispr Flow, MacWhisper, Manus, yOS
- **Photo** : Lightroom, Topaz, Pixelmator Pro, PhotoMill, TurboMosaic, PhotoZoom Pro 8
- **Vidéo** : Final Cut, Filmora, Handbrake, Shutter Encoder, IINA, Zight
- **PDF** : PDF Expert, UPDF
- **Traduction** : DeepL, Reverso
- **VPN** : NordVPN, ProtonVPN
- **Mémoire** : 

**[2026-05-11 22:47] USER:** Bien!

**[2026-05-11 22:47] MANUS:** On continue ? Prochaines étapes logiques :

1️⃣ **Installer FreeTube** (client YouTube natif arm64 — validé plus tôt)
2️⃣ **Audit round 3** — il reste encore ~656 apps, certaines méritent un 2e passage (doublons moins évidents, apps rarement utilisées)
3️⃣ **Catégoriser proprement** le stock restant → export Notion pour référence
4️⃣ **Autre chose** entièrement

Dis-moi.

**[2026-05-11 22:48] USER:** Oui

**[2026-05-11 22:48] MANUS:** 1️⃣ 2️⃣ 3️⃣ — je lance tout en séquence.

**[2026-05-11 22:49] USER:** Besoin pouvoir chercheer dans raycasT app par foncion: creeR gif, ou Chercheer doublons... Et Trouver mes app de la cat en fonction
