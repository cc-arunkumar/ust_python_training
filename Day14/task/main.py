

from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum

app = FastAPI(title="UST Employee API")

# Enum for employee status
# Defines possible values for employee status: active or inactive.
class Status(str, Enum):
    active = "active"
    inactive = "inactive"

# Model for adding a new employee
# Used when creating a new employee record (without ID).
class EmpAdd(BaseModel):
    name: str
    email: EmailStr
    department: str
    role: str

# Employee model
# Represents a complete employee record with ID, name, email, department, role, and status.
class Employee(BaseModel):
    id: int
    name: str
    email: EmailStr
    department: str
    role: str
    status: Status = Status.active

# Attendance model
# Tracks check-in and check-out times for employees on a given date.
class Attendance(BaseModel):
    employee_id: int
    date: str
    check_in: Optional[str] = None
    check_out: Optional[str] = None

# Leave request model
# Represents a leave request with ID, employee ID, date range, reason, and status.
class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: str
    to_date: str
    reason: str
    status: str = "pending"

# Model for creating a leave request (without leave_id)
class Reqleave(BaseModel):
    from_date: str
    to_date: str
    reason: str

# Model for check-in/check-out data
class CheckData(BaseModel):
    date: str
    time: str

# In-memory data storage
# Pre-populated list of employees, along with attendance and leave records.
employees = [
    {"id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active"},
    {"id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active"},
    {"id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department": "HR", "role": "HR", "status": "active"}
]
next_emp_id = 4
attendance = []
leaves = []
next_leave_id = 1

# Utility function to find an employee by ID
def find_employee(emp_id):
    for e in employees:
        if e["id"] == emp_id:
            return e
    return None

# Create a new employee
# Endpoint: POST /employees
# Validates duplicate email, assigns a new ID, and adds the employee to the list.
@app.post("/employees", response_model=Employee, status_code=201)
def create_employee(emp: EmpAdd):
    global next_emp_id
    for e in employees:
        if e["email"] == emp.email:
            raise HTTPException(409, "Email already exists")
    new_emp = {"id": next_emp_id, "name": emp.name, "email": emp.email, "department": emp.department, "role": emp.role, "status": "active"}
    employees.append(new_emp)
    next_emp_id += 1
    return new_emp

# List employees
# Endpoint: GET /employees
# Returns all employees or filters by department if provided.
@app.get("/employees", response_model=List[Employee])
def list_emp(department: str = None):
    if department:
        return [e for e in employees if e["department"].lower() == department.lower()]
    return employees

# Get employee by ID
# Endpoint: GET /employees/{id}
# Returns a single employee record or 404 if not found.
@app.get("/employees/{id}", response_model=Employee)
def get_emp(id: int):
    emp = find_employee(id)
    if not emp:
        raise HTTPException(404, "Employee not found")
    return emp

# Update employee by ID
# Endpoint: PUT /employees/{id}
# Updates employee details, validates duplicate email, and returns updated record.
@app.put("/employees/{id}", response_model=Employee)
def update_emp(id: int, emp: Employee):
    old = find_employee(id)
    if not old:
        raise HTTPException(404, "Employee not found")
    for e in employees:
        if e["email"] == emp.email and e["id"] != id:
            raise HTTPException(409, "Email already exists")
    old.update(emp.dict())
    return old

# Delete employee by ID
# Endpoint: DELETE /employees/{id}
# Removes employee from the list and returns confirmation.
@app.delete("/employees/{id}")
def delete_emp(id: int):
    emp = find_employee(id)
    if not emp:
        raise HTTPException(404, "Employee not found")
    employees.remove(emp)
    return {"detail": "Employee deleted"}

# Employee check-in
# Endpoint: POST /employees/{id}/checkin
# Validates date/time format, ensures employee exists, and records check-in.
@app.post("/employees/{id}/checkin", status_code=201)
def check_in(id: int, data: CheckData):
    if not find_employee(id):
        raise HTTPException(404, "Employee not found")
    try:
        datetime.strptime(data.date, "%Y-%m-%d")
        datetime.strptime(data.time, "%H:%M:%S")
    except:
        raise HTTPException(400, "Invalid date or time format")
    for a in attendance:
        if a["employee_id"] == id and a["date"] == data.date:
            if a["check_in"]:
                raise HTTPException(409, "Already checked in")
            a["check_in"] = data.time
            return a
    record = {"employee_id": id, "date": data.date, "check_in": data.time, "check_out": None}
    attendance.append(record)
    return record

# Employee check-out
# Endpoint: POST /employees/{id}/checkout
# Validates date/time format, ensures check-in exists, and records check-out.
@app.post("/employees/{id}/checkout")
def check_out(id: int, data: CheckData):
    if not find_employee(id):
        raise HTTPException(404, "Employee not found")
    try:
        datetime.strptime(data.date, "%Y-%m-%d")
        datetime.strptime(data.time, "%H:%M:%S")
    except:
        raise HTTPException(400, "Invalid date or time format")
    for a in attendance:
        if a["employee_id"] == id and a["date"] == data.date:
            if not a["check_in"]:
                raise HTTPException(400, "Check-in required before checkout")
            if a["check_out"]:
                raise HTTPException(409, "Already checked out")
            a["check_out"] = data.time
            return a
    raise HTTPException(400, "Check-in required before checkout")

