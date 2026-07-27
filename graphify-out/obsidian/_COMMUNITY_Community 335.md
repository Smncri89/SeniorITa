---
type: community
cohesion: 0.33
members: 4
---

# Community 335

**Cohesion:** 0.33 - loosely connected
**Members:** 4 nodes

## Members
- [[A single `!` re-include must not switch off pruning of unrelated ignored dirs.]] - rationale - graphify/tests/test_detect.py
- [[Siblings under the same subtree must share the cached parent result (1235).]] - rationale - graphify/tests/test_detect.py
- [[test_is_ignored_cache_evaluates_each_dir_once()]] - code - graphify/tests/test_detect.py
- [[test_negation_does_not_disable_directory_pruning()]] - code - graphify/tests/test_detect.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_335
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 123]]

## Top bridge nodes
- [[test_is_ignored_cache_evaluates_each_dir_once()]] - degree 3, connects to 2 communities
- [[test_negation_does_not_disable_directory_pruning()]] - degree 2, connects to 1 community