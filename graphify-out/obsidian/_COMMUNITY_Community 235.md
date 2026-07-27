---
type: community
cohesion: 0.31
members: 11
---

# Community 235

**Cohesion:** 0.31 - loosely connected
**Members:** 11 nodes

## Members
- [[Corrupt graph.json produces an actionable error, not a raw traceback (1536153]] - rationale - graphify/tests/test_corrupt_graph_json.py
- [[Happy path unchanged a well-formed graph.json loads without raising.]] - rationale - graphify/tests/test_corrupt_graph_json.py
- [[Read a JSON graph after applying Graphify's graph-load size cap.]] - rationale - graphify/graphify/diagnostics.py
- [[_corrupt()]] - code - graphify/tests/test_corrupt_graph_json.py
- [[_read_json_file()]] - code - graphify/graphify/diagnostics.py
- [[load_graph()]] - code - graphify/graphify/affected.py
- [[test_affected_load_graph_corrupt_raises_runtimeerror()]] - code - graphify/tests/test_corrupt_graph_json.py
- [[test_build_merge_corrupt_graph_raises_runtimeerror()]] - code - graphify/tests/test_corrupt_graph_json.py
- [[test_corrupt_graph_json.py]] - code - graphify/tests/test_corrupt_graph_json.py
- [[test_diagnostics_read_corrupt_raises_runtimeerror()]] - code - graphify/tests/test_corrupt_graph_json.py
- [[test_valid_graph_still_loads()]] - code - graphify/tests/test_corrupt_graph_json.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_235
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Community 48]]
- 4 edges to [[_COMMUNITY_Community 34]]
- 2 edges to [[_COMMUNITY_Community 218]]
- 2 edges to [[_COMMUNITY_Community 12]]
- 1 edge to [[_COMMUNITY_Community 86]]
- 1 edge to [[_COMMUNITY_Community 36]]

## Top bridge nodes
- [[test_corrupt_graph_json.py]] - degree 12, connects to 3 communities
- [[load_graph()]] - degree 7, connects to 3 communities
- [[_read_json_file()]] - degree 9, connects to 2 communities
- [[test_valid_graph_still_loads()]] - degree 5, connects to 1 community
- [[test_build_merge_corrupt_graph_raises_runtimeerror()]] - degree 3, connects to 1 community