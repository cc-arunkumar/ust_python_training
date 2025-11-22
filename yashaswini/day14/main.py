from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime, date, time

app = FastAPI(title="UST Employee API")

# Counters
next_emp_id = 4
next_leave_id = 1

# ---------------------- MODELS ----------------------

class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "active"

class Attendance(BaseModel):
    employee_id: int
    date: date
    check_in: time | None = None
    check_out: time | None = None

class Leave(BaseModel):
    leave_id: int
    employee_id: int
    from_date: date
    to_date: date
    reason: str
    status: str = "pending"

# ---------------------- STORAGE ----------------------

emp_data: List[Employee] = [
    Employee(id=1, name="Asha Rao", email="asha.rao@ust.com",
             department="Engineering", role="Engineer", status="active"),
    Employee(id=2, name="Vikram S", email="vikram.s@ust.com",
             department="Delivery", role="Manager", status="active"),
    Employee(id=3, name="Meera N", email="meera.n@ust.com",
             department="HR", role="HR", status="active")
]

attendance_records: List[Attendance] = []
leave_records: List[Leave] = []

# ---------------------- EMPLOYEE CRUD ----------------------

@app.post("/employees", response_model=Employee, status_code=201)
def add_employee(emp: Employee):
    global next_emp_id
    for e in emp_data:
        if e.email == emp.email:
            raise HTTPException(status_code=409, detail="Email already exists")
    emp.id = next_emp_id
    next_emp_id += 1
    emp_data.append(emp)
    return emp

@app.get("/employees", response_model=List[Employee])
def get_all_employees(department: str | None = None):
    if department:
        return [e for e in emp_data if e.department == department]
    return emp_data

@app.get("/employees/{emp_id}", response_model=Employee)
def get_employee(emp_id: int):
    for e in emp_data:
        if e.id == emp_id:
            return e
    raise HTTPException(status_code=404, detail="Employee not found")

@app.put("/employees/{emp_id}", response_model=Employee)
def modify_employee(emp_id: int, emp: Employee):
    for e in emp_data:
        if e.email == emp.email and e.id != emp_id:
            raise HTTPException(status_code=409, detail="Email already exists")
    for i in range(len(emp_data)):
        if emp_data[i].id == emp_id:
            emp.id = emp_id
            emp_data[i] = emp
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

@app.delete("/employees/{emp_id}")
def remove_employee(emp_id: int):
    for i in range(len(emp_data)):
        if emp_data[i].id == emp_id:
            emp_data.pop(i)
            return {"detail": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")

# ---------------------- ATTENDANCE ----------------------

@app.post("/employees/{emp_id}/checkin", response_model=Attendance, status_code=201)
def checkin(emp_id: int):
    today = date.today()
    now = datetime.now().time()
    for rec in attendance_records:
        if rec.employee_id == emp_id and rec.date == today and rec.check_in is not None:
            raise HTTPException(status_code=409, detail="Already checked in")
    new_rec = Attendance(employee_id=emp_id, date=today, check_in=now)
    attendance_records.append(new_rec)
    return new_rec

@app.post("/employees/{emp_id}/checkout", response_model=Attendance)
def checkout(emp_id: int):
    today = date.today()
    now = datetime.now().time()
    for rec in attendance_records:
        if rec.employee_id == emp_id and rec.date == today:
            if rec.check_in is None:
                raise HTTPException(status_code=400, detail="Check-in required before checkout")
            if rec.check_out is not None:
                raise HTTPException(status_code=409, detail="Already checked out")
            rec.check_out = now
            return rec
    raise HTTPException(status_code=404, detail="Attendance record not found")

# ---------------------- LEAVE ----------------------

@app.post("/employees/{emp_id}/leave-requests", response_model=Leave, status_code=201)
def request_leave(emp_id: int, from_date: date, to_date: date, reason: str):
    global next_leave_id
    if from_date > to_date:
        raise HTTPException(status_code=400, detail="from_date must be on or before to_date")
    new_leave = Leave(
        leave_id=next_leave_id,
        employee_id=emp_id,
        from_date=from_date,
        to_date=to_date,
        reason=reason,
        status="pending"
    )
    leave_records.append(new_leave)
    next_leave_id += 1
    return new_leave

@app.get("/employees/{emp_id}/leave-requests", response_model=List[Leave])
def list_leaves(emp_id: int):
    result = [lr for lr in leave_records if lr.employee_id == emp_id]
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result
