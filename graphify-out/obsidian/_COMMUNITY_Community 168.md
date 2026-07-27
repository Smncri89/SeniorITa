---
type: community
cohesion: 0.21
members: 18
---

# Community 168

**Cohesion:** 0.21 - loosely connected
**Members:** 18 nodes

## Members
- [[1909 must keep working an alive file excluded by ignore rules is     provably]] - rationale - graphify/tests/test_stale_prune.py
- [[2210 incremental extract's graph-layer prune must not evict ALIVE files.  _s]] - rationale - graphify/tests/test_stale_prune.py
- [[(a) NFD spelling on disk vs NFC spelling in the graph NOT stale.]] - rationale - graphify/tests/test_stale_prune.py
- [[(b) fail-closed a legacy bare-basename source_file whose file is     alive at]] - rationale - graphify/tests/test_stale_prune.py
- [[(c) a source_file with no file on disk anywhere IS pruned.]] - rationale - graphify/tests/test_stale_prune.py
- [[Fail-closed an alive in-root file missing from the corpus without     provable]] - rationale - graphify/tests/test_stale_prune.py
- [[NFC-normalize a path string.      macOS (HFS+APFS) reports filenames in NFD w]] - rationale - graphify/graphify/paths.py
- [[Source files graph.json still references but the current scan no longer     con]] - rationale - graphify/graphify/cli.py
- [[_scan()]] - code - graphify/tests/test_stale_prune.py
- [[_stale_graph_sources()]] - code - graphify/graphify/cli.py
- [[_write_graph()_8]] - code - graphify/tests/test_stale_prune.py
- [[nfc()]] - code - graphify/graphify/paths.py
- [[test_alive_but_ignored_source_is_pruned()]] - code - graphify/tests/test_stale_prune.py
- [[test_alive_unproven_exclusion_kept_with_warning()]] - code - graphify/tests/test_stale_prune.py
- [[test_bare_basename_alive_elsewhere_not_pruned()]] - code - graphify/tests/test_stale_prune.py
- [[test_genuinely_deleted_source_still_pruned()]] - code - graphify/tests/test_stale_prune.py
- [[test_nfd_disk_nfc_graph_source_not_pruned()]] - code - graphify/tests/test_stale_prune.py
- [[test_stale_prune.py]] - code - graphify/tests/test_stale_prune.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_168
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Community 12]]
- 3 edges to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 44]]
- 1 edge to [[_COMMUNITY_Community 76]]

## Top bridge nodes
- [[test_stale_prune.py]] - degree 12, connects to 3 communities
- [[_stale_graph_sources()]] - degree 12, connects to 2 communities
- [[nfc()]] - degree 4, connects to 2 communities
- [[_scan()]] - degree 7, connects to 1 community