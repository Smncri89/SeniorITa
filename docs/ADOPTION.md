# Adoption Guide

For IT teams introducing this protocol into a workspace where developers use
[Claude Code](https://claude.ai/code) for enterprise DevOps tasks.

## Target audience

| Role | What you'll get from this guide |
|------|--------------------------------|
| IT Lead | How to standardise agent behaviour across a team. |
| SecOps | How structural enforcement + audit logs plug into your audit pipeline. |
| DevOps | Break-glass workflow for legitimate destructive ops. |
| Individual dev | 5-minute personal install. |

## Prerequisites

- [Claude Code](https://claude.ai/code) installed and working.
- Bash available (git-bash on Windows, native on Linux/macOS).
- Python 3.8+ (used by hooks for JSON parsing).
- Write access to `~/.claude/` and the current workspace.

Optional but recommended:
- `shellcheck` (for static analysis of Bash) — the hooks and scripts pass shellcheck clean.
- `gitleaks` (for CI secret scanning).

## Installation

### Fastest path (single user)

```bash
git clone https://github.com/Smncri89/enterprise-multi-agent-protocol.git
cd enterprise-multi-agent-protocol
bash scripts/install.sh --dry-run   # preview what will change
bash scripts/install.sh             # actually install
```

### Team rollout (shared enterprise policy)

Fork this repo internally, then adapt:

1. **Customise `rules/clinerules.template`** — remove/add rules to match your compliance regime (SOX, HIPAA, GDPR, PCI-DSS, ISO 27001 §A.14.2.5).
2. **Distribute** via internal package (Chocolatey/Homebrew tap/deb repo) or a bootstrap script pinned to your fork.
3. **Enforce via CI** — copy `.github/workflows/validate.yml` into your governance repo; block PRs that modify rules without approval.
4. **Central audit ingest** — replace the local `~/.claude/telemetry/audit.jsonl` sink with a POST to your SIEM (Splunk HEC, Elastic, Datadog). See `docs/ARCHITECTURE.md` §Audit.
5. **Onboarding** — each developer runs `bash scripts/install.sh` once per workstation; the installer is idempotent.

## Verification post-install

```bash
bash scripts/validate.sh
```

Expected output:
```
✅ Rule count invariant   : 19/19
✅ Hooks executable       : 2/2
✅ Hooks self-test        : 18/18
✅ settings.json syntax   : valid
✅ No secrets in tracked files
```

## Break-glass procedure

The two structural hooks block sensitive operations by default. To perform one:

```bash
# Modify a governance file (RULE-017 scope):
touch ~/.claude/.policy-unlock
# → next single Write/Edit on .clinerules / enterprise_protocol.md / settings.json is allowed
# → token is auto-consumed; subsequent edits are blocked again

# Run a destructive command (RULE-012 scope):
touch ~/.claude/.destructive-unlock
# → next single rm -rf / git push --force / DROP DATABASE / ... is allowed
```

Both events are logged to `~/.claude/telemetry/audit.jsonl` with a correlation ID.

## Uninstall / rollback

```bash
bash scripts/uninstall.sh
```

Restores backups saved during install (`~/.claude/backups/install-<timestamp>/`).

## Team-level policy examples

- **Auditors**: `bash scripts/audit-rotate.sh` daily via cron/Task Scheduler to
  rotate `audit.jsonl` into `~/.claude/telemetry/archive/YYYY-MM-DD/`.
- **On-call**: replicate `session-counters.json` to your monitoring stack.
- **Compliance**: pin the fork commit hash and require all workstations to `bash scripts/validate.sh` on login.

## Common integrations

| Integration | Where to hook it |
|-------------|------------------|
| Splunk / Elastic SIEM | replace `>> audit.jsonl` with `curl -X POST` in hook scripts |
| PagerDuty on CRITICAL risk | add a `curl` in `session-counters.json` update step |
| GitLab CI | port `.github/workflows/validate.yml` to `.gitlab-ci.yml` |
| Jenkins | wrap `bash scripts/validate.sh` in a `sh` step |

## Support

- Questions → open a discussion (or issue with the `question` label).
- Bugs → **Bug Report** issue template.
- Security → see `SECURITY.md` (private advisory).
