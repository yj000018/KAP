---
uid: AGFuvlbEKi82FbjOV2Ts4x
session_url: https://manus.im/app/AGFuvlbEKi82FbjOV2Ts4x
session_title: "Y-Downloads Shelf — macOS SwiftUI Menu-Bar App for Recent Downloads"
date: 2026-06-30
project: "Y-Downloads Shelf"
language: mixed
depth: substantial
length: short
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 12:48
referenced_sessions: []
referenced_artifacts: ["YDownloadsShelf.zip"]
referenced_urls: ["https://manus.im/app/AGFuvlbEKi82FbjOV2Ts4x"]
input_files: []
message_count: 5
---

# Y-Downloads Shelf — macOS SwiftUI Menu-Bar App for Recent Downloads

> **Session:** [AGFuvlbEKi82FbjOV2Ts4x](https://manus.im/app/AGFuvlbEKi82FbjOV2Ts4x) | **Date:** 2026-06-30 | **Project:** Y-Downloads Shelf | **Language:** mixed

## 📋 SESSION CARD

### 🧭 Executive Summary
Yannick requested a fully functional macOS SwiftUI menu-bar app called "Y-Downloads Shelf" to reduce friction when transferring recent downloads across Finder, browsers, and AI tools. Manus delivered a complete, compile-ready Xcode project of 902 lines across 11 Swift source files in approximately 4 minutes. The app includes FSEvents file watching, drag & drop, global hotkey, Quick Look, and a floating NSPanel UI.

---

### 🎯 Context & Intent
Daily workflow friction: moving recently downloaded files between Finder, ChatGPT, Manus, browsers, and automation tools requires too many steps. The goal was a persistent, lightweight shelf always at hand via menu bar or global hotkey (⌘⇧Space), showing the 15 most recent completed downloads with instant drag, copy, open, reveal, and preview actions — no heavy file manager, no context switching.

---

### ✅ What Was Done
1. Received detailed spec from user (monitoring, filtering, file row actions, architecture constraints)
2. Designed 11-file Xcode project architecture covering all specified behaviors
3. Implemented `DownloadsStore` with FSEvents watcher + 2s polling fallback and temp-file filtering (`.download`, `.crdownload`, `.part`, `.tmp`)
4. Built `FileRowView` with drag source, 4 hover action buttons, and full context menu
5. Implemented global hotkey via Carbon `RegisterEventHotKey` (⌘⇧Space)
6. Added `PreferencesManager` with UserDefaults persistence for maxFiles, ignored extensions, hotkey, and panel position
7. Packaged and delivered complete zip archive of the Xcode project

---

### 💡 Key Insights
- **FSEvents + polling hybrid**: Pure FSEvents can miss some download completions (browser writes are incremental); 2s polling fallback ensures reliability
- **Temp-file filter is critical**: Without filtering `.crdownload`/`.part` etc., the shelf would show incomplete files mid-download — noisier than useful
- **Carbon hotkey API**: SwiftUI has no native global hotkey mechanism; Carbon `RegisterEventHotKey` remains the pragmatic macOS choice despite being legacy
- **NSPanel over NSWindow**: Floating panel behavior (non-activating, always-on-top optional) fits the shelf UX better than a standard window
- **902 lines / 11 files**: Substantial but scoped — no external dependencies, pure Apple frameworks (SwiftUI, AppKit, FSEvents, Carbon)

---

### 📦 Outputs Produced
- **[script]** `YDownloadsShelf.zip` (Xcode project): Complete macOS SwiftUI app, 11 source files, 902 lines, compile-ready
  - `main.swift` — Entry point
  - `AppDelegate.swift` — Menu bar + NSPanel + hotkey setup
  - `PreferencesManager.swift` — UserDefaults persistence
  - `FileItem.swift` — File model
  - `DownloadsStore.swift` — FSEvents watcher + polling + temp filter
  - `ShelfView.swift` — Main panel UI (header, search, list, footer)
  - `FileRowView.swift` — Row with drag, info, 4 action buttons, context menu
  - `PreferencesView.swift` — Preferences sheet
  - `HotkeyManager.swift` — Global hotkey via Carbon

---

### ⚠️ Open Items & Blockers
- **[INCERTAIN]** App has not been compiled/tested — build errors may exist (Swift version compatibility, entitlements, sandbox restrictions)
- **[INCERTAIN]** macOS sandbox may block FSEvents on `~/Downloads` without explicit entitlement (`com.apple.security.files.downloads.read-write`) — needs Info.plist + entitlements file
- **[INCERTAIN]** Carbon `RegisterEventHotKey` may require Accessibility permissions or conflict with system hotkeys
- **[INCERTAIN]** Quick Look integration not confirmed in delivered code — listed in spec but implementation details unverified in summary
- No code signing / provisioning profile provided — required for distribution or notarization
- No unit tests included

---

### 🔁 Next Steps
1. **Compile** the project in Xcode and resolve any build errors (Swift 5.9+ target, macOS 13+ recommended)
2. **Add entitlements file** with `com.apple.security.files.downloads.read-write` and verify sandbox behavior
3. **Test FSEvents watcher** by downloading files via Chrome, Safari, and curl to validate temp-file filtering
4. **Test global hotkey** (⌘⇧Space) — check for conflicts with macOS system shortcuts or other apps
5. **Verify Quick Look** integration (`QLPreviewPanel`) works from the file row
6. **Add `.xcconfig` or `Info.plist`** entries if missing from the zip
7. Consider adding **auto-clear** behavior (e.g., remove files older than N days from shelf) as a preference

---

### 🔗 Links & References
- 🔗 session:`AGFuvlbEKi82FbjOV2Ts4x` — This session (Manus build)
- 🌐 https://manus.im/app/AGFuvlbEKi82FbjOV2Ts4x — Session URL
- 📁 `~/Downloads` — Monitored directory
- 📄 Apple FSEvents API — Framework used for directory watching
- 📄 Carbon `RegisterEventHotKey` — Legacy API used for global hotkey

---

### 🧠 Resume Hint
A complete but untested Xcode project for "Y-Downloads Shelf" was delivered as a zip; next agent should focus on compiling, fixing sandbox entitlements, and validating FSEvents + hotkey behavior on the target macOS version.

---

### 🏷️ Tags
`macos-app` `swiftui` `downloads-workflow` `menu-bar-tool` `file-management` `xcode`

---

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 5 messages — 2026-06-30

**[2026-06-30 21:24] USER:** Create a minimal macOS SwiftUI menu-bar/floating-panel app called “Y-Downloads Shelf”.

Goal:
Reduce friction when moving recently downloaded files between Finder, ChatGPT, Manus, browser, and automation tools.

Core behavior:
- Monitor ~/Downloads.
- Display the 15 most recent completed files.
- Ignore partial/download temp files: .download, .crdownload, .part, .tmp.
- Show file icon, filename, extension, size, modified time.
- Floating panel accessible via menu bar and global hotkey.
- Each file row supports:
  1. Drag file to another app.
  2. Copy file URL/path to clipboard.
  3. Open file.
  4. Reveal in Finder.
  5. Quick Look preview if possible.
- Keep UI extremely minimal and fast.

Architecture:
- SwiftUI app.
- NSPanel floating window, always-on-top optional.
- FileManager scann

**[2026-06-30 21:25] MANUS:** Sur ça. Je construis Y-Downloads Shelf — app SwiftUI macOS complète avec menu bar, floating panel, hotkey global, drag & drop, et file watcher. Je génère le projet Xcode complet avec tous les fichiers source.

**[2026-06-30 21:29] MANUS:** **Y-Downloads Shelf** — livré. 902 lignes Swift, 11 fichiers sources, projet Xcode prêt à compiler.

---

## Contenu du zip

| Fichier | Rôle |
|---|---|
| `main.swift` | Entry point, NSApp + AppDelegate |
| `AppDelegate.swift` | Menu bar, NSPanel floating, hotkey setup |
| `PreferencesManager.swift` | UserDefaults persistence (maxFiles, ignoredExt, hotkey, position) |
| `FileItem.swift` | Modèle fichier (icon, size, date, path) |
| `DownloadsStore.swift` | FSEvents watcher + polling 2s, filtre temp files |
| `ShelfView.swift` | Panel principal : header, search bar, file list, footer |
| `FileRowView.swift` | Row : drag icon, info, 4 boutons hover, context menu complet |
| `PreferencesView.swift` | Sheet préférences |
| `HotkeyManager.swift` | Carbon `RegisterEventHotKey` — ⌘⇧Space global 
