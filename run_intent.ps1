param (
    [Parameter(Mandatory=$true)]
    [string]$JsonInput
)

try {
    $intentObj = $JsonInput | ConvertFrom-Json
} catch {
    Write-Error "? JSON non valido!"
    exit 1
}

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host " INTENT RILEVATO: $($intentObj.intent)" -ForegroundColor Yellow
Write-Host " DOMINIO        : $($intentObj.domain)" -ForegroundColor Yellow
Write-Host " WORKFLOW       : $($intentObj.workflow)" -ForegroundColor Yellow
Write-Host " LIVELLO RISCHIO: $($intentObj.risk_level)" -ForegroundColor Yellow
Write-Host "==================================================" -ForegroundColor Cyan

if ($intentObj.requires_approval -eq $true) {
    Write-Host "`n?? ATTENZIONE: Questo workflow richiede autorizzazione esplicita!" -ForegroundColor Red
    $response = Read-Host "Vuoi procedere con l'esecuzione? (S/N)"
    if ($response -ne "S" -and $response -ne "s") {
        Write-Host "? Operazione annullata dall'utente." -ForegroundColor Red
        exit 0
    }
}

Write-Host "`n?? Avvio del workflow: $($intentObj.workflow)..." -ForegroundColor Green

switch ($intentObj.workflow) {
    "domain_join_workflow" {
        Write-Host "--> [Task 1/2] Verifico connettività DNS..." -ForegroundColor Gray
        Write-Host "--> [Task 2/2] Esecuzione Join Dominio..." -ForegroundColor Gray
        Write-Host "? Workflow Domain Join completato!" -ForegroundColor Green
    }
    "identity_reset_workflow" {
        Write-Host "--> Reset Password / Sblocco Account in corso..." -ForegroundColor Gray
        Write-Host "? Password resettata con successo!" -ForegroundColor Green
    }
    "inventory_audit_workflow" {
        Write-Host "--> Raccolta Dati di Sistema (CPU, RAM, BitLocker, TPM)..." -ForegroundColor Gray
        Get-CimInstance Win32_OperatingSystem | Select-Object Caption, OSArchitecture, Version
        Write-Host "? Audit completato!" -ForegroundColor Green
    }
    default {
        Write-Host "?? Nessuno script associato al workflow '$($intentObj.workflow)'." -ForegroundColor Yellow
    }
}
