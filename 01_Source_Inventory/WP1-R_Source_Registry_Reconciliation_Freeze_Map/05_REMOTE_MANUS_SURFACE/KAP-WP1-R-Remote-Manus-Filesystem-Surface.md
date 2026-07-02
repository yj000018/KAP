# KAP Remote Manus Filesystem Surface

**Sprint:** WP1-R
**Generated:** 2026-07-02

This document explicitly classifies the coverage of the remote Manus sandbox filesystem.

| surface | known_path_or_description | current_evidence | classification | wp3_blocking | next_action |
|---|---|---|---|---|---|
| `/home/ubuntu/KAP/` | KAP repository | Git controlled | COVERED_ENOUGH_FOR_WP3 | NO | None |
| `/home/ubuntu/skills/` | Manus skills directory | 59/59 captured in WP2-E1 | COVERED_ENOUGH_FOR_WP3 | NO | None |
| `/home/ubuntu/Downloads/` | Downloads directory | Temporary files | DEFERRED_NON_BLOCKING | NO | None |
| local scripts used by KAP | Scripts in KAP or skills | Covered by KAP/skills | COVERED_ENOUGH_FOR_WP3 | NO | None |
| deployed website source folders | Various project folders | Captured in WP2-E1 | COVERED_ENOUGH_FOR_WP3 | NO | None |
| generated artifacts outside KAP | Unknown | No evidence of critical missed artifacts | DEFERRED_NON_BLOCKING | NO | None |
| browser/shell history | .bash_history, browser profiles | Noise | EXCLUDED | NO | None |
| caches/temp files | /tmp, ~/.cache | Noise | EXCLUDED | NO | None |
| token/secret stores | ~/.manus/config, env vars | Restricted | EXCLUDED | NO | None |

**Conclusion:** The remote Manus filesystem is **COVERED_ENOUGH_FOR_WP3**. No deep harvest required.
