---
type: community
cohesion: 0.08
members: 33
---

# Community 77

**Cohesion:** 0.08 - loosely connected
**Members:** 33 nodes

## Members
- [[IMPORTANT resolve endpoints using source_file only; never infer from labelid]] - rationale - graphify/graphify/analyze.py
- [[Append the `` Work-memory lessons`` section, or nothing when empty.]] - rationale - graphify/graphify/report.py
- [[Cross-file edges between real codedoc entities, ranked by a composite     surp]] - rationale - graphify/graphify/analyze.py
- [[For single-source corpora find edges that bridge different communities.     Th]] - rationale - graphify/graphify/analyze.py
- [[Graph analysis god nodes (most connected), surprising connections (cross-commun]] - rationale - graphify/graphify/analyze.py
- [[Invert communities dict node_id - community_id.]] - rationale - graphify/graphify/analyze.py
- [[Mirrors export.safe_name so community hub filenames and report wikilinks always]] - rationale - graphify/graphify/report.py
- [[Push graph directly to a running FalkorDB instance via the Python SDK.      Re]] - rationale - graphify/graphify/exporters/graphdb.py
- [[Push graph directly to a running Neo4j instance via the Python driver.      Re]] - rationale - graphify/graphify/exporters/graphdb.py
- [[Return True if this node is a file-level hub node (e.g. 'client', 'models')]] - rationale - graphify/graphify/analyze.py
- [[Return True if this node is a manually-injected semantic concept node     rathe]] - rationale - graphify/graphify/analyze.py
- [[Shared constantshelpers for the graphify exporters package.  Symbols used by]] - rationale - graphify/graphify/exporters/base.py
- [[_cross_community_surprises()]] - code - graphify/graphify/analyze.py
- [[_cross_file_surprises()]] - code - graphify/graphify/analyze.py
- [[_html_script()]] - code - graphify/graphify/exporters/html.py
- [[_html_styles()]] - code - graphify/graphify/exporters/html.py
- [[_hyperedge_script()]] - code - graphify/graphify/exporters/html.py
- [[_is_concept_node()]] - code - graphify/graphify/analyze.py
- [[_is_file_node()]] - code - graphify/graphify/analyze.py
- [[_learning_section()]] - code - graphify/graphify/report.py
- [[_node_community_map()]] - code - graphify/graphify/analyze.py
- [[_safe_community_name()]] - code - graphify/graphify/report.py
- [[exportersbase.py]] - code - graphify/graphify/exporters/base.py
- [[graphdb — moved verbatim from graphifyexport.py.]] - rationale - graphify/graphify/exporters/graphdb.py
- [[graphdb.py]] - code - graphify/graphify/exporters/graphdb.py
- [[graphifyanalyze.py]] - code - graphify/graphify/analyze.py
- [[html — moved verbatim from graphifyexport.py.]] - rationale - graphify/graphify/exporters/html.py
- [[html.py]] - code - graphify/graphify/exporters/html.py
- [[push_to_falkordb()]] - code - graphify/graphify/exporters/graphdb.py
- [[push_to_neo4j()]] - code - graphify/graphify/exporters/graphdb.py
- [[report.py]] - code - graphify/graphify/report.py
- [[test_is_concept_node_empty_source()]] - code - graphify/tests/test_analyze.py
- [[test_is_concept_node_real_file()]] - code - graphify/tests/test_analyze.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_77
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_Community 10]]
- 12 edges to [[_COMMUNITY_Community 59]]
- 8 edges to [[_COMMUNITY_Community 25]]
- 7 edges to [[_COMMUNITY_Community 19]]
- 6 edges to [[_COMMUNITY_Community 15]]
- 3 edges to [[_COMMUNITY_Community 95]]
- 2 edges to [[_COMMUNITY_Community 18]]
- 2 edges to [[_COMMUNITY_Community 209]]
- 2 edges to [[_COMMUNITY_Community 186]]
- 2 edges to [[_COMMUNITY_Community 283]]
- 2 edges to [[_COMMUNITY_Community 53]]
- 1 edge to [[_COMMUNITY_Community 34]]
- 1 edge to [[_COMMUNITY_Community 114]]
- 1 edge to [[_COMMUNITY_Community 44]]
- 1 edge to [[_COMMUNITY_Community 288]]
- 1 edge to [[_COMMUNITY_Community 12]]
- 1 edge to [[_COMMUNITY_Community 163]]
- 1 edge to [[_COMMUNITY_Community 36]]
- 1 edge to [[_COMMUNITY_Community 124]]
- 1 edge to [[_COMMUNITY_Community 171]]
- 1 edge to [[_COMMUNITY_Community 277]]
- 1 edge to [[_COMMUNITY_Community 40]]
- 1 edge to [[_COMMUNITY_Community 35]]

## Top bridge nodes
- [[graphifyanalyze.py]] - degree 31, connects to 12 communities
- [[html.py]] - degree 16, connects to 9 communities
- [[report.py]] - degree 15, connects to 9 communities
- [[_node_community_map()]] - degree 15, connects to 4 communities
- [[_is_concept_node()]] - degree 10, connects to 3 communities