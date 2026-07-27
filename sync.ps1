# Script di sincronizzazione automatica per SeniorITA
Write-Host "🔄 Avvio generazione grafo Graphify..." -ForegroundColor Cyan

# 1. Rigenera il grafo del codice ed esporta per Obsidian
graphify . --code-only
graphify export obsidian

# 2. Assicura che la cache sia nel .gitignore
if (-not (Test-Path .gitignore) -or -not (Select-String -Path .gitignore -Pattern "graphify-out/cache/" -Quiet)) {
    Add-Content -Path .gitignore -Value "`ngraphify-out/cache/"
}

# 3. Commit e Push automatico su GitHub
Write-Host "🚀 Invio modifiche a GitHub..." -ForegroundColor Yellow
git add .
git commit -m "auto: sincronizzazione grafo Obsidian e codebase SeniorITA"
git push origin main

Write-Host "✅ Tutto completato con successo!" -ForegroundColor Green