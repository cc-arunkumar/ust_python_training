from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import date, datetime, time

# Initialize FastAPI app with a descriptive title
app = FastAPI(title="UST Employee API")

# ================================
# Data Models
# ================================

# Employee model with default status as "active"
class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "active"

# Model for updating employee details
class EmpUpdate(BaseModel):
    name: str
    email: str
    department: str
    role: str
    status: str

# Model for creating a new employee (no ID or status required)
class EmpCreate(BaseModel):
    name: str
    email: str
    department: str
    role: str

# Attendance record model
class AttendanceRecord(BaseModel):
    employee_id: int
    date: date
    check_in: time = None
    check_out: time = None

# Leave request model
class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: date
    to_date: date
    reason: str
    status: str = "pending"

# Model for creating a leave request (without ID/status)
class CreateLeave(BaseModel):
    from_date: date
    to_date: date
    reason: str

# ================================
# In-memory Data Stores
# ================================
employees: List[Employee] = [
    {"id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active"},
    {"id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active"},
    {"id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department": "HR", "role": "HR", "status": "active"}
]

attendance: List[AttendanceRecord] = []
leave_list: List[LeaveRequest] = []

next_emp = 4          # Auto-increment employee ID
next_leave_id = 1     # Auto-increment leave ID

# ================================
# Employee Endpoints
# ================================

@app.post("/employees", response_model=Employee)
def add_employee(employee: EmpCreate):
    """
    Add a new employee.
    - Checks for duplicate email.
    - Assigns auto-incremented ID.
    """
    for data in employees:
        if data["email"] == employee.email:
            raise HTTPException(status_code=409, detail="Email already exists")

    global next_emp
    new_emp = Employee(
        id=next_emp,
        name=employee.name,
        email=employee.email,
        department=employee.department,
        role=employee.role
    )
    employees.append(new_emp.__dict__)
    next_emp += 1
    return new_emp


@app.get("/employees", response_model=List[Employee])
def get_all_employees():
    """Fetch all employees."""
    return employees


@app.get("/employees/{id}", response_model=Employee)
def get_employee_by_id(id: int):
    """Fetch employee by ID. Raises 404 if not found."""
    for data in employees:
        if data["id"] == id:
            return data
    raise HTTPException(status_code=404, detail="Employee Not Found")


@app.put("/employees/{id}", response_model=Employee)
def update_employee(id: int, employee: EmpUpdate):
    """
    Update employee details.
    - Prevents duplicate email conflicts.
    - Updates record if found.
    """
    for i in range(len(employees)):
        if employees[i]["id"] != id and employees[i]["email"] == employee.email:
            raise HTTPException(status_code=409, detail="Email already exists")

    for i in range(len(employees)):
        if employees[i]["id"] == id:
            new_data = Employee(
                id=id,
                name=employee.name,
                email=employee.email,
                department=employee.department,
                role=employee.role,
                status=employee.status
            )
            employees[i] = new_data.__dict__
            return new_data

    raise HTTPException(status_code=404, detail="Employee Not Found")


@app.delete("/employees/{id}", response_model=Employee)
def delete_employee(id: int):
    """Delete employee by ID. Raises 404 if not found."""
    for i in range(len(employees)):
        if employees[i]["id"] == id:
            return employees.pop(i)
    raise HTTPException(status_code=404, detail="Employee Not Found")

# ================================
# Attendance Endpoints
# ================================

@app.post("/employees/{id}/checkin", response_model=AttendanceRecord)
def checkin(id: int):
    """
    Employee check-in.
    - Prevents multiple check-ins on the same day.
    """
    if get_employee_by_id(id):
        for i in range(len(attendance)):
            if attendance[i]["employee_id"] == id and attendance[i]["date"] == date.today():
                raise HTTPException(status_code=409, detail="Already Checked In")

        check_in_data = AttendanceRecord(
            employee_id=id,
            date=date.today(),
            check_in=datetime.now().time()
        )
        attendance.append(check_in_data.__dict__)
        return check_in_data


@app.post("/employees/{id}/checkout", response_model=AttendanceRecord)
def checkout(id: int):
    """
    Employee check-out.
    - Ensures check-in exists before checkout.
    """
    global current
    if get_employee_by_id(id):
        for i in range(len(attendance)):
            if attendance[i]["employee_id"] == id and (attendance[i]["check_in"] is None):
                raise HTTPException(status_code=409, detail="No Data to Checkout")
            if attendance[i]["employee_id"] == id and attendance[i]["check_out"] is None:
                current = attendance[i]
                check_out_data = AttendanceRecord(
                    employee_id=id,
                    date=current["date"],
                    check_in=current["check_in"],
                    check_out=datetime.now().time()
                )
                break

        attendance.append(check_out_data.__dict__)
    return check_out_data

