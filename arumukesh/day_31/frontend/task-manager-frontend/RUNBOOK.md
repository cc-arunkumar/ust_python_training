# Runbook — frontend (task-manager-frontend)

Quick commands (PowerShell)

Install dependencies:

```powershell
cd c:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_31\frontend\task-manager-frontend
npm install
```

Run development server (Vite):

```powershell
cd c:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_31\frontend\task-manager-frontend
npm run dev
# If your environment doesn't expose `dev`, run `npx vite` directly
```

Build production bundle:

```powershell
cd c:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_31\frontend\task-manager-frontend
npm run build
```

Preview built bundle (serves `dist/` locally):

```powershell
cd c:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_31\frontend\task-manager-frontend
npm run preview
# Or: npx vite preview --host 127.0.0.1 --port 4173
```

Linting:

```powershell
cd c:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_31\frontend\task-manager-frontend
npm run lint
```

Backend run (for local full-stack testing)

1. Start the backend (FastAPI, uvicorn):

```powershell
cd c:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_31\backend
python -m uvicorn main:app --reload --port 8000
```

2. The frontend expects the API base URL to be `http://localhost:8000/api/v1` (configured in `src/api/axios.js`).

Notes and troubleshooting

- If `npm run preview` reports "dist does not exist", run `npm run build` first.
- If the preview URL is unreachable, try binding explicitly to 127.0.0.1 and a known free port:

```powershell
npx vite preview --host 127.0.0.1 --port 4173
```

- API endpoints are protected — unauthenticated GETs may return 401. Use the Login page to obtain a JWT, or call the backend login route to get a token.

Backups

- Original frontend and backend UI code preserved at `backups/original_frontend_src/` and `backups/original_backend_src/` at the repository root.

Contact / Next steps

- For small UX polish (toasts, loading states), run `npm run dev` and I can apply changes live.
- If you'd like, I can prepare a PR description and suggested commit message.
