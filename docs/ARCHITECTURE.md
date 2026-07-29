# Architecture

How the parts fit together.

## Component map

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                          Claude Code (CLI)                          â”‚
â”‚                                                                     â”‚
â”‚  User prompt â†’ Model reasoning â†’ Tool call (Write/Edit/Bash/â€¦)      â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                               â”‚
                               â–¼
              â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
              â”‚  PreToolUse hook dispatcher     â”‚
              â”‚  (~/.claude/settings.json)      â”‚
              â””â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                       â”‚               â”‚
       Write|Edit|     â”‚               â”‚  Bash|PowerShell
       NotebookEdit    â–¼               â–¼
              â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
              â”‚ policy-      â”‚  â”‚ destructive-     â”‚
              â”‚ freeze.sh    â”‚  â”‚ guard.sh         â”‚
              â”‚ (RULE-017)   â”‚  â”‚ (RULE-012)       â”‚
              â””â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                     â”‚                    â”‚
                     â–¼                    â–¼
              â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
              â”‚ .policy-     â”‚   â”‚ .destructive-  â”‚
              â”‚ unlock       â”‚   â”‚ unlock         â”‚
              â”‚ (one-shot)   â”‚   â”‚ (one-shot)     â”‚
              â””â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”˜   â””â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”˜
                     â”‚                    â”‚
                     â””â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                              â–¼
                   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                   â”‚ audit.jsonl        â”‚  â† every allow/deny/unlock
                   â”‚ (append-only)      â”‚    with correlation_id
                   â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜

     â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
     â”‚ .clinerules (workspace)     â”‚  â† 19 behavioural rules
     â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
     â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
     â”‚ enterprise_protocol.md      â”‚  â† persistent memory (Claude Code)
     â”‚ (~/.claude/projects/â€¦)      â”‚
     â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

## The three layers

### 1. Policy (declarative)

- `.clinerules` â€” 19 rules; loaded automatically by Claude Code from workspace root.
- `enterprise_protocol.md` â€” memory file linked from `MEMORY.md`; loaded every session as feedback context.

### 2. Enforcement (imperative)

- `hooks/policy-freeze.sh` â€” intercepts `Write|Edit|NotebookEdit` on governance files. Blocks unless `~/.claude/.policy-unlock` exists (one-shot consumed on allow).
- `hooks/destructive-guard.sh` â€” intercepts `Bash|PowerShell` matching a curated regex of destructive patterns. Blocks unless `~/.claude/.destructive-unlock` exists.

Both scripts:
- Read tool payload from stdin as JSON (Claude Code hook contract).
- Parse via Python heredoc using env-var passing (robust to backslashes/quotes on Windows msys).
- Exit `0` = allow Â· `2` = block with reason on stderr.
- Fail-open on payload parse error (deliberate trade-off; see `SECURITY.md`).

### 3. Audit (immutable-by-convention)

- `~/.claude/telemetry/audit.jsonl` â€” append-only JSON Lines.
- Schema: `timestamp Â· session_id Â· correlation_id Â· protocol_version Â· event_type Â· actor Â· target Â· decision Â· rule_id Â· risk_level Â· data_class`.
- Rotation: `scripts/audit-rotate.sh` (run daily via cron/Task Scheduler).
- Roadmap: replace file sink with authenticated POST to a local write-only Windows service (Gemini#2 recommendation) â€” resists agent-side tampering.

## Data flow â€” a destructive command

```
1. User asks: "clean the /tmp/build folder"
2. Model plans and emits: Bash tool call, command = "rm -rf /tmp/build"
3. Claude Code fires PreToolUse hooks in registered order
4. destructive-guard.sh reads stdin JSON, matches "rm[[:space:]]+-rf" regex
5. Checks for ~/.claude/.destructive-unlock â€” not present
6. Appends audit.jsonl entry: {decision: "deny", rule_id: "RULE-012", ...}
7. Exits 2 with stderr message â†’ Claude Code reports block to model
8. Model shows block reason to user and requests explicit unlock
9. User runs: touch ~/.claude/.destructive-unlock
10. Model retries; hook sees token, consumes it, appends {decision: "unlocked"}, exits 0
11. Command runs; PostToolUse phase captures the result (optional future addition)
```

## Design principles

- **Fail-open on parse error, fail-closed on unknown pattern.** Corrupted payload should not brick Claude Code; unknown-but-suspicious command patterns should be added to the regex, not silently allowed.
- **Break-glass tokens are one-shot.** A stale token cannot compound multiple violations.
- **Behavioural rules survive without hooks.** Anyone can adopt just `.clinerules` without installing the hooks; enforcement degrades to behavioural discipline (still meaningful).
- **Idempotent install.** Re-running `install.sh` is safe; it detects existing state and only patches missing pieces.
- **Rules are text; enforcement is code; both are versioned in git.** Governance change follows the same review discipline as code change.

## Compatibility

| OS | Shell | Status |
|----|-------|--------|
| Windows 11 | Git Bash | âœ… Reference platform |
| macOS | zsh/bash | âœ… Expected to work (Python 3.8+ required) |
| Linux | bash | âœ… Expected to work |
| WSL2 | bash | âœ… Expected to work |

