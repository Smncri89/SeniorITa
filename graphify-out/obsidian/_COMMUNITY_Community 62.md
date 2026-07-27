---
type: community
cohesion: 0.06
members: 39
---

# Community 62

**Cohesion:** 0.06 - loosely connected
**Members:** 39 nodes

## Members
- [[A lone generic-word exact match must not bury a multi-term match.      Reprodu]] - rationale - graphify/tests/test_serve.py
- [[A multi-word query equal to a whole label must resolve uniquely.      Regressi]] - rationale - graphify/tests/test_serve.py
- [[Across many deterministic random graphs and many random multi-term     queries,]] - rationale - graphify/tests/test_serve.py
- [[Combined query scorer returning the existing ranked `(score, node_id)` list.]] - rationale - graphify/graphify/serve.py
- [[Coverage scaling must not touch full-coverage queries (coverage == 1).      A]] - rationale - graphify/tests/test_serve.py
- [[Guard against a per-label multiplicity penalty leaking into _score_nodes     (s]] - rationale - graphify/tests/test_serve.py
- [[IDF results are stored in G.graph so repeated queries don't recompute.]] - rationale - graphify/tests/test_serve.py
- [[Per-token winner the single-pass scorer records matches the legacy     `_score_]] - rationale - graphify/tests/test_serve.py
- [[Reproducible broad-match DiGraph short constructed labels + edge noise._1]] - rationale - graphify/tests/test_serve.py
- [[Searching for '路由' should match a node with label containing '路由'.]] - rationale - graphify/tests/test_serve.py
- [[Test-only oracle for the legacy per-term `_pick_seeds(terms=...)` loop.      R]] - rationale - graphify/tests/test_serve.py
- [[The seeds produced by `_pick_seeds(qs.ranked, G=G, best_seed_by_term=     qs.be]] - rationale - graphify/tests/test_serve.py
- [[Two separate graph instances must not share an IDF cache.]] - rationale - graphify/tests/test_serve.py
- [[When the trigram prefilter falls back to a full-graph scan, the     single-pass]] - rationale - graphify/tests/test_serve.py
- [[_make_random_scoring_graph()]] - code - graphify/tests/test_serve.py
- [[_reference_best_seed_by_term()]] - code - graphify/tests/test_serve.py
- [[_score_nodes()]] - code - graphify/graphify/serve.py
- [[`_query_graph_text` must invoke `_score_query` exactly once per query,     rega]] - rationale - graphify/tests/test_serve.py
- [[`_score_query(..., collect_per_term_seeds=False).ranked` is the byte-for-     b]] - rationale - graphify/tests/test_serve.py
- [[`collect_per_term_seeds=False` returns empty `best_seed_by_term` and     does n]] - rationale - graphify/tests/test_serve.py
- [[parametrize_22]] - code
- [[test_idf_cached_on_graph()]] - code - graphify/tests/test_serve.py
- [[test_idf_new_graph_starts_fresh()]] - code - graphify/tests/test_serve.py
- [[test_pick_seeds_with_optimized_best_seed_matches_legacy_semantics()]] - code - graphify/tests/test_serve.py
- [[test_query_graph_text_makes_exactly_one_score_query_call()]] - code - graphify/tests/test_serve.py
- [[test_score_nodes_chinese_substring_match()]] - code - graphify/tests/test_serve.py
- [[test_score_nodes_coverage_full_coverage_query_is_unchanged()]] - code - graphify/tests/test_serve.py
- [[test_score_nodes_coverage_lone_generic_exact_hit_loses_to_multi_term_match()]] - code - graphify/tests/test_serve.py
- [[test_score_nodes_exact_label_match()]] - code - graphify/tests/test_serve.py
- [[test_score_nodes_ignores_trailing_punctuation()]] - code - graphify/tests/test_serve.py
- [[test_score_nodes_multiword_exact_label_outranks_superset()]] - code - graphify/tests/test_serve.py
- [[test_score_nodes_no_match()]] - code - graphify/tests/test_serve.py
- [[test_score_nodes_scores_identical_labels_equally()]] - code - graphify/tests/test_serve.py
- [[test_score_nodes_source_file_partial()]] - code - graphify/tests/test_serve.py
- [[test_score_query_best_seed_by_term_matches_legacy_singleton_scoring()]] - code - graphify/tests/test_serve.py
- [[test_score_query_collect_per_term_seeds_false_omits_tracking()]] - code - graphify/tests/test_serve.py
- [[test_score_query_matches_legacy_across_random_deterministic_graphs()]] - code - graphify/tests/test_serve.py
- [[test_score_query_matches_legacy_under_full_scan_fallback()]] - code - graphify/tests/test_serve.py
- [[test_score_query_ranked_matches_score_nodes_byte_identical()]] - code - graphify/tests/test_serve.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_62
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_Community 41]]
- 10 edges to [[_COMMUNITY_Community 98]]
- 8 edges to [[_COMMUNITY_Community 67]]
- 4 edges to [[_COMMUNITY_Community 156]]
- 4 edges to [[_COMMUNITY_Community 144]]
- 3 edges to [[_COMMUNITY_Community 101]]
- 2 edges to [[_COMMUNITY_Community 12]]
- 1 edge to [[_COMMUNITY_Community 312]]

## Top bridge nodes
- [[_score_nodes()]] - degree 28, connects to 5 communities
- [[test_pick_seeds_with_optimized_best_seed_matches_legacy_semantics()]] - degree 7, connects to 3 communities
- [[test_score_query_matches_legacy_across_random_deterministic_graphs()]] - degree 7, connects to 3 communities
- [[test_query_graph_text_makes_exactly_one_score_query_call()]] - degree 6, connects to 3 communities
- [[test_score_nodes_coverage_full_coverage_query_is_unchanged()]] - degree 5, connects to 3 communities