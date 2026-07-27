---
type: community
cohesion: 0.11
members: 28
---

# Community 106

**Cohesion:** 0.11 - loosely connected
**Members:** 28 nodes

## Members
- [[1939 a skill's cache read and write must both name the extraction prompt]] - rationale - graphify/tests/test_skillgen.py
- [[A full render carries the always-on files; a --platform render does not.]] - rationale - graphify/tests/test_skillgen.py
- [[A hand-edit of an always_on.md is caught by --check (the drift guard).]] - rationale - graphify/tests/test_skillgen.py
- [[A single generated file its repo-relative path and exact bytes.]] - rationale - graphify/tools/skillgen/gen.py
- [[Byte-diff the render against both committed artifacts and expected.      Retu]] - rationale - graphify/tools/skillgen/gen.py
- [[Generated artifacts use LF newlines and end in exactly one newline.]] - rationale - graphify/tests/test_skillgen.py
- [[No generated artifact carries the package version string.]] - rationale - graphify/tests/test_skillgen.py
- [[Parse platforms.toml into Platform records, keyed by platform name.]] - rationale - graphify/tools/skillgen/gen.py
- [[Regression for 1461 every skill body that describes Step 3 extraction must]] - rationale - graphify/tests/test_skillgen.py
- [[Render the selected platforms (or all), flattened into one artifact list.]] - rationale - graphify/tools/skillgen/gen.py
- [[RenderedArtifact]] - code - graphify/tools/skillgen/gen.py
- [[Rendering twice yields byte-identical output (no timestampsversions).]] - rationale - graphify/tests/test_skillgen.py
- [[The committed artifacts and the expected snapshot match a fresh render.]] - rationale - graphify/tests/test_skillgen.py
- [[The committed codexwindows artifacts match a fresh render and expected.]] - rationale - graphify/tests/test_skillgen.py
- [[check + audit-coverage pass for every rendered progressive host.]] - rationale - graphify/tests/test_skillgen.py
- [[check()]] - code - graphify/tools/skillgen/gen.py
- [[load_platforms()]] - code - graphify/tools/skillgen/gen.py
- [[render_all()]] - code - graphify/tools/skillgen/gen.py
- [[test_all_progressive_hosts_check_and_audit_clean()]] - code - graphify/tests/test_skillgen.py
- [[test_always_on_files_are_guarded_by_check()]] - code - graphify/tests/test_skillgen.py
- [[test_always_on_included_in_full_render_not_per_platform()]] - code - graphify/tests/test_skillgen.py
- [[test_check_passes()]] - code - graphify/tests/test_skillgen.py
- [[test_check_passes_for_codex_and_windows()]] - code - graphify/tests/test_skillgen.py
- [[test_extraction_states_no_api_key_required_for_every_host()]] - code - graphify/tests/test_skillgen.py
- [[test_no_version_or_timestamp_in_output()]] - code - graphify/tests/test_skillgen.py
- [[test_render_is_idempotent()]] - code - graphify/tests/test_skillgen.py
- [[test_render_output_is_lf_only()]] - code - graphify/tests/test_skillgen.py
- [[test_semantic_cache_calls_pass_prompt_file_for_every_split_host()]] - code - graphify/tests/test_skillgen.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_106
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_Community 54]]
- 10 edges to [[_COMMUNITY_Community 92]]
- 10 edges to [[_COMMUNITY_Community 43]]
- 8 edges to [[_COMMUNITY_Community 129]]
- 2 edges to [[_COMMUNITY_Community 167]]
- 2 edges to [[_COMMUNITY_Community 256]]
- 2 edges to [[_COMMUNITY_Community 257]]
- 1 edge to [[_COMMUNITY_Community 287]]

## Top bridge nodes
- [[load_platforms()]] - degree 33, connects to 7 communities
- [[render_all()]] - degree 19, connects to 5 communities
- [[RenderedArtifact]] - degree 9, connects to 3 communities
- [[test_all_progressive_hosts_check_and_audit_clean()]] - degree 6, connects to 2 communities
- [[check()]] - degree 9, connects to 1 community