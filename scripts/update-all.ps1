[CmdletBinding()]
param()

$ProjectRoot = Resolve-Path "$PSScriptRoot\.."
Set-Location $ProjectRoot

Write-Host "=== [SeniorITa] Aggiornamento del Sistema Operativo IT ===" -ForegroundColor Cyan
Write-Host "Cartella operativa: $ProjectRoot" -ForegroundColor DarkGray

if (Test-Path "$ProjectRoot\.env.local") {
    Get-Content "$ProjectRoot\.env.local" | ForEach-Object {
        if ($_ -match "^\s*([^#=]+)\s*=\s*(.*)$") {
            [System.Environment]::SetEnvironmentVariable($matches[1].Trim(), $matches[2].Trim(), "Process")
        }
    }
    Write-Host "--> Variabili caricate da .env.local" -ForegroundColor Green
}

Write-Host "🔍 [1/3] Scansione ed ingestione log..." -ForegroundColor Cyan
if (Test-Path "$ProjectRoot\scripts\ingest-log.py") {
    if (Get-Command "py" -ErrorAction SilentlyContinue) {
        py "$ProjectRoot\scripts\ingest-log.py"
    } elseif (Get-Command "python" -ErrorAction SilentlyContinue) {
        python "$ProjectRoot\scripts\ingest-log.py"
    }
}

Write-Host "🧠 [2/3] Aggiornamento mappa Graphify..." -ForegroundColor Cyan
if (Get-Command "graphify" -ErrorAction SilentlyContinue) {
    graphify update .
}

Write-Host "🚀 [3/3] Sincronizzazione con GitHub..." -ForegroundColor Cyan
if (Test-Path "$ProjectRoot\.git") {
    git add .
    $today = Get-Date -Format "yyyy-MM-dd HH:mm"
    git commit -m "feat(seniorita): portable launcher & dynamic paths for C:\ and USB ($today)"
    git push origin main
}
Write-Host "=== [SeniorITa] Aggiornamento Completato con Successo! ===" -ForegroundColor Green
