---
type: community
cohesion: 1.00
members: 2
---

# Community 529

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[(fix B) Two provenance-less records sharing an ID must NOT cross-pollinate]] - rationale - graphify/tests/test_dedup.py
- [[test_dedup_no_attribute_merge_when_source_file_missing()]] - code - graphify/tests/test_dedup.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_529
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Community 87]]
- 1 edge to [[_COMMUNITY_Community 69]]

## Top bridge nodes
- [[test_dedup_no_attribute_merge_when_source_file_missing()]] - degree 3, connects to 2 communities