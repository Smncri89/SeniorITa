---
type: community
cohesion: 0.13
members: 22
---

# Community 135

**Cohesion:** 0.13 - loosely connected
**Members:** 22 nodes

## Members
- [[.test_both_fail_returns_main()]] - code - graphify/tests/test_prs.py
- [[.test_detect_default_branch_decodes_output_as_utf8()]] - code - graphify/tests/test_prs.py
- [[.test_falls_back_to_git_symbolic_ref()]] - code - graphify/tests/test_prs.py
- [[.test_fetch_pr_files_decodes_output_as_utf8()]] - code - graphify/tests/test_prs.py
- [[.test_fetch_worktrees_decodes_output_as_utf8()]] - code - graphify/tests/test_prs.py
- [[.test_fixture_is_cp1252_undecodable()]] - code - graphify/tests/test_prs.py
- [[.test_gh_decodes_output_as_utf8()]] - code - graphify/tests/test_prs.py
- [[.test_gh_returns_empty_dict_falls_back()]] - code - graphify/tests/test_prs.py
- [[.test_gh_returns_main()]] - code - graphify/tests/test_prs.py
- [[.test_git_timeout_returns_main()]] - code - graphify/tests/test_prs.py
- [[Auto-detect the repo's default branch via gh, then git, then fall back to 'main']] - rationale - graphify/graphify/prs.py
- [[Build the configured low-level MCP Server (shared by every transport).      Al]] - rationale - graphify/graphify/serve.py
- [[Guard the fixture's UTF-8 bytes must be undecodable as cp1252, else         th]] - rationale - graphify/tests/test_prs.py
- [[TestDetectDefaultBranch]] - code - graphify/tests/test_prs.py
- [[TestSubprocessOutputEncoding]] - code - graphify/tests/test_prs.py
- [[_build_server()]] - code - graphify/graphify/serve.py
- [[_detect_default_branch()]] - code - graphify/graphify/prs.py
- [[_gh()]] - code - graphify/graphify/prs.py
- [[fetch_pr_files()]] - code - graphify/graphify/prs.py
- [[fetch_prs()]] - code - graphify/graphify/prs.py
- [[gh returns data but with no defaultBranchRef — should still fall back.]] - rationale - graphify/tests/test_prs.py
- [[prs.py reads ghgitclaude output via subprocess.run(text=True). Without an]] - rationale - graphify/tests/test_prs.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_135
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Community 126]]
- 6 edges to [[_COMMUNITY_Community 117]]
- 5 edges to [[_COMMUNITY_Community 98]]
- 2 edges to [[_COMMUNITY_Community 18]]
- 2 edges to [[_COMMUNITY_Community 264]]
- 2 edges to [[_COMMUNITY_Community 263]]
- 1 edge to [[_COMMUNITY_Community 59]]
- 1 edge to [[_COMMUNITY_Community 10]]
- 1 edge to [[_COMMUNITY_Community 15]]
- 1 edge to [[_COMMUNITY_Community 12]]
- 1 edge to [[_COMMUNITY_Community 237]]
- 1 edge to [[_COMMUNITY_Community 238]]
- 1 edge to [[_COMMUNITY_Community 36]]
- 1 edge to [[_COMMUNITY_Community 83]]
- 1 edge to [[_COMMUNITY_Community 230]]

## Top bridge nodes
- [[_build_server()]] - degree 18, connects to 12 communities
- [[fetch_prs()]] - degree 8, connects to 4 communities
- [[_gh()]] - degree 8, connects to 4 communities
- [[fetch_pr_files()]] - degree 6, connects to 4 communities
- [[_detect_default_branch()]] - degree 14, connects to 3 communities