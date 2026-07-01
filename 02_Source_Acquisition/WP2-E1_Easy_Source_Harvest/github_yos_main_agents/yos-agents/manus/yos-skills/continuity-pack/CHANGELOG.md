# Continuity Pack Skill — Changelog

---

## v0.1 — 2026-06-29 (Hardening Pass)

**Trigger:** Post-v0.0 hardening. Remove v3 confusion from active path.

### Changes
- Validated CP Core v0 with "CP de cette session" test — behavior confirmed correct.
- Confirmed current-session-only behavior (no Mem0, no CSE, no external memory by default).
- Moved all v3 artifacts (`cp_boundary.md`, `validate_cp.py`, `canonical_cp.md`) to `archive/v3-deprecated/`. No active reference to them.
- Removed empty `references/`, `scripts/`, `templates/` directories.
- Clarified negative receiver instructions: replaced ambiguous "Re-read v3 files" wording with explicit "Do not rely on v3 files unless explicitly asked."
- Preserved strict CSE boundary.
- SKILL.md updated to v0.1.

### Active File Structure
```
continuity-pack/
├── SKILL.md          ← CP Core v0.1 (active)
├── CHANGELOG.md      ← this file
└── archive/
    └── v3-deprecated/
        ├── cp_boundary.md
        ├── validate_cp.py
        └── canonical_cp.md
```

---

## v0.0 — 2026-06-29 (Reset to Minimal CP Core)

**Trigger:** v3 was over-complex. Reset to a single-function, reliable primitive.

### Breaking Changes
- Replaced v3 SKILL.md (3-function menu: Generate / Receive / QC) with minimal v0 spec authored by Yannick.
- CP Core = one function only: **Generate CP**.
- Receive-only handled inside the generated CP itself (Receiver Instruction section), not as a separate active function.
- QC removed as active user-facing function.
- External memory never used unless explicitly requested.
- Quality gate reduced from 10 checks to 7.
- Required CP sections reduced from 12 to 11.
- No validation script in active path.

---

## v3.0 — 2026-06-29 (Archived)

See `archive/v3-deprecated/` for all v3 artifacts.

**Summary:** 3-function menu (Generate / Receive / QC), 10-check QC gate, 12-section template, validation script, source layering, staleness fields, target adaptation. Over-complex for field use.

---

## v2.1 — 2026-06-29 (Archived)

Intent Lock, Source Layering, Freshness/Staleness fields, 9-mode menu, CSE boundary. First version with mandatory QC gate.

---

## v2.0 — 2026-06-29 (Archived)

First implementation. 10 modes, canonical template, validator script. No Intent Lock, no Source Layering.
