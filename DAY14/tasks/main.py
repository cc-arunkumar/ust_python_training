from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="UST Employee API")

# Data models
class EmpAdd(BaseModel):
    name: str
    email: str
    department: str
    role: str

class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "active"

class Attendance(BaseModel):
    employee_id: int
    date: str
    check_in: Optional[str] = None
    check_out: Optional[str] = None

class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: str
    to_date: str
    reason: str
    status: str = "pending"

class Reqleave(BaseModel):
    from_date: str
    to_date: str
    reason: str

class CheckData(BaseModel):
    date: str
    time: str

employees = [
    {"id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active"},
    {"id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active"},
    {"id": 3, "name": "Meera N", "email": "meer.n@ust.com", "department": "HR", "role": "HR", "status": "active"}
]
next_emp_id=4
attendance = []
leaves = []
next_leave_id = 1

def find_employee(emp_id):
    for e in employees:
        if e["id"] == emp_id:
            return e
    return None

@app.post("/employees", status_code=201)
def create_employee(emp: EmpAdd):
    global next_emp_id
    for e in employees:
        if e["email"] == emp.email:
            raise HTTPException(409, "Email already exists")
    new_id = next_emp_id
    new_emp = {
        "id": new_id,
        "name": emp.name,
        "email": emp.email,
        "department": emp.department,
        "role": emp.role,
        "status": "active"
    }
    next_emp_id+=1
    employees.append(new_emp)
    return new_emp

@app.get("/employees")
def list_emp(department: str = None):
    if department:
        return [e for e in employees if e["department"] == department]
    return employees

@app.get("/employees/{id}")
def get_emp(id: int):
    emp = find_employee(id)
    if not emp:
        raise HTTPException(404, "Employee not found")
    return emp

@app.put("/employees/{id}")
def update_emp(id: int, emp: Employee):
    old = find_employee(id)
    if not old:
        raise HTTPException(404, "Employee not found")
    for e in employees:
        if e["email"] == emp.email and e["id"] != id:
            raise HTTPException(409, "Email already exists")
    old.update(emp.dict())
    return old

@app.delete("/employees/{id}")
def delete_emp(id: int):
    emp = find_employee(id)
    if not emp:
        raise HTTPException(404, "Employee not found")
    employees.remove(emp)
    return {"detail": "Employee deleted"}

@app.post("/employees/{id}/checkin", status_code=201)
def check_in(id: int, data: CheckData):
    if not find_employee(id):
        raise HTTPException(404, "Employee not found")
    try:
        datetime.strptime(data.date,"%Y-%m-%d")
        datetime.strptime(data.time,"%H:%M:%S")
    except:
        raise HTTPException(400,"Invalid date or time format")
    date = data.date
    time = data.time
    for a in attendance:
        if a["employee_id"] == id and a["date"] == date:
            if a["check_in"]:
                raise HTTPException(409, "Already checked in")
            a["check_in"] = time
            return a
    record = {
        "employee_id": id,
        "date": date,
        "check_in": time,
        "check_out": None
    }
    attendance.append(record)
    return record

@app.post("/employees/{id}/checkout")
def check_out(id: int, data: CheckData):
    if not find_employee(id):
        raise HTTPException(404, "Employee not found")
    try:
        datetime.strptime(data.date,"%Y-%m-%d")
        datetime.strptime(data.time,"%H:%M:%S")
    except:
        raise HTTPException(400,"Invalid date or time format")
    date = data.date
    time = data.time
    for a in attendance:
        if a["employee_id"] == id and a["date"] == date:
            if not a["check_in"]:
                raise HTTPException(400, "Check-in required before checkout")
            if a["check_out"]:
                raise HTTPException(409, "Already checked out")
            a["check_out"] = time
            return a
    raise HTTPException(400, "Check-in required before checkout")

@app.post("/employees/{id}/leave-requests", status_code=201)
def create_leave(id: int, data: Reqleave):
    global next_leave_id
    if not find_employee(id):
        raise HTTPException(404, "Employee not found")
    try:
        f=datetime.strptime(data.from_date,"%Y-%m-%d")
        t=datetime.strptime(data.to_date,"%Y-%m-%d")
    except:
        raise HTTPException(400,"Invalid date format")
    if f>t:
        raise HTTPException(400, "From date must be on or before to date")
    new_leave = {
        "leave_id": next_leave_id,
        "employee_id": id,
        "from_date": data.from_date,
        "to_date": data.to_date,
        "reason": data.reason,
        "status": "pending"
    }
    leaves.append(new_leave)
    next_leave_id += 1
    return new_leave

@app.get("/employees/{id}/leave-requests")
def list_leaves(id: int):
    if not find_employee(id):
        raise HTTPException(404, "Employee not found")
    return [l for l in leaves if l["employee_id"] == id]