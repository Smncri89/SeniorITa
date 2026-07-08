# Pull Request

## What
<!-- One-line summary -->

## Why
<!-- Motivation: linked issue #, incident, review finding, etc. -->

## How
<!-- Approach; if this modifies rules or hooks, apply RULE-010: -->
- **Root Cause**:
- **Blast Radius**:
- **Prevention**:
- **Risk**: [LOW | MEDIUM | HIGH | CRITICAL]
- **Impact**:
- **Rollback**:
- **Dependencies**:

## Debate (RULE-008)
<!-- If ≥2 approaches were viable, briefly justify the choice -->

## Checklist
- [ ] `bash scripts/validate.sh` passes locally
- [ ] `shellcheck -S style` passes on modified `*.sh`
- [ ] `CHANGELOG.md` updated
- [ ] `PROTOCOL.md` version bumped (if governance behaviour changed)
- [ ] No secrets or PII introduced
