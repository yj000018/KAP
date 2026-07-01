---
name: yos-mac-bridge
description: "Full autonomous control of a macOS machine from Manus sandbox. SSH tunnel via bore, screen capture, mouse/keyboard control via cliclick, native app automation via osascript/swift. Use when user asks to control their Mac, click on screen, see what is displayed, automate a native app, debug a GUI issue, interact with any macOS app without CLI, replicate config across machines, or do remote support. Enables the perception-action loop: see screen, act, verify, correct, with zero user relay."
---

# yOS Mac Bridge

Enables Manus to see, click, type, and execute on a remote macOS machine — closing the perception-action loop without user relay.

## Architecture

```
Manus (AWS sandbox)
    ↓ SSH -p 22847
bore.pub:22847  ←→  bore (LaunchAgent, auto-restart)
    ↓
Mac Air (socat relay :2222 → sshd :22)
    ↓ osascript / swift / cliclick / screencapture
macOS GUI + native apps
```

**Key components on Mac:**
- `~/Library/LaunchAgents/com.yos.bore-tunnel.plist` — bore auto-restart at boot
- `~/Library/LaunchAgents/com.yos.socat-relay.plist` — socat relay port 2222→22
- `/opt/homebrew/bin/cliclick` — mouse/keyboard control (Accessibility enabled)
- `/opt/homebrew/bin/bore` — tunnel binary

## SSH Connection

```bash
# From Manus sandbox — always use this exact command:
ssh -i /home/ubuntu/.ssh/manus_mac \
  -o StrictHostKeyChecking=no \
  -o BatchMode=yes \
  -p 22847 yannickjolliet@bore.pub \
  "<command>"
```

**Config alias** (`~/.ssh/config` on Manus sandbox):
```
Host yos-mac-air
  HostName bore.pub
  Port 22847
  User yannickjolliet
  IdentityFile /home/ubuntu/.ssh/manus_mac
  StrictHostKeyChecking no
  BatchMode yes
```

**Test connection:**
```bash
ssh yos-mac-air "hostname; uptime"
```

## Perception — See the Screen

```bash
# Capture screen on Mac (via Desktop Client session):
/usr/sbin/screencapture -x /tmp/screen.png

# Retrieve to Manus sandbox:
ssh yos-mac-air "cat /tmp/screen.png" > /tmp/screen.png

# Then view with file tool to identify coordinates/state
```

**Always capture before acting on GUI.** Never assume what's on screen — versions differ, state changes.

## Action — Click, Type, Navigate

```bash
# Move mouse
/opt/homebrew/bin/cliclick m:X,Y

# Left click
/opt/homebrew/bin/cliclick c:X,Y

# Double click
/opt/homebrew/bin/cliclick dc:X,Y

# Type text
/opt/homebrew/bin/cliclick t:"text to type"

# Key press (Return, Tab, Escape, etc.)
/opt/homebrew/bin/cliclick kp:return
/opt/homebrew/bin/cliclick kp:tab
/opt/homebrew/bin/cliclick kp:escape
```

**Coordinates:** Retina display = 2x logical pixels. screencapture returns full resolution. Divide coordinates by 2 for cliclick if needed, or test empirically.

## Native App Automation — osascript

```bash
# Launch app
osascript -e 'tell application "Notes" to activate'

# Create a Note
osascript << 'EOF'
tell application "Notes"
    make new note at folder "Notes" with properties {name:"Title", body:"Content"}
end tell
EOF

# Open URL in browser
osascript -e 'open location "https://example.com"'

# Hide all apps (show desktop)
osascript -e 'tell application "System Events" to keystroke "h" using {command down, option down}'
```

## System Settings / Wallpaper — swift (macOS Sequoia)

```bash
# Change wallpaper — ONLY method that works on Sequoia:
swift -e '
import AppKit
let url = URL(fileURLWithPath: "/path/to/image.png")
for screen in NSScreen.screens {
    try? NSWorkspace.shared.setDesktopImageURL(url, for: screen, options: [:])
}
'
```

> ⚠️ `osascript set picture of desktop` and sqlite3 `desktoppicture.db` edits do NOT work on macOS Sequoia. Use swift only.

## File Transfer: Manus ↔ Mac

```bash
# Manus → Mac (pipe via SSH):
cat /tmp/local_file.png | ssh yos-mac-air "cat > /tmp/remote_file.png"

# Mac → Manus (pipe via SSH):
ssh yos-mac-air "cat /tmp/remote_file.png" > /tmp/local_file.png

# Via FUSE mount (Desktop Client) — direct read/write:
# /mnt/desktop/Users/yannickjolliet/Desktop/  (Desktop folder only)
```

## The Perception-Action Loop

**Before Mac Bridge:** Manus gives instructions → user executes → user describes result → Manus responds. Multiple round-trips, errors from version mismatches, missing UI elements.

**With Mac Bridge:** Manus sees screen → acts → captures result → verifies → corrects. Zero user relay.

**Core workflow pattern:**
```
1. screencapture → file view → identify state + target coordinates
2. cliclick / osascript / swift → act
3. screencapture → verify result
4. Repeat until done
```

