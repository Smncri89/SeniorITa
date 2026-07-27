---
type: community
cohesion: 0.18
members: 23
---

# Community 130

**Cohesion:** 0.18 - loosely connected
**Members:** 23 nodes

## Members
- [[2197 an item whose source_file is absolute is persisted root-relative     pos]] - rationale - graphify/tests/test_stat_index_portability.py
- [[2199 — stat-index.json must be portable and self-pruning.  The on-disk stat i]] - rationale - graphify/tests/test_stat_index_portability.py
- [[A Windows-shaped absolute source_file (backslash separators) must be     slash-]] - rationale - graphify/tests/test_stat_index_portability.py
- [[A pre-2199 index keyed by absolute paths still HITS on the unmoved     root, a]] - rationale - graphify/tests/test_stat_index_portability.py
- [[Path_100]] - code
- [[Run A under tmpa, copy the corpus (with graphify-out) to tmpb run B     mus]] - rationale - graphify/tests/test_stat_index_portability.py
- [[The stat-index locationanchor are chosen once per process via module     globa]] - rationale - graphify/tests/test_stat_index_portability.py
- [[When an old absolute key and a new relative key resolve to the same     file, t]] - rationale - graphify/tests/test_stat_index_portability.py
- [[Wrap Path.read_bytes with a call counter (file_hash's content read).]] - rationale - graphify/tests/test_stat_index_portability.py
- [[_count_read_bytes()]] - code - graphify/tests/test_stat_index_portability.py
- [[_fail_compute()]] - code - graphify/tests/test_stat_index_portability.py
- [[_flush_stat_index()]] - code - graphify/graphify/cache.py
- [[_read_index()]] - code - graphify/tests/test_stat_index_portability.py
- [[_reset_stat_index()_1]] - code - graphify/tests/test_stat_index_portability.py
- [[_stat_index_path()]] - code - graphify/tests/test_stat_index_portability.py
- [[test_cache_hits_survive_corpus_move()]] - code - graphify/tests/test_stat_index_portability.py
- [[test_deleted_entries_are_pruned_on_flush()]] - code - graphify/tests/test_stat_index_portability.py
- [[test_legacy_absolute_index_migrates_gracefully()]] - code - graphify/tests/test_stat_index_portability.py
- [[test_out_of_root_key_round_trips_absolute()]] - code - graphify/tests/test_stat_index_portability.py
- [[test_relative_key_wins_over_colliding_legacy_absolute()]] - code - graphify/tests/test_stat_index_portability.py
- [[test_semantic_cache_normalizes_absolute_source_file()]] - code - graphify/tests/test_stat_index_portability.py
- [[test_semantic_cache_normalizes_backslash_poisoned_source_file()]] - code - graphify/tests/test_stat_index_portability.py
- [[test_stat_index_portability.py]] - code - graphify/tests/test_stat_index_portability.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_130
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Community 51]]
- 5 edges to [[_COMMUNITY_Community 66]]
- 2 edges to [[_COMMUNITY_Community 57]]
- 1 edge to [[_COMMUNITY_Community 301]]
- 1 edge to [[_COMMUNITY_Community 208]]
- 1 edge to [[_COMMUNITY_Community 31]]

## Top bridge nodes
- [[test_stat_index_portability.py]] - degree 15, connects to 2 communities
- [[_flush_stat_index()]] - degree 9, connects to 2 communities
- [[test_semantic_cache_normalizes_absolute_source_file()]] - degree 5, connects to 2 communities
- [[test_cache_hits_survive_corpus_move()]] - degree 9, connects to 1 community
- [[test_legacy_absolute_index_migrates_gracefully()]] - degree 8, connects to 1 community