---
type: community
cohesion: 0.11
members: 27
---

# Community 109

**Cohesion:** 0.11 - loosely connected
**Members:** 27 nodes

## Members
- [[All three fields present when description is non-empty.]] - rationale - graphify/tests/test_scip_ingest.py
- [[Any_9]] - code
- [[Any kind string maps to 'code'.]] - rationale - graphify/tests/test_scip_ingest.py
- [[Append edges (and stub nodes when needed) for a symbol's relationships.      R]] - rationale - graphify/graphify/scip_ingest.py
- [[Append the canonical node for a SCIP symbol record.]] - rationale - graphify/graphify/scip_ingest.py
- [[Build metadata for a SCIP node.]] - rationale - graphify/graphify/scip_ingest.py
- [[Map SCIP symbol kind to a Graphify file_type.]] - rationale - graphify/graphify/scip_ingest.py
- [[Pick the Graphify relation tag for a SCIP relationship dict.      Flags are ac]] - rationale - graphify/graphify/scip_ingest.py
- [[Read the 1-based line number from the first occurrence range, defensively.]] - rationale - graphify/graphify/scip_ingest.py
- [[Resolve a SCIP relationship target to an emitted node id, or None.      Resolu]] - rationale - graphify/graphify/scip_ingest.py
- [[Return True only when value is exactly the boolean True.      Used for SCIP re]] - rationale - graphify/graphify/scip_ingest.py
- [[Return ``value`` if it is a string, else the ``default`` (also a string).]] - rationale - graphify/graphify/scip_ingest.py
- [[_build_scip_metadata()]] - code - graphify/graphify/scip_ingest.py
- [[_coerce_str()]] - code - graphify/graphify/scip_ingest.py
- [[_emit_relationships()]] - code - graphify/graphify/scip_ingest.py
- [[_emit_symbol_node()]] - code - graphify/graphify/scip_ingest.py
- [[_first_occurrence_line()]] - code - graphify/graphify/scip_ingest.py
- [[_is_true()]] - code - graphify/graphify/scip_ingest.py
- [[_resolve_relationship_target()]] - code - graphify/graphify/scip_ingest.py
- [[_scip_kind_to_file_type()]] - code - graphify/graphify/scip_ingest.py
- [[_scip_relation_for()]] - code - graphify/graphify/scip_ingest.py
- [[scip_description is omitted when description is empty string.]] - rationale - graphify/tests/test_scip_ingest.py
- [[scip_ingest.py]] - code - graphify/graphify/scip_ingest.py
- [[scip_ingest.py — SCIP JSON ingestion (simplified subset).  Reads a simplified]] - rationale - graphify/graphify/scip_ingest.py
- [[test_build_scip_metadata_with_description()]] - code - graphify/tests/test_scip_ingest.py
- [[test_build_scip_metadata_without_description()]] - code - graphify/tests/test_scip_ingest.py
- [[test_scip_kind_to_file_type_always_code()]] - code - graphify/tests/test_scip_ingest.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_109
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Community 74]]
- 5 edges to [[_COMMUNITY_Community 61]]
- 3 edges to [[_COMMUNITY_Community 36]]
- 2 edges to [[_COMMUNITY_Community 191]]
- 1 edge to [[_COMMUNITY_Community 171]]

## Top bridge nodes
- [[scip_ingest.py]] - degree 15, connects to 5 communities
- [[_emit_relationships()]] - degree 11, connects to 3 communities
- [[_emit_symbol_node()]] - degree 9, connects to 2 communities
- [[_build_scip_metadata()]] - degree 7, connects to 1 community
- [[_coerce_str()]] - degree 5, connects to 1 community