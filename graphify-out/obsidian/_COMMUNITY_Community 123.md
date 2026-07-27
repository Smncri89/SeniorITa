---
type: community
cohesion: 0.12
members: 24
---

# Community 123

**Cohesion:** 0.12 - loosely connected
**Members:** 24 nodes

## Members
- [[build must not match srcbuild.]] - rationale - graphify/tests/test_detect.py
- [[inbox must not match srcinbox — only inbox at the anchor root.]] - rationale - graphify/tests/test_detect.py
- [[inbox must still match inbox at the anchor root (positive case).]] - rationale - graphify/tests/test_detect.py
- [[srcinbox must match srcinbox but not xsrcinbox.]] - rationale - graphify/tests/test_detect.py
- [[A ! re-include cannot un-ignore a file whose parent dir is excluded (882).]] - rationale - graphify/tests/test_detect.py
- [[A ! re-include must still un-ignore a file when no ancestor is excluded (882).]] - rationale - graphify/tests/test_detect.py
- [[A shared _cache must not change _is_ignored results, including negation.]] - rationale - graphify/tests/test_detect.py
- [[If the ancestor dir itself is re-included, its children should not be blocked (]] - rationale - graphify/tests/test_detect.py
- [[Read .graphifyignore files and return (anchor_dir, pattern) pairs.      Patter]] - rationale - graphify/graphify/detect.py
- [[Return True if the path should be ignored per .graphifyignore patterns.      U]] - rationale - graphify/graphify/detect.py
- [[_is_ignored()]] - code - graphify/graphify/detect.py
- [[_load_graphifyignore()]] - code - graphify/graphify/detect.py
- [[inbox (no leading ) must still match srcinbox anywhere in the tree.]] - rationale - graphify/tests/test_detect.py
- [[infoexclude is loaded at lowest priority, so a later .gitignore `!` negation]] - rationale - graphify/tests/test_detect.py
- [[test_anchored_dir_matches_at_root()]] - code - graphify/tests/test_detect.py
- [[test_anchored_dir_not_matched_at_depth()]] - code - graphify/tests/test_detect.py
- [[test_anchored_file_not_matched_at_depth()]] - code - graphify/tests/test_detect.py
- [[test_anchored_multi_segment_pattern()]] - code - graphify/tests/test_detect.py
- [[test_git_info_exclude_ranks_below_gitignore_negation()]] - code - graphify/tests/test_detect.py
- [[test_is_ignored_cache_matches_uncached_results()]] - code - graphify/tests/test_detect.py
- [[test_negation_ancestor_itself_reincluded()]] - code - graphify/tests/test_detect.py
- [[test_negation_cannot_rescue_file_under_excluded_dir()]] - code - graphify/tests/test_detect.py
- [[test_negation_works_when_no_ancestor_excluded()]] - code - graphify/tests/test_detect.py
- [[test_unanchored_dir_still_matches_at_depth()]] - code - graphify/tests/test_detect.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_123
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_Community 1]]
- 6 edges to [[_COMMUNITY_Community 44]]
- 6 edges to [[_COMMUNITY_Community 0]]
- 4 edges to [[_COMMUNITY_Community 15]]
- 2 edges to [[_COMMUNITY_Community 24]]
- 2 edges to [[_COMMUNITY_Community 3]]
- 2 edges to [[_COMMUNITY_Community 32]]
- 1 edge to [[_COMMUNITY_Community 335]]

## Top bridge nodes
- [[_is_ignored()]] - degree 23, connects to 8 communities
- [[_load_graphifyignore()]] - degree 26, connects to 7 communities
- [[test_anchored_dir_matches_at_root()]] - degree 4, connects to 1 community
- [[test_anchored_dir_not_matched_at_depth()]] - degree 4, connects to 1 community
- [[test_anchored_file_not_matched_at_depth()]] - degree 4, connects to 1 community