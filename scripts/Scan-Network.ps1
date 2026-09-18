[CmdletBinding()]
param(
    [switch]$QuickScan,
    [string]$ExportBaseName = "Report_Rete_VPN"
)

Write-Host ""
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host " [TOOL] Scansione Completa Rete LAN / Wi-Fi & VPN" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

$DesktopPath = [Environment]::GetFolderPath('Desktop')
$Timestamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$FileBase = Join-Path -Path $DesktopPath -ChildPath "${ExportBaseName}_$Timestamp"
$CacheFile = Join-Path -Path $env:TEMP -ChildPath "mac_oui_cache.json"

# --- CACHE OUI ---
$MacCache = @{}
if (Test-Path -Path $CacheFile) {
    try {
        $JsonData = Get-Content -Path $CacheFile -Raw | ConvertFrom-Json
        foreach ($prop in $JsonData.PSObject.Properties) { 
            $MacCache[$prop.Name] = $prop.Value 
        }
    } catch {}
}

function Resolve-MacVendor([string]$Mac) {
    if ([string]::IsNullOrWhiteSpace($Mac) -or $Mac -eq "N/A") { return "N/A" }
    $Clean = ($Mac -replace "[:-]", "").ToUpper()
    if ($Clean.Length -lt 6) { return "Sconosciuto" }
    $Oui = $Clean.Substring(0, 6)
    if ($MacCache.ContainsKey($Oui)) { return $MacCache[$Oui] }
    
    $Vendor = "Sconosciuto"
    try {
        $res = Invoke-RestMethod -Uri "https://api.macvendors.com/$Oui" -Method Get -TimeoutSec 2 -ErrorAction Stop
        if ($res) { $Vendor = $res.Trim() }
    } catch { 
        $Vendor = "Sconosciuto" 
    }

    $MacCache[$Oui] = $Vendor
    try { 
        $MacCache | ConvertTo-Json | Set-Content -Path $CacheFile -Force 
    } catch {}
    return $Vendor
}

# --- 1. PING SWEEP ASINCRONO ---
Write-Host "[1/3] Scansione dispositivi attivi sulle interfacce..." -ForegroundColor Yellow
$ActiveIPs = Get-NetIPAddress -AddressFamily IPv4 -ErrorAction SilentlyContinue | Where-Object {
    $_.IPAddress -notlike "127.*" -and $_.IPAddress -notlike "169.254.*" -and $_.SkipAsSource -ne $true
}

foreach ($ipObj in $ActiveIPs) {
    $parts = $ipObj.IPAddress.Split('.')
    if ($parts.Count -eq 4) {
        $subnet = "$($parts[0]).$($parts[1]).$($parts[2])"
        1..254 | ForEach-Object {
            $p = New-Object System.Net.NetworkInformation.Ping
            [void]$p.SendAsync("$subnet.$_", 60)
        }
    }
}
Start-Sleep -Seconds 2

# --- 2. RACCOLTA NEIGHBORS / ARP ---
Write-Host "[2/3] Risoluzione HostName e produttori MAC OUI..." -ForegroundColor Yellow
$Neighbors = Get-NetNeighbor -AddressFamily IPv4 -ErrorAction SilentlyContinue | Where-Object {
    $_.State -in 'Reachable','Stale','Delay','Probe' -and
    $_.IPAddress -notlike "127.*" -and 
    $_.IPAddress -notlike "169.254.*" -and
    $_.IPAddress -notlike "224.*" -and 
    $_.IPAddress -notlike "239.*" -and 
    $_.IPAddress -ne "255.255.255.255"
}

$Dispositivi = @()
foreach ($n in $Neighbors) {
    $mac = $n.LinkLayerAddress
    if ([string]::IsNullOrWhiteSpace($mac) -or $mac -eq "00-00-00-00-00-00") { continue }
    
    $hostName = "N/A"
    try {
        $entry = [System.Net.Dns]::GetHostEntry($n.IPAddress)
        if ($entry.HostName) { $hostName = $entry.HostName }
    } catch { 
        $hostName = "Non risolto" 
    }
    
    $iface = $n.InterfaceAlias
    if (-not $iface) {
        $iface = (Get-NetAdapter -InterfaceIndex $n.InterfaceIndex -ErrorAction SilentlyContinue).Name
    }

    $Dispositivi += [PSCustomObject]@{
        IPAddress   = $n.IPAddress
        HostName    = $hostName
        MACAddress  = $mac
        Produttore  = (Resolve-MacVendor $mac)
        Interfaccia = $iface
        Stato       = $n.State
    }
}

