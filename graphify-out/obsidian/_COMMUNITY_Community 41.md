---
type: community
cohesion: 0.06
members: 50
---

# Community 41

**Cohesion:** 0.06 - loosely connected
**Members:** 50 nodes

## Members
- [[A non-decode ValueError (e.g. a non-.json path) must still print the     generi]] - rationale - graphify/tests/test_serve.py
- [[Chinese text should use the cached jieba module and keep the original term.]] - rationale - graphify/tests/test_serve.py
- [[End-to-end for 1900 a German question over a graph with German     heading-no]] - rationale - graphify/tests/test_serve.py
- [[Japanese kana and Hangul are kept as terms but not segmented as Chinese.]] - rationale - graphify/tests/test_serve.py
- [[Mixed Chinese and English text should be handled correctly.]] - rationale - graphify/tests/test_serve.py
- [[Reconstruct community dict from community property stored on nodes.]] - rationale - graphify/graphify/serve.py
- [[Render pre-built lines under the same ~3-charstoken budget rule as     _subgra]] - rationale - graphify/graphify/serve.py
- [[Split a query into searchable terms, segmenting Chinese text, then drop     que]] - rationale - graphify/graphify/serve.py
- [[Tests for serve.py - MCP graph query helpers (no mcp package required).]] - rationale - graphify/tests/test_serve.py
- [[When jieba is not installed, fallback to character bigrams.]] - rationale - graphify/tests/test_serve.py
- [[Write a minimal graph.json with the given node IDs.]] - rationale - graphify/tests/test_serve.py
- [[_communities_from_graph()]] - code - graphify/graphify/serve.py
- [[_community_header()]] - code - graphify/graphify/serve.py
- [[_cut_lines_to_budget()]] - code - graphify/graphify/serve.py
- [[_load_graph()]] - code - graphify/graphify/serve.py
- [[_query_terms()]] - code - graphify/graphify/serve.py
- [[_write_graph()_7]] - code - graphify/tests/test_serve.py
- [[json.JSONDecodeError is a ValueError subclass, so its except clause     must be]] - rationale - graphify/tests/test_serve.py
- [[mtime_ns + size uniquely identifies a graph version (874).]] - rationale - graphify/tests/test_serve.py
- [[serve() picks up a new graph.json written after startup (874).]] - rationale - graphify/tests/test_serve.py
- [[test_communities_from_graph_basic()]] - code - graphify/tests/test_serve.py
- [[test_communities_from_graph_isolated()]] - code - graphify/tests/test_serve.py
- [[test_communities_from_graph_no_community_attr()]] - code - graphify/tests/test_serve.py
- [[test_community_header_falls_back_when_no_name()]] - code - graphify/tests/test_serve.py
- [[test_community_header_sanitizes_name()]] - code - graphify/tests/test_serve.py
- [[test_community_header_shows_real_name()]] - code - graphify/tests/test_serve.py
- [[test_community_header_skips_placeholder_name()]] - code - graphify/tests/test_serve.py
- [[test_cut_lines_to_budget_over_budget_announces_at_top()]] - code - graphify/tests/test_serve.py
- [[test_cut_lines_to_budget_under_budget_is_byte_identical()]] - code - graphify/tests/test_serve.py
- [[test_load_graph_accepts_under_cap()]] - code - graphify/tests/test_serve.py
- [[test_load_graph_cache_key_changes_with_content()]] - code - graphify/tests/test_serve.py
- [[test_load_graph_corrupted_json_prints_recovery_message()]] - code - graphify/tests/test_serve.py
- [[test_load_graph_generic_value_error_message_unchanged()]] - code - graphify/tests/test_serve.py
- [[test_load_graph_missing_file()]] - code - graphify/tests/test_serve.py
- [[test_load_graph_rejects_oversized_file()_1]] - code - graphify/tests/test_serve.py
- [[test_load_graph_roundtrip()]] - code - graphify/tests/test_serve.py
- [[test_maybe_reload_detects_graph_change()]] - code - graphify/tests/test_serve.py
- [[test_pick_seeds_german_query_seeds_content_node_not_heading_noise()]] - code - graphify/tests/test_serve.py
- [[test_query_terms_all_german_stopwords_falls_back_to_unfiltered()]] - code - graphify/tests/test_serve.py
- [[test_query_terms_all_stopwords_falls_back_to_unfiltered()]] - code - graphify/tests/test_serve.py
- [[test_query_terms_chinese_mixed()]] - code - graphify/tests/test_serve.py
- [[test_query_terms_chinese_no_jieba_fallback()]] - code - graphify/tests/test_serve.py
- [[test_query_terms_chinese_segments_with_cached_jieba()]] - code - graphify/tests/test_serve.py
- [[test_query_terms_drops_german_question_stopwords()]] - code - graphify/tests/test_serve.py
- [[test_query_terms_drops_question_stopwords()]] - code - graphify/tests/test_serve.py
- [[test_query_terms_filters_only_short_english_terms()]] - code - graphify/tests/test_serve.py
- [[test_query_terms_non_chinese_scripts_are_not_segmented()]] - code - graphify/tests/test_serve.py
- [[test_query_terms_strips_search_punctuation()]] - code - graphify/tests/test_serve.py
- [[test_score_nodes_prefilter_is_identical_to_full_scan()]] - code - graphify/tests/test_serve.py
- [[test_serve.py]] - code - graphify/tests/test_serve.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_41
SORT file.name ASC
```

## Connections to other communities
- 36 edges to [[_COMMUNITY_Community 67]]
- 22 edges to [[_COMMUNITY_Community 62]]
- 21 edges to [[_COMMUNITY_Community 98]]
- 21 edges to [[_COMMUNITY_Community 118]]
- 14 edges to [[_COMMUNITY_Community 144]]
- 6 edges to [[_COMMUNITY_Community 101]]
- 3 edges to [[_COMMUNITY_Community 156]]
- 3 edges to [[_COMMUNITY_Community 312]]
- 2 edges to [[_COMMUNITY_Community 36]]
- 1 edge to [[_COMMUNITY_Community 219]]
- 1 edge to [[_COMMUNITY_Community 121]]
- 1 edge to [[_COMMUNITY_Community 34]]
- 1 edge to [[_COMMUNITY_Community 12]]
- 1 edge to [[_COMMUNITY_Community 53]]

## Top bridge nodes
- [[test_serve.py]] - degree 138, connects to 8 communities
- [[_query_terms()]] - degree 21, connects to 5 communities
- [[_load_graph()]] - degree 13, connects to 5 communities
- [[_community_header()]] - degree 7, connects to 2 communities
- [[test_pick_seeds_german_query_seeds_content_node_not_heading_noise()]] - degree 6, connects to 2 communities