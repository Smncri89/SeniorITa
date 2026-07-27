---
type: community
cohesion: 0.07
members: 51
---

# Community 37

**Cohesion:** 0.07 - loosely connected
**Members:** 51 nodes

## Members
- [[1746 information_schema.referential_constraints only shows constraints     wh]] - rationale - graphify/tests/test_pg_introspect.py
- [[1854 FK edges must survive routines whose reconstructed DDL the SQL     gramm]] - rationale - graphify/tests/test_pg_introspect.py
- [[A 2-column composite FK must produce exactly ONE references edge, not two.]] - rationale - graphify/tests/test_pg_introspect.py
- [[A psycopg.OperationalError must be re-raised as ConnectionError with a     sani]] - rationale - graphify/tests/test_pg_introspect.py
- [[Assert that the virtual path in postgresql introspection output uses forward sla]] - rationale - graphify/tests/test_pg_introspect.py
- [[Baseline tables, views, routines, and a single-column FK all survive.]] - rationale - graphify/tests/test_pg_introspect.py
- [[Connect to PostgreSQL, reconstruct DDL, and extract via extract_sql().]] - rationale - graphify/graphify/pg_introspect.py
- [[Double-quote a PostgreSQL identifier, escaping embedded double-quotes.]] - rationale - graphify/graphify/pg_introspect.py
- [[If psycopg is missing, introspect_postgres raises ImportError.]] - rationale - graphify/tests/test_pg_introspect.py
- [[Merge multiple extraction results into one graph.]] - rationale - graphify/worked/mixed-corpus/raw/build.py
- [[Raise ValueError with all errors if extraction is invalid.]] - rationale - graphify/graphify/validate.py
- [[Reserved-word and special-character table names must survive DDL round-trip.]] - rationale - graphify/tests/test_pg_introspect.py
- [[Return a mock psycopg module wired to the provided catalog data.      ``routin]] - rationale - graphify/tests/test_pg_introspect.py
- [[Return the label form that tree-sitter produces for a quoted identifier.]] - rationale - graphify/tests/test_pg_introspect.py
- [[Validate an extraction JSON dict against the graphify schema.     Returns a lis]] - rationale - graphify/graphify/validate.py
- [[_make_mock_psycopg()]] - code - graphify/tests/test_pg_introspect.py
- [[_q()]] - code - graphify/tests/test_pg_introspect.py
- [[_quote_ident()]] - code - graphify/graphify/pg_introspect.py
- [[assert_valid()]] - code - graphify/graphify/validate.py
- [[build()_2]] - code - graphify/worked/mixed-corpus/raw/build.py
- [[build_from_json()_1]] - code - graphify/worked/mixed-corpus/raw/build.py
- [[introspect_postgres()]] - code - graphify/graphify/pg_introspect.py
- [[pg_introspect.py]] - code - graphify/graphify/pg_introspect.py
- [[rawbuild.py]] - code - graphify/worked/mixed-corpus/raw/build.py
- [[test_assert_valid_passes_silently()]] - code - graphify/tests/test_validate.py
- [[test_assert_valid_raises_on_errors()]] - code - graphify/tests/test_validate.py
- [[test_dangling_edge_source()]] - code - graphify/tests/test_validate.py
- [[test_dangling_edge_target()]] - code - graphify/tests/test_validate.py
- [[test_invalid_confidence()]] - code - graphify/tests/test_validate.py
- [[test_invalid_file_type()]] - code - graphify/tests/test_validate.py
- [[test_legacy_aliases_valid_after_build_canonicalization()]] - code - graphify/tests/test_validate.py
- [[test_missing_edges_key()]] - code - graphify/tests/test_validate.py
- [[test_missing_node_field()]] - code - graphify/tests/test_validate.py
- [[test_missing_nodes_key()]] - code - graphify/tests/test_validate.py
- [[test_non_hashable_edge_endpoint_reported_not_raised()]] - code - graphify/tests/test_validate.py
- [[test_non_hashable_node_id_does_not_mask_valid_ids()]] - code - graphify/tests/test_validate.py
- [[test_non_hashable_node_id_reported_not_raised()]] - code - graphify/tests/test_validate.py
- [[test_not_a_dict()]] - code - graphify/tests/test_validate.py
- [[test_pg_introspect.py]] - code - graphify/tests/test_pg_introspect.py
- [[test_pg_introspect_composite_fk()]] - code - graphify/tests/test_pg_introspect.py
- [[test_pg_introspect_connection_error()]] - code - graphify/tests/test_pg_introspect.py
- [[test_pg_introspect_fk_edges_survive_unparseable_function_stubs()]] - code - graphify/tests/test_pg_introspect.py
- [[test_pg_introspect_fk_query_avoids_privilege_filtered_view()]] - code - graphify/tests/test_pg_introspect.py
- [[test_pg_introspect_import_error()]] - code - graphify/tests/test_pg_introspect.py
- [[test_pg_introspect_quoted_identifiers()]] - code - graphify/tests/test_pg_introspect.py
- [[test_pg_introspect_success()]] - code - graphify/tests/test_pg_introspect.py
- [[test_pg_introspect_uri_forward_slashes()]] - code - graphify/tests/test_pg_introspect.py
- [[test_valid_passes()]] - code - graphify/tests/test_validate.py
- [[test_validate.py]] - code - graphify/tests/test_validate.py
- [[validate.py]] - code - graphify/graphify/validate.py
- [[validate_extraction()]] - code - graphify/graphify/validate.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_37
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 35]]
- 2 edges to [[_COMMUNITY_Community 34]]
- 2 edges to [[_COMMUNITY_Community 12]]
- 2 edges to [[_COMMUNITY_Community 143]]
- 1 edge to [[_COMMUNITY_Community 3]]
- 1 edge to [[_COMMUNITY_Community 5]]
- 1 edge to [[_COMMUNITY_Community 18]]
- 1 edge to [[_COMMUNITY_Community 74]]
- 1 edge to [[_COMMUNITY_Community 61]]
- 1 edge to [[_COMMUNITY_Community 101]]

## Top bridge nodes
- [[validate_extraction()]] - degree 31, connects to 6 communities
- [[introspect_postgres()]] - degree 15, connects to 2 communities
- [[test_validate.py]] - degree 19, connects to 1 community
- [[validate.py]] - degree 5, connects to 1 community
- [[pg_introspect.py]] - degree 4, connects to 1 community