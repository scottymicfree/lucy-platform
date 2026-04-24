# One-click Windows start (no PowerShell policy issues)

If PowerShell blocks `run.ps1` (unsigned scripts), use the **batch launcher** instead.

## One click

Double-click:

- `run.bat`

It opens three terminal windows:

1) Backend (FastAPI) on `http://127.0.0.1:8000`
2) Frontend (Vite) on `http://localhost:5173`
3) Desktop (Electron)

## Requirements

- Node.js 20.x installed (so `npm` works)
- Python installed with the Windows launcher `py`

## Troubleshooting

- If `py` is not found, install Python from python.org (3.11/3.12 recommended) and include the launcher.
- If ports are busy, set `LUCY_API_PORT` in `backend/.env`.
