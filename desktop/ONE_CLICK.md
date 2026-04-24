# Lucy Desktop — One-click (v1)

Right now the desktop runs in **dev mode**:

- Backend: `python backend/main.py` (FastAPI)
- Frontend: Vite dev server (`http://localhost:5173`)
- Desktop: Electron loads the Vite URL

## One-click run (Windows)

From repo root:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\run.ps1
```

## If you see `Activate.ps1 not recognized` / missing

That means your virtualenv did **not** create the activation script.
Fix:

```powershell
cd backend
rmdir .venv -Recurse -Force
py -m venv .venv
```

Then rerun `.\run.ps1` from repo root.

## Next step (true one-click app)

We will package:

- backend → `lucy-backend.exe` (PyInstaller)
- desktop → `Lucy Desktop Setup.exe` (electron-builder)

so end users do not need Python/Node installed.
