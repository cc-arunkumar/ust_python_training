📌 UST Task Manager – Task Tracker API (Phase 1)

A simple JWT-secured Task Tracker API built using FastAPI + Python, with in-memory storage and full CRUD operations on tasks.

This project is part of the UST Full Stack Developer Training program.

🚀 Features
🔐 Authentication

POST /login

Hardcoded user:

{
  "username": "rahul",
  "password": "password123"
}


Returns a JWT access token (HS256)

All other endpoints require:

Authorization: Bearer <token>

📋 Task Operations (CRUD)
1️⃣ Create Task

POST /tasks

Creates a new task

Auto-increment id

completed defaults to false

2️⃣ Get All Tasks

GET /tasks

3️⃣ Get Single Task

GET /tasks/{task_id}

4️⃣ Update Task

PUT /tasks/{task_id}

5️⃣ Delete Task

DELETE /tasks/{task_id}

🗂 In-Memory Storage Structure

Tasks are stored in memory as a Python list:

tasks = [
  { "id": 1, "title": "...", "description": "...", "completed": false }
]


No database is used in Phase 1.

🔧 Tech Stack

Python 3.12+

FastAPI

Python-Jose (JWT)

Uvicorn

📁 Project Folder Structure
project/
│── main.py        # API routes
│── auth.py        # JWT auth logic
│── models.py      # Pydantic models
│── utils.py       # In-memory task operations
│── README.md

▶️ Running the Project

Install dependencies:

pip install fastapi uvicorn python-jose


Run server:

uvicorn main:app --reload


Open Swagger UI:

http://127.0.0.1:8000/docs

🧪 API Testing Scenarios (Mandatory)
✅ Login – Valid

Request:

{
  "username": "rahul",
  "password": "password123"
}


Response:

{
  "access_token": "<jwt>",
  "token_type": "bearer"
}

❌ Login – Invalid
{ "detail": "Invalid username or password" }

📝 Task Scenarios
1️⃣ Create Task

Input:

{
  "title": "Buy Milk",
  "description": "Buy Nandini milk from nearby shop"
}


Output:

{
  "id": 1,
  "title": "Buy Milk",
  "description": "Buy Nandini milk from nearby shop",
  "completed": false
}

🔐 Authentication Failure Cases
Missing token
{"detail": "Not authenticated"}

Invalid token
{"detail": "Could not validate credentials"}

Expired token
{"detail": "Could not validate credentials"}

🧹 Notes

✔ No database required
✔ No additional libraries allowed
✔ Response format must match exactly
✔ Field order must be:

id → title → description → completed

🏁 Completion Checklist

 Login working

 JWT token generation

 Create Task

 Get All Tasks

 Get Single Task

 Update Task

 Delete Task

 Authentication errors handled

 In-memory storage used

 Tested in Swagger

🙌 Author

Sattaru Venkata Abhilash
UST Global Python Full Stack Developer – Training Phase