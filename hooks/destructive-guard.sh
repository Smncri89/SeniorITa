#!/usr/bin/env bash
# RULE-012 structural enforcement — Safe-Destructive Operations
# Portable version for Enterprise Multi-Agent Protocol v4
#
# Purpose : block Bash/PowerShell commands matching known-destructive patterns
#           unless a one-shot unlock token exists at ~/.claude/.destructive-unlock
# Input   : Claude Code hook JSON via stdin (tool_name, tool_input.command)
# Exit    : 0 allow · 2 block (with reason on stderr)
# Design  : fail-open on payload parse error; audit log captures every decision.
#
# Requires: bash 4+, python 3.8+

set -uo pipefail

AUDIT_LOG="${HOME}/.claude/telemetry/audit.jsonl"
UNLOCK_TOKEN="${HOME}/.claude/.destructive-unlock"
PROTOCOL_VERSION="v4"

mkdir -p "$(dirname "$AUDIT_LOG")" 2>/dev/null || true

PAYLOAD=$(cat 2>/dev/null || true)
[ -z "$PAYLOAD" ] && exit 0

export HOOK_PAYLOAD="$PAYLOAD"
parsed=$(python -c '
import json, os
try:
    d = json.loads(os.environ.get("HOOK_PAYLOAD",""))
    print(d.get("tool_name","") or "")
    print((d.get("tool_input",{}) or {}).get("command","") or "")
except Exception:
    print("")
    print("")
' 2>/dev/null)

TOOL_NAME=$(printf '%s' "$parsed" | sed -n '1p' | tr -d '\r')
CMD=$(printf '%s' "$parsed" | sed -n '2p' | tr -d '\r')

case "$TOOL_NAME" in
  Bash|PowerShell) ;;
  *) exit 0 ;;
esac
[ -z "$CMD" ] && exit 0

# Destructive patterns (ERE). Conservative — prefer false-positive over false-negative.
# Contribute new patterns via PR: tag with a comment linking to the incident that motivated it.
DANGER='(rm[[:space:]]+(-[a-zA-Z]*[rRfF][a-zA-Z]*[[:space:]]+)+|Remove-Item[[:space:]]+.*-Recurse.*-Force|Remove-Item[[:space:]]+.*-Force.*-Recurse|git[[:space:]]+push[[:space:]]+.*--force|git[[:space:]]+reset[[:space:]]+--hard|git[[:space:]]+clean[[:space:]]+-[a-zA-Z]*f[a-zA-Z]*d|DROP[[:space:]]+DATABASE|DROP[[:space:]]+TABLE|TRUNCATE[[:space:]]+TABLE|chmod[[:space:]]+-?R?[[:space:]]*777|shutdown[[:space:]]+/[sr]|del[[:space:]]+/[sfq])'

TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
SID="${CLAUDE_SESSION_ID:-unknown}"
CID="cid-$(date -u +%s%N 2>/dev/null || date -u +%s)-$$"

log_audit() {
  local safe_cmd
  safe_cmd=$(printf '%s' "$CMD" | head -c 200 | tr '"' "'" | tr -d '\n\r')
  printf '{"timestamp":"%s","session_id":"%s","correlation_id":"%s","protocol_version":"%s","event_type":"destructive_guard_hook","actor":"agent","tool":"%s","command":"%s","decision":"%s","rule_id":"RULE-012"}\n' \
    "$TS" "$SID" "$CID" "$PROTOCOL_VERSION" "$TOOL_NAME" "$safe_cmd" "$1" >> "$AUDIT_LOG" 2>/dev/null || true
}

if ! printf '%s' "$CMD" | grep -qE "$DANGER"; then
  exit 0
fi

if [ -f "$UNLOCK_TOKEN" ]; then
  rm -f "$UNLOCK_TOKEN"
  log_audit "unlocked"
  exit 0
fi

log_audit "deny"
cat >&2 <<EOF
[RULE-012 BLOCK] Safe-Destructive Ops gate.
Command matches a known-destructive pattern:
  ${CMD}
Authorise:  touch ~/.claude/.destructive-unlock  (one-shot)
Prefer:     --dry-run, trash-cli, git revert, soft delete.
EOF
exit 2
