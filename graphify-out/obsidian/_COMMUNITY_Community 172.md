---
type: community
cohesion: 0.12
members: 18
---

# Community 172

**Cohesion:** 0.12 - loosely connected
**Members:** 18 nodes

## Members
- [[A None entry in per_file (e.g. failed extraction) must be silently skipped.]] - rationale - graphify/tests/test_symbol_resolution.py
- [[A `bash_sources` entry missing `target_path` must not raise KeyError.]] - rationale - graphify/tests/test_symbol_resolution.py
- [[A bash raw_call with `callee list` (unhashable for dict membership)     must]] - rationale - graphify/tests/test_symbol_resolution.py
- [[A node tagged as bash_function but missing `id` must not raise KeyError.]] - rationale - graphify/tests/test_symbol_resolution.py
- [[A raw_call entry missing `caller_nid` must not raise KeyError.]] - rationale - graphify/tests/test_symbol_resolution.py
- [[Non-dict entries in bash_sourcesraw_callsnodes must be silently skipped.]] - rationale - graphify/tests/test_symbol_resolution.py
- [[Path_53]] - code
- [[Resolve Bash sourceimport edges and source-backed function calls.      Defens]] - rationale - graphify/graphify/symbol_resolution.py
- [[_file_node_id_for_path()]] - code - graphify/graphify/symbol_resolution.py
- [[`source .helper.sh` from amain.sh should resolve to ahelper.sh,     not to .]] - rationale - graphify/tests/test_symbol_resolution.py
- [[resolve_bash_source_edges()]] - code - graphify/graphify/symbol_resolution.py
- [[test_resolve_bash_source_edges_accepts_none_per_file_entries()]] - code - graphify/tests/test_symbol_resolution.py
- [[test_resolve_bash_source_edges_relative_path_resolves_against_source_dir()]] - code - graphify/tests/test_symbol_resolution.py
- [[test_resolve_bash_source_edges_skips_bash_function_node_missing_id()]] - code - graphify/tests/test_symbol_resolution.py
- [[test_resolve_bash_source_edges_skips_malformed_source()]] - code - graphify/tests/test_symbol_resolution.py
- [[test_resolve_bash_source_edges_skips_non_dict_lists()]] - code - graphify/tests/test_symbol_resolution.py
- [[test_resolve_bash_source_edges_skips_raw_call_missing_caller_nid()]] - code - graphify/tests/test_symbol_resolution.py
- [[test_resolve_bash_source_edges_skips_unhashable_callee()]] - code - graphify/tests/test_symbol_resolution.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_172
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_Community 187]]
- 4 edges to [[_COMMUNITY_Community 132]]
- 1 edge to [[_COMMUNITY_Community 3]]
- 1 edge to [[_COMMUNITY_Community 27]]
- 1 edge to [[_COMMUNITY_Community 5]]
- 1 edge to [[_COMMUNITY_Community 231]]
- 1 edge to [[_COMMUNITY_Community 248]]
- 1 edge to [[_COMMUNITY_Community 315]]

## Top bridge nodes
- [[resolve_bash_source_edges()]] - degree 20, connects to 4 communities
- [[_file_node_id_for_path()]] - degree 5, connects to 3 communities
- [[Path_53]] - degree 5, connects to 3 communities
- [[test_resolve_bash_source_edges_accepts_none_per_file_entries()]] - degree 3, connects to 1 community
- [[test_resolve_bash_source_edges_relative_path_resolves_against_source_dir()]] - degree 3, connects to 1 community