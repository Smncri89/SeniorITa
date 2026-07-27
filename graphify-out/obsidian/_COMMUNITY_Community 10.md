---
type: community
cohesion: 0.04
members: 88
---

# Community 10

**Cohesion:** 0.04 - loosely connected
**Members:** 88 nodes

## Members
- [[AMBIGUOUS edge should score higher than an otherwise identical EXTRACTED edge.]] - rationale - graphify/tests/test_analyze.py
- [[Code→doc INFERRED calls edge should score lower than same-language EXTRACTED.]] - rationale - graphify/tests/test_analyze.py
- [[Code↔paper INFERRED calls should still surface — it is a meaningful link.]] - rationale - graphify/tests/test_analyze.py
- [[Code↔paper edge should score higher than code↔code edge.]] - rationale - graphify/tests/test_analyze.py
- [[Compare two graph snapshots and return what changed.      Returns         {]] - rationale - graphify/graphify/analyze.py
- [[Concept nodes (empty source_file) must not appear in surprises.]] - rationale - graphify/tests/test_analyze.py
- [[Create a graph node resembling real graphify schema.]] - rationale - graphify/tests/test_analyze.py
- [[Cross-language INFERRED calls edge should score lower than same-language EXTRACT]] - rationale - graphify/tests/test_analyze.py
- [[Cross-language INFERRED uses edge (the exact rsl-siege-manager false positive) s]] - rationale - graphify/tests/test_analyze.py
- [[Detect circular import dependencies at the file level.      Collapses symbol-l]] - rationale - graphify/graphify/analyze.py
- [[DiGraph_1]] - code
- [[EXTRACTED code↔doc edges are real facts — must not be penalised.]] - rationale - graphify/tests/test_analyze.py
- [[EXTRACTED cross-language edges are real structural facts — must not be penalised]] - rationale - graphify/tests/test_analyze.py
- [[Find connections that are genuinely surprising - not obvious from file structure]] - rationale - graphify/graphify/analyze.py
- [[Helper Python node in backend, TypeScript node in frontend, different communi]] - rationale - graphify/tests/test_analyze.py
- [[Helper build a small nx.Graph from nodeedge specs.]] - rationale - graphify/tests/test_analyze.py
- [[INFERRED calls within the same language family must not be affected.]] - rationale - graphify/tests/test_analyze.py
- [[JSON-key filter must match regardless of label casing.]] - rationale - graphify/tests/test_analyze.py
- [[Multi-file graph should find cross-file edges between real entities.]] - rationale - graphify/tests/test_analyze.py
- [[Return True if two source files belong to different language families.]] - rationale - graphify/graphify/analyze.py
- [[Return the first path component - used to detect cross-repo edges.]] - rationale - graphify/graphify/analyze.py
- [[Score how surprising a cross-file edge is. Returns (score, reasons).]] - rationale - graphify/graphify/analyze.py
- [[Single-file graph should return cross-community edges, not empty list.]] - rationale - graphify/tests/test_analyze.py
- [[Tests for analyze.py.]] - rationale - graphify/tests/test_analyze.py
- [[_cross_language()]] - code - graphify/graphify/analyze.py
- [[_file_category falls back to 'doc' for unknown extensions, so INFERRED     call]] - rationale - graphify/tests/test_analyze.py
- [[_file_category()]] - code - graphify/graphify/analyze.py
- [[_is_json_key_node()]] - code - graphify/graphify/analyze.py
- [[_make_code_doc_graph()]] - code - graphify/tests/test_analyze.py
- [[_make_cross_lang_graph()]] - code - graphify/tests/test_analyze.py
- [[_make_cycle_graph_directed()]] - code - graphify/tests/test_analyze.py
- [[_make_file_node()]] - code - graphify/tests/test_analyze.py
- [[_make_simple_graph()]] - code - graphify/tests/test_analyze.py
- [[_surprise_score()]] - code - graphify/graphify/analyze.py
- [[_top_level_dir()]] - code - graphify/graphify/analyze.py
- [[`semantically_similar_to` across code↔doc is explicit LLM insight — must not be]] - rationale - graphify/tests/test_analyze.py
- [[`semantically_similar_to` across languages is a genuine insight — must not be su]] - rationale - graphify/tests/test_analyze.py
- [[find_import_cycles()]] - code - graphify/graphify/analyze.py
- [[god_nodes must not return generic JSON key nodes like 'name' or 'id'.]] - rationale - graphify/tests/test_analyze.py
- [[graph_diff()]] - code - graphify/graphify/analyze.py
- [[make_graph()]] - code - graphify/tests/test_analyze.py
- [[npm package.json dep-block keys must be filtered from god_nodes output.      C]] - rationale - graphify/tests/test_analyze.py
- [[parametrize_1]] - code
- [[surprising_connections()]] - code - graphify/graphify/analyze.py
- [[test_analyze.py]] - code - graphify/tests/test_analyze.py
- [[test_code_doc_extracted_calls_not_suppressed()]] - code - graphify/tests/test_analyze.py
- [[test_code_doc_inferred_calls_suppressed()]] - code - graphify/tests/test_analyze.py
- [[test_code_doc_inferred_semantically_similar_not_suppressed()]] - code - graphify/tests/test_analyze.py
- [[test_code_doc_inferred_uses_suppressed()]] - code - graphify/tests/test_analyze.py
- [[test_code_paper_inferred_calls_not_suppressed()]] - code - graphify/tests/test_analyze.py
- [[test_code_unknown_extension_inferred_calls_suppressed()]] - code - graphify/tests/test_analyze.py
- [[test_cross_language_extracted_calls_not_suppressed()]] - code - graphify/tests/test_analyze.py
- [[test_cross_language_inferred_calls_suppressed()]] - code - graphify/tests/test_analyze.py
- [[test_cross_language_inferred_uses_suppressed()]] - code - graphify/tests/test_analyze.py
- [[test_cross_language_semantically_similar_not_suppressed()]] - code - graphify/tests/test_analyze.py
- [[test_file_category()]] - code - graphify/tests/test_analyze.py
- [[test_find_import_cycles_detects_2_and_3_cycles()]] - code - graphify/tests/test_analyze.py
- [[test_find_import_cycles_empty_graph()]] - code - graphify/tests/test_analyze.py
- [[test_find_import_cycles_handles_undirected_graph_input()]] - code - graphify/tests/test_analyze.py
- [[test_find_import_cycles_ignores_non_import_relations()]] - code - graphify/tests/test_analyze.py
- [[test_find_import_cycles_includes_self_loop_cycle()]] - code - graphify/tests/test_analyze.py
- [[test_find_import_cycles_no_cycles()]] - code - graphify/tests/test_analyze.py
- [[test_find_import_cycles_respects_max_cycle_length()]] - code - graphify/tests/test_analyze.py
- [[test_find_import_cycles_returns_structured_records()]] - code - graphify/tests/test_analyze.py
- [[test_find_import_cycles_skips_nodes_without_source_file()]] - code - graphify/tests/test_analyze.py
- [[test_god_nodes_excludes_json_noise()]] - code - graphify/tests/test_analyze.py
- [[test_god_nodes_excludes_npm_dep_block_keys()]] - code - graphify/tests/test_analyze.py
- [[test_god_nodes_filter_is_case_insensitive()]] - code - graphify/tests/test_analyze.py
- [[test_god_nodes_have_required_keys()]] - code - graphify/tests/test_analyze.py
- [[test_god_nodes_returns_list()]] - code - graphify/tests/test_analyze.py
- [[test_god_nodes_sorted_by_degree()]] - code - graphify/tests/test_analyze.py
- [[test_graph_diff_empty_diff()]] - code - graphify/tests/test_analyze.py
- [[test_graph_diff_new_edges()]] - code - graphify/tests/test_analyze.py
- [[test_graph_diff_new_nodes()]] - code - graphify/tests/test_analyze.py
- [[test_graph_diff_removed_nodes()]] - code - graphify/tests/test_analyze.py
- [[test_is_json_key_node_noise_label()]] - code - graphify/tests/test_analyze.py
- [[test_is_json_key_node_non_json_file()]] - code - graphify/tests/test_analyze.py
- [[test_is_json_key_node_real_label()]] - code - graphify/tests/test_analyze.py
- [[test_same_language_inferred_calls_not_suppressed()]] - code - graphify/tests/test_analyze.py
- [[test_suggest_questions_excludes_rationale_nodes_from_isolated_count()]] - code - graphify/tests/test_analyze.py
- [[test_surprise_score_accepts_precomputed_degrees()]] - code - graphify/tests/test_analyze.py
- [[test_surprising_connections_ambiguous_scores_higher_than_extracted()]] - code - graphify/tests/test_analyze.py
- [[test_surprising_connections_cross_source_multi_file()]] - code - graphify/tests/test_analyze.py
- [[test_surprising_connections_cross_type_scores_higher()]] - code - graphify/tests/test_analyze.py
- [[test_surprising_connections_excludes_concept_nodes()]] - code - graphify/tests/test_analyze.py
- [[test_surprising_connections_have_required_keys()]] - code - graphify/tests/test_analyze.py
- [[test_surprising_connections_have_why_field()]] - code - graphify/tests/test_analyze.py
- [[test_surprising_connections_single_file_uses_community_bridges()]] - code - graphify/tests/test_analyze.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_10
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_Community 77]]
- 15 edges to [[_COMMUNITY_Community 59]]
- 6 edges to [[_COMMUNITY_Community 19]]
- 4 edges to [[_COMMUNITY_Community 15]]
- 4 edges to [[_COMMUNITY_Community 186]]
- 2 edges to [[_COMMUNITY_Community 12]]
- 2 edges to [[_COMMUNITY_Community 49]]
- 2 edges to [[_COMMUNITY_Community 209]]
- 2 edges to [[_COMMUNITY_Community 166]]
- 2 edges to [[_COMMUNITY_Community 6]]
- 2 edges to [[_COMMUNITY_Community 35]]
- 1 edge to [[_COMMUNITY_Community 98]]
- 1 edge to [[_COMMUNITY_Community 135]]
- 1 edge to [[_COMMUNITY_Community 40]]
- 1 edge to [[_COMMUNITY_Community 34]]
- 1 edge to [[_COMMUNITY_Community 114]]
- 1 edge to [[_COMMUNITY_Community 3]]

## Top bridge nodes
- [[surprising_connections()]] - degree 28, connects to 10 communities
- [[test_analyze.py]] - degree 67, connects to 8 communities
- [[find_import_cycles()]] - degree 18, connects to 4 communities
- [[_surprise_score()]] - degree 24, connects to 2 communities
- [[_is_json_key_node()]] - degree 6, connects to 2 communities