# --- 3. VERIFICA STATO VPN ---
Write-Host "[3/3] Verifica connessioni VPN e schede virtuali..." -ForegroundColor Yellow
$VpnList = @()
try {
    foreach ($vpn in (Get-VpnConnection -ErrorAction SilentlyContinue)) {
        $VpnList += [PSCustomObject]@{
            Nome     = $vpn.Name
            Tipo     = "Client Windows (RAS)"
            Stato    = $vpn.ConnectionStatus
            Dettagli = $vpn.ServerAddress
        }
    }
} catch {}

$TunnelAdapters = Get-NetAdapter -ErrorAction SilentlyContinue | Where-Object {
    $_.InterfaceDescription -match 'WireGuard|TAP|TUN|VPN|Cisco|Fortinet|Palo Alto|CheckPoint|NordVPN|Proton|OpenVPN|Virtual' -or
    $_.Name -match 'WireGuard|TAP|TUN|VPN'
}
foreach ($ad in $TunnelAdapters) {
    $VpnList += [PSCustomObject]@{
        Nome     = $ad.Name
        Tipo     = "Interfaccia Virtuale/Tunnel"
        Stato    = $ad.Status
        Dettagli = $ad.InterfaceDescription
    }
}

# --- OUTPUT CONSOLE IMMEDIATO ---
Write-Host ""
Write-Host ">>> STATO CONNESSIONI VPN <<<" -ForegroundColor Green
if ($VpnList.Count -gt 0) {
    $VpnList | Format-Table Nome, Tipo, Stato, Dettagli -AutoSize
} else {
    Write-Host "Nessuna VPN o interfaccia tunnel attiva rilevata." -ForegroundColor DarkGray
}

Write-Host ""
Write-Host ">>> DISPOSITIVI CONNESSI ($($Dispositivi.Count) trovati) <<<" -ForegroundColor Green
if ($Dispositivi.Count -gt 0) {
    $Dispositivi | Format-Table IPAddress, HostName, MACAddress, Produttore, Interfaccia -AutoSize
} else {
    Write-Host "Nessun dispositivo rilevato nella tabella ARP." -ForegroundColor Red
}

# --- ESPORTAZIONI SUL DESKTOP ---
$Dispositivi | Export-Csv -Path "$FileBase.csv" -NoTypeInformation -Encoding UTF8
$Dispositivi | ConvertTo-Json -Depth 3 | Set-Content -Path "$FileBase.json" -Encoding UTF8
$Dispositivi | Export-Clixml -Path "$FileBase.xml"

# TXT
$txtLines = @(
    "================================================================================",
    "REPORT RETE E VPN - $(Get-Date -Format 'dd/MM/yyyy HH:mm:ss')",
    "================================================================================",
    "",
    "--- VPN ---",
    ($VpnList | Format-Table -AutoSize | Out-String),
    "",
    "--- DISPOSITIVI ---",
    ($Dispositivi | Format-Table -AutoSize | Out-String)
)
$txtLines | Set-Content -Path "$FileBase.txt" -Encoding UTF8

# HTML
$htmlBody = "<h1>Report Scansione Rete e VPN</h1><p>Data: $(Get-Date -Format 'dd/MM/yyyy HH:mm:ss')</p>"
$htmlBody += "<h2>Stato VPN</h2>" + ($VpnList | ConvertTo-Html -Fragment)
$htmlBody += "<h2>Dispositivi Rilevati</h2>" + ($Dispositivi | ConvertTo-Html -Fragment)
$htmlFull = "<html><head><meta charset='UTF-8'><style>body{font-family:Segoe UI,sans-serif;margin:20px;background:#f9f9f9}table{border-collapse:collapse;width:100%;margin-bottom:20px;background:#fff}th,td{padding:8px 12px;border:1px solid #ddd;text-align:left}th{background:#0066cc;color:#fff}tr:nth-child(even){background:#f2f2f2}</style></head><body>$htmlBody</body></html>"
$htmlFull | Set-Content -Path "$FileBase.html" -Encoding UTF8

Write-Host ""
Write-Host "[OK] Report generati sul Desktop:" -ForegroundColor Cyan
Write-Host "     $FileBase.* (CSV, JSON, XML, TXT, HTML)" -ForegroundColor Cyan
Start-Process -FilePath "$FileBase.html"
