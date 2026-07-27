---
type: community
cohesion: 0.11
members: 40
---

# Community 59

**Cohesion:** 0.11 - loosely connected
**Members:** 40 nodes

## Members
- [[AMBIGUOUS edges must have confidence_score = 0.4.]] - rationale - graphify/tests/test_confidence.py
- [[Build a minimal graph.json + analysislabels in tmp_pathgraphify-out.      M]] - rationale - graphify/tests/test_reflect.py
- [[EXTRACTED edges must have confidence_score == 1.0.]] - rationale - graphify/tests/test_confidence.py
- [[INFERRED edges must have confidence_score between 0.0 and 1.0.]] - rationale - graphify/tests/test_confidence.py
- [[No learning input = no section; report identical to pre-feature.]] - rationale - graphify/tests/test_report.py
- [[Report summary line should include avg confidence for INFERRED edges.]] - rationale - graphify/tests/test_confidence.py
- [[Return a minimal extraction dict with one edge of each confidence type.]] - rationale - graphify/tests/test_confidence.py
- [[Return the top_n most-connected real entities - the core abstractions.      Fi]] - rationale - graphify/graphify/analyze.py
- [[Surprising connections section shows confidence score next to INFERRED edges.]] - rationale - graphify/tests/test_confidence.py
- [[Tests for confidence_score on edges.]] - rationale - graphify/tests/test_confidence.py
- [[When a work-memory overlay (preferred sources) and query-scoped dead-ends     a]] - rationale - graphify/tests/test_report.py
- [[_make_extraction()]] - code - graphify/tests/test_confidence.py
- [[_make_graph()_3]] - code - graphify/tests/test_reflect.py
- [[confidence_score survives build_from_json → to_json → JSON parse round-trip.]] - rationale - graphify/tests/test_confidence.py
- [[generate()]] - code - graphify/graphify/report.py
- [[god_nodes()]] - code - graphify/graphify/analyze.py
- [[make_inputs()]] - code - graphify/tests/test_report.py
- [[score_all()]] - code - graphify/graphify/cluster.py
- [[test_ambiguous_edges_score_at_most_04()]] - code - graphify/tests/test_confidence.py
- [[test_confidence.py]] - code - graphify/tests/test_confidence.py
- [[test_confidence_score_round_trip()]] - code - graphify/tests/test_confidence.py
- [[test_extracted_edges_have_score_1()]] - code - graphify/tests/test_confidence.py
- [[test_import_cycles_section_absent_for_documents_only_corpus()]] - code - graphify/tests/test_report.py
- [[test_import_cycles_section_present_for_code_corpus()]] - code - graphify/tests/test_report.py
- [[test_inferred_edges_score_in_range()]] - code - graphify/tests/test_confidence.py
- [[test_report.py]] - code - graphify/tests/test_report.py
- [[test_report_contains_ambiguous_section()]] - code - graphify/tests/test_report.py
- [[test_report_contains_communities()]] - code - graphify/tests/test_report.py
- [[test_report_contains_corpus_check()]] - code - graphify/tests/test_report.py
- [[test_report_contains_god_nodes()]] - code - graphify/tests/test_report.py
- [[test_report_contains_header()]] - code - graphify/tests/test_report.py
- [[test_report_contains_surprising_connections()]] - code - graphify/tests/test_report.py
- [[test_report_hubs_are_plain_text_by_default()]] - code - graphify/tests/test_report.py
- [[test_report_hubs_use_wikilinks_when_obsidian()]] - code - graphify/tests/test_report.py
- [[test_report_inferred_tag_with_score()]] - code - graphify/tests/test_confidence.py
- [[test_report_shows_avg_confidence_for_inferred()]] - code - graphify/tests/test_confidence.py
- [[test_report_shows_raw_cohesion_scores()]] - code - graphify/tests/test_report.py
- [[test_report_shows_token_cost()]] - code - graphify/tests/test_report.py
- [[test_report_work_memory_section_absent_without_overlay()]] - code - graphify/tests/test_report.py
- [[test_report_work_memory_section_present_with_overlay_and_dead_ends()]] - code - graphify/tests/test_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_59
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_Community 10]]
- 13 edges to [[_COMMUNITY_Community 35]]
- 12 edges to [[_COMMUNITY_Community 77]]
- 12 edges to [[_COMMUNITY_Community 19]]
- 6 edges to [[_COMMUNITY_Community 12]]
- 6 edges to [[_COMMUNITY_Community 15]]
- 6 edges to [[_COMMUNITY_Community 209]]
- 6 edges to [[_COMMUNITY_Community 114]]
- 4 edges to [[_COMMUNITY_Community 49]]
- 4 edges to [[_COMMUNITY_Community 162]]
- 3 edges to [[_COMMUNITY_Community 40]]
- 3 edges to [[_COMMUNITY_Community 186]]
- 2 edges to [[_COMMUNITY_Community 288]]
- 2 edges to [[_COMMUNITY_Community 34]]
- 1 edge to [[_COMMUNITY_Community 98]]
- 1 edge to [[_COMMUNITY_Community 135]]
- 1 edge to [[_COMMUNITY_Community 25]]
- 1 edge to [[_COMMUNITY_Community 149]]

## Top bridge nodes
- [[god_nodes()]] - degree 32, connects to 10 communities
- [[generate()]] - degree 35, connects to 7 communities
- [[test_confidence.py]] - degree 21, connects to 7 communities
- [[test_report.py]] - degree 25, connects to 6 communities
- [[score_all()]] - degree 20, connects to 6 communities