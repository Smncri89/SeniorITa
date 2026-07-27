---
type: community
cohesion: 0.14
members: 32
---

# Community 81

**Cohesion:** 0.14 - loosely connected
**Members:** 32 nodes

## Members
- [[F4 global_add must refuse to read a source graph.json that     exceeds the si]] - rationale - graphify/tests/test_global_graph.py
- [[Add or update a project graph in the global graph.      Returns a summary dict]] - rationale - graphify/graphify/global_graph.py
- [[Build a simple nx.Graph from node dicts.]] - rationale - graphify/tests/test_global_graph.py
- [[Edges incident to an external node that gets deduplicated against an     alread]] - rationale - graphify/tests/test_global_graph.py
- [[Remove all nodes tagged with repo_tag from G in-place. Returns count removed.]] - rationale - graphify/graphify/build.py
- [[Return a copy of G with all node IDs prefixed with repo_tag.      Labels are]] - rationale - graphify/graphify/build.py
- [[Tests for the global graph infrastructure (graphifyglobal_graph.py), prefixpr]] - rationale - graphify/tests/test_global_graph.py
- [[_graph_to_json()]] - code - graphify/tests/test_global_graph.py
- [[_load_global_graph()]] - code - graphify/graphify/global_graph.py
- [[_make_graph()_2]] - code - graphify/tests/test_global_graph.py
- [[global_add()]] - code - graphify/graphify/global_graph.py
- [[merge-graphs should prefix node IDs with repo name to avoid silent collision.]] - rationale - graphify/tests/test_global_graph.py
- [[prefix_graph_for_global()]] - code - graphify/graphify/build.py
- [[prune_repo_from_graph()]] - code - graphify/graphify/build.py
- [[test_dedup_ok_with_no_repo_attr()]] - code - graphify/tests/test_global_graph.py
- [[test_dedup_ok_with_single_repo()]] - code - graphify/tests/test_global_graph.py
- [[test_dedup_raises_on_cross_repo_nodes()]] - code - graphify/tests/test_global_graph.py
- [[test_global_add_collision_warning()]] - code - graphify/tests/test_global_graph.py
- [[test_global_add_creates_global_graph()]] - code - graphify/tests/test_global_graph.py
- [[test_global_add_rejects_oversized_source_graph()]] - code - graphify/tests/test_global_graph.py
- [[test_global_add_rewires_edges_to_deduplicated_externals()]] - code - graphify/tests/test_global_graph.py
- [[test_global_add_skip_on_unchanged_hash()]] - code - graphify/tests/test_global_graph.py
- [[test_global_add_two_repos_no_collision()]] - code - graphify/tests/test_global_graph.py
- [[test_global_graph.py]] - code - graphify/tests/test_global_graph.py
- [[test_global_remove()]] - code - graphify/tests/test_global_graph.py
- [[test_global_remove_unknown_tag_raises()]] - code - graphify/tests/test_global_graph.py
- [[test_merge_graphs_prefixes_ids()]] - code - graphify/tests/test_global_graph.py
- [[test_prefix_graph_preserves_label()]] - code - graphify/tests/test_global_graph.py
- [[test_prefix_graph_rewrites_edges()]] - code - graphify/tests/test_global_graph.py
- [[test_prefix_graph_sets_repo_and_local_id()]] - code - graphify/tests/test_global_graph.py
- [[test_prune_repo_removes_correct_nodes()]] - code - graphify/tests/test_global_graph.py
- [[test_prune_repo_returns_zero_if_not_present()]] - code - graphify/tests/test_global_graph.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_81
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_Community 12]]
- 4 edges to [[_COMMUNITY_Community 87]]
- 2 edges to [[_COMMUNITY_Community 34]]
- 2 edges to [[_COMMUNITY_Community 36]]
- 1 edge to [[_COMMUNITY_Community 101]]

## Top bridge nodes
- [[_load_global_graph()]] - degree 8, connects to 3 communities
- [[test_global_graph.py]] - degree 27, connects to 2 communities
- [[global_add()]] - degree 21, connects to 2 communities
- [[prefix_graph_for_global()]] - degree 11, connects to 2 communities
- [[prune_repo_from_graph()]] - degree 8, connects to 2 communities