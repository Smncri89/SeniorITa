---
type: community
cohesion: 0.20
members: 10
---

# Community 256

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[Assert a monolith renders diff-clean vs its v8 blob modulo allowed changes.]] - rationale - graphify/tools/skillgen/gen.py
- [[Each monolith is diff-clean vs v8 except the file_type enum unification.]] - rationale - graphify/tests/test_skillgen.py
- [[Every line that differs from pristine v8 is a sanctioned change-class.      Th]] - rationale - graphify/tests/test_skillgen.py
- [[Whether a line is the non-spec ``trigger`` frontmatter field (1180).      Th]] - rationale - graphify/tools/skillgen/gen.py
- [[Whether a single addedremoved monolith line is an allowed change.]] - rationale - graphify/tools/skillgen/gen.py
- [[_is_sanctioned_monolith_diff()]] - code - graphify/tools/skillgen/gen.py
- [[_is_trigger_line()]] - code - graphify/tools/skillgen/gen.py
- [[monolith_roundtrip()]] - code - graphify/tools/skillgen/gen.py
- [[test_monolith_roundtrip_passes_for_aider_and_devin()]] - code - graphify/tests/test_skillgen.py
- [[test_monoliths_change_only_sanctioned_lines()]] - code - graphify/tests/test_skillgen.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_256
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 92]]
- 4 edges to [[_COMMUNITY_Community 43]]
- 2 edges to [[_COMMUNITY_Community 54]]
- 2 edges to [[_COMMUNITY_Community 106]]
- 1 edge to [[_COMMUNITY_Community 129]]

## Top bridge nodes
- [[monolith_roundtrip()]] - degree 11, connects to 3 communities
- [[test_monoliths_change_only_sanctioned_lines()]] - degree 5, connects to 3 communities
- [[test_monolith_roundtrip_passes_for_aider_and_devin()]] - degree 4, connects to 2 communities
- [[_is_sanctioned_monolith_diff()]] - degree 3, connects to 1 community
- [[_is_trigger_line()]] - degree 3, connects to 1 community