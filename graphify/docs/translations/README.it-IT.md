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

**Una skill per assistenti di codice IA.** Scrivi `/graphify` in Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro o Google Antigravity â€” legge i tuoi file, costruisce un grafo della conoscenza e ti restituisce struttura che non sapevi esistesse. Comprendi una codebase piÃ¹ velocemente. Trova il "perchÃ©" dietro le decisioni architetturali.

Completamente multimodale. Aggiungi codice, PDF, markdown, screenshot, diagrammi, foto di lavagne, immagini in altre lingue, o file video e audio â€” graphify estrae concetti e relazioni da tutto e li connette in un unico grafo. I video vengono trascritti localmente con Whisper. Supporta 25 linguaggi di programmazione via tree-sitter AST.

> Andrej Karpathy mantiene una cartella `/raw` dove deposita paper, tweet, screenshot e note. graphify Ã¨ la risposta a quel problema â€” **71,5x** meno token per query rispetto alla lettura dei file grezzi, persistente tra le sessioni.

```
/graphify .                        # funziona con qualsiasi cartella
```

```
graphify-out/
â”œâ”€â”€ graph.html       grafo interattivo â€” apri in qualsiasi browser
â”œâ”€â”€ GRAPH_REPORT.md  nodi dio, connessioni sorprendenti, domande suggerite
â”œâ”€â”€ graph.json       grafo persistente â€” interrogabile settimane dopo
â””â”€â”€ cache/           cache SHA256 â€” le riesecuzioni elaborano solo i file modificati
```

## Come funziona

graphify esegue in tre passaggi. Prima, un passaggio AST deterministico estrae la struttura dai file di codice senza LLM. Poi, i file video e audio vengono trascritti localmente con faster-whisper. Infine, i subagenti Claude eseguono in parallelo su documenti, paper, immagini e trascrizioni. I risultati vengono uniti in un grafo NetworkX, raggruppati con Leiden e esportati come HTML interattivo, JSON interrogabile e report di audit.

Ogni relazione Ã¨ etichettata `EXTRACTED`, `INFERRED` (con punteggio di confidenza) o `AMBIGUOUS`.

## Installazione

**Requisiti:** Python 3.10+ e uno tra: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [Aider](https://aider.chat) e altri.

```bash
uv tool install graphifyy && graphify install
# oppure con pipx
pipx install graphifyy && graphify install
# oppure pip
pip install graphifyy && graphify install
```

> **Pacchetto ufficiale:** Il pacchetto PyPI si chiama `graphifyy`. L'unico repository ufficiale Ã¨ [safishamsi/graphify](https://github.com/safishamsi/graphify).

## Utilizzo

```
/graphify .
/graphify ./raw --update           # solo file modificati
/graphify ./raw --mode deep
/graphify query "cosa connette Attention all'ottimizzatore?"
/graphify path "DigestAuth" "Response"
graphify hook install
graphify update ./src
```

## Cosa ottieni

**Nodi dio** â€” concetti con il grado piÃ¹ alto Â· **Connessioni sorprendenti** â€” classificate per punteggio Â· **Domande suggerite** â€” 4-5 domande che il grafo Ã¨ in grado di rispondere in modo unico Â· **Il "perchÃ©"** â€” docstring e rationale di design estratti come nodi Â· **Benchmark token** â€” **71,5x** meno token su corpus misto.

## Privacy

I file di codice vengono elaborati localmente via tree-sitter AST. I video vengono trascritti localmente con faster-whisper. Nessuna telemetria.

## Costruito su graphify â€” Penpax

[**Penpax**](https://safishamsi.github.io/penpax.ai) Ã¨ il livello enterprise su graphify. **Prova gratuita in arrivo.** [Unisciti alla lista d'attesa â†’](https://safishamsi.github.io/penpax.ai)

[![Star History Chart](https://api.star-history.com/svg?repos=safishamsi/graphify&type=Date)](https://star-history.com/#safishamsi/graphify&Date)

