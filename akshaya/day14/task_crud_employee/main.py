from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date, time, timedelta

app = FastAPI(title="UST Employee API")

# Initial In-memory data
employees: List[Employee] = [
    { "id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active" },
    { "id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active" },
    { "id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department": "HR", "role": "HR", "status": "active" }
]

# Global counters
next_emp_id = 4
next_leave_id = 1

# Data Models
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
    check_in: Optional[time] = None
    check_out: Optional[time] = None

attendance: List[Attendance] = []

class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: date
    to_date: Optional[date] = None
    reason: str
    status: str = "pending"

leaves: List[LeaveRequest] = []

class CheckInRequest(BaseModel):
    date: date
    time: time

class CheckOutRequest(BaseModel):
    date: date
    time: time

class CheckLeaveRequest(BaseModel):
    from_date: date
    to_date: date
    reason: str

# CRUD Operations

# Create Employee
@app.post("/employees", response_model=Employee)
def create_employee(employee: Employee):
    global next_emp_id

    # Check if email already exists
    if any(e.email == employee.email for e in employees):
        raise HTTPException(status_code=409, detail="Email already exists")

    employee.id = next_emp_id
    employees.append(employee.dict())  # Add the employee to the list
    next_emp_id += 1  

    return employee

# Get All Employees
@app.get("/employees", response_model=List[Employee])
def get_all_employees(department: Optional[str] = None):
    if department:
        return [e for e in employees if e['department'] == department]
    return employees

# Get Employee by ID
@app.get("/employees/{id}", response_model=Employee)
def get_employee_by_id(id: int):
    employee = next((e for e in employees if e.id == id), None)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

# Update Employee
@app.put("/employees/{id}", response_model=Employee)
def update_employee(id: int, updated_employee: Employee):
    employee = next((e for e in employees if e.id == id), None)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    if updated_employee.email != employee.email:
        if any(e.email == updated_employee.email for e in employees):
            raise HTTPException(status_code=409, detail="Email already exists")

    for e in employees:
        if e.id == id:
            e.name = updated_employee.name
            e.email = updated_employee.email
            e.department = updated_employee.department
            e.role = updated_employee.role
            e.status = updated_employee.status

    return employee

# Delete Employee
@app.delete("/employees/{id}", response_model=Employee)
def delete_employee(id: int):
    employee = next((e for e in employees if e.id == id), None)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    employees.remove(employee)
    return employee

# Check-in Attendance
@app.post("/employees/{id}/checkin", response_model=Attendance, status_code=201)
def check_in(id: int, req: CheckInRequest):
    employee = next((e for e in employees if e.id == id), None)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    record = next((a for a in attendance if a.date == req.date and a.employee_id == id), None)
    if record:
        if record.check_in is not None:
            raise HTTPException(status_code=409, detail="Check-in already done")
        else:
            record.check_in = req.time
            return Attendance(**record)

    n_record = {
        "employee_id": id,
        "date": req.date,
        "check_in": req.time,
        "check_out": None
    }
    attendance.append(n_record)
    return Attendance(**n_record)

# Check-out Attendance
@app.post("/employees/{id}/checkout", response_model=Attendance)
def check_out(id: int, req: CheckOutRequest):
    employee = next((e for e in employees if e.id == id), None)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    record = next((a for a in attendance if a.date == req.date and a.employee_id == id), None)
    if not record:
        raise HTTPException(status_code=400, detail="Check-in required before checkout")

    if record.check_in is None:
        raise HTTPException(status_code=400, detail="Check-in required before checkout")

    if record.check_out is not None:
        raise HTTPException(status_code=409, detail="Already checked out")

    record.check_out = req.time
    return Attendance(**record)

# Create Leave Request
@app.post("/employees/{id}/leave-requests", response_model=LeaveRequest, status_code=201)
def create_leave_request(id: int, req: CheckLeaveRequest):
    global next_leave_id
    employee = next((e for e in employees if e.id == id), None)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    # Set default to_date if not provided
    to_date = req.to_date if req.to_date else req.from_date + timedelta(days=10)

    if req.from_date > to_date:
        raise HTTPException(status_code=400, detail="from_date must be on or before to_date")

    new_leave = {
        "leave_id": next_leave_id,
        "employee_id": id,
        "from_date": req.from_date,
        "to_date": to_date,
        "reason": req.reason,
        "status": "pending"
    }
    leaves.append(new_leave)
    next_leave_id += 1
    return LeaveRequest(**new_leave)

# List Leave Requests for an Employee
@app.get("/employees/{id}/leave-requests", response_model=List[LeaveRequest])
def list_leave_requests(id: int):
    employee = next((e for e in employees if e.id == id), None)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    emp_leaves = [LeaveRequest(**l) for l in leaves if l["employee_id"] == id]
    return emp_leaves
