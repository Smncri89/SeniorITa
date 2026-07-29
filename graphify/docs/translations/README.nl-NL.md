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

**Een vaardigheid voor AI-codeassistenten.** Typ `/graphify` in Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro of Google Antigravity â€” het leest je bestanden, bouwt een kennisgraaf en geeft je structuur terug die je niet wist dat er was. Begrijp een codebase sneller. Vind het "waarom" achter architecturale beslissingen.

Volledig multimodaal. Voeg code, PDF's, markdown, schermafbeeldingen, diagrammen, whiteboard-foto's, afbeeldingen in andere talen of video- en audiobestanden toe â€” graphify extraheert concepten en relaties uit alles en verbindt ze in Ã©Ã©n graaf. Video's worden lokaal getranscribeerd met Whisper. Ondersteunt 25 programmeertalen via tree-sitter AST.

> Andrej Karpathy houdt een `/raw`-map bij waar hij papers, tweets, schermafbeeldingen en notities neerlegt. graphify is het antwoord op dat probleem â€” **71,5x** minder tokens per query versus het lezen van ruwe bestanden, persistent tussen sessies.

```
/graphify .
```

```
graphify-out/
â”œâ”€â”€ graph.html       interactieve graaf â€” open in elke browser
â”œâ”€â”€ GRAPH_REPORT.md  godknooppunten, verrassende verbindingen, voorgestelde vragen
â”œâ”€â”€ graph.json       persistente graaf â€” weken later opvraagbaar
â””â”€â”€ cache/           SHA256-cache â€” herhaalde runs verwerken alleen gewijzigde bestanden
```

## Hoe het werkt

graphify werkt in drie passes. Eerst extraheert een deterministische AST-pass structuur uit codebestanden zonder LLM. Vervolgens worden video- en audiobestanden lokaal getranscribeerd met faster-whisper. Ten slotte werken Claude-subagenten parallel over documenten, papers, afbeeldingen en transcripties. De resultaten worden samengevoegd in een NetworkX-graaf, geclusterd met Leiden en geÃ«xporteerd als interactieve HTML, opvraagbare JSON en een auditrapport.

Elke relatie is gelabeld als `EXTRACTED`, `INFERRED` (met betrouwbaarheidsscore) of `AMBIGUOUS`.

## Installatie

**Vereisten:** Python 3.10+ en Ã©Ã©n van: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [Cursor](https://cursor.com), [Aider](https://aider.chat) en andere.

```bash
uv tool install graphifyy && graphify install
# of met pipx
pipx install graphifyy && graphify install
# of pip
pip install graphifyy && graphify install
```

> **Officieel pakket:** Het PyPI-pakket heet `graphifyy`. De enige officiÃ«le repository is [safishamsi/graphify](https://github.com/safishamsi/graphify).

## Gebruik

```
/graphify .
/graphify ./raw --update
/graphify query "wat verbindt Attention met de optimizer?"
/graphify path "DigestAuth" "Response"
graphify hook install
graphify update ./src
```

## Wat je krijgt

**Godknooppunten** â€” concepten met de hoogste graad Â· **Verrassende verbindingen** â€” gerangschikt op score Â· **Voorgestelde vragen** Â· **Het "waarom"** â€” docstrings en ontwerprationale als knooppunten Â· **Tokenbenchmark** â€” **71,5x** minder tokens op gemengd corpus.

## Privacy

Codebestanden worden lokaal verwerkt via tree-sitter AST. Video's lokaal getranscribeerd met faster-whisper. Geen telemetrie.

## Gebouwd op graphify â€” Penpax

[**Penpax**](https://safishamsi.github.io/penpax.ai) is de enterprise-laag boven op graphify. **Gratis proefversie binnenkort.** [Meld je aan voor de wachtlijst â†’](https://safishamsi.github.io/penpax.ai)

[![Star History Chart](https://api.star-history.com/svg?repos=safishamsi/graphify&type=Date)](https://star-history.com/#safishamsi/graphify&Date)

