from fastapi import FastAPI, HTTPException   # Import FastAPI framework and HTTPException for error handling
from pydantic import BaseModel               # Import BaseModel for request/response validation
from typing import List, Optional            # Import typing for type hints
from datetime import datetime                # Import datetime for date/time handling

# Create FastAPI app instance
app = FastAPI(title="UST Employee API")

# Define Employee model using Pydantic
class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "active"   # Default status is active

# Define AttendanceRecord model
class AttendanceRecord(BaseModel):
    employee_id: int
    date: str
    check_in: Optional[str] = None
    check_out: Optional[str] = None

# Define LeaveRequest model
class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: str
    to_date: str
    reason: str
    status: str = "pending"   # Default status is pending

# Initial employee data stored in a list of dictionaries
employees: List[Employee] = [
    { "id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active" },
    { "id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active" },
    { "id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department": "HR", "role": "HR", "status": "active" }
]

# Empty lists for attendance and leave requests
attendance: List[AttendanceRecord] = []
leaves: List[LeaveRequest] = []

# Counters for generating new IDs
next_emp_id = 4
next_leave_id = 1

# ---------------- Employee Endpoints ----------------

@app.post("/employees")
def create_employee(emp: Employee):
    global next_emp_id
    # Check if email already exists
    for e in employees:
        if e["email"] == emp["email"]:
            raise HTTPException(status_code=409, detail="Email already exists")
    
    # Create new employee dictionary
    new_emp = {
        "id": next_emp_id,
        "name": emp["name"],
        "email": emp["email"],
        "department": emp["department"],
        "role": emp["role"]
    }
    
    employees.append(new_emp)   # Add to employee list
    next_emp_id += 1            # Increment ID counter
    return {"Employee created": new_emp}

@app.get("/employee")
def list_employees(department: Optional[str] = None):
    # If department filter is provided
    if department:
        result = []
        for e in employees:
            if e["department"] == department:
                result.append(e)
        return result
    return employees   # Return all employees

@app.get("/employee/{id}")
def getById(id: int):
    # Find employee by ID
    for e in employees:
        if e["id"] == id:
            return e
    raise HTTPException(status_code=404, detail="Employee not found")

@app.put("/employee/{id}")
def update(id: int, emp: Employee):
    # Update employee details
    for e in employees:
        if e["id"] == id:
            for other in employees:
                if other["email"] == emp["email"]:
                    raise HTTPException(status_code=409, detail="Email already exist")
            e["name"] = emp["name"]
            e["email"] = emp["email"]
            e["department"] = emp["department"]
            e["role"] = emp["role"]
            e["status"] = emp["status"]
            return e
    raise HTTPException(status_code=404, detail="Employee not found")

@app.delete("/employee/{id}")
def delete(id: int):
    # Delete employee by ID
    for e in employees:
        if e["id"] == id:
            employees.remove(e)
            return {"detail": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")

# ---------------- Attendance Endpoints ----------------

@app.post("/employee/{id}/checkin")
def check_in(id: int, data: dict):
    # Employee check-in
    for e in employees:
        if e["id"] == id:
            for r in attendance:
                if r["employee_id"] == id and r["date"] == data["date"]:
                    if r["check_in"]:
                        raise HTTPException(status_code=409, detail="Already checkin")
                    r["check_in"] = data["time"]
                    return r
        # Create new attendance record
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
    # Employee check-out
    for e in employees:
        if e["id"] == id:
            for r in attendance:
                if r["employee_id"] == id and r["date"] == data["date"]:
                    if not r["check_in"]:
                        raise HTTPException(status_code=404, detail="First checkin")
                    if r["check_out"]:
                        raise HTTPException(status_code=409, detail="already checkout")
                    r["check_out"] = data["time"]
                    return r
    raise HTTPException(status_code=404, detail="Employee not found")

# ---------------- Leave Endpoints ----------------

@app.post("/employees/{id}/leave-requests")
def create_leave(id: int, data: dict):
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

@app.get("/employees/{id}/leave-requests")
def list_leaves(id: int):
    # List leave requests for employee
    for e in employees:
        if e["id"] == id:
            result = []
            for l in leaves:
                if l["employee_id"] == id:
                    result.append(l)
            return result
    raise HTTPException(status_code=404, detail="Employee not found")

# ==================sample output====================
# {
#   "employees": [
#     {
#       "id": 1,
#       "name": "Asha Rao",
#       "email": "asha.rao@ust.com",
#       "department": "Engineering",
#       "role": "Engineer",
#       "status": "active"
#     },
#     {
#       "id": 2,
#       "name": "Vikram S",
#       "email": "vikram.s@ust.com",
#       "department": "Delivery",
#       "role": "Manager",
#       "status": "active"
#     },
#     {
#       "id": 3,
#       "name": "Meera N",
#       "email": "meera.n@ust.com",
#       "department": "HR",
#       "role": "HR",
#       "status": "active"
#     }
#   ],
#   "attendance": [
#     {
#       "employee_id": 1,
#       "date": "2025-11-24",
#       "check_in": "09:00",
#       "check_out": null
#     },
#     {
#       "employee_id": 1,
#       "date": "2025-11-24",
#       "check_in": "09:00",
#       "check_out": "17:00"
#     }
#   ],
#   "leave_requests": [
#     {
#       "leave_id": 1,
#       "employee_id": 1,
#       "from_date": "2025-11-25",
#       "to_date": "2025-11-27",
#       "reason": "Medical leave",
#       "status": "pending"
#     },
#     {
#       "leave_id": 2,
#       "employee_id": 2,
#       "from_date": "2025-12-01",
#       "to_date": "2025-12-05",
#       "reason": "Vacation",
#       "status": "pending"
#     }
#   ]
# }
