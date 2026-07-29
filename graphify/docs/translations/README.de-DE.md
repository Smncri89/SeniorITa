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
  <a href="https://www.linkedin.com/company/graphify-labs"><img src="https://img.shields.io/badge/LinkedIn-Graphify%20Labs-0077B5?logo=linkedin" alt="LinkedIn"/></a>
</p>

**Eine KI-Coding-Assistent-Skill.** Tippe `/graphify` in Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro oder Google Antigravity â€” es liest deine Dateien, baut einen Wissensgraphen und gibt dir Struktur zurÃ¼ck, die du vorher nicht sehen konntest. Verstehe eine Codebasis schneller. Finde das â€žWarum" hinter Architekturentscheidungen.

VollstÃ¤ndig multimodal. Leg Code, PDFs, Markdown, Screenshots, Diagramme, Whiteboard-Fotos, Bilder in anderen Sprachen oder Video- und Audiodateien ab â€” graphify extrahiert Konzepte und Beziehungen aus allem und verbindet sie in einem einzigen Graphen. Videos werden lokal mit Whisper transkribiert, angetrieben durch einen domÃ¤nenspezifischen Prompt aus deinem Korpus. 25 Programmiersprachen werden Ã¼ber tree-sitter AST unterstÃ¼tzt (Python, JS, TS, Go, Rust, Java, C, C++, Ruby, C#, Kotlin, Scala, PHP, Swift, Lua, Zig, PowerShell, Elixir, Objective-C, Julia, Verilog, SystemVerilog, Vue, Svelte, Dart).

> Andrej Karpathy fÃ¼hrt einen `/raw`-Ordner, in dem er Papers, Tweets, Screenshots und Notizen ablegt. graphify ist die Antwort auf dieses Problem â€” 71,5-fach weniger Tokens pro Abfrage gegenÃ¼ber dem Lesen der Rohdateien, persistent Ã¼ber Sitzungen hinweg, ehrlich darÃ¼ber, was gefunden vs. erschlossen wurde.

```
/graphify .                        # funktioniert mit jedem Ordner â€” Codebase, Notizen, Papers, alles
```

```
graphify-out/
â”œâ”€â”€ graph.html       interaktiver Graph â€” im Browser Ã¶ffnen, Knoten anklicken, suchen, filtern
â”œâ”€â”€ GRAPH_REPORT.md  Gott-Knoten, Ã¼berraschende Verbindungen, vorgeschlagene Fragen
â”œâ”€â”€ graph.json       persistenter Graph â€” Wochen spÃ¤ter abfragen, ohne neu zu lesen
â””â”€â”€ cache/           SHA256-Cache â€” erneute AusfÃ¼hrungen verarbeiten nur geÃ¤nderte Dateien
```

FÃ¼ge eine `.graphifyignore`-Datei hinzu, um Ordner auszuschlieÃŸen:

```
# .graphifyignore
vendor/
node_modules/
dist/
*.generated.py
```

Gleiche Syntax wie `.gitignore`. Du kannst eine einzelne `.graphifyignore` im Repo-Stammverzeichnis behalten â€” Muster funktionieren korrekt, auch wenn graphify auf einem Unterordner ausgefÃ¼hrt wird.

## So funktioniert es

graphify lÃ¤uft in drei DurchgÃ¤ngen. Zuerst extrahiert ein deterministischer AST-Durchgang Strukturen aus Code-Dateien (Klassen, Funktionen, Importe, Aufrufgraphen, Docstrings, BegrÃ¼ndungskommentare) â€” ohne LLM. Zweitens werden Video- und Audiodateien lokal mit faster-whisper transkribiert, angetrieben durch einen domÃ¤nenspezifischen Prompt aus Korpus-Gott-Knoten â€” Transkripte werden gecacht, sodass erneute AusfÃ¼hrungen sofort sind. Drittens laufen Claude-Subagenten parallel Ã¼ber Dokumente, Papers, Bilder und Transkripte, um Konzepte, Beziehungen und DesignbegrÃ¼ndungen zu extrahieren. Die Ergebnisse werden in einem NetworkX-Graphen zusammengefÃ¼hrt, mit Leiden-Community-Erkennung geclustert und als interaktives HTML, abfragbares JSON und ein Klartext-Audit-Report exportiert.

**Clustering basiert auf Graph-Topologie â€” keine Embeddings.** Leiden findet Communities durch Kantendichte. Die semantischen Ã„hnlichkeitskanten, die Claude extrahiert (`semantically_similar_to`, markiert als INFERRED), sind bereits im Graphen, sodass sie die Community-Erkennung direkt beeinflussen. Die Graphstruktur ist das Ã„hnlichkeitssignal â€” kein separater Embedding-Schritt oder Vektordatenbank nÃ¶tig.

Jede Beziehung ist markiert als `EXTRACTED` (direkt in der Quelle gefunden), `INFERRED` (begrÃ¼ndete Schlussfolgerung mit Konfidenzwert) oder `AMBIGUOUS` (zur ÃœberprÃ¼fung markiert). Du weiÃŸt immer, was gefunden vs. erschlossen wurde.

## Installation

**Voraussetzungen:** Python 3.10+ und eines von: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli), [VS Code Copilot Chat](https://code.visualstudio.com/docs/copilot/overview), [Aider](https://aider.chat), [OpenClaw](https://openclaw.ai), [Factory Droid](https://factory.ai), [Trae](https://trae.ai), [Kiro](https://kiro.dev), Hermes oder [Google Antigravity](https://antigravity.google)

```bash
# Empfohlen â€” funktioniert auf Mac und Linux ohne PATH-Einrichtung
uv tool install graphifyy && graphify install
# oder mit pipx
pipx install graphifyy && graphify install
# oder einfaches pip
pip install graphifyy && graphify install
```

> **Offizielles Paket:** Das PyPI-Paket heiÃŸt `graphifyy` (installieren mit `pip install graphifyy`). Andere Pakete mit Namen `graphify*` auf PyPI sind nicht mit diesem Projekt verbunden. Das einzige offizielle Repository ist [safishamsi/graphify](https://github.com/safishamsi/graphify). CLI und Skill-Befehl heiÃŸen weiterhin `graphify`.

> **`graphify: command not found`?** Verwende `uv tool install graphifyy` (empfohlen) oder `pipx install graphifyy` â€” beide platzieren die CLI an einem verwalteten Ort, der automatisch im PATH ist. Mit einfachem `pip` musst du mÃ¶glicherweise `~/.local/bin` (Linux) oder `~/Library/Python/3.x/bin` (Mac) zum PATH hinzufÃ¼gen, oder `python -m graphify` verwenden.

### PlattformunterstÃ¼tzung

| Plattform | Installationsbefehl |
|-----------|---------------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (automatisch erkannt) oder `graphify install --platform windows` |
| Codex | `graphify install --platform codex` |
| OpenCode | `graphify install --platform opencode` |
| GitHub Copilot CLI | `graphify install --platform copilot` |
| VS Code Copilot Chat | `graphify vscode install` |
| Aider | `graphify install --platform aider` |
| OpenClaw | `graphify install --platform claw` |
| Factory Droid | `graphify install --platform droid` |
| Trae | `graphify install --platform trae` |
| Trae CN | `graphify install --platform trae-cn` |
| Gemini CLI | `graphify install --platform gemini` |
| Hermes | `graphify install --platform hermes` |
| Kiro IDE/CLI | `graphify kiro install` |
| Cursor | `graphify cursor install` |
| Google Antigravity | `graphify antigravity install` |

Dann Ã¶ffne deinen KI-Coding-Assistenten und tippe:

```
/graphify .
```

Hinweis: Codex verwendet `$` statt `/` fÃ¼r Skill-Aufrufe, also tippe `$graphify .`.

### Assistenten immer den Graphen nutzen lassen (empfohlen)

Nach dem Erstellen eines Graphen, fÃ¼hre dies einmal in deinem Projekt aus:

| Plattform | Befehl |
|-----------|--------|
| Claude Code | `graphify claude install` |
| Codex | `graphify codex install` |
| OpenCode | `graphify opencode install` |
| GitHub Copilot CLI | `graphify copilot install` |
| VS Code Copilot Chat | `graphify vscode install` |
| Aider | `graphify aider install` |
| OpenClaw | `graphify claw install` |
| Factory Droid | `graphify droid install` |
| Trae | `graphify trae install` |
| Trae CN | `graphify trae-cn install` |
| Cursor | `graphify cursor install` |
| Gemini CLI | `graphify gemini install` |
| Hermes | `graphify hermes install` |
| Kiro IDE/CLI | `graphify kiro install` |
| Google Antigravity | `graphify antigravity install` |

## Verwendung

```
/graphify                          # aktuelles Verzeichnis verarbeiten
/graphify ./raw                    # spezifischen Ordner verarbeiten
/graphify ./raw --mode deep        # aggressivere INFERRED-Kanten-Extraktion
/graphify ./raw --update           # nur geÃ¤nderte Dateien neu extrahieren
/graphify ./raw --directed         # gerichteten Graphen erstellen
/graphify ./raw --cluster-only     # Clustering auf bestehendem Graphen neu ausfÃ¼hren
/graphify ./raw --no-viz           # kein HTML, nur Report + JSON
/graphify ./raw --obsidian         # Obsidian-Vault generieren (opt-in)

/graphify add https://arxiv.org/abs/1706.03762   # Paper abrufen, speichern, Graphen aktualisieren
/graphify add <video-url>                         # Audio herunterladen, transkribieren, hinzufÃ¼gen
/graphify query "was verbindet Attention mit dem Optimizer?"
/graphify path "DigestAuth" "Response"
/graphify explain "SwinTransformer"

graphify hook install              # Git-Hooks installieren
graphify update ./src              # Code-Dateien neu extrahieren, kein LLM benÃ¶tigt
graphify watch ./src               # Graphen bei Ã„nderungen automatisch aktualisieren
```

## Was du bekommst

**Gott-Knoten** â€” Konzepte mit dem hÃ¶chsten Grad (durch die alles flieÃŸt)

**Ãœberraschende Verbindungen** â€” nach Composite-Score eingestuft. Code-Paper-Kanten werden hÃ¶her bewertet. Jedes Ergebnis enthÃ¤lt ein Klartext-Warum.

**Vorgeschlagene Fragen** â€” 4-5 Fragen, die der Graph einzigartig gut beantworten kann

**Das â€žWarum"** â€” Docstrings, Inline-Kommentare (`# NOTE:`, `# IMPORTANT:`, `# HACK:`, `# WHY:`), und DesignbegrÃ¼ndungen aus Dokumenten werden als `rationale_for`-Knoten extrahiert.

**Konfidenzwerte** â€” jede INFERRED-Kante hat einen `confidence_score` (0,0-1,0).

**Token-Benchmark** â€” wird automatisch nach jeder AusfÃ¼hrung gedruckt. Auf einem gemischten Korpus: **71,5-fach** weniger Tokens pro Abfrage gegenÃ¼ber Rohdateien.

**Auto-Sync** (`--watch`) â€” lÃ¤uft im Hintergrund und aktualisiert den Graphen bei CodeÃ¤nderungen automatisch.

**Git-Hooks** (`graphify hook install`) â€” installiert Post-Commit- und Post-Checkout-Hooks.

## Datenschutz

graphify sendet Dateiinhalte an die Modell-API deines KI-Assistenten fÃ¼r semantische Extraktion von Dokumenten, Papers und Bildern. Code-Dateien werden lokal via tree-sitter AST verarbeitet â€” kein Dateiinhalt verlÃ¤sst dein GerÃ¤t fÃ¼r Code. Video- und Audiodateien werden lokal mit faster-whisper transkribiert. Keine Telemetrie, keine Nutzungsverfolgung.

## Tech-Stack

NetworkX + Leiden (graspologic) + tree-sitter + vis.js. Semantische Extraktion via Claude, GPT-4 oder welches Modell deine Plattform verwendet. Video-Transkription via faster-whisper + yt-dlp (optional).

## Auf graphify aufgebaut â€” Penpax

[**Penpax**](https://safishamsi.github.io/penpax.ai) ist die Enterprise-Schicht Ã¼ber graphify. Wo graphify einen Ordner mit Dateien in einen Wissensgraphen verwandelt, wendet Penpax denselben Graphen auf dein gesamtes Arbeitsleben an â€” kontinuierlich.

**Kostenlose Testversion startet bald.** [Auf die Warteliste setzen â†’](https://safishamsi.github.io/penpax.ai)

## Star-Verlauf

[![Star History Chart](https://api.star-history.com/svg?repos=safishamsi/graphify&type=Date)](https://star-history.com/#safishamsi/graphify&Date)

