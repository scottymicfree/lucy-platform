@echo off
setlocal enabledelayedexpansion

REM Lucy Platform - One click dev launcher for Windows
REM - avoids PowerShell execution policy issues
REM - uses Python launcher 'py' and Node/npm

cd /d "%~dp0"

echo [lucy] repo root: %cd%

REM 1) Start backend in a new window
echo [lucy] starting backend...
start "Lucy Backend" cmd /k "cd backend && py -m venv .venv && call .venv\Scripts\activate.bat && pip install -r requirements.txt && if not exist .env copy .env.example .env && py -m backend.main"

REM 2) Ensure frontend deps and start Vite
echo [lucy] starting frontend...
start "Lucy Frontend" cmd /k "cd frontend && if not exist node_modules npm install && npm run dev"

REM 3) Ensure desktop deps and start Electron
echo [lucy] starting desktop...
start "Lucy Desktop" cmd /k "cd desktop && if not exist node_modules npm install && npm start"

echo [lucy] launched. If desktop shows 'failed to fetch', wait for backend to finish starting.
endlocal
