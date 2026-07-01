# KAP-WP2-INFRA-2-Recommended-Next-Step

**Immediate action required (user):**

Provide a valid GitHub PAT with `repo` scope for `yannick-jolliet`:
1. Go to https://github.com/settings/tokens/new
2. Select scope: `repo` (full control)
3. Generate token → copy
4. Send to Manus via Manus Secrets or directly in chat

**Then Manus will execute automatically:**
```bash
gh auth login --with-token <<< "<PAT>"
gh repo create yannick-jolliet/KAP --private --confirm
git remote add origin https://github.com/yannick-jolliet/KAP.git
git push -u origin main
```

**Next sprint after push:** WP2-NORM-1 — Corpus Normalization & Source Card Standardization
