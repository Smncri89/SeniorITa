---
type: community
cohesion: 0.06
members: 38
---

# Community 66

**Cohesion:** 0.06 - loosely connected
**Members:** 38 nodes

## Members
- [[1656 — word counts are cached against each file's stat signature so detect() d]] - rationale - graphify/tests/test_word_count_cache.py
- [[1894 follow-up to 1527 prune must sweep cachesemantic AND     cachesemant]] - rationale - graphify/tests/test_cache.py
- [[1916 guard-rail unscoped callers (allowed_source_files=None) must stay     by]] - rationale - graphify/tests/test_cache.py
- [[1989 the stat-index memo must be keyed by the salt (path relative to     root]] - rationale - graphify/tests/test_word_count_cache.py
- [[A .md file with no frontmatter is hashed by its full content.]] - rationale - graphify/tests/test_cache.py
- [[A pre-1989 entry carrying a bare hash (no salt) is never trusted.]] - rationale - graphify/tests/test_word_count_cache.py
- [[Cache entries written by an older graphify (with absolute source_file     insid]] - rationale - graphify/tests/test_cache.py
- [[Changing only frontmatter fields in a .md file does not change the hash.]] - rationale - graphify/tests/test_cache.py
- [[Changing the body of a .md file produces a different hash.]] - rationale - graphify/tests/test_cache.py
- [[Different file contents give different hashes.]] - rationale - graphify/tests/test_cache.py
- [[Editing content above a mid-document ``----`` break must change the     hash --]] - rationale - graphify/tests/test_cache.py
- [[Entries written by pre-versioning graphify (flat cache or unversioned     cach]] - rationale - graphify/tests/test_cache.py
- [[Non-.md files are still hashed by their full content.]] - rationale - graphify/tests/test_cache.py
- [[Normalize path for consistent cache keys across Windows path spellings.]] - rationale - graphify/graphify/cache.py
- [[SHA256 of file contents + path relative to root.      Uses a stat-based fastpa]] - rationale - graphify/graphify/cache.py
- [[Same file gives same hash on repeated calls.]] - rationale - graphify/tests/test_cache.py
- [[Word count with the same (size, mtime_ns) stat-fastpath cache as     func`fil]] - rationale - graphify/graphify/cache.py
- [[_normalize_path()]] - code - graphify/graphify/cache.py
- [[cached_files reports deep-namespace entries too.]] - rationale - graphify/tests/test_cache.py
- [[cached_word_count()]] - code - graphify/graphify/cache.py
- [[file_hash()]] - code - graphify/graphify/cache.py
- [[test_cached_files_includes_deep_namespace()]] - code - graphify/tests/test_cache.py
- [[test_file_hash_changes()]] - code - graphify/tests/test_cache.py
- [[test_file_hash_consistent()]] - code - graphify/tests/test_cache.py
- [[test_file_hash_ignores_legacy_unsalted_entry()]] - code - graphify/tests/test_word_count_cache.py
- [[test_file_hash_is_order_independent_across_roots()]] - code - graphify/tests/test_word_count_cache.py
- [[test_legacy_unversioned_ast_entries_not_served()]] - code - graphify/tests/test_cache.py
- [[test_load_cached_passes_through_legacy_absolute_source_file()]] - code - graphify/tests/test_cache.py
- [[test_md_body_change_different_hash()]] - code - graphify/tests/test_cache.py
- [[test_md_edit_above_hr_changes_hash()]] - code - graphify/tests/test_cache.py
- [[test_md_frontmatter_only_change_same_hash()]] - code - graphify/tests/test_cache.py
- [[test_md_no_frontmatter_hashed_normally()]] - code - graphify/tests/test_cache.py
- [[test_non_md_file_hashed_fully()]] - code - graphify/tests/test_cache.py
- [[test_save_semantic_cache_unscoped_preserves_dangling_refs_verbatim()]] - code - graphify/tests/test_cache.py
- [[test_semantic_prune_sweeps_both_namespaces_against_same_live_set()]] - code - graphify/tests/test_cache.py
- [[test_word_count_augments_existing_hash_entry()]] - code - graphify/tests/test_word_count_cache.py
- [[test_word_count_cache.py]] - code - graphify/tests/test_word_count_cache.py
- [[test_word_count_cached_until_file_changes()]] - code - graphify/tests/test_word_count_cache.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_66
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_Community 51]]
- 16 edges to [[_COMMUNITY_Community 31]]
- 6 edges to [[_COMMUNITY_Community 57]]
- 5 edges to [[_COMMUNITY_Community 130]]
- 2 edges to [[_COMMUNITY_Community 12]]
- 2 edges to [[_COMMUNITY_Community 208]]
- 1 edge to [[_COMMUNITY_Community 301]]
- 1 edge to [[_COMMUNITY_Community 274]]
- 1 edge to [[_COMMUNITY_Community 174]]

## Top bridge nodes
- [[file_hash()]] - degree 43, connects to 8 communities
- [[test_cached_files_includes_deep_namespace()]] - degree 5, connects to 3 communities
- [[test_load_cached_passes_through_legacy_absolute_source_file()]] - degree 5, connects to 3 communities
- [[test_save_semantic_cache_unscoped_preserves_dangling_refs_verbatim()]] - degree 5, connects to 3 communities
- [[test_semantic_prune_sweeps_both_namespaces_against_same_live_set()]] - degree 5, connects to 3 communities