---
name: yos-helpdesk
version: 1.0.0
description: "Autonomous IT support and debug agent for yOS devices. Use when Yannick reports a problem (app crash, slowdown, process hanging, config broken), or when autonomous investigation is needed without user relay. Activates the Mac Bridge perception-action loop to diagnose, fix, and verify — without asking the user to take screenshots or run commands."
triggers:
  - "ça plante"
  - "aide-moi"
  - "mon mac rame"
  - "app freeze"
  - "bug"
  - "helpdesk"
  - "yos-helpdesk"
  - "investigate"
  - "debug"
requires:
  - yos-mac-bridge
---

# yOS Helpdesk

Autonomous IT support agent. Diagnoses, fixes, and verifies issues on yOS devices without user relay.

## When to Activate

Read this skill when the user reports:
- An app that crashes, freezes, or behaves unexpectedly
- Mac slowdown, overheating, or high CPU/RAM
- A process that won't stop
- A config that broke after an update
- Any "help me fix this" request on a device

**Do NOT ask the user to take screenshots or run commands.** Use the Mac Bridge to investigate directly.

## Investigation Protocol

### Phase 1 — Capture Current State (always first)

```bash
# 1. Screenshot — see what's on screen
ssh yos-mac-air "screencapture -x /tmp/s.png && sips -s format jpeg -s formatOptions 25 /tmp/s.png --out /tmp/s.jpg 2>/dev/null && cat /tmp/s.jpg" > /tmp/screen.jpg
# Then: file view /tmp/screen.jpg

# 2. System health snapshot
ssh yos-mac-air "
echo '=== LOAD ==='
uptime
echo '=== SWAP ==='
sysctl vm.swapusage
echo '=== TOP CPU ==='
ps aux | sort -rk3 | head -8
echo '=== TOP RAM ==='
ps aux | sort -rk4 | head -8
echo '=== DISK ==='
df -h /System/Volumes/Data
"
```

### Phase 2 — Targeted Diagnosis

```bash
# Find a specific process
ssh yos-mac-air "ps aux | grep -i 'AppName' | grep -v grep"

# Check if app is responding
ssh yos-mac-air "osascript -e 'tell application \"AppName\" to running'"

# Recent system logs (last 5 min)
ssh yos-mac-air "log show --last 5m --predicate 'eventMessage contains \"error\"' 2>/dev/null | tail -20"

# Crash logs
ssh yos-mac-air "ls -lt ~/Library/Logs/DiagnosticReports/ | head -5"
ssh yos-mac-air "cat ~/Library/Logs/DiagnosticReports/AppName_*.crash 2>/dev/null | head -50"
```

### Phase 3 — Fix

```bash
# Kill a hanging process (graceful then force)
ssh yos-mac-air "pkill -TERM 'AppName' || pkill -KILL 'AppName'"

# Kill by PID
ssh yos-mac-air "kill -9 PID"

# Restart an app
ssh yos-mac-air "osascript -e 'quit app \"AppName\"'; sleep 2; open -a 'AppName'"

# Free memory cache (purge — requires sudo)
ssh yos-mac-air "sudo purge"

# Remove a login item (startup app)
ssh yos-mac-air "osascript -e 'tell application \"System Events\" to delete (login items whose name is \"AppName\")'"

# List all login items
ssh yos-mac-air "osascript -e 'tell application \"System Events\" to get the name of every login item'"
```

### Phase 4 — Verify

```bash
# Screenshot after fix — confirm visual state
ssh yos-mac-air "screencapture -x /tmp/s.png && sips -s format jpeg -s formatOptions 25 /tmp/s.png --out /tmp/s.jpg 2>/dev/null && cat /tmp/s.jpg" > /tmp/screen_after.jpg

# Confirm process is gone
ssh yos-mac-air "ps aux | grep -i 'AppName' | grep -v grep"

# Confirm system is healthier
ssh yos-mac-air "uptime && sysctl vm.swapusage"
```

## Common Scenarios

### Mac is slow / high CPU

```bash
ssh yos-mac-air "
echo '=== TOP 5 CPU ==='
ps aux | sort -rk3 | head -5
echo '=== SWAP ==='
sysctl vm.swapusage
echo '=== LOAD ==='
uptime
"
# Identify offender → kill or restart
```

### App won't quit

```bash
ssh yos-mac-air "osascript -e 'tell application \"AppName\" to quit'"
sleep 3
ssh yos-mac-air "pkill -KILL 'AppName'"
```

### Remove all startup/login items (audit)

```bash
ssh yos-mac-air "osascript << 'EOF'
tell application \"System Events\"
    set loginItems to get the name of every login item
    return loginItems
end tell
EOF"
# Then selectively remove:
ssh yos-mac-air "osascript -e 'tell application \"System Events\" to delete (login items whose name is \"UnwantedApp\")'"
```

### App crashes on launch — read crash log

```bash
ssh yos-mac-air "ls -lt ~/Library/Logs/DiagnosticReports/ | head -3"
ssh yos-mac-air "cat ~/Library/Logs/DiagnosticReports/LATEST.crash | head -80"
```

### Background agents audit (find hidden processes)

```bash
ssh yos-mac-air "
echo '=== LAUNCH AGENTS (user) ==='
ls ~/Library/LaunchAgents/
echo '=== LAUNCH DAEMONS (system) ==='
ls /Library/LaunchDaemons/ 2>/dev/null
echo '=== RUNNING AGENTS ==='
launchctl list | grep -v com.apple | head -20
"
```

## Routing Rules

| Situation | Tool |
|---|---|
| App with web interface | Browser (Playwright or browser tool) |
| Electron app (Manus, VS Code, Notion) | Browser on web URL |
| Native macOS app / system issue | Mac Bridge (this skill) |
| File operations only | Desktop Client FUSE mount |
| Scheduled/unattended fix | Mac Bridge via LaunchAgent or cron |

## Device Registry (yOS Mesh)

| Device | Access | Tailscale IP |
|---|---|---|
| Mac Air (primary) | `ssh yos-mac-air` via bore.pub:22847 | 100.67.176.122 |
| N100 / anandaz-ubuntu | Offline — via Tailscale when online | 100.87.123.30 |
| iPhone | Tailscale app | 100.115.151.92 |
| NAS Synology | Tailscale (offline) | 100.71.221.108 |

**When N100 is online:** `ssh ubuntu@100.87.123.30` from Mac Air (jump host) → then SSH to any device via Tailscale.

## Performance Notes

- **1 SSH call = ~1.5-2s latency** — batch all commands into a single SSH session
- **Screenshot cycle = 3s** (optimized: capture + compress + transfer in 1 call)
- **Avoid multiple SSH round-trips** — chain commands with `&&` or use heredoc
- JPEG 25% quality is sufficient for debug; use 50+ only for pixel-precise coordinate work
