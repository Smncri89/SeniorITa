---
type: community
cohesion: 0.05
members: 72
---

# Community 17

**Cohesion:** 0.05 - loosely connected
**Members:** 72 nodes

## Members
- [[1561 a `members`-keyed hyperedge with =2 surviving members must be     KEPT]] - rationale - graphify/tests/test_semantic_cleanup.py
- [[1561 an alias-keyed hyperedge must not be rejected for a missing     `nodes`]] - rationale - graphify/tests/test_semantic_cleanup.py
- [[A hyperedge referencing only nodes not present in the fragment is dropped.]] - rationale - graphify/tests/test_semantic_cleanup.py
- [[A node with file_type='rationale' is removed wholesale.]] - rationale - graphify/tests/test_semantic_cleanup.py
- [[A rationale node connected to ONE target via `rationale_for` and to ANOTHER]] - rationale - graphify/tests/test_semantic_cleanup.py
- [[A short named node with a period (e.g. abbreviation) is NOT sentence-like.]] - rationale - graphify/tests/test_semantic_cleanup.py
- [[A valid fragment may legitimately contain no entities; it still counts.]] - rationale - graphify/tests/test_merge_chunks_validation.py
- [[An unknownsynonym file_type is NOT a validation failure build_from_json     c]] - rationale - graphify/tests/test_semantic_cleanup.py
- [[Append one or more rationale strings to node's ``rationale`` attribute.]] - rationale - graphify/graphify/semantic_cleanup.py
- [[Boundary a label with exactly 8 words + colon is sentence-like;     a 7-word l]] - rationale - graphify/tests/test_semantic_cleanup.py
- [[Clean up a semantic extraction fragment in-place.      Operations     1. Rem]] - rationale - graphify/graphify/semantic_cleanup.py
- [[F3 a node with file_type='document' (allowed) that is BOTH sentence-like     A]] - rationale - graphify/tests/test_semantic_cleanup.py
- [[F4 hyperedges referencing removed nodes are repaired or dropped.]] - rationale - graphify/tests/test_semantic_cleanup.py
- [[Invalid JSON returns an error instead of raising.]] - rationale - graphify/tests/test_semantic_cleanup.py
- [[LLM output with file_type='concept' must pass validation for the same reason.]] - rationale - graphify/tests/test_semantic_cleanup.py
- [[LLM output with file_type='rationale' must pass validation so the cleanup     p]] - rationale - graphify/tests/test_semantic_cleanup.py
- [[Load and validate a semantic chunk, rejecting oversize files before parsing.]] - rationale - graphify/graphify/semantic_cleanup.py
- [[Oversize files are rejected by stat() — payload is never parsed.]] - rationale - graphify/tests/test_semantic_cleanup.py
- [[Path_52]] - code
- [[Return True if label looks like prose  rationale text rather than an     ent]] - rationale - graphify/graphify/semantic_cleanup.py
- [[Return validation errors for an untrusted semantic extraction fragment.      E]] - rationale - graphify/graphify/semantic_cleanup.py
- [[Sentence-like rationale node connected via `rationale_for` → attribute on target]] - rationale - graphify/tests/test_semantic_cleanup.py
- [[Tests for graphify.semantic_cleanup.validate_semantic_fragment (825).]] - rationale - graphify/tests/test_semantic_cleanup.py
- [[Tests that `graphify merge-chunks` validates untrusted subagent chunk JSON.  m]] - rationale - graphify/tests/test_merge_chunks_validation.py
- [[_append_rationale_attr()]] - code - graphify/graphify/semantic_cleanup.py
- [[_is_sentence_like_rationale_label()]] - code - graphify/graphify/semantic_cleanup.py
- [[_run_merge()]] - code - graphify/tests/test_merge_chunks_validation.py
- [[_valid_fragment()]] - code - graphify/tests/test_semantic_cleanup.py
- [[_validate_semantic_id()]] - code - graphify/graphify/semantic_cleanup.py
- [[_write()_14]] - code - graphify/tests/test_merge_chunks_validation.py
- [[load_validated_semantic_fragment()]] - code - graphify/graphify/semantic_cleanup.py
- [[sanitize_semantic_fragment()]] - code - graphify/graphify/semantic_cleanup.py
- [[semantic_cleanup.py]] - code - graphify/graphify/semantic_cleanup.py
- [[test_load_validated_semantic_fragment_accepts_valid()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_load_validated_semantic_fragment_rejects_invalid_json()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_load_validated_semantic_fragment_rejects_oversize_before_parse()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_merge_chunks_accepts_synonym_file_type()]] - code - graphify/tests/test_merge_chunks_validation.py
- [[test_merge_chunks_accepts_unicode_id()]] - code - graphify/tests/test_merge_chunks_validation.py
- [[test_merge_chunks_accepts_valid_empty_chunk()]] - code - graphify/tests/test_merge_chunks_validation.py
- [[test_merge_chunks_fails_closed_on_unmatched_glob()]] - code - graphify/tests/test_merge_chunks_validation.py
- [[test_merge_chunks_fails_closed_when_every_chunk_is_invalid()]] - code - graphify/tests/test_merge_chunks_validation.py
- [[test_merge_chunks_fails_closed_without_chunk_arguments()]] - code - graphify/tests/test_merge_chunks_validation.py
- [[test_merge_chunks_merges_valid_chunks()]] - code - graphify/tests/test_merge_chunks_validation.py
- [[test_merge_chunks_skips_chunk_with_path_escape_id()]] - code - graphify/tests/test_merge_chunks_validation.py
- [[test_merge_chunks_validation.py]] - code - graphify/tests/test_merge_chunks_validation.py
- [[test_sanitize_boundary_sentence_threshold()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_sanitize_converts_allowed_filetype_sentence_via_rationale_for_edge()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_sanitize_converts_sentence_rationale_node_to_attribute()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_sanitize_drops_hyperedge_with_only_unknown_refs()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_sanitize_drops_rationale_filetype_node()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_sanitize_filters_hyperedges_after_node_removal()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_sanitize_keeps_members_keyed_hyperedge()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_sanitize_keeps_short_concept_named_node_with_punctuation()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_sanitize_rationale_only_propagates_through_rationale_for_edges()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_semantic_cleanup.py]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_validate_accepts_node_ids_keyed_hyperedge()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_validate_hyperedge_caps_count()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_validate_hyperedge_rejects_bad_id()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_validate_hyperedge_rejects_bad_node_ref()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_validate_hyperedge_requires_list()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_validate_semantic_fragment_accepts_concept_file_type()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_validate_semantic_fragment_accepts_rationale_file_type()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_validate_semantic_fragment_accepts_synonyms_and_unicode()]] - code - graphify/tests/test_merge_chunks_validation.py
- [[test_validate_semantic_fragment_accepts_unknown_file_type()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_validate_semantic_fragment_accepts_valid()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_validate_semantic_fragment_rejects_non_object()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_validate_semantic_fragment_rejects_oversize_payload()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_validate_semantic_fragment_rejects_path_separator_in_id()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_validate_semantic_fragment_rejects_too_many_edges()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_validate_semantic_fragment_rejects_too_many_nodes()]] - code - graphify/tests/test_semantic_cleanup.py
- [[test_validate_semantic_fragment_still_blocks_path_escape()]] - code - graphify/tests/test_merge_chunks_validation.py
- [[validate_semantic_fragment()]] - code - graphify/graphify/semantic_cleanup.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_17
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 35]]
- 2 edges to [[_COMMUNITY_Community 12]]
- 1 edge to [[_COMMUNITY_Community 301]]
- 1 edge to [[_COMMUNITY_Community 4]]
- 1 edge to [[_COMMUNITY_Community 47]]
- 1 edge to [[_COMMUNITY_Community 34]]

## Top bridge nodes
- [[semantic_cleanup.py]] - degree 9, connects to 2 communities
- [[test_semantic_cleanup.py]] - degree 30, connects to 1 community
- [[validate_semantic_fragment()]] - degree 22, connects to 1 community
- [[test_merge_chunks_validation.py]] - degree 15, connects to 1 community
- [[sanitize_semantic_fragment()]] - degree 14, connects to 1 community