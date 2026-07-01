"""
Delete GitHub PATs via API using the token itself.
The /authorizations endpoint is deprecated but the delete via token page works.
We'll use the GitHub web interface via requests with session cookies.
"""
import subprocess
import time

# Token IDs to delete (all "Never used" ones)
tokens_to_delete = {
    "12.6.2026": 4692333118,
    "12.6.2006": 4692328427,
    "FULL PAT": 4632899129,
    "Manus-Orchestrator": 3992675076,
    "Y-OS-MANUS-FULL-2026": 3963771808,
    "yos-pipeline-2026-03": 3677275723,
    "yos-llm-pipeline deploy": 3677262719,
}

# Navigate to each token page and click delete
for name, token_id in tokens_to_delete.items():
    url = f"https://github.com/settings/tokens/{token_id}"
    print(f"Deleting: {name} (ID: {token_id})")
    print(f"  URL: {url}")
