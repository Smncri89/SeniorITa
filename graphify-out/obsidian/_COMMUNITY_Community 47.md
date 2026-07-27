---
type: community
cohesion: 0.05
members: 49
---

# Community 47

**Cohesion:** 0.05 - loosely connected
**Members:** 49 nodes

## Members
- [[F4 query CLI must refuse to parse a graph.json that exceeds the cap.]] - rationale - graphify/tests/test_query_cli.py
- [[--timing prints per-stage `graphify timing` lines to stderr (1490); omitting]] - rationale - graphify/tests/test_extract_cli.py
- [[A pre-fix ~.ampskillsgraphify install is removed on the next install.]] - rationale - graphify/tests/test_install.py
- [[A single directed `calls` edge on an (on-disk) undirected graph.json,      the]] - rationale - graphify/tests/test_query_cli.py
- [[Console entry point. Wraps the CLI so that when a downstream consumer closes]] - rationale - graphify/graphify/__main__.py
- [[Global `graphify antigravity install` must write to ~.geminiconfigskills (1]] - rationale - graphify/tests/test_install.py
- [[Global `graphify antigravity uninstall` must remove from ~.geminiconfigskills]] - rationale - graphify/tests/test_install.py
- [[Handle a downstream reader that closed the pipe early. Redirect stdout to     d]] - rationale - graphify/graphify/__main__.py
- [[Project-scope amp install lands in .agentsskills, an Amp project search root.]] - rationale - graphify/tests/test_install.py
- [[Project-scoped install via CLI prints a git add hint.]] - rationale - graphify/tests/test_codebuddy.py
- [[Same edge, seeded from the caller side — must stay correct too.]] - rationale - graphify/tests/test_query_cli.py
- [[Tests for graphify query CLI context filtering.]] - rationale - graphify/tests/test_query_cli.py
- [[The user-scope `graphify uninstall` enumeration removes the amp skill.]] - rationale - graphify/tests/test_install.py
- [[_silence_broken_pipe()]] - code - graphify/graphify/__main__.py
- [[_write_calls_graph()]] - code - graphify/tests/test_query_cli.py
- [[_write_graph()_6]] - code - graphify/tests/test_query_cli.py
- [[`graphify --help` must list codebuddy in the platform list and per-platform sect]] - rationale - graphify/tests/test_codebuddy.py
- [[`graphify amp install` (user scope) must drop the skill into an Amp search]] - rationale - graphify/tests/test_install.py
- [[`graphify amp uninstall` removes the user-scope skill and AGENTS.md section.]] - rationale - graphify/tests/test_install.py
- [[`graphify query` must render `calls` edges caller-callee regardless of     whi]] - rationale - graphify/tests/test_query_cli.py
- [[main()]] - code - graphify/graphify/__main__.py
- [[parametrize_15]] - code
- [[test_amp_install_cleans_legacy_amp_skills_dir()]] - code - graphify/tests/test_install.py
- [[test_amp_project_install_lands_in_dot_agents()]] - code - graphify/tests/test_install.py
- [[test_amp_user_install_lands_in_config_agents()]] - code - graphify/tests/test_install.py
- [[test_amp_user_uninstall_removes_skill_and_agents()]] - code - graphify/tests/test_install.py
- [[test_antigravity_global_install_writes_gemini_config_skills()]] - code - graphify/tests/test_install.py
- [[test_antigravity_global_uninstall_removes_gemini_config_skill()]] - code - graphify/tests/test_install.py
- [[test_antigravity_install_project_writes_project_skill()]] - code - graphify/tests/test_install.py
- [[test_antigravity_uninstall_project_removes_project_skill_only()]] - code - graphify/tests/test_install.py
- [[test_claude_subcommand_project_install_and_uninstall_are_project_scoped()]] - code - graphify/tests/test_install.py
- [[test_codebuddy_in_main_help_text()]] - code - graphify/tests/test_codebuddy.py
- [[test_codebuddy_install_hint_git_add()]] - code - graphify/tests/test_codebuddy.py
- [[test_codex_subcommand_project_install_and_uninstall_are_project_scoped()]] - code - graphify/tests/test_install.py
- [[test_diagnose_multigraph_cli_usage_errors()]] - code - graphify/tests/test_multigraph_diagnostics.py
- [[test_extract_timing_flag_emits_stage_timings()]] - code - graphify/tests/test_extract_cli.py
- [[test_install_help_does_not_install_default()]] - code - graphify/tests/test_install.py
- [[test_install_positional_platform_opencode()]] - code - graphify/tests/test_install.py
- [[test_install_project_claude_writes_project_scope()]] - code - graphify/tests/test_install.py
- [[test_install_project_codex_writes_skill_and_agents()]] - code - graphify/tests/test_install.py
- [[test_query_cli.py]] - code - graphify/tests/test_query_cli.py
- [[test_query_cli_explicit_context_filter()]] - code - graphify/tests/test_query_cli.py
- [[test_query_cli_heuristic_context_filter()]] - code - graphify/tests/test_query_cli.py
- [[test_query_cli_preserves_calls_direction_when_seeded_on_callee()]] - code - graphify/tests/test_query_cli.py
- [[test_query_cli_preserves_calls_direction_when_seeded_on_caller()]] - code - graphify/tests/test_query_cli.py
- [[test_query_cli_rejects_oversized_graph()]] - code - graphify/tests/test_query_cli.py
- [[test_uninstall_all_removes_amp_user_skill()]] - code - graphify/tests/test_install.py
- [[test_uninstall_project_removes_project_skill_only()]] - code - graphify/tests/test_install.py
- [[test_uninstall_project_without_platform_removes_project_installs()]] - code - graphify/tests/test_install.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_47
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_Community 8]]
- 10 edges to [[_COMMUNITY_Community 30]]
- 9 edges to [[_COMMUNITY_Community 42]]
- 9 edges to [[_COMMUNITY_Community 160]]
- 7 edges to [[_COMMUNITY_Community 86]]
- 6 edges to [[_COMMUNITY_Community 48]]
- 5 edges to [[_COMMUNITY_Community 22]]
- 4 edges to [[_COMMUNITY_Community 4]]
- 2 edges to [[_COMMUNITY_Community 12]]
- 2 edges to [[_COMMUNITY_Community 63]]
- 2 edges to [[_COMMUNITY_Community 148]]
- 1 edge to [[_COMMUNITY_Community 102]]
- 1 edge to [[_COMMUNITY_Community 128]]
- 1 edge to [[_COMMUNITY_Community 270]]
- 1 edge to [[_COMMUNITY_Community 17]]

## Top bridge nodes
- [[main()]] - degree 83, connects to 15 communities
- [[test_query_cli.py]] - degree 9, connects to 1 community
- [[_silence_broken_pipe()]] - degree 3, connects to 1 community
- [[test_codebuddy_in_main_help_text()]] - degree 3, connects to 1 community
- [[test_codebuddy_install_hint_git_add()]] - degree 3, connects to 1 community