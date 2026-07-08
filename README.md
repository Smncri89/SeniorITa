# Enterprise Multi-Agent Protocol

Turnkey **governance protocol** and **adoption kit** for teams deploying [Claude Code](https://claude.ai/code) as an autonomous DevOps agent inside enterprises with critical-infrastructure requirements.

> Zero-Trust posture · Security-first decision priority · 19 operational rules
> Structural enforcement via `PreToolUse` hooks · Peer-reviewed by multiple LLMs

[![Validation](https://img.shields.io/badge/validation-invariant--checked-brightgreen)](.github/workflows/validate.yml)
[![Rules](https://img.shields.io/badge/rules-19-blue)](PROTOCOL.md)
[![License](https://img.shields.io/badge/license-MIT-informational)](LICENSE)

---

## What you get

- **`PROTOCOL.md`** — the full protocol specification (v4), sanitized for external review.
- **`rules/clinerules.template`** — portable `.clinerules` file to drop into any workspace.
- **`hooks/`** — two production-tested Bash hooks (`policy-freeze.sh` + `destructive-guard.sh`) enforcing RULE-012 and RULE-017 at the `PreToolUse` layer.
- **`templates/settings.hooks.snippet.json`** — copy-paste-ready snippet for `~/.claude/settings.json`.
- **`scripts/install.sh`** — idempotent one-command bootstrap (Linux/macOS/Windows-Git-Bash).
- **`scripts/validate.sh`** — invariant checks (rule count, schema, secret-scan) suitable for CI.
- **`scripts/audit-rotate.sh`** — daily log rotation for `audit.jsonl`.
- **`.github/workflows/validate.yml`** — GitHub Actions running the invariants on every PR.
- **Issue templates** — YAML-schema-guided intake for external reviews, rule proposals, bug reports.

## Who it's for

- Enterprise IT teams standardising how AI coding agents interact with critical systems.
- SecOps / DevOps engineers who want auditable, testable AI-agent governance.
- Solo senior developers running Claude Code on production-adjacent workstations.

## 5-minute install

```bash
git clone https://github.com/Smncri89/enterprise-multi-agent-protocol.git
cd enterprise-multi-agent-protocol
bash scripts/install.sh --dry-run   # preview
bash scripts/install.sh             # apply
```

The installer:
1. Backs up any existing `~/.clinerules`, `~/.claude/settings.json`, memory files.
2. Copies portable rules to `~/.clinerules` (skipping if identical — idempotent).
3. Installs the two hook scripts to `~/.claude/hooks/` and marks them executable.
4. Merges the hook registration snippet into `~/.claude/settings.json` (preserves your existing hooks).
5. Initialises `~/.claude/telemetry/audit.jsonl` with a `protocol_bootstrap` event.
6. Runs `scripts/validate.sh` to confirm all invariants hold.

Uninstall: `bash scripts/uninstall.sh` (restores backups).

## Concepts (skim these)

| Concept | Where to read |
|---------|--------------|
| Why this protocol exists + install | [`docs/ADOPTION.md`](docs/ADOPTION.md) |
| How the pieces fit together | [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) |
| Detailed rule-by-rule reference | [`docs/RULES.md`](docs/RULES.md) |
| Common questions | [`docs/FAQ.md`](docs/FAQ.md) |
| Contributing new rules | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Reporting vulnerabilities | [`SECURITY.md`](SECURITY.md) |
| Version history | [`CHANGELOG.md`](CHANGELOG.md) |

## Break-glass workflow (RULE-012 / RULE-017)

When the hooks block a legitimate operation, the user drops a one-shot token:

```bash
touch ~/.claude/.policy-unlock        # next Write/Edit on governance files
touch ~/.claude/.destructive-unlock   # next destructive command
```

Tokens are **auto-consumed** on first matching operation — no permanent bypass.
Every allow/deny/unlock event is logged to `~/.claude/telemetry/audit.jsonl`.

## Peer-review history

| Reviewer | Round | Contribution |
|----------|:-:|-----------|
| Gemini   | 1 | Security-first priority, self-mod lock, structural roadmap |
| ChatGPT  | 1 | Data classification, risk tagging, audit log, change-mgmt |
| Gemini   | 2 | Write-only audit service, WDAC/AppLocker (roadmap) |
| ChatGPT  | 2 | Evidence-gated retry, operative data-class behaviours, schema uplift |

Full delta in [`CHANGELOG.md`](CHANGELOG.md).

## License
MIT — see [`LICENSE`](LICENSE).
