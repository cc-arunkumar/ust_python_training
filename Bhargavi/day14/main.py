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

# from fastapi import FastAPI,HTTPException
# from pydantic import BaseModel
# from typing import List

# app = FastAPI(title="Student Management System")

# class Student(BaseModel):
#     name : str
#     age : int
#     grade : str = "Not Provided"

# students : List[Student] = []

# @app.post("/students",response_model=Student)
# def add_student(student:Student):
#     students.append(student)
#     return student

# @app.get("/students",response_model=List[Student])
# def get_all_students():
#     return students

# @app.get("/students/{index}",response_model=Student)
# def get_student_by_index(index:int):
#     try:
#         return students[index]
#     except IndexError:
#         raise HTTPException(status_Code=404,detail="student not found")
    
# @app.put("/students/{index}", response_model= List[Student])
# def update_student(index: int, updated_student: Student):
#     try:
#         students[index] = updated_student
#         return updated_student
#     except IndexError:
#         raise HTTPException(status_code=404,detail="student not found")
    
# @app.delete("/students/{index}",response_model=Student)
# def delete_student(index: int):
#     try:
#         removed = students.pop(index)
#         return removed
#     except IndexError:
#         raise HTTPException(status_code=404,detail="student not found")
# from fastapi import FastAPI,HTTPException
# from pydantic import BaseModel
# from typing import List

# app = FastAPI(title="Student Management System")

# class Student(BaseModel):
#     name : str
#     age : int
#     grade : str = "Not Provided"

# students : List[Student] = []

# @app.post("/students",response_model=Student)
# def add_student(student:Student):
#     students.append(student)
#     return student

# @app.get("/students",response_model=List[Student])
# def get_all_students():
#     return students

# @app.get("/students/{index}",response_model=Student)
# def get_student_by_index(index:int):
#     try:
#         return students[index]
#     except IndexError:
#         raise HTTPException(status_Code=404,detail="student not found")
    
# @app.put("/students/{index}", response_model= List[Student])
# def update_student(index: int, updated_student: Student):
#     try:
#         students[index] = updated_student
#         return updated_student
#     except IndexError:
#         raise HTTPException(status_code=404,detail="student not found")
    
# @app.delete("/students/{index}",response_model=Student)
# def delete_student(index: int):
#     try:
#         removed = students.pop(index)
#         return removed
#     except IndexError:
#         raise HTTPException(status_code=404,detail="student not found")
 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, date, time

app = FastAPI(title="UST Employee API")

# Employee Pydantic model
class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "active"

# AttendanceRecord model
class AttendanceRecord(BaseModel):
    employee_id: int
    date: date
    check_in: Optional[time] = None
    check_out: Optional[time] = None

# LeaveRequest model
class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: date
    to_date: date
    reason: str
    status: str = "pending"


employees: List[Employee] = [
    {"id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active"},
    {"id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active"},
    {"id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department": "HR", "role": "HR", "status": "active"}
]

attendance: List[AttendanceRecord] = []
leaves: List[LeaveRequest] = []

next_emp_id = 4
next_leave_id = 1


# 1. Create employee
@app.post("/employees", status_code=201)
def create_employee(emp: Employee):
    global next_emp_id
    for i in employees:
        if i["email"] == emp.email:
            raise HTTPException(status_code=409, detail="Email already exists")
    emp.id = next_emp_id
    next_emp_id += 1
    employees.append(emp.dict())
    return {"Employee Created": emp}


# 2. List all employees 
@app.get("/employees", response_model=List[Employee])
def list_employees(department: Optional[str] = None):
    if department:
        return [emp for emp in employees if emp["department"] == department]
    return employees


# 3. Get employee by ID 
@app.get("/employees/{id}", response_model=Employee)
def get_employee(id: int):
    for emp in employees:
        if emp["id"] == id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")


# 4. Update employee 
@app.put("/employees/{id}")
def update_employee(id: int, emp: Employee):
    for i in range(len(employees)):
        if employees[i]["id"] == id:
            if any(e["email"] == emp.email for e in employees if e["id"] != id):
                raise HTTPException(status_code=409, detail="Email already exists")
            employees[i] = emp.dict()
            return employees[i]
    raise HTTPException(status_code=404, detail="Employee not found")


