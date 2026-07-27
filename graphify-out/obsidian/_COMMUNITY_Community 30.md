---
type: community
cohesion: 0.06
members: 55
---

# Community 30

**Cohesion:** 0.06 - loosely connected
**Members:** 55 nodes

## Members
- [[1894 repro over a warm manifest + warm standard semantic cache,     `extract]] - rationale - graphify/tests/test_extract_cli.py
- [[1897 fresh extraction returns nodes with ROOT-RELATIVE source_file,     while]] - rationale - graphify/tests/test_extract_cli.py
- [[1920 end-to-end a fresh extraction whose only output for a doc is a     hyper]] - rationale - graphify/tests/test_extract_cli.py
- [[1920 a doc whose only chunk output is a hyperedge (3+ nodes sharing a     con]] - rationale - graphify/tests/test_extract_cli.py
- [[1925 `graphify extract --code-only` with a MISSING manifest.json must     not]] - rationale - graphify/tests/test_extract_cli.py
- [[1939 cache-check --prompt-file only counts entries produced by that same]] - rationale - graphify/tests/test_extract_cli.py
- [[1948 caller-side guard an incremental run that only re-dispatches the     CHA]] - rationale - graphify/tests/test_extract_cli.py
- [[1948 x 1950 interaction a doc stamped complete on a prior run that     TRUNC]] - rationale - graphify/tests/test_extract_cli.py
- [[--no-cluster's exclusion-only early exit must still scrub the excluded     file]] - rationale - graphify/tests/test_extract_cli.py
- [[A code-only corpus must run with no LLM API key.      Regression graphify ext]] - rationale - graphify/tests/test_extract_cli.py
- [[A corpus with only code — no docspapersimages.]] - rationale - graphify/tests/test_extract_cli.py
- [[Clear every env var that detect_backend() or _get_backend_api_key() reads.]] - rationale - graphify/tests/test_extract_cli.py
- [[GRAPHIFY_FORCE=1 behaves like --force (env parity with `update`).]] - rationale - graphify/tests/test_extract_cli.py
- [[Key requirement still fires when semantic work is needed.      A corpus with a]] - rationale - graphify/tests/test_extract_cli.py
- [[Minimal corpus one Go code file + one Markdown doc.      Both file types are]] - rationale - graphify/tests/test_extract_cli.py
- [[Post-1897 state the excluded file IS manifest-listed. It must be     pruned f]] - rationale - graphify/tests/test_extract_cli.py
- [[Sanity counter-test a successful chunk run keeps exit 0. Confirms the     new]] - rationale - graphify/tests/test_extract_cli.py
- [[Seed a graph with nodes for x.py, drop x.py from the manifest (pre-1897     ma]] - rationale - graphify/tests/test_extract_cli.py
- [[Tests for `graphify extract` CLI dispatch path in graphify.__main__.]] - rationale - graphify/tests/test_extract_cli.py
- [[Unit test for the 1897 helper relative (fresh) and absolute (cache-hit)     s]] - rationale - graphify/tests/test_extract_cli.py
- [[When every semantic chunk errors (e.g. backend SDK not installed),     the CLI]] - rationale - graphify/tests/test_extract_cli.py
- [[_clear_backend_keys()]] - code - graphify/tests/test_extract_cli.py
- [[_code_only_corpus()]] - code - graphify/tests/test_extract_cli.py
- [[_make_corpus()_1]] - code - graphify/tests/test_extract_cli.py
- [[_node_sources()]] - code - graphify/tests/test_extract_cli.py
- [[_recording_extractor()]] - code - graphify/tests/test_extract_cli.py
- [[_run_extract()]] - code - graphify/tests/test_extract_cli.py
- [[_two_file_corpus()]] - code - graphify/tests/test_extract_cli.py
- [[`extract --out DIR` routes every artifact to DIRgraphify-out and the     scan]] - rationale - graphify/tests/test_extract_cli.py
- [[cache-check --mode deep consults cachesemantic-deep; without the flag     it]] - rationale - graphify/tests/test_extract_cli.py
- [[extract accepts --force a warm tree re-dispatches every semantic file     (cac]] - rationale - graphify/tests/test_extract_cli.py
- [[extract_corpus_parallel stand-in that records each dispatch.]] - rationale - graphify/tests/test_extract_cli.py
- [[parametrize_5]] - code
- [[test_cache_check_mode_deep_reads_deep_namespace()]] - code - graphify/tests/test_extract_cli.py
- [[test_cache_check_prompt_file_scopes_hits_to_that_prompt()]] - code - graphify/tests/test_extract_cli.py
- [[test_extract_cli.py]] - code - graphify/tests/test_extract_cli.py
- [[test_extract_codeonly_succeeds_without_api_key()]] - code - graphify/tests/test_extract_cli.py
- [[test_extract_exits_nonzero_when_all_semantic_chunks_fail()]] - code - graphify/tests/test_extract_cli.py
- [[test_extract_force_flag_redispatches_and_stamps_manifest()]] - code - graphify/tests/test_extract_cli.py
- [[test_extract_graphify_force_env_redispatches()]] - code - graphify/tests/test_extract_cli.py
- [[test_extract_mode_deep_dispatches_over_warm_cache()]] - code - graphify/tests/test_extract_cli.py
- [[test_extract_out_keeps_project_root_clean()]] - code - graphify/tests/test_extract_cli.py
- [[test_extract_succeeds_when_at_least_one_chunk_completes()]] - code - graphify/tests/test_extract_cli.py
- [[test_extract_without_key_still_errors_when_docs_present()]] - code - graphify/tests/test_extract_cli.py
- [[test_incremental_extract_prunes_excluded_file_listed_in_manifest()]] - code - graphify/tests/test_extract_cli.py
- [[test_incremental_extract_prunes_newly_excluded_file_not_in_manifest()]] - code - graphify/tests/test_extract_cli.py
- [[test_incremental_partial_run_preserves_untouched_semantic_hash()]] - code - graphify/tests/test_extract_cli.py
- [[test_manifest_stamps_freshly_extracted_semantic_docs()]] - code - graphify/tests/test_extract_cli.py
- [[test_manifest_stamps_hyperedge_only_docs()]] - code - graphify/tests/test_extract_cli.py
- [[test_missing_manifest_code_only_preserves_semantic_layer()]] - code - graphify/tests/test_extract_cli.py
- [[test_no_cluster_incremental_prunes_newly_excluded_file()]] - code - graphify/tests/test_extract_cli.py
- [[test_pathless_postgres_extract_initializes_empty_detection()]] - code - graphify/tests/test_extract_cli.py
- [[test_stamped_manifest_files_counts_hyperedge_only_docs()]] - code - graphify/tests/test_extract_cli.py
- [[test_stamped_manifest_files_normalizes_both_sides()]] - code - graphify/tests/test_extract_cli.py
- [[test_truncated_doc_semantic_hash_is_cleared_for_requeue()]] - code - graphify/tests/test_extract_cli.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_30
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Community 47]]
- 3 edges to [[_COMMUNITY_Community 57]]
- 3 edges to [[_COMMUNITY_Community 12]]
- 1 edge to [[_COMMUNITY_Community 4]]
- 1 edge to [[_COMMUNITY_Community 145]]

## Top bridge nodes
- [[test_extract_cli.py]] - degree 33, connects to 4 communities
- [[_run_extract()]] - degree 12, connects to 2 communities
- [[test_no_cluster_incremental_prunes_newly_excluded_file()]] - degree 6, connects to 1 community
- [[test_extract_codeonly_succeeds_without_api_key()]] - degree 5, connects to 1 community
- [[test_extract_out_keeps_project_root_clean()]] - degree 5, connects to 1 community