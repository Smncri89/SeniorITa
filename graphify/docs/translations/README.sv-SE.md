<p align="center">
  <img src="https://raw.githubusercontent.com/safishamsi/graphify/v4/docs/logo-text.svg" width="260" height="64" alt="Graphify"/>
</p>

<p align="center">
  ðŸ‡ºðŸ‡¸ <a href="../../README.md">English</a> | ðŸ‡¨ðŸ‡³ <a href="README.zh-CN.md">ç®€ä½“ä¸­æ–‡</a> | ðŸ‡¯ðŸ‡µ <a href="README.ja-JP.md">æ—¥æœ¬èªž</a> | ðŸ‡°ðŸ‡· <a href="README.ko-KR.md">í•œêµ­ì–´</a> | ðŸ‡©ðŸ‡ª <a href="README.de-DE.md">Deutsch</a> | ðŸ‡«ðŸ‡· <a href="README.fr-FR.md">FranÃ§ais</a> | ðŸ‡ªðŸ‡¸ <a href="README.es-ES.md">EspaÃ±ol</a> | ðŸ‡®ðŸ‡³ <a href="README.hi-IN.md">à¤¹à¤¿à¤¨à¥à¤¦à¥€</a> | ðŸ‡§ðŸ‡· <a href="README.pt-BR.md">PortuguÃªs</a> | ðŸ‡·ðŸ‡º <a href="README.ru-RU.md">Ð ÑƒÑÑÐºÐ¸Ð¹</a> | ðŸ‡¸ðŸ‡¦ <a href="README.ar-SA.md">Ø§Ù„Ø¹Ø±Ø¨ÙŠØ©</a> | ðŸ‡®ðŸ‡¹ <a href="README.it-IT.md">Italiano</a> | ðŸ‡µðŸ‡± <a href="README.pl-PL.md">Polski</a> | ðŸ‡³ðŸ‡± <a href="README.nl-NL.md">Nederlands</a> | ðŸ‡¹ðŸ‡· <a href="README.tr-TR.md">TÃ¼rkÃ§e</a> | ðŸ‡ºðŸ‡¦ <a href="README.uk-UA.md">Ð£ÐºÑ€Ð°Ñ—Ð½ÑÑŒÐºÐ°</a> | ðŸ‡»ðŸ‡³ <a href="README.vi-VN.md">Tiáº¿ng Viá»‡t</a> | ðŸ‡®ðŸ‡© <a href="README.id-ID.md">Bahasa Indonesia</a> | ðŸ‡¸ðŸ‡ª <a href="README.sv-SE.md">Svenska</a> | ðŸ‡¬ðŸ‡· <a href="README.el-GR.md">Î•Î»Î»Î·Î½Î¹ÎºÎ¬</a> | ðŸ‡·ðŸ‡´ <a href="README.ro-RO.md">RomÃ¢nÄƒ</a> | ðŸ‡¨ðŸ‡¿ <a href="README.cs-CZ.md">ÄŒeÅ¡tina</a> | ðŸ‡«ðŸ‡® <a href="README.fi-FI.md">Suomi</a> | ðŸ‡©ðŸ‡° <a href="README.da-DK.md">Dansk</a> | ðŸ‡³ðŸ‡´ <a href="README.no-NO.md">Norsk</a> | ðŸ‡­ðŸ‡º <a href="README.hu-HU.md">Magyar</a> | ðŸ‡¹ðŸ‡­ <a href="README.th-TH.md">à¸ à¸²à¸©à¸²à¹„à¸—à¸¢</a> | ðŸ‡ºðŸ‡¿ <a href="README.uz-UZ.md">OÊ»zbekcha</a> | ðŸ‡¹ðŸ‡¼ <a href="README.zh-TW.md">ç¹é«”ä¸­æ–‡</a>
</p>

<p align="center">
  <a href="https://github.com/safishamsi/graphify/actions/workflows/ci.yml"><img src="https://github.com/safishamsi/graphify/actions/workflows/ci.yml/badge.svg?branch=v4" alt="CI"/></a>
  <a href="https://pypi.org/project/graphifyy/"><img src="https://img.shields.io/pypi/v/graphifyy" alt="PyPI"/></a>
  <a href="https://pepy.tech/project/graphifyy"><img src="https://static.pepy.tech/badge/graphifyy" alt="Downloads"/></a>
  <a href="https://github.com/sponsors/safishamsi"><img src="https://img.shields.io/badge/sponsor-safishamsi-ea4aaa?logo=github-sponsors" alt="Sponsor"/></a>
