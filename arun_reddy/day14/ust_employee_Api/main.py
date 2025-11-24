# CRUD Task
# Simpler use-case: UST Employee API
# Data models
# Employee
# id: int — auto-increment (1, 2, 3, ...)
# name: str
# email: str
# department: str
# role: str
# status: str — "active" or "resigned" (default "active" )
# AttendanceRecord
# employee_id: int
# date: "YYYY-MM-DD"
# check_in: "HH:MM:SS" | null
# check_out: "HH:MM:SS" | null
# LeaveRequest
# leave_id: int — auto-increment
# employee_id: int
# from_date: "YYYY-MM-DD"
# to_date: "YYYY-MM-DD"
# reason: str
# CRUD Task 1
# status: "pending" | "approved" | "denied" (defaults to "pending" )
# Initial in-memory sample data (copy into your code)
# Employees list (start with these 3):
# [
#  { "id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department":
# "Engineering", "role": "Engineer", "status": "active" },
#  { "id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department":
# "Delivery", "role": "Manager", "status": "active" },
#  { "id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department":
# "HR", "role": "HR", "status": "active" }
# ]
# Attendance: start empty []
# Leaves: start empty []
# Also keep counters:
# next_emp_id = 4
# next_leave_id = 1
# Endpoints
# 1) Create employee
# POST /employees
# Request body (JSON):
# { "name": "Nisha Rao", "email": "nisha@ust.com", "department": "Engineerin
# g", "role": "QA" }
# Behavior
# id assigned automatically ( next_emp_id )
# CRUD Task 2
# status = "active" by default
# If email already exists → return 409 Conflict
# Success (201) response:
# { "id": 4, "name":"Nisha Rao", "email":"nisha@ust.com", "department":"Engine
# ering", "role":"QA", "status":"active" }
# Errors
# 409: {"detail":"Email already exists"}
# 2) List employees
# GET /employees
# Optional query: department (filter by exact match)
# Success (200) response: array of employee objects (maybe empty)
# Example:
# GET /employees → returns all 3 sample employees.
# GET /employees?department=Engineering → returns only Asha and Nisha (if created).
# 3) Get employee by id
# GET /employees/{id}
# Success (200):
# { "id":1, "name":"Asha Rao", "email":"asha.rao@ust.com", "department":"Engi
# neering", "role":"Engineer", "status":"active" }
# Errors
# 404: {"detail":"Employee not found"}
# 4) Update employee (replace)
# PUT /employees/{id}
# CRUD Task 3
# Request body — full employee fields except id :
# { "name":"Asha Rao", "email":"asha.rao@ust.com", "department":"Engineerin
# g", "role":"Sr Engineer", "status":"active" }
# Behavior
# Replace fields for employee with given id.
# If id not found → 404
# If email is changed to one that already exists for other employee → 409
# Response (200) → updated employee object
# 5) Delete employee
# DELETE /employees/{id}
# Behavior
# Remove employee from list (permanent)
# If not found → 404
# Success (200):
# {"detail":"Employee deleted"}
# 6) Check-in (attendance)
# POST /employees/{id}/checkin
# Request JSON (simple required fields):
# { "date": "2025-11-21", "time": "09:10:00" }
# Behavior
# If employee not found → 404
# CRUD Task 4
# If an attendance record for that date exists with a check_in → 409 (already
# checked in)
# Otherwise: create or update record for that date with check_in set
# Response (201):
# { "employee_id":1, "date":"2025-11-21", "check_in":"09:10:00", "check_out": n
# ull }
# 7) Check-out (attendance)
# POST /employees/{id}/checkout
# Request JSON:
# { "date": "2025-11-21", "time": "18:00:00" }
# Behavior
# If employee not found → 404
# If no attendance record for that date or no check_in recorded → 400
# ( {"detail":"Check-in required before checkout"} )
# If check_out already set → 409
# Otherwise set check_out and return updated record (200)
# Response (200):
# { "employee_id":1, "date":"2025-11-21", "check_in":"09:10:00", "check_out":"1
# 8:00:00" }
# 8) Create leave request (very simple)
# POST /employees/{id}/leave-requests
# Request JSON:
# CRUD Task 5
# { "from_date":"2025-12-24", "to_date":"2025-12-25", "reason":"family" }
# Behavior
# If from_date > to_date → 400
# Create leave_id using next_leave_id , status "pending"
# Return created leave (201)
# Response (201):
# { "leave_id":1, "employee_id":1, "from_date":"2025-12-24", "to_date":"2025-12
# -25", "reason":"family", "status":"pending" }
# 9) List leave requests for employee
# GET /employees/{id}/leave-requests
# Behavior — return array (possibly empty). 404 if employee not found.
# Error response format (consistent)
# Every error returns JSON:
# {"detail":"<clear message>"}
# Examples:
# 404 {"detail":"Employee not found"}
# 400 {"detail":"from_date must be on or before to_date"}
# 409 {"detail":"Email already exists"}
# Implementation notes (very short & simple)
# Use lists: employees , attendance , leaves
# Auto-increment counters: next_emp_id , next_leave_id
# CRUD Task 6
# Parse dates/times only for basic comparison (you can accept strings but
# check format using datetime.strptime and return 400 on parse error)
# No concurrency handling needed for this demo (single-process, in-memory)


