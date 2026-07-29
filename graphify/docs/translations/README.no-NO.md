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

**En ferdighet for AI-kodeassistenter.** Skriv `/graphify` i Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro eller Google Antigravity â€” den leser filene dine, bygger en kunnskapsgraf og gir deg tilbake strukturen du ikke visste eksisterte. ForstÃ¥ en kodebase raskere. Finn Â«hvorforÂ» bak arkitektoniske beslutninger.

Fullt multimodal. Legg til kode, PDF-er, markdown, skjermbilder, diagrammer, whiteboardbilder, bilder pÃ¥ andre sprÃ¥k eller video- og lydfiler â€” graphify ekstraherer begreper og relasjoner fra alt og kobler dem i Ã©n graf. Videoer transkriberes lokalt med Whisper. StÃ¸tter 25 programmeringssprÃ¥k via tree-sitter AST.

> Andrej Karpathy opprettholder en `/raw`-mappe der han legger artikler, tweets, skjermbilder og notater. graphify er svaret pÃ¥ det problemet â€” **71,5x** fÃ¦rre tokens per spÃ¸rring sammenlignet med Ã¥ lese rÃ¥filer, vedvarende mellom sesjoner.

```
/graphify .
```

```
graphify-out/
â”œâ”€â”€ graph.html       interaktiv graf â€” Ã¥pne i en hvilken som helst nettleser
â”œâ”€â”€ GRAPH_REPORT.md  gudnoder, overraskende forbindelser, foreslÃ¥tte spÃ¸rsmÃ¥l
â”œâ”€â”€ graph.json       vedvarende graf â€” forespÃ¸rselbar uker senere
â””â”€â”€ cache/           SHA256-cache â€” gjentatte kjÃ¸ringer behandler bare endrede filer
```

## Hvordan det fungerer

graphify arbeider i tre gjennomganger. FÃ¸rst ekstraherer et deterministisk AST-gjennomgang struktur fra kodefiler uten LLM. Deretter transkriberes video- og lydfiler lokalt med faster-whisper. Til slutt kjÃ¸rer Claude-underagenter parallelt pÃ¥ dokumenter, artikler, bilder og transkripsjoner. Resultatene slÃ¥s sammen i en NetworkX-graf, klynges med Leiden og eksporteres som interaktiv HTML, forespÃ¸rselbar JSON og revisjonsrapport.

Hver relasjon er merket `EXTRACTED`, `INFERRED` (med konfidenspoeng) eller `AMBIGUOUS`.

## Installasjon

**Krav:** Python 3.10+ og Ã©n av: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com) og andre.

```bash
uv tool install graphifyy && graphify install
# eller med pipx
pipx install graphifyy && graphify install
# eller pip
pip install graphifyy && graphify install
```

> **Offisiell pakke:** PyPI-pakken heter `graphifyy`. Det eneste offisielle depotet er [safishamsi/graphify](https://github.com/safishamsi/graphify).

## Bruk

```
/graphify .
/graphify ./raw --update
/graphify query "hva kobler Attention til optimizeren?"
/graphify path "DigestAuth" "Response"
graphify hook install
graphify update ./src
```

## Hva du fÃ¥r

**Gudnoder** â€” begreper med hÃ¸yest grad Â· **Overraskende forbindelser** â€” rangert etter poeng Â· **ForeslÃ¥tte spÃ¸rsmÃ¥l** Â· **Â«HvorforÂ»** â€” docstrings og designbegrunnelse ekstrahert som noder Â· **Token-benchmark** â€” **71,5x** fÃ¦rre tokens pÃ¥ blandet korpus.

## Personvern

Kodefiler behandles lokalt via tree-sitter AST. Videoer transkriberes lokalt med faster-whisper. Ingen telemetri.

## Bygget pÃ¥ graphify â€” Penpax

[**Penpax**](https://safishamsi.github.io/penpax.ai) er enterprise-laget oppÃ¥ graphify. **Gratis prÃ¸veperiode kommer snart.** [Bli med pÃ¥ ventelisten â†’](https://safishamsi.github.io/penpax.ai)

[![Star History Chart](https://api.star-history.com/svg?repos=safishamsi/graphify&type=Date)](https://star-history.com/#safishamsi/graphify&Date)

