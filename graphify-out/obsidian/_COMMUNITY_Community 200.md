---
type: community
cohesion: 0.13
members: 15
---

# Community 200

**Cohesion:** 0.13 - loosely connected
**Members:** 15 nodes

## Members
- [[A real cross-file call must resolve to the SRC definition even when a     same-]] - rationale - graphify/tests/test_symbol_resolution.py
- [[A test file calling save() with both a src def and a test-local def present]] - rationale - graphify/tests/test_symbol_resolution.py
- [[One src def plus many same-named test stubs exactly one edge to src.]] - rationale - graphify/tests/test_symbol_resolution.py
- [[Resolve unqualified raw calls conservatively after all files are known.      T]] - rationale - graphify/graphify/symbol_resolution.py
- [[The python cross-file resolver returns  (not crash) on bad raw_calls.]] - rationale - graphify/tests/test_symbol_resolution.py
- [[Two genuine NON-test defs of the same name the god-node guard must still     h]] - rationale - graphify/tests/test_symbol_resolution.py
- [[resolve_cross_file_raw_calls()]] - code - graphify/graphify/symbol_resolution.py
- [[test_resolve_cross_file_raw_calls_call_site_is_test_prefers_test_local()]] - code - graphify/tests/test_symbol_resolution.py
- [[test_resolve_cross_file_raw_calls_emits_unique_unqualified_call()]] - code - graphify/tests/test_symbol_resolution.py
- [[test_resolve_cross_file_raw_calls_n_mock_scale()]] - code - graphify/tests/test_symbol_resolution.py
- [[test_resolve_cross_file_raw_calls_real_edge_survives_test_mock()]] - code - graphify/tests/test_symbol_resolution.py
- [[test_resolve_cross_file_raw_calls_skips_ambiguous_duplicate_labels()]] - code - graphify/tests/test_symbol_resolution.py
- [[test_resolve_cross_file_raw_calls_skips_existing_pair()]] - code - graphify/tests/test_symbol_resolution.py
- [[test_resolve_cross_file_raw_calls_skips_member_calls()]] - code - graphify/tests/test_symbol_resolution.py
- [[test_resolve_cross_file_raw_calls_survives_malformed_raw_calls()]] - code - graphify/tests/test_symbol_resolution.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_200
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Community 187]]
- 4 edges to [[_COMMUNITY_Community 132]]
- 1 edge to [[_COMMUNITY_Community 76]]
- 1 edge to [[_COMMUNITY_Community 278]]

## Top bridge nodes
- [[resolve_cross_file_raw_calls()]] - degree 16, connects to 4 communities
- [[test_resolve_cross_file_raw_calls_call_site_is_test_prefers_test_local()]] - degree 3, connects to 1 community
- [[test_resolve_cross_file_raw_calls_n_mock_scale()]] - degree 3, connects to 1 community
- [[test_resolve_cross_file_raw_calls_real_edge_survives_test_mock()]] - degree 3, connects to 1 community
- [[test_resolve_cross_file_raw_calls_skips_ambiguous_duplicate_labels()]] - degree 3, connects to 1 community