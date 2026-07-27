---
type: community
cohesion: 0.06
members: 53
---

# Community 33

**Cohesion:** 0.06 - loosely connected
**Members:** 53 nodes

## Members
- [[2076 review with --json-schema the CLI puts the constrained object in     `st]] - rationale - graphify/tests/test_claude_cli_backend.py
- [[--system-prompt must NOT be used the CLI ignores its 'raw JSON only'     direc]] - rationale - graphify/tests/test_claude_cli_backend.py
- [[A probe that fails to run is treated as unsupported (safe fallback) and     cac]] - rationale - graphify/tests/test_claude_cli_backend.py
- [[Call Claude via the locally-installed Claude Code CLI (`claude -p`).      Rout]] - rationale - graphify/graphify/llm.py
- [[Estimate USD cost for a given token count using published pricing.]] - rationale - graphify/graphify/llm.py
- [[Honour GRAPHIFY_API_TIMEOUT env var override, else use default (seconds).]] - rationale - graphify/graphify/llm.py
- [[If `claude.cmd` is somehow unavailable but `claude` resolves     (e.g. WSL-styl]] - rationale - graphify/tests/test_claude_cli_backend.py
- [[If neither `claude.cmd` nor `claude` are on PATH on Windows,     raise the stan]] - rationale - graphify/tests/test_claude_cli_backend.py
- [[Older CLIs without --json-schema must not receive the flag (it would be     an]] - rationale - graphify/tests/test_claude_cli_backend.py
- [[On Windows, npm installs `claude.ps1` alongside `claude.cmd`.     `CreateProces]] - rationale - graphify/tests/test_claude_cli_backend.py
- [[On non-Windows platforms, behaviour is unchanged bare `claude`     is passed t]] - rationale - graphify/tests/test_claude_cli_backend.py
- [[Return True if this Claude Code CLI accepts ``--json-schema``.      Structured]] - rationale - graphify/graphify/llm.py
- [[Tests for the `claude-cli` backend (855856).  Mocks subprocess.run + shutil]] - rationale - graphify/tests/test_claude_cli_backend.py
- [[The untrusted_source guardrails from _extraction_system must survive     the]] - rationale - graphify/tests/test_claude_cli_backend.py
- [[The full extraction schema, an explicit imperative, and the source must     all]] - rationale - graphify/tests/test_claude_cli_backend.py
- [[When errors='replace' is set, non-UTF-8 bytes in stderr produce replacement]] - rationale - graphify/tests/test_llm_backends.py
- [[When the CLI advertises --json-schema, it is passed with a schema that     pins]] - rationale - graphify/tests/test_claude_cli_backend.py
- [[_call_claude_cli()]] - code - graphify/graphify/llm.py
- [[_claude_cli_supports_json_schema()]] - code - graphify/graphify/llm.py
- [[_no_window_kwargs()]] - code - graphify/graphify/llm.py
- [[_resolve_api_timeout()]] - code - graphify/graphify/llm.py
- [[estimate_cost()]] - code - graphify/graphify/llm.py
- [[fake_claude()]] - code - graphify/tests/test_claude_cli_backend.py
- [[subprocess kwargs that suppress the console window claude.cmd would     otherwi]] - rationale - graphify/graphify/llm.py
- [[test_backend_registered_with_zero_cost()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_call_claude_cli_tolerates_non_utf8_in_stderr()]] - code - graphify/tests/test_llm_backends.py
- [[test_claude_cli_backend.py]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_claude_cli_extraction_honours_timeout()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_estimate_cost_azure_no_keyerror()]] - code - graphify/tests/test_llm_backends.py
- [[test_extraction_instructions_ride_in_user_turn()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_finish_reason_length_on_max_tokens()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_json_schema_flag_absent_when_cli_lacks_it()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_json_schema_flag_added_when_cli_supports_it()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_no_session_persistence_flag_in_subprocess()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_no_system_prompt_flag_in_subprocess()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_non_windows_uses_bare_claude()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_prefers_structured_output_over_prose_result()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_raises_on_garbage_envelope()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_raises_on_nonzero_exit()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_raises_when_cli_missing()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_resolve_api_timeout_default()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_resolve_api_timeout_env_override()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_resolve_api_timeout_ignores_invalid()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_resolve_api_timeout_ignores_nonpositive()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_returns_parsed_nodes_and_edges()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_supports_json_schema_detects_flag_in_help()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_supports_json_schema_false_and_cached_on_probe_error()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_supports_json_schema_false_when_flag_absent()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_token_accounting_includes_cache()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_user_turn_preserves_untrusted_source_guardrails()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_windows_falls_back_to_bare_claude_when_cmd_missing()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_windows_prefers_claude_cmd_over_bare_claude()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_windows_raises_when_neither_cmd_nor_bare_claude_present()]] - code - graphify/tests/test_claude_cli_backend.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_33
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Community 58]]
- 5 edges to [[_COMMUNITY_Community 89]]
- 5 edges to [[_COMMUNITY_Community 38]]
- 5 edges to [[_COMMUNITY_Community 16]]
- 4 edges to [[_COMMUNITY_Community 78]]
- 2 edges to [[_COMMUNITY_Community 12]]
- 2 edges to [[_COMMUNITY_Community 39]]
- 1 edge to [[_COMMUNITY_Community 301]]
- 1 edge to [[_COMMUNITY_Community 20]]
- 1 edge to [[_COMMUNITY_Community 119]]

## Top bridge nodes
- [[_call_claude_cli()]] - degree 37, connects to 7 communities
- [[test_claude_cli_backend.py]] - degree 33, connects to 4 communities
- [[_resolve_api_timeout()]] - degree 10, connects to 4 communities
- [[estimate_cost()]] - degree 6, connects to 2 communities
- [[_no_window_kwargs()]] - degree 5, connects to 2 communities