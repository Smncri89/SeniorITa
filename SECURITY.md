# Security Policy

## Scope

This repository contains **governance rules and hook scripts**, not application code.
Vulnerabilities of interest:

- Bypass of `policy-freeze.sh` (RULE-017) — any way to modify governance files
  without consuming the unlock token.
- Bypass of `destructive-guard.sh` (RULE-012) — any known-destructive command that
  passes the regex without unlock.
- Payload injection in hook inputs that causes arbitrary code execution.
- Audit log tampering paths that leave no trace.
- Weakness in the auto-detection heuristics of RULE-015 (false-negative SECRET tagging).

## Reporting

Please **do not open a public issue** for a vulnerability.

Instead:
1. Open a private security advisory on GitHub: `Settings → Security → Advisories → New draft`.
2. Or email the maintainer with `[SECURITY]` in the subject.
3. Provide: reproduction steps, affected version, expected vs actual behaviour, suggested remediation.

Response SLA: initial acknowledgement within 3 business days.

## Known limitations (already public)

Documented in `PROTOCOL.md` §9 (residual gaps). These are **not** considered
vulnerabilities as they are disclosed by design:

- Hooks fail-open on payload parse errors (documented trade-off).
- Audit log lives on a filesystem writable by the agent (mitigation on roadmap).
- No OS-level sandbox; single-user workstation trust boundary assumed.
- TOCTOU race on unlock-token consume (low likelihood on single-user host).

## Not in scope

- Claude Code itself — report to Anthropic.
- The user's underlying OS or shell — report upstream.
- Vulnerabilities that require prior root/admin on the workstation.
