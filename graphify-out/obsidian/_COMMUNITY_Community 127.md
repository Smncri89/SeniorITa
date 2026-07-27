---
type: community
cohesion: 0.10
members: 24
---

# Community 127

**Cohesion:** 0.10 - loosely connected
**Members:** 24 nodes

## Members
- [[1059 after the primary rebuild, the lock-holder must loop and drain     any p]] - rationale - graphify/tests/test_watch.py
- [[1059 the process that acquires the lock must drain .pending_changes     and p]] - rationale - graphify/tests/test_watch.py
- [[1059 when the rebuild lock is held, an incremental hook must queue     its ch]] - rationale - graphify/tests/test_watch.py
- [[Changed files under followed symlinks retain their watched lexical path.]] - rationale - graphify/tests/test_watch.py
- [[End-to-end probe of the post-commit-delete bug fix.      Build a tiny graph, d]] - rationale - graphify/tests/test_watch.py
- [[GH-858 a non-blocking caller that fails to acquire the lock must not     trunc]] - rationale - graphify/tests/test_watch.py
- [[GH-858 each acquisition truncates and rewrites the PID line rather     than ap]] - rationale - graphify/tests/test_watch.py
- [[GH-858 lock file must be unlinked once the rebuild completes so     downstream]] - rationale - graphify/tests/test_watch.py
- [[Per-repo advisory lock around a rebuild.      Yields True if acquired, False i]] - rationale - graphify/graphify/watch.py
- [[_rebuild_lock()]] - code - graphify/graphify/watch.py
- [[gh-928 .graphifyignore must be parsed exactly once at watch() startup,     not]] - rationale - graphify/tests/test_watch.py
- [[gh-928 the watch Handler must short-circuit paths matching     .graphifyignore]] - rationale - graphify/tests/test_watch.py
- [[skipif_2]] - code
- [[test_rebuild_code_drains_late_arrivals()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_incremental_rename_preserves_symlink_source_path()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_merges_pending_on_acquire()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_prunes_deleted_file_nodes()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_code_queues_on_lock_contention()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_lock_does_not_accumulate_pids_across_runs()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_lock_non_blocking_does_not_clobber_holder()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_lock_removed_after_release()]] - code - graphify/tests/test_watch.py
- [[test_rebuild_lock_writes_pid_with_newline()]] - code - graphify/tests/test_watch.py
- [[test_watch_handler_honors_graphifyignore()]] - code - graphify/tests/test_watch.py
- [[test_watch_loads_graphifyignore_once()]] - code - graphify/tests/test_watch.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_127
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_Community 7]]
- 7 edges to [[_COMMUNITY_Community 15]]

## Top bridge nodes
- [[_rebuild_lock()]] - degree 10, connects to 2 communities
- [[test_rebuild_code_queues_on_lock_contention()]] - degree 5, connects to 2 communities
- [[test_rebuild_code_incremental_rename_preserves_symlink_source_path()]] - degree 4, connects to 2 communities
- [[test_rebuild_code_merges_pending_on_acquire()]] - degree 4, connects to 2 communities
- [[test_rebuild_code_prunes_deleted_file_nodes()]] - degree 4, connects to 2 communities