</p>

**En fÃ¤rdighet fÃ¶r AI-kodassistenter.** Skriv `/graphify` i Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro eller Google Antigravity â€” den lÃ¤ser dina filer, bygger ett kunskapsgrafer och ger tillbaka strukturen du inte visste fanns. FÃ¶rstÃ¥ en kodbas snabbare. Hitta "varfÃ¶r" bakom arkitekturella beslut.

Helt multimodal. LÃ¤gg till kod, PDF:er, markdown, skÃ¤rmdumpar, diagram, whiteboardfoton, bilder pÃ¥ andra sprÃ¥k eller video- och ljudfiler â€” graphify extraherar begrepp och relationer frÃ¥n allt och kopplar samman dem i ett enda graf. Videor transkriberas lokalt med Whisper. StÃ¶djer 25 programmeringssprÃ¥k via tree-sitter AST.

> Andrej Karpathy hÃ¥ller en `/raw`-mapp dÃ¤r han lÃ¤gger papper, tweets, skÃ¤rmdumpar och anteckningar. graphify Ã¤r svaret pÃ¥ det problemet â€” **71,5x** fÃ¤rre tokens per frÃ¥ga jÃ¤mfÃ¶rt med att lÃ¤sa rÃ¥filer, bestÃ¤ndigt mellan sessioner.

```
/graphify .
```

```
graphify-out/
â”œâ”€â”€ graph.html       interaktivt diagram â€” Ã¶ppna i valfri webblÃ¤sare
â”œâ”€â”€ GRAPH_REPORT.md  gudnoder, Ã¶verraskande kopplingar, fÃ¶reslagna frÃ¥gor
â”œâ”€â”€ graph.json       bestÃ¤ndigt diagram â€” kan frÃ¥gas veckor senare
â””â”€â”€ cache/           SHA256-cache â€” upprepade kÃ¶rningar behandlar bara Ã¤ndrade filer
```

## Hur det fungerar

graphify arbetar i tre pass. FÃ¶rst extraherar ett deterministiskt AST-pass struktur frÃ¥n kodfiler utan LLM. Sedan transkriberas video- och ljudfiler lokalt med faster-whisper. Slutligen kÃ¶r Claude-subagenter parallellt pÃ¥ dokument, papper, bilder och transkriptioner. Resultaten slÃ¥s samman i ett NetworkX-diagram, klustras med Leiden och exporteras som interaktiv HTML, frÃ¥gebar JSON och revisionsrapport.

Varje relation Ã¤r mÃ¤rkt `EXTRACTED`, `INFERRED` (med konfidenspoÃ¤ng) eller `AMBIGUOUS`.

## Installation

**Krav:** Python 3.10+ och ett av: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com) med flera.

```bash
uv tool install graphifyy && graphify install
# eller med pipx
pipx install graphifyy && graphify install
# eller pip
pip install graphifyy && graphify install
```

> **Officiellt paket:** PyPI-paketet heter `graphifyy`. Det enda officiella fÃ¶rrÃ¥det Ã¤r [safishamsi/graphify](https://github.com/safishamsi/graphify).

## AnvÃ¤ndning

```
/graphify .
/graphify ./raw --update
/graphify query "vad kopplar Attention till optimizern?"
/graphify path "DigestAuth" "Response"
graphify hook install
graphify update ./src
```

## Vad du fÃ¥r

**Gudnoder** â€” begrepp med hÃ¶gst grad Â· **Ã–verraskande kopplingar** â€” rangordnade efter poÃ¤ng Â· **FÃ¶reslagna frÃ¥gor** Â· **"VarfÃ¶r"** â€” docstrÃ¤ngar och designmotivering extraherade som noder Â· **Token-benchmark** â€” **71,5x** fÃ¤rre tokens pÃ¥ blandat korpus.

## Integritet

Kodfiler behandlas lokalt via tree-sitter AST. Videor transkriberas lokalt med faster-whisper. Ingen telemetri.

## Byggt pÃ¥ graphify â€” Penpax

[**Penpax**](https://safishamsi.github.io/penpax.ai) Ã¤r enterprise-lagret ovanpÃ¥ graphify. **Gratis provperiod kommer snart.** [GÃ¥ med i vÃ¤ntelistan â†’](https://safishamsi.github.io/penpax.ai)

[![Star History Chart](https://api.star-history.com/svg?repos=safishamsi/graphify&type=Date)](https://star-history.com/#safishamsi/graphify&Date)

