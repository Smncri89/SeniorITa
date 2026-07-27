---
type: community
cohesion: 0.04
members: 83
---

# Community 12

**Cohesion:** 0.04 - loosely connected
**Members:** 83 nodes

## Members
- [[.__init__()_3]] - code - graphify/graphify/cli.py
- [[.mark()]] - code - graphify/graphify/cli.py
- [[.total()]] - code - graphify/graphify/cli.py
- [[A path inside the configured output dir, e.g. ``out_path(cache)``.      ``Pa]] - rationale - graphify/graphify/paths.py
- [[All-default labels → no backup (not curated).]] - rationale - graphify/tests/test_export.py
- [[Atomically claim a one-time strict block for this session. Returns True only]] - rationale - graphify/graphify/cli.py
- [[Atomically write ``obj`` as JSON to ``path``, streaming the encode into the]] - rationale - graphify/graphify/paths.py
- [[Changed graph.json on same day overwrites the existing backup in place.]] - rationale - graphify/tests/test_export.py
- [[Clone a GitHub repo to a local cache dir and return the path.      Clones into]] - rationale - graphify/graphify/cli.py
- [[Drop nodesedgeshyperedges owned by ``stale_sources`` from graph.json     in p]] - rationale - graphify/graphify/cli.py
- [[Export graph as an SVG file using matplotlib + spring layout.      Lightweight]] - rationale - graphify/graphify/export.py
- [[GRAPHIFY_NO_BACKUP=1 disables backup entirely.]] - rationale - graphify/tests/test_export.py
- [[Guard the strict deny only block a read of a file the graph actually indexes.]] - rationale - graphify/graphify/cli.py
- [[Manifest-safe files dict only stamp semantic files that actually     produced]] - rationale - graphify/graphify/cli.py
- [[No graph.json → no backup.]] - rationale - graphify/tests/test_export.py
- [[Path_6]] - code
- [[Path_38]] - code
- [[Pick a path endpoint from a _score_nodes result, preferring full-token matches.]] - rationale - graphify/graphify/serve.py
- [[Print per-stage wall-clock timings to stderr when --timing is set (1490).]] - rationale - graphify/graphify/cli.py
- [[Record that graphify oriented the agent recently, next to the queried graph.]] - rationale - graphify/graphify/cli.py
- [[Reject oversized graph files before parsing (CLI exit-on-fail flavor).      De]] - rationale - graphify/graphify/cli.py
- [[Relabel colliding-basename file nodes on a raw node-dict list, in place     (2]] - rationale - graphify/graphify/build.py
- [[Remove all nodes for repo_tag from the global graph. Returns count removed.]] - rationale - graphify/graphify/global_graph.py
- [[Remove the internal ``_partial`` marker from every item in ``result``.      Ca]] - rationale - graphify/graphify/llm.py
- [[Resolve strict mode GRAPHIFY_HOOK_STRICT env overrides the baked-in flag     (]] - rationale - graphify/graphify/cli.py
- [[Return a unique, human-meaningful repo tag per input graph for merge-graphs.]] - rationale - graphify/graphify/build.py
- [[Return the current git HEAD commit hash, or None if not in a git repo.]] - rationale - graphify/graphify/export.py
- [[Return the manifest repos dict.]] - rationale - graphify/graphify/global_graph.py
- [[Return user-facing accepted API-key variable names.]] - rationale - graphify/graphify/llm.py
- [[Same content on same day returns existing backup dir without re-copying.]] - rationale - graphify/tests/test_export.py
- [[Shell-agnostic PreToolUse guard (522).      Reads the tool-call JSON from std]] - rationale - graphify/graphify/cli.py
- [[Snapshot graph artifacts to a dated subfolder before an overwrite.      Trigge]] - rationale - graphify/graphify/export.py
- [[Structural safety check for a custom-provider base_url.      A custom provider]] - rationale - graphify/graphify/llm.py
- [[True if a queryexplainpath ran within GRAPHIFY_HOOK_STRICT_TTL (default     1]] - rationale - graphify/graphify/cli.py
- [[_StageTimer]] - code - graphify/graphify/cli.py
- [[_clone_repo()]] - code - graphify/graphify/cli.py
- [[_custom_providers_path()]] - code - graphify/graphify/llm.py
- [[_default_graph_path()]] - code - graphify/graphify/cli.py
- [[_enforce_graph_size_cap_or_exit()]] - code - graphify/graphify/cli.py
- [[_file_hash()]] - code - graphify/graphify/global_graph.py
- [[_format_backend_env_keys()]] - code - graphify/graphify/llm.py
- [[_git_head()]] - code - graphify/graphify/export.py
- [[_hook_strict_enabled()]] - code - graphify/graphify/cli.py
- [[_load_manifest()]] - code - graphify/graphify/global_graph.py
- [[_mark_session_denied()]] - code - graphify/graphify/cli.py
- [[_pick_scored_endpoint()]] - code - graphify/graphify/serve.py
- [[_prune_graph_json_sources()]] - code - graphify/graphify/cli.py
- [[_query_stamp_fresh()]] - code - graphify/graphify/cli.py
- [[_reenter_main()]] - code - graphify/graphify/cli.py
- [[_run_hook_guard()]] - code - graphify/graphify/cli.py
- [[_save_global_graph()]] - code - graphify/graphify/global_graph.py
- [[_save_manifest()]] - code - graphify/graphify/global_graph.py
- [[_stamped_manifest_files()]] - code - graphify/graphify/cli.py
- [[_strip_partial_markers()]] - code - graphify/graphify/llm.py
- [[_target_is_indexed()]] - code - graphify/graphify/cli.py
- [[_touch_query_stamp()]] - code - graphify/graphify/cli.py
- [[backup_if_protected()]] - code - graphify/graphify/export.py
- [[cli.py]] - code - graphify/graphify/cli.py
- [[disambiguate_file_labels_in_nodes()]] - code - graphify/graphify/build.py
- [[dispatch_command()]] - code - graphify/graphify/cli.py
- [[distinct_repo_tags()]] - code - graphify/graphify/build.py
- [[global_graph.py]] - code - graphify/graphify/global_graph.py
- [[global_list()]] - code - graphify/graphify/global_graph.py
- [[global_path()]] - code - graphify/graphify/global_graph.py
- [[global_remove()]] - code - graphify/graphify/global_graph.py
- [[graph.json + .graphify_semantic_marker → backup taken.]] - rationale - graphify/tests/test_export.py
- [[graph.json + non-default label in .graphify_labels.json → backup taken.]] - rationale - graphify/tests/test_export.py
- [[graph.json present but no sentinel and no curated labels → no backup.]] - rationale - graphify/tests/test_export.py
- [[graphify command dispatch — every non-install subcommand.  Extracted verbatim]] - rationale - graphify/graphify/cli.py
- [[out_path()]] - code - graphify/graphify/paths.py
- [[provider_base_url_ok()]] - code - graphify/graphify/llm.py
- [[test_backup_curated_labels()]] - code - graphify/tests/test_export.py
- [[test_backup_default_labels_only()]] - code - graphify/tests/test_export.py
- [[test_backup_env_disable()]] - code - graphify/tests/test_export.py
- [[test_backup_no_graph_json()]] - code - graphify/tests/test_export.py
- [[test_backup_no_markers()]] - code - graphify/tests/test_export.py
- [[test_backup_same_day_changed_content()]] - code - graphify/tests/test_export.py
- [[test_backup_same_day_no_accumulation()]] - code - graphify/tests/test_export.py
- [[test_backup_semantic_marker()]] - code - graphify/tests/test_export.py
- [[test_strict_enabled_env_precedence()]] - code - graphify/tests/test_hook_strict.py
- [[test_strip_partial_markers_removes_internal_key()]] - code - graphify/tests/test_partial_cache.py
- [[to_svg()]] - code - graphify/graphify/export.py
- [[write_json_atomic()]] - code - graphify/graphify/paths.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_12
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_Community 15]]
- 20 edges to [[_COMMUNITY_Community 81]]
- 20 edges to [[_COMMUNITY_Community 19]]
- 11 edges to [[_COMMUNITY_Community 25]]
- 10 edges to [[_COMMUNITY_Community 76]]
- 8 edges to [[_COMMUNITY_Community 4]]
- 8 edges to [[_COMMUNITY_Community 34]]
- 8 edges to [[_COMMUNITY_Community 39]]
- 7 edges to [[_COMMUNITY_Community 57]]
- 6 edges to [[_COMMUNITY_Community 59]]
- 6 edges to [[_COMMUNITY_Community 48]]
- 6 edges to [[_COMMUNITY_Community 36]]
- 5 edges to [[_COMMUNITY_Community 95]]
- 5 edges to [[_COMMUNITY_Community 168]]
- 5 edges to [[_COMMUNITY_Community 24]]
- 5 edges to [[_COMMUNITY_Community 58]]
- 4 edges to [[_COMMUNITY_Community 219]]
- 4 edges to [[_COMMUNITY_Community 18]]
- 4 edges to [[_COMMUNITY_Community 180]]
- 4 edges to [[_COMMUNITY_Community 90]]
- 4 edges to [[_COMMUNITY_Community 20]]
- 4 edges to [[_COMMUNITY_Community 53]]
- 3 edges to [[_COMMUNITY_Community 1]]
- 3 edges to [[_COMMUNITY_Community 119]]
- 3 edges to [[_COMMUNITY_Community 30]]
- 3 edges to [[_COMMUNITY_Community 170]]
- 2 edges to [[_COMMUNITY_Community 47]]
- 2 edges to [[_COMMUNITY_Community 218]]
- 2 edges to [[_COMMUNITY_Community 235]]
- 2 edges to [[_COMMUNITY_Community 10]]
- 2 edges to [[_COMMUNITY_Community 121]]
- 2 edges to [[_COMMUNITY_Community 35]]
- 2 edges to [[_COMMUNITY_Community 179]]
- 2 edges to [[_COMMUNITY_Community 285]]
- 2 edges to [[_COMMUNITY_Community 66]]
- 2 edges to [[_COMMUNITY_Community 51]]
- 2 edges to [[_COMMUNITY_Community 31]]
- 2 edges to [[_COMMUNITY_Community 96]]
- 2 edges to [[_COMMUNITY_Community 111]]
- 2 edges to [[_COMMUNITY_Community 27]]
- 2 edges to [[_COMMUNITY_Community 88]]
- 2 edges to [[_COMMUNITY_Community 141]]
- 2 edges to [[_COMMUNITY_Community 142]]
- 2 edges to [[_COMMUNITY_Community 33]]
- 2 edges to [[_COMMUNITY_Community 52]]
- 2 edges to [[_COMMUNITY_Community 37]]
- 2 edges to [[_COMMUNITY_Community 117]]
- 2 edges to [[_COMMUNITY_Community 79]]
- 2 edges to [[_COMMUNITY_Community 276]]
- 2 edges to [[_COMMUNITY_Community 17]]
- 2 edges to [[_COMMUNITY_Community 118]]
- 2 edges to [[_COMMUNITY_Community 67]]
- 2 edges to [[_COMMUNITY_Community 62]]
- 2 edges to [[_COMMUNITY_Community 7]]
- 2 edges to [[_COMMUNITY_Community 21]]
- 2 edges to [[_COMMUNITY_Community 87]]
- 2 edges to [[_COMMUNITY_Community 44]]
- 1 edge to [[_COMMUNITY_Community 77]]
- 1 edge to [[_COMMUNITY_Community 8]]
- 1 edge to [[_COMMUNITY_Community 135]]
- 1 edge to [[_COMMUNITY_Community 41]]
- 1 edge to [[_COMMUNITY_Community 334]]
- 1 edge to [[_COMMUNITY_Community 89]]
- 1 edge to [[_COMMUNITY_Community 230]]
- 1 edge to [[_COMMUNITY_Community 68]]
- 1 edge to [[_COMMUNITY_Community 98]]
- 1 edge to [[_COMMUNITY_Community 156]]

## Top bridge nodes
- [[cli.py]] - degree 118, connects to 52 communities
- [[dispatch_command()]] - degree 114, connects to 51 communities
- [[write_json_atomic()]] - degree 16, connects to 5 communities
- [[out_path()]] - degree 11, connects to 4 communities
- [[_format_backend_env_keys()]] - degree 9, connects to 4 communities