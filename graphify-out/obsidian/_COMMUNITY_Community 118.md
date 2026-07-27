---
type: community
cohesion: 0.10
members: 25
---

# Community 118

**Cohesion:** 0.10 - loosely connected
**Members:** 25 nodes

## Members
- [[A graph large enough that the selectivity guard lets the fast-path fire for]] - rationale - graphify/tests/test_serve.py
- [[Character trigrams of `text`; for 3-char text the whole string is the key.]] - rationale - graphify/graphify/serve.py
- [[Disable the prefilter so a call exercises the original full-node scan.]] - rationale - graphify/tests/test_serve.py
- [[Lazily build and cache a trigram - node-position postings map on the graph.]] - rationale - graphify/graphify/serve.py
- [[Node IDs whose text could contain any `needle` as a substring, via the     trig]] - rationale - graphify/graphify/serve.py
- [[Return node IDs whose label or ID matches the search term (diacritic-insensitive]] - rationale - graphify/graphify/serve.py
- [[_find_node()]] - code - graphify/graphify/serve.py
- [[_force_full_scan()]] - code - graphify/tests/test_serve.py
- [[_get_trigram_index()]] - code - graphify/graphify/serve.py
- [[_make_big_graph()]] - code - graphify/tests/test_serve.py
- [[_trigram_candidates()]] - code - graphify/graphify/serve.py
- [[_trigrams()]] - code - graphify/graphify/serve.py
- [[test_find_node_ignores_trailing_punctuation()]] - code - graphify/tests/test_serve.py
- [[test_find_node_label_tokens_branch_covered_by_index()]] - code - graphify/tests/test_serve.py
- [[test_find_node_matches_full_punctuated_unicode_label()]] - code - graphify/tests/test_serve.py
- [[test_find_node_matches_punctuated_file_label_exactly()]] - code - graphify/tests/test_serve.py
- [[test_find_node_prefilter_is_identical_to_full_scan()]] - code - graphify/tests/test_serve.py
- [[test_find_node_resolves_when_label_and_norm_label_diverge()]] - code - graphify/tests/test_serve.py
- [[test_find_node_source_file_path_prefers_file_level_node()]] - code - graphify/tests/test_serve.py
- [[test_node_search_text_includes_all_matched_fields()]] - code - graphify/tests/test_serve.py
- [[test_trigram_candidates_falls_back_on_common_term()]] - code - graphify/tests/test_serve.py
- [[test_trigram_candidates_falls_back_on_short_token()]] - code - graphify/tests/test_serve.py
- [[test_trigram_candidates_fast_path_fires_for_rare_term()]] - code - graphify/tests/test_serve.py
- [[test_trigram_index_cached_and_rebuilt_per_graph()]] - code - graphify/tests/test_serve.py
- [[test_trigrams_basic()]] - code - graphify/tests/test_serve.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_118
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_Community 41]]
- 8 edges to [[_COMMUNITY_Community 98]]
- 4 edges to [[_COMMUNITY_Community 101]]
- 3 edges to [[_COMMUNITY_Community 156]]
- 2 edges to [[_COMMUNITY_Community 12]]
- 2 edges to [[_COMMUNITY_Community 95]]
- 1 edge to [[_COMMUNITY_Community 67]]

## Top bridge nodes
- [[_find_node()]] - degree 17, connects to 5 communities
- [[_get_trigram_index()]] - degree 9, connects to 3 communities
- [[_make_big_graph()]] - degree 12, connects to 2 communities
- [[_trigram_candidates()]] - degree 10, connects to 2 communities
- [[_trigrams()]] - degree 6, connects to 2 communities