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

**Keterampilan untuk asisten kode AI.** Ketik `/graphify` di Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro, atau Google Antigravity â€” membaca file Anda, membangun graf pengetahuan, dan mengembalikan struktur yang tidak Anda ketahui ada. Pahami codebase lebih cepat. Temukan "mengapa" di balik keputusan arsitektur.

Sepenuhnya multimodal. Tambahkan kode, PDF, markdown, tangkapan layar, diagram, foto papan tulis, gambar dalam bahasa lain, atau file video dan audio â€” graphify mengekstrak konsep dan hubungan dari semuanya dan menghubungkannya dalam satu graf. Video ditranskrip secara lokal dengan Whisper. Mendukung 25 bahasa pemrograman melalui tree-sitter AST.

> Andrej Karpathy memelihara folder `/raw` tempat ia menyimpan makalah, tweet, tangkapan layar, dan catatan. graphify adalah jawaban untuk masalah itu â€” **71,5x** lebih sedikit token per kueri dibandingkan membaca file mentah, persisten di antara sesi.

```
/graphify .
```

```
graphify-out/
â”œâ”€â”€ graph.html       graf interaktif â€” buka di browser mana saja
â”œâ”€â”€ GRAPH_REPORT.md  node dewa, koneksi mengejutkan, pertanyaan yang disarankan
â”œâ”€â”€ graph.json       graf persisten â€” dapat dikueri berminggu-minggu kemudian
â””â”€â”€ cache/           cache SHA256 â€” pengulangan hanya memproses file yang berubah
```

## Cara Kerja

graphify bekerja dalam tiga tahap. Pertama, tahap AST deterministik mengekstrak struktur dari file kode tanpa LLM. Kemudian file video dan audio ditranskrip secara lokal dengan faster-whisper. Terakhir, sub-agen Claude berjalan secara paralel pada dokumen, makalah, gambar, dan transkripsi. Hasilnya digabungkan ke dalam graf NetworkX, dikelompokkan dengan Leiden, dan diekspor sebagai HTML interaktif, JSON yang dapat dikueri, dan laporan audit.

Setiap hubungan diberi label `EXTRACTED`, `INFERRED` (dengan skor kepercayaan), atau `AMBIGUOUS`.

## Instalasi

**Persyaratan:** Python 3.10+ dan salah satu dari: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com) dan lainnya.

```bash
uv tool install graphifyy && graphify install
# atau dengan pipx
pipx install graphifyy && graphify install
# atau pip
pip install graphifyy && graphify install
```

> **Paket resmi:** Paket PyPI bernama `graphifyy`. Satu-satunya repositori resmi adalah [safishamsi/graphify](https://github.com/safishamsi/graphify).

## Penggunaan

```
/graphify .
/graphify ./raw --update
/graphify query "apa yang menghubungkan Attention dengan optimizer?"
/graphify path "DigestAuth" "Response"
graphify hook install
graphify update ./src
```

## Apa yang Anda Dapatkan

**Node dewa** â€” konsep dengan derajat tertinggi Â· **Koneksi mengejutkan** â€” diurutkan berdasarkan skor Â· **Pertanyaan yang disarankan** Â· **"Mengapa"** â€” docstring dan alasan desain diekstrak sebagai node Â· **Benchmark token** â€” **71,5x** lebih sedikit token pada corpus campuran.

## Privasi

File kode diproses secara lokal melalui tree-sitter AST. Video ditranskrip secara lokal dengan faster-whisper. Tidak ada telemetri.

## Dibangun di atas graphify â€” Penpax

[**Penpax**](https://safishamsi.github.io/penpax.ai) adalah lapisan enterprise di atas graphify. **Uji coba gratis segera hadir.** [Bergabunglah dengan daftar tunggu â†’](https://safishamsi.github.io/penpax.ai)

[![Star History Chart](https://api.star-history.com/svg?repos=safishamsi/graphify&type=Date)](https://star-history.com/#safishamsi/graphify&Date)

