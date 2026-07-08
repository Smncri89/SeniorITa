# Architecture

How the parts fit together.

## Component map

```
┌─────────────────────────────────────────────────────────────────────┐
│                          Claude Code (CLI)                          │
│                                                                     │
│  User prompt → Model reasoning → Tool call (Write/Edit/Bash/…)      │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
              ┌─────────────────────────────────┐
              │  PreToolUse hook dispatcher     │
              │  (~/.claude/settings.json)      │
              └────────┬───────────────┬────────┘
                       │               │
       Write|Edit|     │               │  Bash|PowerShell
       NotebookEdit    ▼               ▼
              ┌──────────────┐  ┌──────────────────┐
              │ policy-      │  │ destructive-     │
              │ freeze.sh    │  │ guard.sh         │
              │ (RULE-017)   │  │ (RULE-012)       │
              └──────┬───────┘  └────────┬─────────┘
                     │                    │
                     ▼                    ▼
              ┌──────────────┐   ┌────────────────┐
              │ .policy-     │   │ .destructive-  │
              │ unlock       │   │ unlock         │
              │ (one-shot)   │   │ (one-shot)     │
              └──────┬───────┘   └────────┬───────┘
                     │                    │
                     └────────┬───────────┘
                              ▼
                   ┌────────────────────┐
                   │ audit.jsonl        │  ← every allow/deny/unlock
                   │ (append-only)      │    with correlation_id
                   └────────────────────┘

     ┌─────────────────────────────┐
     │ .clinerules (workspace)     │  ← 19 behavioural rules
     └─────────────────────────────┘
     ┌─────────────────────────────┐
     │ enterprise_protocol.md      │  ← persistent memory (Claude Code)
     │ (~/.claude/projects/…)      │
     └─────────────────────────────┘
```

## The three layers

### 1. Policy (declarative)

- `.clinerules` — 19 rules; loaded automatically by Claude Code from workspace root.
- `enterprise_protocol.md` — memory file linked from `MEMORY.md`; loaded every session as feedback context.

### 2. Enforcement (imperative)

- `hooks/policy-freeze.sh` — intercepts `Write|Edit|NotebookEdit` on governance files. Blocks unless `~/.claude/.policy-unlock` exists (one-shot consumed on allow).
- `hooks/destructive-guard.sh` — intercepts `Bash|PowerShell` matching a curated regex of destructive patterns. Blocks unless `~/.claude/.destructive-unlock` exists.

Both scripts:
- Read tool payload from stdin as JSON (Claude Code hook contract).
- Parse via Python heredoc using env-var passing (robust to backslashes/quotes on Windows msys).
- Exit `0` = allow · `2` = block with reason on stderr.
- Fail-open on payload parse error (deliberate trade-off; see `SECURITY.md`).

### 3. Audit (immutable-by-convention)

- `~/.claude/telemetry/audit.jsonl` — append-only JSON Lines.
- Schema: `timestamp · session_id · correlation_id · protocol_version · event_type · actor · target · decision · rule_id · risk_level · data_class`.
- Rotation: `scripts/audit-rotate.sh` (run daily via cron/Task Scheduler).
- Roadmap: replace file sink with authenticated POST to a local write-only Windows service (Gemini#2 recommendation) — resists agent-side tampering.

## Data flow — a destructive command

```
1. User asks: "clean the /tmp/build folder"
2. Model plans and emits: Bash tool call, command = "rm -rf /tmp/build"
3. Claude Code fires PreToolUse hooks in registered order
4. destructive-guard.sh reads stdin JSON, matches "rm[[:space:]]+-rf" regex
5. Checks for ~/.claude/.destructive-unlock — not present
6. Appends audit.jsonl entry: {decision: "deny", rule_id: "RULE-012", ...}
7. Exits 2 with stderr message → Claude Code reports block to model
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
| Windows 11 | Git Bash | ✅ Reference platform |
| macOS | zsh/bash | ✅ Expected to work (Python 3.8+ required) |
| Linux | bash | ✅ Expected to work |
| WSL2 | bash | ✅ Expected to work |
