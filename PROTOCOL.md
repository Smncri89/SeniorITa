---
title: Enterprise Multi-Agent Protocol v4 — External Review Package
created: 2026-07-08
updated: 2026-07-08
version: 4
tags: [governance, ai-agent, devops, security, review]
status: active
audience: external reviewers (peer architects, security, compliance)
prior_reviews:
  - {reviewer: Gemini,  round: 1, version_reviewed: v2}
  - {reviewer: ChatGPT, round: 1, version_reviewed: v2}
  - {reviewer: Gemini,  round: 2, version_reviewed: v3}
  - {reviewer: ChatGPT, round: 2, version_reviewed: v3}
  - {reviewer: Internal, round: 1, version_reviewed: v2}
---

# Enterprise Multi-Agent Protocol v4 — External Review Package

> **Purpose.** Sanitized snapshot of the internal operational protocol governing an AI
> coding agent in a high-criticality S.p.A. environment. **v4 introduces structural
> enforcement (PreToolUse hooks) and incorporates convergent findings from a second
> round of external LLM review (Gemini#2, ChatGPT#2).** Section 12 summarises deltas.

---

## 1. Context

- **Deployment**: single-developer workstation (Windows 11) running an AI coding assistant
  as an autonomous Local Multi-Agent Orchestrator for enterprise DevOps work.
- **Stakes**: production-adjacent scripting, infrastructure automation, security-sensitive changes.
- **Enforcement model (v4)**:
  - **Structural** for RULE-012 (destructive ops) and RULE-017 (policy immutability) —
    two `PreToolUse` hooks with break-glass unlock tokens (one-shot, auto-consumed).
  - **Behavioural** for the remaining rules — with roadmap toward further structural gates.

## 2. Guiding principles

### 2.1 Decision priority (v3 reorder, unchanged in v4 — Security-first)

| # | Priority         | Rationale |
|---|------------------|-----------|
| 1 | Security         | Zero-Trust posture; a correct-but-insecure solution is a defect. |
| 2 | Correctness      | Wrong-but-fast is worse than slow-but-right. |
| 3 | Maintainability  | Code must survive a 10-year maintenance horizon. |
| 4 | Simplicity       | Minimum sufficient complexity. |
| 5 | Performance      | Optimise only on empirical evidence. |

*Documented exception*: security theatre without real protection may be waived (state in `[STATUS]`).

### 2.2 Four-persona review lens
Senior IT Architect · SecOps Auditor · QA Engineer · DevOps Enterprise Operations Engineer.

### 2.3 Mandatory workflow
`Understand → Plan → Validate → Code → Test → Review`.

## 3. Operational rules (RULE-001 … RULE-019)

| ID | Name | Intent (v4 changes in **bold**) |
|----|------|--------------------------------|
| 001 | Test-Before-Confirm | Empirical CLI test log required. |
| 002 | Zero-Trust sources | ≥2 primary sources; cite versions + dates. |
| 003 | Persist learnings | File non-trivial fixes via post-mortem / curator. |
| 004 | Enterprise output baseline | Error handling, exit codes, structured logs, comments. |
| 005 | Growth notes | Every macro-task ends with a growth reflection. |
| 006 | Static analysis gate | shellcheck / PSScriptAnalyzer, documented fallback. |
| 007 | Multi-Agent lens | 4-persona review before emission. |
| 008 | Debate-Before-Code | ≥2 approaches scored. |
| 009 | Auto-Correction Loop | **v4: evidence-gated** — retry requires NEW evidence, not just "try again". |
| 010 | Root Cause First | Declare RootCause·BlastRadius·Prevention·Risk·Impact·Rollback·Dependencies. |
| 011 | Idempotency mandate | Scripts safely re-runnable. |
| 012 | Safe-Destructive Ops | **v4 STRUCTURAL** — `destructive-guard.sh` PreToolUse hook + one-shot unlock token. |
| 013 | Decision Priority (v3) | Security > Correctness > Maintainability > Simplicity > Performance. |
| 014 | 6-step workflow gate | Understand→Plan→Validate→Code→Test→Review. |
| 015 | Data Classification | **v4: operative behaviours per class** — SECRET→fingerprint hash, CONFIDENTIAL→redact, auto-detection heuristics. |
| 016 | Pre-emptive Task Risk Tagging | Every task tagged LOW\|MEDIUM\|HIGH\|CRITICAL in first line of [STATUS]. |
| 017 | Policy Immutability Gate | **v4 STRUCTURAL** — `policy-freeze.sh` PreToolUse hook + one-shot unlock token. |
| 018 | Persistent Append-Only Audit Log | **v4 schema** — mandatory: session_id, correlation_id, protocol_version. |
| 019 | Risk-Adaptive Confirmation Gate | **v4 rewrite** — no arbitrary caps; HIGH/CRITICAL requires explicit confirm. |

## 4. Data classification — operative handling (RULE-015 v4)

| Class | Chat/Logs | Files/Exports | Audit log emission |
|-------|-----------|---------------|--------------------|
| PUBLIC       | No restriction | Allowed anywhere | Full detail |
| INTERNAL     | Local only, no export | Workspace only | Full detail |
| CONFIDENTIAL | Redact/truncate unless user explicit | No export | Truncated |
| SECRET       | NEVER plaintext; reference by env var | NEVER plaintext | `data_class:"SECRET"` + fingerprint hash only |

Auto-detection heuristics (when unlabelled): password/api-key/token/PEM/JWT → SECRET · email/SSN/IBAN → CONFIDENTIAL · else → INTERNAL (fail-safe default).

## 5. Structural enforcement — PreToolUse hooks (v4 new)

Two Bash scripts registered as `PreToolUse` hooks in `~/.claude/settings.json`:

| Hook | Matcher | Action | Unlock token |
|------|---------|--------|--------------|
| `policy-freeze.sh` | `Write\|Edit\|NotebookEdit` on governance files | exit 2 with reason | `~/.claude/.policy-unlock` (one-shot) |
| `destructive-guard.sh` | `Bash\|PowerShell` matching destructive regex | exit 2 with reason | `~/.claude/.destructive-unlock` (one-shot) |

Destructive patterns intercepted: `rm -rf`, `Remove-Item -Force -Recurse`, `git push --force`, `git reset --hard`, `git clean -fd`, `DROP DATABASE/TABLE`, `TRUNCATE TABLE`, `chmod 777`, `shutdown /s|/r`, `del /s|/f|/q`.

Break-glass semantics: token file must exist to allow the operation; the hook deletes it immediately after allowing (one-shot). Every decision (allow/deny/unlocked) is logged to `audit.jsonl`.

Fail-safe design: on payload parse error, hooks exit 0 (do not break the harness). This is a deliberate trade-off — a corrupt payload could theoretically bypass the gate, but the alternative (fail-closed on any hiccup) would render Claude Code unusable on any harness/protocol version mismatch.

## 6. Output template (Italian by default)

```
[STATUS]      Task risk: <LEVEL> · Data class: <IF_APPLICABLE> · debate + RULE-010 fields
[CODE/SCRIPT] production-ready, 10-year-maintainable
[TEST LOG]    empirical CLI output + audit-log JSONL append (RULE-018)
### 💡 Note di crescita professionale e Ottimizzazione
```

## 7. Logging standard (RULE-018 v4 schema)

Every audit event MUST include:
- `timestamp` (ISO-8601 UTC)
- `session_id`
- `correlation_id` (per logical operation, enables chaining)
- `protocol_version` ("v4")
- `event_type`, `actor`, `target`, `decision`
- `rule_id`, `risk_level`, `data_class` (when applicable)

## 8. Support ecosystem
- Agents: `tech-scout`, `knowledge-curator`, `security-analyst`.
- Skills: `/tech-radar`, `/learn-topic`, `/postmortem`.
- KB: `tech-radar/`, `postmortems/`, `patterns/`, `runbooks/`, `security/`.
- Backup: timestamped snapshots pre-mutation of any governance file.
- Telemetry (v3+): `~/.claude/telemetry/{audit.jsonl,session-counters.json}`.
- **Hooks (v4)**: `~/.claude/hooks/{policy-freeze,destructive-guard}.sh`.

## 9. Residual gaps (self-disclosed after v4)

| Gap | Current mitigation | Long-term fix |
|-----|-------------------|---------------|
| Audit log writable by agent (potential tampering) | Behavioural + append-only convention | **Local write-only Windows service** exposing authenticated POST endpoint (Gemini#2 recommendation) |
| No OS-level sandbox / privilege drop | Single-user workstation trust boundary | **WDAC/AppLocker** or container-isolated CLI (Gemini#2) |
| Hooks fail-open on parse error | Documented trade-off | Structured logging of parse failures + periodic anomaly review |
| No filesystem ACL on policy files | RULE-017 hook covers Write/Edit tools | ACL denying write to agent-user (requires admin) |
| TOCTOU race on unlock-token consume | Single-user workstation, low likelihood | `flock`/atomic rename on token |
| No four-eyes for policy changes | Single-dev deployment | External webhook approval flow |

## 10. Reviewer feedback registry (aggregated)

| Reviewer | Round | Version | Verdict | Contributions merged in |
|----------|:-:|:-:|---------|-------------------------|
| Gemini   | 1 | v2 | Adopt-with-changes | v3: Security→#1, policy self-mod lock, structural-enforcement roadmap |
| ChatGPT  | 1 | v2 | Adopt-with-changes | v3: data classification, task risk tagging, persistent audit log, change-mgmt flow |
| Internal | 1 | v2 | Adopt-with-changes | v3: blast-radius session cap (later reworked in v4) |
| Gemini   | 2 | v3 | Adopt-with-changes | v4 roadmap: audit log write-only Windows service, WDAC/AppLocker |
| ChatGPT  | 2 | v3 | Adopt-with-changes | v4: RULE-009 evidence-gated, RULE-015 operative behaviours, RULE-018 schema (+correlation_id, +protocol_version), RULE-019 risk-adaptive gate |

## 11. Open questions for the next reviewer (v4 targets)

1. **Structural enforcement adequacy** — the hooks fail-open on parse error and can be bypassed by any process running as the same user. Is this acceptable for "critical infrastructure" or should we require OS-level isolation before considering RULE-012/RULE-017 "enforced"?
2. **Audit log integrity** — the log lives on a filesystem writable by the agent. Without the roadmap Windows-service front-end, is the current append-only convention meaningful, or is it security theatre?
3. **RULE-015 auto-detection heuristics** — the regex-based classification is best-effort. What's the acceptable false-negative rate for SECRET detection before we require an explicit tagging turn?
4. **RULE-019 risk-adaptive gate** — HIGH/CRITICAL requires explicit user confirmation. Is *any* HIGH/CRITICAL operation admissible in auto-mode, or should auto-mode downgrade to manual on such tasks?
5. **Governance drift** — the protocol now has 19 rules. At what count does the protocol itself become a maintainability liability?
6. **Recursive review risk** — v4 was proposed by the same AI it constrains. Does the review chain still catch AI-agreeable governance bias, or are we in an echo chamber?

## 12. Requested reviewer output

```yaml
reviewer: <name/role/model>
version_reviewed: 4
overall_verdict: [Adopt-as-is | Adopt-with-changes | Do-not-adopt]
critical_findings:
  - <finding + suggested remediation>
recommended_additions:
  - <new rule proposal>
priority_disagreements:
  - <e.g. "Auto-detection default should be CONFIDENTIAL because ...">
convergence_check: <do you agree with prior reviewers' convergent findings? if not, why?>
structural_vs_behavioural: <is v4's structural enforcement (2 hooks) meaningful, or theatre?>
```

## 13. Delta v3 → v4

**Structural enforcement activated** (v4 headline):
- `~/.claude/hooks/policy-freeze.sh` — blocks Write/Edit on governance files without one-shot token.
- `~/.claude/hooks/destructive-guard.sh` — blocks known-destructive Bash/PowerShell without one-shot token.
- Both registered in `settings.json` as `PreToolUse`, tested 18/18 standalone.

**Rule amendments** (from ChatGPT#2 review):
- **RULE-009** — retry requires *new evidence*; "try again" is not a hypothesis.
- **RULE-015** — operative handling per class + auto-detection heuristics.
- **RULE-018** — schema now mandates `correlation_id` and `protocol_version` alongside `session_id`.
- **RULE-019** — no arbitrary counter caps; risk-adaptive confirmation gate keyed on RULE-016 tag.

**Roadmap** (from Gemini#2, not yet implemented):
- Local Windows service for write-only audit log ingestion (tamper-resistance).
- WDAC/AppLocker or container isolation for CLI process.

## 14. Version history

- **v1** (2026-07-08) — initial 9 rules, self-learning ecosystem.
- **v2** (2026-07-08) — +RULE-010…014, decision priority, 6-step workflow, DevOpsOps persona.
- **v3** (2026-07-08) — Security-first reorder, +RULE-015…019 (external round-1 convergence).
- **v4** (2026-07-08) — Structural enforcement (2 PreToolUse hooks), RULE-009/015/018/019 amendments from external round-2.

---

*End of external-review package v4. No secrets, credentials, or PII contained.*
