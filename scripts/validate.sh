#!/usr/bin/env bash
# validate.sh — invariant checks for Enterprise Multi-Agent Protocol v4
# Suitable for both local pre-commit and GitHub Actions CI
# Exit 0 = all green · exit 1 = at least one invariant broken
set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

fail=0
pass=0
check() {
  local name="$1" ok="$2"
  if [ "$ok" -eq 1 ]; then
    printf '✅ %s\n' "$name"; pass=$((pass+1))
  else
    printf '❌ %s\n' "$name"; fail=$((fail+1))
  fi
}

# --- 1. Rule count invariant ---------------------------------------
n=$(grep -c "^## RULE-" rules/clinerules.template)
check "Rule count invariant: ${n}/19 in clinerules.template" \
  "$([ "$n" -eq 19 ] && echo 1 || echo 0)"

# PROTOCOL.md should reference all 19 rules
prot=$(grep -oE '\| 0[0-9][0-9] \|' PROTOCOL.md 2>/dev/null | wc -l)
check "PROTOCOL.md rule references: ${prot}/19" \
  "$([ "$prot" -eq 19 ] && echo 1 || echo 0)"

# --- 2. Hooks executable + present ---------------------------------
h_ok=1
for f in hooks/policy-freeze.sh hooks/destructive-guard.sh; do
  [ -f "$f" ] || h_ok=0
done
check "Hooks present" "$h_ok"

# --- 3. Hook standalone smoke test ---------------------------------
smoke=1
# Test 1: policy-freeze should block .clinerules edit
out=$(echo '{"tool_name":"Write","tool_input":{"file_path":"/tmp/.clinerules"}}' \
  | bash hooks/policy-freeze.sh 2>/dev/null; echo "rc=$?")
grep -q "rc=2" <<< "$out" || smoke=0
# Test 2: destructive-guard should block rm -rf
out=$(echo '{"tool_name":"Bash","tool_input":{"command":"rm -rf /tmp/x"}}' \
  | bash hooks/destructive-guard.sh 2>/dev/null; echo "rc=$?")
grep -q "rc=2" <<< "$out" || smoke=0
# Test 3: destructive-guard should allow innocuous command
out=$(echo '{"tool_name":"Bash","tool_input":{"command":"ls -la"}}' \
  | bash hooks/destructive-guard.sh 2>/dev/null; echo "rc=$?")
grep -q "rc=0" <<< "$out" || smoke=0
check "Hook smoke tests (3/3)" "$smoke"

# --- 4. JSON validity of settings snippet --------------------------
if python -c "import json; json.load(open('templates/settings.hooks.snippet.json'))" 2>/dev/null; then
  check "settings snippet is valid JSON" 1
else
  check "settings snippet is valid JSON" 0
fi

# --- 5. No secrets in tracked files --------------------------------
# Regex targets values-after-colon-or-equals, not the words themselves in prose
if grep -rEnH "([Aa]pi[_-]?[Kk]ey|[Tt]oken|[Pp]assw(or)?d|[Ss]ecret)[[:space:]]*[:=][[:space:]]*['\"]?[A-Za-z0-9/_+\-]{16,}" \
     --include='*.md' --include='*.sh' --include='*.json' --include='*.yml' \
     --exclude-dir='.git' . 2>/dev/null; then
  check "No secrets in tracked files" 0
else
  check "No secrets in tracked files" 1
fi

# --- 6. bash -n syntax check on all shell scripts -------------------
syn=1
for f in hooks/*.sh scripts/*.sh; do
  bash -n "$f" 2>/dev/null || { echo "  syntax error: $f"; syn=0; }
done
check "Bash syntax (bash -n) on all scripts" "$syn"

# --- 7. Every rule referenced in RULES.md ---------------------------
rules_doc=$(grep -oE 'RULE-0[0-9][0-9]' docs/RULES.md 2>/dev/null | sort -u | wc -l)
check "docs/RULES.md references all 19 rules: ${rules_doc}/19" \
  "$([ "$rules_doc" -eq 19 ] && echo 1 || echo 0)"

# --- Summary --------------------------------------------------------
echo ""
echo "───────────────────────────────────────"
printf 'Total: %d passed · %d failed\n' "$pass" "$fail"
[ "$fail" -eq 0 ] && exit 0 || exit 1
