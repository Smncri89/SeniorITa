---
type: community
cohesion: 0.25
members: 11
---

# Community 237

**Cohesion:** 0.25 - loosely connected
**Members:** 11 nodes

## Members
- [[.test_basic_grouping()]] - code - graphify/tests/test_prs.py
- [[.test_empty_nodes()]] - code - graphify/tests/test_prs.py
- [[.test_no_community_field_skipped()]] - code - graphify/tests/test_prs.py
- [[.test_top_n_capped()]] - code - graphify/tests/test_prs.py
- [[Fetch PR file lists concurrently, compute graph impact, return community labels.]] - rationale - graphify/graphify/prs.py
- [[Path_47]] - code
- [[Return {community_id top_labels} extracted from graph node data.]] - rationale - graphify/graphify/prs.py
- [[TestBuildCommunityLabels]] - code - graphify/tests/test_prs.py
- [[_load_graph_json()]] - code - graphify/graphify/prs.py
- [[attach_graph_impact()]] - code - graphify/graphify/prs.py
- [[build_community_labels()]] - code - graphify/graphify/prs.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_237
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Community 117]]
- 4 edges to [[_COMMUNITY_Community 126]]
- 1 edge to [[_COMMUNITY_Community 135]]
- 1 edge to [[_COMMUNITY_Community 293]]
- 1 edge to [[_COMMUNITY_Community 36]]

## Top bridge nodes
- [[attach_graph_impact()]] - degree 9, connects to 4 communities
- [[build_community_labels()]] - degree 8, connects to 2 communities
- [[_load_graph_json()]] - degree 4, connects to 2 communities
- [[TestBuildCommunityLabels]] - degree 6, connects to 1 community
- [[Path_47]] - degree 3, connects to 1 community