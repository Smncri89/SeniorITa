---
type: community
cohesion: 0.14
members: 18
---

# Community 170

**Cohesion:** 0.14 - loosely connected
**Members:** 18 nodes

## Members
- [[A project-local ..graphifyproviders.json is NOT loaded by default (F1).]] - rationale - graphify/tests/test_provider_registry.py
- [[A provider whose base_url uses a non-http(s) scheme is skipped on load (F1).]] - rationale - graphify/tests/test_provider_registry.py
- [[Built-in provider names are protected from being overridden.]] - rationale - graphify/tests/test_provider_registry.py
- [[Custom providers appear after all built-ins in detect_backend() priority.]] - rationale - graphify/tests/test_provider_registry.py
- [[Full round-trip add → list → show → remove via providers.json.]] - rationale - graphify/tests/test_provider_registry.py
- [[Missing pricing field defaults to zero so estimate_cost doesn't blow up.]] - rationale - graphify/tests/test_provider_registry.py
- [[With explicit opt-in the project-local file is honoured (F1).]] - rationale - graphify/tests/test_provider_registry.py
- [[_load_custom_providers()]] - code - graphify/graphify/llm.py
- [[provider_base_url_ok rejects bad schemes and warns on plaintext-http egress (F1)]] - rationale - graphify/tests/test_provider_registry.py
- [[test_custom_provider_add_list_show_remove()]] - code - graphify/tests/test_provider_registry.py
- [[test_custom_provider_cannot_shadow_builtin()]] - code - graphify/tests/test_provider_registry.py
- [[test_custom_provider_pricing_defaults_to_zero()]] - code - graphify/tests/test_provider_registry.py
- [[test_detect_backend_custom_provider_after_builtins()]] - code - graphify/tests/test_provider_registry.py
- [[test_non_http_provider_base_url_rejected()]] - code - graphify/tests/test_provider_registry.py
- [[test_project_local_providers_ignored_without_optin()]] - code - graphify/tests/test_provider_registry.py
- [[test_project_local_providers_loaded_with_optin()]] - code - graphify/tests/test_provider_registry.py
- [[test_provider_base_url_ok_scheme_and_warnings()]] - code - graphify/tests/test_provider_registry.py
- [[test_provider_registry.py]] - code - graphify/tests/test_provider_registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_170
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 12]]
- 2 edges to [[_COMMUNITY_Community 58]]
- 1 edge to [[_COMMUNITY_Community 39]]

## Top bridge nodes
- [[_load_custom_providers()]] - degree 9, connects to 2 communities
- [[test_provider_registry.py]] - degree 9, connects to 1 community
- [[test_detect_backend_custom_provider_after_builtins()]] - degree 3, connects to 1 community
- [[test_provider_base_url_ok_scheme_and_warnings()]] - degree 3, connects to 1 community