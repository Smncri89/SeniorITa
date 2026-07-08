# Hooks

Two `PreToolUse` hooks providing **structural enforcement** for RULE-012 (destructive ops) and RULE-017 (policy immutability).

## Files

| Script | Purpose | Rule | Unlock token |
|--------|---------|------|--------------|
| `policy-freeze.sh` | Block edits to governance files | RULE-017 | `~/.claude/.policy-unlock` |
| `destructive-guard.sh` | Block destructive Bash/PowerShell commands | RULE-012 | `~/.claude/.destructive-unlock` |

## Local self-test

Standalone smoke test (no Claude Code needed):

```bash
# Should block (exit 2):
echo '{"tool_name":"Write","tool_input":{"file_path":"/tmp/.clinerules"}}' \
  | bash hooks/policy-freeze.sh; echo "exit=$?"

# Should allow (exit 0):
echo '{"tool_name":"Bash","tool_input":{"command":"ls -la"}}' \
  | bash hooks/destructive-guard.sh; echo "exit=$?"

# Break-glass:
touch ~/.claude/.destructive-unlock
echo '{"tool_name":"Bash","tool_input":{"command":"rm -rf /tmp/test"}}' \
  | bash hooks/destructive-guard.sh; echo "exit=$?"   # allow + consume token
ls ~/.claude/.destructive-unlock  # should error (file gone)
```

## Registration in `~/.claude/settings.json`

See `templates/settings.hooks.snippet.json` for the exact JSON to merge into the `hooks.PreToolUse` array. The `install.sh` script does this automatically and preserves any pre-existing hooks.

## Extending the destructive pattern regex

Edit `destructive-guard.sh` and add your pattern to the `DANGER` variable. Include a comment linking to the incident/CVE that motivated it — future maintainers will thank you.

Example (adding `dd of=/dev/sda`):

```bash
# Before:
DANGER='(rm[[:space:]]+(-[a-zA-Z]*[rRfF]...|shutdown[[:space:]]+/[sr]|del[[:space:]]+/[sfq])'
# After:
DANGER='(rm...|del[[:space:]]+/[sfq]|dd[[:space:]]+.*of=/dev/[a-z]+)'
# Reason: prevents accidental disk wipe; see incident #2025-11-14 (internal)
```

Run the smoke test above with your new pattern to confirm.

## Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Hook exits 0 on a governance file edit | Path doesn't match glob | Check normalisation (backslash/case) |
| Hook exits 0 on `rm -rf` | Regex miss | Add pattern; test standalone |
| Hook exits non-0/2 (e.g. 127) | `python` not on PATH | Install Python 3.8+ or adapt hook to use jq |
| Payload parse error, hook fail-opens | JSON malformed by harness | Report to Anthropic; check `audit.jsonl` for parse-fail records |
