# FAQ

**Q: Does this replace my company's existing security policy?**
No. It complements it. The rules here concern *how the AI coding agent behaves*.
Your existing policies (change management, IAM, DLP) apply on top.

**Q: Can I use only a subset of rules?**
Yes. `rules/clinerules.template` is a starting point; delete rules that don't apply to your context. Every rule is independent; RULE-012 and RULE-017 additionally depend on the hooks being installed.

**Q: Does this work outside Claude Code?**
The `.clinerules` file is Claude Code-specific. The hook contract (`PreToolUse` with JSON stdin, exit 2 for block) is also Claude Code-specific. The *ideas* (evidence-gated retry, break-glass tokens, risk-adaptive gates) port to any autonomous agent; you'd re-implement the enforcement layer for that agent's runtime.

**Q: What happens if I lose the unlock token file after touching it?**
Nothing — the token is one-shot. Once consumed (by the hook allowing an operation), the token file is deleted. If no matching operation runs, the token stays there indefinitely; you can also `rm` it manually. The token file contains no secrets.

**Q: Can the agent create the unlock token itself?**
Yes, technically — the token is just a file. This is a known limitation documented in `PROTOCOL.md` §9. Mitigations: RULE-017 makes the agent's own token creation itself a policy modification (audit-logged); OS-level ACL denying agent-user write to `~/.claude/.policy-unlock` (roadmap).

**Q: Why Bash for the hooks, not PowerShell?**
Portability. Bash runs cross-platform; the same script works on Linux, macOS, WSL, and Windows via git-bash. PowerShell 5.1 vs 7.x fragmentation on Windows makes portable hooks harder. If you have a Linux/macOS-first team, Bash is definitely the right choice.

**Q: The hooks fail-open on parse error. Isn't that a vulnerability?**
It's a *deliberate trade-off* documented in `SECURITY.md`. Rationale: a parser-fragile hook that fail-closes on any hiccup would render Claude Code unusable on the first protocol/harness mismatch. The alternative — reviewing every parse failure via `audit.jsonl` and hardening incrementally — is preferable.

**Q: How is this different from just prompting Claude to be careful?**
Two things: (1) the hooks are *structural* — the model cannot argue past them, they run in the harness before the tool call executes. (2) the audit log is *persistent* — a policy violation leaves evidence outside the chat.

**Q: What's the maintenance overhead?**
Low. The rules are text; the hooks are ~50 lines of Bash each; CI is one workflow file. Expect ~1 hour per quarter to review `audit.jsonl` patterns and tune the destructive regex.

**Q: We're a big org — how does this scale to 200 devs?**
Fork this repo internally, pin a commit hash, distribute the install via your existing MDM/package manager, and pipe `audit.jsonl` into your SIEM. The protocol itself is stateless per workstation.

**Q: We already use OPA/Kyverno for policy-as-code. Can we integrate?**
The rules aren't OPA-consumable today (they're Markdown, not Rego). A future workstream could translate structural rules (012, 017) into OPA policies + a webhook-based Claude Code hook. Contributions welcome.

**Q: The peer review used LLMs. Isn't that circular?**
Partially — see `PROTOCOL.md` §11 question 6. The mitigation is *cross-model triangulation* (Claude proposed, Gemini + ChatGPT reviewed) plus human final approval on every version bump. The convergence-adoption rule (require ≥2 independent reviewers to flag an issue) reduces single-model bias.
