# Task Manager Frontend

This folder contains the consolidated React + Vite frontend for the Task Manager app.

Quick commands

```powershell
# Install dependencies (if not already done)
npm install

# Run dev server
npm run dev

# Build production bundle
npm run build

# Preview built bundle (serves `dist/` locally)
npm run preview
```

Notes

- API base URL used by the frontend: `http://localhost:8000/api/v1` (axios instance in `src/api/axios.js`).
- Auth: JWT stored in `localStorage` under `token`; `AuthContext` sets Authorization header for axios.
- Backups of the original UIs (before consolidation) are available under the repository `backups/` directory at the project root.

Changed files (high level)

- Replaced duplicate UIs and consolidated a new frontend under `frontend/task-manager-frontend/src/`.
- Key files added/updated: `src/context/AuthContext.jsx`, `src/api/*`, `src/pages/*`, `src/components/*` (Login, Navbar, Sidebar, Dashboard, Kanban).

If you want, I can:

- Run ESLint and fix any remaining findings (already run and fixed in this branch).
- Start a preview server and do a short smoke test (login, fetch employees, open Kanban).

Contact

- For restore or rollback, use the backups under `backups/original_frontend_src` and `backups/original_backend_src`.

# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) (or [oxc](https://oxc.rs) when used in [rolldown-vite](https://vite.dev/guide/rolldown)) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.