# Create leave request
# Endpoint: POST /employees/{id}/leave-requests
# Validates employee existence, date format, and date range before creating a leave request.
@app.post("/employees/{id}/leave-requests", status_code=201)
def create_leave(id: int, data: Reqleave):
    global next_leave_id
    if not find_employee(id):
        raise HTTPException(404, "Employee not found")
    try:
        f = datetime.strptime(data.from_date, "%Y-%m-%d")
        t = datetime.strptime(data.to_date, "%Y-%m-%d")
    except:
        raise HTTPException(400, "Invalid date format")
    if f > t:
        raise HTTPException(400, "From date must be on or before to date")
    new_leave = {"leave_id": next_leave_id, "employee_id": id, "from_date": data.from_date, "to_date": data.to_date, "reason": data.reason, "status": "pending"}
    leaves.append(new_leave)
    next_leave_id += 1
    return new_leave

# List leave requests for an employee
# Endpoint: GET /employees/{id}/leave-requests
# Returns all leave requests for the given employee.
@app.get("/employees/{id}/leave-requests", response_model=List[LeaveRequest])
def list_leaves(id: int):
    if not find_employee(id):
        raise HTTPException(404, "Employee not found")
    return [l for l in leaves if l["employee_id"] == id]


# sample output:

# Sample Output for UST Employee API (Important Test Cases)

# Test 1: Create a New Employee
## Input:
# POST /employees
# {
#   "name": "Ravi Kumar",
#   "email": "ravi.kumar@ust.com",
#   "department": "Finance",
#   "role": "Analyst"
# }

## Output:
# HTTP Status: 201 Created
# {
#   "id": 4,
#   "name": "Ravi Kumar",
#   "email": "ravi.kumar@ust.com",
#   "department": "Finance",
#   "role": "Analyst",
#   "status": "active"
# }
### Comment:
# Adds a new employee with auto-generated ID. Validates duplicate email before creation.


# Test 2: List All Employees
## Input:
# GET /employees

## Output:
# HTTP Status: 200 OK
# [
#   { "id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active" },
#   { "id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active" },
#   { "id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department": "HR", "role": "HR", "status": "active" },
#   { "id": 4, "name": "Ravi Kumar", "email": "ravi.kumar@ust.com", "department": "Finance", "role": "Analyst", "status": "active" }
# ]
### Comment:
# Returns all employees. Supports optional filtering by department using query parameter.



# Test 3: Get Employee by ID
## Input:
# GET /employees/2

## Output:
# HTTP Status: 200 OK
# {
#   "id": 2,
#   "name": "Vikram S",
#   "email": "vikram.s@ust.com",
#   "department": "Delivery",
#   "role": "Manager",
#   "status": "active"
# }
### Comment:
# Retrieves a single employee record by ID. Returns 404 if not found.



# Test 4: Update Employee
## Input:
# PUT /employees/2
# {
#   "id": 2,
#   "name": "Vikram Singh",
#   "email": "vikram.s@ust.com",
#   "department": "Delivery",
#   "role": "Senior Manager",
#   "status": "active"
# }

## Output:
# HTTP Status: 200 OK
# {
#   "id": 2,
#   "name": "Vikram Singh",
#   "email": "vikram.s@ust.com",
#   "department": "Delivery",
#   "role": "Senior Manager",
#   "status": "active"
# }
### Comment:
# Updates employee details. Validates duplicate email before saving changes.


# Test 5: Delete Employee
## Input:
# DELETE /employees/3

## Output:
# HTTP Status: 200 OK
# {
#   "detail": "Employee deleted"
# }
### Comment:
# Removes employee record by ID. Returns 404 if employee does not exist.



# Test 6: Employee Check-In
## Input:
# POST /employees/1/checkin
# {
#   "date": "2025-11-24",
#   "time": "09:00:00"
# }

## Output:
# HTTP Status: 201 Created
# {
#   "employee_id": 1,
#   "date": "2025-11-24",
#   "check_in": "09:00:00",
#   "check_out": null
# }
### Comment:
# Records check-in time for an employee. Validates date/time format and prevents duplicate check-ins.

# Test 7: Employee Check-Out
## Input:
# POST /employees/1/checkout
# {
#   "date": "2025-11-24",
#   "time": "17:30:00"
# }

## Output:
# HTTP Status: 200 OK
# {
#   "employee_id": 1,
#   "date": "2025-11-24",
#   "check_in": "09:00:00",
#   "check_out": "17:30:00"
# }
### Comment:
# Records check-out time. Requires check-in first and prevents duplicate check-outs.


# Test 8: Create Leave Request
## Input:
# POST /employees/2/leave-requests
# {
#   "from_date": "2025-12-01",
#   "to_date": "2025-12-05",
#   "reason": "Vacation"
# }

## Output:
# HTTP Status: 201 Created
# {
#   "leave_id": 1,
#   "employee_id": 2,
#   "from_date": "2025-12-01",
#   "to_date": "2025-12-05",
#   "reason": "Vacation",
#   "status": "pending"
# }
### Comment:
# Creates a leave request for an employee. Validates date format and ensures from_date ≤ to_date.



# Test 9: List Leave Requests for Employee
## Input:
# GET /employees/2/leave-requests

## Output:
# HTTP Status: 200 OK
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
### Comment:
# Returns all leave requests for a given employee. Returns 404 if employee not found.
