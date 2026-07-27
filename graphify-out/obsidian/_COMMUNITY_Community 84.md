---
type: community
cohesion: 0.12
members: 32
---

# Community 84

**Cohesion:** 0.12 - loosely connected
**Members:** 32 nodes

## Members
- [[1770 a method invoked directly on a `new X(...)` object-creation     expressi]] - rationale - graphify/tests/test_csharp_member_calls.py
- [[A caller in namespace A resolves `Svc` to A.Svc even though B.Svc also     exis]] - rationale - graphify/tests/test_csharp_member_calls.py
- [[A local `Other x` shadowing a field `Server x` makes the name's type     confli]] - rationale - graphify/tests/test_csharp_member_calls.py
- [[A method not declared on the receiver's type but inherited from a     resolvabl]] - rationale - graphify/tests/test_csharp_member_calls.py
- [[C receiver-typed member-call resolution (1609).  `recv.Method()` where `recv]] - rationale - graphify/tests/test_csharp_member_calls.py
- [[No using directive and `Svc` in two foreign namespaces genuinely     ambiguous]] - rationale - graphify/tests/test_csharp_member_calls.py
- [[The receiver's type inherits from an out-of-corpus base a method missing     o]] - rationale - graphify/tests/test_csharp_member_calls.py
- [[_calls()]] - code - graphify/tests/test_csharp_member_calls.py
- [[_find()]] - code - graphify/tests/test_csharp_member_calls.py
- [[`Svc` exists in namespaces A and B; a caller file `using A;` must bind an     `]] - rationale - graphify/tests/test_csharp_member_calls.py
- [[`this._s.Save()` types the field exactly like a bare `_s.Save()`.]] - rationale - graphify/tests/test_csharp_member_calls.py
- [[`var x = Compute();` (untypable) redeclaring a typed field poisons the     name]] - rationale - graphify/tests/test_csharp_member_calls.py
- [[test_base_receiver_resolves_to_base_class_method()]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_cross_file_receiver_resolves()]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_csharp_member_calls.py]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_field_receiver_resolves_to_declared_type_not_bare_match()]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_inherited_method_resolves_through_base_chain()]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_local_shadowing_field_of_different_type_poisons_name()]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_local_var_receiver_resolves()]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_method_absent_on_type_emits_no_edge()]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_method_chained_off_new_expression_resolves()]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_namespace_ambiguous_without_using_bails()]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_namespace_using_directive_disambiguates_receiver_type()]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_namespace_using_directive_resolves_to_other_namespace()]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_parameter_receiver_resolves()]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_same_namespace_receiver_resolves_without_using()]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_this_and_static_receivers()]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_this_field_receiver_resolves()]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_unqualified_call_still_resolves()]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_unresolved_base_poisons_inherited_member_lookup()]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_untyped_receiver_emits_no_edge()]] - code - graphify/tests/test_csharp_member_calls.py
- [[test_untyped_redeclaration_poisons_typed_field()]] - code - graphify/tests/test_csharp_member_calls.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_84
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Community 27]]
- 1 edge to [[_COMMUNITY_Community 3]]

## Top bridge nodes
- [[test_csharp_member_calls.py]] - degree 24, connects to 2 communities
- [[_calls()]] - degree 21, connects to 1 community