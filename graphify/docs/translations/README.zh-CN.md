# graphify

ðŸ‡ºðŸ‡¸ [English](../../README.md) | ðŸ‡¨ðŸ‡³ [ç®€ä½“ä¸­æ–‡](README.zh-CN.md) | ðŸ‡¯ðŸ‡µ [æ—¥æœ¬èªž](README.ja-JP.md) | ðŸ‡°ðŸ‡· [í•œêµ­ì–´](README.ko-KR.md) | ðŸ‡©ðŸ‡ª [Deutsch](README.de-DE.md) | ðŸ‡«ðŸ‡· [FranÃ§ais](README.fr-FR.md) | ðŸ‡ªðŸ‡¸ [EspaÃ±ol](README.es-ES.md) | ðŸ‡®ðŸ‡³ [à¤¹à¤¿à¤¨à¥à¤¦à¥€](README.hi-IN.md) | ðŸ‡§ðŸ‡· [PortuguÃªs](README.pt-BR.md) | ðŸ‡·ðŸ‡º [Ð ÑƒÑÑÐºÐ¸Ð¹](README.ru-RU.md) | ðŸ‡¸ðŸ‡¦ [Ø§Ù„Ø¹Ø±Ø¨ÙŠØ©](README.ar-SA.md) | ðŸ‡®ðŸ‡¹ [Italiano](README.it-IT.md) | ðŸ‡µðŸ‡± [Polski](README.pl-PL.md) | ðŸ‡³ðŸ‡± [Nederlands](README.nl-NL.md) | ðŸ‡¹ðŸ‡· [TÃ¼rkÃ§e](README.tr-TR.md) | ðŸ‡ºðŸ‡¦ [Ð£ÐºÑ€Ð°Ñ—Ð½ÑÑŒÐºÐ°](README.uk-UA.md) | ðŸ‡»ðŸ‡³ [Tiáº¿ng Viá»‡t](README.vi-VN.md) | ðŸ‡®ðŸ‡© [Bahasa Indonesia](README.id-ID.md) | ðŸ‡¸ðŸ‡ª [Svenska](README.sv-SE.md) | ðŸ‡¬ðŸ‡· [Î•Î»Î»Î·Î½Î¹ÎºÎ¬](README.el-GR.md) | ðŸ‡·ðŸ‡´ [RomÃ¢nÄƒ](README.ro-RO.md) | ðŸ‡¨ðŸ‡¿ [ÄŒeÅ¡tina](README.cs-CZ.md) | ðŸ‡«ðŸ‡® [Suomi](README.fi-FI.md) | ðŸ‡©ðŸ‡° [Dansk](README.da-DK.md) | ðŸ‡³ðŸ‡´ [Norsk](README.no-NO.md) | ðŸ‡­ðŸ‡º [Magyar](README.hu-HU.md) | ðŸ‡¹ðŸ‡­ [à¸ à¸²à¸©à¸²à¹„à¸—à¸¢](README.th-TH.md) | ðŸ‡ºðŸ‡¿ [OÊ»zbekcha](README.uz-UZ.md) | ðŸ‡¹ðŸ‡¼ [ç¹é«”ä¸­æ–‡](README.zh-TW.md)

