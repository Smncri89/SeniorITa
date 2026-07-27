---
type: community
cohesion: 0.05
members: 50
---

# Community 42

**Cohesion:** 0.05 - loosely connected
**Members:** 50 nodes

## Members
- [[graphify skill must mention graphify query (query-first policy)._1]] - rationale - graphify/tests/test_devin.py
- [[Devin skill frontmatter must list triggers for model-invocable activation.]] - rationale - graphify/tests/test_devin.py
- [[Devin skill must use inline python -c syntax (cross-platform, no bash heredocs).]] - rationale - graphify/tests/test_devin.py
- [[Installed skill file must include Devin-specific YAML frontmatter.]] - rationale - graphify/tests/test_devin.py
- [[Installing rules twice does not change content and prints 'no change'.]] - rationale - graphify/tests/test_devin.py
- [[Project-scope destination must be project.devinskillsgraphifySKILL.md.]] - rationale - graphify/tests/test_devin.py
- [[Project-scope install copies skill to .devinskillsgraphifySKILL.md.]] - rationale - graphify/tests/test_devin.py
- [[Project-scope install prints a git add hint covering .devin and .windsurf.]] - rationale - graphify/tests/test_devin.py
- [[Project-scope install writes .windsurfrulesgraphify.md.]] - rationale - graphify/tests/test_devin.py
- [[Project-scope uninstall must not remove the user-scope skill file.]] - rationale - graphify/tests/test_devin.py
- [[Project-scope uninstall removes .devinskillsgraphifySKILL.md.]] - rationale - graphify/tests/test_devin.py
- [[Project-scope uninstall removes .windsurfrulesgraphify.md.]] - rationale - graphify/tests/test_devin.py
- [[Tests for graphify devin install  uninstall commands.]] - rationale - graphify/tests/test_devin.py
- [[The rules file installed by devin must use query-first policy.]] - rationale - graphify/tests/test_devin.py
- [[User-scope destination must be ~.configdevinskillsgraphifySKILL.md.]] - rationale - graphify/tests/test_devin.py
- [[User-scope install copies skill to ~.configdevinskillsgraphifySKILL.md.]] - rationale - graphify/tests/test_devin.py
- [[User-scope install does NOT write .windsurfrules — that's project-only.]] - rationale - graphify/tests/test_devin.py
- [[User-scope uninstall prints an appropriate message when nothing is installed.]] - rationale - graphify/tests/test_devin.py
- [[User-scope uninstall removes the skill file.]] - rationale - graphify/tests/test_devin.py
- [[_devin_install_user()]] - code - graphify/tests/test_devin.py
- [[_devin_rules_uninstall does nothing if the rules file was never written.]] - rationale - graphify/tests/test_devin.py
- [[_rules_path()]] - code - graphify/tests/test_devin.py
- [[_skill_path_project()_1]] - code - graphify/tests/test_devin.py
- [[_skill_path_user()_1]] - code - graphify/tests/test_devin.py
- [[`graphify --help` must list devin in the platform list and in the per-platform s]] - rationale - graphify/tests/test_devin.py
- [[devin must be registered in _PLATFORM_CONFIG.]] - rationale - graphify/tests/test_devin.py
- [[skill-devin.md must be present in the installed package.]] - rationale - graphify/tests/test_devin.py
- [[test_devin.py]] - code - graphify/tests/test_devin.py
- [[test_devin_in_main_help_text()]] - code - graphify/tests/test_devin.py
- [[test_devin_in_platform_config()]] - code - graphify/tests/test_devin.py
- [[test_devin_install_project_creates_rules_file()]] - code - graphify/tests/test_devin.py
- [[test_devin_install_project_creates_skill_file()]] - code - graphify/tests/test_devin.py
- [[test_devin_install_project_hints_git_add()]] - code - graphify/tests/test_devin.py
- [[test_devin_install_user_creates_skill_file()]] - code - graphify/tests/test_devin.py
- [[test_devin_install_user_does_not_write_rules()]] - code - graphify/tests/test_devin.py
- [[test_devin_platform_skill_destination_project_scope()]] - code - graphify/tests/test_devin.py
- [[test_devin_platform_skill_destination_user_scope()]] - code - graphify/tests/test_devin.py
- [[test_devin_rules_content_recommends_graphify_query()]] - code - graphify/tests/test_devin.py
- [[test_devin_rules_install_idempotent()]] - code - graphify/tests/test_devin.py
- [[test_devin_rules_uninstall_noop_when_not_installed()]] - code - graphify/tests/test_devin.py
- [[test_devin_skill_file_contains_frontmatter()]] - code - graphify/tests/test_devin.py
- [[test_devin_skill_file_exists_in_package()]] - code - graphify/tests/test_devin.py
- [[test_devin_skill_file_frontmatter_has_triggers()]] - code - graphify/tests/test_devin.py
- [[test_devin_skill_file_references_graphify_query()]] - code - graphify/tests/test_devin.py
- [[test_devin_skill_file_uses_python_c_syntax()]] - code - graphify/tests/test_devin.py
- [[test_devin_uninstall_project_does_not_touch_user_scope()]] - code - graphify/tests/test_devin.py
- [[test_devin_uninstall_project_removes_rules_file()]] - code - graphify/tests/test_devin.py
- [[test_devin_uninstall_project_removes_skill_file()]] - code - graphify/tests/test_devin.py
- [[test_devin_uninstall_user_noop_when_not_installed()]] - code - graphify/tests/test_devin.py
- [[test_devin_uninstall_user_removes_skill_file()]] - code - graphify/tests/test_devin.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_42
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Community 47]]
- 6 edges to [[_COMMUNITY_Community 4]]

## Top bridge nodes
- [[test_devin.py]] - degree 28, connects to 1 community
- [[test_devin_install_project_creates_skill_file()]] - degree 5, connects to 1 community
- [[test_devin_uninstall_user_removes_skill_file()]] - degree 5, connects to 1 community
- [[test_devin_install_project_creates_rules_file()]] - degree 4, connects to 1 community
- [[test_devin_rules_content_recommends_graphify_query()]] - degree 4, connects to 1 community