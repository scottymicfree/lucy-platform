# Lucy Platform — Single-Repo Build

This repository is the **single main repo** for the Lucy Platform hub.

## What’s in here

- `docs/` — canonical architecture specs and process checklists
- `backend/` — unified backend implementation (EventBus + NodeMesh + Emma/LucyPrime + API)
- `frontend/` — Vite/React Twin Earth dashboard (optional; can run standalone or as desktop shell later)

## Quick start (local)

### Backend

```bash
cd backend
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python main.py
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Canonical specs

- `docs/architecture/ENHANCED_LUCY_MIND_UNIFIED_BUILD_SPEC.md`
- `docs/architecture/LUCY_137_NODE_SYSTEM.md`
- `docs/process/MERGE_REVIEW_CHECKLIST.md`
