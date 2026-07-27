---
type: community
cohesion: 0.12
members: 17
---

# Community 179

**Cohesion:** 0.12 - loosely connected
**Members:** 17 nodes

## Members
- [[1007 manifest stores absolute paths, graph nodes store relative paths.     pr]] - rationale - graphify/tests/test_build.py
- [[1007 prune_sources with Windows-style backslash absolute paths must still matc]] - rationale - graphify/tests/test_build.py
- [[Fold legacy node field aliases onto canonical keys, in place (2194).      ``n]] - rationale - graphify/graphify/build.py
- [[Merge multiple extraction results into one graph.      directed=True produces]] - rationale - graphify/graphify/build.py
- [[Re-extracting a CHANGED file must REPLACE its prior nodesedges, not     accumu]] - rationale - graphify/tests/test_build.py
- [[Regression for 760.      When the callee is defined before the caller in sour]] - rationale - graphify/tests/test_build.py
- [[Skill contract the extraction subagent must emit source_file as the     verbat]] - rationale - graphify/tests/test_build.py
- [[_fold_node_aliases()]] - code - graphify/graphify/build.py
- [[build()]] - code - graphify/graphify/build.py
- [[build() passes root through to build_from_json (932).]] - rationale - graphify/tests/test_build.py
- [[test_build_merge_preserves_call_edge_direction()]] - code - graphify/tests/test_build.py
- [[test_build_merge_prune_absolute_paths_match_relative_nodes()]] - code - graphify/tests/test_build.py
- [[test_build_merge_prune_windows_backslash_paths()]] - code - graphify/tests/test_build.py
- [[test_build_merge_replaces_changed_file_stale_edges()]] - code - graphify/tests/test_build.py
- [[test_build_merge_root_collapses_convention_drift()]] - code - graphify/tests/test_build.py
- [[test_build_merges_multiple_extractions()]] - code - graphify/tests/test_build.py
- [[test_build_relativizes_absolute_source_file()]] - code - graphify/tests/test_build.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_179
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Community 34]]
- 8 edges to [[_COMMUNITY_Community 18]]
- 4 edges to [[_COMMUNITY_Community 166]]
- 3 edges to [[_COMMUNITY_Community 69]]
- 2 edges to [[_COMMUNITY_Community 35]]
- 2 edges to [[_COMMUNITY_Community 12]]
- 1 edge to [[_COMMUNITY_Community 87]]
- 1 edge to [[_COMMUNITY_Community 19]]
- 1 edge to [[_COMMUNITY_Community 29]]

## Top bridge nodes
- [[build()]] - degree 24, connects to 7 communities
- [[test_build_merge_preserves_call_edge_direction()]] - degree 6, connects to 4 communities
- [[_fold_node_aliases()]] - degree 4, connects to 2 communities
- [[test_build_merge_prune_absolute_paths_match_relative_nodes()]] - degree 4, connects to 2 communities
- [[test_build_merge_prune_windows_backslash_paths()]] - degree 4, connects to 2 communities