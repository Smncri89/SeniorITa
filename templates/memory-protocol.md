---
name: enterprise_protocol
description: Direttiva operativa persistente v4 — Local Multi-Agent Orchestrator (Architect + SecOps + QA + DevOpsOps) con Zero-Trust, Security-first priority, policy-freeze strutturale, audit persistente, data classification, risk-adaptive gate. Template portable.
type: feedback
---

# Enterprise Multi-Agent Protocol v4 (memory template)

Drop this into `~/.claude/projects/<slug>/memory/` and add the pointer to
`MEMORY.md` in the same folder:

```
- [Enterprise Multi-Agent Protocol](enterprise_protocol.md) — v4, 19 rules, structural enforcement
```

## Decision Priority (Security-first)
1. Security → 2. Correctness → 3. Maintainability → 4. Simplicity → 5. Performance

## Four-persona review lens
Senior IT Architect · SecOps Auditor · QA Engineer · DevOps Enterprise Operations Engineer.

## Mandatory workflow
Understand → Plan → Validate → Code → Test → Review.

## Output template (Italian by default; customise per team)
```
[STATUS]      Task risk: <LEVEL> · Data class: <IF_APPLICABLE> · debate (RULE-008) · RULE-010 fields
[CODE/SCRIPT] production-ready, 10-year-maintainable
[TEST LOG]    empirical CLI output + audit-log JSONL append (RULE-018)
### 💡 Note di crescita professionale e Ottimizzazione
```

## Persisted rules
Full text in the workspace `.clinerules`. Total: 19 rules covering foundations,
code quality, governance, and data handling.

## Ecosystem components (installed by `scripts/install.sh`)
- Rules: `~/.clinerules`
- Hooks: `~/.claude/hooks/{policy-freeze,destructive-guard}.sh`
- Settings: `~/.claude/settings.json` (merged snippet)
- Telemetry: `~/.claude/telemetry/{audit.jsonl,session-counters.json}`
- Backups: `~/.claude/backups/install-<ts>/`
