from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="UST Employee API")

class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "active"

class EmployeeCreate(BaseModel):
    name: str
    email: str
    department: str
    role: str

class AttendanceRecord(BaseModel):
    employee_id: int
    date: str
    check_in: str | None = None
    check_out: str | None = None

class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: str
    to_date: str
    reason: str
    status: str = "pending"

class CheckinRequest(BaseModel):
    date: str
    time: str

class CheckoutRequest(BaseModel):
    date: str
    time: str

class LeaveCreation(BaseModel):
    from_date: str
    to_date: str
    leave_reason: str

employees = [
    { "id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active" },
    { "id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active" },
    { "id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department": "HR", "role": "HR", "status": "active" }
]

attendance = []
leaves = []

next_emp_id = 4
next_leave_id = 1


@app.post("/employees", response_model=Employee, status_code=201)
def post_employee(emp: EmployeeCreate):
    global next_emp_id
    if any(e["email"] == emp.email for e in employees):
        raise HTTPException(status_code=409, detail="Email already exists")
    new_emp = {
        "id": next_emp_id,
        "name": emp.name,
        "email": emp.email,
        "department": emp.department,
        "role": emp.role,
        "status": "active"
    }
    employees.append(new_emp)
    next_emp_id += 1
    return new_emp

@app.get("/employees")
def list_of_employees(department: str):
    if department:
        return [e for e in employees if e["department"] == department]
    return employees

@app.get("/employees/{id}")
def get_by_id(id: int):
    for em in employees:
        if em["id"] == id:
            return em
    raise HTTPException(status_code=404, detail="Employee not found")

@app.put("/employees/{id}")
def update_by_id(id: int, emp: Employee):
    for i, e in enumerate(employees):
        if e["id"] == id:
            for em in employees:
                if em["id"] != id and em["email"] == emp.email:
                    raise HTTPException(status_code=409, detail="Email already exists")

            employees[i] = emp
            return employees[i]
    raise HTTPException(status_code=404, detail="Employee not found")


@app.delete("/employees/{id}")
def delete_employee(id: int):
    for i, e in enumerate(employees):
        if e["id"] == id:
            employees.pop(i)
            return {"detail": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")

@app.post("/employees/{id}/checkin", status_code=201)
def check_in(id: int, req: CheckinRequest):
    for e in employees:
        if e["id"] == id:
            try:
                datetime.strptime(req.date, "%Y-%m-%d")
                datetime.strptime(req.time, "%H:%M:%S")
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid date/time format")

            for record in attendance:
                if record["employee_id"] == id and record["date"] == req.date:
                    if record["check_in"]:
                        raise HTTPException(status_code=409, detail="Already checked in")
                    record["check_in"] = req.time
                    return record

            new_record = {"employee_id": id, "date": req.date, "check_in": req.time, "check_out": None}
            attendance.append(new_record)
            return new_record
    raise HTTPException(status_code=404, detail="Employee not found")

@app.post("/employees/{id}/checkout")
def check_out(id: int, req: CheckoutRequest):
    for e in employees:
        if e["id"] == id:
            try:
                datetime.strptime(req.date, "%Y-%m-%d")
                datetime.strptime(req.time, "%H:%M:%S")
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid date/time format")

            for record in attendance:
                if record["employee_id"] == id and record["date"] == req.date:
                    if not record["check_in"]:
                        raise HTTPException(status_code=400, detail="Check-in required before checkout")
                    if record["check_out"]:
                        raise HTTPException(status_code=409, detail="Already checked out")
                    record["check_out"] = req.time
                    return record
            raise HTTPException(status_code=400, detail="Check-in required before checkout")
    raise HTTPException(status_code=404, detail="Employee not found")

@app.post("/employees/{id}/leave-requests", status_code=201)
def create_leave(id: int, req: LeaveCreation):
    global next_leave_id
    for e in employees:
        if e["id"] == id:
            from_date = datetime.strptime(req.from_date, "%Y-%m-%d")
            to_date = datetime.strptime(req.to_date, "%Y-%m-%d")
            if from_date > to_date:
                raise HTTPException(status_code=400, detail="from_date must be on or before to_date")

            new_leave = {
                "leave_id": next_leave_id,
                "employee_id": id,
                "from_date": req.from_date,
                "to_date": req.to_date,
                "reason": req.leave_reason,
                "status": "pending"
            }
            leaves.append(new_leave)
            next_leave_id += 1
            return new_leave
    raise HTTPException(status_code=404, detail="Employee not found")

@app.get("/employees/{id}/leave-requests")
def list_leaves(id: int):
    for e in employees:
        if e["id"] == id:
            for l in leaves:
                if l['employee_id']==id:
                    return l
    raise HTTPException(status_code=404, detail="Employee not found")
