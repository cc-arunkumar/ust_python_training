from fastapi import FastAPI, HTTPException  # Import FastAPI and HTTPException for error handling
from pydantic import BaseModel  # Import BaseModel from Pydantic for data validation
from typing import List  # Import List from typing to specify lists in type hints
from datetime import datetime, date, time  # Import datetime, date, and time for date/time handling

# Initialize the FastAPI app with the title "UST Employee API"
app = FastAPI(title="UST Employee API")

# ---------------------- Counters ----------------------
# Variables to generate unique IDs for employees and leave requests
next_emp_id = 4
next_leave_id = 1

# ---------------------- MODELS ----------------------

# Employee model to define the structure of an employee
class Employee(BaseModel):
    id: int  # Employee ID
    name: str  # Employee name
    email: str  # Employee email
    department: str  # Department of the employee
    role: str  # Role of the employee
    status: str = "active"  # Default status is "active"

# Attendance model to store attendance records
class Attendance(BaseModel):
    employee_id: int  # Employee ID
    date: date  # Date of attendance
    check_in: time | None = None  # Check-in time (optional)
    check_out: time | None = None  # Check-out time (optional)

# Leave model to store leave requests for employees
class Leave(BaseModel):
    leave_id: int  # Leave request ID
    employee_id: int  # Employee ID who requested the leave
    from_date: date  # Start date of leave
    to_date: date  # End date of leave
    reason: str  # Reason for the leave
    status: str = "pending"  # Default status of leave is "pending"

# ---------------------- STORAGE ----------------------

# In-memory list to store employee data
emp_data: List[Employee] = [
    Employee(id=1, name="Asha Rao", email="asha.rao@ust.com", department="Engineering", role="Engineer", status="active"),
    Employee(id=2, name="Vikram S", email="vikram.s@ust.com", department="Delivery", role="Manager", status="active"),
    Employee(id=3, name="Meera N", email="meera.n@ust.com", department="HR", role="HR", status="active")
]

# In-memory list to store attendance records
attendance_records: List[Attendance] = []

# In-memory list to store leave requests
leave_records: List[Leave] = []

# ---------------------- EMPLOYEE CRUD ----------------------

# Add a new employee
@app.post("/employees", response_model=Employee, status_code=201)
def add_employee(emp: Employee):
    global next_emp_id
    # Check if the email already exists in the database
    for e in emp_data:
        if e.email == emp.email:
            raise HTTPException(status_code=409, detail="Email already exists")
    # Assign a new ID and add the employee to the list
    emp.id = next_emp_id
    next_emp_id += 1
    emp_data.append(emp)
    return emp

# Get all employees, optionally filtered by department
@app.get("/employees", response_model=List[Employee])
def get_all_employees(department: str | None = None):
    if department:
        # Return employees from the specified department
        return [e for e in emp_data if e.department == department]
    # Return all employees if no department filter is applied
    return emp_data

# Get a specific employee by their ID
@app.get("/employees/{emp_id}", response_model=Employee)
def get_employee(emp_id: int):
    # Find the employee by ID and return it
    for e in emp_data:
        if e.id == emp_id:
            return e
    raise HTTPException(status_code=404, detail="Employee not found")

# Modify an existing employee’s details
@app.put("/employees/{emp_id}", response_model=Employee)
def modify_employee(emp_id: int, emp: Employee):
    # Check if another employee has the same email
    for e in emp_data:
        if e.email == emp.email and e.id != emp_id:
            raise HTTPException(status_code=409, detail="Email already exists")
    # Find the employee and update their details
    for i in range(len(emp_data)):
        if emp_data[i].id == emp_id:
            emp.id = emp_id
            emp_data[i] = emp
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

