# Start the Speaking Meeting Bot Server
# Run this script to start the server

$ErrorActionPreference = "Stop"

Write-Host "Starting Speaking Meeting Bot Server..." -ForegroundColor Green

# Set paths
$projectPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectPath

# Add Poetry to PATH
$env:Path += ";$env:USERPROFILE\AppData\Roaming\Python\Scripts"
$env:PYTHONPATH = $projectPath

# Check if server is already running
$portCheck = Test-NetConnection -ComputerName localhost -Port 7014 -WarningAction SilentlyContinue
if ($portCheck.TcpTestSucceeded) {
    Write-Host "Server is already running on port 7014!" -ForegroundColor Yellow
    Write-Host "Access it at: http://localhost:7014" -ForegroundColor Cyan
    Write-Host "API Docs: http://localhost:7014/docs" -ForegroundColor Cyan
    exit 0
}

# Start the server
Write-Host "Starting server on port 7014..." -ForegroundColor Green
Write-Host "Note: Make sure ngrok is running in another terminal:" -ForegroundColor Yellow
Write-Host "  ngrok start --all --config config\ngrok\config.yml" -ForegroundColor Cyan
Write-Host ""
poetry run python app/main.py --port 7014 --local-dev

