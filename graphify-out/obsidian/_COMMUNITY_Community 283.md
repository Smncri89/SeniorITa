---
type: community
cohesion: 0.29
members: 8
---

# Community 283

**Cohesion:** 0.29 - loosely connected
**Members:** 8 nodes

## Members
- [[Integration test for push_to_falkordb against a real FalkorDB instance.  Runs]] - rationale - graphify/tests/test_falkordb_integration.py
- [[MERGE-based push is safe to re-run - counts must not grow.]] - rationale - graphify/tests/test_falkordb_integration.py
- [[Return a connected FalkorDB client, or skip if none is reachable.]] - rationale - graphify/tests/test_falkordb_integration.py
- [[_connect()]] - code - graphify/tests/test_falkordb_integration.py
- [[db()]] - code - graphify/tests/test_falkordb_integration.py
- [[test_falkordb_integration.py]] - code - graphify/tests/test_falkordb_integration.py
- [[test_push_to_falkordb_creates_expected_graph()]] - code - graphify/tests/test_falkordb_integration.py
- [[test_push_to_falkordb_is_idempotent()]] - code - graphify/tests/test_falkordb_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_283
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 35]]
- 2 edges to [[_COMMUNITY_Community 77]]
- 1 edge to [[_COMMUNITY_Community 119]]

## Top bridge nodes
- [[test_push_to_falkordb_is_idempotent()]] - degree 4, connects to 2 communities
- [[test_push_to_falkordb_creates_expected_graph()]] - degree 3, connects to 2 communities
- [[test_falkordb_integration.py]] - degree 6, connects to 1 community
- [[db()]] - degree 3, connects to 1 community