---
type: community
cohesion: 0.08
members: 50
---

# Community 38

**Cohesion:** 0.08 - loosely connected
**Members:** 50 nodes

## Members
- [[.b64()]] - code - graphify/graphify/llm.py
- [[.bedrock_format()]] - code - graphify/graphify/llm.py
- [[A corpus with one raster image, one svg (text), and one markdown doc.]] - rationale - graphify/tests/test_image_vision.py
- [[A single image destined for a vision request.      `raw` is None when the imag]] - rationale - graphify/graphify/llm.py
- [[Build `_ImageRef`s for raster images.      `read_bytes=True` (base64 backends)]] - rationale - graphify/graphify/llm.py
- [[Build the Anthropic `messages.content` value (str, or block list with images).]] - rationale - graphify/graphify/llm.py
- [[Build the Bedrock Converse user content list (raw bytes, not base64).]] - rationale - graphify/graphify/llm.py
- [[Build the OpenAI-compatible user `content` value (str, or part list with images)]] - rationale - graphify/graphify/llm.py
- [[Call AWS Bedrock via boto3 Converse API using the standard AWS credential chain.]] - rationale - graphify/graphify/llm.py
- [[Call Anthropic Claude directly (not via OpenAI compat layer).]] - rationale - graphify/graphify/llm.py
- [[Return refs with pixel data dropped (for non-vision backends).]] - rationale - graphify/graphify/llm.py
- [[Tests for image-vision support across the direct extraction backends.  Covers]] - rationale - graphify/tests/test_image_vision.py
- [[Text block listing the images so the model emits one node per image.      Alwa]] - rationale - graphify/graphify/llm.py
- [[_ImageRef]] - code - graphify/graphify/llm.py
- [[_anthropic_content()]] - code - graphify/graphify/llm.py
- [[_bedrock_content()]] - code - graphify/graphify/llm.py
- [[_build_image_refs()]] - code - graphify/graphify/llm.py
- [[_call_bedrock()]] - code - graphify/graphify/llm.py
- [[_call_claude()]] - code - graphify/graphify/llm.py
- [[_fake_anthropic()]] - code - graphify/tests/test_image_vision.py
- [[_fake_boto3()]] - code - graphify/tests/test_image_vision.py
- [[_fake_openai()]] - code - graphify/tests/test_image_vision.py
- [[_image_notes()]] - code - graphify/graphify/llm.py
- [[_make_corpus()_2]] - code - graphify/tests/test_image_vision.py
- [[_openai_content()]] - code - graphify/graphify/llm.py
- [[_strip_pixels()]] - code - graphify/graphify/llm.py
- [[_with_image_notes()]] - code - graphify/graphify/llm.py
- [[test_anthropic_content_has_base64_block()]] - code - graphify/tests/test_image_vision.py
- [[test_bedrock_content_uses_raw_bytes()]] - code - graphify/tests/test_image_vision.py
- [[test_build_image_refs_drops_oversized()]] - code - graphify/tests/test_image_vision.py
- [[test_build_image_refs_sets_rel_media_and_bytes()]] - code - graphify/tests/test_image_vision.py
- [[test_build_image_refs_skips_out_of_root_symlink()]] - code - graphify/tests/test_image_vision.py
- [[test_builders_fall_back_to_string_without_pixels()]] - code - graphify/tests/test_image_vision.py
- [[test_call_bedrock_sends_raw_image_bytes()]] - code - graphify/tests/test_image_vision.py
- [[test_call_claude_sends_image_block()]] - code - graphify/tests/test_image_vision.py
- [[test_call_openai_compat_sends_image_url()]] - code - graphify/tests/test_image_vision.py
- [[test_call_openai_compat_text_only_without_images()]] - code - graphify/tests/test_image_vision.py
- [[test_chunk_packing_caps_images_per_chunk()]] - code - graphify/tests/test_image_vision.py
- [[test_claude_cli_adds_dir_and_read_instruction()]] - code - graphify/tests/test_image_vision.py
- [[test_claude_cli_passes_oversized_image_by_path()]] - code - graphify/tests/test_image_vision.py
- [[test_extract_files_direct_gates_pixels_by_capability()]] - code - graphify/tests/test_image_vision.py
- [[test_image_vision.py]] - code - graphify/tests/test_image_vision.py
- [[test_no_images_is_byte_identical()]] - code - graphify/tests/test_image_vision.py
- [[test_non_pdf_still_read_as_plain_text()]] - code - graphify/tests/test_image_vision.py
- [[test_openai_content_has_data_uri()]] - code - graphify/tests/test_image_vision.py
- [[test_partition_splits_raster_from_text()]] - code - graphify/tests/test_image_vision.py
- [[test_path_backend_skips_byte_read_and_size_cap()]] - code - graphify/tests/test_image_vision.py
- [[test_pdf_is_not_treated_as_vision_image()]] - code - graphify/tests/test_image_vision.py
- [[test_pdf_routed_through_pypdf_not_readtext()]] - code - graphify/tests/test_image_vision.py
- [[test_read_files_skips_out_of_root_symlink()]] - code - graphify/tests/test_image_vision.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_38
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_Community 58]]
- 6 edges to [[_COMMUNITY_Community 16]]
- 6 edges to [[_COMMUNITY_Community 39]]
- 5 edges to [[_COMMUNITY_Community 33]]
- 5 edges to [[_COMMUNITY_Community 20]]
- 3 edges to [[_COMMUNITY_Community 89]]
- 2 edges to [[_COMMUNITY_Community 78]]
- 1 edge to [[_COMMUNITY_Community 301]]
- 1 edge to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 72]]

## Top bridge nodes
- [[_call_claude()]] - degree 12, connects to 7 communities
- [[_call_bedrock()]] - degree 10, connects to 6 communities
- [[test_image_vision.py]] - degree 31, connects to 4 communities
- [[_ImageRef]] - degree 16, connects to 4 communities
- [[_build_image_refs()]] - degree 19, connects to 2 communities