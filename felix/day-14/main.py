from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime, date, time

app = FastAPI(title="UST Employee API")

# Auto-increment counters for employee IDs and leave IDs
next_emp_id = 4
next_leave_id = 1

# ---------------------- DATA MODELS ----------------------

class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "active"  # Default employee status
    

class AttendanceRecord(BaseModel):
    employee_id: int
    date: date
    check_in: time = None
    check_out: time = None
    

class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: date = None
    to_date: date = None
    reason: str
    status: str = "pending"  # default leave request status
    

class EmailExistedError(Exception):
    """Custom exception for email duplication."""
    pass


# ---------------------- IN-MEMORY STORAGE ----------------------

# predefined employee list
employee_list: List[Employee] = [
    { "id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com",
      "department": "Engineering", "role": "Engineer", "status": "active" },

    { "id": 2, "name": "Vikram S", "email": "vikram.s@ust.com",
      "department": "Delivery", "role": "Manager", "status": "active" },

    { "id": 3, "name": "Meera N", "email": "meera.n@ust.com",
      "department": "HR", "role": "HR", "status": "active" }
]

# list to store attendance
attendance: List[AttendanceRecord] = []

# list to store leave requests
leaves: List[LeaveRequest] = []


# ---------------------- EMPLOYEE CRUD ----------------------

@app.post("/employees")
def create_employee(employee: Employee):
    """
    Create a new employee.
    Checks if email already exists; if yes, raises 409 error.
    """
    try:
        email = employee.email
        for i in employee_list:
            if email == i["email"]:
                raise EmailExistedError

        global next_emp_id
        employee.id = next_emp_id
        next_emp_id += 1

        employee_list.append(employee)
        return {"Employee Created: ": employee}

    except EmailExistedError:
        raise HTTPException(status_code=409, detail="Email already exist")


@app.get("/employees")
def list_employee(department: str = "not selected"):
    """
    List all employees.
    If department is specified, filter employees by department.
    """
    emp = []
    if department == "not selected":
        return employee_list
    else:
        for i in employee_list:
            if i["department"] == department:
                emp.append(i)
        return emp
    

@app.get("/employees/{id}")
def get_employee(id: int):
    """Retrieve employee by ID."""
    for i in employee_list:
        if i["id"] == id:
            return i
    raise HTTPException(status_code=404, detail="Employee not found")


@app.put("/employees/{id}")
def update_employee(id: int, employee: Employee):
    """
    Update employee details.
    Prevents email duplication.
    """
    try:
        email = employee.email
        for i in range(len(employee_list)):
            # check if email already exists
            if email == employee_list[i]["email"]:
                raise EmailExistedError
    except EmailExistedError:
        raise HTTPException(status_code=409, detail="Email already exist")

    for i in range(len(employee_list)):
        if employee_list[i]["id"] == id:
            employee_list[i] = employee
            return {"Employee updated": employee}

    raise HTTPException(status_code=404, detail="Employee not found")


@app.delete("/employees/{id}")
def delete_employee(id: int):
    """Delete an employee by ID."""
    for i in range(len(employee_list)):
        if employee_list[i]["id"] == id:
            emp = employee_list.pop(i)
            return {"Employee Deleted: ": emp}
    raise HTTPException(status_code=404, detail="Employee not found")


# ---------------------- ATTENDANCE ----------------------

@app.post("/employees/{id}/check_in")
def check_in(id: int):
    """
    Mark attendance check-in.
    Prevents multiple check-ins on the same day.
    """
    current_time = datetime.now().time()
    current_date = date.today()

    check_in_data = AttendanceRecord(
        employee_id=id,
        date=current_date,
        check_in=current_time
    )

    # prevent multiple check-ins for today
    for i in attendance:
        if i["date"] == current_date and i["employee_id"] == id:
            raise HTTPException(status_code=409, detail="Already checked in")

    attendance.append(check_in_data.__dict__)
    return {"Attendance": attendance}


@app.post("/employee/{id}/checkout")
def checkout(id: int):
    """
    Mark checkout time for today's attendance.
    Requires check-in to be already done.
    """
    current_time = datetime.now().time()
    current_date = date.today()

    for i in range(len(attendance)):
        if attendance[i]["employee_id"] == id:
            # must have check-in first
            if attendance[i]["check_in"] is None:
                raise HTTPException(status_code=400, detail="Check-in required before checkout")
            # prevent multiple checkouts
            elif attendance[i]["check_out"] is not None:
                raise HTTPException(status_code=409, detail="Already checked out")
            else:
                attendance[i]["check_out"] = current_time
                return attendance[i]

    raise HTTPException(status_code=404, detail="Employee not found")


# ---------------------- LEAVE MANAGEMENT ----------------------

@app.post("/employees/{id}/leave-requests")
def leave_request(id: int, from_date: date, to_date: date, reason: str):
    """
    Create a leave request for an employee.
    Validates date range.
    """
    if from_date > to_date:
        raise HTTPException(status_code=400, detail="From date is after to date")

    global next_leave_id

    leave = LeaveRequest(
        leave_id=next_leave_id,
        employee_id=id,
        from_date=from_date,
        to_date=to_date,
        reason=reason
    )

    leaves.append(leave.__dict__)
    next_leave_id += 1

    # RETURN the response, do not raise it
    return {"status": 201, "message": "Leave request created"}


@app.get("/employees/{id}/leave-requests")
def leave_request(id: int):
    """Retrieve all leave requests for a specific employee."""
    req = []
    for i in leaves:
        if i["employee_id"] == id:
            req.append(i)

    if req:
        return req
    else:
        raise HTTPException(status_code=404, detail="Employee not found")
