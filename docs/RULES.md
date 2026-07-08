# Detailed Rule Reference

Compact per-rule reference. For the canonical narrative see `PROTOCOL.md`.

## Foundations
- **RULE-001 Test-Before-Confirm** — no task complete without empirical CLI test log.
- **RULE-002 Zero-Trust sources** — cross-check ≥2 primary sources; cite versions + dates.
- **RULE-003 Persist learnings** — file non-trivial fixes via post-mortem / curator.
- **RULE-004 Enterprise output baseline** — error handling, exit codes, structured logs, comments.
- **RULE-005 Growth notes** — every macro-task ends with a growth reflection.

## Code quality
- **RULE-006 Static analysis gate** — `shellcheck -S style` (Bash), `Invoke-ScriptAnalyzer` (PS); documented fallback allowed.
- **RULE-007 Multi-Agent lens** — Architect + SecOps + QA + DevOps Enterprise Ops review on every task.
- **RULE-008 Debate-Before-Code** — ≥2 approaches scored on security/maintainability/perf/blast-radius.
- **RULE-009 Auto-Correction Loop (evidence-gated, v4)** — retry requires NEW evidence; "try again" is not a hypothesis; max 3 iterations then escalate.

## Governance & operational safety
- **RULE-010 Root Cause First** — declare RootCause · BlastRadius · Prevention · Risk · Impact · Rollback · Dependencies.
- **RULE-011 Idempotency mandate** — scripts safely re-runnable; justify non-idempotent code in header.
- **RULE-012 Safe-Destructive Ops (STRUCTURAL v4)** — enforced by `hooks/destructive-guard.sh` + one-shot `~/.claude/.destructive-unlock` token.
- **RULE-013 Decision Priority** — Security > Correctness > Maintainability > Simplicity > Performance.
- **RULE-014 6-step workflow gate** — Understand→Plan→Validate→Code→Test→Review.

## Governance hardening (v3+)
- **RULE-015 Data Classification (v4 operative)** — PUBLIC / INTERNAL / CONFIDENTIAL / SECRET; SECRET → fingerprint hash only; auto-detection heuristics for unlabelled data.
- **RULE-016 Pre-emptive Task Risk Tagging** — LOW / MEDIUM / HIGH / CRITICAL as first line of `[STATUS]`.
- **RULE-017 Policy Immutability Gate (STRUCTURAL v4)** — enforced by `hooks/policy-freeze.sh` + one-shot `~/.claude/.policy-unlock` token.
- **RULE-018 Persistent Append-Only Audit Log (v4 schema)** — mandatory: `session_id`, `correlation_id`, `protocol_version`.
- **RULE-019 Risk-Adaptive Confirmation Gate (v4)** — HIGH/CRITICAL requires explicit user confirmation; no arbitrary counter caps.

## Enforcement matrix

| Rule | Mode | Bypassable by | Detection |
|------|------|---------------|-----------|
| 001–011 | Behavioural | Model self-compliance failure | Missing `[TEST LOG]` in output |
| 012 | Structural (hook) | Different tool name / regex miss | `audit.jsonl` deny records |
| 013–016 | Behavioural | Missing tag in `[STATUS]` | Text scan of `[STATUS]` block |
| 017 | Structural (hook) | Different tool / bypass Claude Code | `audit.jsonl` deny records |
| 018 | Behavioural + hook side-effect | Direct write to `audit.jsonl` | External SIEM ingestion check |
| 019 | Behavioural | Missing confirm on HIGH/CRITICAL | Cross-ref `[STATUS]` + audit |

## Roadmap (from external review, not yet implemented)

- Windows service exposing an authenticated POST endpoint for audit ingestion (replaces file sink, resists agent-side tampering).
- WDAC/AppLocker or container-isolated CLI process for OS-level sandboxing.
- Filesystem ACL denying agent-user write on policy files (belt-and-braces on RULE-017).
- External webhook approval for `CRITICAL` risk tasks (four-eyes at team scale).
