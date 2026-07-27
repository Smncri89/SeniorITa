---
type: community
cohesion: 0.04
members: 62
---

# Community 24

**Cohesion:** 0.04 - loosely connected
**Members:** 62 nodes

## Members
- [[1948 a file stamped in an earlier run, then omitted from ``files`` on     a l]] - rationale - graphify/tests/test_detect.py
- [[2221 (portablerelative-key manifest) a manifest whose keys were     written]] - rationale - graphify/tests/test_detect.py
- [[2221 exact repro legacy manifest saved WITHOUT root (absolute keys),     then]] - rationale - graphify/tests/test_detect.py
- [[A previously-indexed file that becomes excluded (still on disk) must     land i]] - rationale - graphify/tests/test_detect.py
- [[A row for a file that still exists on disk but left the scan corpus     (newly]] - rationale - graphify/tests/test_detect.py
- [[A schema-drifted manifest whose entry stores mtime as a nested dict     (instea]] - rationale - graphify/tests/test_detect.py
- [[After a full-scan save prunes the excluded row, later incremental runs     repo]] - rationale - graphify/tests/test_detect.py
- [[Back-compat callers that don't pass ``root`` still get the legacy     absolute]] - rationale - graphify/tests/test_detect.py
- [[Code files must be stamped in the manifest regardless of semantic cache.]] - rationale - graphify/tests/test_detect.py
- [[Counterpart a manifest row whose file is gone from disk stays in     deleted_f]] - rationale - graphify/tests/test_detect.py
- [[End-to-end a manifest written at one root must be readable from a     differen]] - rationale - graphify/tests/test_detect.py
- [[Files in failed chunks have no semantic cache entry; save_manifest must     lea]] - rationale - graphify/tests/test_detect.py
- [[Files outside ``root`` (e.g. symlinked external corpora) are stored     absolut]] - rationale - graphify/tests/test_detect.py
- [[Genuine deletions keep being pruned when scan_corpus is passed.]] - rationale - graphify/tests/test_detect.py
- [[In-root symlinks must store under the symlink's own name, not the     resolved]] - rationale - graphify/tests/test_detect.py
- [[Inverse of func`_to_relative_for_storage`.      Re-anchor a stored key again]] - rationale - graphify/graphify/detect.py
- [[Legacy absolute-keyed manifests still load correctly when ``root``     is suppl]] - rationale - graphify/tests/test_detect.py
- [[Legacy float manifests must re-extract when mtime moves BACKWARDS (1859).]] - rationale - graphify/tests/test_detect.py
- [[Like detect(), but returns only new or modified files since the last run.]] - rationale - graphify/graphify/detect.py
- [[Load the manifest from a previous run. Returns {} on any error.      When ``ro]] - rationale - graphify/graphify/detect.py
- [[NFC-normalize a path string used as a manifest key.      On macOS, ``os.walk``]] - rationale - graphify/graphify/detect.py
- [[Non-regression for the fix above legacy float branch still skips when     the]] - rationale - graphify/tests/test_detect.py
- [[Out-of-root entries (--include sources, symlinked corpora) are never     walked]] - rationale - graphify/tests/test_detect.py
- [[Path_7]] - code
- [[Return ``key`` as a forward-slash relative path from ``root``.      Keys outsi]] - rationale - graphify/graphify/detect.py
- [[Rewrite a saved manifest so every key is in NFD form, simulating a     manifest]] - rationale - graphify/tests/test_detect.py
- [[Save current file mtimes + content hashes for change detection.      kind=ast]] - rationale - graphify/graphify/detect.py
- [[Without scan_corpus (changed_paths hooks, skill runbooks, 917) a     subset sa]] - rationale - graphify/tests/test_detect.py
- [[_nfc()]] - code - graphify/graphify/detect.py
- [[_rewrite_manifest_keys_nfd()]] - code - graphify/tests/test_detect.py
- [[_to_absolute_from_storage()]] - code - graphify/graphify/detect.py
- [[_to_relative_for_storage()]] - code - graphify/graphify/detect.py
- [[``load_manifest(root=...)`` re-anchors stored relative keys so the     in-memor]] - rationale - graphify/tests/test_detect.py
- [[``save_manifest(root=...)`` writes forward-slash relative keys.]] - rationale - graphify/tests/test_detect.py
- [[detect_incremental must forward follow_symlinks so symlinked sub-trees     appe]] - rationale - graphify/tests/test_detect.py
- [[detect_incremental()]] - code - graphify/graphify/detect.py
- [[load_manifest()]] - code - graphify/graphify/detect.py
- [[manifest.py]] - code - graphify/graphify/manifest.py
- [[save_manifest()]] - code - graphify/graphify/detect.py
- [[test_detect_incremental_exclusion_stable_across_runs()]] - code - graphify/tests/test_detect.py
- [[test_detect_incremental_legacy_float_reextracts_on_backwards_mtime()]] - code - graphify/tests/test_detect.py
- [[test_detect_incremental_legacy_float_skips_when_mtime_matches()]] - code - graphify/tests/test_detect.py
- [[test_detect_incremental_portable_across_paths()]] - code - graphify/tests/test_detect.py
- [[test_detect_incremental_propagates_follow_symlinks()]] - code - graphify/tests/test_detect.py
- [[test_detect_incremental_reports_excluded_not_deleted()]] - code - graphify/tests/test_detect.py
- [[test_detect_incremental_still_reports_real_deletions()]] - code - graphify/tests/test_detect.py
- [[test_detect_incremental_survives_dict_valued_mtime()]] - code - graphify/tests/test_detect.py
- [[test_load_manifest_absolutizes_relative_keys()]] - code - graphify/tests/test_detect.py
- [[test_load_manifest_passes_through_legacy_absolute_keys()]] - code - graphify/tests/test_detect.py
- [[test_manifest_nfc_keys_legacy_absolute()]] - code - graphify/tests/test_detect.py
- [[test_manifest_nfc_keys_survive_macos_path_forms()]] - code - graphify/tests/test_detect.py
- [[test_save_manifest_clear_semantic_erases_stale_hash_for_omitted_file()]] - code - graphify/tests/test_detect.py
- [[test_save_manifest_full_scan_keeps_out_of_root_rows()]] - code - graphify/tests/test_detect.py
- [[test_save_manifest_full_scan_prunes_excluded_but_alive_row()]] - code - graphify/tests/test_detect.py
- [[test_save_manifest_full_scan_still_prunes_missing_file()]] - code - graphify/tests/test_detect.py
- [[test_save_manifest_in_root_symlink_roundtrips()]] - code - graphify/tests/test_detect.py
- [[test_save_manifest_out_of_root_keeps_absolute()]] - code - graphify/tests/test_detect.py
- [[test_save_manifest_relativizes_keys_when_root_given()]] - code - graphify/tests/test_detect.py
- [[test_save_manifest_skips_semantic_hash_for_files_without_cache()]] - code - graphify/tests/test_detect.py
- [[test_save_manifest_subset_save_preserves_untouched_rows()]] - code - graphify/tests/test_detect.py
- [[test_save_manifest_without_filter_unchanged_for_code()]] - code - graphify/tests/test_detect.py
- [[test_save_manifest_without_root_keeps_absolute_keys()]] - code - graphify/tests/test_detect.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_24
SORT file.name ASC
```

## Connections to other communities
- 35 edges to [[_COMMUNITY_Community 1]]
- 24 edges to [[_COMMUNITY_Community 44]]
- 6 edges to [[_COMMUNITY_Community 100]]
- 5 edges to [[_COMMUNITY_Community 12]]
- 2 edges to [[_COMMUNITY_Community 11]]
- 2 edges to [[_COMMUNITY_Community 123]]
- 2 edges to [[_COMMUNITY_Community 15]]
- 2 edges to [[_COMMUNITY_Community 76]]
- 1 edge to [[_COMMUNITY_Community 51]]
- 1 edge to [[_COMMUNITY_Community 153]]

## Top bridge nodes
- [[Path_7]] - degree 32, connects to 6 communities
- [[save_manifest()]] - degree 34, connects to 5 communities
- [[detect_incremental()]] - degree 23, connects to 3 communities
- [[load_manifest()]] - degree 13, connects to 2 communities
- [[test_save_manifest_skips_semantic_hash_for_files_without_cache()]] - degree 4, connects to 2 communities