from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------
# ADMIN LOGIN
# ---------------------------------------------------------
ADMIN_EMAIL = "admin@ust.com"
ADMIN_PASSWORD = "admin123"

@app.post("/api/login")
def login(data: dict):
    if data["email"] == ADMIN_EMAIL and data["password"] == ADMIN_PASSWORD:
        return {"token": "admin-secret-token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")


# ---------------------------------------------------------
# EMPLOYEE DATA (IN-MEMORY)
# ---------------------------------------------------------
employees = [
    {
        "id": 1,
        "name": "Rahul Sharma",
        "email": "rahul.sharma@ust.com",
        "designation": "Software Engineer",
        "managerId": None
    }
]

@app.get("/api/employees")
def get_employees():
    return employees

@app.get("/api/employees/{id}")
def get_employee(id: int):
    for emp in employees:
        if emp["id"] == id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

@app.post("/api/employees")
def create_employee(emp: dict):
    emp["id"] = len(employees) + 1

    if "managerId" not in emp:
        emp["managerId"] = None

    employees.append(emp)
    return {"message": "Employee created successfully", "id": emp["id"]}

@app.put("/api/employees/{id}")
def update_employee(id: int, emp: dict):
    for i, e in enumerate(employees):
        if e["id"] == id:
            employees[i] = {**e, **emp}
            return {"message": "Employee updated successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")

@app.delete("/api/employees/{id}")
def delete_employee(id: int):
    global employees
    employees = [e for e in employees if e["id"] != id]
    return {"message": "Employee deleted successfully"}


# ---------------------------------------------------------
# TASK DATA (IN-MEMORY)
# ---------------------------------------------------------
tasks = []
task_counter = 1

@app.post("/api/tasks")
def create_task(task: dict):
    global task_counter
    task["task_id"] = task_counter
    task_counter += 1
    tasks.append(task)
    return {"message": "Task created successfully", "task": task}

@app.get("/api/tasks")
def get_tasks():
    return tasks

@app.get("/api/tasks/{task_id}")
def get_task(task_id: int):
    for t in tasks:
        if t["task_id"] == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/api/tasks/{task_id}")
def update_task(task_id: int, updated_task: dict):
    for i, t in enumerate(tasks):
        if t["task_id"] == task_id:
            tasks[i] = {**t, **updated_task, "task_id": task_id}
            return {"message": "Task updated successfully", "task": tasks[i]}
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [t for t in tasks if t["task_id"] != task_id]
    return {"message": "Task deleted successfully"}
