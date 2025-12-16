# UST Task Manager Backend

## Stack
- FastAPI, Pydantic v2
- SQLAlchemy (MySQL via PyMySQL)
- MongoDB (Users)
- Auth: JWT (python-jose), Argon2
- Logging: Rotating file + SQL logs table

## Run
1. Fill `.env`
2. Install deps: `pip install -r requirements.txt`
3. Start MongoDB and MySQL
4. Create MySQL database `ust_task_db`
5. Run the app: `uvicorn app.main:app --reload`

## Roles and capabilities
- Admin:
  - Full CRUD on employees and tasks
  - Cannot review tasks (not enforced explicitly; “review” is a task field that managers use)
- Manager:
  - Create/assign tasks
  - Update tasks for employees under them
  - Review tasks for their direct reports or tasks assigned to them
  - Limited updates on employees (designation only for direct reports)
- Employee:
  - View assigned tasks
  - Update own task status and remark
  - Update own profile (name, email, designation)

## Endpoints
- Users:
  - POST /api/users/login
  - POST /api/users
  - PUT /api/users/{user_id}
  - DELETE /api/users/{user_id}
  - PATCH /api/users/{user_id}/status
  - GET /api/users/{user_id}
- Employees:
  - GET /api/employees
  - GET /api/employees/{emp_id}
  - POST /api/employees
  - PUT /api/employees/{emp_id}
  - DELETE /api/employees/{emp_id}
- Tasks:
  - GET /api/tasks
  - GET /api/tasks/{task_id}
  - POST /api/tasks
  - PUT /api/tasks/{task_id}
  - DELETE /api/tasks/{task_id}
- Utils:
  - POST /api/utils/upload

## Notes
- Pydantic v2 syntax is used for schema classes.
- JWT embeds `sub` (UserId), `role`, and `status`.
- Users are stored in MongoDB; employees and tasks in MySQL.
- Logs are stored in both a rotating file and SQL `logs` table.
