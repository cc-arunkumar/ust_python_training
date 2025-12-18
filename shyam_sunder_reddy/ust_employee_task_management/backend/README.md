# Backend - quick start

This folder contains the FastAPI backend for the UST Employee Task Management app.

Run locally (Windows PowerShell):

1. Start the backend (from the `backend` folder):

   cd d:\ust_python_training\shyam_sunder_reddy\ust_employee_task_management\backend; python -m uvicorn main:app --reload --port 8000

2. Start the frontend (from the repository root):

   cd d:\ust_python_training\shyam_sunder_reddy\ust_employee_task_management\frontend; npm install; npm run dev

Notes

- The backend listens on http://127.0.0.1:8000. The frontend dev server uses Vite and may pick ports 5173 or 5174; the backend CORS list includes both 5173 and 5174.
- The app expects a running MySQL instance reachable at the URL in `database/sql_db.py` (default: mysql+pymysql://root:password123@localhost:3306/ust_task_db).
- If you need to change ports or DB connection, edit `main.py` (CORS origins) or `database/sql_db.py`.

If you want, I can also add npm scripts or a single-start script to start both servers together.
