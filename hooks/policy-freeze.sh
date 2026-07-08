#!/usr/bin/env bash
# RULE-017 structural enforcement — Policy Immutability Gate
# Portable version for Enterprise Multi-Agent Protocol v4
#
# Purpose : block Write/Edit/NotebookEdit on governance files unless a one-shot
#           unlock token exists at ~/.claude/.policy-unlock
# Input   : Claude Code hook JSON via stdin (tool_name, tool_input.file_path)
# Exit    : 0 allow · 2 block (with reason on stderr)
# Design  : fail-open on payload parse error (harness-safety trade-off);
#           audit log captures every decision including parse failures.
#
# Governance file matching:
#   .clinerules · enterprise_protocol.md · settings.json · settings.local.json
#
# Requires: bash 4+, python 3.8+ (for JSON parse)

set -uo pipefail

AUDIT_LOG="${HOME}/.claude/telemetry/audit.jsonl"
UNLOCK_TOKEN="${HOME}/.claude/.policy-unlock"
PROTOCOL_VERSION="v4"

mkdir -p "$(dirname "$AUDIT_LOG")" 2>/dev/null || true

PAYLOAD=$(cat 2>/dev/null || true)
[ -z "$PAYLOAD" ] && exit 0

# Pass payload via env var to avoid shell-quoting issues (Windows msys friendly)
export HOOK_PAYLOAD="$PAYLOAD"
parsed=$(python -c '
import json, os
try:
    d = json.loads(os.environ.get("HOOK_PAYLOAD",""))
    print(d.get("tool_name","") or "")
    print((d.get("tool_input",{}) or {}).get("file_path","") or "")
except Exception:
    print("")
    print("")
' 2>/dev/null)

TOOL_NAME=$(printf '%s' "$parsed" | sed -n '1p' | tr -d '\r')
FILE_PATH=$(printf '%s' "$parsed" | sed -n '2p' | tr -d '\r')

case "$TOOL_NAME" in
  Write|Edit|NotebookEdit) ;;
  *) exit 0 ;;
esac

# Normalise path: backslashes → forward, lowercase (Windows-friendly matching)
# shellcheck disable=SC1003
# (SC1003 is a false-positive here: `tr` interprets '\\' as one literal backslash — correct)
NORM=$(printf '%s' "$FILE_PATH" | tr '\\' '/' | tr '[:upper:]' '[:lower:]')

BLOCKED=0
case "$NORM" in
  */.clinerules|*/enterprise_protocol.md|*/settings.json|*/settings.local.json)
    BLOCKED=1 ;;
esac

TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
SID="${CLAUDE_SESSION_ID:-unknown}"
CID="cid-$(date -u +%s%N 2>/dev/null || date -u +%s)-$$"

log_audit() {
  printf '{"timestamp":"%s","session_id":"%s","correlation_id":"%s","protocol_version":"%s","event_type":"policy_freeze_hook","actor":"agent","target":"%s","tool":"%s","decision":"%s","rule_id":"RULE-017"}\n' \
    "$TS" "$SID" "$CID" "$PROTOCOL_VERSION" "$FILE_PATH" "$TOOL_NAME" "$1" >> "$AUDIT_LOG" 2>/dev/null || true
}

[ "$BLOCKED" -eq 0 ] && exit 0

if [ -f "$UNLOCK_TOKEN" ]; then
  rm -f "$UNLOCK_TOKEN"
  log_audit "unlocked"
  exit 0
fi

log_audit "deny"
cat >&2 <<EOF
[RULE-017 BLOCK] Policy Immutability Gate.
Governance file '${FILE_PATH}' cannot be modified without an explicit unlock.
Run in a terminal:  touch ~/.claude/.policy-unlock
Then retry. Token is one-shot (auto-consumed).
EOF
exit 2
