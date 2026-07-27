---
type: community
cohesion: 0.20
members: 14
---

# Community 212

**Cohesion:** 0.20 - loosely connected
**Members:** 14 nodes

## Members
- [[Add keyword index and cross-references to a validated document.]] - rationale - graphify/worked/example/raw/processor.py
- [[Enrich a validated document and persist it. Returns the record ID.]] - rationale - graphify/worked/example/raw/processor.py
- [[Look up the index and return IDs of related documents by keyword overlap.]] - rationale - graphify/worked/example/raw/processor.py
- [[Lowercase, strip extra whitespace, remove control characters.]] - rationale - graphify/worked/example/raw/processor.py
- [[Processor module - transforms validated documents into enriched records ready f]] - rationale - graphify/worked/example/raw/processor.py
- [[Pull non-stopword tokens from text, deduplicated.]] - rationale - graphify/worked/example/raw/processor.py
- [[Re-enrich all records in the index. Returns count of records updated.]] - rationale - graphify/worked/example/raw/processor.py
- [[enrich_document()]] - code - graphify/worked/example/raw/processor.py
- [[extract_keywords()]] - code - graphify/worked/example/raw/processor.py
- [[find_cross_references()]] - code - graphify/worked/example/raw/processor.py
- [[normalize_text()]] - code - graphify/worked/example/raw/processor.py
- [[process_and_save()]] - code - graphify/worked/example/raw/processor.py
- [[processor.py]] - code - graphify/worked/example/raw/processor.py
- [[reprocess_all()]] - code - graphify/worked/example/raw/processor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_212
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Community 188]]
- 5 edges to [[_COMMUNITY_Community 157]]

## Top bridge nodes
- [[process_and_save()]] - degree 7, connects to 2 communities
- [[processor.py]] - degree 10, connects to 1 community
- [[enrich_document()]] - degree 6, connects to 1 community
- [[normalize_text()]] - degree 5, connects to 1 community
- [[find_cross_references()]] - degree 4, connects to 1 community