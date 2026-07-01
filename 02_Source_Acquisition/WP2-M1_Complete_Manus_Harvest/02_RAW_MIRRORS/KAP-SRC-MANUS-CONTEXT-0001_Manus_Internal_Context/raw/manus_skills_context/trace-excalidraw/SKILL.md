---
name: trace-excalidraw
description: Generate a Y-OS Team Trace visualization in the consulting/sketch infographic style. Use when Yannick asks for a trace, execution diagram, team trace, mission trace, or says "/trace-excalidraw [MISSION_ID]". Produces PNG + SVG + Excalidraw file showing WHO worked, WHAT happened, WHAT value was created, and WITHOUT vs WITH Y-OS comparison. CEO-readable in 30 seconds.
---

# trace-excalidraw

Generates the canonical Y-OS Team Trace visualization from any mission's execution data.

## Visual Template (MANDATORY)

The output MUST match `templates/reference_template.png` exactly:

- White background, consulting infographic style (NOT dark mode, NOT cyberpunk)
- 9 numbered team member columns with colored headers + role icon circles
- Artifact handoffs row below columns (arrows with artifact name + tokens + latency)
- 3 synchronized views side by side (Architecture / Team / Value)
- Right-side Runtime Metrics panel (dark header, 7 KPIs)
- "DID Y-OS CREATE VALUE?" verdict box (green = YES, red = NO, amber = AMBER)
- WITHOUT Y-OS (red) vs WITH Y-OS (green) comparison at bottom
- PLUGINS NOT ACTIVATED panel (left side, red border)

## Invocation

Triggered by any of:
- `/trace-excalidraw [MISSION_ID]`
- "génère un trace excalidraw de [mission]"
- "trace du team/process/mission"
- "visualise la mission [X]"

## Workflow

### 1. Collect mission data

Gather from session context or ask if missing:
- Mission ID and date
- Team members used (role, worker name, provider, model)
- Tools used per member
- Inputs / outputs / artifacts per member
- Latency and cost per member
- Handoff artifact names + token counts
- Plugins that were NOT activated (with reason)
- Final verdict: YES / NO / AMBER

### 2. Populate the data dicts in render_trace.py

Edit `scripts/render_trace.py` — update these sections:
- `COLS` list: one dict per team member (num, title, icon, color, fields)
- `handoffs` list: artifact name + detail per transfer
- `metrics` list: right-panel KPIs
- `checkmarks` list: verdict bullet points
- Title, Mission ID, Date, Trace ID at top

### 3. Run the renderer

```bash
python /home/ubuntu/skills/trace-excalidraw/scripts/render_trace.py
```

The `base` variable in the script controls the output path. Edit it to point to the mission directory.

### 4. Verify output

View the PNG — confirm it matches `templates/reference_template.png` layout.
If zones are clipped or overlapping, adjust `FIG_H`, `COL_H`, or `CMP_H` constants.

### 5. Commit and deliver

```bash
cd /home/ubuntu/yreg && git add mission_[ID]/ && git commit -m "TRACE: [MISSION_ID] team trace" && git push origin master:y-os-doctrine
```

Deliver PNG + SVG as attachments. Mention `.excalidraw` file is importable at excalidraw.com.

## Color coding (fixed)

| Role | Color |
| :--- | :--- |
| Human (Yannick) | `#1a4fa0` Blue |
| Orchestrator | `#444444` Mid-grey |
| Architect | `#6b3fa0` Purple |
| Researcher / Builder / Writer | `#1a7a6e` Teal |
| Validator (Lakshmi) | `#c85a00` Orange |
| Memory / Git | `#444444` Mid-grey |
| Deliverable | `#b87800` Amber |
| Verdict YES | `#1a6e2e` Green |
| Plugins skipped | `#c0392b` Red |

## Key constants to adjust

| Constant | Purpose |
| :--- | :--- |
| `FIG_W`, `FIG_H` | Canvas size (default 38×26) |
| `COL_H` | Height of team member columns (default 7.8) |
| `N_COLS` | Number of team columns (default 9) |
| `CMP_H` | Height of WITHOUT/WITH comparison (default 3.2) |
| `VIEWS_H` | Height of 3 synchronized views (default 3.8) |

## CSO constraint

No new runtime modules. No dashboard. Static artifact generated on demand.
The renderer is a standalone Python script — no orchestration required.
