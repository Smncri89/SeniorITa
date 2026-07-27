---
type: community
cohesion: 0.05
members: 60
---

# Community 25

**Cohesion:** 0.05 - loosely connected
**Members:** 60 nodes

## Members
- [[1236 follow-up the fix landed in to_obsidian but not to_canvas, so     `graph]] - rationale - graphify/tests/test_obsidian_dangling_member.py
- [[1452 a community's node cards are laid out in the same ceil(sqrt(n))-column]] - rationale - graphify/tests/test_export.py
- [[1506 exporting into an existing vault must not overwrite a user's note that]] - rationale - graphify/tests/test_export.py
- [[1896 follow-on a node that disappears and later returns must be writable]] - rationale - graphify/tests/test_export.py
- [[1896 re-exporting into the same vault must delete graphify's own notes for]] - rationale - graphify/tests/test_export.py
- [[A community whose members are all dangling should still not crash.]] - rationale - graphify/tests/test_obsidian_dangling_member.py
- [[A re-run overwrites graphify's own prior notes (via the manifest) but leaves a]] - rationale - graphify/tests/test_export.py
- [[Cap a filename stem to ``limit`` UTF-8 bytes so it stays under the 255-byte]] - rationale - graphify/graphify/export.py
- [[Escape a string for safe embedding in a Cypher single-quoted literal.      Han]] - rationale - graphify/graphify/export.py
- [[Escape a value for safe embedding in a YAML double-quoted scalar (F-009).]] - rationale - graphify/graphify/export.py
- [[Export graph as an Obsidian Canvas file - communities as groups, nodes as cards.]] - rationale - graphify/graphify/export.py
- [[Export graph as an Obsidian vault - one .md file per node with wikilinks,]] - rationale - graphify/graphify/export.py
- [[Map each node_id to a unique note filename, appending a numeric suffix on     c]] - rationale - graphify/graphify/export.py
- [[No regression a freshempty dir still gets every note + .obsidiangraph.json.]] - rationale - graphify/tests/test_export.py
- [[Node count of an existing graph.json.      Returns       - an ``int`` node c]] - rationale - graphify/graphify/export.py
- [[Path_9]] - code
- [[Regression test for issue 1236 to_obsidian must not crash with KeyError when]] - rationale - graphify/tests/test_obsidian_dangling_member.py
- [[Regression tests for issue 1094 to_obsidian  to_canvas must cap filenames to]] - rationale - graphify/tests/test_obsidian_filename_cap.py
- [[Remove edges whose source or target node is not in the node set.      Returns]] - rationale - graphify/graphify/export.py
- [[Sanitise a value used in identifier position (node label  rel type).      Cyp]] - rationale - graphify/graphify/export.py
- [[Sanitize a community name for use as an Obsidian tag.      Obsidian tags only]] - rationale - graphify/graphify/export.py
- [[The CLI calls to_obsidian and to_canvas separately with no shared map, so     t]] - rationale - graphify/tests/test_export.py
- [[Two community labels differing only by case must each get their own     `_COMMU]] - rationale - graphify/tests/test_export.py
- [[Two real nodes plus a community that references a third, non-existent id.]] - rationale - graphify/tests/test_obsidian_dangling_member.py
- [[_cap_filename()]] - code - graphify/graphify/export.py
- [[_cypher_escape()]] - code - graphify/graphify/export.py
- [[_cypher_label()]] - code - graphify/graphify/export.py
- [[_dedup_node_filenames()]] - code - graphify/graphify/export.py
- [[_four_node_two_community_graph()]] - code - graphify/tests/test_export.py
- [[_graph()_1]] - code - graphify/tests/test_obsidian_filename_cap.py
- [[_graph_with_dangling_member()]] - code - graphify/tests/test_obsidian_dangling_member.py
- [[_max_name_bytes()]] - code - graphify/tests/test_obsidian_filename_cap.py
- [[_obsidian_tag()]] - code - graphify/graphify/export.py
- [[_strip_diacritics()]] - code - graphify/graphify/export.py
- [[_two_node_graph()]] - code - graphify/tests/test_export.py
- [[_yaml_str()]] - code - graphify/graphify/export.py
- [[existing_graph_node_count()]] - code - graphify/graphify/export.py
- [[export.py]] - code - graphify/graphify/export.py
- [[prune_dangling_edges()]] - code - graphify/graphify/export.py
- [[test_canvas_dangling_community_member_does_not_crash()]] - code - graphify/tests/test_obsidian_dangling_member.py
- [[test_canvas_long_label_file_ref_capped()]] - code - graphify/tests/test_obsidian_filename_cap.py
- [[test_existing_graph_node_count()]] - code - graphify/tests/test_export.py
- [[test_obsidian_canvas_filenames_agree()]] - code - graphify/tests/test_export.py
- [[test_obsidian_community_of_only_dangling_members()]] - code - graphify/tests/test_obsidian_dangling_member.py
- [[test_obsidian_dangling_community_member_does_not_crash()]] - code - graphify/tests/test_obsidian_dangling_member.py
- [[test_obsidian_dangling_member.py]] - code - graphify/tests/test_obsidian_dangling_member.py
- [[test_obsidian_distinct_long_labels_sharing_prefix_do_not_collide()]] - code - graphify/tests/test_obsidian_filename_cap.py
- [[test_obsidian_filename_cap.py]] - code - graphify/tests/test_obsidian_filename_cap.py
- [[test_obsidian_long_ascii_label_does_not_crash()]] - code - graphify/tests/test_obsidian_filename_cap.py
- [[test_obsidian_long_cjk_label_byte_cap()]] - code - graphify/tests/test_obsidian_filename_cap.py
- [[test_obsidian_wikilink_resolves_after_truncation()]] - code - graphify/tests/test_obsidian_filename_cap.py
- [[test_to_canvas_node_grid_matches_box_columns()]] - code - graphify/tests/test_export.py
- [[test_to_obsidian_community_notes_case_collision()]] - code - graphify/tests/test_export.py
- [[test_to_obsidian_empty_dir_writes_full_vault()]] - code - graphify/tests/test_export.py
- [[test_to_obsidian_preserves_existing_user_notes_and_obsidian_config()]] - code - graphify/tests/test_export.py
- [[test_to_obsidian_removed_node_returning_is_writable_again()]] - code - graphify/tests/test_export.py
- [[test_to_obsidian_rerun_prunes_removed_nodes()]] - code - graphify/tests/test_export.py
- [[test_to_obsidian_rerun_updates_own_notes_but_not_user_files()]] - code - graphify/tests/test_export.py
- [[to_canvas()]] - code - graphify/graphify/export.py
- [[to_obsidian()]] - code - graphify/graphify/export.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_25
SORT file.name ASC
```

## Connections to other communities
- 33 edges to [[_COMMUNITY_Community 19]]
- 11 edges to [[_COMMUNITY_Community 12]]
- 8 edges to [[_COMMUNITY_Community 77]]
- 4 edges to [[_COMMUNITY_Community 35]]
- 3 edges to [[_COMMUNITY_Community 36]]
- 3 edges to [[_COMMUNITY_Community 209]]
- 2 edges to [[_COMMUNITY_Community 18]]
- 1 edge to [[_COMMUNITY_Community 34]]
- 1 edge to [[_COMMUNITY_Community 171]]
- 1 edge to [[_COMMUNITY_Community 59]]
- 1 edge to [[_COMMUNITY_Community 166]]

## Top bridge nodes
- [[export.py]] - degree 39, connects to 11 communities
- [[to_obsidian()]] - degree 31, connects to 5 communities
- [[existing_graph_node_count()]] - degree 8, connects to 3 communities
- [[to_canvas()]] - degree 17, connects to 2 communities
- [[Path_9]] - degree 6, connects to 2 communities