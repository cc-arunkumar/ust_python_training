from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

employees = [
    {
        "id": 1,
        "name": "Rahul Sharma",
        "email": "rahul.sharma@ust.com",
        "designation": "Software Engineer",
        "department": "Digital",
        "location": "Bangalore",
        "status": "Active",
        "salary": 75000,
        "date_of_joining": "2022-06-15",
        "createdBy": "Admin",
        "updatedBy": "Admin",
        "createdAt": "2025-01-01",
        "updatedAt": "2025-01-01"
    }
]
ADMIN_EMAIL = "admin@ust.com"
ADMIN_PASSWORD = "admin123"

@app.post("/api/login")
def login(data: dict):
    if data["email"] == ADMIN_EMAIL and data["password"] == ADMIN_PASSWORD:
        return {"token": "admin-secret-token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/api/employees")
def get_employees():
    return employees

@app.get("/api/employees/{id}")
def get_employee(id: int):
    for emp in employees:
        if emp["id"] == id:
            return emp
    return {"error": "Employee not found"}

@app.post("/api/employees")
def create_employee(emp: dict):
    emp["id"] = len(employees) + 1
    employees.append(emp)
    return {"message": "Employee created successfully", "id": emp["id"]}

@app.put("/api/employees/{id}")
def update_employee(id: int, emp: dict):
    for i, e in enumerate(employees):
        if e["id"] == id:
            employees[i] = {**e, **emp}
            return {"message": "Employee updated successfully"}
    return {"error": "Employee not found"}

@app.delete("/api/employees/{id}")
def delete_employee(id: int):
    global employees
    employees = [e for e in employees if e["id"] != id]
    return {"message": "Employee deleted successfully"}