# Delete an employee by ID
@app.delete("/employees/{emp_id}")
def remove_employee(emp_id: int):
    # Find the employee by ID and remove them from the list
    for i in range(len(emp_data)):
        if emp_data[i].id == emp_id:
            emp_data.pop(i)
            return {"detail": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")

# ---------------------- ATTENDANCE ----------------------

# Check-in for an employee
@app.post("/employees/{emp_id}/checkin", response_model=Attendance, status_code=201)
def checkin(emp_id: int):
    today = date.today()  # Get today's date
    now = datetime.now().time()  # Get the current time
    # Check if the employee has already checked in today
    for rec in attendance_records:
        if rec.employee_id == emp_id and rec.date == today and rec.check_in is not None:
            raise HTTPException(status_code=409, detail="Already checked in")
    # Create a new attendance record for the employee
    new_rec = Attendance(employee_id=emp_id, date=today, check_in=now)
    attendance_records.append(new_rec)
    return new_rec

# Check-out for an employee
@app.post("/employees/{emp_id}/checkout", response_model=Attendance)
def checkout(emp_id: int):
    today = date.today()  # Get today's date
    now = datetime.now().time()  # Get the current time
    # Find the attendance record for the employee
    for rec in attendance_records:
        if rec.employee_id == emp_id and rec.date == today:
            # Check if the employee has checked in before checking out
            if rec.check_in is None:
                raise HTTPException(status_code=400, detail="Check-in required before checkout")
            # Check if the employee has already checked out
            if rec.check_out is not None:
                raise HTTPException(status_code=409, detail="Already checked out")
            # Update the check-out time
            rec.check_out = now
            return rec
    raise HTTPException(status_code=404, detail="Attendance record not found")

# ---------------------- LEAVE ----------------------

# Request leave for an employee
@app.post("/employees/{emp_id}/leave-requests", response_model=Leave, status_code=201)
def request_leave(emp_id: int, from_date: date, to_date: date, reason: str):
    global next_leave_id
    # Ensure that the from_date is before or equal to the to_date
    if from_date > to_date:
        raise HTTPException(status_code=400, detail="from_date must be on or before to_date")
    # Create a new leave request
    new_leave = Leave(
        leave_id=next_leave_id,
        employee_id=emp_id,
        from_date=from_date,
        to_date=to_date,
        reason=reason,
        status="pending"
    )
    leave_records.append(new_leave)  # Add the leave request to the list
    next_leave_id += 1  # Increment the leave request ID
    return new_leave

# List all leave requests for an employee
@app.get("/employees/{emp_id}/leave-requests", response_model=List[Leave])
def list_leaves(emp_id: int):
    # Find all leave requests for the given employee
    result = [lr for lr in leave_records if lr.employee_id == emp_id]
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result




# output

# 1) Create Employee (POST /employees)

# Request:

# {
#     "name": "Nisha Rao",
#     "email": "nisha@ust.com",
#     "department": "Engineering",
#     "role": "QA"
# }


# Response (201):

# {
#     "id": 4,
#     "name": "Nisha Rao",
#     "email": "nisha@ust.com",
#     "department": "Engineering",
#     "role": "QA",
#     "status": "active"
# }


# Conflict (409): If the email already exists (e.g., asha.rao@ust.com):

# {
#     "detail": "Email already exists"
# }

# 2) List Employees (GET /employees)

# Request:

# GET /employees


# Response (200):

# [
#     { "id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active" },
#     { "id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active" },
#     { "id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department": "HR", "role": "HR", "status": "active" }
# ]


# Request with department filter:

# GET /employees?department=Engineering


# Response (200):

# [
#     { "id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active" }
# ]

# 3) Get Employee by ID (GET /employees/{id})

# Request:

# GET /employees/1


# Response (200):

# {
#     "id": 1,
#     "name": "Asha Rao",
#     "email": "asha.rao@ust.com",
#     "department": "Engineering",
#     "role": "Engineer",
#     "status": "active"
# }


# Not Found (404): If the employee ID doesn't exist:

# {
#     "detail": "Employee not found"
# }

# 4) Update Employee (PUT /employees/{id})

# Request:

# {
#     "name": "Asha Rao",
#     "email": "asha.rao@ust.com",
#     "department": "Engineering",
#     "role": "Sr Engineer",
#     "status": "active"
# }


# Response (200):

# {
#     "id": 1,
#     "name": "Asha Rao",
#     "email": "asha.rao@ust.com",
#     "department": "Engineering",
#     "role": "Sr Engineer",
#     "status": "active"
# }


# Conflict (409): If the email is changed to one that already exists for another employee:

# {
#     "detail": "Email already exists"
# }


# Not Found (404): If the employee ID doesn't exist:

# {
#     "detail": "Employee not found"
# }

# 5) Delete Employee (DELETE /employees/{id})

# Request:

# DELETE /employees/1


# Response (200):

# {
#     "detail": "Employee deleted"
# }


# Not Found (404): If the employee ID doesn't exist:

# {
#     "detail": "Employee not found"
# }

# 6) Check-in Attendance (POST /employees/{id}/checkin)

# Request:

# {
#     "date": "2025-11-21",
#     "time": "09:10:00"
# }


# Response (201):

# {
#     "employee_id": 1,
#     "date": "2025-11-21",
#     "check_in": "09:10:00",
#     "check_out": null
# }


# Conflict (409): If the employee has already checked in on the same day:

# {
#     "detail": "Already checked in"
# }


# Not Found (404): If the employee doesn't exist:

# {
#     "detail": "Employee not found"
# }

# 7) Check-out Attendance (POST /employees/{id}/checkout)

# Request:

# {
#     "date": "2025-11-21",
#     "time": "18:00:00"
# }


# Response (200):

# {
#     "employee_id": 1,
#     "date": "2025-11-21",
#     "check_in": "09:10:00",
#     "check_out": "18:00:00"
# }


# Bad Request (400): If the employee hasn't checked in yet:

# {
#     "detail": "Check-in required before checkout"
# }


# Conflict (409): If the employee has already checked out:

# {
#     "detail": "Already checked out"
# }


# Not Found (404): If the attendance record doesn't exist:

# {
#     "detail": "Attendance record not found"
# }

# 8) Create Leave Request (POST /employees/{id}/leave-requests)

# Request:

# {
#     "from_date": "2025-12-24",
#     "to_date": "2025-12-25",
#     "reason": "family"
# }


# Response (201):

# {
#     "leave_id": 1,
#     "employee_id": 1,
#     "from_date": "2025-12-24",
#     "to_date": "2025-12-25",
#     "reason": "family",
#     "status": "pending"
# }


# Bad Request (400): If from_date is after to_date:

# {
#     "detail": "from_date must be on or before to_date"
# }


# Not Found (404): If the employee doesn't exist:

# {
#     "detail": "Employee not found"
# }

# 9) List Leave Requests for Employee (GET /employees/{id}/leave-requests)

# Request:

# GET /employees/1/leave-requests


# Response (200):

# [
#     {
#         "leave_id": 1,
#         "employee_id": 1,
#         "from_date": "2025-12-24",
#         "to_date": "2025-12-25",
#         "reason": "family",
#         "status": "pending"
#     }
# ]


# Not Found (404): If the employee doesn't exist:

# {
#     "detail": "Employee not found"
# }