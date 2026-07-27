---
type: community
cohesion: 0.09
members: 45
---

# Community 52

**Cohesion:** 0.09 - loosely connected
**Members:** 45 nodes

## Members
- [[2073 --no-label must not write .graphify_labels.json with 'Community N'     p]] - rationale - graphify/tests/test_labeling.py
- [[2073 an already-polluted sidecar (a placeholder for one community, a     genu]] - rationale - graphify/tests/test_labeling.py
- [[CLI entry point resolve a backend, name communities, and degrade to     ``Comm]] - rationale - graphify/graphify/llm.py
- [[Concurrency must not change the result same cid-name map either way.]] - rationale - graphify/tests/test_labeling.py
- [[One prompt line per community (largest first), sampling up to ``top_k``     rep]] - rationale - graphify/graphify/llm.py
- [[Return a complete ``{cid name}`` map using ``backend`` for naming.      Commu]] - rationale - graphify/graphify/llm.py
- [[Tests for LLM-backed community labeling (issue 1097).  Backend calls are mock]] - rationale - graphify/tests/test_labeling.py
- [[Two disconnected components - two stable communities, each hub-labelled     by]] - rationale - graphify/tests/test_labeling.py
- [[_community_label_lines()]] - code - graphify/graphify/llm.py
- [[_graph()]] - code - graphify/tests/test_labeling.py
- [[_many_communities()]] - code - graphify/tests/test_labeling.py
- [[_peak_tracker()]] - code - graphify/tests/test_labeling.py
- [[_placeholder_community_labels()]] - code - graphify/graphify/llm.py
- [[_two_community_graph()]] - code - graphify/tests/test_labeling.py
- [[_wide_graph()]] - code - graphify/tests/test_labeling.py
- [[generate_community_labels()]] - code - graphify/graphify/llm.py
- [[god_nodes() returns listdict with an 'id' key, not bare ids.]] - rationale - graphify/tests/test_labeling.py
- [[label_communities()]] - code - graphify/graphify/llm.py
- [[ollamaclaude-cli must stay serial regardless of --max-concurrency.]] - rationale - graphify/tests/test_labeling.py
- [[test_cluster_only_heals_persisted_placeholder_but_reuses_genuine()]] - code - graphify/tests/test_labeling.py
- [[test_cluster_only_no_label_does_not_persist_placeholders()]] - code - graphify/tests/test_labeling.py
- [[test_empty_communities_returns_placeholders()]] - code - graphify/tests/test_labeling.py
- [[test_generate_community_labels_degrades_on_error()]] - code - graphify/tests/test_labeling.py
- [[test_generate_community_labels_no_backend()]] - code - graphify/tests/test_labeling.py
- [[test_generate_community_labels_success()]] - code - graphify/tests/test_labeling.py
- [[test_gods_as_dicts_do_not_crash()]] - code - graphify/tests/test_labeling.py
- [[test_label_cli_missing_only_preserves_existing_labels()]] - code - graphify/tests/test_labeling.py
- [[test_label_cli_passes_model_override()]] - code - graphify/tests/test_labeling.py
- [[test_label_communities_accumulates_token_usage()]] - code - graphify/tests/test_labeling.py
- [[test_label_communities_all_batches_fail_raises()]] - code - graphify/tests/test_labeling.py
- [[test_label_communities_batch_size_controls_batch_count()]] - code - graphify/tests/test_labeling.py
- [[test_label_communities_batches_when_over_batch_size()]] - code - graphify/tests/test_labeling.py
- [[test_label_communities_counts_tokens_for_failed_batch()]] - code - graphify/tests/test_labeling.py
- [[test_label_communities_forces_serial_for_ollama()]] - code - graphify/tests/test_labeling.py
- [[test_label_communities_happy_path()]] - code - graphify/tests/test_labeling.py
- [[test_label_communities_malformed_raises()]] - code - graphify/tests/test_labeling.py
- [[test_label_communities_max_communities_caps_total()]] - code - graphify/tests/test_labeling.py
- [[test_label_communities_parallel_matches_sequential()]] - code - graphify/tests/test_labeling.py
- [[test_label_communities_partial_batch_failure_keeps_successful_batches()]] - code - graphify/tests/test_labeling.py
- [[test_label_communities_partial_reply_fills_placeholder()]] - code - graphify/tests/test_labeling.py
- [[test_label_communities_passes_model_override()]] - code - graphify/tests/test_labeling.py
- [[test_label_communities_runs_batches_concurrently()]] - code - graphify/tests/test_labeling.py
- [[test_label_communities_salvages_truncated_reply()]] - code - graphify/tests/test_labeling.py
- [[test_label_communities_strips_code_fences()]] - code - graphify/tests/test_labeling.py
- [[test_labeling.py]] - code - graphify/tests/test_labeling.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_52
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Community 58]]
- 2 edges to [[_COMMUNITY_Community 12]]
- 1 edge to [[_COMMUNITY_Community 39]]

## Top bridge nodes
- [[generate_community_labels()]] - degree 11, connects to 3 communities
- [[test_labeling.py]] - degree 34, connects to 1 community
- [[label_communities()]] - degree 24, connects to 1 community
- [[_community_label_lines()]] - degree 3, connects to 1 community
- [[_placeholder_community_labels()]] - degree 3, connects to 1 community