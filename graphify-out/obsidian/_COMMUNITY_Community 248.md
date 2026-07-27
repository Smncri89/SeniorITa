---
type: community
cohesion: 0.20
members: 10
---

# Community 248

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[A None per_file slot is treated as empty fragment (no crash, no edges).]] - rationale - graphify/tests/test_symbol_resolution.py
- [[A non-dict per_file slot (e.g. a string) must not raise AttributeError.]] - rationale - graphify/tests/test_symbol_resolution.py
- [[Python import-guided resolver also tolerates malformed raw_calls.]] - rationale - graphify/tests/test_symbol_resolution.py
- [[Resolve raw Python calls using explicit import evidence.      Only ``from modu]] - rationale - graphify/graphify/symbol_resolution.py
- [[per_file shorter than paths must not raise IndexError.]] - rationale - graphify/tests/test_symbol_resolution.py
- [[resolve_python_import_guided_calls()]] - code - graphify/graphify/symbol_resolution.py
- [[test_resolve_python_import_guided_calls_non_dict_per_file_slot()]] - code - graphify/tests/test_symbol_resolution.py
- [[test_resolve_python_import_guided_calls_per_file_none_slot()]] - code - graphify/tests/test_symbol_resolution.py
- [[test_resolve_python_import_guided_calls_per_file_shorter_than_paths()]] - code - graphify/tests/test_symbol_resolution.py
- [[test_resolve_python_import_guided_calls_survives_malformed_raw_calls()]] - code - graphify/tests/test_symbol_resolution.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_248
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Community 187]]
- 4 edges to [[_COMMUNITY_Community 132]]
- 2 edges to [[_COMMUNITY_Community 231]]
- 1 edge to [[_COMMUNITY_Community 36]]
- 1 edge to [[_COMMUNITY_Community 172]]

## Top bridge nodes
- [[resolve_python_import_guided_calls()]] - degree 17, connects to 5 communities
- [[test_resolve_python_import_guided_calls_non_dict_per_file_slot()]] - degree 3, connects to 1 community
- [[test_resolve_python_import_guided_calls_per_file_none_slot()]] - degree 3, connects to 1 community
- [[test_resolve_python_import_guided_calls_per_file_shorter_than_paths()]] - degree 3, connects to 1 community
- [[test_resolve_python_import_guided_calls_survives_malformed_raw_calls()]] - degree 3, connects to 1 community