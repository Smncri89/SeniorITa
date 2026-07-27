---
type: community
cohesion: 0.02
members: 154
---

# Community 1

**Cohesion:** 0.02 - loosely connected
**Members:** 154 nodes

## Members
- [[1666 a bare snapshots dir with no .snap files is a legit code namespace]] - rationale - graphify/tests/test_detect.py
- [[2058 must not loosen the unambiguous names venv.venv_venv are still     pr]] - rationale - graphify/tests/test_detect.py
- [[2058 a real source directory named env or _env with no virtualenv     mark]] - rationale - graphify/tests/test_detect.py
- [[2058 an env dir that IS a real virtualenv (has markers) is still pruned,]] - rationale - graphify/tests/test_detect.py
- [[2112 .graphifyinclude support was removed (dead since 873).      A leftover]] - rationale - graphify/tests/test_detect.py
- [[.gitinfoexclude (where `git worktree add` records nested worktree paths,]] - rationale - graphify/tests/test_detect.py
- [[.graphify (extraction cache) must never be re-indexed as source (873).]] - rationale - graphify/tests/test_detect.py
- [[.graphifyignore is evaluated after .gitignore, so a `!` negation in it can]] - rationale - graphify/tests/test_detect.py
- [[.next (Next.js build cache) must be excluded even after dot-dir fix (873).]] - rationale - graphify/tests/test_detect.py
- [[.nox (nox virtualenvs, tox's successor) must be excluded like .tox (1804).]] - rationale - graphify/tests/test_detect.py
- [[A .gitignore in a subdirectory below the scan root is honored too (1206).]] - rationale - graphify/tests/test_detect.py
- [[A .graphifyignore at the git repo root is included when scanning a subdir.]] - rationale - graphify/tests/test_detect.py
- [[A .graphifyignore containing only a BOM yields zero patterns, not one     bogus]] - rationale - graphify/tests/test_detect.py
- [[A BOM at the start of $GIT_DIRinfoexclude must not corrupt the first     patt]] - rationale - graphify/tests/test_detect.py
- [[A BOM followed by a comment must still parse as a comment, not become     a `]] - rationale - graphify/tests/test_detect.py
- [[A BOM'd .gitignore below the scan root (loaded live during the walk,     1206]] - rationale - graphify/tests/test_detect.py
- [[A BOM'd .gitignore first pattern must match, exactly like git (2163).]] - rationale - graphify/tests/test_detect.py
- [[A UTF-8 BOM at the start of .graphifyignore must not corrupt the first     patt]] - rationale - graphify/tests/test_detect.py
- [[A closer (nested) .gitignore's `!` re-include wins over a root exclude,     mat]] - rationale - graphify/tests/test_detect.py
- [[A nested .gitignore ('data') in one project must not drop a sibling     projec]] - rationale - graphify/tests/test_detect.py
- [[A nested .gitignore containing a bare `` (auto-written by e.g. the     hypothe]] - rationale - graphify/tests/test_detect.py
- [[A nested .gitignore excluding a directory prevents descending into it.]] - rationale - graphify/tests/test_detect.py
- [[A prose file whose stem IS exactly a bare keyword still reads as a dump.]] - rationale - graphify/tests/test_detect.py
- [[A regular `` matches one component; recursive matching requires ``.]] - rationale - graphify/tests/test_detect.py
- [[A trailing slash restricts a pattern to directories, as in gitignore.]] - rationale - graphify/tests/test_detect.py
- [[An explicit follow_symlinks=False skips symlinked directories.]] - rationale - graphify/tests/test_detect.py
- [[Comment lines in .graphifyignore are not treated as patterns.]] - rationale - graphify/tests/test_detect.py
- [[Counterpart guard the anchor-scoped fix must not stop nested ignore     files]] - rationale - graphify/tests/test_detect.py
- [[Files inside .claudeworktrees (nested placement) are never indexed (1023).]] - rationale - graphify/tests/test_detect.py
- [[Files inside .github (workflows etc.) are now indexed (873).]] - rationale - graphify/tests/test_detect.py
- [[Files inside .worktrees are never indexed (947).]] - rationale - graphify/tests/test_detect.py
- [[Files matching .graphifyignore patterns are excluded from detect().]] - rationale - graphify/tests/test_detect.py
- [[Inside a VCS repo, parent .graphifyignore applies to subdirectory scans.]] - rationale - graphify/tests/test_detect.py
- [[No .graphifyignore is not an error.]] - rationale - graphify/tests/test_detect.py
- [[Noise dot dirs (.next, .nuxt, .graphify cache, …) are skipped (873).     Non-n]] - rationale - graphify/tests/test_detect.py
- [[Ordinary scans still walk normal directories by default.]] - rationale - graphify/tests/test_detect.py
- [[Precedence across all three sources a nested `.gitignore` `!` re-include     o]] - rationale - graphify/tests/test_detect.py
- [[Re-including a child cannot rescue it while its parent stays excluded.]] - rationale - graphify/tests/test_detect.py
- [[Return True if this file likely contains secrets and should be skipped.]] - rationale - graphify/graphify/detect.py
- [[Symlink directory following is explicit opt-in.]] - rationale - graphify/tests/test_detect.py
- [[Upward search stops at the git repo root (.git directory).]] - rationale - graphify/tests/test_detect.py
- [[Video files do not contribute to total_words.]] - rationale - graphify/tests/test_detect.py
- [[When both exist, their patterns are MERGED — a file excluded only by     .gitig]] - rationale - graphify/tests/test_detect.py
- [[When no .graphifyignore exists, .gitignore patterns are honored (945).]] - rationale - graphify/tests/test_detect.py
- [[Without a VCS root, parent .graphifyignore does NOT apply (hermetic).]] - rationale - graphify/tests/test_detect.py
- [[__snapshots__ and real jestvitest snapshots dirs are artefacts — excluded.]] - rationale - graphify/tests/test_detect.py
- [[_is_sensitive()]] - code - graphify/graphify/detect.py
- [[`` retains recursive gitignore matching at zero or more depths.]] - rationale - graphify/tests/test_detect.py
- [[`` stays at the root, so `!src` makes the subtree walkable (1975).]] - rationale - graphify/tests/test_detect.py
- [[coverage and lcov-report are noise dirs — HTML reports inside must be excluded]] - rationale - graphify/tests/test_detect.py
- [[detect()]] - code - graphify/graphify/detect.py
- [[detect() always surfaces a walk_errors list so callers can tell whether     enu]] - rationale - graphify/tests/test_detect.py
- [[detect() correctly counts video files and does not add them to word count.]] - rationale - graphify/tests/test_detect.py
- [[detect() result always includes a 'video' key even with no video files.]] - rationale - graphify/tests/test_detect.py
- [[extra_excludes patterns exclude matching files from detect() (947).]] - rationale - graphify/tests/test_detect.py
- [[os.walk silently skips a subtree whose scandir raises (permissions, or a     di]] - rationale - graphify/tests/test_detect.py
- [[parametrize_3]] - code
- [[storybook-static is a build artefact — must be excluded.]] - rationale - graphify/tests/test_detect.py
- [[test_anchored_double_star_crosses_path_segments()]] - code - graphify/tests/test_detect.py
- [[test_anchored_negation_cannot_skip_excluded_parent()]] - code - graphify/tests/test_detect.py
- [[test_anchored_root_wildcard_negation_reincludes_subtree()]] - code - graphify/tests/test_detect.py
- [[test_detect.py]] - code - graphify/tests/test_detect.py
- [[test_detect_allows_github_dir()]] - code - graphify/tests/test_detect.py
- [[test_detect_converts_google_workspace_shortcuts_when_enabled()]] - code - graphify/tests/test_detect.py
- [[test_detect_default_does_not_auto_follow_direct_symlink_child()]] - code - graphify/tests/test_detect.py
- [[test_detect_default_does_not_follow_when_no_symlinks()]] - code - graphify/tests/test_detect.py
- [[test_detect_explicit_false_overrides_auto_detect()]] - code - graphify/tests/test_detect.py
- [[test_detect_extra_excludes_pattern()]] - code - graphify/tests/test_detect.py
- [[test_detect_finds_fixtures()]] - code - graphify/tests/test_detect.py
- [[test_detect_finds_video_files()]] - code - graphify/tests/test_detect.py
- [[test_detect_follows_symlinked_directory()]] - code - graphify/tests/test_detect.py
- [[test_detect_follows_symlinked_file()]] - code - graphify/tests/test_detect.py
- [[test_detect_handles_circular_symlinks()]] - code - graphify/tests/test_detect.py
- [[test_detect_honors_git_info_exclude()]] - code - graphify/tests/test_detect.py
- [[test_detect_includes_video_key()]] - code - graphify/tests/test_detect.py
- [[test_detect_keeps_env_source_dirs()]] - code - graphify/tests/test_detect.py
- [[test_detect_keeps_snapshots_code_namespace()]] - code - graphify/tests/test_detect.py
- [[test_detect_prunes_venv_names_without_markers()]] - code - graphify/tests/test_detect.py
- [[test_detect_records_unclassified_extensionless_files()]] - code - graphify/tests/test_detect.py
- [[test_detect_reports_walk_errors_key()]] - code - graphify/tests/test_detect.py
- [[test_detect_skips_coverage_dir()]] - code - graphify/tests/test_detect.py
- [[test_detect_skips_google_workspace_shortcuts_by_default()]] - code - graphify/tests/test_detect.py
- [[test_detect_skips_graphify_own_cache()]] - code - graphify/tests/test_detect.py
- [[test_detect_skips_nested_worktrees_dir()]] - code - graphify/tests/test_detect.py
- [[test_detect_skips_next_cache()]] - code - graphify/tests/test_detect.py
- [[test_detect_skips_noise_dot_dirs()]] - code - graphify/tests/test_detect.py
- [[test_detect_skips_nox_virtualenv()]] - code - graphify/tests/test_detect.py
- [[test_detect_skips_out_of_root_symlinked_directory_even_when_following()]] - code - graphify/tests/test_detect.py
- [[test_detect_skips_out_of_root_symlinked_file_by_default()]] - code - graphify/tests/test_detect.py
- [[test_detect_skips_snapshots_dir()]] - code - graphify/tests/test_detect.py
- [[test_detect_skips_storybook_static_dir()]] - code - graphify/tests/test_detect.py
- [[test_detect_skips_visual_tests_dir()]] - code - graphify/tests/test_detect.py
- [[test_detect_skips_worktrees_dir()]] - code - graphify/tests/test_detect.py
- [[test_detect_still_prunes_real_env_venv()]] - code - graphify/tests/test_detect.py
- [[test_detect_surfaces_unreadable_dir_instead_of_silent_skip()]] - code - graphify/tests/test_detect.py
- [[test_detect_unclassified_empty_when_all_supported()]] - code - graphify/tests/test_detect.py
- [[test_detect_video_not_in_words()]] - code - graphify/tests/test_detect.py
- [[test_detect_warns_small_corpus()]] - code - graphify/tests/test_detect.py
- [[test_directory_only_negation_does_not_reinclude_file()]] - code - graphify/tests/test_detect.py
- [[test_git_info_exclude_utf8_bom()]] - code - graphify/tests/test_detect.py
- [[test_gitignore_fallback_when_no_graphifyignore()]] - code - graphify/tests/test_detect.py
- [[test_gitignore_nested_below_root_excludes_file()]] - code - graphify/tests/test_detect.py
- [[test_gitignore_nested_below_root_prunes_whole_directory()]] - code - graphify/tests/test_detect.py
- [[test_gitignore_nested_negation_overrides_broader_root_rule()]] - code - graphify/tests/test_detect.py
- [[test_gitignore_utf8_bom_matches_git()]] - code - graphify/tests/test_detect.py
- [[test_graphifyignore_and_gitignore_are_merged()]] - code - graphify/tests/test_detect.py
- [[test_graphifyignore_at_git_root_is_included()]] - code - graphify/tests/test_detect.py
- [[test_graphifyignore_bom_only_file()]] - code - graphify/tests/test_detect.py
- [[test_graphifyignore_bom_then_comment()]] - code - graphify/tests/test_detect.py
- [[test_graphifyignore_comments_ignored()]] - code - graphify/tests/test_detect.py
- [[test_graphifyignore_discovered_from_parent_in_vcs()]] - code - graphify/tests/test_detect.py
- [[test_graphifyignore_excludes_file()]] - code - graphify/tests/test_detect.py
- [[test_graphifyignore_hermetic_without_vcs()]] - code - graphify/tests/test_detect.py
- [[test_graphifyignore_missing_is_fine()]] - code - graphify/tests/test_detect.py
- [[test_graphifyignore_negation_overrides_gitignore()]] - code - graphify/tests/test_detect.py
- [[test_graphifyignore_stops_at_git_boundary()]] - code - graphify/tests/test_detect.py
- [[test_graphifyignore_utf8_bom_first_pattern_honored()]] - code - graphify/tests/test_detect.py
- [[test_graphifyinclude_is_inert_and_not_unclassified()]] - code - graphify/tests/test_detect.py
- [[test_nested_gitignore_does_not_govern_sibling_project()]] - code - graphify/tests/test_detect.py
- [[test_nested_gitignore_patterns_still_apply_inside_their_dir()]] - code - graphify/tests/test_detect.py
- [[test_nested_gitignore_star_does_not_ignore_outside_its_dir()]] - code - graphify/tests/test_detect.py
- [[test_nested_gitignore_utf8_bom()]] - code - graphify/tests/test_detect.py
- [[test_nested_ignore_overrides_git_info_exclude_and_root()]] - code - graphify/tests/test_detect.py
- [[test_path_pattern_single_star_does_not_cross_segment()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_bare_keyword_prose_still_dropped()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_dir_carveout_does_not_bypass_name_screens()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_dir_carveout_still_drops_tfvars_values_store()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_does_not_flag_password_policy_discussion()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_does_not_flag_passwords_py()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_does_not_flag_root_file_named_credentials()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_does_not_flag_ruby_code_modules()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_does_not_flag_source_under_secrets_dir()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_does_not_flag_token_economics_note()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_does_not_flag_tokenize_py()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_does_not_flag_tokenizer_py()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_filter_indexes_topic_prose_and_source()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_filter_still_excludes_real_secrets()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_flags_api_token_txt()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_flags_credentials_json()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_flags_dotfile_token()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_flags_everything_under_credential_store_dirs()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_flags_keyword_at_end_of_long_name()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_flags_my_private_key_txt()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_flags_oauth_token_json()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_flags_plural_tokens_txt()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_flags_secrets_dir()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_flags_ssh_dir()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_flags_token_txt()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_flags_underscore_secret()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_secret_handler_txt()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_still_flags_data_secret_stores()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_still_flags_data_under_secrets_dir()]] - code - graphify/tests/test_detect.py
- [[test_sensitive_token_config_yaml()]] - code - graphify/tests/test_detect.py
- [[visual-tests bundles and snapshots are noise — must be excluded (869).]] - rationale - graphify/tests/test_detect.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1
SORT file.name ASC
```

## Connections to other communities
- 51 edges to [[_COMMUNITY_Community 11]]
- 35 edges to [[_COMMUNITY_Community 24]]
- 14 edges to [[_COMMUNITY_Community 123]]
- 11 edges to [[_COMMUNITY_Community 44]]
- 6 edges to [[_COMMUNITY_Community 153]]
- 5 edges to [[_COMMUNITY_Community 100]]
- 3 edges to [[_COMMUNITY_Community 12]]
- 3 edges to [[_COMMUNITY_Community 168]]
- 2 edges to [[_COMMUNITY_Community 115]]
- 2 edges to [[_COMMUNITY_Community 15]]
- 2 edges to [[_COMMUNITY_Community 209]]
- 2 edges to [[_COMMUNITY_Community 335]]
- 1 edge to [[_COMMUNITY_Community 301]]
- 1 edge to [[_COMMUNITY_Community 51]]
- 1 edge to [[_COMMUNITY_Community 32]]
- 1 edge to [[_COMMUNITY_Community 38]]

## Top bridge nodes
- [[detect()]] - degree 97, connects to 13 communities
- [[test_detect.py]] - degree 199, connects to 9 communities
- [[_is_sensitive()]] - degree 39, connects to 4 communities