[![CI](https://github.com/safishamsi/graphify/actions/workflows/ci.yml/badge.svg?branch=v3)](https://github.com/safishamsi/graphify/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/graphifyy)](https://pypi.org/project/graphifyy/)

**ä¸€ä¸ªé¢å‘ AI ç¼–ç åŠ©æ‰‹çš„æŠ€èƒ½ã€‚** åœ¨ Claude Codeã€CodeBuddyã€Codexã€OpenCodeã€OpenClawã€Factory Droid æˆ– Trae ä¸­è¾“å…¥ `/graphify`ï¼Œå®ƒä¼šè¯»å–ä½ çš„æ–‡ä»¶ã€æž„å»ºçŸ¥è¯†å›¾è°±ï¼Œå¹¶æŠŠåŽŸæœ¬ä¸æ˜Žæ˜¾çš„ç»“æž„å…³ç³»è¿˜ç»™ä½ ã€‚æ›´å¿«ç†è§£ä»£ç åº“ï¼Œæ‰¾åˆ°æž¶æž„å†³ç­–èƒŒåŽçš„"ä¸ºä»€ä¹ˆ"ã€‚

å®Œå…¨å¤šæ¨¡æ€ã€‚ä½ å¯ä»¥ç›´æŽ¥ä¸¢è¿›åŽ»ä»£ç ã€PDFã€Markdownã€æˆªå›¾ã€æµç¨‹å›¾ã€ç™½æ¿ç…§ç‰‡ï¼Œç”šè‡³å…¶ä»–è¯­è¨€çš„å›¾ç‰‡ â€”â€” graphify ä¼šç”¨ Claude vision ä»Žè¿™äº›å†…å®¹ä¸­æå–æ¦‚å¿µå’Œå…³ç³»ï¼Œå¹¶æŠŠå®ƒä»¬è¿žæŽ¥åˆ°åŒä¸€å¼ å›¾é‡Œã€‚

> Andrej Karpathy ä¼šç»´æŠ¤ä¸€ä¸ª `/raw` æ–‡ä»¶å¤¹ï¼ŒæŠŠè®ºæ–‡ã€æŽ¨æ–‡ã€æˆªå›¾å’Œç¬”è®°éƒ½ä¸¢è¿›åŽ»ã€‚graphify å°±æ˜¯åœ¨è§£å†³è¿™ç±»é—®é¢˜ â€”â€” ç›¸æ¯”ç›´æŽ¥è¯»å–åŽŸå§‹æ–‡ä»¶ï¼Œæ¯æ¬¡æŸ¥è¯¢çš„ token æ¶ˆè€—å¯é™ä½Ž **71.5 å€**ï¼Œç»“æžœè¿˜èƒ½è·¨ä¼šè¯æŒä¹…ä¿å­˜ï¼Œå¹¶ä¸”ä¼šæ˜Žç¡®åŒºåˆ†å“ªäº›å†…å®¹æ˜¯å®žé™…å‘çŽ°çš„ï¼Œå“ªäº›åªæ˜¯åˆç†æŽ¨æ–­ã€‚

```
/graphify .                        # å¯ç”¨äºŽä»»æ„ç›®å½•ï¼šä»£ç åº“ã€ç¬”è®°ã€è®ºæ–‡éƒ½å¯ä»¥
```

```
graphify-out/
â”œâ”€â”€ graph.html       å¯äº¤äº’å›¾è°±ï¼šå¯ç‚¹èŠ‚ç‚¹ã€æœç´¢ã€æŒ‰ç¤¾åŒºè¿‡æ»¤
â”œâ”€â”€ GRAPH_REPORT.md  God nodesã€æ„å¤–è¿žæŽ¥ã€å»ºè®®æé—®
â”œâ”€â”€ graph.json       æŒä¹…åŒ–å›¾è°±ï¼šæ•°å‘¨åŽä»å¯æŸ¥è¯¢ï¼Œæ— éœ€é‡æ–°è¯»åŽŸå§‹æ–‡ä»¶
â””â”€â”€ cache/           SHA256 ç¼“å­˜ï¼šé‡å¤è¿è¡Œæ—¶åªå¤„ç†å˜æ›´è¿‡çš„æ–‡ä»¶
```

## å·¥ä½œåŽŸç†

graphify åˆ†ä¸¤è½®æ‰§è¡Œã€‚ç¬¬ä¸€è½®æ˜¯ç¡®å®šæ€§çš„ AST æå–ï¼Œå¯¹ä»£ç æ–‡ä»¶åšç»“æž„åˆ†æžï¼ˆç±»ã€å‡½æ•°ã€å¯¼å…¥ã€è°ƒç”¨å›¾ã€docstringã€è§£é‡Šæ€§æ³¨é‡Šï¼‰ï¼Œè¿™ä¸€è½®ä¸éœ€è¦ LLMã€‚ç¬¬äºŒè½®ä¼šå¹¶è¡Œè°ƒç”¨ Claude å­ä»£ç†å¤„ç†æ–‡æ¡£ã€è®ºæ–‡å’Œå›¾ç‰‡ï¼Œä»Žä¸­æå–æ¦‚å¿µã€å…³ç³»å’Œè®¾è®¡åŠ¨æœºã€‚æœ€åŽæŠŠä¸¤è¾¹ç»“æžœåˆå¹¶åˆ°ä¸€ä¸ª NetworkX å›¾é‡Œï¼Œç”¨ Leiden ç¤¾åŒºå‘çŽ°ç®—æ³•åšèšç±»ï¼Œå¹¶å¯¼å‡ºæˆå¯äº¤äº’ HTMLã€å¯æŸ¥è¯¢ JSONï¼Œä»¥åŠä¸€ä»½äººç±»å¯è¯»çš„å®¡è®¡æŠ¥å‘Šã€‚

**èšç±»æ˜¯åŸºäºŽå›¾æ‹“æ‰‘å®Œæˆçš„ï¼Œä¸ä¾èµ– embeddingsã€‚** Leiden æŒ‰è¾¹å¯†åº¦å‘çŽ°ç¤¾åŒºã€‚Claude æŠ½å–å‡ºçš„è¯­ä¹‰ç›¸ä¼¼è¾¹ï¼ˆ`semantically_similar_to`ï¼Œæ ‡è®°ä¸º `INFERRED`ï¼‰æœ¬æ¥å°±å­˜åœ¨äºŽå›¾ä¸­ï¼Œæ‰€ä»¥ä¼šç›´æŽ¥å½±å“ç¤¾åŒºåˆ’åˆ†ã€‚å›¾ç»“æž„æœ¬èº«å°±æ˜¯ç›¸ä¼¼æ€§ä¿¡å·ï¼Œä¸éœ€è¦é¢å¤–çš„ embedding æ­¥éª¤ï¼Œä¹Ÿä¸éœ€è¦å‘é‡æ•°æ®åº“ã€‚

æ¯æ¡å…³ç³»éƒ½ä¼šè¢«æ ‡è®°ä¸º `EXTRACTED`ï¼ˆç›´æŽ¥åœ¨æºææ–™ä¸­æ‰¾åˆ°ï¼‰ã€`INFERRED`ï¼ˆåˆç†æŽ¨æ–­ï¼Œå¹¶é™„å¸¦ç½®ä¿¡åº¦åˆ†æ•°ï¼‰æˆ– `AMBIGUOUS`ï¼ˆæœ‰æ­§ä¹‰ï¼Œéœ€è¦å¤æ ¸ï¼‰ã€‚æ‰€ä»¥ä½ å§‹ç»ˆçŸ¥é“å“ªäº›æ˜¯å®žé™…å‘çŽ°çš„ï¼Œå“ªäº›æ˜¯æ¨¡åž‹çŒœå‡ºæ¥çš„ã€‚

## å®‰è£…

**è¦æ±‚ï¼š** Python 3.10+ï¼Œå¹¶ä¸”ä½¿ç”¨ä»¥ä¸‹å¹³å°ä¹‹ä¸€ï¼š[Claude Code](https://claude.ai/code)ã€[CodeBuddy](https://codebuddy.ai)ã€[Codex](https://openai.com/codex)ã€[OpenCode](https://opencode.ai)ã€[OpenClaw](https://openclaw.ai)ã€[Factory Droid](https://factory.ai) æˆ– [Trae](https://trae.ai)

```bash
pip install graphifyy && graphify install
```

> PyPI åŒ…å½“å‰æš‚æ—¶å« `graphifyy`ï¼Œå› ä¸º `graphify` è¿™ä¸ªåå­—è¿˜åœ¨å›žæ”¶ä¸­ã€‚CLI å‘½ä»¤å’Œ skill å‘½ä»¤ä»ç„¶éƒ½æ˜¯ `graphify`ã€‚

### å¹³å°æ”¯æŒ

| å¹³å° | å®‰è£…å‘½ä»¤ |
|------|----------|
| Claude Code | `graphify install` |
| CodeBuddy | `graphify install --platform codebuddy` |
| Codex | `graphify install --platform codex` |
| OpenCode | `graphify install --platform opencode` |
| OpenClaw | `graphify install --platform claw` |
| Factory Droid | `graphify install --platform droid` |
| Trae | `graphify install --platform trae` |
| Trae CN | `graphify install --platform trae-cn` |

Codex ç”¨æˆ·è¿˜éœ€è¦åœ¨ `~/.codex/config.toml` çš„ `[features]` ä¸‹æ‰“å¼€ `multi_agent = true`ï¼Œè¿™æ ·æ‰èƒ½å¹¶è¡Œæå–ã€‚CodeBuddy ä½¿ç”¨ä¸Ž Claude Code ç›¸åŒçš„ Agent å·¥å…·å’Œ PreToolUse hook æœºåˆ¶ã€‚OpenClaw ç›®å‰çš„å¹¶è¡Œ agent æ”¯æŒè¿˜æ¯”è¾ƒæ—©æœŸï¼Œæ‰€ä»¥ä½¿ç”¨é¡ºåºæå–ã€‚Trae ä½¿ç”¨ Agent å·¥å…·è¿›è¡Œå¹¶è¡Œå­ä»£ç†è°ƒåº¦ï¼Œ**ä¸æ”¯æŒ** PreToolUse hookï¼Œå› æ­¤ AGENTS.md æ˜¯å…¶å¸¸é©»æœºåˆ¶ã€‚

ç„¶åŽæ‰“å¼€ä½ çš„ AI ç¼–ç åŠ©æ‰‹ï¼Œè¾“å…¥ï¼š

```
/graphify .
```

### è®©åŠ©æ‰‹å§‹ç»ˆä¼˜å…ˆä½¿ç”¨å›¾è°±ï¼ˆæŽ¨èï¼‰

å›¾æž„å»ºå®ŒæˆåŽï¼Œåœ¨é¡¹ç›®é‡Œè¿è¡Œä¸€æ¬¡ï¼š

| å¹³å° | å‘½ä»¤ |
|------|------|
| Claude Code | `graphify claude install` |
| CodeBuddy | `graphify codebuddy install` |
| Codex | `graphify codex install` |
| OpenCode | `graphify opencode install` |
| OpenClaw | `graphify claw install` |
| Factory Droid | `graphify droid install` |
| Trae | `graphify trae install` |
| Trae CN | `graphify trae-cn install` |

**Claude Code** ä¼šåšä¸¤ä»¶äº‹ï¼š
1. åœ¨ `CLAUDE.md` ä¸­å†™å…¥ä¸€æ®µè§„åˆ™ï¼Œå‘Šè¯‰ Claude åœ¨å›žç­”æž¶æž„é—®é¢˜å‰å…ˆè¯» `graphify-out/GRAPH_REPORT.md`
2. å®‰è£…ä¸€ä¸ª **PreToolUse hook**ï¼ˆå†™å…¥ `settings.json`ï¼‰ï¼Œåœ¨æ¯æ¬¡ `Glob` å’Œ `Grep` å‰è§¦å‘

å¦‚æžœçŸ¥è¯†å›¾è°±å­˜åœ¨ï¼ŒClaude ä¼šå…ˆçœ‹åˆ°ï¼š_"graphify: Knowledge graph exists. Read graphify-out/GRAPH_REPORT.md for god nodes and community structure before searching raw files."_ â€”â€” è¿™æ · Claude ä¼šä¼˜å…ˆæŒ‰å›¾è°±å¯¼èˆªï¼Œè€Œä¸æ˜¯ä¸€ä¸Šæ¥å°± grep æ•´ä¸ªé¡¹ç›®ã€‚

**CodeBuddy** ä¸Ž Claude Code ç›¸åŒï¼Œä¹Ÿä¼šåšä¸¤ä»¶äº‹ï¼šåœ¨ `CODEBUDDY.md` ä¸­å†™å…¥è§„åˆ™ï¼Œå¹¶å®‰è£… **PreToolUse hook**ï¼ˆå†™å…¥ `.codebuddy/settings.json`ï¼‰ï¼Œåœ¨æ¯æ¬¡ `Glob` å’Œ `Grep` å‰è§¦å‘ã€‚

**Codexã€OpenCodeã€OpenClawã€Factory Droidã€Trae** ä¼šæŠŠåŒæ ·çš„è§„åˆ™å†™è¿›é¡¹ç›®æ ¹ç›®å½•çš„ `AGENTS.md`ã€‚è¿™äº›å¹³å°æ²¡æœ‰ PreToolUse hookï¼Œæ‰€ä»¥ `AGENTS.md` æ˜¯å®ƒä»¬çš„å¸¸é©»æœºåˆ¶ã€‚

å¸è½½æ—¶ä½¿ç”¨å¯¹åº”å¹³å°çš„ uninstall å‘½ä»¤å³å¯ï¼ˆä¾‹å¦‚ `graphify claude uninstall`ï¼‰ã€‚

**å¸¸é©»æ¨¡å¼å’Œæ˜¾å¼è§¦å‘æœ‰ä»€ä¹ˆåŒºåˆ«ï¼Ÿ**

å¸¸é©» hook ä¼šä¼˜å…ˆæš´éœ² `GRAPH_REPORT.md` â€”â€” è¿™æ˜¯ä¸€é¡µå¼æ€»ç»“ï¼ŒåŒ…å« god nodesã€ç¤¾åŒºç»“æž„å’Œæ„å¤–è¿žæŽ¥ã€‚ä½ çš„åŠ©æ‰‹åœ¨æœç´¢æ–‡ä»¶å‰ä¼šå…ˆè¯»å®ƒï¼Œå› æ­¤ä¼šæŒ‰ç»“æž„å¯¼èˆªï¼Œè€Œä¸æ˜¯æŒ‰å…³é”®å­—ä¹±æœã€‚è¿™å·²ç»èƒ½è¦†ç›–å¤§éƒ¨åˆ†æ—¥å¸¸é—®é¢˜ã€‚

`/graphify query`ã€`/graphify path` å’Œ `/graphify explain` ä¼šæ›´æ·±å…¥ï¼šå®ƒä»¬ä¼šé€è·³éåŽ†åº•å±‚ `graph.json`ï¼Œè¿½è¸ªèŠ‚ç‚¹ä¹‹é—´çš„ç²¾ç¡®è·¯å¾„ï¼Œå¹¶å±•ç¤ºè¾¹çº§åˆ«ç»†èŠ‚ï¼ˆå…³ç³»ç±»åž‹ã€ç½®ä¿¡åº¦ã€æºä½ç½®ï¼‰ã€‚å½“ä½ æƒ³ä»Žå›¾è°±é‡Œç²¾ç¡®å›žç­”æŸä¸ªé—®é¢˜ï¼Œè€Œä¸ä»…ä»…æ˜¯èŽ·å¾—æ•´ä½“æ„ŸçŸ¥æ—¶ï¼Œå°±è¯¥ç”¨è¿™äº›å‘½ä»¤ã€‚

å¯ä»¥è¿™æ ·ç†è§£ï¼šå¸¸é©» hook æ˜¯å…ˆç»™åŠ©æ‰‹ä¸€å¼ åœ°å›¾ï¼Œ`/graphify` è¿™å‡ ä¸ªå‘½ä»¤åˆ™æ˜¯è®©å®ƒæ²¿ç€åœ°å›¾ç²¾ç¡®å¯¼èˆªã€‚

<details>
<summary>æ‰‹åŠ¨å®‰è£…ï¼ˆcurlï¼‰</summary>

```bash
mkdir -p ~/.claude/skills/graphify
curl -fsSL https://raw.githubusercontent.com/safishamsi/graphify/v3/graphify/skill.md \
  > ~/.claude/skills/graphify/SKILL.md
```

æŠŠä¸‹é¢å†…å®¹åŠ åˆ° `~/.claude/CLAUDE.md`ï¼š

```
- **graphify** (`~/.claude/skills/graphify/SKILL.md`) - any input to knowledge graph. Trigger: `/graphify`
When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.
```

</details>

## ç”¨æ³•

```
/graphify                          # å¯¹å½“å‰ç›®å½•è¿è¡Œ
/graphify ./raw                    # å¯¹æŒ‡å®šç›®å½•è¿è¡Œ
/graphify ./raw --mode deep        # æ›´æ¿€è¿›åœ°æŠ½å– INFERRED è¾¹
/graphify ./raw --update           # åªé‡æ–°æå–å˜æ›´æ–‡ä»¶ï¼Œå¹¶åˆå¹¶åˆ°å·²æœ‰å›¾è°±
/graphify ./raw --cluster-only     # åªé‡æ–°èšç±»å·²æœ‰å›¾è°±ï¼Œä¸é‡æ–°æå–
/graphify ./raw --no-viz           # è·³è¿‡ HTMLï¼Œåªç”Ÿæˆ report + JSON
/graphify ./raw --obsidian         # é¢å¤–ç”Ÿæˆ Obsidian vaultï¼ˆå¯é€‰ï¼‰

/graphify add https://arxiv.org/abs/1706.03762        # æ‹‰å–è®ºæ–‡ã€ä¿å­˜å¹¶æ›´æ–°å›¾è°±
/graphify add https://x.com/karpathy/status/...       # æ‹‰å–æŽ¨æ–‡
/graphify add https://... --author "Name"             # æ ‡è®°åŽŸä½œè€…
/graphify add https://... --contributor "Name"        # æ ‡è®°æ˜¯è°æŠŠå®ƒåŠ å…¥è¯­æ–™åº“çš„

/graphify query "what connects attention to the optimizer?"
/graphify query "what connects attention to the optimizer?" --dfs   # è¿½è¸ªä¸€æ¡å…·ä½“è·¯å¾„
/graphify query "what connects attention to the optimizer?" --budget 1500  # æŠŠé¢„ç®—é™åˆ¶åœ¨ N tokens
/graphify path "DigestAuth" "Response"
/graphify explain "SwinTransformer"

/graphify ./raw --watch            # æ–‡ä»¶å˜æ›´æ—¶è‡ªåŠ¨åŒæ­¥å›¾è°±ï¼ˆä»£ç ï¼šç«‹å³æ›´æ–°ï¼›æ–‡æ¡£ï¼šæé†’ä½ ï¼‰
/graphify ./raw --wiki             # æž„å»ºå¯ä¾› agent æŠ“å–çš„ wikiï¼ˆindex.md + æ¯ä¸ª community ä¸€ç¯‡æ–‡ç« ï¼‰
/graphify ./raw --svg              # å¯¼å‡º graph.svg
/graphify ./raw --graphml          # å¯¼å‡º graph.graphmlï¼ˆGephiã€yEdï¼‰
/graphify ./raw --neo4j            # ç”Ÿæˆç»™ Neo4j ç”¨çš„ cypher.txt
/graphify ./raw --neo4j-push bolt://localhost:7687    # ç›´æŽ¥æŽ¨é€åˆ°è¿è¡Œä¸­çš„ Neo4j
/graphify ./raw --mcp              # å¯åŠ¨ MCP stdio server

# git hooks - è·¨å¹³å°ï¼Œåœ¨ commit å’Œåˆ‡åˆ†æ”¯åŽé‡å»ºå›¾è°±
graphify hook install
graphify hook uninstall
graphify hook status

# å¸¸é©»åŠ©æ‰‹è§„åˆ™ - æŒ‰å¹³å°åŒºåˆ†
graphify claude install            # CLAUDE.md + PreToolUse hookï¼ˆClaude Codeï¼‰
graphify claude uninstall
graphify codex install             # AGENTS.mdï¼ˆCodexï¼‰
graphify opencode install          # AGENTS.mdï¼ˆOpenCodeï¼‰
graphify claw install              # AGENTS.mdï¼ˆOpenClawï¼‰
graphify droid install             # AGENTS.mdï¼ˆFactory Droidï¼‰
graphify trae install              # AGENTS.mdï¼ˆTraeï¼‰
graphify trae uninstall
graphify trae-cn install           # AGENTS.mdï¼ˆTrae CNï¼‰
graphify trae-cn uninstall
```

æ”¯æŒæ··åˆæ–‡ä»¶ç±»åž‹ï¼š

| ç±»åž‹ | æ‰©å±•å | æå–æ–¹å¼ |
|------|--------|----------|
| ä»£ç  | `.py .ts .js .go .rs .java .c .cpp .rb .cs .kt .scala .php` | tree-sitter AST + è°ƒç”¨å›¾ + docstring / æ³¨é‡Šä¸­çš„ rationale |
| æ–‡æ¡£ | `.md .txt .rst` | é€šè¿‡ Claude æå–æ¦‚å¿µã€å…³ç³»å’Œè®¾è®¡åŠ¨æœº |
| è®ºæ–‡ | `.pdf` | å¼•æ–‡æŒ–æŽ˜ + æ¦‚å¿µæå– |
| å›¾ç‰‡ | `.png .jpg .webp .gif` | Claude vision â€”â€” æˆªå›¾ã€å›¾è¡¨ã€ä»»æ„è¯­è¨€éƒ½å¯ä»¥ |

## ä½ ä¼šå¾—åˆ°ä»€ä¹ˆ

**God nodes** â€”â€” åº¦æœ€é«˜çš„æ¦‚å¿µèŠ‚ç‚¹ï¼ˆæ•´ä¸ªç³»ç»Ÿæœ€å®¹æ˜“æ±‡èšåˆ°çš„åœ°æ–¹ï¼‰

**æ„å¤–è¿žæŽ¥** â€”â€” æŒ‰ç»¼åˆå¾—åˆ†æŽ’åºã€‚ä»£ç -è®ºæ–‡ä¹‹é—´çš„è¾¹ä¼šæ¯”ä»£ç -ä»£ç è¾¹æƒé‡æ›´é«˜ã€‚æ¯æ¡ç»“æžœéƒ½ä¼šé™„å¸¦ä¸€æ®µäººè¯è§£é‡Šã€‚

**å»ºè®®æé—®** â€”â€” å›¾è°±ç‰¹åˆ«æ“…é•¿å›žç­”çš„ 4 åˆ° 5 ä¸ªé—®é¢˜ã€‚

**â€œä¸ºä»€ä¹ˆâ€** â€”â€” docstringã€è¡Œå†…æ³¨é‡Šï¼ˆ`# NOTE:`ã€`# IMPORTANT:`ã€`# HACK:`ã€`# WHY:`ï¼‰ä»¥åŠæ–‡æ¡£é‡Œçš„è®¾è®¡åŠ¨æœºéƒ½ä¼šè¢«æŠ½å–æˆ `rationale_for` èŠ‚ç‚¹ã€‚ä¸åªæ˜¯çŸ¥é“ä»£ç â€œåšäº†ä»€ä¹ˆâ€ï¼Œè¿˜èƒ½çŸ¥é“â€œä¸ºä»€ä¹ˆè¦è¿™ä¹ˆå†™â€ã€‚

**ç½®ä¿¡åº¦åˆ†æ•°** â€”â€” æ¯æ¡ `INFERRED` è¾¹éƒ½æœ‰ `confidence_score`ï¼ˆ0.0-1.0ï¼‰ã€‚ä½ ä¸åªçŸ¥é“å“ªäº›æ˜¯çŒœå‡ºæ¥çš„ï¼Œè¿˜çŸ¥é“æ¨¡åž‹å¯¹è¿™ä¸ªçŒœæµ‹æœ‰å¤šæœ‰æŠŠæ¡ã€‚`EXTRACTED` è¾¹æ’ä¸º 1.0ã€‚

**è¯­ä¹‰ç›¸ä¼¼è¾¹** â€”â€” è·¨æ–‡ä»¶çš„æ¦‚å¿µè¿žæŽ¥ï¼Œå³ä½¿ç»“æž„ä¸Šæ²¡æœ‰ç›´æŽ¥ä¾èµ–ä¹Ÿèƒ½å»ºç«‹å…³è”ã€‚æ¯”å¦‚ä¸¤ä¸ªå‡½æ•°åšçš„æ˜¯åŒä¸€ç±»é—®é¢˜ä½†å½¼æ­¤æ²¡æœ‰è°ƒç”¨ï¼Œæˆ–è€…æŸä¸ªä»£ç ç±»å’ŒæŸç¯‡è®ºæ–‡é‡Œçš„ç®—æ³•æ¦‚å¿µæœ¬è´¨ç›¸åŒã€‚

**è¶…è¾¹ï¼ˆHyperedgesï¼‰** â€”â€” ç”¨æ¥è¡¨è¾¾ 3 ä¸ªä»¥ä¸ŠèŠ‚ç‚¹çš„ç¾¤ç»„å…³ç³»ï¼Œè¿™æ˜¯æ™®é€šä¸¤ä¸¤è¾¹è¡¨è¾¾ä¸å‡ºæ¥çš„ã€‚æ¯”å¦‚ï¼šä¸€ç»„ç±»å…±åŒå®žçŽ°ä¸€ä¸ªåè®®ã€è®¤è¯é“¾è·¯é‡Œçš„ä¸€ç»„å‡½æ•°ã€åŒä¸€ç¯‡è®ºæ–‡æŸä¸€èŠ‚é‡Œçš„å¤šä¸ªæ¦‚å¿µå…±åŒç»„æˆä¸€ä¸ªæƒ³æ³•ã€‚

**Token åŸºå‡†** â€”â€” æ¯æ¬¡è¿è¡ŒåŽéƒ½ä¼šè‡ªåŠ¨æ‰“å°ã€‚å¯¹æ··åˆè¯­æ–™ï¼ˆKarpathy çš„ä»“åº“ + è®ºæ–‡ + å›¾ç‰‡ï¼‰ï¼Œæ¯æ¬¡æŸ¥è¯¢çš„ token æ¶ˆè€—å¯ä»¥æ¯”ç›´æŽ¥è¯»åŽŸæ–‡ä»¶å°‘ **71.5 å€**ã€‚ç¬¬ä¸€æ¬¡è¿è¡Œéœ€è¦å…ˆæå–å¹¶å»ºå›¾ï¼Œè¿™ä¸€æ­¥ä¼šèŠ± tokenï¼›åŽç»­æŸ¥è¯¢ç›´æŽ¥è¯»å–åŽ‹ç¼©åŽçš„å›¾è°±ï¼ŒèŠ‚çœä¼šè¶Šæ¥è¶Šæ˜Žæ˜¾ã€‚SHA256 ç¼“å­˜ä¿è¯é‡å¤è¿è¡Œæ—¶åªé‡æ–°å¤„ç†å˜æ›´æ–‡ä»¶ã€‚

**è‡ªåŠ¨åŒæ­¥**ï¼ˆ`--watch`ï¼‰â€”â€” åœ¨åŽå°ç»ˆç«¯é‡Œè·‘ç€ï¼Œä»£ç åº“ä¸€å˜åŒ–ï¼Œå›¾è°±å°±ä¼šè·Ÿç€æ›´æ–°ã€‚ä»£ç æ–‡ä»¶ä¿å­˜ä¼šç«‹åˆ»è§¦å‘é‡å»ºï¼ˆåªèµ° ASTï¼Œä¸ç”¨ LLMï¼‰ï¼›æ–‡æ¡£/å›¾ç‰‡å˜æ›´åˆ™ä¼šæé†’ä½ è·‘ `--update` è¿›è¡Œ LLM å†æå–ã€‚

**Git hooks**ï¼ˆ`graphify hook install`ï¼‰â€”â€” å®‰è£… `post-commit` å’Œ `post-checkout` hookã€‚æ¯æ¬¡ commit åŽã€æ¯æ¬¡åˆ‡åˆ†æ”¯åŽéƒ½ä¼šè‡ªåŠ¨é‡å»ºå›¾è°±ï¼Œä¸éœ€è¦é¢å¤–å¼€ä¸€ä¸ªåŽå°è¿›ç¨‹ã€‚

**Wiki**ï¼ˆ`--wiki`ï¼‰â€”â€” ä¸ºæ¯ä¸ª community å’Œ god node ç”Ÿæˆç±»ä¼¼ç»´åŸºç™¾ç§‘çš„ Markdown æ–‡ç« ï¼Œå¹¶æä¾› `index.md` ä½œä¸ºå…¥å£ã€‚ä»»ä½• agent åªè¦è¯» `index.md`ï¼Œå°±èƒ½é€šè¿‡æ™®é€šæ–‡ä»¶å¯¼èˆªæ•´ä¸ªçŸ¥è¯†åº“ï¼Œè€Œä¸å¿…ç›´æŽ¥è§£æž JSONã€‚

## Worked examples

| è¯­æ–™ | æ–‡ä»¶æ•° | åŽ‹ç¼©æ¯” | è¾“å‡º |
|------|--------|--------|------|
| Karpathy çš„ä»“åº“ + 5 ç¯‡è®ºæ–‡ + 4 å¼ å›¾ç‰‡ | 52 | **71.5x** | [`worked/karpathy-repos/`](worked/karpathy-repos/) |
| graphify æºç  + Transformer è®ºæ–‡ | 4 | **5.4x** | [`worked/mixed-corpus/`](worked/mixed-corpus/) |
| httpxï¼ˆåˆæˆ Python åº“ï¼‰ | 6 | ~1x | [`worked/httpx/`](worked/httpx/) |

Token åŽ‹ç¼©æ•ˆæžœä¼šéšç€è¯­æ–™è§„æ¨¡å¢žå¤§è€Œæ›´æ˜Žæ˜¾ã€‚6 ä¸ªæ–‡ä»¶æœ¬æ¥å°±å¡žå¾—è¿›ä¸Šä¸‹æ–‡çª—å£ï¼Œæ‰€ä»¥ graphify åœ¨è¿™ç§åœºæ™¯é‡Œçš„ä»·å€¼æ›´å¤šæ˜¯ç»“æž„æ¸…æ™°åº¦ï¼Œè€Œä¸æ˜¯ token åŽ‹ç¼©ã€‚åˆ°äº† 52 ä¸ªæ–‡ä»¶ï¼ˆä»£ç  + è®ºæ–‡ + å›¾ç‰‡ï¼‰è¿™ç§è§„æ¨¡ï¼Œå°±èƒ½åšåˆ° 71x+ã€‚æ¯ä¸ª `worked/` ç›®å½•é‡Œéƒ½å¸¦äº†åŽŸå§‹è¾“å…¥å’ŒçœŸå®žè¾“å‡ºï¼ˆ`GRAPH_REPORT.md`ã€`graph.json`ï¼‰ï¼Œä½ å¯ä»¥è‡ªå·±è·‘ä¸€éæ ¸å¯¹æ•°å­—ã€‚

## éšç§

graphify ä¼šæŠŠæ–‡æ¡£ã€è®ºæ–‡å’Œå›¾ç‰‡çš„å†…å®¹å‘é€ç»™ä½ æ‰€ç”¨ AI ç¼–ç åŠ©æ‰‹èƒŒåŽçš„æ¨¡åž‹ API æ¥åšè¯­ä¹‰æå– â€”â€” å¯èƒ½æ˜¯ Anthropicï¼ˆClaude Codeï¼‰ã€OpenAIï¼ˆCodexï¼‰ï¼Œæˆ–è€…ä½ å½“å‰å¹³å°ä½¿ç”¨çš„å…¶ä»–æä¾›æ–¹ã€‚ä»£ç æ–‡ä»¶åˆ™å®Œå…¨åœ¨æœ¬åœ°é€šè¿‡ tree-sitter AST å¤„ç†ï¼Œä¸ä¼šæŠŠä»£ç å†…å®¹å‘å‡ºåŽ»ã€‚é¡¹ç›®æœ¬èº«æ²¡æœ‰ä»»ä½•é¥æµ‹ã€ä½¿ç”¨è·Ÿè¸ªæˆ–åˆ†æžã€‚å”¯ä¸€çš„ç½‘ç»œè¯·æ±‚å°±æ˜¯è¯­ä¹‰æå–é˜¶æ®µè°ƒç”¨ä½ å¹³å°è‡ªå·±çš„æ¨¡åž‹ APIï¼Œä½¿ç”¨çš„ä¹Ÿæ˜¯ä½ è‡ªå·±çš„ API keyã€‚

## æŠ€æœ¯æ ˆ

NetworkX + Leidenï¼ˆgraspologicï¼‰+ tree-sitter + vis.jsã€‚è¯­ä¹‰æå–ç”± Claudeï¼ˆClaude Codeï¼‰ã€GPT-4ï¼ˆCodexï¼‰æˆ–ä½ å½“å‰å¹³å°æ‰€è¿è¡Œçš„æ¨¡åž‹å®Œæˆã€‚ä¸éœ€è¦ Neo4jï¼Œä¸éœ€è¦ serverï¼Œæ•´ä½“æ˜¯çº¯æœ¬åœ°è¿è¡Œã€‚

<details>
<summary>è´¡çŒ®</summary>

**Worked examples** æ˜¯æœ€èƒ½å»ºç«‹ä¿¡ä»»çš„è´¡çŒ®æ–¹å¼ã€‚å¯¹ä¸€ä¸ªçœŸå®žè¯­æ–™è·‘ `/graphify`ï¼ŒæŠŠè¾“å‡ºä¿å­˜åˆ° `worked/{slug}/`ï¼Œå†å†™ä¸€ä»½è¯šå®žçš„ `review.md`ï¼Œè¯„ä»·å›¾è°±å“ªäº›åœ°æ–¹åšå¾—å¯¹ã€å“ªäº›åœ°æ–¹åšå¾—ä¸å¯¹ï¼Œç„¶åŽæäº¤ PRã€‚

**æå– bug** â€”â€” æ issue æ—¶è¯·é™„ä¸Šè¾“å…¥æ–‡ä»¶ã€å¯¹åº”çš„ç¼“å­˜é¡¹ï¼ˆ`graphify-out/cache/`ï¼‰ä»¥åŠå®ƒæ¼æå–æˆ–çžŽç¼–äº†ä»€ä¹ˆã€‚

æ¨¡å—èŒè´£å’Œæ–°å¢žè¯­è¨€çš„æ–¹æ³•è§ [ARCHITECTURE.md](ARCHITECTURE.md)ã€‚

</details>

