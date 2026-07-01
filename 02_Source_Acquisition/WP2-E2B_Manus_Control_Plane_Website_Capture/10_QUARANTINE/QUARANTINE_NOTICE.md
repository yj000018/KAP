# KAP WP2-E2B — Quarantine Notice

**Date:** 2026-07-01
**Sprint:** WP2-E2B — Credential Remediation

## Files Quarantined

| File | Reason | Redacted Copy |
|------|--------|---------------|
| collect_session.py (WP2-E2) | Contains hardcoded Manus JWT fallback token | collect_session.py.REDACTED |
| run_pipeline.py (WP2-E2) | Contains hardcoded Manus JWT fallback token | run_pipeline.py.REDACTED |
| collect_session.py (WP2-E1/manus_skills) | Contains hardcoded Manus JWT fallback token | collect_session.py.REDACTED |

## Action Required

1. Rotate the Manus JWT token (expires ~2026-08-07 per earlier analysis)
2. Replace hardcoded fallback with env var: `MANUS_JWT_TOKEN`
3. Update 1Password entry for Manus session token
4. Do NOT distribute the `.SENSITIVE` copies

## Status

- [x] Sensitive files identified
- [x] Redacted copies created (JWT replaced with `[REDACTED_JWT_TOKEN]`)
- [ ] Token rotation pending (user action required)
- [ ] 1Password update pending
