from fastapi import FastAPI, HTTPException
from typing import List
import datetime
from pydantic import BaseModel

# -----------------------------
# FastAPI Application
# -----------------------------
app = FastAPI(title="UST Employee API")

# -----------------------------
# Data Models
# -----------------------------
class Employee(BaseModel):
    """
    Employee schema:
    - id: unique employee ID
    - name: employee name
    - email: must be unique
    - department: department name
    - role: job role
    - status: defaults to "active"
    """
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "active"


class AttendenceRecord(BaseModel):
    """
    Attendance schema:
    - employee_id: ID of employee
    - date: date of attendance
    - check_in: optional time
    - check_out: optional time
    """
    employee_id: int
    date: datetime.date
    check_in: datetime.time = None
    check_out: datetime.time = None


class LeaveRequest(BaseModel):
    """
    Leave request schema:
    - leave_id: auto-generated unique ID
    - employee_id: ID of employee
    - from_date: start date of leave
    - to_date: end date of leave
    - reason: reason for leave
    - status: defaults to "pending"
    """
    leave_id: int = 0
    employee_id: int = 0
    from_date: datetime.date
    to_date: datetime.date
    reason: str
    status: str = "pending"


# -----------------------------
# In-Memory Storage
# -----------------------------
leaves: List[LeaveRequest] = []
attendence: List[AttendenceRecord] = []
employees: List[Employee] = [
    Employee(id=1, name="Asha Rao", email="asha.rao@ust.com", department="Engineering", role="Engineer", status="active"),
    Employee(id=2, name="Vikram S", email="vikram.s@ust.com", department="Delivery", role="Manager", status="active"),
    Employee(id=3, name="Meera N", email="meera.n@ust.com", department="HR", role="HR", status="active")
]

next_e_id = 3
next_l_id = 0


# -----------------------------
# Employee CRUD
# -----------------------------

@app.post("/employees", response_model=Employee)
def create_emp(emp: Employee):
    """
    Create a new employee.
    Prevents duplicate email.

    Sample Output:
    POST /employees
    Request:
    {"name":"Ravi","email":"ravi@ust.com","department":"Finance","role":"Analyst"}
    Response:
    {"id":4,"name":"Ravi","email":"ravi@ust.com","department":"Finance","role":"Analyst","status":"active"}
    """
    for row in employees:
        if row.email == emp.email:
            raise HTTPException(status_code=409, detail="Conflict: email already exists")
    global next_e_id
    next_e_id += 1
    emp.id = next_e_id
    employees.append(emp)
    return emp


@app.get("/employees", response_model=List[Employee])
def display_all(dep: str = ""):
    """
    Get all employees or filter by department.

    Sample Output:
    GET /employees
    [
      {"id":1,"name":"Asha Rao","email":"asha.rao@ust.com","department":"Engineering","role":"Engineer","status":"active"},
      {"id":2,"name":"Vikram S","email":"vikram.s@ust.com","department":"Delivery","role":"Manager","status":"active"}
    ]

    GET /employees?dep=HR
    [
      {"id":3,"name":"Meera N","email":"meera.n@ust.com","department":"HR","role":"HR","status":"active"}
    ]
    """
    if dep == "":
        return employees
    return [row for row in employees if row.department == dep]


@app.get("/employees/{id}", response_model=Employee)
def search_by_id(id: int):
    """
    Get employee by ID.

    Sample Output:
    GET /employees/1
    {"id":1,"name":"Asha Rao","email":"asha.rao@ust.com","department":"Engineering","role":"Engineer","status":"active"}

    Error Case:
    GET /employees/99
    Response: 404 {"detail":"Employee not found"}
    """
    try:
        return employees[id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail="Employee not found")


@app.post("/employees/{id}", response_model=Employee)
def update_emp(id: int, emp: Employee):
    """
    Update employee details by ID.
    Prevents duplicate email.

    Sample Output:
    POST /employees/1
    Request:
    {"id":1,"name":"Asha Rao","email":"asha.rao@ust.com","department":"Engineering","role":"Senior Engineer","status":"active"}
    Response:
    {"id":1,"name":"Asha Rao","email":"asha.rao@ust.com","department":"Engineering","role":"Senior Engineer","status":"active"}
    """
    try:
        for row in employees:
            if emp.email == row.email and row.id != id:
                raise HTTPException(status_code=409, detail="Email already exists")
        emp.id = id
        employees[id - 1] = emp
        return emp
    except IndexError:
        raise HTTPException(status_code=404, detail="Employee not found")


