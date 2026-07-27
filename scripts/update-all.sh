#!/usr/bin/env bash
# ==============================================================================
# SeniorITa — Script di Aggiornamento Unificato (1-Click)
# ==============================================================================
set -e

echo "🔍 [1/3] Scansione ed ingestione log/correzioni..."
if [ -f "scripts/ingest-log.py" ]; then
    python scripts/ingest-log.py
else
    echo "⚠️  scripts/ingest-log.py non trovato, salto il passaggio."
fi

echo "📊 [2/3] Aggiornamento del grafo di conoscenza (Graphify)..."
if command -v graphify &> /dev/null; then
    graphify update .
else
    echo "⚠️  Graphify non installato o non presente nel PATH, salto il passaggio."
fi

echo "🚀 [3/3] Sincronizzazione con il repository GitHub..."
git add .
git commit -m "auto(update): aggiornamento automatico log e grafo del $(date +'%Y-%m-%d %H:%M')" || echo "Nessun cambiamento da salvare."
git push origin main

echo "✅ Aggiornamento completato con successo!"
