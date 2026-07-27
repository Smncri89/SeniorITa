---
type: community
cohesion: 0.02
members: 100
---

# Community 7

**Cohesion:** 0.02 - loosely connected
**Members:** 100 nodes

## Members
- [[09b33b7 guard a doc with NO semantic layer still gets the AST     quick-scan]] - rationale - graphify/tests/test_watch.py
- [[1007 graphify update (_rebuild_code with no changed_paths) must remove     no]] - rationale - graphify/tests/test_watch.py
- [[1116 graphify update (_rebuild_code with no changed_paths) must prune a     s]] - rationale - graphify/tests/test_watch.py
- [[1118 backward-compat a graph.json built before 1116 has no `_origin`     mar]] - rationale - graphify/tests/test_watch.py
- [[1348 git-hook paths are repo-root-relative even when the graph root is a subdi]] - rationale - graphify/tests/test_watch.py
- [[1755 AST-only updates must not drop semantic hyperedges whose members survive.]] - rationale - graphify/tests/test_watch.py
- [[1808 `graphify update`  _rebuild_code must forward community_labels to     t]] - rationale - graphify/tests/test_watch.py
- [[1837 after an initial build, a plain `graphify update` (full re-scan, no]] - rationale - graphify/tests/test_watch.py
- [[1865 AST-only updates must not evict semantic edges whose source_file     is]] - rationale - graphify/tests/test_watch.py
- [[1880 `graphify update` must not emit 0 nodes (and then refuse to     overwrit]] - rationale - graphify/tests/test_watch.py
- [[1915 a full _rebuild_code must not AST-quick-scan a doc whose semantic     (L]] - rationale - graphify/tests/test_watch.py
- [[1915 a graph already bloated by the bug (semantic doc nodes PLUS stale     _o]] - rationale - graphify/tests/test_watch.py
- [[1915 an incremental rebuild whose change set includes a semantic-backed     d]] - rationale - graphify/tests/test_watch.py
- [[1954 a doc represented ONLY by conceptrationale nodes (no     file_type==do]] - rationale - graphify/tests/test_watch.py
- [[1954 incremental analogue — a conceptrationale-only semantic doc     must no]] - rationale - graphify/tests/test_watch.py
- [[2014 a doc represented ONLY by code-typed semantic nodes (symbols     surface]] - rationale - graphify/tests/test_watch.py
- [[2051 a full `graphify update` must evict semantic nodes whose non-AST     sou]] - rationale - graphify/tests/test_watch.py
- [[2056 an incremental rebuild whose change set names a file that exists but]] - rationale - graphify/tests/test_watch.py
- [[777 ``.graphify_root`` stores the user-supplied path (``.``), not the     res]] - rationale - graphify/tests/test_watch.py
- [[A full rebuild of a subdirectory must not prune graph data outside it.]] - rationale - graphify/tests/test_watch.py
- [[A hook-style rename list may contain only the destination path.]] - rationale - graphify/tests/test_watch.py
- [[A rejected candidate keeps the marker paired with the existing graph.]] - rationale - graphify/tests/test_watch.py
- [[An incremental rebuild must not treat .foo.py as a deleted live source.]] - rationale - graphify/tests/test_watch.py
- [[Build a code-only graph, then add guide.md represented ONLY semantically.]] - rationale - graphify/tests/test_watch.py
- [[Check for pending semantic update flag and notify the user if set.      Cron-s]] - rationale - graphify/graphify/watch.py
- [[Crossing the viz node limit must not leave the project with no graph.html.]] - rationale - graphify/tests/test_watch.py
- [[Deleting the final code file must reconcile the existing graph.]] - rationale - graphify/tests/test_watch.py
- [[Destination-only rename reconciliation also covers AST-backed docs.]] - rationale - graphify/tests/test_watch.py
- [[Detached hooks can inherit a CWD that no longer exists.      Without GRAPHIFY_]] - rationale - graphify/tests/test_watch.py
- [[Empty change set must not create an empty .pending_changes file.]] - rationale - graphify/tests/test_watch.py
- [[Fail-closed eviction a file that leaves the scan corpus (newly ignored)     bu]] - rationale - graphify/tests/test_watch.py
- [[GRAPHIFY_REPO_ROOT lets detached hook rebuilds recover from a deleted CWD.]] - rationale - graphify/tests/test_watch.py
- [[Like ``_seed_semantic_doc_graph``, but guide.md's semantic layer is     ONLY co]] - rationale - graphify/tests/test_watch.py
- [[Persisted source paths keep their meaning when invocation style changes.]] - rationale - graphify/tests/test_watch.py
- [[Pre-rebase subdirectory graphs stored source_file relative to watch_root.]] - rationale - graphify/tests/test_watch.py
- [[Tests for watch.py - file watcher helpers (no watchdog required).]] - rationale - graphify/tests/test_watch.py
- [[The fail-closed preserve must not weaken true-deletion eviction once the     e]] - rationale - graphify/tests/test_watch.py
- [[When the caller supplies an absolute path, ``.graphify_root`` stores     that a]] - rationale - graphify/tests/test_watch.py
- [[Write a flag file and print a notification (fallback for non-code-only corpora).]] - rationale - graphify/graphify/watch.py
- [[_add_unrelated_semantic_pair()]] - code - graphify/tests/test_watch.py
- [[_merge_changed_paths preserves first-seen order and drops dupes.]] - rationale - graphify/tests/test_watch.py
- [[_notify_only()]] - code - graphify/graphify/watch.py
- [[_seed_semantic_doc_graph()]] - code - graphify/tests/test_watch.py
- [[_seed_semantic_doc_graph_code_only()]] - code - graphify/tests/test_watch.py
- [[_seed_semantic_doc_graph_concept_only()]] - code - graphify/tests/test_watch.py
- [[_watchdog_available()]] - code - graphify/tests/test_watch.py
- [[check_update never removes the needs_update flag (clearing is LLM's job).]] - rationale - graphify/tests/test_watch.py
- [[check_update returns True and is silent when needs_update flag is absent.]] - rationale - graphify/tests/test_watch.py
- [[check_update returns True and prints notification when flag exists.]] - rationale - graphify/tests/test_watch.py
- [[check_update()]] - code - graphify/graphify/watch.py
- [[parametrize_25]] - code
- [[test_check_update_does_not_clear_flag()]] - code - graphify/tests/test_watch.py
- [[test_check_update_no_flag_returns_true()]] - code - graphify/tests/test_watch.py
- [[test_check_update_with_flag_returns_true_and_prints()]] - code - graphify/tests/test_watch.py
- [[test_graphify_root_preserves_absolute_when_user_supplied()]] - code - graphify/tests/test_watch.py
- [[test_graphify_root_preserves_relative_when_invoked_with_relative_path()]] - code - graphify/tests/test_watch.py
- [[test_merge_changed_paths_dedupes_in_order()]] - code - graphify/tests/test_watch.py
- [[test_notify_only_creates_flag()]] - code - graphify/tests/test_watch.py
- [[test_notify_only_creates_flag_dir()]] - code - graphify/tests/test_watch.py
- [[test_notify_only_idempotent()]] - code - graphify/tests/test_watch.py
- [[test_queue_pending_noop_on_empty_list()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_accepts_repo_relative_changed_path_for_subdir_root()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_code_only_semantic_doc_not_double_represented_on_full_rebuild()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_concept_only_semantic_doc_not_double_represented_on_full_rebuild()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_deleted_cwd_uses_graphify_repo_root()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_deleted_cwd_without_repo_root_returns_false()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_does_not_update_root_marker_when_write_is_refused()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_evicts_nodes_from_deleted_files()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_evicts_removed_symbol_from_surviving_file()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_evicts_semantic_nodes_from_deleted_non_ast_source()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_incremental_preserves_concept_only_semantic_doc_nodes_and_edges()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_incremental_preserves_present_non_ast_source()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_incremental_preserves_semantic_doc_nodes_and_edges()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_is_idempotent_when_cluster_ids_flap()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_keeps_a_visualization_when_over_the_viz_cap()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_normalizes_preserved_source_paths()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_polluted_graph_self_heals_on_full_rebuild()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_preserves_hyperedges_for_rebuilt_surviving_source()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_preserves_nodes_from_excluded_but_alive_file()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_preserves_semantic_edges_from_reextracted_doc()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_preupgrade_marker_less_node_one_cycle_lag()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_prunes_final_deleted_file()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_prunes_legacy_watch_relative_subdir_source()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_prunes_renamed_ast_backed_document()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_prunes_renamed_source_not_listed_by_hook()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_quick_scans_doc_without_semantic_nodes()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_semantic_doc_not_double_represented_on_full_rebuild()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_skips_cluster_when_topology_unchanged()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_still_evicts_when_excluded_file_is_also_deleted()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_subdir_preserves_outside_ast_nodes()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_subdir_survives_absolute_to_relative_invocation()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_writes_community_name()]] - code - graphify/tests/test_watch.py
- [[test_update_discovers_newly_added_files_and_dirs()]] - code - graphify/tests/test_watch.py
- [[test_update_rebuilds_with_nested_star_gitignore()]] - code - graphify/tests/test_watch.py
- [[test_watch.py]] - code - graphify/tests/test_watch.py
- [[test_watch_raises_without_watchdog()]] - code - graphify/tests/test_watch.py
- [[test_watched_extensions_excludes_noise()]] - code - graphify/tests/test_watch.py
- [[test_watched_extensions_includes_code()]] - code - graphify/tests/test_watch.py
- [[test_watched_extensions_includes_docs()]] - code - graphify/tests/test_watch.py
- [[test_watched_extensions_includes_images()]] - code - graphify/tests/test_watch.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_7
SORT file.name ASC
```

## Connections to other communities
- 60 edges to [[_COMMUNITY_Community 15]]
- 12 edges to [[_COMMUNITY_Community 127]]
- 11 edges to [[_COMMUNITY_Community 136]]
- 2 edges to [[_COMMUNITY_Community 12]]
- 2 edges to [[_COMMUNITY_Community 180]]
- 1 edge to [[_COMMUNITY_Community 114]]
- 1 edge to [[_COMMUNITY_Community 44]]

## Top bridge nodes
- [[test_watch.py]] - degree 97, connects to 6 communities
- [[check_update()]] - degree 9, connects to 2 communities
- [[_notify_only()]] - degree 8, connects to 1 community
- [[_seed_semantic_doc_graph()]] - degree 5, connects to 1 community
- [[_seed_semantic_doc_graph_concept_only()]] - degree 5, connects to 1 community