---
type: community
cohesion: 0.07
members: 46
---

# Community 51

**Cohesion:** 0.07 - loosely connected
**Members:** 46 nodes

## Members
- [[A glob that stopped at the top level would leave every fingerprinted     entry]] - rationale - graphify/tests/test_cache.py
- [[An entry for a file that no longer exists (dropped from the live set) is     pr]] - rationale - graphify/tests/test_cache.py
- [[Changing a file's content leaves the old content-hash entry orphaned;     pruni]] - rationale - graphify/tests/test_cache.py
- [[Fingerprint the caller's extraction prompt, or None when it supplied none.]] - rationale - graphify/graphify/cache.py
- [[Inverse of func`_relativize_source_files_in`.      Re-anchor relative ``sour]] - rationale - graphify/graphify/cache.py
- [[Inverse of func`_stat_key_to_relative`.      Re-anchor a stored relative key]] - rationale - graphify/graphify/cache.py
- [[Mutate ``payload`` to rewrite absolute ``source_file`` fields as     forward-sl]] - rationale - graphify/graphify/cache.py
- [[Path_3]] - code
- [[Prune touches only cachesemantic.json AST entries and atomic-write     .tm]] - rationale - graphify/tests/test_cache.py
- [[Pruning against the FULL live set must keep every live entry — guards     the t]] - rationale - graphify/tests/test_cache.py
- [[Remove AST cache entries left behind by other graphify versions.      Sweeps s]] - rationale - graphify/graphify/cache.py
- [[Remove orphaned semantic cache entries, returning the count pruned.      The s]] - rationale - graphify/graphify/cache.py
- [[Return ``key`` as a forward-slash relative path from ``anchor``.      Local du]] - rationale - graphify/graphify/cache.py
- [[Return ``src`` in portable form backslashes flipped to forward slashes,     th]] - rationale - graphify/graphify/cache.py
- [[Return set of file hashes that have a valid cache entry (any kind).]] - rationale - graphify/graphify/cache.py
- [[Returns the cache directory for ``kind`` - creates it if needed.      kind is]] - rationale - graphify/graphify/cache.py
- [[Save extraction result for this file.      Stores as graphify-outcache{kind}]] - rationale - graphify/graphify/cache.py
- [[The on-disk cache JSON contains forward-slash relative source_file     entries]] - rationale - graphify/tests/test_cache.py
- [[The semantic cache is deliberately not versioned entries are produced     by t]] - rationale - graphify/tests/test_cache.py
- [[Upgrading removes AST entries left behind by previous versions so the     cache]] - rationale - graphify/tests/test_cache.py
- [[_absolutize_source_files_in()]] - code - graphify/graphify/cache.py
- [[_cleanup_stale_ast_entries()]] - code - graphify/graphify/cache.py
- [[_ensure_stat_index()]] - code - graphify/graphify/cache.py
- [[_normalize_source_file_value()]] - code - graphify/graphify/cache.py
- [[_relativize_source_files_in()]] - code - graphify/graphify/cache.py
- [[_resolve_prompt_fp()]] - code - graphify/graphify/cache.py
- [[_stat_index_file()]] - code - graphify/graphify/cache.py
- [[_stat_key_to_absolute()]] - code - graphify/graphify/cache.py
- [[_stat_key_to_relative()]] - code - graphify/graphify/cache.py
- [[``source_file`` for an in-root symlink must be stored under the     symlink's o]] - rationale - graphify/tests/test_cache.py
- [[cache.py]] - code - graphify/graphify/cache.py
- [[cache_dir()]] - code - graphify/graphify/cache.py
- [[cached_files returns the set of cached hashes.]] - rationale - graphify/tests/test_cache.py
- [[cached_files()]] - code - graphify/graphify/cache.py
- [[prune_semantic_cache()]] - code - graphify/graphify/cache.py
- [[save_cached()]] - code - graphify/graphify/cache.py
- [[test_ast_cache_version_bump_cleans_stale_entries()]] - code - graphify/tests/test_cache.py
- [[test_cached_files()]] - code - graphify/tests/test_cache.py
- [[test_save_cached_in_root_symlink_keeps_symlink_name()]] - code - graphify/tests/test_cache.py
- [[test_save_cached_relativizes_source_file()]] - code - graphify/tests/test_cache.py
- [[test_semantic_cache_survives_version_bump()]] - code - graphify/tests/test_cache.py
- [[test_semantic_prune_and_clear_reach_fingerprint_subdirs()]] - code - graphify/tests/test_cache.py
- [[test_semantic_prune_handles_deleted_file()]] - code - graphify/tests/test_cache.py
- [[test_semantic_prune_ignores_ast_and_tmp()]] - code - graphify/tests/test_cache.py
- [[test_semantic_prune_keeps_live_unchanged_entries()]] - code - graphify/tests/test_cache.py
- [[test_semantic_prune_removes_orphan_entries()]] - code - graphify/tests/test_cache.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_51
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_Community 31]]
- 21 edges to [[_COMMUNITY_Community 66]]
- 12 edges to [[_COMMUNITY_Community 57]]
- 6 edges to [[_COMMUNITY_Community 130]]
- 5 edges to [[_COMMUNITY_Community 205]]
- 2 edges to [[_COMMUNITY_Community 274]]
- 2 edges to [[_COMMUNITY_Community 3]]
- 2 edges to [[_COMMUNITY_Community 32]]
- 2 edges to [[_COMMUNITY_Community 12]]
- 1 edge to [[_COMMUNITY_Community 76]]
- 1 edge to [[_COMMUNITY_Community 44]]
- 1 edge to [[_COMMUNITY_Community 208]]
- 1 edge to [[_COMMUNITY_Community 174]]
- 1 edge to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 24]]

## Top bridge nodes
- [[cache.py]] - degree 34, connects to 11 communities
- [[save_cached()]] - degree 29, connects to 8 communities
- [[Path_3]] - degree 20, connects to 4 communities
- [[test_semantic_prune_and_clear_reach_fingerprint_subdirs()]] - degree 7, connects to 4 communities
- [[cache_dir()]] - degree 17, connects to 3 communities