@app.delete("/employees/{id}")
def delete_byid(id: int):
    """
    Delete employee by ID.

    Sample Output:
    DELETE /employees/1
    {"detail":"Employee deleted"}

    Error Case:
    DELETE /employees/99
    Response: 404 {"detail":"Employee not found"}
    """
    try:
        employees.pop(id - 1)
        return {"detail": "Employee deleted"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Employee not found")


# -----------------------------
# Attendance
# -----------------------------

@app.post("/employees/{id}/checkin")
def check_in(id: int, attend: AttendenceRecord):
    """
    Employee check-in.
    Prevents duplicate check-in for same date.

    Sample Output:
    POST /employees/1/checkin
    Request:
    {"date":"2025-11-24","check_in":"09:00:00"}
    Response:
    {"detail":"Check-in successful","record":{"employee_id":1,"date":"2025-11-24","check_in":"09:00:00","check_out":null}}
    """
    if not any(emp.id == id for emp in employees):
        raise HTTPException(status_code=404, detail="Employee not found")

    for att in attendence:
        if att.employee_id == id and att.date == attend.date and att.check_in is not None:
            raise HTTPException(status_code=409, detail="Already checked in")

    attend.employee_id = id
    attendence.append(attend)
    return {"detail": "Check-in successful", "record": attend}


@app.put("/employees/{id}/checkout")
def checkout(id: int, attend: AttendenceRecord):
    """
    Employee checkout.
    Requires prior check-in.

    Sample Output:
    PUT /employees/1/checkout
    Request:
    {"date":"2025-11-24","check_out":"18:00:00"}
    Response:
    {"detail":"Checkout successful","record":{"employee_id":1,"date":"2025-11-24","check_in":"09:00:00","check_out":"18:00:00"}}
    """
    if not any(emp.id == id for emp in employees):
        raise HTTPException(status_code=404, detail="Employee not found")

    for att in attendence:
        if att.employee_id == id and att.date == attend.date:
            if att.check_in is None:
                raise HTTPException(status_code=400, detail="Check-in required before checkout")
            if att.check_out is not None:
                raise HTTPException(status_code=409, detail="Already checked out")

            att.check_out = attend.check_out
            return {"detail": "Checkout successful", "record": att}

    raise HTTPException(status_code=404, detail="No check-in record found for this date")


# -----------------------------
# Leave Requests
# -----------------------------

@app.post("/employees/{id}/leave-requests", response_model=LeaveRequest)
def create_leave(id: int, leave: LeaveRequest):
    """
    Create a leave request.
    Validates date range.

    Sample Output:
    POST /employees/1/leave-requests
    Request:
    {"from_date":"2025-11-25","to_date":"2025-11-27","reason":"Medical"}
    Response:
    {"leave_id":1,"employee_id":1,"from_date":"2025-11-25","to_date":"2025-11-27","reason":"Medical","status":"pending"}
    """
    global next_l_id
    next_l_id += 1
    leave.leave_id = next_l_id
    leave.employee_id = id
    if leave.from_date > leave.to_date:
        raise HTTPException(status_code=400, detail="to date cannot be less than from date")
    leaves.append(leave)
    return leave
    
# -----------------------------
# Get Leave Requests for Employee
# -----------------------------
@app.get("/employees/{id}/leave-requests", response_model=List[LeaveRequest])
def display_all(id: int):
    """
    Fetch all leave requests for a given employee ID.
    - Validates that the employee exists.
    - Returns a list of leave requests belonging to that employee.
    - Raises 404 if employee not found.

    Sample Output:
    GET /employees/1/leave-requests
    [
      {
        "leave_id": 1,
        "employee_id": 1,
        "from_date": "2025-11-25",
        "to_date": "2025-11-27",
        "reason": "Medical",
        "status": "pending"
      },
      {
        "leave_id": 2,
        "employee_id": 1,
        "from_date": "2025-12-01",
        "to_date": "2025-12-05",
        "reason": "Vacation",
        "status": "pending"
      }
    ]

    Error Case:
    GET /employees/99/leave-requests
    Response: 404 {"detail":"Employee not found"}
    """
    new_li = []
    flag = True

    # Check if employee exists
    for emp in employees:
        if emp.id == id:
            flag = False

    if not flag:
        # Collect all leave requests for this employee
        for leave in leaves:
            if leave.employee_id == id:
                new_li.append(leave)
    else:
        raise HTTPException(status_code=404, detail="Employee not found")

    return new_li


    



