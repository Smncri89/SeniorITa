---
type: community
cohesion: 0.04
members: 55
---

# Community 29

**Cohesion:** 0.04 - loosely connected
**Members:** 55 nodes

## Members
- [[A class field initialised with an arrow function (`x = () = {}`) must be     c]] - rationale - graphify/tests/test_extract.py
- [[All re_exports edges should have confidence=EXTRACTED.]] - rationale - graphify/tests/test_extract.py
- [[Barrel file must emit file-level imports_from edges to source modules.]] - rationale - graphify/tests/test_extract.py
- [[Calls inside JSX expressions like `{fmtDate(now)}` must yield call edges.]] - rationale - graphify/tests/test_extract.py
- [[Destructured CJS requires must emit symbol-level `imports` edges per binder.]] - rationale - graphify/tests/test_extract.py
- [[Dynamic import edge source should be the enclosing function, not the file.]] - rationale - graphify/tests/test_languages.py
- [[Dynamic import() calls inside functions should produce imports_from edges.]] - rationale - graphify/tests/test_languages.py
- [[Dynamic imports should have EXTRACTED confidence (they are deterministic string]] - rationale - graphify/tests/test_languages.py
- [[Dynamic template literals (with ${}) must not produce an imports_from edge.]] - rationale - graphify/tests/test_languages.py
- [[Extract classes, functions, arrow functions, and imports from a .js.ts.tsx.mt]] - rationale - graphify/graphify/extract.py
- [[Functions defined alongside a JSX-returning component must be captured.]] - rationale - graphify/tests/test_extract.py
- [[Functions without dynamic imports should not get spurious imports_from edges.]] - rationale - graphify/tests/test_languages.py
- [[Guard against the phantom-god-node class (1077) an arbitrary     `obj.x = fn`]] - rationale - graphify/tests/test_extract.py
- [[Real-world repro a TS file uses `await import('.foo')` (no extension)     to]] - rationale - graphify/tests/test_import_extension_resolution.py
- [[Regression arrow functions in lexical_declaration must still produce nodes.]] - rationale - graphify/tests/test_extract.py
- [[Static template literals (no ${}) should resolve the same as a plain string.]] - rationale - graphify/tests/test_languages.py
- [[`Foo.prototype.bar = fn` must be captured as a method owned by Foo.]] - rationale - graphify/tests/test_extract.py
- [[`const f = function(){}` (function expression, not arrow) must be captured.]] - rationale - graphify/tests/test_extract.py
- [[`const x = require('.m').y` must emit symbol edge for `y`.]] - rationale - graphify/tests/test_extract.py
- [[`const { foo } = require('.mod')` must emit imports_from to the resolved module]] - rationale - graphify/tests/test_extract.py
- [[`exports.X = fn` and `module.exports.X = fn` must produce function nodes.]] - rationale - graphify/tests/test_extract.py
- [[export functionconst in a barrel file must still create nodes.]] - rationale - graphify/tests/test_extract.py
- [[export { X } from '.mod' must emit re_exports edges for each named specifier.]] - rationale - graphify/tests/test_extract.py
- [[export { localVar } without 'from' should NOT create re_exports edges.]] - rationale - graphify/tests/test_extract.py
- [[extract_js()]] - code - graphify/graphify/extract.py
- [[re_exports edges should have context='re-export'.]] - rationale - graphify/tests/test_extract.py
- [[test_barrel_local_exports_still_extracted()]] - code - graphify/tests/test_extract.py
- [[test_barrel_reexport_confidence_extracted()]] - code - graphify/tests/test_extract.py
- [[test_barrel_reexport_context_tagged()]] - code - graphify/tests/test_extract.py
- [[test_barrel_reexport_emits_imports_from()]] - code - graphify/tests/test_extract.py
- [[test_barrel_reexport_emits_re_exports_edges()]] - code - graphify/tests/test_extract.py
- [[test_extract_js_arbitrary_member_assignment_not_captured()]] - code - graphify/tests/test_extract.py
- [[test_extract_js_arrow_function_still_extracted()]] - code - graphify/tests/test_extract.py
- [[test_extract_js_commonjs_exports_assignment()]] - code - graphify/tests/test_extract.py
- [[test_extract_js_const_function_expression()]] - code - graphify/tests/test_extract.py
- [[test_extract_js_destructured_require_imports_from()]] - code - graphify/tests/test_extract.py
- [[test_extract_js_destructured_require_named_symbols()]] - code - graphify/tests/test_extract.py
- [[test_extract_js_member_require_emits_property_symbol()]] - code - graphify/tests/test_extract.py
- [[test_extract_js_prototype_method_assignment()]] - code - graphify/tests/test_extract.py
- [[test_extract_ts_class_arrow_field()]] - code - graphify/tests/test_extract.py
- [[test_extract_tsx_finds_helpers_and_component()]] - code - graphify/tests/test_extract.py
- [[test_extract_tsx_jsx_expression_calls_resolve()]] - code - graphify/tests/test_extract.py
- [[test_pure_export_no_from_not_treated_as_reexport()]] - code - graphify/tests/test_extract.py
- [[test_ts_calls_are_extracted()]] - code - graphify/tests/test_multilang.py
- [[test_ts_dynamic_import_bare_path_resolves()]] - code - graphify/tests/test_import_extension_resolution.py
- [[test_ts_dynamic_import_confidence()]] - code - graphify/tests/test_languages.py
- [[test_ts_dynamic_import_extracts_edges()]] - code - graphify/tests/test_languages.py
- [[test_ts_dynamic_import_no_error()]] - code - graphify/tests/test_languages.py
- [[test_ts_dynamic_import_source_is_function()]] - code - graphify/tests/test_languages.py
- [[test_ts_dynamic_template_literal_skipped()]] - code - graphify/tests/test_languages.py
- [[test_ts_no_dangling_edges()]] - code - graphify/tests/test_multilang.py
- [[test_ts_no_dynamic_import_in_sync_fn()]] - code - graphify/tests/test_languages.py
- [[test_ts_static_template_literal_resolved()]] - code - graphify/tests/test_languages.py
- [[test_ts_this_field_receiver_not_same_file_collision()]] - code - graphify/tests/test_languages.py
- [[this.db.query() should NOT match an unrelated query() in the same file (1316).]] - rationale - graphify/tests/test_languages.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_29
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_Community 0]]
- 16 edges to [[_COMMUNITY_Community 14]]
- 9 edges to [[_COMMUNITY_Community 9]]
- 9 edges to [[_COMMUNITY_Community 26]]
- 6 edges to [[_COMMUNITY_Community 45]]
- 3 edges to [[_COMMUNITY_Community 5]]
- 2 edges to [[_COMMUNITY_Community 244]]
- 2 edges to [[_COMMUNITY_Community 23]]
- 2 edges to [[_COMMUNITY_Community 234]]
- 1 edge to [[_COMMUNITY_Community 3]]
- 1 edge to [[_COMMUNITY_Community 32]]
- 1 edge to [[_COMMUNITY_Community 2]]
- 1 edge to [[_COMMUNITY_Community 18]]
- 1 edge to [[_COMMUNITY_Community 179]]
- 1 edge to [[_COMMUNITY_Community 97]]

## Top bridge nodes
- [[extract_js()]] - degree 72, connects to 15 communities
- [[test_extract_js_destructured_require_named_symbols()]] - degree 4, connects to 2 communities
- [[test_extract_js_member_require_emits_property_symbol()]] - degree 4, connects to 2 communities
- [[test_ts_dynamic_import_bare_path_resolves()]] - degree 4, connects to 1 community
- [[test_barrel_local_exports_still_extracted()]] - degree 3, connects to 1 community