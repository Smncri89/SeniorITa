---
type: community
cohesion: 0.18
members: 11
---

# Community 239

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Members
- [[A plain markdown file with no frontmatter is skipped, not crashed on.]] - rationale - graphify/tests/test_reflect.py
- [[Parse the frontmatter of a memory doc into a dict, or None if it has none.]] - rationale - graphify/graphify/reflect.py
- [[Reverse the double-quoted escaping that ingest._yaml_str applies.]] - rationale - graphify/graphify/reflect.py
- [[_yaml_unescape()]] - code - graphify/graphify/reflect.py
- [[parse_memory_doc reads back exactly what save_query_result wrote, including]] - rationale - graphify/tests/test_reflect.py
- [[parse_memory_doc()]] - code - graphify/graphify/reflect.py
- [[save - parse preserves tricky characters in the question, the correction,]] - rationale - graphify/tests/test_reflect.py
- [[test_parse_handles_crlf()]] - code - graphify/tests/test_reflect.py
- [[test_parse_returns_none_for_foreign_doc()]] - code - graphify/tests/test_reflect.py
- [[test_parse_round_trips_a_saved_doc()]] - code - graphify/tests/test_reflect.py
- [[test_round_trip_survives_backslash_newline_and_quoted_node()]] - code - graphify/tests/test_reflect.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_239
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Community 40]]
- 3 edges to [[_COMMUNITY_Community 53]]
- 2 edges to [[_COMMUNITY_Community 142]]
- 1 edge to [[_COMMUNITY_Community 277]]

## Top bridge nodes
- [[parse_memory_doc()]] - degree 11, connects to 3 communities
- [[test_parse_round_trips_a_saved_doc()]] - degree 4, connects to 2 communities
- [[test_round_trip_survives_backslash_newline_and_quoted_node()]] - degree 4, connects to 2 communities
- [[_yaml_unescape()]] - degree 3, connects to 1 community
- [[test_parse_returns_none_for_foreign_doc()]] - degree 3, connects to 1 community