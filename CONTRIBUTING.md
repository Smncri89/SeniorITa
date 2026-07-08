# Contributing

Thanks for wanting to strengthen this protocol. Contributions come in three shapes.

## 1. Propose a new rule

Use the **Rule Proposal** issue template. State:
- **Root Cause** — what real incident or class of risk motivates the rule?
- **Blast Radius** — what does this rule cover / not cover?
- **Enforcement mode** — behavioural, structural, or roadmap?
- **Dependencies** — does it require infrastructure the reader may not have?

Rules that only add documentation without changing behaviour are rejected.

## 2. Submit an external review

Use the **External Review** issue template. It embeds the YAML schema from
`PROTOCOL.md` §12 — fill it in and open the issue. Reviews from LLM agents
(Claude, GPT, Gemini, Grok, Llama, Mistral, …) are welcome and encouraged;
please state which model produced the review for reproducibility.

## 3. Fix a bug or improve the tooling

Use the **Bug Report** issue template. For code changes:
- Keep PRs focused (one concern per PR).
- All Bash scripts must pass `shellcheck -S style` (CI enforced).
- Run `bash scripts/validate.sh` locally before pushing.
- Update `CHANGELOG.md` under an `[Unreleased]` heading.

## Review checklist for maintainers

Before merging, verify:
- [ ] Invariants still hold: `bash scripts/validate.sh` green.
- [ ] Rule count stays at the documented number, or `CHANGELOG.md` reflects the change.
- [ ] No secret / PII introduced (`gitleaks` check in CI).
- [ ] Structural enforcement path still tested (`hooks/*.sh` self-tests).
- [ ] `PROTOCOL.md` version bumped if governance behaviour changes.

## Commit style
- Use present-tense imperative: `add`, `fix`, `refactor`, `docs`.
- Reference issue number when applicable.
- Sign off if your employer requires it.
