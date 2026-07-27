---
type: community
cohesion: 0.09
members: 48
---

# Community 49

**Cohesion:** 0.09 - loosely connected
**Members:** 48 nodes

## Members
- [[1423 `graphify extract` honours GRAPHIFY_OUT for where it WRITES, not only]] - rationale - graphify/tests/test_cli_export.py
- [[1747 Case 1 `extract corpus --out elsewhere` must not leave a stray     g]] - rationale - graphify/tests/test_cli_export.py
- [[1747 Case 2 `cluster-only --graph elsewheregraphify-outgraph.json`     mu]] - rationale - graphify/tests/test_cli_export.py
- [[Build a minimal graph.json + analysislabels files in tmp_pathgraphify-out.]] - rationale - graphify/tests/test_cli_export.py
- [[CompletedProcess]] - code
- [[If a graph.json was somehow written without any per-node `community`     attrib]] - rationale - graphify/tests/test_cli_export.py
- [[Integration tests for graphify export subcommands and CLI commands.  Each test]] - rationale - graphify/tests/test_cli_export.py
- [[Path_64]] - code
- [[Stronger assertion the reconstructed `communities` dict should have the     SA]] - rationale - graphify/tests/test_cli_export.py
- [[When .graphify_analysis.json is absent, export html should reconstruct     comm]] - rationale - graphify/tests/test_cli_export.py
- [[_make_graph()_1]] - code - graphify/tests/test_cli_export.py
- [[_run()_1]] - code - graphify/tests/test_cli_export.py
- [[cluster-only must invoke remap_communities_to_previous so the existing     .gra]] - rationale - graphify/tests/test_cli_export.py
- [[cluster-only must not crash with FileNotFoundError when graphify-out is absent]] - rationale - graphify/tests/test_cli_export.py
- [[cluster-only must refresh .graphify_analysis.json alongside graph.json.      D]] - rationale - graphify/tests/test_cli_export.py
- [[test_cli_export.py]] - code - graphify/tests/test_cli_export.py
- [[test_cluster_only_creates_output_dir_when_missing()]] - code - graphify/tests/test_cli_export.py
- [[test_cluster_only_graph_in_graphify_out_writes_beside_it()]] - code - graphify/tests/test_cli_export.py
- [[test_cluster_only_persists_analysis_sidecar()]] - code - graphify/tests/test_cli_export.py
- [[test_cluster_only_remaps_labels_to_previous_cids()]] - code - graphify/tests/test_cli_export.py
- [[test_explain_missing_graph_fails()]] - code - graphify/tests/test_cli_export.py
- [[test_explain_runs_without_error()]] - code - graphify/tests/test_cli_export.py
- [[test_explain_uses_graphify_out_env()]] - code - graphify/tests/test_cli_export.py
- [[test_export_falkordb_creates_cypher()]] - code - graphify/tests/test_cli_export.py
- [[test_export_graphml_creates_file()]] - code - graphify/tests/test_cli_export.py
- [[test_export_html_creates_file()]] - code - graphify/tests/test_cli_export.py
- [[test_export_html_error_without_graph()]] - code - graphify/tests/test_cli_export.py
- [[test_export_html_fallback_recovers_multiple_communities()]] - code - graphify/tests/test_cli_export.py
- [[test_export_html_falls_back_to_node_community_attribute()]] - code - graphify/tests/test_cli_export.py
- [[test_export_html_no_community_data_at_all_still_succeeds()]] - code - graphify/tests/test_cli_export.py
- [[test_export_html_no_viz_removes_file()]] - code - graphify/tests/test_cli_export.py
- [[test_export_neo4j_creates_cypher()]] - code - graphify/tests/test_cli_export.py
- [[test_export_obsidian_creates_vault()]] - code - graphify/tests/test_cli_export.py
- [[test_export_obsidian_custom_dir()]] - code - graphify/tests/test_cli_export.py
- [[test_export_unknown_format_fails()]] - code - graphify/tests/test_cli_export.py
- [[test_export_wiki_accepts_edges_only_graph_json()]] - code - graphify/tests/test_cli_export.py
- [[test_export_wiki_creates_articles()]] - code - graphify/tests/test_cli_export.py
- [[test_extract_out_does_not_pollute_corpus()]] - code - graphify/tests/test_cli_export.py
- [[test_extract_writes_to_graphify_out_env()]] - code - graphify/tests/test_cli_export.py
- [[test_path_missing_graph_fails()]] - code - graphify/tests/test_cli_export.py
- [[test_path_runs_without_error()]] - code - graphify/tests/test_cli_export.py
- [[test_path_uses_graphify_out_env()]] - code - graphify/tests/test_cli_export.py
- [[test_query_budget_flag()]] - code - graphify/tests/test_cli_export.py
- [[test_query_dfs_flag()]] - code - graphify/tests/test_cli_export.py
- [[test_query_missing_graph_fails()]] - code - graphify/tests/test_cli_export.py
- [[test_query_returns_output()]] - code - graphify/tests/test_cli_export.py
- [[test_query_uses_graphify_out_env()]] - code - graphify/tests/test_cli_export.py
- [[test_update_no_cluster_writes_raw_graph()]] - code - graphify/tests/test_cli_export.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_49
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 59]]
- 4 edges to [[_COMMUNITY_Community 19]]
- 2 edges to [[_COMMUNITY_Community 10]]
- 2 edges to [[_COMMUNITY_Community 35]]
- 1 edge to [[_COMMUNITY_Community 334]]

## Top bridge nodes
- [[test_cli_export.py]] - degree 42, connects to 5 communities
- [[_make_graph()_1]] - degree 33, connects to 4 communities