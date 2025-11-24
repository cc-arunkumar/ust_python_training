from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI(title="UST Employee API")

# -----------------------------
# Data Models
# -----------------------------

class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "active"   # Default status is active

class AttendanceRecord(BaseModel):
    employee_id: int
    date: str
    check_in: Optional[str] = None
    check_out: Optional[str] = None

class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: str
    to_date: str
    reason: str
    status: str = "pending"  # Default status is pending

# -----------------------------
# In-memory storage
# -----------------------------
employees: List[Employee] = [
    {"id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active"},
    {"id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active"},
    {"id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department": "HR", "role": "HR", "status": "active"}
]

attendance: List[AttendanceRecord] = []
leaves: List[LeaveRequest] = []

next_emp_id = 4
next_leave_id = 1

# -----------------------------
# Employee CRUD Endpoints
# -----------------------------

@app.post("/employees")
def create_employee(emp: Employee):
    """
    Create a new employee.
    """
    global next_emp_id
    for e in employees:
        if e["email"] == emp.email:
            raise HTTPException(status_code=409, detail="Email already exists")

    new_emp = {
        "id": next_emp_id,
        "name": emp.name,
        "email": emp.email,
        "department": emp.department,
        "role": emp.role,
        "status": emp.status
    }
    employees.append(new_emp)
    next_emp_id += 1
    return {"Employee created": new_emp}


@app.get("/employee")
def list_employees(department: Optional[str] = None):
    """
    List all employees.
    - Optional filter by department.
    """
    if department:
        result = [e for e in employees if e["department"] == department]
        return result
    return employees


@app.get("/employee/{id}")
def getById(id: int):
    """
    Get employee details by ID.
    """
    for e in employees:
        if e["id"] == id:
            return e
    raise HTTPException(status_code=404, detail="Employee not found")


@app.put("/employee/{id}")
def update(id: int, emp: Employee):
    """
    Update employee details.
    - Prevents duplicate email usage.
    """
    for e in employees:
        if e["id"] == id:
            for other in employees:
                if other["email"] == emp.email and other["id"] != id:
                    raise HTTPException(status_code=409, detail="Email already exists")
            e.update({
                "name": emp.name,
                "email": emp.email,
                "department": emp.department,
                "role": emp.role,
                "status": emp.status
            })
            return e
    raise HTTPException(status_code=404, detail="Employee not found")


@app.delete("/employee/{id}")
def delete(id: int):
    """
    Delete employee by ID.
    """
    for e in employees:
        if e["id"] == id:
            employees.remove(e)
            return {"detail": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")

# -----------------------------
# Attendance Endpoints
# -----------------------------

@app.post("/employee/{id}/checkin")
def check_in(id: int, data: dict):
    """
    Employee check-in.
    - Prevents multiple check-ins on same date.
    """
    for e in employees:
        if e["id"] == id:
            for r in attendance:
                if r["employee_id"] == id and r["date"] == data["date"]:
                    if r["check_in"]:
                        raise HTTPException(status_code=409, detail="Already checked in")
                    r["check_in"] = data["time"]
                    return r
            newrecord = {
                "employee_id": id,
                "date": data["date"],
                "check_in": data["time"],
                "check_out": None
            }
            attendance.append(newrecord)
            return newrecord
    raise HTTPException(status_code=404, detail="Employee not found")


@app.post("/employee/{id}/checkout")
def check_out(id: int, data: dict):
    """
    Employee check-out.
    - Requires prior check-in.
    - Prevents multiple check-outs.
    """
    for e in employees:
        if e["id"] == id:
            for r in attendance:
                if r["employee_id"] == id and r["date"] == data["date"]:
                    if not r["check_in"]:
                        raise HTTPException(status_code=404, detail="First check in required")
                    if r["check_out"]:
                        raise HTTPException(status_code=409, detail="Already checked out")
                    r["check_out"] = data["time"]
                    return r
    raise HTTPException(status_code=404, detail="Employee not found")

# -----------------------------
# Leave Request Endpoints
# -----------------------------

@app.post("/employees/{id}/leave-requests")
def create_leave(id: int, data: dict):
    """
    Create a leave request for an employee.
    - Validates date range.
    """
    global next_leave_id
    for e in employees:
        if e["id"] == id:
            if data["from_date"] > data["to_date"]:
                raise HTTPException(status_code=400, detail="from_date must be on or before to_date")
            leave = {
                "leave_id": next_leave_id,
                "employee_id": id,
                "from_date": data["from_date"],
                "to_date": data["to_date"],
                "reason": data["reason"],
                "status": "pending"
            }
            leaves.append(leave)
            next_leave_id += 1
            return leave
    raise HTTPException(status_code=404, detail="Employee not found")


# -----------------------------
# SAMPLE INPUT/OUTPUT SUMMARY
# -----------------------------
# 1. Create Employee (POST /employees)
# Request:
# {
#   "id": 0,
#   "name": "Ravi Kumar",
#   "email": "ravi.kumar@ust.com",
#   "department": "Finance",
#   "role": "Analyst"
# }
# Response:
# {
#   "Employee created": {
#     "id": 4,
#     "name": "Ravi Kumar",
#     "email": "ravi.kumar@ust.com",
#     "department": "Finance",
#     "role": "Analyst",
#     "status": "active"
#   }
# }

# 2. List Employees (GET /employee)
# Response:
# [
#   {"id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active"},
#   {"id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active"},
#   {"id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department": "HR", "role": "HR", "status": "active"},
#   {"id": 4, "name": "Ravi Kumar", "email": "ravi.kumar@ust.com", "department": "Finance", "role": "Analyst", "status": "active"}
# ]

# 3. Employee Check-in (POST /employee/1/checkin)
# Request:
# {
#   "date": "2025-11-24",
#   "time": "09:00"
# }
# Response:
# {
#   "employee_id": 1,
#   "date": "2025-11-24",
#   "check_in": "09:00",
#   "check_out": null
# }

# 4. Employee Check-out (POST /employee/1/checkout)
# Request:
# {
#   "date": "2025-11-24",
#   "time": "17:00"
# }
# Response:
# {
#   "employee_id": 1,
#   "date": "2025-11-24",
#   "check_in": "09:00",
#   "check_out": "17:00"
# }

# 5. Leave Request (POST /employees/1/leave-requests)
# Request:
# {
#   "from_date": "2025-12-01",
#   "to_date": "2025-12-05",
#   "reason": "Family function"
# }
# Response:
# {
#   "leave_id": 1,
#   "employee_id": 1,
#   "from_date": "