# ================================
# Leave Endpoints
# ================================

@app.post("/employees/{id}/leave-requests", response_model=LeaveRequest)
def leave_request(id: int, leave: CreateLeave):
    """
    Create a leave request.
    - Validates date range.
    - Assigns auto-incremented leave ID.
    """
    if get_employee_by_id(id):
        if leave.from_date < leave.to_date:
            global next_leave_id
            new_leave = LeaveRequest(
                leave_id=next_leave_id,
                employee_id=id,
                from_date=leave.from_date,
                to_date=leave.to_date,
                reason=leave.reason,
            )
            next_leave_id += 1
            leave_list.append(new_leave.__dict__)
            return new_leave
        else:
            raise HTTPException(status_code=400, detail="From date cannot be greater than To date")
    else:
        raise HTTPException(status_code=404, detail="Employee Data not found")


@app.get("/employees/{id}/leave-requests", response_model=List[LeaveRequest])
def get_leave_requests(id: int):
    """Fetch all leave requests for an employee."""
    lis = []
    if get_employee_by_id(id):
        for data in leave_list:
            if data["employee_id"] == id:
                lis.append(data)
        return lis
    
# ===============================
#  SAMPLE INPUT AND OUTPUT
# ===============================

# 1) Add Employee
# ---------------
# Request (POST /employees):
# {
#   "name": "Ravi Kumar",
#   "email": "ravi.kumar@ust.com",
#   "department": "Finance",
#   "role": "Analyst"
# }

# Response:
# {
#   "id": 4,
#   "name": "Ravi Kumar",
#   "email": "ravi.kumar@ust.com",
#   "department": "Finance",
#   "role": "Analyst",
#   "status": "active"
# }


# 2) Get All Employees
# --------------------
# Request (GET /employees)

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
#     "name": "Ravi Kumar",
#     "email": "ravi.kumar@ust.com",
#     "department": "Finance",
#     "role": "Analyst",
#     "status": "active"
#   }
# ]


# 3) Get Employee by ID
# ---------------------
# Request (GET /employees/2)

# Response:
# {
#   "id": 2,
#   "name": "Vikram S",
#   "email": "vikram.s@ust.com",
#   "department": "Delivery",
#   "role": "Manager",
#   "status": "active"
# }


# 4) Update Employee
# ------------------
# Request (PUT /employees/2):
# {
#   "name": "Vikram Sharma",
#   "email": "vikram.sharma@ust.com",
#   "department": "Delivery",
#   "role": "Senior Manager",
#   "status": "active"
# }

# Response:
# {
#   "id": 2,
#   "name": "Vikram Sharma",
#   "email": "vikram.sharma@ust.com",
#   "department": "Delivery",
#   "role": "Senior Manager",
#   "status": "active"
# }


# 5) Delete Employee
# ------------------
# Request (DELETE /employees/3)

# Response:
# {
#   "id": 3,
#   "name": "Meera N",
#   "email": "meera.n@ust.com",
#   "department": "HR",
#   "role": "HR",
#   "status": "active"
# }


# 6) Employee Check-in
# --------------------
# Request (POST /employees/1/checkin)

# Response:
# {
#   "employee_id": 1,
#   "date": "2025-11-24",
#   "check_in": "09:45:12",
#   "check_out": null
# }


# 7) Employee Checkout
# --------------------
# Request (POST /employees/1/checkout)

# Response:
# {
#   "employee_id": 1,
#   "date": "2025-11-24",
#   "check_in": "09:45:12",
#   "check_out": "17:30:45"
# }


# 8) Create Leave Request
# -----------------------
# Request (POST /employees/2/leave-requests):
# {
#   "from_date": "2025-12-01",
#   "to_date": "2025-12-05",
#   "reason": "Family function"
# }

# Response:
# {
#   "leave_id": 1,
#   "employee_id": 2,
#   "from_date": "2025-12-01",
#   "to_date": "2025-12-05",
#   "reason": "Family function",
#   "status": "pending"
# }


# 9) Get Leave Requests
# ---------------------
# Request (GET /employees/2/leave-requests)

# Response:
# [
#   {
#     "leave_id": 1,
#     "employee_id": 2,
#     "from_date": "2025-12-01",
#     "to_date": "2025-12-05",
#     "reason": "Family function",
#     "status": "pending"
#   }
# ]