# LaunchAgent Plists — yOS Mac Bridge

Full plist content to recreate from scratch if lost.

## com.yos.bore-tunnel.plist

Path: `~/Library/LaunchAgents/com.yos.bore-tunnel.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.yos.bore-tunnel</string>
    <key>ProgramArguments</key>
    <array>
        <string>/opt/homebrew/bin/bore</string>
        <string>local</string>
        <string>2222</string>
        <string>--to</string>
        <string>bore.pub</string>
        <string>--port</string>
        <string>22847</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/Users/yannickjolliet/.yos/logs/bore-tunnel.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/yannickjolliet/.yos/logs/bore-tunnel.log</string>
</dict>
</plist>
```

## com.yos.socat-relay.plist

Path: `~/Library/LaunchAgents/com.yos.socat-relay.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.yos.socat-relay</string>
    <key>ProgramArguments</key>
    <array>
        <string>/opt/homebrew/bin/socat</string>
        <string>TCP-LISTEN:2222,fork,reuseaddr,bind=0.0.0.0</string>
        <string>TCP:127.0.0.1:22</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/Users/yannickjolliet/.yos/logs/socat-relay.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/yannickjolliet/.yos/logs/socat-relay.log</string>
</dict>
</plist>
```

## Install Commands

```bash
mkdir -p ~/.yos/logs
# Copy plists to LaunchAgents
cp com.yos.bore-tunnel.plist ~/Library/LaunchAgents/
cp com.yos.socat-relay.plist ~/Library/LaunchAgents/
# Load
launchctl load ~/Library/LaunchAgents/com.yos.bore-tunnel.plist
launchctl load ~/Library/LaunchAgents/com.yos.socat-relay.plist
```

## SSH Key on Manus Sandbox

Private key: `/home/ubuntu/.ssh/manus_mac`
Public key deployed to: `/Users/yannickjolliet/.ssh/authorized_keys` on Mac

To regenerate:
```bash
ssh-keygen -t ed25519 -f /home/ubuntu/.ssh/manus_mac -N "" -C "manus-yos-bridge"
# Then copy public key to Mac's authorized_keys
cat /home/ubuntu/.ssh/manus_mac.pub
# Paste into /Users/yannickjolliet/.ssh/authorized_keys on Mac
```
