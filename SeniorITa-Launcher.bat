@echo off
setlocal enabledelayedexpansion
set "PROJECT_DIR=%~dp0"
cd /d "%PROJECT_DIR%"
title SeniorITa - Console Operativa IT (%PROJECT_DIR%)
echo =======================================================
echo          SeniorITa - IT Operations Environment
echo =======================================================
echo Cartella di lavoro: %PROJECT_DIR%
echo.
powershell.exe -NoExit -ExecutionPolicy Bypass -NoLogo -Command "& { Set-Location '%PROJECT_DIR%'; Write-Host 'Protocollo SeniorITa Pronto.' -ForegroundColor Green; Write-Host 'Digita .\scripts\update-all.ps1 per sincronizzare grafo e log.' -ForegroundColor Cyan; }"
