# Run Lucy Platform (dev) on Windows

# 1) Start backend
Set-Location -Path "$PSScriptRoot\backend"
if (!(Test-Path ".venv")) {
  python -m venv .venv
}
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
if (!(Test-Path ".env")) {
  Copy-Item .env.example .env
}
Start-Process powershell -ArgumentList "-NoExit", "-Command", "python main.py"

# 2) Start frontend + electron
Set-Location -Path "$PSScriptRoot\desktop"
if (!(Test-Path "node_modules")) {
  npm install
}
Set-Location -Path "$PSScriptRoot\frontend"
if (!(Test-Path "node_modules")) {
  npm install
}
Set-Location -Path "$PSScriptRoot\desktop"
node dev.mjs
