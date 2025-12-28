$ErrorActionPreference = "Stop"

Write-Host "=== Speaking Meeting Bot: Local Dev Startup ==="

$projectPath = Split-Path -Parent $PSScriptRoot
Set-Location $projectPath

if (-not (Get-Command ngrok -ErrorAction SilentlyContinue)) {
    Write-Error "ngrok not found in PATH. Install ngrok and try again."
    exit 1
}

$ngrokProcess = Get-Process ngrok -ErrorAction SilentlyContinue
if (-not $ngrokProcess) {
    Write-Host "Starting ngrok tunnel on port 7014..."
    Start-Process -FilePath ngrok -ArgumentList "http 7014" -NoNewWindow
    Start-Sleep -Seconds 2
}

$ngrokUrl = $null
for ($i = 0; $i -lt 20 -and -not $ngrokUrl; $i++) {
    try {
        $tunnels = Invoke-RestMethod -Uri "http://localhost:4040/api/tunnels" -TimeoutSec 2
        $ngrokUrl = ($tunnels.tunnels | Where-Object { $_.proto -eq "https" } | Select-Object -First 1).public_url
    } catch {
        Start-Sleep -Seconds 1
    }
}

if (-not $ngrokUrl) {
    Write-Error "Failed to detect ngrok URL from http://localhost:4040/api/tunnels"
    exit 1
}

Write-Host "ngrok URL: $ngrokUrl"

$envPath = Join-Path $projectPath ".env"
if (-not (Test-Path $envPath)) {
    $examplePath = Join-Path $projectPath ".env.example"
    if (Test-Path $examplePath) {
        Copy-Item $examplePath $envPath
    }
}

if (Test-Path $envPath) {
    $envContent = Get-Content $envPath
    if ($envContent -match "^BASE_URL=") {
        $envContent = $envContent -replace "^BASE_URL=.*$", "BASE_URL=$ngrokUrl"
    } else {
        $envContent += "BASE_URL=$ngrokUrl"
    }
    Set-Content -Path $envPath -Value $envContent
}

$cursorPath = Join-Path $projectPath ".cursor"
if (-not (Test-Path $cursorPath)) {
    New-Item -ItemType Directory -Path $cursorPath | Out-Null
}

Write-Host "Starting API server..."
$pythonPath = Join-Path $projectPath ".venv\\Scripts\\python.exe"
Start-Process -FilePath $pythonPath `
    -ArgumentList "-m uvicorn app:app --host 0.0.0.0 --port 7014" `
    -WorkingDirectory $projectPath `
    -RedirectStandardOutput (Join-Path $cursorPath "uvicorn.out.log") `
    -RedirectStandardError (Join-Path $cursorPath "uvicorn.err.log") `
    -NoNewWindow

Write-Host "Waiting for health check..."
$healthy = $false
for ($i = 0; $i -lt 20 -and -not $healthy; $i++) {
    try {
        $health = Invoke-RestMethod -Uri "http://localhost:7014/health" -TimeoutSec 2
        if ($health) { $healthy = $true }
    } catch {
        Start-Sleep -Seconds 1
    }
}

if ($healthy) {
    Write-Host "Local health check OK."
} else {
    Write-Warning "Local health check did not respond."
}

try {
    $publicHealth = Invoke-RestMethod -Uri "$ngrokUrl/health" -TimeoutSec 3
    if ($publicHealth) {
        Write-Host "Public health check OK."
    }
} catch {
    Write-Warning "Public health check failed. The tunnel may not be reachable."
}

Write-Host "Logs: .cursor\\uvicorn.out.log and .cursor\\uvicorn.err.log"
