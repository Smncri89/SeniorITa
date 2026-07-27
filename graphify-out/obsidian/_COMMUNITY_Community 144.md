---
type: community
cohesion: 0.11
members: 21
---

# Community 144

**Cohesion:** 0.11 - loosely connected
**Members:** 21 nodes

## Members
- [[DiGraph_2]] - code
- [[FooBarService at 1000 vs error nodes at 1.0 → only 1 seed chosen.]] - rationale - graphify/tests/test_serve.py
- [[Gbest_seed_by_term are optional and default to None existing callers     see]] - rationale - graphify/tests/test_serve.py
- [[Many nodes sharing one generic label (e.g. framework `GET` handlers)     must c]] - rationale - graphify/tests/test_serve.py
- [[Never return more than max_k seeds even when all scores are close.]] - rationale - graphify/tests/test_serve.py
- [[Reproduces 1445 a vague natural-language query where one term's     incidenta]] - rationale - graphify/tests/test_serve.py
- [[Select BFS seed nodes, stopping when score drops too far below the top.      P]] - rationale - graphify/graphify/serve.py
- [[The per-term guarantee loop must honor the same per-label cap, so it can't]] - rationale - graphify/tests/test_serve.py
- [[When all scores are within 20% of the top, keep up to 3 seeds.]] - rationale - graphify/tests/test_serve.py
- [[_pick_seeds()]] - code - graphify/graphify/serve.py
- [[`GET``Get``get` are the same generic label and must dedup together.]] - rationale - graphify/tests/test_serve.py
- [[test_pick_seeds_close_scores_keeps_multiple()]] - code - graphify/tests/test_serve.py
- [[test_pick_seeds_dedup_key_is_case_and_diacritic_normalized()]] - code - graphify/tests/test_serve.py
- [[test_pick_seeds_dedups_homonymous_generic_labels()]] - code - graphify/tests/test_serve.py
- [[test_pick_seeds_diversity_recovers_starved_term()]] - code - graphify/tests/test_serve.py
- [[test_pick_seeds_dominant_identifier_gives_one_seed()]] - code - graphify/tests/test_serve.py
- [[test_pick_seeds_empty()]] - code - graphify/tests/test_serve.py
- [[test_pick_seeds_per_term_guarantee_does_not_reintroduce_generic_dupe()]] - code - graphify/tests/test_serve.py
- [[test_pick_seeds_respects_max_k()]] - code - graphify/tests/test_serve.py
- [[test_pick_seeds_single()]] - code - graphify/tests/test_serve.py
- [[test_pick_seeds_without_diversity_args_is_unchanged()]] - code - graphify/tests/test_serve.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_144
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_Community 41]]
- 4 edges to [[_COMMUNITY_Community 62]]
- 3 edges to [[_COMMUNITY_Community 98]]
- 3 edges to [[_COMMUNITY_Community 156]]
- 1 edge to [[_COMMUNITY_Community 67]]

## Top bridge nodes
- [[_pick_seeds()]] - degree 20, connects to 5 communities
- [[DiGraph_2]] - degree 8, connects to 2 communities
- [[test_pick_seeds_diversity_recovers_starved_term()]] - degree 5, connects to 2 communities
- [[test_pick_seeds_per_term_guarantee_does_not_reintroduce_generic_dupe()]] - degree 5, connects to 2 communities
- [[test_pick_seeds_dedup_key_is_case_and_diacritic_normalized()]] - degree 4, connects to 1 community