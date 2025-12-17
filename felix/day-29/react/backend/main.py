from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    # allow_headers=["*"],
)

class Employee(BaseModel):
    id: int | None = None
    name: str
    designation: str
    location: str | None = None
    project: str | None = None

employees = []
current_id = 1


@app.post("/employees")
def create_employee(emp: Employee):
    global current_id
    emp.id = current_id
    current_id += 1
    employees.append(emp)
    return emp


@app.get("/employees")
def get_all_employees():
    return employees


#  Get Single Employee
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    for emp in employees:
        if emp.id == emp_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")


# Update Employee
@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, updated: Employee):
    for index, emp in enumerate(employees):
        if emp.id == emp_id:
            updated.id = emp_id
            employees[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Employee not found")


# Delete Employee
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):
    for emp in employees:
        if emp.id == emp_id:
            employees.remove(emp)
            return {"message": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")