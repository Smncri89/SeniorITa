---
type: community
cohesion: 0.09
members: 31
---

# Community 86

**Cohesion:** 0.09 - loosely connected
**Members:** 31 nodes

## Members
- [[A caller whose call site (L158) differs from its own def line (L90).]] - rationale - graphify/tests/test_affected_cli.py
- [[A graph persisted with directed=false must still recover caller-callee     dir]] - rationale - graphify/tests/test_affected_cli.py
- [[A trailing path separator must not change the match (parity with explain's]] - rationale - graphify/tests/test_affected_cli.py
- [[An edge with no stored location honestly falls back to the node's def line.]] - rationale - graphify/tests/test_affected_cli.py
- [[Lowercased label with the callable decoration (trailing ()) removed.]] - rationale - graphify/graphify/affected.py
- [[Path_1]] - code
- [[Return the file-level node when a source_file query matches many nodes.]] - rationale - graphify/graphify/affected.py
- [[Several nodes share a source_file but none is the L1 file node and none's     b]] - rationale - graphify/tests/test_affected_cli.py
- [[_bare_name()]] - code - graphify/graphify/affected.py
- [[_normalize_label()]] - code - graphify/graphify/affected.py
- [[_prefer_file_node()]] - code - graphify/graphify/affected.py
- [[_write_callsite_graph()]] - code - graphify/tests/test_affected_cli.py
- [[_write_graph()]] - code - graphify/tests/test_affected_cli.py
- [[graphify's `extract` writes graph.json with an edges key (not networkx's]] - rationale - graphify/tests/test_affected_cli.py
- [[resolve_seed()]] - code - graphify/graphify/affected.py
- [[test_affected_cli.py]] - code - graphify/tests/test_affected_cli.py
- [[test_affected_cli_forces_directed_on_undirected_graph()]] - code - graphify/tests/test_affected_cli.py
- [[test_affected_cli_loads_edges_keyed_graph()]] - code - graphify/tests/test_affected_cli.py
- [[test_affected_cli_relation_filter_limits_reverse_traversal()]] - code - graphify/tests/test_affected_cli.py
- [[test_affected_cli_reverse_traverses_impact_edges()]] - code - graphify/tests/test_affected_cli.py
- [[test_affected_cli_source_file_path_uses_file_level_node()]] - code - graphify/tests/test_affected_cli.py
- [[test_affected_falls_back_to_def_line_when_edge_has_no_location()]] - code - graphify/tests/test_affected_cli.py
- [[test_affected_reports_call_site_line_not_def_line()]] - code - graphify/tests/test_affected_cli.py
- [[test_resolve_seed_bare_name_matches_callable_label()]] - code - graphify/tests/test_affected_cli.py
- [[test_resolve_seed_bare_name_tie_still_returns_none()]] - code - graphify/tests/test_affected_cli.py
- [[test_resolve_seed_decorated_query_matches_bare_label()]] - code - graphify/tests/test_affected_cli.py
- [[test_resolve_seed_matches_unicode_normalized_label()]] - code - graphify/tests/test_affected_cli.py
- [[test_resolve_seed_preserves_distinct_accents()]] - code - graphify/tests/test_affected_cli.py
- [[test_resolve_seed_source_file_ambiguous_no_file_node_returns_none()]] - code - graphify/tests/test_affected_cli.py
- [[test_resolve_seed_source_file_path_prefers_file_level_node()]] - code - graphify/tests/test_affected_cli.py
- [[test_resolve_seed_source_file_trailing_slash_parity()]] - code - graphify/tests/test_affected_cli.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_86
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Community 47]]
- 5 edges to [[_COMMUNITY_Community 218]]
- 1 edge to [[_COMMUNITY_Community 4]]
- 1 edge to [[_COMMUNITY_Community 235]]

## Top bridge nodes
- [[test_affected_cli.py]] - degree 19, connects to 1 community
- [[resolve_seed()]] - degree 14, connects to 1 community
- [[_prefer_file_node()]] - degree 5, connects to 1 community
- [[_bare_name()]] - degree 4, connects to 1 community
- [[_normalize_label()]] - degree 4, connects to 1 community