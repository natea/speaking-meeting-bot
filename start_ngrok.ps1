# Start ngrok for the Speaking Meeting Bot
# Run this script in a separate terminal from the server

$ErrorActionPreference = "Stop"

Write-Host "Starting ngrok tunnels..." -ForegroundColor Green

# Set paths
$projectPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectPath

# Check if ngrok is already running
try {
    $ngrokCheck = Invoke-RestMethod -Uri "http://localhost:4040/api/tunnels" -TimeoutSec 2 -ErrorAction Stop
    Write-Host "Ngrok is already running!" -ForegroundColor Yellow
    Write-Host "Dashboard: http://localhost:4040" -ForegroundColor Cyan
    $ngrokCheck.tunnels | ForEach-Object {
        Write-Host "  $($_.public_url) -> $($_.config.addr)" -ForegroundColor Cyan
    }
    exit 0
} catch {
    Write-Host "Ngrok is not running, starting it now..." -ForegroundColor Yellow
}

# Check if config file exists
$configPath = Join-Path $projectPath "config\ngrok\config.yml"
if (-not (Test-Path $configPath)) {
    Write-Host "ERROR: Config file not found at: $configPath" -ForegroundColor Red
    exit 1
}

Write-Host "Config file: $configPath" -ForegroundColor Gray
Write-Host "Starting ngrok tunnels on ports 7014 and 7015..." -ForegroundColor Green
Write-Host "Dashboard will be available at: http://localhost:4040" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop ngrok" -ForegroundColor Yellow
Write-Host ""

# Start ngrok
ngrok start --all --config $configPath


