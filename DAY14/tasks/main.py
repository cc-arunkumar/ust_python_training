# Import required libraries
from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(title="UST Employee API")

# -----------------------------
# Data Models
# -----------------------------

# Model for adding a new employee (input only, no ID/status)
class EmpAdd(BaseModel):
    name: str
    email: str
    department: str
    role: str

# Full Employee model (includes ID and status)
class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "active"   # Default status is active

# Attendance record model
class Attendance(BaseModel):
    employee_id: int
    date: str
    check_in: Optional[str] = None
    check_out: Optional[str] = None

# Leave request model (stored in system)
class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: str
    to_date: str
    reason: str
    status: str = "pending"

# Model for creating a leave request (input only)
class Reqleave(BaseModel):
    from_date: str
    to_date: str
    reason: str

# Model for check-in/check-out data
class CheckData(BaseModel):
    date: str
    time: str

# -----------------------------
# In-Memory Storage
# -----------------------------
employees = [
    {"id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active"},
    {"id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active"},
    {"id": 3, "name": "Meera N", "email": "meer.n@ust.com", "department": "HR", "role": "HR", "status": "active"}
]
next_emp_id = 4   # Auto-increment employee ID
attendance = []   # Stores check-in/out records
leaves = []       # Stores leave requests
next_leave_id = 1 # Auto-increment leave ID

# -----------------------------
# Helper Function
# -----------------------------
def find_employee(emp_id):
    """Find employee by ID, return dict or None"""
    for e in employees:
        if e["id"] == emp_id:
            return e
    return None

# -----------------------------
# Employee CRUD Endpoints
# -----------------------------

@app.post("/employees", status_code=201)
def create_employee(emp: EmpAdd):
    """Create a new employee"""
    global next_emp_id
    # Prevent duplicate emails
    for e in employees:
        if e["email"] == emp.email:
            raise HTTPException(409, "Email already exists")
    new_emp = {
        "id": next_emp_id,
        "name": emp.name,
        "email": emp.email,
        "department": emp.department,
        "role": emp.role,
        "status": "active"
    }
    next_emp_id += 1
    employees.append(new_emp)
    return new_emp

@app.get("/employees")
def list_emp(department: str = None):
    """List all employees, optionally filter by department"""
    if department:
        return [e for e in employees if e["department"] == department]
    return employees

@app.get("/employees/{id}")
def get_emp(id: int):
    """Get employee by ID"""
    emp = find_employee(id)
    if not emp:
        raise HTTPException(404, "Employee not found")
    return emp

@app.put("/employees/{id}")
def update_emp(id: int, emp: Employee):
    """Update employee details"""
    old = find_employee(id)
    if not old:
        raise HTTPException(404, "Employee not found")
    # Prevent duplicate email usage
    for e in employees:
        if e["email"] == emp.email and e["id"] != id:
            raise HTTPException(409, "Email already exists")
    old.update(emp.dict())
    return old

@app.delete("/employees/{id}")
def delete_emp(id: int):
    """Delete employee by ID"""
    emp = find_employee(id)
    if not emp:
        raise HTTPException(404, "Employee not found")
    employees.remove(emp)
    return {"detail": "Employee deleted"}

# -----------------------------
# Attendance Endpoints
# -----------------------------

@app.post("/employees/{id}/checkin", status_code=201)
def check_in(id: int, data: CheckData):
    """Employee check-in"""
    if not find_employee(id):
        raise HTTPException(404, "Employee not found")
    # Validate date/time format
    try:
        datetime.strptime(data.date, "%Y-%m-%d")
        datetime.strptime(data.time, "%H:%M:%S")
    except:
        raise HTTPException(400, "Invalid date or time format")
    # Check if already checked in
    for a in attendance:
        if a["employee_id"] == id and a["date"] == data.date:
            if a["check_in"]:
                raise HTTPException(409, "Already checked in")
            a["check_in"] = data.time
            return a
    # New record
    record = {
        "employee_id": id,
        "date": data.date,
        "check_in": data.time,
        "check_out": None
    }
    attendance.append(record)
    return record

@app.post("/employees/{id}/checkout")
def check_out(id: int, data: CheckData):
    """Employee check-out"""
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

# -----------------------------
# Leave Request Endpoints
# -----------------------------

@app.post("/employees/{id}/leave-requests", status_code=201)
def create_leave(id: int, data: Reqleave):
    """Create a leave request"""
    global next_leave_id
    if not find_employee(id):
        raise HTTPException(404, "Employee not found")
    # Validate date format
    try:
        f = datetime.strptime(data.from_date, "%Y-%m-%d")
        t = datetime.strptime(data.to_date, "%Y-%m-%d")
    except:
        raise HTTPException(400, "Invalid date format")
    if f > t:
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
    """List all leave requests for an employee"""
    if not find_employee(id):
        raise HTTPException(404, "Employee not found")
    return [l for l in leaves if l["employee_id"] == id]



"""SAMPLE OUTPUT
1. CREATE EMPLOYEE (POST /employees)
{
  "id": 4,
  "name": "Gowtham",
  "email": "gowtham@ust.com",
  "department": "Engineering",
  "role": "Developer",
  "status": "active"
}
2. LIST ALL EMPLOYEES (GET /employees)
[
  {
    "id": 1,
    "name": "Asha Rao",
    "email": "asha.rao@ust.com",
    "department": "Engineering",
    "role": "Engineer",
    "status": "active"
  },
  {
    "id": 2,
    "name": "Vikram S",
    "email": "vikram.s@ust.com",
    "department": "Delivery",
    "role": "Manager",
    "status": "active"
  },
  {
    "id": 3,
    "name": "Meera N",
    "email": "meer.n@ust.com",
    "department": "HR",
    "role": "HR",
    "status": "active"
  },
  {
    "id": 4,
    "name": "Gowtham",
    "email": "gowtham@ust.com",
    "department": "Engineering",
    "role": "Developer",
    "status": "active"
  }
]
3. GET EMPLOYEE BY ID (GET /employees/4)
{
  "id": 4,
  "name": "Gowtham",
  "email": "gowtham@ust.com",
  "department": "Engineering",
  "role": "Developer",
  "status": "active"
}
4. UPDATE EMPLOYEE (PUT /employees/4)
{
  "id": 4,
  "name": "Dinesh",
  "email": "dinesh@ust.com",
  "department": "Delivery",
  "role": "Manager",
  "status": "active"
}
5. DELETE EMPLOYEE (DELETE /employees/4)
{
  "detail": "Employee deleted"
}
6. CHECK-IN (POST /employees/1/checkin)
{
  "employee_id": 1,
  "date": "2025-11-24",
  "check_in": "09:00:00",
  "check_out": null
}
7. CHECK-OUT (POST /employees/1/checkout)
{
  "employee_id": 1,
  "date": "2025-11-24",
  "check_in": "09:00:00",
  "check_out": "17:30:00"
}

8. CREATE LEAVE REQUEST (POST /employees/2/leave-requests)
{
  "leave_id": 1,
  "employee_id": 2,
  "from_date": "2025-11-25",
  "to_date": "2025-11-27",
  "reason": "Personal work",
  "status": "pending"
}
9. LIST LEAVE REQUESTS (GET /employees/2/leave-requests)
[
  {
    "leave_id": 1,
    "employee_id": 2,
    "from_date": "2025-11-25",
    "to_date": "2025-11-27",
    "reason": "Personal work",
    "status": "pending"
  }
]


"""