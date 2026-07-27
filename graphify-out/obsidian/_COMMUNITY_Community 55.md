---
type: community
cohesion: 0.05
members: 43
---

# Community 55

**Cohesion:** 0.05 - loosely connected
**Members:** 43 nodes

## Members
- [[@selector(doThing) must resolve to `-doThing` exactly, not be suppressed by]] - rationale - graphify/tests/test_languages.py
- [[@selector(doThing) with two doThing methods must emit zero calls edges.]] - rationale - graphify/tests/test_languages.py
- [[@selector(uniqueMethod) with exactly one match produces a calls edge.]] - rationale - graphify/tests/test_languages.py
- [[A compound message `self ax by` resolves to the compound method def (1475).]] - rationale - graphify/tests/test_languages.py
- [[A macro-free header still parses exactly as before (regression).]] - rationale - graphify/tests/test_languages.py
- [[A substring-colliding sibling must neither be falsely matched nor suppress]] - rationale - graphify/tests/test_languages.py
- [[Accessing a property not defined in the current class produces zero accesses edg]] - rationale - graphify/tests/test_languages.py
- [[Extract interfaces, implementations, protocols, methods, and imports from .m.mm]] - rationale - graphify/graphify/extractors/objc.py
- [[Path_25]] - code
- [[Two classes each declaring -name self.name in A must NOT fan out to B's -name.]] - rationale - graphify/tests/test_languages.py
- [[`+ (…)shared` is a class method and must be labeled +shared, not -shared (1475)]] - rationale - graphify/tests/test_languages.py
- [[`@import Foundation;`  `@import UIKit.UIView;` produce imports edges (1475).]] - rationale - graphify/tests/test_languages.py
- [[`@protocol Derived Base` must emit an implements edge Derived-Base.     Prot]] - rationale - graphify/tests/test_languages.py
- [[`NSArrayProduct  ` must reference the element type Product (and the     con]] - rationale - graphify/tests/test_languages.py
- [[`NS_ASSUME_NONNULL_BEGIN` before `@interface` made tree-sitter-objc fail to]] - rationale - graphify/tests/test_languages.py
- [[`Unknown alloc init` with no such class must not produce a resolved     ref]] - rationale - graphify/tests/test_languages.py
- [[`self speak` inside Dog.fetch must produce a calls edge. The method-body]] - rationale - graphify/tests/test_languages.py
- [[extract_objc()]] - code - graphify/graphify/extractors/objc.py
- [[self.name dot-syntax resolves to an accesses edge within the same class.]] - rationale - graphify/tests/test_languages.py
- [[test_objc_alloc_init_unknown_class_no_resolved_edge()]] - code - graphify/tests/test_languages.py
- [[test_objc_class_method_labeled_with_plus()]] - code - graphify/tests/test_languages.py
- [[test_objc_compound_selector_call_resolves()]] - code - graphify/tests/test_languages.py
- [[test_objc_dot_syntax_no_fanout_two_same_named_properties()]] - code - graphify/tests/test_languages.py
- [[test_objc_dot_syntax_property_accesses_edge()]] - code - graphify/tests/test_languages.py
- [[test_objc_dot_syntax_substring_sibling_exact_match()]] - code - graphify/tests/test_languages.py
- [[test_objc_dot_syntax_unresolvable_property_zero_edges()]] - code - graphify/tests/test_languages.py
- [[test_objc_finds_imports()]] - code - graphify/tests/test_languages.py
- [[test_objc_finds_interface()]] - code - graphify/tests/test_languages.py
- [[test_objc_finds_methods()]] - code - graphify/tests/test_languages.py
- [[test_objc_finds_subclass()]] - code - graphify/tests/test_languages.py
- [[test_objc_generic_property_type_extracted()]] - code - graphify/tests/test_languages.py
- [[test_objc_inherits_edge()]] - code - graphify/tests/test_languages.py
- [[test_objc_macro_free_header_unchanged()]] - code - graphify/tests/test_languages.py
- [[test_objc_module_import_edge()]] - code - graphify/tests/test_languages.py
- [[test_objc_no_dangling_edges()]] - code - graphify/tests/test_languages.py
- [[test_objc_ns_assume_nonnull_macro_does_not_break_parsing()]] - code - graphify/tests/test_languages.py
- [[test_objc_property_type_context()]] - code - graphify/tests/test_languages.py
- [[test_objc_protocol_adopts_protocol()]] - code - graphify/tests/test_languages.py
- [[test_objc_resolves_self_method_calls()]] - code - graphify/tests/test_languages.py
- [[test_objc_selector_expression_calls_edge()]] - code - graphify/tests/test_languages.py
- [[test_objc_selector_no_fanout_two_same_named_methods()]] - code - graphify/tests/test_languages.py
- [[test_objc_selector_substring_method_exact_match()]] - code - graphify/tests/test_languages.py
- [[test_objc_splits_inherits_and_implements()]] - code - graphify/tests/test_languages.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_55
SORT file.name ASC
```

## Connections to other communities
- 25 edges to [[_COMMUNITY_Community 9]]
- 6 edges to [[_COMMUNITY_Community 50]]
- 3 edges to [[_COMMUNITY_Community 5]]
- 3 edges to [[_COMMUNITY_Community 2]]
- 2 edges to [[_COMMUNITY_Community 3]]
- 1 edge to [[_COMMUNITY_Community 32]]
- 1 edge to [[_COMMUNITY_Community 157]]

## Top bridge nodes
- [[extract_objc()]] - degree 37, connects to 6 communities
- [[test_objc_generic_property_type_extracted()]] - degree 4, connects to 2 communities
- [[test_objc_macro_free_header_unchanged()]] - degree 4, connects to 2 communities
- [[test_objc_ns_assume_nonnull_macro_does_not_break_parsing()]] - degree 4, connects to 2 communities
- [[test_objc_protocol_adopts_protocol()]] - degree 4, connects to 2 communities