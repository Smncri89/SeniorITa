#!/usr/bin/env bash
# audit-rotate.sh — daily rotation of ~/.claude/telemetry/audit.jsonl
# Idempotent (RULE-011): safe to run multiple times per day
# Suggested cron:   0 0 * * *  bash scripts/audit-rotate.sh
# Suggested Task Scheduler (Windows): daily at 00:00 with git-bash

set -euo pipefail

TELEMETRY="${HOME}/.claude/telemetry"
AUDIT="${TELEMETRY}/audit.jsonl"
ARCHIVE_ROOT="${TELEMETRY}/archive"
TODAY=$(date -u +%Y-%m-%d)
ARCHIVE_DIR="${ARCHIVE_ROOT}/${TODAY}"

[ -f "${AUDIT}" ] || { echo "[INFO] No audit log yet at ${AUDIT}; nothing to rotate"; exit 0; }

# If file is empty, skip
if [ ! -s "${AUDIT}" ]; then
  echo "[INFO] Audit log is empty; skipping rotation"
  exit 0
fi

mkdir -p "${ARCHIVE_DIR}"

# Only rotate if the file has content and archived version doesn't already exist
ARCHIVED="${ARCHIVE_DIR}/audit.jsonl.gz"
if [ -f "${ARCHIVED}" ]; then
  # Append today's events to existing archive (idempotent append-only)
  gzip -c "${AUDIT}" >> "${ARCHIVED}"
  echo "[INFO] Appended to existing archive: ${ARCHIVED}"
else
  gzip -c "${AUDIT}" > "${ARCHIVED}"
  echo "[INFO] Archived to: ${ARCHIVED}"
fi

# Truncate live file after successful archive
: > "${AUDIT}"

# Log the rotation event to the freshly-truncated live file
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
printf '{"timestamp":"%s","session_id":"rotation","correlation_id":"cid-rotate-%s","protocol_version":"v4","event_type":"audit_rotation","actor":"scheduler","target":"%s","decision":"rotated","summary":"rotation archive: %s"}\n' \
  "${TS}" "$(date -u +%s)" "${AUDIT}" "${ARCHIVED}" >> "${AUDIT}"

echo "[INFO] Rotation complete"
exit 0
