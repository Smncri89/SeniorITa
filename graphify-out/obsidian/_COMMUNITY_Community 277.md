---
type: community
cohesion: 0.25
members: 8
---

# Community 277

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[Determinism hinges on this sort docs come back oldest-first, filename as tiebre]] - rationale - graphify/tests/test_reflect.py
- [[Parse every memory doc under ``memory_dir``, sorted by date then filename.]] - rationale - graphify/graphify/reflect.py
- [[dead_endscorrections are appended in doc order, so their determinism rides on]] - rationale - graphify/tests/test_reflect.py
- [[load_memory_docs()]] - code - graphify/graphify/reflect.py
- [[test_dead_ends_and_corrections_follow_doc_order()]] - code - graphify/tests/test_reflect.py
- [[test_load_memory_docs_missing_dir_is_empty()]] - code - graphify/tests/test_reflect.py
- [[test_load_memory_docs_orders_by_date_then_filename()]] - code - graphify/tests/test_reflect.py
- [[test_load_memory_docs_skips_foreign_and_sorts()]] - code - graphify/tests/test_reflect.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_277
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Community 40]]
- 4 edges to [[_COMMUNITY_Community 53]]
- 2 edges to [[_COMMUNITY_Community 149]]
- 1 edge to [[_COMMUNITY_Community 142]]
- 1 edge to [[_COMMUNITY_Community 239]]
- 1 edge to [[_COMMUNITY_Community 77]]
- 1 edge to [[_COMMUNITY_Community 15]]

## Top bridge nodes
- [[load_memory_docs()]] - degree 15, connects to 5 communities
- [[test_dead_ends_and_corrections_follow_doc_order()]] - degree 5, connects to 2 communities
- [[test_load_memory_docs_orders_by_date_then_filename()]] - degree 4, connects to 2 communities
- [[test_load_memory_docs_skips_foreign_and_sorts()]] - degree 3, connects to 2 communities
- [[test_load_memory_docs_missing_dir_is_empty()]] - degree 2, connects to 1 community