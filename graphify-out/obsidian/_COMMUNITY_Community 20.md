---
type: community
cohesion: 0.04
members: 70
---

# Community 20

**Cohesion:** 0.04 - loosely connected
**Members:** 70 nodes

## Members
- [[1632 merged nodeedge order must be deterministic (submission order),     not]] - rationale - graphify/tests/test_chunking.py
- [[1870 the checkpoint's allowlist must resolve a FileSlice to its parent     pa]] - rationale - graphify/tests/test_chunking.py
- [[1890 a chunk can return a clean, non-empty response that omits some of the]] - rationale - graphify/tests/test_chunking.py
- [[1894 the per-chunk checkpoint must follow the run's mode — a     deep_mode=Tr]] - rationale - graphify/tests/test_chunking.py
- [[1895 the 1757 cache guard skips the CACHE write for a node attributed     to]] - rationale - graphify/tests/test_chunking.py
- [[.ok()]] - code - graphify/graphify/multigraph_compat.py
- [[A doc containing a literal tiktoken special token (e.g. endoftext)     must]] - rationale - graphify/tests/test_chunking.py
- [[A file larger than the budget can't be split — it goes alone in a chunk.]] - rationale - graphify/tests/test_chunking.py
- [[A single chunk raising should be logged but not abort the run.     Other chunks]] - rationale - graphify/tests/test_chunking.py
- [[A single-file chunk that stays truncated is checkpointed as a PARTIAL     entry]] - rationale - graphify/tests/test_chunking.py
- [[Append a chunk result into the running merged accumulator.]] - rationale - graphify/graphify/llm.py
- [[Build a deterministic fake extraction result for a chunk.]] - rationale - graphify/tests/test_chunking.py
- [[Build a stub extraction result with a controllable finish_reason.]] - rationale - graphify/tests/test_chunking.py
- [[Counter-test a clean run records out_of_scope_dropped == 0 and no warning.]] - rationale - graphify/tests/test_chunking.py
- [[End to end packing a corpus that includes a special-token doc must not     rai]] - rationale - graphify/tests/test_chunking.py
- [[End-to-end extract_corpus_parallel routes through adaptive retry,     so a chu]] - rationale - graphify/tests/test_chunking.py
- [[Estimate the prompt-token cost of a file or slice under `_read_files` rules.]] - rationale - graphify/graphify/llm.py
- [[Extract a corpus in chunks, merging results.      Chunking strategy]] - rationale - graphify/graphify/llm.py
- [[Files in the same directory should land in the same chunk when they fit.]] - rationale - graphify/tests/test_chunking.py
- [[Force the chars4 fallback so packing math is deterministic regardless     of w]] - rationale - graphify/tests/test_chunking.py
- [[Greedily pack filesslices into chunks that fit a token budget.      Units are]] - rationale - graphify/graphify/llm.py
- [[Many small files should land in a single chunk, not one chunk per file.]] - rationale - graphify/tests/test_chunking.py
- [[Return the semantic-extraction system prompt, optionally in deep mode.]] - rationale - graphify/graphify/llm.py
- [[Tests for token-aware chunking and parallel chunk execution in graphify.llm.]] - rationale - graphify/tests/test_chunking.py
- [[The native-backend prompt must request hyperedges, like the skill's     extract]] - rationale - graphify/tests/test_llm_backends.py
- [[When the next file would push the chunk past the budget, start a new chunk.]] - rationale - graphify/tests/test_chunking.py
- [[When tiktoken is installed, the estimator should call into it for     accurate]] - rationale - graphify/tests/test_chunking.py
- [[With max_concurrency  1, total wall time should be ~max(chunk times),     not]] - rationale - graphify/tests/test_chunking.py
- [[With the default token_budget, many tiny files pack into one chunk.]] - rationale - graphify/tests/test_chunking.py
- [[Without tiktoken installed, the estimator falls back to chars4.]] - rationale - graphify/tests/test_chunking.py
- [[_estimate_file_tokens()]] - code - graphify/graphify/llm.py
- [[_extraction_system()]] - code - graphify/graphify/llm.py
- [[_merge_into()]] - code - graphify/graphify/llm.py
- [[_pack_chunks_by_tokens()]] - code - graphify/graphify/llm.py
- [[_stub_chunk_result()]] - code - graphify/tests/test_chunking.py
- [[_stub_with_finish()]] - code - graphify/tests/test_chunking.py
- [[extract_corpus_parallel must accept a cache_root kwarg without raising     (imp]] - rationale - graphify/tests/test_semantic_cache_out_root.py
- [[extract_corpus_parallel()]] - code - graphify/graphify/llm.py
- [[max_concurrency=1 should run sequentially (no thread pool).]] - rationale - graphify/tests/test_chunking.py
- [[no_tokenizer()]] - code - graphify/tests/test_chunking.py
- [[test_checkpoint_caches_sliced_document_chunks()]] - code - graphify/tests/test_chunking.py
- [[test_checkpoint_writes_deep_namespace_in_deep_mode()]] - code - graphify/tests/test_chunking.py
- [[test_chunking.py]] - code - graphify/tests/test_chunking.py
- [[test_corpus_parallel_continues_after_chunk_failure()]] - code - graphify/tests/test_chunking.py
- [[test_corpus_parallel_legacy_mode_when_token_budget_is_none()]] - code - graphify/tests/test_chunking.py
- [[test_corpus_parallel_merge_order_is_submission_order_not_completion()]] - code - graphify/tests/test_chunking.py
- [[test_corpus_parallel_oversized_markdown_does_not_crash_on_fileslice()]] - code - graphify/tests/test_llm_backends.py
- [[test_corpus_parallel_runs_chunks_concurrently()]] - code - graphify/tests/test_chunking.py
- [[test_corpus_parallel_sequential_when_max_concurrency_is_one()]] - code - graphify/tests/test_chunking.py
- [[test_corpus_parallel_token_budget_default_packs_files()]] - code - graphify/tests/test_chunking.py
- [[test_corpus_parallel_uses_adaptive_retry()]] - code - graphify/tests/test_chunking.py
- [[test_estimate_file_tokens_falls_back_to_chars_when_no_tokenizer()]] - code - graphify/tests/test_chunking.py
- [[test_estimate_file_tokens_handles_tiktoken_special_token()]] - code - graphify/tests/test_chunking.py
- [[test_estimate_file_tokens_uses_tiktoken_when_available()]] - code - graphify/tests/test_chunking.py
- [[test_extract_corpus_parallel_accepts_cache_root_kwarg()]] - code - graphify/tests/test_semantic_cache_out_root.py
- [[test_extract_corpus_parallel_accepts_str_and_mixed_paths()]] - code - graphify/tests/test_llm_backends.py
- [[test_extract_corpus_parallel_ollama_runs_serially()]] - code - graphify/tests/test_llm_backends.py
- [[test_image_token_estimate_is_flat()]] - code - graphify/tests/test_image_vision.py
- [[test_native_extraction_prompt_requests_hyperedges()]] - code - graphify/tests/test_llm_backends.py
- [[test_omitted_documents_are_reconciled_and_warned()]] - code - graphify/tests/test_chunking.py
- [[test_out_of_scope_drop_count_is_zero_when_all_in_scope()]] - code - graphify/tests/test_chunking.py
- [[test_out_of_scope_nodes_are_dropped_from_merged_result()]] - code - graphify/tests/test_chunking.py
- [[test_pack_chunks_groups_by_directory()]] - code - graphify/tests/test_chunking.py
- [[test_pack_chunks_oversized_file_gets_its_own_chunk()]] - code - graphify/tests/test_chunking.py
- [[test_pack_chunks_packs_small_files_together()]] - code - graphify/tests/test_chunking.py
- [[test_pack_chunks_rejects_non_positive_budget()]] - code - graphify/tests/test_chunking.py
- [[test_pack_chunks_starts_new_chunk_when_budget_would_overflow()]] - code - graphify/tests/test_chunking.py
- [[test_pack_chunks_with_special_token_doc_does_not_crash()]] - code - graphify/tests/test_chunking.py
- [[test_truncated_chunk_is_cached_partial_and_missed_on_reload()]] - code - graphify/tests/test_chunking.py
- [[token_budget=None should fall back to legacy fixed-count chunking.]] - rationale - graphify/tests/test_chunking.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_20
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Community 58]]
- 9 edges to [[_COMMUNITY_Community 57]]
- 9 edges to [[_COMMUNITY_Community 93]]
- 6 edges to [[_COMMUNITY_Community 72]]
- 6 edges to [[_COMMUNITY_Community 16]]
- 5 edges to [[_COMMUNITY_Community 38]]
- 4 edges to [[_COMMUNITY_Community 12]]
- 3 edges to [[_COMMUNITY_Community 39]]
- 2 edges to [[_COMMUNITY_Community 174]]
- 1 edge to [[_COMMUNITY_Community 89]]
- 1 edge to [[_COMMUNITY_Community 33]]
- 1 edge to [[_COMMUNITY_Community 131]]
- 1 edge to [[_COMMUNITY_Community 119]]

## Top bridge nodes
- [[extract_corpus_parallel()]] - degree 32, connects to 7 communities
- [[_extraction_system()]] - degree 15, connects to 7 communities
- [[test_chunking.py]] - degree 43, connects to 4 communities
- [[_pack_chunks_by_tokens()]] - degree 15, connects to 3 communities
- [[_estimate_file_tokens()]] - degree 10, connects to 2 communities