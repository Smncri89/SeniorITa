---
type: community
cohesion: 0.06
members: 52
---

# Community 35

**Cohesion:** 0.06 - loosely connected
**Members:** 52 nodes

## Members
- [[1749 an `imports``references` edge must not bind across a language     famil]] - rationale - graphify/tests/test_build.py
- [[1753 two NON-AST (semantic) nodes sharing (basename, label) but from     DIFF]] - rationale - graphify/tests/test_build.py
- [[2194 a mixed batch of schema errors must report per-cause counts, not     jus]] - rationale - graphify/tests/test_build.py
- [[2194 nodes carrying `name``path` instead of `label``source_file` must     b]] - rationale - graphify/tests/test_build.py
- [[Alias normalization must run BEFORE the semantic id-remap loop so a     `member]] - rationale - graphify/tests/test_hypergraph.py
- [[Build a NetworkX graph from an extraction dict.      directed=True produces a]] - rationale - graphify/graphify/build.py
- [[Canonicalize a hyperedge's member list onto the `nodes` key, in place.      If]] - rationale - graphify/graphify/build.py
- [[Companion to the ambiguous case above when exactly one real file claims     an]] - rationale - graphify/tests/test_build.py
- [[Legacy 'from''to' keys on edges are accepted alongside 'source''target'.]] - rationale - graphify/tests/test_build.py
- [[Non-numeric  NaN  inf  negative weights fall back to 1.0 (the backends     r]] - rationale - graphify/tests/test_build.py
- [[Semantic subagents emit absolute source_file paths; build_from_json must     re]] - rationale - graphify/tests/test_build.py
- [[Store hyperedges in the graph's metadata dict.]] - rationale - graphify/graphify/export.py
- [[Tests for hyperedge support in graphify.]] - rationale - graphify/tests/test_hypergraph.py
- [[Three hyperedges, one per member-key spelling nodes  members  node_ids.]] - rationale - graphify/tests/test_hypergraph.py
- [[Unknown file_type values are coerced through the synonym mapper, falling     ba]] - rationale - graphify/tests/test_build.py
- [[Write graph.json then reload it - hyperedges must survive.]] - rationale - graphify/tests/test_hypergraph.py
- [[_alias_extraction()]] - code - graphify/tests/test_hypergraph.py
- [[_make_report()]] - code - graphify/tests/test_hypergraph.py
- [[_normalize_hyperedge_members()]] - code - graphify/graphify/build.py
- [[attach_hyperedges()]] - code - graphify/graphify/export.py
- [[build_from_json()]] - code - graphify/graphify/build.py
- [[build_from_json(root=...) must relativize hyperedge source_file like it     alr]] - rationale - graphify/tests/test_hypergraph.py
- [[test_attach_hyperedges_adds_new()]] - code - graphify/tests/test_hypergraph.py
- [[test_attach_hyperedges_deduplicates()]] - code - graphify/tests/test_hypergraph.py
- [[test_attach_hyperedges_multiple_different_ids()]] - code - graphify/tests/test_hypergraph.py
- [[test_attach_hyperedges_skips_entry_without_id()]] - code - graphify/tests/test_hypergraph.py
- [[test_build_canonical_nodes_wins_over_alias()]] - code - graphify/tests/test_hypergraph.py
- [[test_build_dedups_alias_members_preserving_order()]] - code - graphify/tests/test_hypergraph.py
- [[test_build_from_json_missing_hyperedges_key()]] - code - graphify/tests/test_hypergraph.py
- [[test_build_from_json_no_hyperedges()]] - code - graphify/tests/test_hypergraph.py
- [[test_build_from_json_relativizes_absolute_source_file()]] - code - graphify/tests/test_build.py
- [[test_build_from_json_relativizes_hyperedge_source_file()]] - code - graphify/tests/test_hypergraph.py
- [[test_build_from_json_stores_hyperedges()]] - code - graphify/tests/test_hypergraph.py
- [[test_build_from_json_unambiguous_old_stem_alias_still_resolves()]] - code - graphify/tests/test_build.py
- [[test_build_normalizes_member_aliases_to_nodes()]] - code - graphify/tests/test_hypergraph.py
- [[test_build_rekeys_alias_keyed_hyperedge_members()]] - code - graphify/tests/test_hypergraph.py
- [[test_build_warns_once_per_aliased_hyperedge()]] - code - graphify/tests/test_hypergraph.py
- [[test_cross_language_imports_references_are_dropped()]] - code - graphify/tests/test_build.py
- [[test_extraction_warning_breakdown_by_cause()]] - code - graphify/tests/test_build.py
- [[test_ghost_merge_non_ast_different_files_both_survive()]] - code - graphify/tests/test_build.py
- [[test_hyperedges_roundtrip_via_json_file()]] - code - graphify/tests/test_hypergraph.py
- [[test_hypergraph.py]] - code - graphify/tests/test_hypergraph.py
- [[test_legacy_edge_from_to_canonicalized()]] - code - graphify/tests/test_build.py
- [[test_legacy_node_name_path_aliases_folded()]] - code - graphify/tests/test_build.py
- [[test_malformed_weights_normalize()]] - code - graphify/tests/test_build.py
- [[test_real_invalid_file_type_coerced_to_concept()]] - code - graphify/tests/test_build.py
- [[test_report_includes_hyperedge_node_list()]] - code - graphify/tests/test_hypergraph.py
- [[test_report_includes_hyperedges_section()]] - code - graphify/tests/test_hypergraph.py
- [[test_report_skips_hyperedges_section_when_empty()]] - code - graphify/tests/test_hypergraph.py
- [[test_report_skips_hyperedges_section_when_key_missing()]] - code - graphify/tests/test_hypergraph.py
- [[test_to_json_hyperedges_empty_when_none()]] - code - graphify/tests/test_hypergraph.py
- [[test_to_json_includes_hyperedges()]] - code - graphify/tests/test_hypergraph.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_35
SORT file.name ASC
```

## Connections to other communities
- 41 edges to [[_COMMUNITY_Community 18]]
- 13 edges to [[_COMMUNITY_Community 59]]
- 10 edges to [[_COMMUNITY_Community 34]]
- 10 edges to [[_COMMUNITY_Community 19]]
- 4 edges to [[_COMMUNITY_Community 94]]
- 4 edges to [[_COMMUNITY_Community 37]]
- 4 edges to [[_COMMUNITY_Community 25]]
- 3 edges to [[_COMMUNITY_Community 17]]
- 3 edges to [[_COMMUNITY_Community 95]]
- 3 edges to [[_COMMUNITY_Community 190]]
- 3 edges to [[_COMMUNITY_Community 159]]
- 3 edges to [[_COMMUNITY_Community 283]]
- 3 edges to [[_COMMUNITY_Community 271]]
- 3 edges to [[_COMMUNITY_Community 203]]
- 3 edges to [[_COMMUNITY_Community 82]]
- 3 edges to [[_COMMUNITY_Community 286]]
- 3 edges to [[_COMMUNITY_Community 258]]
- 2 edges to [[_COMMUNITY_Community 179]]
- 2 edges to [[_COMMUNITY_Community 12]]
- 2 edges to [[_COMMUNITY_Community 48]]
- 2 edges to [[_COMMUNITY_Community 15]]
- 2 edges to [[_COMMUNITY_Community 10]]
- 2 edges to [[_COMMUNITY_Community 49]]
- 2 edges to [[_COMMUNITY_Community 114]]
- 2 edges to [[_COMMUNITY_Community 0]]
- 2 edges to [[_COMMUNITY_Community 209]]
- 2 edges to [[_COMMUNITY_Community 45]]
- 2 edges to [[_COMMUNITY_Community 186]]
- 2 edges to [[_COMMUNITY_Community 210]]
- 2 edges to [[_COMMUNITY_Community 289]]
- 2 edges to [[_COMMUNITY_Community 184]]
- 1 edge to [[_COMMUNITY_Community 5]]
- 1 edge to [[_COMMUNITY_Community 101]]
- 1 edge to [[_COMMUNITY_Community 9]]
- 1 edge to [[_COMMUNITY_Community 23]]
- 1 edge to [[_COMMUNITY_Community 40]]
- 1 edge to [[_COMMUNITY_Community 74]]
- 1 edge to [[_COMMUNITY_Community 61]]
- 1 edge to [[_COMMUNITY_Community 3]]
- 1 edge to [[_COMMUNITY_Community 77]]

## Top bridge nodes
- [[build_from_json()]] - degree 155, connects to 38 communities
- [[test_hypergraph.py]] - degree 30, connects to 5 communities
- [[attach_hyperedges()]] - degree 9, connects to 2 communities
- [[_normalize_hyperedge_members()]] - degree 6, connects to 2 communities
- [[test_legacy_node_name_path_aliases_folded()]] - degree 4, connects to 2 communities