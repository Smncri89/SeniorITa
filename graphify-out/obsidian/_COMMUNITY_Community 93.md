---
type: community
cohesion: 0.07
members: 29
---

# Community 93

**Cohesion:** 0.07 - loosely connected
**Members:** 29 nodes

## Members
- [[A non-splittable single-file truncation keeps its partial result but     marks]] - rationale - graphify/tests/test_chunking.py
- [[A single file that truncates can't be split further — surface a     warning and]] - rationale - graphify/tests/test_chunking.py
- [[A truncation that IS recovered by splitting yields a complete result —     it m]] - rationale - graphify/tests/test_chunking.py
- [[BaseException]] - code
- [[Extract a chunk; if the response is truncated (`finish_reason=length`)     or]] - rationale - graphify/graphify/llm.py
- [[Heuristically classify an exception as a context-window overflow.      Differe]] - rationale - graphify/graphify/llm.py
- [[If everything truncates, retries stop at max_depth — partial result     kept wi]] - rationale - graphify/tests/test_chunking.py
- [[No retry when finish_reason='stop' — single call, result passes through.]] - rationale - graphify/tests/test_chunking.py
- [[Union of the ``_partial_files`` carried by each result (survives merges).]] - rationale - graphify/graphify/llm.py
- [[When even the half-chunk truncates, split again. With 8 files and a     truncat]] - rationale - graphify/tests/test_chunking.py
- [[When recursion caps at max_depth with everything still truncated, the     merge]] - rationale - graphify/tests/test_chunking.py
- [[_extract_with_adaptive_retry()]] - code - graphify/graphify/llm.py
- [[_looks_like_context_exceeded()]] - code - graphify/graphify/llm.py
- [[_merged_partial_files()]] - code - graphify/graphify/llm.py
- [[finish_reason='length' triggers split-in-half. Both halves succeed     on the s]] - rationale - graphify/tests/test_chunking.py
- [[test_adaptive_retry_bisects_on_hollow_ollama_response()]] - code - graphify/tests/test_llm_backends.py
- [[test_adaptive_retry_caps_at_max_depth()]] - code - graphify/tests/test_chunking.py
- [[test_adaptive_retry_gives_up_on_single_file_overflow()]] - code - graphify/tests/test_llm_backends.py
- [[test_adaptive_retry_marks_max_depth_giveup_partial()]] - code - graphify/tests/test_chunking.py
- [[test_adaptive_retry_marks_single_file_truncation_partial()]] - code - graphify/tests/test_chunking.py
- [[test_adaptive_retry_re_raises_unrelated_errors()]] - code - graphify/tests/test_llm_backends.py
- [[test_adaptive_retry_recurses_for_persistent_truncation()]] - code - graphify/tests/test_chunking.py
- [[test_adaptive_retry_returns_directly_when_not_truncated()]] - code - graphify/tests/test_chunking.py
- [[test_adaptive_retry_single_file_truncation_does_not_recurse()]] - code - graphify/tests/test_chunking.py
- [[test_adaptive_retry_splits_on_context_exceeded()]] - code - graphify/tests/test_llm_backends.py
- [[test_adaptive_retry_splits_when_finish_reason_length()]] - code - graphify/tests/test_chunking.py
- [[test_adaptive_retry_successful_split_is_not_marked_partial()]] - code - graphify/tests/test_chunking.py
- [[test_looks_like_context_exceeded_ignores_unrelated_errors()]] - code - graphify/tests/test_llm_backends.py
- [[test_looks_like_context_exceeded_matches_common_messages()]] - code - graphify/tests/test_llm_backends.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_93
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Community 20]]
- 6 edges to [[_COMMUNITY_Community 58]]
- 6 edges to [[_COMMUNITY_Community 16]]
- 1 edge to [[_COMMUNITY_Community 72]]
- 1 edge to [[_COMMUNITY_Community 39]]
- 1 edge to [[_COMMUNITY_Community 57]]

## Top bridge nodes
- [[_extract_with_adaptive_retry()]] - degree 23, connects to 5 communities
- [[_looks_like_context_exceeded()]] - degree 6, connects to 1 community
- [[_merged_partial_files()]] - degree 3, connects to 1 community
- [[test_adaptive_retry_caps_at_max_depth()]] - degree 3, connects to 1 community
- [[test_adaptive_retry_marks_max_depth_giveup_partial()]] - degree 3, connects to 1 community