Write-Host "🔍 [1/3] Scansione ed ingestione log..." -ForegroundColor Cyan
if (Test-Path "scripts/ingest-log.py") {
    python scripts/ingest-log.py
}

Write-Host "📊 [2/3] Aggiornamento del grafo di conoscenza (Graphify)..." -ForegroundColor Cyan
if (Get-Command "graphify" -ErrorAction SilentlyContinue) {
    graphify update .
}

Write-Host "🚀 [3/3] Sincronizzazione con GitHub..." -ForegroundColor Cyan
git add .
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
git commit -m "auto(update): aggiornamento automatico log e grafo del $timestamp"
git push origin main

Write-Host "✅ Aggiornamento completato con successo!" -ForegroundColor Green
