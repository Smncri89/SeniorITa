---
type: community
cohesion: 0.06
members: 36
---

# Community 74

**Cohesion:** 0.06 - loosely connected
**Members:** 36 nodes

## Members
- [[A non-dict entry in `documents` is silently skipped.]] - rationale - graphify/tests/test_scip_ingest.py
- [[A relationship entry whose `symbol` is a non-string is silently skipped.]] - rationale - graphify/tests/test_scip_ingest.py
- [[Comprehensive tests for graphify.scip_ingest.]] - rationale - graphify/tests/test_scip_ingest.py
- [[Control characters in SCIP description must not survive into the graph.]] - rationale - graphify/tests/test_scip_ingest.py
- [[Cross-document relationship resolves to the target document's node id.]] - rationale - graphify/tests/test_scip_ingest.py
- [[Duplicate symbol records within the SAME document collapse to one node id     i]] - rationale - graphify/tests/test_scip_ingest.py
- [[Empty dict input produces empty nodes and edges.]] - rationale - graphify/tests/test_scip_ingest.py
- [[Missing relationships key — symbol still becomes a node.]] - rationale - graphify/tests/test_scip_ingest.py
- [[Non-dict entries in the symbols list are silently skipped.]] - rationale - graphify/tests/test_scip_ingest.py
- [[SCIP-supplied description must be HTML-escaped before reaching node     metadat]] - rationale - graphify/tests/test_scip_ingest.py
- [[The source_file param provides a fallback when doc has no relative_path.]] - rationale - graphify/tests/test_scip_ingest.py
- [[When display_name is missing, label falls back to the portion after .]] - rationale - graphify/tests/test_scip_ingest.py
- [[When doc has no language field, uses the language function parameter.]] - rationale - graphify/tests/test_scip_ingest.py
- [[When documentation key is missing, scip_description is not in metadata.]] - rationale - graphify/tests/test_scip_ingest.py
- [[When documents is not a list, ingestion stops and returns empty.]] - rationale - graphify/tests/test_scip_ingest.py
- [[When occurrences key is missing entirely, falls back to empty source_location.]] - rationale - graphify/tests/test_scip_ingest.py
- [[When occurrences list is empty, source_location is empty string.]] - rationale - graphify/tests/test_scip_ingest.py
- [[When two docs both have `F`, a relationship from b.py's F to F must     reso]] - rationale - graphify/tests/test_scip_ingest.py
- [[test_document_entry_non_dict_is_skipped()]] - code - graphify/tests/test_scip_ingest.py
- [[test_duplicate_local_symbol_resolves_to_same_document()]] - code - graphify/tests/test_scip_ingest.py
- [[test_duplicate_same_document_definition_does_not_create_false_ambiguity()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_document_without_language_defaults_to_function_param()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_documents_not_a_list_is_skipped()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_empty_doc_returns_empty_lists()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_node_metadata_control_chars_stripped()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_node_metadata_html_escaped()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_source_file_falls_back_to_function_param()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_symbol_item_not_a_dict_is_skipped()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_symbol_without_display_name_uses_suffix()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_symbol_without_documentation_omits_description()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_symbol_without_occurrences_has_empty_source_location()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_symbol_without_occurrences_key()]] - code - graphify/tests/test_scip_ingest.py
- [[test_ingest_symbol_without_relationships_key_still_creates_node()]] - code - graphify/tests/test_scip_ingest.py
- [[test_relationship_symbol_non_string_is_skipped()]] - code - graphify/tests/test_scip_ingest.py
- [[test_relationship_target_across_documents_resolves_via_index()]] - code - graphify/tests/test_scip_ingest.py
- [[test_scip_ingest.py]] - code - graphify/tests/test_scip_ingest.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_74
SORT file.name ASC
```

## Connections to other communities
- 37 edges to [[_COMMUNITY_Community 61]]
- 14 edges to [[_COMMUNITY_Community 105]]
- 8 edges to [[_COMMUNITY_Community 191]]
- 6 edges to [[_COMMUNITY_Community 109]]
- 1 edge to [[_COMMUNITY_Community 35]]
- 1 edge to [[_COMMUNITY_Community 37]]
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

## Top bridge nodes
- [[test_scip_ingest.py]] - degree 94, connects to 32 communities
- [[test_document_entry_non_dict_is_skipped()]] - degree 3, connects to 1 community
- [[test_duplicate_local_symbol_resolves_to_same_document()]] - degree 3, connects to 1 community
- [[test_duplicate_same_document_definition_does_not_create_false_ambiguity()]] - degree 3, connects to 1 community
- [[test_ingest_document_without_language_defaults_to_function_param()]] - degree 3, connects to 1 community