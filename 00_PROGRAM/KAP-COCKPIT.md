# KAP COCKPIT

> Single operational view for KAP. Complexity stays behind this page.

**Updated:** 2026-07-15  
**Mode:** State reconciliation  
**Rule:** One active objective. One next action. Evidence before assumptions.

---

## 1. NOW

### Current phase

**Close WP1/WP2 state gaps and prepare the first controlled WP3 normalization pilot.**

### Active objective

**KAP STATE-RECONCILIATION-GATE**

Build one trustworthy state from Git evidence, source reports, MPM ledger and live connectors.

### Current blocker

Several registries describe sources as planned or partial even though later Git evidence shows substantial acquisition. The system lacks one reconciled source-of-truth state.

### One next action

**Reconcile each source against its strongest available evidence and update this cockpit.**

### Owner

**ChatGPT — Architect & Guardian, temporary direct operator**

---

## 2. PROGRAM PULSE

| Work package | Operational state | Confidence | Meaning |
|---|---|---:|---|
| WP1 — Inventory & architecture | Advanced | High | Core architecture, source model, gates and registries exist |
| WP2 — Acquisition | Advanced but not uniformly closed | Medium | Major corpora acquired; closure evidence differs by source |
| WP3 — Normalization | Ready for pilot | Medium | Gates allow it; no verified broad normalization run found |
| WP4 — Deduplication & evolutionary merge | Not operational at scale | High | Architecture exists; execution not demonstrated |
| WP5 — Synthesis & Current Best Knowledge | Not started broadly | High | No validated global synthesis corpus |
| WP6 — Canonization & chronology | Not started | High | Must wait for provenance, normalization and review |

**Overall program state:** `WP2 closure / WP3 pilot preparation`

---

## 3. SOURCE STATUS

Legend:

- `CLOSED` — denominator known and acquisition evidence sufficient
- `ADVANCED` — substantial acquisition exists, closure still needs proof
- `PENDING` — source identified but meaningful acquisition not complete
- `DEFERRED` — intentionally postponed

| Source | Acquisition state | Strongest verified evidence | Transformation state | Next gate / action |
|---|---|---|---|---|
| Manus human sessions | **CLOSED with caveat** | 363 sessions reported in Notion and KAP Git; 0 useful missing candidates identified | 194 factsheets reported; no corpus-wide claim extraction verified | Register 363 raw / 194 factsheets distinction; select WP3 pilot sample |
| Notion | **ADVANCED** | 431 pages, 14,356 blocks and 793 files reported extracted; wider workspace described as 1,300+ pages | Census and selective Y-OS relevance closure unclear | Reconcile extracted corpus against current Notion roots and census reports |
| GitHub | **ADVANCED** | 36 repositories inventoried; large WP2-E1 corpus persisted in KAP | Systematic fragment and claim extraction not verified | Produce repo coverage matrix and select high-priority pilot repos |
| Mem0 | **CLOSED as derivative** | 316 memories reported acquired | Must remain routing aid, not source of truth | Cross-reference only after primary-source normalization |
| Obsidian | **PENDING** | 9 vaults discovered; six-module pipeline tested on fake vault | Real multi-vault acquisition not proven | Run safe real-vault census when files are accessible |
| ChatGPT conversations | **PENDING** | Context packs and general memory exist; no complete `conversations.json` verified | No systematic corpus extraction | Obtain export or use selected high-value sessions first |
| ChatGPT internal memory | **DEFERRED** | Persistent context available but derivative and incomplete | Prompt extraction planned after taxonomy stabilization | Run structured topic extraction after WP3 pilot taxonomy |
| Other LLM histories | **DEFERRED** | No complete exports verified | Not started | Add only after core Y-OS sources are stable |
| Google Drive / personal sources | **DEFERRED** | Limited quarantine/fingerprint work reported | Outside immediate KAP closure | Activate under YOUniverse scope, not current critical path |

---

## 4. THE NUMBER THAT MATTERS

Different counts represent different layers. Never compare them as if they were the same thing.

```text
363 Manus sessions acquired
        ↓
194 factsheets produced
        ↓
fragment / claim corpus not yet verified
        ↓
Current Best Knowledge not yet produced broadly
        ↓
canon not yet produced
```

This distinction is mandatory in every future status report.

---

## 5. ACTIVE WORK — MAXIMUM ONE ITEM

| ID | Work | Status | Done when |
|---|---|---|---|
| KAP-SR-001 | Reconcile source coverage and execution evidence | **ACTIVE** | Every source has denominator, stage, confidence, evidence and one next action |

No second active item may be added until KAP-SR-001 is closed or explicitly paused.

---

## 6. QUEUED — NOT ACTIVE

1. **MPM Guardian Review Closure** — classify each open MPM as accepted, rejected, superseded or genuinely pending.
2. **WP3-N1 Normalization Pilot** — small representative sample only.
3. **Obsidian Real-Vault Census** — read-only, after accessible snapshot is available.
4. **ChatGPT Corpus Acquisition** — full export or curated priority sessions.
5. **Current Best Knowledge Pilot** — only after provenance and claims are validated.

---

## 7. AGENT ROUTING

| Work type | Default executor |
|---|---|
| Architecture, state reconciliation, review, synthesis decisions | ChatGPT |
| GitHub and Notion inspection, light extraction, registry maintenance | ChatGPT direct connectors |
| Filesystem scans, huge batch transforms, parallel workers, long scripts | Manus after quota renewal or local runner |
| Canon acceptance, strategic scope changes, irreversible choices | Yannick + ChatGPT Guardian |

### Manus credit rule

Do not spend Manus credits on simple GitHub or Notion browsing. Use Manus where batch scale, filesystem access or parallel execution creates real leverage.

---

## 8. SAFETY BOUNDARIES

Until State Reconciliation is accepted:

- no deletion;
- no blind merge into canonical repositories;
- no contradiction auto-resolution;
- no historical variant removal;
- no broad WP3 run;
- no new parallel architecture;
- all durable outputs go to Git;
- all claims retain provenance and confidence.

---

## 9. DECISIONS NEEDED FROM YANNICK

**None now.**

Yannick should only be interrupted for:

- a genuine strategic fork;
- an irreversible operation;
- a contradiction that cannot be resolved from evidence;
- access to a missing high-value source.

---

## 10. RECOVERY PROTOCOL

Whenever the program feels confusing:

1. Open this cockpit.
2. Read **NOW**.
3. Execute only **One next action**.
4. Update source evidence.
5. Move completed work out of **ACTIVE**.
6. Never reconstruct program state from chat memory alone.

---

## 11. EVIDENCE ANCHORS

Initial reconciliation is based on these durable anchors:

- `01_Source_Inventory/SOURCE-CATALOG.md`
- WP2-M8C Manus API / Notion / KAP crosswalk reports
- WP2-M6C Notion block extraction reports
- GitHub repository registry and WP2-E1 acquisition corpus
- Obsidian pipeline patch and harness reports
- Evolutionary Knowledge Merge registries
- `kap-control-plane/00_META/inter_llm_execution_ledger.json`

The next reconciliation pass must replace summary statements with exact file paths and commit hashes in a dedicated evidence matrix.

---

## 12. NEXT UPDATE

**Expected cockpit change:** source-by-source evidence matrix completed and stale registry entries identified.

**Next action remains:** `KAP-SR-001 — reconcile source coverage and execution evidence`.
