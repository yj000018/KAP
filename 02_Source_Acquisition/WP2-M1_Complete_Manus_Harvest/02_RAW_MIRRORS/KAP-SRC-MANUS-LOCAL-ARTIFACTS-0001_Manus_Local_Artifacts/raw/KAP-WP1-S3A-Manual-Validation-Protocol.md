# KAP WP1-S3A — Manual Validation Protocol

## Context

Direct extension validation is blocked. The Manus sandbox browser is not logged into ChatGPT, and the "My Browser" connector is disabled. This protocol provides step-by-step instructions for Yannick to perform the validation sample export manually.

## Step 1: Identify Your Export Extension

Open Chrome and navigate to `chrome://extensions/`. Locate the ChatGPT export extension you use. Record:

| Field | What to record |
|-------|---------------|
| Extension name | Exact name as shown in Chrome |
| Version | Version number (e.g., 2.4.1) |
| Permissions | Click "Details" → note all permissions listed |
| Developer | Developer name or website |
| Source | Chrome Web Store URL |
| Local-only export | Does it export to local files only, or does it send data to a server? |

## Step 2: Export 3-4 Test Conversations

Export the following conversations as Markdown (`.md`) files:

### Conversation A — Short / Low-Risk
- **Criteria:** A short conversation (< 20 messages), no sensitive data, basic text only.
- **Purpose:** Baseline fidelity test.
- **Example:** A quick question about a tool, a definition, or a simple how-to.

### Conversation B — Medium / Formatted
- **Criteria:** A medium conversation (20-60 messages) containing at least:
  - One code block (any language)
  - One table
  - One Markdown heading structure
- **Purpose:** Formatting fidelity test (code, tables, structure).
- **Example:** A coding session, a comparison table, or a structured analysis.

### Conversation C — Long / Architecture
- **Criteria:** A long conversation (60+ messages) about yOS architecture, COSA, KRE, or similar.
- **Purpose:** Length handling, conversation threading, and content relevance test.
- **Example:** An architecture discussion, a design session, or a planning conversation.

### Conversation D — Optional / Attachments
- **Criteria:** A conversation where you uploaded a file (PDF, image, code file).
- **Purpose:** Test how the extension handles file references and attachments.
- **Only if safe** — skip if the file contains sensitive data.

## Step 3: Reproducibility Test

For **Conversation A only**, export it **twice** (two separate exports). Save both files with different names:
- `conv_a_export_1.md`
- `conv_a_export_2.md`

This tests whether the extension produces identical output on repeated exports.

## Step 4: Place Files in This Structure

```
/home/ubuntu/kap/wp1-s3a/validation_samples/
├── extension_info.json          ← See template below
├── conv_a_short/
│   ├── conv_a_export_1.md
│   └── conv_a_export_2.md       ← For reproducibility test
├── conv_b_medium/
│   └── conv_b.md
├── conv_c_long/
│   └── conv_c.md
└── conv_d_attachments/          ← Optional
    └── conv_d.md
```

### extension_info.json Template

```json
{
  "extension_name": "ChatGPT Exporter",
  "version": "2.4.1",
  "developer": "Example Dev",
  "chrome_web_store_url": "https://chromewebstore.google.com/detail/...",
  "permissions": [
    "Read and change your data on chatgpt.com",
    "Storage"
  ],
  "sends_data_externally": false,
  "export_format": "Markdown",
  "export_options_used": {
    "include_metadata": true,
    "include_timestamps": true,
    "include_code_blocks": true,
    "include_images": false
  },
  "notes": ""
}
```

## Step 5: Provide to Manus

Once the files are placed, tell Manus:
> "WP1-S3A validation samples ready in `/home/ubuntu/kap/wp1-s3a/validation_samples/`"

Or upload the folder as a ZIP. Manus will then:
1. Run `validate_chatgpt_export.py` on all samples.
2. Run `reproducibility_test.py` on the two Conversation A exports.
3. Generate the full validation report.
4. Issue a recommendation (APPROVED_PRIMARY / APPROVED_WITH_LIMITATIONS / NEEDS_MORE_TESTING / REJECTED).

## Step 6: Validation Checklist

| # | Check | Pass Criteria |
|---|-------|---------------|
| 1 | Extension identified | Name + version recorded |
| 2 | Permissions reviewed | No suspicious network permissions beyond chatgpt.com |
| 3 | Local-only export confirmed | Extension does NOT send data to third-party servers |
| 4 | Conv A exported (×2) | Two files, both non-empty |
| 5 | Conv B exported | Contains code blocks + tables in output |
| 6 | Conv C exported | File size > 10KB, conversation threading preserved |
| 7 | Conv D exported (optional) | File references noted (even if images not embedded) |
| 8 | Reproducibility | Two exports of Conv A produce identical checksums |
| 9 | No data leakage | Exported files contain only conversation content, no auth tokens or cookies |

## Security Notes

- Do NOT export conversations containing API keys, passwords, or financial data.
- Do NOT export conversations about other people's private information.
- Verify the extension does not phone home by checking its permissions and network activity.
- If in doubt about an extension's safety, check its source code on GitHub (if open-source) or its privacy policy.
