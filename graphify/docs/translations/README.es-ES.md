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

**Una habilidad para asistentes de cÃ³digo IA.** Escribe `/graphify` en Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro o Google Antigravity â€” lee tus archivos, construye un grafo de conocimiento y te devuelve estructura que no sabÃ­as que existÃ­a. Entiende una base de cÃ³digo mÃ¡s rÃ¡pido. Encuentra el Â«por quÃ©Â» detrÃ¡s de las decisiones arquitectÃ³nicas.

Totalmente multimodal. Deposita cÃ³digo, PDFs, markdown, capturas de pantalla, diagramas, fotos de pizarras, imÃ¡genes en otros idiomas, o archivos de video y audio â€” graphify extrae conceptos y relaciones de todo ello y los conecta en un solo grafo. Los videos se transcriben localmente con Whisper usando un prompt adaptado al dominio derivado de tu corpus. 25 lenguajes de programaciÃ³n soportados mediante tree-sitter AST (Python, JS, TS, Go, Rust, Java, C, C++, Ruby, C#, Kotlin, Scala, PHP, Swift, Lua, Zig, PowerShell, Elixir, Objective-C, Julia, Verilog, SystemVerilog, Vue, Svelte, Dart).

> Andrej Karpathy mantiene una carpeta `/raw` donde deposita papers, tweets, capturas de pantalla y notas. graphify es la respuesta a ese problema â€” 71,5 veces menos tokens por consulta versus leer los archivos sin procesar, persistente entre sesiones, honesto sobre lo que encontrÃ³ versus lo que infiriÃ³.

```
/graphify .                        # funciona con cualquier carpeta â€” tu cÃ³digo, notas, papers, todo
```

```
graphify-out/
â”œâ”€â”€ graph.html       grafo interactivo â€” abrir en cualquier navegador, hacer clic en nodos, buscar
â”œâ”€â”€ GRAPH_REPORT.md  nodos dios, conexiones sorprendentes, preguntas sugeridas
â”œâ”€â”€ graph.json       grafo persistente â€” consultar semanas despuÃ©s sin releer
â””â”€â”€ cache/           cachÃ© SHA256 â€” las re-ejecuciones solo procesan archivos modificados
```

AÃ±ade un archivo `.graphifyignore` para excluir carpetas:

```
# .graphifyignore
vendor/
node_modules/
dist/
*.generated.py
```

Misma sintaxis que `.gitignore`. Puedes mantener un Ãºnico `.graphifyignore` en la raÃ­z del repositorio.

## CÃ³mo funciona

graphify se ejecuta en tres pasadas. Primero, una pasada AST determinista extrae estructura de los archivos de cÃ³digo (clases, funciones, importaciones, grafos de llamadas, docstrings, comentarios de justificaciÃ³n) sin necesidad de LLM. Segundo, los archivos de video y audio se transcriben localmente con faster-whisper usando un prompt adaptado al dominio derivado de los nodos dios del corpus. Tercero, subagentes de Claude se ejecutan en paralelo sobre documentos, papers, imÃ¡genes y transcripciones para extraer conceptos, relaciones y justificaciones de diseÃ±o. Los resultados se fusionan en un grafo NetworkX, se agrupan con detecciÃ³n de comunidades Leiden, y se exportan como HTML interactivo, JSON consultable y un informe de auditorÃ­a en lenguaje natural.

**El clustering se basa en la topologÃ­a del grafo â€” sin embeddings.** Leiden encuentra comunidades por densidad de aristas. Las aristas de similitud semÃ¡ntica que Claude extrae (`semantically_similar_to`, marcadas como INFERRED) ya estÃ¡n en el grafo. La estructura del grafo es la seÃ±al de similitud â€” no se necesita paso de embedding separado ni base de datos vectorial.

Cada relaciÃ³n estÃ¡ etiquetada como `EXTRACTED` (encontrada directamente en la fuente), `INFERRED` (inferencia razonable con puntuaciÃ³n de confianza) o `AMBIGUOUS` (marcada para revisiÃ³n).

## InstalaciÃ³n

**Requisitos:** Python 3.10+ y uno de: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli), [VS Code Copilot Chat](https://code.visualstudio.com/docs/copilot/overview), [Aider](https://aider.chat), [OpenClaw](https://openclaw.ai), [Factory Droid](https://factory.ai), [Trae](https://trae.ai), [Kiro](https://kiro.dev), Hermes o [Google Antigravity](https://antigravity.google)

```bash
# Recomendado â€” funciona en Mac y Linux sin configurar el PATH
uv tool install graphifyy && graphify install
# o con pipx
pipx install graphifyy && graphify install
# o pip simple
pip install graphifyy && graphify install
```

> **Paquete oficial:** El paquete PyPI se llama `graphifyy` (instalar con `pip install graphifyy`). Otros paquetes llamados `graphify*` en PyPI no estÃ¡n afiliados con este proyecto. El Ãºnico repositorio oficial es [safishamsi/graphify](https://github.com/safishamsi/graphify).

### Soporte de plataformas

| Plataforma | Comando de instalaciÃ³n |
|------------|------------------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (detecciÃ³n automÃ¡tica) o `graphify install --platform windows` |
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

Luego abre tu asistente de cÃ³digo IA y escribe:

```
/graphify .
```

Nota: Codex usa `$` en lugar de `/` para habilidades, asÃ­ que escribe `$graphify .`.

### Hacer que el asistente siempre use el grafo (recomendado)

DespuÃ©s de construir un grafo, ejecuta esto una vez en tu proyecto:

| Plataforma | Comando |
|------------|---------|
| Claude Code | `graphify claude install` |
| Codex | `graphify codex install` |
| OpenCode | `graphify opencode install` |
| Cursor | `graphify cursor install` |
| Gemini CLI | `graphify gemini install` |
| Kiro IDE/CLI | `graphify kiro install` |
| Google Antigravity | `graphify antigravity install` |

## Uso

```
/graphify                          # directorio actual
/graphify ./raw                    # carpeta especÃ­fica
/graphify ./raw --mode deep        # extracciÃ³n de aristas INFERRED mÃ¡s agresiva
/graphify ./raw --update           # re-extraer solo archivos modificados
/graphify ./raw --directed         # grafo dirigido
/graphify ./raw --cluster-only     # re-ejecutar clustering en grafo existente
/graphify ./raw --no-viz           # sin HTML, solo informe + JSON
/graphify ./raw --obsidian         # generar vault de Obsidian (opt-in)

/graphify add https://arxiv.org/abs/1706.03762   # obtener un paper
/graphify add <video-url>                         # descargar audio, transcribir, aÃ±adir
/graphify query "Â¿quÃ© conecta Attention con el optimizador?"
/graphify path "DigestAuth" "Response"
/graphify explain "SwinTransformer"

graphify hook install              # instalar hooks de Git
graphify update ./src              # re-extraer archivos de cÃ³digo, sin LLM
graphify watch ./src               # actualizaciÃ³n automÃ¡tica del grafo
```

## QuÃ© obtienes

**Nodos dios** â€” conceptos con mayor grado (por donde todo pasa)

**Conexiones sorprendentes** â€” clasificadas por puntuaciÃ³n compuesta. Las aristas cÃ³digo-paper puntÃºan mÃ¡s alto. Cada resultado incluye un por quÃ© en lenguaje natural.

**Preguntas sugeridas** â€” 4-5 preguntas que el grafo estÃ¡ en posiciÃ³n Ãºnica de responder

**El Â«por quÃ©Â»** â€” docstrings, comentarios inline (`# NOTE:`, `# IMPORTANT:`, `# HACK:`, `# WHY:`), y justificaciones de diseÃ±o extraÃ­das como nodos `rationale_for`.

**Puntuaciones de confianza** â€” cada arista INFERRED tiene un `confidence_score` (0,0-1,0).

**Benchmark de tokens** â€” impreso automÃ¡ticamente tras cada ejecuciÃ³n. En un corpus mixto: **71,5 veces** menos tokens por consulta vs archivos sin procesar.

**SincronizaciÃ³n automÃ¡tica** (`--watch`) â€” actualiza el grafo automÃ¡ticamente cuando cambia el cÃ³digo.

**Hooks de Git** (`graphify hook install`) â€” instala hooks post-commit y post-checkout.

## Privacidad

graphify envÃ­a contenido de archivos a la API del modelo de tu asistente IA para extracciÃ³n semÃ¡ntica de documentos, papers e imÃ¡genes. Los archivos de cÃ³digo se procesan localmente mediante tree-sitter AST. Los archivos de video y audio se transcriben localmente con faster-whisper. Sin telemetrÃ­a, sin seguimiento de uso.

## Stack tÃ©cnico

NetworkX + Leiden (graspologic) + tree-sitter + vis.js. ExtracciÃ³n semÃ¡ntica via Claude, GPT-4 o el modelo de tu plataforma. TranscripciÃ³n de video via faster-whisper + yt-dlp (opcional).

## Construido sobre graphify â€” Penpax

[**Penpax**](https://safishamsi.github.io/penpax.ai) es la capa enterprise sobre graphify. Donde graphify convierte una carpeta de archivos en un grafo de conocimiento, Penpax aplica el mismo grafo a toda tu vida laboral â€” continuamente.

**Prueba gratuita prÃ³ximamente.** [Unirse a la lista de espera â†’](https://safishamsi.github.io/penpax.ai)

## Historial de estrellas

[![Star History Chart](https://api.star-history.com/svg?repos=safishamsi/graphify&type=Date)](https://star-history.com/#safishamsi/graphify&Date)

