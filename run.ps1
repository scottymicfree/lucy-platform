# Run Lucy Platform (dev) on Windows

$ErrorActionPreference = 'Stop'

function Ensure-LocalVenv {
  param([string]$BackendDir)

  $venvDir = Join-Path $BackendDir ".venv"
  $activate = Join-Path $venvDir "Scripts\Activate.ps1"
  $pythonExe = Join-Path $venvDir "Scripts\python.exe"

  if (!(Test-Path $venvDir)) {
    Write-Host "[backend] creating venv..." -ForegroundColor Cyan
    Push-Location $BackendDir
    try {
      # Use the launcher if available (more reliable on Windows Store Python).
      if (Get-Command py -ErrorAction SilentlyContinue) {
        py -m venv .venv
      } else {
        python -m venv .venv
      }
    } finally {
      Pop-Location
    }
  }

  if (!(Test-Path $activate)) {
    throw "[backend] venv activation script not found: $activate`nYour venv may not have been created correctly. Try deleting '$venvDir' and rerun."
  }

  return @{ Activate = $activate; Python = $pythonExe }
}

$repoRoot = $PSScriptRoot
$backendDir = Join-Path $repoRoot "backend"
$desktopDir = Join-Path $repoRoot "desktop"
$frontendDir = Join-Path $repoRoot "frontend"

# 1) Backend
$venv = Ensure-LocalVenv -BackendDir $backendDir

Write-Host "[backend] activating venv..." -ForegroundColor Cyan
. $venv.Activate

Write-Host "[backend] installing python deps..." -ForegroundColor Cyan
pip install -r (Join-Path $backendDir "requirements.txt")

if (!(Test-Path (Join-Path $backendDir ".env"))) {
  Copy-Item (Join-Path $backendDir ".env.example") (Join-Path $backendDir ".env")
}

Write-Host "[backend] starting API (new window)..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$backendDir'; . '$($venv.Activate)'; python main.py"

# 2) Desktop + Frontend
Write-Host "[desktop] ensuring node deps..." -ForegroundColor Cyan
Push-Location $desktopDir
try {
  if (!(Test-Path "node_modules")) { npm install }
} finally { Pop-Location }

Write-Host "[frontend] ensuring node deps..." -ForegroundColor Cyan
Push-Location $frontendDir
try {
  if (!(Test-Path "node_modules")) { npm install }
} finally { Pop-Location }

Write-Host "[desktop] starting dev orchestrator (this window)..." -ForegroundColor Cyan
Push-Location $desktopDir
try {
  node dev.mjs
} finally { Pop-Location }
