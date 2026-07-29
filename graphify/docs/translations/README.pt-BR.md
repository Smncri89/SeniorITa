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

**Uma habilidade para assistentes de cÃ³digo IA.** Digite `/graphify` no Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro ou Google Antigravity â€” ele lÃª seus arquivos, constrÃ³i um grafo de conhecimento e devolve a vocÃª estrutura que vocÃª nÃ£o sabia que existia. Entenda uma base de cÃ³digo mais rapidamente. Encontre o "porquÃª" por trÃ¡s das decisÃµes arquiteturais.

Totalmente multimodal. Adicione cÃ³digo, PDFs, markdown, capturas de tela, diagramas, fotos de quadros brancos, imagens em outros idiomas, ou arquivos de vÃ­deo e Ã¡udio â€” graphify extrai conceitos e relaÃ§Ãµes de tudo isso e os conecta em um Ãºnico grafo. VÃ­deos sÃ£o transcritos localmente com Whisper usando um prompt adaptado ao domÃ­nio derivado do seu corpus. 25 linguagens de programaÃ§Ã£o suportadas via tree-sitter AST (Python, JS, TS, Go, Rust, Java, C, C++, Ruby, C#, Kotlin, Scala, PHP, Swift, Lua, Zig, PowerShell, Elixir, Objective-C, Julia, Verilog, SystemVerilog, Vue, Svelte, Dart).

> Andrej Karpathy mantÃ©m uma pasta `/raw` onde deposita papers, tweets, capturas de tela e notas. graphify Ã© a resposta para esse problema â€” 71,5x menos tokens por consulta versus ler os arquivos brutos, persistente entre sessÃµes, honesto sobre o que foi encontrado versus inferido.

```
/graphify .                        # funciona em qualquer pasta â€” seu cÃ³digo, notas, papers, tudo
```

```
graphify-out/
â”œâ”€â”€ graph.html       grafo interativo â€” abrir em qualquer navegador, clicar em nÃ³s, pesquisar
â”œâ”€â”€ GRAPH_REPORT.md  nÃ³s deus, conexÃµes surpreendentes, perguntas sugeridas
â”œâ”€â”€ graph.json       grafo persistente â€” consultar semanas depois sem reler
â””â”€â”€ cache/           cache SHA256 â€” re-execuÃ§Ãµes processam apenas arquivos modificados
```

Adicione um arquivo `.graphifyignore` para excluir pastas:

```
# .graphifyignore
vendor/
node_modules/
dist/
*.generated.py
```

Mesma sintaxe do `.gitignore`.

## Como funciona

graphify executa em trÃªs passes. Primeiro, uma passagem AST determinÃ­stica extrai estrutura de arquivos de cÃ³digo (classes, funÃ§Ãµes, importaÃ§Ãµes, grafos de chamadas, docstrings, comentÃ¡rios de justificativa) sem LLM. Segundo, arquivos de vÃ­deo e Ã¡udio sÃ£o transcritos localmente com faster-whisper. Terceiro, subagentes Claude executam em paralelo sobre documentos, papers, imagens e transcriÃ§Ãµes para extrair conceitos, relaÃ§Ãµes e justificativas de design. Os resultados sÃ£o mesclados em um grafo NetworkX, agrupados com detecÃ§Ã£o de comunidades Leiden, e exportados como HTML interativo, JSON consultÃ¡vel e um relatÃ³rio de auditoria em linguagem natural.

**O clustering Ã© baseado em topologia de grafo â€” sem embeddings.** Leiden encontra comunidades por densidade de arestas. As arestas de similaridade semÃ¢ntica que Claude extrai (`semantically_similar_to`, marcadas INFERRED) jÃ¡ estÃ£o no grafo. A estrutura do grafo Ã© o sinal de similaridade â€” nenhum passo de embedding separado ou banco de dados vetorial Ã© necessÃ¡rio.

Cada relaÃ§Ã£o Ã© marcada como `EXTRACTED` (encontrada diretamente na fonte), `INFERRED` (inferÃªncia razoÃ¡vel com pontuaÃ§Ã£o de confianÃ§a) ou `AMBIGUOUS` (marcada para revisÃ£o).

## InstalaÃ§Ã£o

**Requisitos:** Python 3.10+ e um de: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli), [VS Code Copilot Chat](https://code.visualstudio.com/docs/copilot/overview), [Aider](https://aider.chat), [OpenClaw](https://openclaw.ai), [Factory Droid](https://factory.ai), [Trae](https://trae.ai), [Kiro](https://kiro.dev), Hermes ou [Google Antigravity](https://antigravity.google)

```bash
# Recomendado â€” funciona no Mac e Linux sem configurar o PATH
uv tool install graphifyy && graphify install
# ou com pipx
pipx install graphifyy && graphify install
# ou pip simples
pip install graphifyy && graphify install
```

> **Pacote oficial:** O pacote PyPI chama-se `graphifyy` (instalar com `pip install graphifyy`). Outros pacotes chamados `graphify*` no PyPI nÃ£o sÃ£o afiliados a este projeto. O Ãºnico repositÃ³rio oficial Ã© [safishamsi/graphify](https://github.com/safishamsi/graphify).

### Suporte a plataformas

| Plataforma | Comando de instalaÃ§Ã£o |
|------------|-----------------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (detecÃ§Ã£o automÃ¡tica) ou `graphify install --platform windows` |
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

Depois abra seu assistente de cÃ³digo IA e digite:

```
/graphify .
```

Nota: Codex usa `$` em vez de `/` para habilidades, entÃ£o digite `$graphify .`.

### Fazer o assistente sempre usar o grafo (recomendado)

ApÃ³s construir um grafo, execute isso uma vez no seu projeto:

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
/graphify                          # diretÃ³rio atual
/graphify ./raw                    # pasta especÃ­fica
/graphify ./raw --mode deep        # extraÃ§Ã£o de arestas INFERRED mais agressiva
/graphify ./raw --update           # re-extrair apenas arquivos modificados
/graphify ./raw --directed         # grafo dirigido
/graphify ./raw --cluster-only     # re-executar clustering no grafo existente
/graphify ./raw --no-viz           # sem HTML, apenas relatÃ³rio + JSON
/graphify ./raw --obsidian         # gerar vault do Obsidian (opt-in)

/graphify add https://arxiv.org/abs/1706.03762   # buscar um paper
/graphify add <video-url>                         # baixar Ã¡udio, transcrever, adicionar
/graphify query "o que conecta Attention ao otimizador?"
/graphify path "DigestAuth" "Response"
/graphify explain "SwinTransformer"

graphify hook install              # instalar hooks do Git
graphify update ./src              # re-extrair arquivos de cÃ³digo, sem LLM
graphify watch ./src               # atualizaÃ§Ã£o automÃ¡tica do grafo
```

## O que vocÃª obtÃ©m

**NÃ³s deus** â€” conceitos com maior grau (por onde tudo passa)

**ConexÃµes surpreendentes** â€” classificadas por pontuaÃ§Ã£o composta. Arestas cÃ³digo-paper pontuam mais alto. Cada resultado inclui um porquÃª em linguagem natural.

**Perguntas sugeridas** â€” 4-5 perguntas que o grafo estÃ¡ em posiÃ§Ã£o Ãºnica de responder

**O "porquÃª"** â€” docstrings, comentÃ¡rios inline (`# NOTE:`, `# IMPORTANT:`, `# HACK:`, `# WHY:`), e justificativas de design extraÃ­das como nÃ³s `rationale_for`.

**PontuaÃ§Ãµes de confianÃ§a** â€” cada aresta INFERRED tem um `confidence_score` (0,0-1,0).

**Benchmark de tokens** â€” impresso automaticamente apÃ³s cada execuÃ§Ã£o. Em um corpus misto: **71,5x** menos tokens por consulta vs arquivos brutos.

**SincronizaÃ§Ã£o automÃ¡tica** (`--watch`) â€” atualiza o grafo automaticamente quando o cÃ³digo muda.

**Hooks do Git** (`graphify hook install`) â€” instala hooks post-commit e post-checkout.

## Privacidade

graphify envia conteÃºdo de arquivos para a API do modelo do seu assistente IA para extraÃ§Ã£o semÃ¢ntica de documentos, papers e imagens. Arquivos de cÃ³digo sÃ£o processados localmente via tree-sitter AST. Arquivos de vÃ­deo e Ã¡udio sÃ£o transcritos localmente com faster-whisper. Sem telemetria, sem rastreamento de uso.

## Stack tÃ©cnico

NetworkX + Leiden (graspologic) + tree-sitter + vis.js. ExtraÃ§Ã£o semÃ¢ntica via Claude, GPT-4 ou o modelo da sua plataforma. TranscriÃ§Ã£o de vÃ­deo via faster-whisper + yt-dlp (opcional).

## ConstruÃ­do sobre graphify â€” Penpax

[**Penpax**](https://safishamsi.github.io/penpax.ai) Ã© a camada enterprise sobre o graphify. Onde o graphify transforma uma pasta de arquivos em um grafo de conhecimento, o Penpax aplica o mesmo grafo a toda a sua vida profissional â€” continuamente.

**Teste gratuito em breve.** [Entrar na lista de espera â†’](https://safishamsi.github.io/penpax.ai)

## HistÃ³rico de estrelas

[![Star History Chart](https://api.star-history.com/svg?repos=safishamsi/graphify&type=Date)](https://star-history.com/#safishamsi/graphify&Date)

