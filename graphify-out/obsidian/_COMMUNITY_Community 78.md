---
type: community
cohesion: 0.09
members: 33
---

# Community 78

**Cohesion:** 0.09 - loosely connected
**Members:** 33 nodes

## Members
- [[1631 — a malformed LLM chunk (a stray non-dict entry in edgesnodes) must not]] - rationale - graphify/tests/test_semantic_fragment_sanitize.py
- [[Claude often prefixes the JSON with a short preamble before the     ```json fen]] - rationale - graphify/tests/test_llm_parser.py
- [[Default behaviour when the env var is not set, --model is not     added so cla]] - rationale - graphify/tests/test_llm_parser.py
- [[Extraction instructions must be delivered in the user turn, not via     --syste]] - rationale - graphify/tests/test_llm_parser.py
- [[Force ``nodes````edges````hyperedges`` to lists of dicts, in place.      A m]] - rationale - graphify/graphify/llm.py
- [[GRAPHIFY_CLAUDE_CLI_MODEL must be forwarded to claude -p --model.]] - rationale - graphify/tests/test_llm_parser.py
- [[Regression clean JSON input (the original happy path) must keep     parsing ex]] - rationale - graphify/tests/test_llm_parser.py
- [[Some models return prose around bare JSON with no markdown fence.     The balan]] - rationale - graphify/tests/test_llm_parser.py
- [[Strip optional markdown fences and parse JSON. Returns empty fragment on failure]] - rationale - graphify/graphify/llm.py
- [[Tests for `_parse_llm_json` robustness and the `_call_claude_cli` subprocess ar]] - rationale - graphify/tests/test_llm_parser.py
- [[Truncated response the model started the fence but ran out of     tokens befor]] - rationale - graphify/tests/test_llm_parser.py
- [[When the model refuses or returns unrelated prose, the parser     must degrade]] - rationale - graphify/tests/test_llm_parser.py
- [[_make_envelope()]] - code - graphify/tests/test_llm_parser.py
- [[_parse_llm_json()]] - code - graphify/graphify/llm.py
- [[_sanitize_fragment()]] - code - graphify/graphify/llm.py
- [[patch]] - code
- [[test_empty_response_returns_empty_fragment()]] - code - graphify/tests/test_llm_parser.py
- [[test_fence_with_uppercase_language_tag()]] - code - graphify/tests/test_llm_parser.py
- [[test_fence_without_closing_backticks()]] - code - graphify/tests/test_llm_parser.py
- [[test_instructions_ride_in_user_turn_not_system_prompt()]] - code - graphify/tests/test_llm_parser.py
- [[test_llm_parser.py]] - code - graphify/tests/test_llm_parser.py
- [[test_merge_after_sanitize_does_not_raise_on_source_file_access()]] - code - graphify/tests/test_semantic_fragment_sanitize.py
- [[test_model_env_var_adds_model_flag()]] - code - graphify/tests/test_llm_parser.py
- [[test_no_model_flag_when_env_var_unset()]] - code - graphify/tests/test_llm_parser.py
- [[test_parse_llm_json_fenced_response_is_sanitized()]] - code - graphify/tests/test_semantic_fragment_sanitize.py
- [[test_parse_llm_json_sanitizes_stray_list_in_edges()]] - code - graphify/tests/test_semantic_fragment_sanitize.py
- [[test_preamble_then_fence_is_parsed()]] - code - graphify/tests/test_llm_parser.py
- [[test_prose_wrapped_json_without_fence_is_parsed()]] - code - graphify/tests/test_llm_parser.py
- [[test_raw_json_still_works()]] - code - graphify/tests/test_llm_parser.py
- [[test_sanitize_coerces_non_list_values_to_empty()]] - code - graphify/tests/test_semantic_fragment_sanitize.py
- [[test_sanitize_drops_non_dict_edge_entries()]] - code - graphify/tests/test_semantic_fragment_sanitize.py
- [[test_semantic_fragment_sanitize.py]] - code - graphify/tests/test_semantic_fragment_sanitize.py
- [[test_total_refusal_returns_empty_fragment()]] - code - graphify/tests/test_llm_parser.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_78
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 58]]
- 4 edges to [[_COMMUNITY_Community 33]]
- 2 edges to [[_COMMUNITY_Community 38]]
- 1 edge to [[_COMMUNITY_Community 301]]
- 1 edge to [[_COMMUNITY_Community 89]]
- 1 edge to [[_COMMUNITY_Community 16]]

## Top bridge nodes
- [[_parse_llm_json()]] - degree 19, connects to 5 communities
- [[test_llm_parser.py]] - degree 14, connects to 2 communities
- [[test_semantic_fragment_sanitize.py]] - degree 9, connects to 1 community
- [[_sanitize_fragment()]] - degree 6, connects to 1 community
- [[test_instructions_ride_in_user_turn_not_system_prompt()]] - degree 5, connects to 1 community