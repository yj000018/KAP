# KAP Core Engine Gates

**Sprint:** WP0-CORE-1
**Generated:** 2026-07-02

## 1. Gate 1 — Source Inventory Gate
| gate | pass_condition | fail_action |
|---|---|---|
| Source Inventory Gate | Source exists, family known, status assigned, owner/access/risk documented. | Block acquisition until inventory is complete. |

## 2. Gate 2 — Acquisition & Preservation Gate
| gate | pass_condition | fail_action |
|---|---|---|
| Acquisition & Preservation Gate | Raw captured (or limitation documented), source card created, manifest created, checksum created, no unexplained missing output. | Mark source as `BLOCKED` or `REOPEN_REQUIRED`. |

## 3. Gate 3 — Persistence Gate
| gate | pass_condition | fail_action |
|---|---|---|
| Persistence Gate | `file exists → in KAP → tracked → committed → pushed → visible on GitHub` | Block pipeline advancement. Trigger Git disaster recovery runbook. |

## 4. Gate 4 — Routing Gate
| gate | pass_condition | fail_action |
|---|---|---|
| Routing Gate | Item classified, domain assigned, sensitivity assigned, ambiguous high-value items flagged for review. | Route to `ARCHIVE_ONLY` and flag for manual Architect review. |

## 5. Gate 5 — Delta Gate
| gate | pass_condition | fail_action |
|---|---|---|
| Delta Gate | Previous state loaded, new state compared, new/changed/deleted detected, delta manifest created, source registry updated. | Revert to previous known state. Block downstream processing. |