# code starts from here
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime, date, time

# Initialize FastAPI application with a title
app = FastAPI(title="UST Employee API")

# ---------------------- COUNTERS ----------------------
# These counters are used to auto-generate IDs for new employees and leave requests
next_emp_id = 4        # Next employee ID (starts after initial 3 employees)
next_leave_id = 1      # Next leave request ID

# ---------------------- MODELS ----------------------

class Employee(BaseModel):
    """
    Represents an employee record.
    Includes basic details such as name, email, department, role, and status.
    """
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "active"   # Default status is 'active'

class Attendance(BaseModel):
    """
    Represents an attendance record for an employee.
    Tracks check-in and check-out times for a given date.
    """
    employee_id: int
    date: date
    check_in: time | None = None
    check_out: time | None = None

class Leave(BaseModel):
    """
    Represents a leave request made by an employee.
    Includes leave duration, reason, and approval status.
    """
    leave_id: int
    employee_id: int
    from_date: date
    to_date: date
    reason: str
    status: str = "pending"   # Default status is 'pending'

# ---------------------- STORAGE ----------------------
# In-memory storage for employees, attendance, and leave requests

emp_data: List[Employee] = [
    Employee(id=1, name="Asha Rao", email="asha.rao@ust.com",
             department="Engineering", role="Engineer", status="active"),
    Employee(id=2, name="Vikram S", email="vikram.s@ust.com",
             department="Delivery", role="Manager", status="active"),
    Employee(id=3, name="Meera N", email="meera.n@ust.com",
             department="HR", role="HR", status="active")
]

attendance_records: List[Attendance] = []   # Stores attendance records
leave_records: List[Leave] = []             # Stores leave requests

# ---------------------- EMPLOYEE CRUD ----------------------

@app.post("/employees", response_model=Employee, status_code=201)
def add_employee(emp: Employee):
    """
    Add a new employee.
    - Ensures email is unique.
    - Assigns a new auto-generated ID.
    """
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
    """
    Retrieve all employees.
    - Optionally filter by department.
    """
    if department:
        return [e for e in emp_data if e.department == department]
    return emp_data

@app.get("/employees/{emp_id}", response_model=Employee)
def get_employee(emp_id: int):
    """
    Retrieve a specific employee by ID.
    Raises 404 if not found.
    """
    for e in emp_data:
        if e.id == emp_id:
            return e
    raise HTTPException(status_code=404, detail="Employee not found")

