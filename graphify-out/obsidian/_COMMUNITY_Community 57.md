---
type: community
cohesion: 0.08
members: 42
---

# Community 57

**Cohesion:** 0.08 - loosely connected
**Members:** 42 nodes

## Members
- [[1715 merge_existing=True unions with the prior entry so a file split     acro]] - rationale - graphify/tests/test_cache.py
- [[1757 an undispatched file must keep its complete cache entry when a     seman]] - rationale - graphify/tests/test_cache.py
- [[1757 the per-chunk incremental checkpoint must not let a chunk's     mis-attr]] - rationale - graphify/tests/test_chunking.py
- [[1916 + 1715 with merge_existing=True (the llm.py checkpoint path),     only]] - rationale - graphify/tests/test_cache.py
- [[1950 empty-parse gap a chunk that truncates to an empty parse produces     NO]] - rationale - graphify/tests/test_partial_cache.py
- [[A file sliced across chunks an earlier truncated slice must not be     dropped]] - rationale - graphify/tests/test_partial_cache.py
- [[A truncated file produced output this run but is left unstamped in the     mani]] - rationale - graphify/tests/test_partial_cache.py
- [[Default save_semantic_cache replaces a file's cached entry (the final,     auth]] - rationale - graphify/tests/test_cache.py
- [[Ordering guard once a file is partial (from an empty-parse truncation,     so]] - rationale - graphify/tests/test_partial_cache.py
- [[Return cached extraction for this file if hash matches, else None.      Cache]] - rationale - graphify/graphify/cache.py
- [[Save semantic extraction results to cache, keyed by source_file.      Groups n]] - rationale - graphify/graphify/cache.py
- [[Source files known partial those carrying a ``_partial`` item marker, plus]] - rationale - graphify/graphify/llm.py
- [[Tag every nodeedgehyperedge in a truncated chunk result with an internal]] - rationale - graphify/graphify/llm.py
- [[Tests for partial-extraction cache promotion.  A truncated LLM chunk (`finish_]] - rationale - graphify/tests/test_partial_cache.py
- [[True if any nodeedgehyperedge in a per-file group carries the internal     ``]] - rationale - graphify/graphify/cache.py
- [[_doc()]] - code - graphify/tests/test_partial_cache.py
- [[_group_has_partial_marker()]] - code - graphify/graphify/cache.py
- [[_mark_partial()]] - code - graphify/graphify/llm.py
- [[_partial_source_files must surface a file recorded in _partial_files even     w]] - rationale - graphify/tests/test_partial_cache.py
- [[_partial_source_files()]] - code - graphify/graphify/llm.py
- [[load_cached()]] - code - graphify/graphify/cache.py
- [[merge_existing must not union a pre-fingerprint entry into a write it is     ab]] - rationale - graphify/tests/test_cache.py
- [[save_semantic_cache()]] - code - graphify/graphify/cache.py
- [[test_checkpoint_scopes_cache_writes_to_chunk_files()]] - code - graphify/tests/test_chunking.py
- [[test_clean_slice_does_not_repromote_empty_parse_partial()]] - code - graphify/tests/test_partial_cache.py
- [[test_group_has_partial_marker()]] - code - graphify/tests/test_partial_cache.py
- [[test_intrinsic_partial_marker_makes_entry_a_cache_miss()]] - code - graphify/tests/test_partial_cache.py
- [[test_mark_partial_and_partial_source_files()]] - code - graphify/tests/test_partial_cache.py
- [[test_merge_existing_accumulates_slices_and_stays_partial()]] - code - graphify/tests/test_partial_cache.py
- [[test_non_partial_entry_loads_normally()]] - code - graphify/tests/test_partial_cache.py
- [[test_partial_cache.py]] - code - graphify/tests/test_partial_cache.py
- [[test_partial_entry_self_heals_on_complete_reextraction()]] - code - graphify/tests/test_partial_cache.py
- [[test_partial_files_carries_empty_parse_truncation()]] - code - graphify/tests/test_partial_cache.py
- [[test_partial_source_files_arg_stamps_entry()]] - code - graphify/tests/test_partial_cache.py
- [[test_partial_source_files_empty_when_unmarked()]] - code - graphify/tests/test_partial_cache.py
- [[test_save_semantic_cache_merge_existing_prunes_only_incoming()]] - code - graphify/tests/test_cache.py
- [[test_save_semantic_cache_merge_existing_unions()]] - code - graphify/tests/test_cache.py
- [[test_save_semantic_cache_overwrites_by_default()]] - code - graphify/tests/test_cache.py
- [[test_save_semantic_cache_rejects_out_of_scope_source_file()]] - code - graphify/tests/test_cache.py
- [[test_save_stamps_partial_file_with_no_items()]] - code - graphify/tests/test_partial_cache.py
- [[test_semantic_cache_merge_existing_never_fuses_legacy_vintage()]] - code - graphify/tests/test_cache.py
- [[test_stamped_manifest_excludes_partial_files()]] - code - graphify/tests/test_partial_cache.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_57
SORT file.name ASC
```

## Connections to other communities
- 25 edges to [[_COMMUNITY_Community 31]]
- 12 edges to [[_COMMUNITY_Community 51]]
- 9 edges to [[_COMMUNITY_Community 20]]
- 8 edges to [[_COMMUNITY_Community 174]]
- 7 edges to [[_COMMUNITY_Community 12]]
- 6 edges to [[_COMMUNITY_Community 66]]
- 4 edges to [[_COMMUNITY_Community 58]]
- 3 edges to [[_COMMUNITY_Community 27]]
- 3 edges to [[_COMMUNITY_Community 30]]
- 2 edges to [[_COMMUNITY_Community 208]]
- 2 edges to [[_COMMUNITY_Community 130]]
- 1 edge to [[_COMMUNITY_Community 301]]
- 1 edge to [[_COMMUNITY_Community 3]]
- 1 edge to [[_COMMUNITY_Community 32]]
- 1 edge to [[_COMMUNITY_Community 205]]
- 1 edge to [[_COMMUNITY_Community 274]]
- 1 edge to [[_COMMUNITY_Community 93]]

## Top bridge nodes
- [[save_semantic_cache()]] - degree 56, connects to 11 communities
- [[load_cached()]] - degree 44, connects to 9 communities
- [[test_partial_cache.py]] - degree 22, connects to 4 communities
- [[_partial_source_files()]] - degree 7, connects to 2 communities
- [[_mark_partial()]] - degree 4, connects to 2 communities