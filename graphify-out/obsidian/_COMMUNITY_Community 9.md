---
type: community
cohesion: 0.03
members: 92
---

# Community 9

**Cohesion:** 0.03 - loosely connected
**Members:** 92 nodes

## Members
- [[An ObjC `.h` (has @interface) routes to extract_objc; a plain C `.h` stays]] - rationale - graphify/tests/test_languages.py
- [[Dot-source `. .Shared.psm1` emits an imports_from edge.]] - rationale - graphify/tests/test_languages.py
- [[Dot-source `. .Utils.ps1` (backslash path) emits an imports_from edge.]] - rationale - graphify/tests/test_languages.py
- [[Dot-source inside a function body still produces an imports_from edge.]] - rationale - graphify/tests/test_languages.py
- [[Extract functions and includes from a .c.h file.]] - rationale - graphify/graphify/extract.py
- [[Extract modules, functions, imports, and calls from a .ex.exs file.]] - rationale - graphify/graphify/extractors/elixir.py
- [[Extract modules, structs, functions, imports, and calls from a .jl file.]] - rationale - graphify/graphify/extractors/julia.py
- [[If the injected field's type name is ambiguous (two classes named Database),]] - rationale - graphify/tests/test_languages.py
- [[Import-Module -Name Bar.psm1 resolves to module stem 'bar'.]] - rationale - graphify/tests/test_languages.py
- [[Import-Module Foo at top level emits an imports_from edge.]] - rationale - graphify/tests/test_languages.py
- [[Import-Module inside a function body still produces an imports_from edge.]] - rationale - graphify/tests/test_languages.py
- [[Import-Module must not appear in raw_calls (it is an import, not a function call]] - rationale - graphify/tests/test_languages.py
- [[Path_18]] - code
- [[Path_23]] - code
- [[Qualified (`using Base.Threads`) and relative (`using ..Mod`) imports     must]] - rationale - graphify/tests/test_languages.py
- [[Quoted `import X.h` edges must target the real (disambiguated) file node id,]] - rationale - graphify/tests/test_languages.py
- [[Tests for language extractors Java, C, C++, Ruby, C, Kotlin, Scala, PHP, Swift]] - rationale - graphify/tests/test_languages.py
- [[The decisive 1316 guardrail two classes each define `query`, but the     inje]] - rationale - graphify/tests/test_languages.py
- [[_edges_with_relation()]] - code - graphify/tests/test_languages.py
- [[_get_extractor should route .psd1 to extract_powershell_manifest.]] - rationale - graphify/tests/test_languages.py
- [[_node_by_label()]] - code - graphify/tests/test_languages.py
- [[_normalize_symbol_label()]] - code - graphify/tests/test_languages.py
- [[_ts_label_calls()]] - code - graphify/tests/test_languages.py
- [[`alias Foo.{Bar, Baz}` must emit one imports edge per expanded module.      Th]] - rationale - graphify/tests/test_languages.py
- [[`class Sub  Base` must emit an inherits edge.      Ruby exposes the base clas]] - rationale - graphify/tests/test_languages.py
- [[`extension Foo` in a separate file from `class Foo` must resolve to a     singl]] - rationale - graphify/tests/test_languages.py
- [[extract_c()]] - code - graphify/graphify/extract.py
- [[extract_elixir()]] - code - graphify/graphify/extractors/elixir.py
- [[extract_julia()]] - code - graphify/graphify/extractors/julia.py
- [[test_c_call_edges_have_call_context()]] - code - graphify/tests/test_languages.py
- [[test_c_calls_are_extracted()]] - code - graphify/tests/test_languages.py
- [[test_c_emits_calls()]] - code - graphify/tests/test_languages.py
- [[test_c_finds_functions()]] - code - graphify/tests/test_languages.py
- [[test_c_finds_includes()]] - code - graphify/tests/test_languages.py
- [[test_c_import_edges_have_import_context()]] - code - graphify/tests/test_languages.py
- [[test_c_no_error()]] - code - graphify/tests/test_languages.py
- [[test_c_parameter_and_return_type_contexts()]] - code - graphify/tests/test_languages.py
- [[test_cpp_import_edges_have_import_context()]] - code - graphify/tests/test_languages.py
- [[test_dmf_elem_under_window()]] - code - graphify/tests/test_languages.py
- [[test_dmf_no_dangling_edges()]] - code - graphify/tests/test_languages.py
- [[test_dmf_no_error()]] - code - graphify/tests/test_languages.py
- [[test_dmi_no_error()]] - code - graphify/tests/test_languages.py
- [[test_dmi_state_contained_by_file()]] - code - graphify/tests/test_languages.py
- [[test_elixir_call_edges_have_call_context()]] - code - graphify/tests/test_languages.py
- [[test_elixir_finds_calls()]] - code - graphify/tests/test_languages.py
- [[test_elixir_finds_functions()]] - code - graphify/tests/test_languages.py
- [[test_elixir_finds_imports()]] - code - graphify/tests/test_languages.py
- [[test_elixir_finds_module()]] - code - graphify/tests/test_languages.py
- [[test_elixir_import_edges_have_import_context()]] - code - graphify/tests/test_languages.py
- [[test_elixir_method_edges()]] - code - graphify/tests/test_languages.py
- [[test_elixir_multi_alias_expands()]] - code - graphify/tests/test_languages.py
- [[test_java_import_edges_have_import_context()]] - code - graphify/tests/test_languages.py
- [[test_julia_abstract_concrete_hierarchy_inherits()]] - code - graphify/tests/test_languages.py
- [[test_julia_call_edges_have_call_context()]] - code - graphify/tests/test_languages.py
- [[test_julia_finds_abstract_type()]] - code - graphify/tests/test_languages.py
- [[test_julia_finds_calls()]] - code - graphify/tests/test_languages.py
- [[test_julia_finds_functions()]] - code - graphify/tests/test_languages.py
- [[test_julia_finds_imports()]] - code - graphify/tests/test_languages.py
- [[test_julia_finds_inherits()]] - code - graphify/tests/test_languages.py
- [[test_julia_finds_module()]] - code - graphify/tests/test_languages.py
- [[test_julia_finds_short_function()]] - code - graphify/tests/test_languages.py
- [[test_julia_finds_structs()]] - code - graphify/tests/test_languages.py
- [[test_julia_import_edges_have_import_context()]] - code - graphify/tests/test_languages.py
- [[test_julia_no_dangling_edges()]] - code - graphify/tests/test_languages.py
- [[test_julia_qualified_and_relative_imports()]] - code - graphify/tests/test_languages.py
- [[test_julia_struct_field_type_context()]] - code - graphify/tests/test_languages.py
- [[test_languages.py]] - code - graphify/tests/test_languages.py
- [[test_metal_is_code_extension()]] - code - graphify/tests/test_languages.py
- [[test_objc_header_dispatch_routes_objc_not_c()]] - code - graphify/tests/test_languages.py
- [[test_objc_import_edges_have_import_context()]] - code - graphify/tests/test_languages.py
- [[test_objc_quoted_import_edges_resolve_to_real_nodes()]] - code - graphify/tests/test_languages.py
- [[test_php_call_edges_have_call_context()]] - code - graphify/tests/test_languages.py
- [[test_php_import_edges_have_import_context()]] - code - graphify/tests/test_languages.py
- [[test_powershell_dot_source_backslash_emits_edge()]] - code - graphify/tests/test_languages.py
- [[test_powershell_dot_source_forward_slash_emits_edge()]] - code - graphify/tests/test_languages.py
- [[test_powershell_dot_source_inside_function_emits_edge()]] - code - graphify/tests/test_languages.py
- [[test_powershell_finds_class_and_method()]] - code - graphify/tests/test_languages.py
- [[test_powershell_import_module_emits_edge()]] - code - graphify/tests/test_languages.py
- [[test_powershell_import_module_inside_function_emits_edge()]] - code - graphify/tests/test_languages.py
- [[test_powershell_import_module_not_a_raw_call()]] - code - graphify/tests/test_languages.py
- [[test_powershell_import_module_with_name_param()]] - code - graphify/tests/test_languages.py
- [[test_powershell_no_error()]] - code - graphify/tests/test_languages.py
- [[test_powershell_psd1_dispatched()]] - code - graphify/tests/test_languages.py
- [[test_ruby_inherits_edge()]] - code - graphify/tests/test_languages.py
- [[test_scala_call_edges_have_call_context()]] - code - graphify/tests/test_languages.py
- [[test_swift_call_edges_have_call_context()]] - code - graphify/tests/test_languages.py
- [[test_swift_extension_across_files_merges_into_canonical_type()]] - code - graphify/tests/test_languages.py
- [[test_swift_import_edges_have_import_context()]] - code - graphify/tests/test_languages.py
- [[test_ts_constructor_injection_calls_edge()]] - code - graphify/tests/test_languages.py
- [[test_ts_injected_field_ambiguous_type_emits_no_edge()]] - code - graphify/tests/test_languages.py
- [[test_ts_injected_field_resolves_to_typed_class_not_same_named_collision()]] - code - graphify/tests/test_languages.py
- [[this.repo.findById() in a class with constructor(private repo IUserRepository)]] - rationale - graphify/tests/test_languages.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_9
SORT file.name ASC
```

## Connections to other communities
- 59 edges to [[_COMMUNITY_Community 23]]
- 49 edges to [[_COMMUNITY_Community 50]]
- 30 edges to [[_COMMUNITY_Community 97]]
- 27 edges to [[_COMMUNITY_Community 5]]
- 25 edges to [[_COMMUNITY_Community 55]]
- 20 edges to [[_COMMUNITY_Community 140]]
- 17 edges to [[_COMMUNITY_Community 154]]
- 16 edges to [[_COMMUNITY_Community 169]]
- 15 edges to [[_COMMUNITY_Community 181]]
- 13 edges to [[_COMMUNITY_Community 137]]
- 13 edges to [[_COMMUNITY_Community 165]]
- 11 edges to [[_COMMUNITY_Community 125]]
- 9 edges to [[_COMMUNITY_Community 32]]
- 9 edges to [[_COMMUNITY_Community 29]]
- 8 edges to [[_COMMUNITY_Community 183]]
- 8 edges to [[_COMMUNITY_Community 229]]
- 6 edges to [[_COMMUNITY_Community 27]]
- 4 edges to [[_COMMUNITY_Community 3]]
- 4 edges to [[_COMMUNITY_Community 2]]
- 4 edges to [[_COMMUNITY_Community 13]]
- 3 edges to [[_COMMUNITY_Community 46]]
- 2 edges to [[_COMMUNITY_Community 26]]
- 1 edge to [[_COMMUNITY_Community 35]]
- 1 edge to [[_COMMUNITY_Community 157]]

## Top bridge nodes
- [[test_languages.py]] - degree 364, connects to 22 communities
- [[extract_julia()]] - degree 24, connects to 4 communities
- [[_edges_with_relation()]] - degree 20, connects to 3 communities
- [[extract_c()]] - degree 13, connects to 3 communities
- [[extract_elixir()]] - degree 15, connects to 2 communities