# Configure and start ngrok for Speaking Meeting Bot
# This script will help you set up ngrok

$ErrorActionPreference = "Stop"

Write-Host "=== Ngrok Setup for Speaking Meeting Bot ===" -ForegroundColor Green
Write-Host ""

# Set paths
$projectPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectPath

# Check if authtoken is in .env
$env:Path += ";$env:USERPROFILE\AppData\Roaming\Python\Scripts"
$token = poetry run python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('NGROK_AUTHTOKEN', ''))" 2>$null

if ($token -and $token -ne "your_ngrok_auth_token_here" -and $token.Trim() -ne "") {
    Write-Host "Found NGROK_AUTHTOKEN in .env file" -ForegroundColor Green
    Write-Host "Configuring ngrok..." -ForegroundColor Yellow
    ngrok config add-authtoken $token.Trim()
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Ngrok authtoken configured successfully!" -ForegroundColor Green
    } else {
        Write-Host "Failed to configure ngrok authtoken" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "NGROK_AUTHTOKEN not found in .env file" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Please:" -ForegroundColor Yellow
    Write-Host "1. Get your authtoken from: https://dashboard.ngrok.com/get-started/your-authtoken" -ForegroundColor Cyan
    Write-Host "2. Add it to your .env file as: NGROK_AUTHTOKEN=your_token_here" -ForegroundColor Cyan
    Write-Host "3. Or run manually: ngrok config add-authtoken YOUR_TOKEN" -ForegroundColor Cyan
    Write-Host ""
    $manualToken = Read-Host "Or enter your ngrok authtoken now (press Enter to skip)"
    if ($manualToken -and $manualToken.Trim() -ne "") {
        ngrok config add-authtoken $manualToken.Trim()
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Ngrok authtoken configured successfully!" -ForegroundColor Green
        } else {
            Write-Host "Failed to configure ngrok authtoken" -ForegroundColor Red
            exit 1
        }
    } else {
        Write-Host "Skipping authtoken configuration" -ForegroundColor Yellow
        exit 1
    }
}

Write-Host ""
Write-Host "Starting ngrok tunnels..." -ForegroundColor Green
Write-Host "Dashboard will be available at: http://localhost:4040" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop ngrok" -ForegroundColor Yellow
Write-Host ""

$configPath = Join-Path $projectPath "config\ngrok\config.yml"
ngrok start --all --config $configPath