**When this loop is essential (vs plain CLI):**

| Scenario | Why loop matters |
|---|---|
| App wizard/GUI setup | No CLI equivalent; must navigate dialogs |
| "Click here" but button missing | See actual screen before acting, not assumed state |
| App freeze/hang | Diagnose visual state, force-quit, relaunch |
| Form filling in native apps | Accounting, CRM, admin panels with no API |
| Version-dependent UI | See what's actually rendered in this version |
| Accessibility/Privacy prompts | Dialogs that block automation until dismissed |

## System Diagnostic

Quick health check:
```bash
# CPU/Memory top processes
ps aux | sort -rk3 | head -10

# Swap usage
sysctl vm.swapusage

# Disk usage
df -h /System/Volumes/Data

# Load average
uptime
```

**Red flags:**
- Swap > 80% → memory pressure, Mac will slow down
- Load average > number of CPU cores → sustained overload
- Any process > 50% CPU sustained → investigate

## Reinstallation Guide

If the tunnel breaks:

### Step 1 — Check bore status on Mac
```bash
# Via Desktop Client session:
ps aux | grep bore | grep -v grep
cat ~/.yos/logs/bore-tunnel.log | tail -20
```

### Step 2 — Restart LaunchAgents
```bash
launchctl unload ~/Library/LaunchAgents/com.yos.bore-tunnel.plist
launchctl unload ~/Library/LaunchAgents/com.yos.socat-relay.plist
sleep 5
launchctl load ~/Library/LaunchAgents/com.yos.bore-tunnel.plist
launchctl load ~/Library/LaunchAgents/com.yos.socat-relay.plist
```

### Step 3 — Verify port
```bash
cat ~/.yos/logs/bore-tunnel.log | grep "listening at"
# Expected: listening at bore.pub:22847
```

### Step 4 — Test from Manus sandbox
```bash
ssh yos-mac-air "echo OK"
```

### If port changed (bore assigned a new one):
1. Update `Port` in `~/.ssh/config` on Manus sandbox
2. Update `--port XXXXX` in the bore LaunchAgent plist on Mac

See `references/launchagents.md` for full plist content to recreate from scratch.

## Tailscale Mesh (Future — when N100 is online)

When N100 (anandaz-ubuntu, 100.87.123.30) is running, bore becomes obsolete:
```bash
# On N100 (one-time setup):
sudo tailscale up --advertise-routes=192.168.1.0/24 --accept-routes

# Then Manus → N100 → all devices via Tailscale stable IPs
```

## High-Value Use Cases for the Perception-Action Loop

These are the scenarios where the loop delivers maximum value — impossible or very painful without it:

### 1. Debug & Support (Remote Assistance)
> "Mon app X plante, aide-moi."

Manus sees the actual error dialog, the exact version, the real state — not a description. Acts directly: dismisses dialogs, reads crash logs, adjusts settings, restarts services. No back-and-forth.

### 2. Complex Config & Parameters
> "Configure le démarrage automatique de cet outil, active ce flag dans les préférences avancées."

Many apps have settings buried 4 levels deep in GUI with no `defaults write` equivalent. Manus navigates the UI, finds the exact toggle, sets it, verifies.

### 3. Config Replication Across Machines
> "Copie mes paramètres de l'app X sur le Mac de Robi."

Workflow:
1. Capture settings screen on source Mac (Mac Air)
2. Read config files (`~/Library/Preferences/*.plist`, `~/.config/`)
3. Connect to target Mac (Mac Robi, via Tailscale when online)
4. Apply identical config — via plist copy or GUI navigation
5. Verify visually on target

### 4. Remote Machine Administration
> "Sur le N100, installe Docker, configure le démarrage auto, et ouvre le port 8080."

For machines with a frontend (Proxmox, TrueNAS, Synology DSM, pfSense):
- SSH for CLI operations
- Browser automation (via Playwright MCP) for web admin panels
- screencapture + cliclick for any native GUI

### 5. App Installation & Setup Wizard
> "Installe et configure Tailscale sur le Mac de Robi avec mon compte."

Wizards, license dialogs, account login screens — all require GUI interaction. Manus handles the full flow: download → install → configure → verify → done.

### 6. Monitoring & Alerting
> "Surveille mon Mac, préviens-moi si ça rame ou si une app consomme trop."

Scheduled task: every N minutes, capture CPU/RAM/swap, screenshot if anomaly detected, send alert via Slack/Notion.

---

## Device Inventory

| Device | Tailscale IP | OS | SSH User | Status |
|---|---|---|---|---|
| macbook-air-yannick | 100.67.176.122 | macOS Sequoia | yannickjolliet | ✅ Active |
| anandaz-ubuntu (N100) | 100.87.123.30 | Ubuntu | ubuntu | ⚠️ Offline |
| iphone-yan | 100.115.151.92 | iOS | — | ✅ Tailscale |
| nas-synology | 100.71.221.108 | Linux | — | ⚠️ Offline |
