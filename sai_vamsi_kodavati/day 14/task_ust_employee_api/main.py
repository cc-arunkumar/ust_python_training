from fastapi import FastAPI, HTTPException
from typing import List
import datetime
from pydantic import BaseModel

# Initialize FastAPI app with a custom title
app = FastAPI(title="UST Employee API")

# Define the Employee model using Pydantic for validation
class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "active"  # Default status is "active"

# Define the AttendanceRecord model for checking in and checking out
class AttendenceRecord(BaseModel):
    employee_id: int
    date: datetime.date
    check_in: datetime.time = None
    check_out: datetime.time = None

# Define the LeaveRequest model for employee leave requests
class LeaveRequest(BaseModel):
    leave_id: int = 0
    employee_id: int = 0
    from_date: datetime.date
    to_date: datetime.date
    reason: str
    status: str = "pending"  # Default status is "pending"

# Initializing the lists to simulate in-memory storage
leaves: List[LeaveRequest] = []
attendence: List[AttendenceRecord] = []
employees: List[Employee] = [
    Employee(id=1, name="Asha Rao", email="asha.rao@ust.com", department="Engineering", role="Engineer", status="active"),
    Employee(id=2, name="Vikram S", email="vikram.s@ust.com", department="Delivery", role="Manager", status="active"),
    Employee(id=3, name="Meera N", email="meera.n@ust.com", department="HR", role="HR", status="active")
]

# For auto-incrementing employee and leave IDs
next_e_id = 3
next_l_id = 0

# Create a new employee
@app.post("/employees", response_model=Employee)
def create_emp(emp: Employee):
    for row in employees:
        if row.email == emp.email:
            raise HTTPException(status_code=409, detail="Conflict email already exists")
    global next_e_id
    next_e_id += 1
    emp.id = next_e_id
    employees.append(emp)
    return emp

# Display all employee details or filter by department
@app.get("/employees", response_model=List[Employee])
def display_all(dep: str = ""):
    if dep == "":
        return employees
    new_li = [row for row in employees if row.department == dep]
    return new_li

# Search for an employee by their ID
@app.get("/employees/{id}", response_model=Employee)
def search_by_id(id: int):
    try:
        return employees[id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail="Employee not found")

# Update employee details by their ID
@app.post("/employees/{id}", response_model=Employee)
def update_emp(id: int, emp: Employee):
    try:
        for row in employees:
            if emp.email == row.email and row.id != id:
                raise HTTPException(status_code=409, detail="Email already exists")
        emp.id = id
        employees[id - 1] = emp
        return emp
    except IndexError:
        raise HTTPException(status_code=404, detail="Employee not found")

# Delete an employee by ID
@app.delete("/employees/{id}")
def delete_byid(id: int):
    try:
        employees.pop(id - 1)
        return {"detail": "Employee deleted"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Employee not found")

# Check-in for an employee
@app.post("/employees/{id}/checkin")
def check_in(id: int, attend: AttendenceRecord):
    # Verify employee exists
    if not any(emp.id == id for emp in employees):
        raise HTTPException(status_code=404, detail="Employee not found")

    # Prevent duplicate check-in for the same date
    for att in attendence:
        if att.employee_id == id and att.date == attend.date and att.check_in is not None:
            raise HTTPException(status_code=409, detail="Already checked in")

    # Save the check-in record
    attend.employee_id = id
    attendence.append(attend)
    return {"detail": "Check-in successful", "record": attend}

# Checkout for an employee
@app.put("/employees/{id}/checkout")
def checkout(id: int, attend: AttendenceRecord):
    # Verify employee exists
    if not any(emp.id == id for emp in employees):
        raise HTTPException(status_code=404, detail="Employee not found")

    # Find matching attendance record
    for att in attendence:
        if att.employee_id == id and att.date == attend.date:
            if att.check_in is None:
                raise HTTPException(status_code=400, detail="Check-in required before checkout")
            if att.check_out is not None:
                raise HTTPException(status_code=409, detail="Already checked out")

            # Perform checkout
            att.check_out = attend.check_out
            return {"detail": "Checkout successful", "record": att}

    # No matching check-in found
    raise HTTPException(status_code=404, detail="No check-in record found for this date")

# Create a leave request for an employee
@app.post("/employees/{id}/leave-requests", response_model=LeaveRequest)
def create_leave(id: int, leave: LeaveRequest):
    global next_l_id
    next_l_id += 1
    leave.leave_id = next_l_id
    leave.employee_id = id
    if leave.from_date > leave.to_date:
        raise HTTPException(status_code=400, detail="To date cannot be less than from date")
    leaves.append(leave)
    return leave

# Display all leave requests for a specific employee
@app.get("/employees/{id}/leave-requests", response_model=List[LeaveRequest])
def display_leave_requests(id: int):
    new_li = [leave for leave in leaves if leave.employee_id == id]
    if not new_li:
        raise HTTPException(status_code=404, detail="No leave requests found for this employee")
    return new_li


# -----------------------------------------------------------------------------------

# Sample Output

# 1. POST /employees - Create a new employee

# Request:

# POST /employees
# Content-Type: application/json

# {
#   "name": "John Doe",
#   "email": "john.doe@ust.com",
#   "department": "Engineering",
#   "role": "Developer"
# }
# Response:

# {
#   "id": 4,
#   "name": "John Doe",
#   "email": "john.doe@ust.com",
#   "department": "Engineering",
#   "role": "Developer",
#   "status": "active"
# }


# 2. GET /employees - Retrieve all employees

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
#     "name": "John Doe",
#     "email": "john.doe@ust.com",
#     "department": "Engineering",
#     "role": "Developer",
#     "status": "active"
#   }
# ]

# 3. GET /employees/{id} - Retrieve an employee by ID

# Request:
# GET /employees/1
# Response:

# {
#   "id": 1,
#   "name": "Asha Rao",
#   "email": "asha.rao@ust.com",
#   "department": "Engineering",
#   "role": "Engineer",
#   "status": "active"
# }
# 4. POST /employees/{id}/checkin - Employee Check-in

# Request:

# POST /employees/1/checkin
# Content-Type: application/json

# {
#   "date": "2023-10-10",
#   "check_in": "09:00:00"
# }

# Response:
# {
#   "detail": "Check-in successful",
#   "record": {
#     "employee_id": 1,
#     "date": "2023-10-10",
#     "check_in": "09:00:00",
#     "check_out": null
#   }
# }
