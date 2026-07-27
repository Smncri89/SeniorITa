---
type: community
cohesion: 0.06
members: 73
---

# Community 15

**Cohesion:** 0.06 - loosely connected
**Members:** 73 nodes

## Members
- [[1059 changed_paths=None means a full-corpus rebuild — the queue     must not]] - rationale - graphify/tests/test_watch.py
- [[1886 `--exclude` recorded at extract time must survive into updatewatch]] - rationale - graphify/tests/test_watch.py
- [[2051 follow-up a node whose source_file is a URLvirtual scheme     (gdoc,]] - rationale - graphify/tests/test_watch.py
- [[.__init__()_8]] - code - graphify/graphify/watch.py
- [[.absolute_identity()]] - code - graphify/graphify/watch.py
- [[.identity()]] - code - graphify/graphify/watch.py
- [[.in_watch_root()]] - code - graphify/graphify/watch.py
- [[.is_evicted()]] - code - graphify/graphify/watch.py
- [[.normalize()]] - code - graphify/graphify/watch.py
- [[.rebase_preserved()]] - code - graphify/graphify/watch.py
- [[Append ``changed_paths`` to ``out_dir.pending_changes`` (one per line).]] - rationale - graphify/graphify/watch.py
- [[Assemble the report's work-memory inputs from sibling artifacts.      Reads th]] - rationale - graphify/graphify/report.py
- [[Best-effort nice + memory cap. Called from inline hook scripts.      GRAPHIFY_]] - rationale - graphify/graphify/watch.py
- [[Collapse exact parallel edges by ``(source, target, relation)``, keeping the]] - rationale - graphify/graphify/build.py
- [[Collapse nodes sharing an ``id``, last-writer-wins on attributes.      Mirrors]] - rationale - graphify/graphify/build.py
- [[Concatenate path lists, preserving order and dropping duplicates.      Used to]] - rationale - graphify/graphify/watch.py
- [[Ensure relative rebuild paths have a usable CWD before queuelock setup.]] - rationale - graphify/graphify/watch.py
- [[Generate questions the graph is uniquely positioned to answer.     Based on AM]] - rationale - graphify/graphify/analyze.py
- [[Merge fresh extraction with preserved graph entries and evict stale sources.]] - rationale - graphify/graphify/watch.py
- [[Path_56]] - code
- [[Persist corpus-shaping options under ``out_dir``.      Best effort and non clo]] - rationale - graphify/graphify/watch.py
- [[Re-run AST extraction + build + optional cluster + report for code files. No LLM]] - rationale - graphify/graphify/watch.py
- [[Read + unlink ``out_dir.pending_changes`` and return deduplicated paths.]] - rationale - graphify/graphify/watch.py
- [[Rebase cache-root-relative source paths onto the project root.]] - rationale - graphify/graphify/watch.py
- [[Remap community IDs to maximize overlap with a previous assignment.      Uses]] - rationale - graphify/graphify/cluster.py
- [[Repeated appends across concurrent contenders must dedupe; partial     writes l]] - rationale - graphify/tests/test_watch.py
- [[Resolve source_file values across current and legacy graph roots.]] - rationale - graphify/graphify/watch.py
- [[Return current git HEAD commit hash, or None outside a repo.]] - rationale - graphify/graphify/watch.py
- [[Return plausible absolute locations for a hook-provided changed path.      Git]] - rationale - graphify/graphify/watch.py
- [[Return the effective viz node limit, honoring GRAPHIFY_VIZ_NODE_LIMIT env var.]] - rationale - graphify/graphify/exporters/html.py
- [[Return the persisted ``--exclude`` patterns for this graph, or .]] - rationale - graphify/graphify/watch.py
- [[Return whether rebuilds should honor VCS ignore files (default True).]] - rationale - graphify/graphify/watch.py
- [[Watch watch_path for new or modified files and auto-update the graph.      For]] - rationale - graphify/graphify/watch.py
- [[_StoredSourcePaths]] - code - graphify/graphify/watch.py
- [[_apply_resource_limits()]] - code - graphify/graphify/watch.py
- [[_canonical_graph_for_compare()]] - code - graphify/graphify/watch.py
- [[_canonical_topology_for_compare()]] - code - graphify/graphify/watch.py
- [[_changed_path_candidates()]] - code - graphify/graphify/watch.py
- [[_drain_pending()]] - code - graphify/graphify/watch.py
- [[_git_head()_1]] - code - graphify/graphify/watch.py
- [[_has_non_code()]] - code - graphify/graphify/watch.py
- [[_is_relative_to()]] - code - graphify/graphify/watch.py
- [[_is_remote_source()]] - code - graphify/graphify/watch.py
- [[_json_text()]] - code - graphify/graphify/watch.py
- [[_merge_changed_paths()]] - code - graphify/graphify/watch.py
- [[_node_community_map()_1]] - code - graphify/graphify/watch.py
- [[_queue_pending writes one path per line; _drain_pending reads + unlinks     and]] - rationale - graphify/tests/test_watch.py
- [[_queue_pending()]] - code - graphify/graphify/watch.py
- [[_read_build_excludes()]] - code - graphify/graphify/watch.py
- [[_read_build_gitignore()]] - code - graphify/graphify/watch.py
- [[_rebase_relative_source_files()]] - code - graphify/graphify/watch.py
- [[_rebuild_code()]] - code - graphify/graphify/watch.py
- [[_reconcile_existing_graph()]] - code - graphify/graphify/watch.py
- [[_relativize_source_files()]] - code - graphify/graphify/watch.py
- [[_report_for_compare()]] - code - graphify/graphify/watch.py
- [[_report_root_label()]] - code - graphify/graphify/watch.py
- [[_stabilize_rebuild_cwd()]] - code - graphify/graphify/watch.py
- [[_topology_from_graph()]] - code - graphify/graphify/watch.py
- [[_viz_node_limit()]] - code - graphify/graphify/exporters/html.py
- [[_write_build_config()]] - code - graphify/graphify/watch.py
- [[dedupe_edges()]] - code - graphify/graphify/build.py
- [[dedupe_nodes()]] - code - graphify/graphify/build.py
- [[load_learning_for_report()]] - code - graphify/graphify/report.py
- [[remap_communities_to_previous()]] - code - graphify/graphify/cluster.py
- [[suggest_questions()]] - code - graphify/graphify/analyze.py
- [[test_drain_pending_dedupes_and_skips_blank_lines()]] - code - graphify/tests/test_watch.py
- [[test_queue_and_drain_pending_round_trip()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_full_corpus_skips_pending_queue()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_preserves_remote_source_across_repeated_updates()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_honors_persisted_excludes()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_honors_persisted_no_gitignore()]] - code - graphify/tests/test_watch.py
- [[watch()]] - code - graphify/graphify/watch.py
- [[watch.py]] - code - graphify/graphify/watch.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_15
SORT file.name ASC
```

## Connections to other communities
- 60 edges to [[_COMMUNITY_Community 7]]
- 22 edges to [[_COMMUNITY_Community 12]]
- 7 edges to [[_COMMUNITY_Community 127]]
- 6 edges to [[_COMMUNITY_Community 77]]
- 6 edges to [[_COMMUNITY_Community 59]]
- 6 edges to [[_COMMUNITY_Community 19]]
- 5 edges to [[_COMMUNITY_Community 114]]
- 5 edges to [[_COMMUNITY_Community 18]]
- 5 edges to [[_COMMUNITY_Community 180]]
- 4 edges to [[_COMMUNITY_Community 10]]
- 4 edges to [[_COMMUNITY_Community 34]]
- 4 edges to [[_COMMUNITY_Community 123]]
- 3 edges to [[_COMMUNITY_Community 32]]
- 3 edges to [[_COMMUNITY_Community 36]]
- 2 edges to [[_COMMUNITY_Community 209]]
- 2 edges to [[_COMMUNITY_Community 35]]
- 2 edges to [[_COMMUNITY_Community 96]]
- 2 edges to [[_COMMUNITY_Community 1]]
- 2 edges to [[_COMMUNITY_Community 24]]
- 2 edges to [[_COMMUNITY_Community 27]]
- 2 edges to [[_COMMUNITY_Community 136]]
- 1 edge to [[_COMMUNITY_Community 98]]
- 1 edge to [[_COMMUNITY_Community 135]]
- 1 edge to [[_COMMUNITY_Community 44]]
- 1 edge to [[_COMMUNITY_Community 76]]
- 1 edge to [[_COMMUNITY_Community 277]]
- 1 edge to [[_COMMUNITY_Community 40]]
- 1 edge to [[_COMMUNITY_Community 53]]

## Top bridge nodes
- [[watch.py]] - degree 58, connects to 19 communities
- [[_rebuild_code()]] - degree 101, connects to 16 communities
- [[suggest_questions()]] - degree 16, connects to 7 communities
- [[load_learning_for_report()]] - degree 9, connects to 5 communities
- [[watch()]] - degree 13, connects to 3 communities