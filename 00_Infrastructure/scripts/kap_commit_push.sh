#!/bin/bash
# KAP Standard Sprint Commit & Push Script
# Usage: ./kap_commit_push.sh <sprint_folder_path> <sprint_id> "<commit_message>"
# Example: ./kap_commit_push.sh /home/ubuntu/KAP/02_Source_Acquisition/WP2-M7_Mem0 WP2-M7 "KAP: complete WP2-M7 Mem0 export"

set -e

SPRINT_FOLDER="${1}"
SPRINT_ID="${2}"
COMMIT_MSG="${3:-KAP: complete ${SPRINT_ID}}"
KAP_ROOT="/home/ubuntu/KAP"
PAT="<GITHUB_PAT_IN_MANUS_SECRETS>"
PROOF_FILE="${SPRINT_FOLDER}/GIT_PUSH_PROOF.md"

echo "=== KAP Sprint Commit & Push ==="
echo "Sprint: ${SPRINT_ID}"
echo "Folder: ${SPRINT_FOLDER}"
echo "Message: ${COMMIT_MSG}"

# Validate inputs
if [ -z "${SPRINT_FOLDER}" ] || [ -z "${SPRINT_ID}" ]; then
    echo "ERROR: Missing arguments. Usage: $0 <sprint_folder> <sprint_id> [commit_message]"
    exit 1
fi

if [ ! -d "${SPRINT_FOLDER}" ]; then
    echo "ERROR: Sprint folder does not exist: ${SPRINT_FOLDER}"
    exit 1
fi

cd "${KAP_ROOT}"

# Check remote
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "ERROR: No git remote configured. Run: git remote add origin https://yj000018:${PAT}@github.com/yj000018/KAP.git"
    exit 1
fi

# Ensure remote uses PAT
git remote set-url origin "https://yj000018:${PAT}@github.com/yj000018/KAP.git"

# Git status
echo ""
echo "--- Git Status ---"
git status --short "${SPRINT_FOLDER}" | head -20
CHANGES=$(git status --short "${SPRINT_FOLDER}" | wc -l)

if [ "${CHANGES}" -eq 0 ]; then
    echo "WARNING: No changes to commit in ${SPRINT_FOLDER}"
    COMMIT_HASH=$(git log -1 --format="%H")
    PUSH_STATUS="SKIPPED (no changes)"
else
    # Stage sprint folder
    git add "${SPRINT_FOLDER}"
    
    # Also stage any .github/workflows changes
    git add "${KAP_ROOT}/.github/" 2>/dev/null || true
    git add "${KAP_ROOT}/00_Infrastructure/scripts/" 2>/dev/null || true
    
    # Commit
    git commit -m "${COMMIT_MSG}"
    COMMIT_HASH=$(git log -1 --format="%H")
    
    # Push
    echo ""
    echo "--- Pushing to GitHub ---"
    if git push origin main; then
        PUSH_STATUS="SUCCESS"
        echo "✅ Push successful: https://github.com/yj000018/KAP/commit/${COMMIT_HASH:0:7}"
    else
        PUSH_STATUS="FAILED"
        echo "❌ Push failed"
        exit 1
    fi
fi

# Write proof file
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
cat > "${PROOF_FILE}" << PROOF
# KAP Git Push Proof

| field | value |
|---|---|
| sprint_id | ${SPRINT_ID} |
| sprint_folder | ${SPRINT_FOLDER} |
| commit_hash | \`${COMMIT_HASH}\` |
| commit_message | ${COMMIT_MSG} |
| push_status | ${PUSH_STATUS} |
| repo_url | https://github.com/yj000018/KAP |
| timestamp | ${TIMESTAMP} |
PROOF

echo ""
echo "=== PROOF ==="
cat "${PROOF_FILE}"
