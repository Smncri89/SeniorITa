---
type: community
cohesion: 0.03
members: 71
---

# Community 18

**Cohesion:** 0.03 - loosely connected
**Members:** 71 nodes

## Members
- [[1145 ghost-merge a semantic ghost collapses into the single AST node     shar]] - rationale - graphify/tests/test_build.py
- [[1279 a semanticLLM edge lacking source_file must inherit it from its     sou]] - rationale - graphify/tests/test_build.py
- [[1799 guard a code symbol `foo` and an unrelated `foo_doc` (not     file_type=]] - rationale - graphify/tests/test_build.py
- [[1799 the markdown quick-scan's bare `slug` doc node and the semantic     `]] - rationale - graphify/tests/test_build.py
- [[1916 build_from_json used to copy hyperedges into G.graphhyperedges     v]] - rationale - graphify/tests/test_build.py
- [[1960 an explicit ``weight null`` (JSON null - None) used to survive     `]] - rationale - graphify/tests/test_build.py
- [[2068 the ghost-merge key is the full source_file, not the bare basename.]] - rationale - graphify/tests/test_build.py
- [[2068 two unrelated non-AST nodes with the same basename+label in     DIFFEREN]] - rationale - graphify/tests/test_build.py
- [[2194 a recovered alias node must serialize with a non-empty norm_label     so]] - rationale - graphify/tests/test_build.py
- [[2194 an alias-only semantic node (namepath) must participate in the     AST]] - rationale - graphify/tests/test_build.py
- [[2194 edges carrying `type``confidence_score` instead of     `relation``conf]] - rationale - graphify/tests/test_build.py
- [[2194 when both the canonical field and its alias are present, the     canonic]] - rationale - graphify/tests/test_build.py
- [[A genuine duplicate — two non-AST nodes with the SAME source_file and     label]] - rationale - graphify/tests/test_build.py
- [[A node_link JSON with multigraph true must load as MultiGraph and the     help]] - rationale - graphify/tests/test_build.py
- [[A same-directory .h.cpp pair collides on their shared pre-extension id     and]] - rationale - graphify/tests/test_build.py
- [[Already-relative source_file paths must not be modified.]] - rationale - graphify/tests/test_build.py
- [[Known invalid file_type values map to their canonical equivalents.]] - rationale - graphify/tests/test_build.py
- [[Legacy 'source' key on nodes is renamed to 'source_file' before graph build.]] - rationale - graphify/tests/test_build.py
- [[Legacy nodes with file_type=None (e.g. preserved from older graph.json     by `]] - rationale - graphify/tests/test_build.py
- [[Nodes missing file_type entirely should also be canonicalized to 'concept'.]] - rationale - graphify/tests/test_build.py
- [[Regression for 1061.      When an extraction emits two `calls` edges between]] - rationale - graphify/tests/test_build.py
- [[Return every edge attribute dict for (u, v); always a list.]] - rationale - graphify/graphify/build.py
- [[Return one edge attribute dict for (u, v), tolerating MultiGraph.      For Mul]] - rationale - graphify/graphify/build.py
- [[The 1504 old-stem alias (e.g. ping.h - bare ping) is meant to let a     s]] - rationale - graphify/tests/test_build.py
- [[The 1749 guard only drops when BOTH endpoints are known code languages,     so]] - rationale - graphify/tests/test_build.py
- [[The read-only-consumer nudge (queryserve) flags a pre-1504 graph and     leav]] - rationale - graphify/tests/test_build.py
- [[Windows backslash paths and POSIX paths for the same file must produce one node.]] - rationale - graphify/tests/test_build.py
- [[edge_data()]] - code - graphify/graphify/build.py
- [[edge_datas()]] - code - graphify/graphify/build.py
- [[load_extraction()]] - code - graphify/tests/test_build.py
- [[test_alias_node_gets_nonempty_norm_label()]] - code - graphify/tests/test_build.py
- [[test_alias_node_ghost_merges_into_ast_twin()]] - code - graphify/tests/test_build.py
- [[test_ambiguous_edge_preserved()]] - code - graphify/tests/test_build.py
- [[test_build.py]] - code - graphify/tests/test_build.py
- [[test_build_from_json_ambiguous_alias_detected_despite_header_impl_salting()]] - code - graphify/tests/test_build.py
- [[test_build_from_json_ambiguous_old_stem_alias_stays_dangling()]] - code - graphify/tests/test_build.py
- [[test_build_from_json_edge_count()]] - code - graphify/tests/test_build.py
- [[test_build_from_json_node_count()]] - code - graphify/tests/test_build.py
- [[test_build_from_json_preserves_first_direction_on_bidirectional_pair()]] - code - graphify/tests/test_build.py
- [[test_build_from_json_prunes_dangling_hyperedge_members()]] - code - graphify/tests/test_build.py
- [[test_build_from_json_relative_source_file_unchanged()]] - code - graphify/tests/test_build.py
- [[test_build_from_json_skips_edge_with_non_hashable_endpoint()]] - code - graphify/tests/test_build.py
- [[test_build_from_json_skips_non_hashable_node_id()]] - code - graphify/tests/test_build.py
- [[test_cross_family_reference_to_unknown_ext_is_kept()]] - code - graphify/tests/test_build.py
- [[test_dedupe_edges_collapses_exact_parallels()]] - code - graphify/tests/test_build.py
- [[test_dedupe_edges_is_idempotent()]] - code - graphify/tests/test_build.py
- [[test_dedupe_nodes_collapses_by_id_last_wins()]] - code - graphify/tests/test_build.py
- [[test_doc_twin_merge_does_not_touch_code_symbols()]] - code - graphify/tests/test_build.py
- [[test_edge_data_multidigraph()]] - code - graphify/tests/test_build.py
- [[test_edge_data_multigraph_with_parallel_edges()]] - code - graphify/tests/test_build.py
- [[test_edge_data_node_link_multigraph_roundtrip()]] - code - graphify/tests/test_build.py
- [[test_edge_data_simple_graph()]] - code - graphify/tests/test_build.py
- [[test_edge_datas_multigraph_returns_all_parallel_edges()]] - code - graphify/tests/test_build.py
- [[test_edge_datas_simple_graph_returns_singleton_list()]] - code - graphify/tests/test_build.py
- [[test_edge_missing_source_file_backfilled_from_node()]] - code - graphify/tests/test_build.py
- [[test_edges_have_confidence()]] - code - graphify/tests/test_build.py
- [[test_file_type_synonym_mapping()]] - code - graphify/tests/test_build.py
- [[test_ghost_merge_non_ast_same_file_still_merges()]] - code - graphify/tests/test_build.py
- [[test_ghost_merge_not_across_directories_same_basename()]] - code - graphify/tests/test_build.py
- [[test_ghost_merge_unique_located_node_still_merges()]] - code - graphify/tests/test_build.py
- [[test_ghost_merge_uses_source_file_not_basename()]] - code - graphify/tests/test_build.py
- [[test_graph_has_legacy_ids_detects_old_scheme()]] - code - graphify/tests/test_build.py
- [[test_legacy_edge_type_confidence_score_aliases_folded()]] - code - graphify/tests/test_build.py
- [[test_legacy_node_source_canonicalized()]] - code - graphify/tests/test_build.py
- [[test_markdown_doc_twin_merges_into_semantic_doc_node()]] - code - graphify/tests/test_build.py
- [[test_missing_file_type_defaults_to_concept()]] - code - graphify/tests/test_build.py
- [[test_node_alias_canonical_field_wins()]] - code - graphify/tests/test_build.py
- [[test_nodes_have_label()]] - code - graphify/tests/test_build.py
- [[test_none_file_type_defaults_to_concept()]] - code - graphify/tests/test_build.py
- [[test_null_weight_edge_builds_and_clusters()]] - code - graphify/tests/test_build.py
- [[test_source_file_backslash_normalized()]] - code - graphify/tests/test_build.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_18
SORT file.name ASC
```

## Connections to other communities
- 41 edges to [[_COMMUNITY_Community 35]]
- 8 edges to [[_COMMUNITY_Community 179]]
- 7 edges to [[_COMMUNITY_Community 34]]
- 5 edges to [[_COMMUNITY_Community 15]]
- 5 edges to [[_COMMUNITY_Community 19]]
- 4 edges to [[_COMMUNITY_Community 12]]
- 3 edges to [[_COMMUNITY_Community 21]]
- 3 edges to [[_COMMUNITY_Community 94]]
- 2 edges to [[_COMMUNITY_Community 77]]
- 2 edges to [[_COMMUNITY_Community 25]]
- 2 edges to [[_COMMUNITY_Community 98]]
- 2 edges to [[_COMMUNITY_Community 135]]
- 2 edges to [[_COMMUNITY_Community 190]]
- 1 edge to [[_COMMUNITY_Community 219]]
- 1 edge to [[_COMMUNITY_Community 121]]
- 1 edge to [[_COMMUNITY_Community 29]]
- 1 edge to [[_COMMUNITY_Community 37]]

## Top bridge nodes
- [[edge_data()]] - degree 24, connects to 10 communities
- [[test_build.py]] - degree 76, connects to 9 communities
- [[edge_datas()]] - degree 11, connects to 4 communities
- [[test_build_from_json_preserves_first_direction_on_bidirectional_pair()]] - degree 5, connects to 2 communities
- [[test_alias_node_gets_nonempty_norm_label()]] - degree 4, connects to 2 communities