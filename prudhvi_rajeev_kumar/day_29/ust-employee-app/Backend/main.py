from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

# Employee model with the fields you requested
class Employee(BaseModel):
    name: str
    designation: str
    location: str
    project: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory list to store employees
employees: List[Employee] = []

@app.get("/")
def root():
    return {"message": "Employee API is running!"}

# Get all employees
@app.get("/employees", response_model=List[Employee])
def get_employees():
    return employees

# Get employee by name
@app.get("/employees/{employee_name}", response_model=Employee)
def get_employee(employee_name: str):
    for emp in employees:
        if emp.name.lower() == employee_name.lower():
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

# Add new employee
@app.post("/employees", response_model=Employee)
def add_employee(employee: Employee):
    # Prevent duplicate names
    for emp in employees:
        if emp.name.lower() == employee.name.lower():
            raise HTTPException(status_code=400, detail="Employee already exists")
    employees.append(employee)
    return employee

# Update employee by name
@app.put("/employees/{employee_name}", response_model=Employee)
def update_employee(employee_name: str, updated_employee: Employee):
    for index, emp in enumerate(employees):
        if emp.name.lower() == employee_name.lower():
            employees[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee not found")

# Delete employee by name
@app.delete("/employees/{employee_name}")
def delete_employee(employee_name: str):
    for index, emp in enumerate(employees):
        if emp.name.lower() == employee_name.lower():
            employees.pop(index)
            return {"message": f"Employee '{employee_name}' deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")
