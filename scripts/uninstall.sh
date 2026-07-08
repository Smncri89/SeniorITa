#!/usr/bin/env bash
# uninstall.sh — restore backup made by install.sh
# Idempotent (RULE-011)
set -euo pipefail

TARGET="${HOME}"
BACKUP_ROOT="${TARGET}/.claude/backups"

# Find the most recent install-* backup
LATEST=$(ls -td "${BACKUP_ROOT}"/install-* 2>/dev/null | head -1 || true)
if [ -z "${LATEST}" ] || [ ! -d "${LATEST}" ]; then
  echo "[ERROR] No install backup found under ${BACKUP_ROOT}" >&2
  exit 1
fi
echo "[INFO] Restoring from: ${LATEST}"

restore() {
  local dst bak
  dst="$1"
  bak="${LATEST}/$(basename "$1").bak"
  if [ -f "${bak}" ]; then
    cp "${bak}" "${dst}"
    echo "[INFO] Restored: ${dst}"
  else
    echo "[INFO] No backup for ${dst}; removing installed copy if present"
    rm -f "${dst}"
  fi
}

restore "${TARGET}/.clinerules"
restore "${TARGET}/.claude/settings.json"

# Remove installed hooks (they belong to us)
rm -f "${TARGET}/.claude/hooks/policy-freeze.sh"
rm -f "${TARGET}/.claude/hooks/destructive-guard.sh"
rmdir "${TARGET}/.claude/hooks" 2>/dev/null || true
echo "[INFO] Removed installed hooks"

echo "[INFO] Uninstall complete. Audit log preserved at ${TARGET}/.claude/telemetry/audit.jsonl"
exit 0
