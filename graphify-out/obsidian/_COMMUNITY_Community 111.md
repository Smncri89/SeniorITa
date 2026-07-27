---
type: community
cohesion: 0.15
members: 26
---

# Community 111

**Cohesion:** 0.15 - loosely connected
**Members:** 26 nodes

## Members
- [[A rename pointing at an external (non-workspace) crate stays a no-op.      Gua]] - rationale - graphify/tests/test_cargo_introspect.py
- [[Any]] - code
- [[Cargo manifest introspection for workspace-internal crate dependencies.]] - rationale - graphify/graphify/cargo_introspect.py
- [[Degenerate but parseable manifests should not invent graph data or crash.]] - rationale - graphify/tests/test_cargo_introspect.py
- [[Large deterministic workspace proves chain extraction scales by shape, not timin]] - rationale - graphify/tests/test_cargo_introspect.py
- [[Legacy manifests still resolve path deps and ignore bare-string externals.]] - rationale - graphify/tests/test_cargo_introspect.py
- [[Malformed manifests surface the TOML parser failure, not an arbitrary crash.]] - rationale - graphify/tests/test_cargo_introspect.py
- [[Modern workspace forms cover virtual roots, workspace deps, and root packages.]] - rationale - graphify/tests/test_cargo_introspect.py
- [[Path_5]] - code
- [[Real workspace pin raw graph fields while excluding registry-only deps.]] - rationale - graphify/tests/test_cargo_introspect.py
- [[Renamed workspace-internal deps still produce a `crate_depends_on` edge (1858).]] - rationale - graphify/tests/test_cargo_introspect.py
- [[Return crate nodes and internal dependency edges from Cargo manifests.]] - rationale - graphify/graphify/cargo_introspect.py
- [[_load_toml()]] - code - graphify/graphify/cargo_introspect.py
- [[_member_manifest_paths()]] - code - graphify/graphify/cargo_introspect.py
- [[_write_manifest()]] - code - graphify/tests/test_cargo_introspect.py
- [[cargo_introspect.py]] - code - graphify/graphify/cargo_introspect.py
- [[introspect_cargo()]] - code - graphify/graphify/cargo_introspect.py
- [[test_cargo_introspect.py]] - code - graphify/tests/test_cargo_introspect.py
- [[test_cargo_introspect_degenerate_manifests_return_empty_or_skip_bad_deps()]] - code - graphify/tests/test_cargo_introspect.py
- [[test_cargo_introspect_honors_package_rename_on_internal_dep()]] - code - graphify/tests/test_cargo_introspect.py
- [[test_cargo_introspect_large_workspace_dependency_chain()]] - code - graphify/tests/test_cargo_introspect.py
- [[test_cargo_introspect_malformed_toml_reports_parser_error()]] - code - graphify/tests/test_cargo_introspect.py
- [[test_cargo_introspect_modern_virtual_and_root_package_workspaces()]] - code - graphify/tests/test_cargo_introspect.py
- [[test_cargo_introspect_old_manifest_keeps_internal_path_dep_and_skips_external()]] - code - graphify/tests/test_cargo_introspect.py
- [[test_cargo_introspect_package_rename_falls_through_when_unresolved()]] - code - graphify/tests/test_cargo_introspect.py
- [[test_cargo_introspect_workspace_internal_dependency_only()]] - code - graphify/tests/test_cargo_introspect.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_111
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Community 12]]

## Top bridge nodes
- [[introspect_cargo()]] - degree 17, connects to 1 community