---
uid: PIrfBF2GHJOdeSxsEnmlXu
session_url: https://manus.im/app/PIrfBF2GHJOdeSxsEnmlXu
session_title: "Fritz!Box + Deco XE75 Mesh + Sonos — Architecture & Reset Setup"
date: 2026-05-18
project: "Home Network Configuration"
language: fr
depth: moderate
length: short
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 14:56
referenced_sessions: []
referenced_artifacts: []
referenced_urls: ["https://manus.im/app/PIrfBF2GHJOdeSxsEnmlXu"]
input_files: []
message_count: 13
---

# Fritz!Box + Deco XE75 Mesh + Sonos — Architecture & Reset Setup

> **Session:** [PIrfBF2GHJOdeSxsEnmlXu](https://manus.im/app/PIrfBF2GHJOdeSxsEnmlXu) | **Date:** 2026-05-18 | **Project:** Home Network Configuration | **Language:** fr

## 📋 SESSION CARD

### 🧭 Executive Summary
Yannick initiated a home network configuration session to set up a Fritz!Box + TP-Link Deco XE75 mesh + Sonos ecosystem. Manus provided a reset procedure for the Deco units and the key architectural principle (Fritz as router, Deco in Access Point mode, Fritz WiFi disabled). The session was cut short mid-explanation — the Sonos configuration advice was not completed.

---

### 🎯 Context & Intent
Yannick needs to rebuild/reconfigure a home network combining:
- A recent Fritz!Box (likely Fritz!Box 7590 or 7690 with WiFi 6) as the main router
- 3× TP-Link Deco XE75 units as a WiFi 6 mesh system
- Sonos speakers on top of the mesh

Primary blockers: couldn't reset the Deco units, and was unsure of the optimal architecture (Fritz WiFi on or off? Deco in router or AP mode?).

---

### ✅ What Was Done
1. Clarified hardware context via back-and-forth (3× Deco XE75, recent Fritz!Box WiFi 6)
2. Defined the optimal network architecture: Fritz!Box as router, Deco XE75 in **Access Point mode**, Fritz WiFi disabled
3. Explained the "double NAT" problem and why it's critical to avoid for Sonos stability
4. Provided Deco XE75 reset procedure (short 1–2s press, LED sequence: yellow → blinking blue)
5. Began Sonos integration advice (cut off mid-sentence)

---

### 💡 Key Insights
- **Architecture rule**: Fritz!Box handles routing/NAT; Deco XE75 handles all WiFi in AP mode — this is the stable configuration for Sonos
- **Double NAT is fatal for Sonos**: running two routers in series causes Sonos discovery/stability failures
- **Fritz WiFi should be disabled** when Deco mesh is in place — no benefit in running both simultaneously
- **Deco reset**: short press only (1–2s), NOT the long 10s press which may have different behavior
- Hardware confirmation: 3× Deco XE75 (WiFi 6E capable), Fritz!Box WiFi 6 — well-matched for a high-performance mesh setup

---

### 📦 Outputs Produced
- **[doc]** `architecture-fritzbox-deco-sonos`: Inline architectural recommendation (Fritz router + Deco AP mode + Sonos wiring rules) — produced in chat, not saved as file
- **[doc]** `deco-xe75-reset-procedure`: Step-by-step reset instructions delivered in session

---

### ⚠️ Open Items & Blockers
- ⚠️ Sonos integration advice was **cut off mid-sentence** — rule about Sonos wiring/connection was not completed
- [INCERTAIN] Exact Fritz!Box model not confirmed (assumed 7590/7690 WiFi 6 based on context)
- [INCERTAIN] Whether Deco units were actually reset successfully — no user confirmation received
- [INCERTAIN] ISP connection type (fibre/ADSL/cable) not established — may affect Fritz!Box WAN config
- [INCERTAIN] Whether Fritz WiFi disablement steps were provided (session ended before covering this)

---

### 🔁 Next Steps
1. **Confirm Deco reset succeeded** — verify LED blinks blue after reset procedure
2. **Complete Sonos integration rules** — resume the cut-off advice (wired vs wireless, SonosNet vs WiFi mode)
3. **Disable Fritz!Box WiFi** — walk through the Fritz!Box admin UI to turn off 2.4GHz and 5GHz radios
4. **Configure Deco XE75 in AP mode** — step-by-step via Deco app (set main unit to AP mode before pairing satellites)
5. **Verify ISP/WAN type** on Fritz!Box to ensure correct internet connection setup
6. **Test Sonos discovery** post-setup and validate mesh stability

---

### 🔗 Links & References
- 🌐 https://manus.im/app/PIrfBF2GHJOdeSxsEnmlXu — Session URL
- 📄 TP-Link Deco XE75 product page (not linked — reference for reset procedure validation)
- 📄 Fritz!Box admin UI: `http://fritz.box` (standard local access)

---

### 🧠 Resume Hint
User has 3× Deco XE75 + Fritz!Box WiFi 6; architecture decided (Fritz router, Deco in AP mode, Fritz WiFi off); Deco reset procedure given but not confirmed successful; Sonos advice was cut off mid-sentence — resume from "don't wire any Sonos speaker to…" and complete full Sonos + mesh integration steps.

---

### 🏷️ Tags
`home-network` `wifi-mesh` `fritzbox` `deco-xe75` `sonos` `access-point-mode`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 13 messages — 2026-05-18

**[2026-05-18 10:34] USER:** YOu are an IT expert helping me with my wifi/network

 have to configure  DECO mesh to extend, think best is Fritz as router (NO WIFI as not mesh?? or better use fritz ifi 6 + extnad with deco?... need o add sonos on top, so mesh must work well 
)but 1rst need to reset them : cant manage

**[2026-05-18 10:34] MANUS:** Contexte capté. Avant de te donner l'archi optimale + procédure reset, j'ai besoin de 3 précisions :

**① Quel modèle exact de DECO ?**
(ex: Deco M5, Deco XE75, Deco BE85…) — ça change la procédure reset et les capacités mesh

**② Quel modèle exact de Fritz !Box ?**
(ex: Fritz!Box 7590, 7690, 6591…) — pour savoir si tu as le Fritz!Repeater ou juste la box

**③ Combien de Deco units tu as, et quel est ton setup actuel ?**
(ex: 3 Deco en place, Fritz comme modem/routeur en entrée, FAI = fibre/ADSL/câble ?)

Avec ça je te donne : reset procédure + archi recommandée Fritz+Deco+Sonos en un bloc.

**[2026-05-18 10:35] USER:** continue

**[2026-05-18 10:35] MANUS:** Tu veux que je continue sans les infos ? Je peux te donner :

**Option A** — Procédure reset générique Deco (couvre 90% des modèles) + archi recommandée Fritz+Deco+Sonos en mode "best practice"

**Option B** — Attendre tes réponses pour une config 100% précise

👉 Dis-moi A ou B — ou donne-moi les infos modèles directement.

**[2026-05-18 15:12] USER:** Alors, trois décors. Sauf erreur, c'est un, euh... C'est une des dernières frites box. Euh, il y a le wifi- Je pensais que tu l'aidais sur Wi-Fi 6. C'est pour ça que j'ai changé de papier, que... Pour aller avec les décos qui doivent être des 75. Euh...

**[2026-05-18 15:12] MANUS:** OK, je synthétise ce que j'ai compris + je complète avec les best practices. On va tout couvrir.

**[2026-05-18 15:13] MANUS:** Voici l'architecture optimale et la procédure exacte, structurées pour ton matériel.

### 💡 Le concept clé (Architecture)
Ta Fritz!Box est un excellent routeur. Les Deco XE75 sont d'excellents points d'accès WiFi Mesh. 
👉 **La règle d'or :** Il faut désactiver le WiFi de la Fritz!Box, et configurer les Deco en mode **"Point d'accès" (Access Point)**. Cela évite le "Double NAT" (deux routeurs qui se marchent dessus), ce qui est mortel pour la stabilité de Sonos.

### 🔄 Le Reset des Deco XE75
1. Appareil allumé, trouve le bouton Reset en dessous.
2. Appuie avec un trombone **1 à 2 secondes** (pas plus, pas 10 secondes). La LED devient jaune.
3. Attends 2 minutes jusqu'à ce que ça clignote en bleu.

### 🎵 La règle pour Sonos
Avec un réseau Mesh puissant comme le XE75, **ne branche aucune ence