@app.put("/employees/{emp_id}", response_model=Employee)
def modify_employee(emp_id: int, emp: Employee):
    """
    Update an existing employee record.
    - Prevents duplicate emails.
    - Replaces the record if found.
    """
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
    """
    Delete an employee by ID.
    Raises 404 if not found.
    """
    for i in range(len(emp_data)):
        if emp_data[i].id == emp_id:
            emp_data.pop(i)
            return {"detail": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")

# ---------------------- ATTENDANCE ----------------------

@app.post("/employees/{emp_id}/checkin", response_model=Attendance, status_code=201)
def checkin(emp_id: int):
    """
    Record employee check-in for the current date.
    - Prevents multiple check-ins on the same day.
    """
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
    """
    Record employee check-out for the current date.
    - Requires check-in before checkout.
    - Prevents multiple check-outs.
    """
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
    """
    Submit a leave request for an employee.
    - Validates that from_date is not after to_date.
    - Assigns a new leave ID.
    """
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
    """
    Retrieve all leave requests for a specific employee.
    Raises 404 if no leave requests found.
    """
    result = [lr for lr in leave_records if lr.employee_id == emp_id]
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result


# sample API requests and responses
# 1. Add Employee
# Request:
# {
#   "id": 0,
#   "name": "Ravi Kumar",
#   "email": "ravi.kumar@ust.com",
#   "department": "Finance",
#   "role": "Analyst",
#   "status": "active"
# }
# Response:
# {
#   "id": 4,
#   "name": "Ravi Kumar",
#   "email": "ravi.kumar@ust.com",
#   "department": "Finance",
#   "role": "Analyst",
#   "status": "active"
# }
# 2. Get All Employees
# Request:
# GET /employees
# Response:
# [
#   {
#     "id": 1,
#     "name": "Asha Rao",
#     "email": "asha.rao@ust.com",
#     "department": "Engineering",
#     "role": "Engineer",
#     "status": "active"
#   },
#   {
#     "id": 2,
#     "name": "Vikram S",
#     "email": "vikram.s@ust.com",
#     "department": "Delivery",
#     "role": "Manager",
#     "status": "active"
#   },
#   {
#     "id": 3,
#     "name": "Meera N",
#     "email": "meera.n@ust.com",
#     "department": "HR",
#     "role": "HR",
#     "status": "active"
#   },
#   {
#     "id": 4,
#     "name": "Ravi Kumar",
#     "email": "ravi.kumar@ust.com",
#     "department": "Finance",
#     "role": "Analyst",
#     "status": "active"
#   }
# ]
# 3. Get Employee by ID
# Request:
# GET /employees/2
# Response:
# {
#   "id": 2,
#   "name": "Vikram S",
#   "email": "vikram.s@ust.com",
#   "department": "Delivery",
#   "role": "Manager",
#   "status": "active"
# }
# 4. Modify Employee
# Request:
# PUT /employees/3
# Body:
# {
#   "id": 3,
#   "name": "Meera N",
#   "email": "meera.n@ust.com",
#   "department": "HR",
#   "role": "Senior HR",
#   "status": "active"
# }
# Response:
# {
#   "id": 3,
#   "name": "Meera N",
#   "email": "meera.n@ust.com",
#   "department": "HR",
#   "role": "Senior HR",
#   "status": "active"
# }
# 5. Delete Employee
# Request:
# DELETE /employees/4
# Response:
# {"detail": "Employee deleted"}
# 6. Check-in
# Request:
# POST /employees/1/checkin
# Response (example with today’s date and time):
# {
#   "employee_id": 1,
#   "date": "2025-11-24",
#   "check_in": "10:30:00",
#   "check_out": null
# }
# 7. Check-out
# Request:
# POST /employees/1/checkout
# Response (example with today’s date and time):
# {
#   "employee_id": 1,
#   "date": "2025-11-24",
#   "check_in": "10:30:00",
#   "check_out": "17:45:00"
# }
# 8. Request Leave
# Request:
# POST /employees/2/leave-requests?from_date=2025-12-01&to_date=2025-12-05&reason=Vacation
# Response:
# {
#   "leave_id": 1,
#   "employee_id": 2,
#   "from_date": "2025-12-01",
#   "to_date": "2025-12-05",
#   "reason": "Vacation",
#   "status": "pending"
# }
# 9. List Leave Requests
# Request:
# GET /employees/2/leave-requests
# Response:
# [
#   {
#     "leave_id": 1,
#     "employee_id": 2,
#     "from_date": "2025-12-01",
#     "to_date": "2025-12-05",
#     "reason": "Vacation",
#     "status": "pending"
#   }
# ]