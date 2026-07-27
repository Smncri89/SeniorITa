---
type: community
cohesion: 0.07
members: 42
---

# Community 58

**Cohesion:** 0.07 - loosely connected
**Members:** 42 nodes

## Members
- [[Defang known chat-template  jailbreak control tokens in untrusted text.]] - rationale - graphify/graphify/llm.py
- [[Demonstrates the bug fix.      The full batch of 4 communities triggers malfor]] - rationale - graphify/tests/test_label_retry.py
- [[Honour GRAPHIFY_MAX_OUTPUT_TOKENS env var override, else use backend default.]] - rationale - graphify/graphify/llm.py
- [[Label a batch of communities, splitting in half and retrying on parse failure.]] - rationale - graphify/graphify/llm.py
- [[Map each dispatched text unit's resolved path to the (lower-cased, capped)]] - rationale - graphify/graphify/llm.py
- [[Parse the backend's JSON ``{cid name}`` reply. Raises on non-JSON or a     non]] - rationale - graphify/graphify/llm.py
- [[Path_43]] - code
- [[Return a text-like file's content for the extraction prompt.      Most files a]] - rationale - graphify/graphify/llm.py
- [[Return a tiktoken encoder for accurate token counts, or None if tiktoken     is]] - rationale - graphify/graphify/llm.py
- [[Return fileslice contents formatted for the extraction prompt.      Each unit]] - rationale - graphify/graphify/llm.py
- [[Return the resolved path only when it stays inside ``root``.]] - rationale - graphify/graphify/llm.py
- [[Source paths covered by a chunk, for marking a chunk that truncated to an     E]] - rationale - graphify/graphify/llm.py
- [[Split a chunk into (text-like units, raster-image files).      A ``FileSlice``]] - rationale - graphify/graphify/llm.py
- [[Tests for ANTHROPIC_BASE_URL  ANTHROPIC_MODEL overrides on the claude backend.]] - rationale - graphify/tests/test_anthropic_custom_endpoint.py
- [[Tests for OPENAI_BASE_URL  OPENAI_MODEL overrides on the openai backend.  The]] - rationale - graphify/tests/test_openai_custom_endpoint.py
- [[Tests for graphify.llm._label_batch_with_retry — adaptive split-and-retry on JS]] - rationale - graphify/tests/test_label_retry.py
- [[The on-disk path a unit belongs to (the parent file for a slice).]] - rationale - graphify/graphify/file_slice.py
- [[Wrap one file's content in a labelled, hash-stamped untrusted-data block.]] - rationale - graphify/graphify/llm.py
- [[_chunk_partial_files()]] - code - graphify/graphify/llm.py
- [[_dispatched_source_text()]] - code - graphify/graphify/llm.py
- [[_file_to_text()]] - code - graphify/graphify/llm.py
- [[_get_tokenizer()]] - code - graphify/graphify/llm.py
- [[_is_vision_image()]] - code - graphify/graphify/llm.py
- [[_label_batch_with_retry()]] - code - graphify/graphify/llm.py
- [[_neutralise_injection_sentinels()]] - code - graphify/graphify/llm.py
- [[_parse_label_response()]] - code - graphify/graphify/llm.py
- [[_partition_semantic_files()]] - code - graphify/graphify/llm.py
- [[_read_files()]] - code - graphify/graphify/llm.py
- [[_resolve_max_tokens()]] - code - graphify/graphify/llm.py
- [[_resolve_under_root()]] - code - graphify/graphify/llm.py
- [[_wrap_untrusted()]] - code - graphify/graphify/llm.py
- [[llm.py]] - code - graphify/graphify/llm.py
- [[test_anthropic_custom_endpoint.py]] - code - graphify/tests/test_anthropic_custom_endpoint.py
- [[test_claude_base_url_and_model_env_override()]] - code - graphify/tests/test_anthropic_custom_endpoint.py
- [[test_claude_defaults_without_env()]] - code - graphify/tests/test_anthropic_custom_endpoint.py
- [[test_graphify_openai_model_wins_over_openai_model()]] - code - graphify/tests/test_openai_custom_endpoint.py
- [[test_label_batch_recovers_via_split_on_invalid_json()]] - code - graphify/tests/test_label_retry.py
- [[test_label_retry.py]] - code - graphify/tests/test_label_retry.py
- [[test_openai_base_url_and_model_env_override()]] - code - graphify/tests/test_openai_custom_endpoint.py
- [[test_openai_custom_endpoint.py]] - code - graphify/tests/test_openai_custom_endpoint.py
- [[test_openai_defaults_without_env()]] - code - graphify/tests/test_openai_custom_endpoint.py
- [[unit_path()]] - code - graphify/graphify/file_slice.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_58
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_Community 38]]
- 14 edges to [[_COMMUNITY_Community 72]]
- 12 edges to [[_COMMUNITY_Community 39]]
- 11 edges to [[_COMMUNITY_Community 20]]
- 10 edges to [[_COMMUNITY_Community 89]]
- 7 edges to [[_COMMUNITY_Community 16]]
- 6 edges to [[_COMMUNITY_Community 93]]
- 6 edges to [[_COMMUNITY_Community 33]]
- 5 edges to [[_COMMUNITY_Community 143]]
- 5 edges to [[_COMMUNITY_Community 52]]
- 5 edges to [[_COMMUNITY_Community 12]]
- 4 edges to [[_COMMUNITY_Community 57]]
- 4 edges to [[_COMMUNITY_Community 78]]
- 3 edges to [[_COMMUNITY_Community 301]]
- 2 edges to [[_COMMUNITY_Community 100]]
- 2 edges to [[_COMMUNITY_Community 170]]
- 1 edge to [[_COMMUNITY_Community 117]]
- 1 edge to [[_COMMUNITY_Community 91]]

## Top bridge nodes
- [[llm.py]] - degree 98, connects to 17 communities
- [[Path_43]] - degree 12, connects to 6 communities
- [[unit_path()]] - degree 12, connects to 3 communities
- [[_read_files()]] - degree 12, connects to 3 communities
- [[_partition_semantic_files()]] - degree 8, connects to 3 communities