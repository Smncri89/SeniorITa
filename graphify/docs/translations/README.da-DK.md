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

**En fÃ¦rdighed til AI-kodeassistenter.** Skriv `/graphify` i Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro eller Google Antigravity â€” den lÃ¦ser dine filer, bygger en vidensgraf og giver dig den struktur tilbage, du ikke vidste eksisterede. ForstÃ¥ en kodebase hurtigere. Find "hvorfor" bag arkitektoniske beslutninger.

Fuldt multimodal. TilfÃ¸j kode, PDF'er, markdown, skÃ¦rmbilleder, diagrammer, whiteboardfotos, billeder pÃ¥ andre sprog eller video- og lydfiler â€” graphify udtrÃ¦kker begreber og relationer fra alt og forbinder dem i Ã©n graf. Videoer transskriberes lokalt med Whisper. UnderstÃ¸tter 25 programmeringssprog via tree-sitter AST.

> Andrej Karpathy opretholder en `/raw`-mappe, hvor han lÃ¦gger artikler, tweets, skÃ¦rmbilleder og noter. graphify er svaret pÃ¥ det problem â€” **71,5x** fÃ¦rre tokens pr. forespÃ¸rgsel sammenlignet med at lÃ¦se rÃ¥ filer, vedvarende mellem sessioner.

```
/graphify .
```

```
graphify-out/
â”œâ”€â”€ graph.html       interaktiv graf â€” Ã¥bn i enhver browser
â”œâ”€â”€ GRAPH_REPORT.md  gudknuder, overraskende forbindelser, foreslÃ¥ede spÃ¸rgsmÃ¥l
â”œâ”€â”€ graph.json       vedvarende graf â€” forespÃ¸rgselsbar uger senere
â””â”€â”€ cache/           SHA256-cache â€” gentagne kÃ¸rsler behandler kun Ã¦ndrede filer
```

## SÃ¥dan fungerer det

graphify arbejder i tre gennemlÃ¸b. FÃ¸rst udtrÃ¦kker et deterministisk AST-gennemlÃ¸b struktur fra kodefiler uden LLM. Derefter transskriberes video- og lydfiler lokalt med faster-whisper. Endelig kÃ¸rer Claude-underagenter parallelt pÃ¥ dokumenter, artikler, billeder og transskriptioner. Resultaterne flettes ind i en NetworkX-graf, klynges med Leiden og eksporteres som interaktiv HTML, forespÃ¸rgselsbar JSON og revisionsrapport.

Hver relation er mÃ¦rket `EXTRACTED`, `INFERRED` (med konfidensscore) eller `AMBIGUOUS`.

## Installation

**Krav:** Python 3.10+ og Ã©n af: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com) og andre.

```bash
uv tool install graphifyy && graphify install
# eller med pipx
pipx install graphifyy && graphify install
# eller pip
pip install graphifyy && graphify install
```

> **Officiel pakke:** PyPI-pakken hedder `graphifyy`. Det eneste officielle lager er [safishamsi/graphify](https://github.com/safishamsi/graphify).

## Brug

```
/graphify .
/graphify ./raw --update
/graphify query "hvad forbinder Attention med optimizeren?"
/graphify path "DigestAuth" "Response"
graphify hook install
graphify update ./src
```

## Hvad du fÃ¥r

**Gudknuder** â€” begreber med den hÃ¸jeste grad Â· **Overraskende forbindelser** â€” rangeret efter score Â· **ForeslÃ¥ede spÃ¸rgsmÃ¥l** Â· **"Hvorfor"** â€” docstrings og designbegrundelse udtrukket som knuder Â· **Token-benchmark** â€” **71,5x** fÃ¦rre tokens pÃ¥ blandet korpus.

## Privatliv

Kodefiler behandles lokalt via tree-sitter AST. Videoer transskriberes lokalt med faster-whisper. Ingen telemetri.

## Bygget pÃ¥ graphify â€” Penpax

[**Penpax**](https://safishamsi.github.io/penpax.ai) er enterprise-laget oven pÃ¥ graphify. **Gratis prÃ¸veperiode kommer snart.** [Tilmeld dig ventelisten â†’](https://safishamsi.github.io/penpax.ai)

[![Star History Chart](https://api.star-history.com/svg?repos=safishamsi/graphify&type=Date)](https://star-history.com/#safishamsi/graphify&Date)

