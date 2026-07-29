Write-Host "======================================"
Write-Host " SeniorITa Environment Setup"
Write-Host "======================================"


Write-Host ""
Write-Host "[1] Checking Python..."

python --version


Write-Host ""
Write-Host "[2] Creating virtual environment..."

if (!(Test-Path ".venv")) {

    python -m venv .venv

}
else {

    Write-Host ".venv already exists"

}


Write-Host ""
Write-Host "[3] Activating environment..."

.\.venv\Scripts\Activate.ps1


Write-Host ""
Write-Host "[4] Installing dependencies..."

python -m pip install --upgrade pip

pip install -r requirements.txt


Write-Host ""
Write-Host "[5] Testing SeniorITa Engine..."

pytest


Write-Host ""
Write-Host "======================================"
Write-Host " SeniorITa READY"
Write-Host "======================================"