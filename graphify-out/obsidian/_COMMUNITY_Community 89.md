---
type: community
cohesion: 0.07
members: 31
---

# Community 89

**Cohesion:** 0.07 - loosely connected
**Members:** 31 nodes

## Members
- [[Build Bedrock inferenceConfig, honouring GRAPHIFY_LLM_TEMPERATURE.      Bedroc]] - rationale - graphify/graphify/llm.py
- [[Call Azure OpenAI Service via the AzureOpenAI SDK client.]] - rationale - graphify/graphify/llm.py
- [[Construct an AzureOpenAI client with env-driven api_version and timeout.]] - rationale - graphify/graphify/llm.py
- [[Default retry count is generous (so 429s are absorbed, 1523); env overrides.]] - rationale - graphify/tests/test_llm_backends.py
- [[How many times the provider SDK retries a transient error (notably HTTP 429]] - rationale - graphify/graphify/llm.py
- [[Opt-in (GRAPHIFY_DISABLE_THINKING) to send ``{thinking {type disabled}}`]] - rationale - graphify/graphify/llm.py
- [[Package-missing message that works for the recommended `uv tool` install.]] - rationale - graphify/graphify/llm.py
- [[Parse the JSON returned by `claude -p --output-format json`.      Older Claude]] - rationale - graphify/graphify/llm.py
- [[Same 1442 fix for the OpenAI-compatible branch of _call_llm.]] - rationale - graphify/tests/test_llm_backends.py
- [[Send a plain-text prompt to `backend` and return the model's text reply.]] - rationale - graphify/graphify/llm.py
- [[The claude backend must be installable via an extra, and the missing-package me]] - rationale - graphify/tests/test_backend_extras.py
- [[The label_simple_completion path must spawn the resolved claude.cmd on     Win]] - rationale - graphify/tests/test_claude_cli_backend.py
- [[The secondary dispatch path (_call_llm, used by the dedup tiebreaker)     must]] - rationale - graphify/tests/test_llm_backends.py
- [[_azure_client()]] - code - graphify/graphify/llm.py
- [[_backend_pkg_hint()]] - code - graphify/graphify/llm.py
- [[_bedrock_inference_config()]] - code - graphify/graphify/llm.py
- [[_call_azure()]] - code - graphify/graphify/llm.py
- [[_call_llm()]] - code - graphify/graphify/llm.py
- [[_claude_cli_envelope()]] - code - graphify/graphify/llm.py
- [[_extras()]] - code - graphify/tests/test_backend_extras.py
- [[_resolve_max_retries()]] - code - graphify/graphify/llm.py
- [[_thinking_disabled_via_env()]] - code - graphify/graphify/llm.py
- [[test_anthropic_extra_exists()]] - code - graphify/tests/test_backend_extras.py
- [[test_anthropic_in_all_extra()]] - code - graphify/tests/test_backend_extras.py
- [[test_backend_extras.py]] - code - graphify/tests/test_backend_extras.py
- [[test_backend_pkg_hint_points_at_uv_tool_and_extra()]] - code - graphify/tests/test_backend_extras.py
- [[test_call_llm_claude_cli_branch_honours_timeout()]] - code - graphify/tests/test_claude_cli_backend.py
- [[test_call_llm_claude_client_built_with_timeout_and_retries()]] - code - graphify/tests/test_llm_backends.py
- [[test_call_llm_openai_compat_client_built_with_timeout_and_retries()]] - code - graphify/tests/test_llm_backends.py
- [[test_resolve_max_retries_default_and_env()]] - code - graphify/tests/test_llm_backends.py
- [[test_simple_completion_resolves_cmd_shim_on_windows()]] - code - graphify/tests/test_claude_cli_backend.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_89
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Community 16]]
- 10 edges to [[_COMMUNITY_Community 58]]
- 5 edges to [[_COMMUNITY_Community 33]]
- 3 edges to [[_COMMUNITY_Community 38]]
- 3 edges to [[_COMMUNITY_Community 39]]
- 2 edges to [[_COMMUNITY_Community 87]]
- 1 edge to [[_COMMUNITY_Community 20]]
- 1 edge to [[_COMMUNITY_Community 78]]
- 1 edge to [[_COMMUNITY_Community 12]]
- 1 edge to [[_COMMUNITY_Community 117]]

## Top bridge nodes
- [[_call_llm()]] - degree 23, connects to 7 communities
- [[_call_azure()]] - degree 8, connects to 5 communities
- [[_backend_pkg_hint()]] - degree 7, connects to 3 communities
- [[_resolve_max_retries()]] - degree 7, connects to 3 communities
- [[_bedrock_inference_config()]] - degree 5, connects to 3 communities