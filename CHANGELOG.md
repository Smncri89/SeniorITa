# Changelog

All notable changes to this protocol are documented here.
Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

## [v4] — 2026-07-08

### Added
- **Structural enforcement** — two `PreToolUse` hooks (`policy-freeze.sh`, `destructive-guard.sh`) with break-glass one-shot unlock tokens.
- **Turnkey adoption kit** — `install.sh`, `uninstall.sh`, `validate.sh`, `audit-rotate.sh`.
- **GitHub Actions CI** — `validate.yml` runs invariants on every PR.
- **Issue templates** — external-review, rule-proposal, bug-report YAML schemas.

### Changed
- **RULE-009** Auto-Correction Loop — now *evidence-gated*: retry requires new evidence, "try again" is not a hypothesis.
- **RULE-015** Data Classification — expanded with *operative handling per class* (PUBLIC/INTERNAL/CONFIDENTIAL/SECRET) and auto-detection heuristics.
- **RULE-018** Persistent Audit Log — schema uplift: mandatory `session_id`, `correlation_id`, `protocol_version`.
- **RULE-019** — from arbitrary session caps to *risk-adaptive confirmation gate* keyed on RULE-016 tags.

### Reviewer origin
ChatGPT round-2 review (structural gaps + operational uplifts), Gemini round-2 review (audit-log write-only service, WDAC/AppLocker roadmap items).

## [v3] — 2026-07-08

### Added
- **RULE-015** Data Classification (PUBLIC/INTERNAL/CONFIDENTIAL/SECRET, default INTERNAL).
- **RULE-016** Pre-emptive Task Risk Tagging (LOW/MEDIUM/HIGH/CRITICAL as first line of `[STATUS]`).
- **RULE-017** Policy Immutability Gate (behavioural in v3, structural in v4).
- **RULE-018** Persistent Append-Only Audit Log (JSONL).
- **RULE-019** Blast-Radius Session Cap (later reworked in v4).

### Changed
- **RULE-013 Decision Priority** reordered to Security-first (was Correctness-first).

### Reviewer origin
Gemini round-1 + ChatGPT round-1 convergent findings + internal review.

## [v2] — 2026-07-08

### Added
- **RULE-010** Root Cause First (RootCause·BlastRadius·Prevention·Risk·Impact·Rollback·Dependencies).
- **RULE-011** Idempotency mandate.
- **RULE-012** Safe-Destructive Ops.
- **RULE-013** Decision Priority (initial version, Correctness-first).
- **RULE-014** 6-step workflow gate.
- Fourth reviewer persona: **DevOps Enterprise Operations Engineer**.

## [v1] — 2026-07-08

### Added
- Initial 9 rules (RULE-001 … RULE-009).
- Multi-Agent lens (Architect + SecOps + QA).
- Self-learning ecosystem (agents, skills, knowledge base).