# 5. Delete employee 
@app.delete("/employees/{id}")
def delete_employee(id: int):
    global employees
    for i in range(len(employees)):
        if employees[i]["id"] == id:
            employees.pop(i)
            return {"detail": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")


# 6. Check-in (attendance)
@app.post("/employees/{id}/checkin", status_code=201)
def check_in(id: int, record: AttendanceRecord):
    for emp in employees:
        if emp["id"] == id:
            for att in attendance:
                if att.employee_id == id and att.date == record.date and att.check_in is not None:
                    raise HTTPException(status_code=409, detail="Already checked in")
            attendance.append(record)
            return record
    raise HTTPException(status_code=404, detail="Employee not found")


# 7. Check-out (attendance)
@app.post("/employees/{id}/checkout")
def check_out(id: int, record: AttendanceRecord):
    for emp in employees:
        if emp["id"] == id:
            for att in attendance:
                if att.employee_id == id and att.date == record.date and att.check_in is not None:
                    if att.check_out is not None:
                        raise HTTPException(status_code=409, detail="Already checked out")
                    att.check_out = record.check_out
                    return att
            raise HTTPException(status_code=400, detail="Check-in required before checkout")
    raise HTTPException(status_code=404, detail="Employee not found")


# 8. Create leave request 
@app.post("/employees/{id}/leave-requests", status_code=201)
def create_leave_request(id: int, leave_request: LeaveRequest):
    global next_leave_id
    if leave_request.from_date > leave_request.to_date:
        raise HTTPException(status_code=400, detail="from_date must be on or before to_date")
    for emp in employees:
        if emp["id"] == id:
            leave_request.leave_id = next_leave_id
            next_leave_id += 1
            leaves.append(leave_request.dict())
            return leave_request
    raise HTTPException(status_code=404, detail="Employee not found")


# 9. List leave requests for an employee
@app.get("/employees/{id}/leave-requests")
def list_leave_requests(id: int):
    for emp in employees:
        if emp["id"] == id:
            return [leave for leave in leaves if leave["employee_id"] == id]
    raise HTTPException(status_code=404, detail="Employee not found")


# output

# Create Employee (POST /employees)
# Request:
# {
#   "name": "Nisha Rao",
#   "email": "nisha@ust.com",
#   "department": "Engineering",
#   "role": "QA"
# }
# response:
# {
#   "Employee Created": {
#     "id": 4,
#     "name": "Nisha Rao",
#     "email": "nisha@ust.com",
#     "department": "Engineering",
#     "role": "QA",
#     "status": "active"
#   }
# }

# If Email Already Exists (409 Conflict):
# Request:
# {
#   "name": "Nisha Rao",
#   "email": "asha.rao@ust.com",
#   "department": "Engineering",
#   "role": "QA"
# }
# response:
# {
#   "detail": "Email already exists"
# }

# List Employees (GET /employees)
# Request:
# GET /employees
# response:
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
#   }
# ]

# With Department Filter (GET /employees?department=Engineering):
# Request:
# GET /employees?department=Engineering
# response:
# [
#   {
#     "id": 1,
#     "name": "Asha Rao",
#     "email": "asha.rao@ust.com",
#     "department": "Engineering",
#     "role": "Engineer",
#     "status": "active"
#   }
# ]

# Get Employee by ID (GET /employees/{id})
# Request:
# GET /employees/1
# response:
# {
#   "id": 1,
#   "name": "Asha Rao",
#   "email": "asha.rao@ust.com",
#   "department": "Engineering",
#   "role": "Engineer",
#   "status": "active"
# }

# Update Employee (PUT /employees/{id})
# Request:
# {
#   "name": "Asha Rao",
#   "email": "asha.rao@ust.com",
#   "department": "Engineering",
#   "role": "Sr Engineer",
#   "status": "active"
# }
# response:
# {
#   "id": 1,
#   "name": "Asha Rao",
#   "email": "asha.rao@ust.com",
#   "department": "Engineering",
#   "role": "Sr Engineer",
#   "status": "active"
# }


# Delete Employee (DELETE /employees/{id})
# Request:
#    DELETE /employees/1
# response:
#    {
#   "detail": "Employee deleted"
# }
 
# Check-in Attendance (POST /employees/{id}/checkin)
# Request: 
# {
#   "employee_id": 1,
#   "date": "2025-11-21",
#   "check_in": "09:10:00",
#   "check_out": null
# }
# response:
# {
#   "date": "2025-11-21",
#   "time": "09:10:00"
# }

# Check-out Attendance (POST /employees/{id}/checkout)
# Request:
#     {
#   "date": "2025-11-21",
#   "time": "18:00:00"
# }
# response:
#    {
#   "employee_id": 1,
#   "date": "2025-11-21",
#   "check_in": "09:10:00",
#   "check_out": "18:00:00"
# }
 
#  Create Leave Request (POST /employees/{id}/leave-requests)
# Request:
# {
#   "from_date": "2025-12-24",
#   "to_date": "2025-12-25",
#   "reason": "family"
# }
# response:
# {
#   "leave_id": 1,
#   "employee_id": 1,
#   "from_date": "2025-12-24",
#   "to_date": "2025-12-25",
#   "reason": "family",
#   "status": "pending"
# }


