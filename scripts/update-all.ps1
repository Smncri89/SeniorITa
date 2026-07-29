Write-Host "=== [SeniorITa] Aggiornamento del Sistema Operativo IT ===" -ForegroundColor Cyan

if (Test-Path "scripts/ingest-log.py") {
    Write-Host "🔍 [1/3] Scansione ed ingestione log..." -ForegroundColor Cyan
    if (Get-Command "py" -ErrorAction SilentlyContinue) {
        py scripts/ingest-log.py
    } elseif (Get-Command "python" -ErrorAction SilentlyContinue) {
        python scripts/ingest-log.py
    }
}

if (Get-Command "graphify" -ErrorAction SilentlyContinue) {
    Write-Host "--> [2/3] Aggiornamento del grafo di conoscenza Graphify..." -ForegroundColor Yellow
    graphify update .
} else {
    Write-Host "--> [WARN] Graphify non trovato nel PATH. Saltato." -ForegroundColor Red
}

Write-Host "🚀 [3/3] Sincronizzazione con GitHub..." -ForegroundColor Cyan
git add .

$today = Get-Date -Format "yyyy-MM-dd HH:mm"
git commit -m "feat(seniorita): auto-update kb, logs & graph report ($today)"
git push origin main

Write-Host "=== [SeniorITa] Aggiornamento Completato con Successo! ===" -ForegroundColor Green
