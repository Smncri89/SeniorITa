---
type: community
cohesion: 0.03
members: 87
---

# Community 11

**Cohesion:** 0.03 - loosely connected
**Members:** 87 nodes

## Members
- [[A .md file with enough paper signals should classify as PAPER.]] - rationale - graphify/tests/test_detect.py
- [[A `-S` payload that itself starts with `-S` is rejected (allow_split=False]] - rationale - graphify/tests/test_detect.py
- [[A plain .md file without paper signals should stay DOCUMENT.]] - rationale - graphify/tests/test_detect.py
- [[Classify file type via interpreter, including env -S form.]] - rationale - graphify/tests/test_detect.py
- [[Clumped `-uPYTHONPATH` form (no space between flag and operand) is one arg.]] - rationale - graphify/tests/test_detect.py
- [[Compact `-Spython3 -u` form (no space between -S and packed string).]] - rationale - graphify/tests/test_detect.py
- [[Compact `-vSpython3` (-v plus compact -S).]] - rationale - graphify/tests/test_detect.py
- [[File without shebang returns None.]] - rationale - graphify/tests/test_detect.py
- [[GNU `--chdir tmp python3` (separate operand).]] - rationale - graphify/tests/test_detect.py
- [[GNU `--chdir=tmp python3` (`=` operand form).]] - rationale - graphify/tests/test_detect.py
- [[GNU `--split-string python3 -u` (separate operand) → python3.]] - rationale - graphify/tests/test_detect.py
- [[GNU `--split-string='python3 -u'` (with `=` operand) → python3.]] - rationale - graphify/tests/test_detect.py
- [[GNU `--unset PYTHONPATH python3` (separate operand).]] - rationale - graphify/tests/test_detect.py
- [[GNU `--unset=PYTHONPATH python3` (`=` operand form).]] - rationale - graphify/tests/test_detect.py
- [[GNU `-a alias python3` skips both -a and its argv0 operand.]] - rationale - graphify/tests/test_detect.py
- [[GNU signal-handling flags skip transparently.]] - rationale - graphify/tests/test_detect.py
- [[Plain shebang returns the interpreter basename.]] - rationale - graphify/tests/test_detect.py
- [[Quoted interpreter path with spaces parses correctly via shlex.]] - rationale - graphify/tests/test_detect.py
- [[Return the interpreter name from a shebang line.      Handles forms that a nai]] - rationale - graphify/graphify/detect.py
- [[The real attention paper file should be classified as PAPER.]] - rationale - graphify/tests/test_detect.py
- [[Unknown hyphen-prefixed env option → return None rather than guessing.]] - rationale - graphify/tests/test_detect.py
- [[Unreadable  nonexistent files return None, never raise.]] - rationale - graphify/tests/test_detect.py
- [[Video and audio file extensions should classify as VIDEO.]] - rationale - graphify/tests/test_detect.py
- [[_shebang_interpreter()]] - code - graphify/graphify/detect.py
- [[`!usrbinenv -S python3 -u` (-S split-args form) recovers the interpreter.]] - rationale - graphify/tests/test_detect.py
- [[`!usrbinenv -i bash` skips env flags and resolves to the interpreter.]] - rationale - graphify/tests/test_detect.py
- [[`!usrbinenv DEBUG=1 python3` skips var=value assignments.]] - rationale - graphify/tests/test_detect.py
- [[`!usrbinenv python3` returns the interpreter, not 'env'.]] - rationale - graphify/tests/test_detect.py
- [[`--split-string=` payload may carry assignments before the interpreter.]] - rationale - graphify/tests/test_detect.py
- [[`--split-string=` payload may carry env flags before the interpreter.]] - rationale - graphify/tests/test_detect.py
- [[`-S` payload may carry NAME=value assignments before the interpreter.]] - rationale - graphify/tests/test_detect.py
- [[`-S` payload may carry env flags (e.g. -i) before the interpreter.]] - rationale - graphify/tests/test_detect.py
- [[`-vS` packed payload also re-parses for leading assignments.]] - rationale - graphify/tests/test_detect.py
- [[`env -C tmp python3` skips both -C and its workdir operand.]] - rationale - graphify/tests/test_detect.py
- [[`env -P bin python3` skips both -P and its utilpath operand.]] - rationale - graphify/tests/test_detect.py
- [[`env -i -S python3 -u` handles -S after another env flag.]] - rationale - graphify/tests/test_detect.py
- [[`env -u VAR python3` skips both -u and its required operand.]] - rationale - graphify/tests/test_detect.py
- [[`env -u` with no operand → not a valid command, return None.]] - rationale - graphify/tests/test_detect.py
- [[classify_file()]] - code - graphify/graphify/detect.py
- [[test_classify_attention_paper()]] - code - graphify/tests/test_detect.py
- [[test_classify_google_workspace_shortcuts()]] - code - graphify/tests/test_detect.py
- [[test_classify_image()]] - code - graphify/tests/test_detect.py
- [[test_classify_markdown()]] - code - graphify/tests/test_detect.py
- [[test_classify_md_doc_without_signals()]] - code - graphify/tests/test_detect.py
- [[test_classify_md_paper_by_signals()]] - code - graphify/tests/test_detect.py
- [[test_classify_pdf()]] - code - graphify/tests/test_detect.py
- [[test_classify_pdf_in_xcassets_root_skipped()]] - code - graphify/tests/test_detect.py
- [[test_classify_pdf_in_xcassets_skipped()]] - code - graphify/tests/test_detect.py
- [[test_classify_powershell_manifest()]] - code - graphify/tests/test_detect.py
- [[test_classify_powershell_module()]] - code - graphify/tests/test_detect.py
- [[test_classify_python()]] - code - graphify/tests/test_detect.py
- [[test_classify_skill()]] - code - graphify/tests/test_detect.py
- [[test_classify_typescript()]] - code - graphify/tests/test_detect.py
- [[test_classify_unknown_returns_none()]] - code - graphify/tests/test_detect.py
- [[test_classify_video_extensions()]] - code - graphify/tests/test_detect.py
- [[test_shebang_file_type_classifies_via_interpreter()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_chdir_with_operand()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_clumped_u_operand()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_compact_dash_s()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_compact_v_then_s()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_dash_s()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_dash_s_after_flag()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_dash_s_assignment_before_interpreter()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_dash_s_flag_before_interpreter()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_gnu_argv0_operand()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_gnu_split_string_equals()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_gnu_split_string_separate()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_long_chdir_equals()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_long_chdir_separate_operand()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_long_split_assignment_before_interpreter()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_long_split_flag_before_interpreter()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_long_unset_equals()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_long_unset_separate_operand()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_missing_operand_returns_none()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_nested_split_string_rejected()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_path_with_operand()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_signal_flags()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_single_arg()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_unknown_option_returns_none()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_unset_with_operand()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_vs_assignment_before_interpreter()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_with_assignment()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_env_with_flags()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_no_shebang()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_plain()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_quoted_path()]] - code - graphify/tests/test_detect.py
- [[test_shebang_interpreter_unreadable_returns_none()]] - code - graphify/tests/test_detect.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_11
SORT file.name ASC
```

## Connections to other communities
- 51 edges to [[_COMMUNITY_Community 1]]
- 8 edges to [[_COMMUNITY_Community 44]]
- 3 edges to [[_COMMUNITY_Community 82]]
- 2 edges to [[_COMMUNITY_Community 24]]
- 1 edge to [[_COMMUNITY_Community 3]]
- 1 edge to [[_COMMUNITY_Community 32]]

## Top bridge nodes
- [[_shebang_interpreter()]] - degree 39, connects to 5 communities
- [[classify_file()]] - degree 48, connects to 4 communities
- [[test_shebang_interpreter_env_chdir_with_operand()]] - degree 4, connects to 1 community
- [[test_shebang_interpreter_env_clumped_u_operand()]] - degree 4, connects to 1 community
- [[test_shebang_interpreter_env_compact_dash_s()]] - degree 4, connects to 1 community