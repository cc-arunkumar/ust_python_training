# Changelog

All notable changes made during the UI consolidation and cleanup are recorded here.

## 2025-12-18 — Consolidated UI, build & lint

- Consolidated two UIs into a single professional frontend at `frontend/task-manager-frontend/src/`.
- Backups of original UI code placed under the repository `backups/` folder:
  - `backups/original_frontend_src/` — original frontend `src` files
  - `backups/original_backend_src/` — original backend `src` UI files
- Implemented `AuthContext` and preserved API wrapper function signatures (e.g. `getEmployees`, `createEmployee`, `loginUser`, `getTasks`, `updateTaskStatus`).
- Fixed multiple ESLint issues (hook usage, unused variables, catch blocks) and ensured a clean production build.
- Built production bundle with Vite; `dist/` produced successfully.

### Known issues / notes

- Preview server startup was attempted and Vite reported the preview URL (typically http://127.0.0.1:4173/), but probes in this environment sometimes failed to connect. The build artifacts are valid — if you cannot reach the preview, run the preview locally via the runbook commands below.
- Backend API endpoints are protected; unauthenticated probes to `/api/v1/tasks` returned 401 Unauthorized as expected.

## How to revert

- Restore the original frontend UI by copying files from `backups/original_frontend_src/` back into `frontend/task-manager-frontend/src/`.
  (Or restore original backend UI from `backups/original_backend_src/`.)
