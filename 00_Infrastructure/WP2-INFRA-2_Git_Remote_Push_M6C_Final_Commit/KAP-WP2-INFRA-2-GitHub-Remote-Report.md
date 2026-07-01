# KAP-WP2-INFRA-2-GitHub-Remote-Report

| remote_configured | remote_url | repo_exists | action_taken | blocker |
|---|---|---|---|---|
| NO | https://github.com/yannick-jolliet/KAP.git | UNKNOWN | None — auth failed | GitHub PAT expired / connector not active |

**Blocker detail:**
- `gh auth status`: not logged in
- PAT from memory (`GHgolfkit1+`): HTTP 401 Bad credentials — token expired or incorrect
- GitHub MCP connector: enabled in config but MCP server not running
- Resolution: Provide a valid GitHub PAT via Manus Secrets, or enable GitHub connector in Manus UI

**To unblock:**
```bash
git remote add origin https://github.com/yannick-jolliet/KAP.git
git push -u origin main
```
Requires a valid PAT with `repo` scope for `yannick-jolliet`.
