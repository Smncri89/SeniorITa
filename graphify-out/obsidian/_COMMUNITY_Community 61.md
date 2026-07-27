---
type: community
cohesion: 0.05
members: 40
---

# Community 61

**Cohesion:** 0.05 - loosely connected
**Members:** 40 nodes

## Members
- [[A symbol entry with `symbol int` is silently skipped.]] - rationale - graphify/tests/test_scip_ingest.py
- [[A symbol with `kind` as a non-string falls back to 'unknown'.]] - rationale - graphify/tests/test_scip_ingest.py
- [[A symbol with `relationships None` ingests without error and emits no edges.]] - rationale - graphify/tests/test_scip_ingest.py
- [[Convert a SCIP-style JSON document into Graphify nodes and edges.      Paramet]] - rationale - graphify/graphify/scip_ingest.py
- [[Cross-symbol relationship within ONE document resolves via the symbol index.]] - rationale - graphify/tests/test_scip_ingest.py
- [[Ingestion handles a large number of symbols gracefully.]] - rationale - graphify/tests/test_scip_ingest.py
- [[Only the first occurrence is used; if it is not a dict, sourceline stays 0.]] - rationale - graphify/tests/test_scip_ingest.py
- [[Result passes Graphify's validate_extraction and build_from_json keeps the edges]] - rationale - graphify/tests/test_scip_ingest.py
- [[SCIP relationship payloads embedded in edge metadata must be sanitized.]] - rationale - graphify/tests/test_scip_ingest.py
- [[Same symbol in different files produces different node ids.]] - rationale - graphify/tests/test_scip_ingest.py
- [[Top-level non-dict shapes still return the empty result.]] - rationale - graphify/tests/test_scip_ingest.py
- [[When a target symbol is defined in 2+ documents AND the source is in a     thir]] - rationale - graphify/tests/test_scip_ingest.py
- [[When no relative_path is given on document, source_file defaults to ''.]] - rationale - graphify/tests/test_scip_ingest.py
- [[When range is not a list, sourceline stays 0 (empty source_location).]] - rationale - graphify/tests/test_scip_ingest.py
- [[When symbol has no , the label is the full symbol id.]] - rationale - graphify/tests/test_scip_ingest.py
- [[When symbols is not a list, that document is skipped.]] - rationale - graphify/tests/test_scip_ingest.py
- [[`display_name` as a non-string falls back to the symbol suffix.]] - rationale - graphify/tests/test_scip_ingest.py
- [[`documentation` first entry that isn't a string yields empty description (not cr]] - rationale - graphify/tests/test_scip_ingest.py
- [[documents key not present → no processing → empty result.]] - rationale - graphify/tests/test_scip_ingest.py
- [[ingest_scip_json()]] - code - graphify/graphify/scip_ingest.py
- [[range0 = True (which is technically an int subclass) must not produce 'LTrue'.]] - rationale - graphify/tests/test_scip_ingest.py
- [[test_ambiguous_duplicate_target_across_docs_creates_stub()]] - code - graphify/tests/test_scip_ingest.py
- [[test_documentation_with_non_string_entries_is_ignored()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_default_source_file_is_empty_string()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_dict_without_documents_key()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_document_with_symbols_not_a_list()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_many_symbols()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_node_id_differs_by_source_file()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_relationship_metadata_sanitized()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_symbol_with_non_dict_occurrence_is_skipped()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_symbol_with_non_list_range_falls_back_to_zero()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_symbol_without_hash_uses_full_symbol_as_label()]] - code - graphify/tests/test_scip_ingest.py
- [[test_non_string_display_name_falls_back()]] - code - graphify/tests/test_scip_ingest.py
- [[test_non_string_kind_falls_back_to_unknown()]] - code - graphify/tests/test_scip_ingest.py
- [[test_non_string_symbol_id_is_skipped()]] - code - graphify/tests/test_scip_ingest.py
- [[test_occurrence_bool_line_falls_back_to_zero()]] - code - graphify/tests/test_scip_ingest.py
- [[test_relationship_edges_survive_validate_extraction_and_build()]] - code - graphify/tests/test_scip_ingest.py
- [[test_relationship_target_in_same_document_resolves_via_index()]] - code - graphify/tests/test_scip_ingest.py
- [[test_relationships_none_is_treated_as_empty()]] - code - graphify/tests/test_scip_ingest.py
- [[test_unrecognized_top_level_structure_returns_empty()]] - code - graphify/tests/test_scip_ingest.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_61
SORT file.name ASC
```

## Connections to other communities
- 37 edges to [[_COMMUNITY_Community 74]]
- 13 edges to [[_COMMUNITY_Community 105]]
- 5 edges to [[_COMMUNITY_Community 109]]
- 1 edge to [[_COMMUNITY_Community 35]]
- 1 edge to [[_COMMUNITY_Community 191]]
- 1 edge to [[_COMMUNITY_Community 539]]
- 1 edge to [[_COMMUNITY_Community 551]]
- 1 edge to [[_COMMUNITY_Community 555]]
- 1 edge to [[_COMMUNITY_Community 553]]
- 1 edge to [[_COMMUNITY_Community 547]]
- 1 edge to [[_COMMUNITY_Community 550]]
- 1 edge to [[_COMMUNITY_Community 548]]
- 1 edge to [[_COMMUNITY_Community 559]]
- 1 edge to [[_COMMUNITY_Community 546]]
- 1 edge to [[_COMMUNITY_Community 545]]
- 1 edge to [[_COMMUNITY_Community 347]]
- 1 edge to [[_COMMUNITY_Community 549]]
- 1 edge to [[_COMMUNITY_Community 535]]
- 1 edge to [[_COMMUNITY_Community 557]]
- 1 edge to [[_COMMUNITY_Community 558]]
- 1 edge to [[_COMMUNITY_Community 556]]
- 1 edge to [[_COMMUNITY_Community 554]]
- 1 edge to [[_COMMUNITY_Community 552]]
- 1 edge to [[_COMMUNITY_Community 538]]
- 1 edge to [[_COMMUNITY_Community 537]]
- 1 edge to [[_COMMUNITY_Community 540]]
- 1 edge to [[_COMMUNITY_Community 544]]
- 1 edge to [[_COMMUNITY_Community 543]]
- 1 edge to [[_COMMUNITY_Community 536]]
- 1 edge to [[_COMMUNITY_Community 542]]
- 1 edge to [[_COMMUNITY_Community 541]]
- 1 edge to [[_COMMUNITY_Community 37]]

## Top bridge nodes
- [[ingest_scip_json()]] - degree 83, connects to 30 communities
- [[test_relationship_edges_survive_validate_extraction_and_build()]] - degree 5, connects to 3 communities
- [[test_ambiguous_duplicate_target_across_docs_creates_stub()]] - degree 3, connects to 1 community
- [[test_documentation_with_non_string_entries_is_ignored()]] - degree 3, connects to 1 community
- [[test_ingest_default_source_file_is_empty_string()]] - degree 3, connects to 1 community