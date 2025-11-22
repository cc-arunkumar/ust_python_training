
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime

# Initialize FastAPI app
app = FastAPI(title="UST Employee API")

# Global counters for IDs
next_emp_id = 4
next_leave_id = 0

# -----------------------------
# MODELS
# -----------------------------

class Employee(BaseModel):
    """Employee model with default status as active"""
    id: int = next_emp_id
    name: str
    email: str
    department: str
    role: str
    status: str = "active"

class AttendanceRecord(BaseModel):
    """Attendance record model"""
    employee_id: int
    date: datetime.date
    check_in: datetime.time
    check_out: datetime.time | None = None  # optional check_out

class LeaveRequest(BaseModel):
    """Leave request model"""
    leave_id: int = next_leave_id
    employee_id: int
    from_date: datetime.date
    to_date: datetime.date   # FIXED: should be date, not time
    reason: str
    status: str = "pending"

# -----------------------------
# IN-MEMORY DATA STORAGE
# -----------------------------

employees: List[dict] = [
    {"id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active"},
    {"id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active"},
    {"id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department": "HR", "role": "HR", "status": "active"}
]

attendance: List[dict] = []
leaves: List[dict] = []

# -----------------------------
# EMPLOYEE ENDPOINTS
# -----------------------------

@app.post("/employees")
def create_employee(employee: Employee):
    """Create a new employee if email is unique"""
    for emp in employees:
        if employee.email == emp['email']:
            raise HTTPException(status_code=409, detail="Email Already Exists")

    global next_emp_id
    employee.id = next_emp_id
    next_emp_id += 1
    employees.append(employee.dict())  # store as dict
    return {"Employee Created": employee}

@app.get("/employees")
def get_all_employees(department: str = ""):
    """Retrieve all employees or filter by department"""
    if not department:
        return employees
    filtered = [emp for emp in employees if emp['department'] == department]
    if filtered:
        return filtered
    return {"details": "Employee not found in Department"}

@app.get("/employees/{id}")
def get_emp_id(id: int):
    """Retrieve employee by ID"""
    for emp in employees:
        if emp['id'] == id:
            return emp
    return {"details": "Employee Not Found!"}

@app.put("/employees/{id}", response_model=Employee)
def update_employee(id: int, employee: Employee):
    """Update employee details by ID"""
    for emp in employees:
        if emp['id'] == id:
            # Check email uniqueness excluding current employee
            for emp_check in employees:
                if employee.email == emp_check['email'] and emp_check['id'] != id:
                    raise HTTPException(status_code=409, detail="Email Already Exists")
            emp.update(employee.dict())
            return employee
    raise HTTPException(status_code=404, detail="ID Not Found")

@app.delete("/employees/{id}")
def delete_employee(id: int):
    """Delete employee by ID"""
    for index, emp in enumerate(employees):
        if emp['id'] == id:
            employees.pop(index)
            return {"detail": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee Not Found")

# -----------------------------
# ATTENDANCE ENDPOINTS
# -----------------------------

@app.post("/employees/{id}/check_in")
def check_in(id: int):
    """Employee check-in"""
    current_time = datetime.datetime.now().time()
    current_date = datetime.date.today()

    # Prevent duplicate check-in for same day
    for record in attendance:
        if record["date"] == current_date and record["employee_id"] == id:
            raise HTTPException(status_code=409, detail="Already checked in")

    check_in_data = AttendanceRecord(employee_id=id, date=current_date, check_in=current_time)
    attendance.append(check_in_data.dict())
    return {"Attendance": attendance}

@app.post("/employees/{id}/checkout")
def checkout(id: int):
    """Employee checkout"""
    current_time = datetime.datetime.now().time()
    for record in attendance:
        if record["employee_id"] == id:
            if record["check_in"] is None:
                raise HTTPException(status_code=400, detail="Check-in required before checkout")
            if record.get("check_out"):
                raise HTTPException(status_code=409, detail="Already checked out")
            record["check_out"] = current_time
            return record
    raise HTTPException(status_code=404, detail="Employee not found")

# -----------------------------
# LEAVE REQUEST ENDPOINTS
# -----------------------------

@app.post("/employees/{id}/leave-requests")
def create_leave_request(id: int, from_date: datetime.date, to_date: datetime.date, reason: str):
    """Create a leave request for an employee"""
    if from_date > to_date:
        raise HTTPException(status_code=400, detail="From date is after to date")

    global next_leave_id
    leave = LeaveRequest(leave_id=next_leave_id, employee_id=id, from_date=from_date, to_date=to_date, reason=reason)
    leaves.append(leave.dict())
    next_leave_id += 1
    return {"status": 201, "message": "Leave request created"}

@app.get("/employees/{id}/leave-requests")
def get_leave_requests(id: int):
    """Retrieve all leave requests for a specific employee"""
    req = [leave for leave in leaves if leave["employee_id"] == id]
    if req:
        return req
    raise HTTPException(status_code=404, detail="Employee not found")
