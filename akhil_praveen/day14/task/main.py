from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date, datetime, time

# FastAPI app initialization
app = FastAPI(title="UST Employee API ")

# Employee model
class Employees(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "Active"

# Employee model for creating new employees
class EmpModel(BaseModel):
    name: str
    email: str
    department: str
    role: str

# Update employee model
class UpdateModel(BaseModel):
    name: str
    email: str
    department: str
    role: str
    status: str

# Attendance record model
class AttendanceRecord(BaseModel):
    employee_id: int
    date: date
    check_in: time = None
    check_out: time = None

# Check-in model
class CheckIn(BaseModel):
    date: date
    check_in: time

# Check-out model
class CheckOut(BaseModel):
    check_out: time = None

# Leave request model
class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: date
    to_date: date
    reason: str
    status: str = "Pending"

# Create leave model
class CreateLeave(BaseModel):
    from_date: date
    to_date: date
    reason: str

# Dummy data
emp_list = [
    { "id": 1, "name": "Asha Rao",   "email": "asha.rao@ust.com",  "department": "Engineering", "role": "Engineer", "status": "active" },
    { "id": 2, "name": "Vikram S",  "email": "vikram.s@ust.com",  "department": "Delivery",    "role": "Manager",  "status": "active" },
    { "id": 3, "name": "Meera N",   "email": "meera.n@ust.com",   "department": "HR",          "role": "HR",       "status": "active" }
]

attendance = [] 
leaves = []
email_list = ["asha.rao@ust.com", "meera.n@ust.com", "vikram.s@ust.com"]
attendance_id_list = []
next_emp = 4
next_leave_id = 1

# Create new employee
@app.post("/employee", response_model=Employees)
def create_emp(employee: EmpModel):
    if employee.email in email_list:
        raise HTTPException(status_code=409, detail="Email already exists!")
    email_list.append(employee.email)
    global next_emp
    new_emp = Employees(id=next_emp, name=employee.name, email=employee.email, department=employee.department, role=employee.role)
    emp_list.append(new_emp.__dict__)
    next_emp += 1
    return new_emp

# Get all employees
@app.get("/employee", response_model=List[Employees])
def get_all_details():
    return emp_list

# Get employee by ID
@app.get("/employee/{id}", response_model=Employees)
def get_details_byid(id: str):
    for emp in emp_list:
        if emp["id"] == id:
            return emp
    raise HTTPException(status_code=404, detail="Id not found")

# Update employee details
@app.put("/employee/{id}", response_model=Employees)
def update(id: int, update_emp: UpdateModel):
    if update_emp.email in email_list:
        raise HTTPException(status_code=409, detail="Email already exists!")
    for i in range(len(emp_list)):
        if emp_list[i]["id"] == id:
            email_list.append(update_emp.email)
            email_list.remove(emp_list[i]["email"])
            new_emp = Employees(id=id, name=update_emp.name, email=update_emp.email, department=update_emp.department, role=update_emp.role)
            emp_list[i] = new_emp.__dict__
            return new_emp
    raise HTTPException(status_code=404, detail="Employee not found")

# Delete employee
@app.delete("/employee/{id}", response_model=Employees)
def delete_student(id: int):
    for i in range(len(emp_list)):
        if emp_list[i]["id"] == id:
            removed = emp_list.pop(i)
            return removed
    raise HTTPException(status_code=404, detail="Employee not found")

# Check-in employee
@app.post("/employee/{id}/checkin")
def check_in(id: int):
    for i in range(len(emp_list)):
        if emp_list[i]["id"] == id:
            if id in attendance_id_list:
                raise HTTPException(status_code=409, detail="Already checked in")
            new_attend = AttendanceRecord(
                employee_id=id,
                date=date.today(),
                check_in=datetime.now().time()
            )
            attendance.append(new_attend)
            attendance_id_list.append(id)
            return new_attend
    raise HTTPException(status_code=404, detail="Employee not found")

# Check-out employee
@app.post("/employee/{id}/checkout")
def check_out(id: int):
    for i in range(len(emp_list)):
        if emp_list[i]["id"] == id:
            if id not in attendance_id_list:
                raise HTTPException(status_code=400, detail="Check-in required before checkout")
            temp_attend = None
            for j in attendance:
                if j.employee_id == id and j.check_out:
                    raise HTTPException(status_code=409, detail="Already checked out")
            for j in attendance:
                if j.employee_id == id:
                    temp_attend = j
            new_attend = AttendanceRecord(
                employee_id=id,
                date=temp_attend.date,
                check_in=temp_attend.check_in,
                check_out=datetime.now().time()
            )
            attendance.append(new_attend)
            return new_attend
    raise HTTPException(status_code=404, detail="Employee not found")

# Request leave for an employee
@app.post("/employee/{id}/leave-request")
def leave_req(id: int, leave: CreateLeave):
    global next_leave_id
    if get_details_byid(id):
        if leave.from_date > leave.to_date:
            raise HTTPException(status_code=400, detail="from_date must be on or before to_date")
        new_leave = LeaveRequest(
            leave_id=next_leave_id,
            employee_id=id,
            from_date=leave.from_date,
            to_date=leave.to_date,
            reason=leave.reason
        )
        leaves.append(new_leave)
        next_leave_id += 1
        return new_leave

# Get leave requests of an employee
@app.get("/employee/{id}/leave-request")
def leave_req(id: int): 
    temp_req = []
    if get_details_byid(id):
        for i in leaves:
            if id == i.employee_id:
                temp_req.append(i)
        return temp_req

# Sample Output

"""
Sample Output for /employee (POST):
Input:
{
    "name": "John Smith",
    "email": "john.smith@ust.com",
    "department": "Engineering",
    "role": "Engineer"
}
Output:
{
    "id": 4,
    "name": "John Smith",
    "email": "john.smith@ust.com",
    "department": "Engineering",
    "role": "Engineer",
    "status": "Active"
}

Sample Output for /employee (GET):
Output:
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
        "email": "meera.n@ust.com",
        "department": "HR",
        "role": "HR",
        "status": "active"
    },
    {
        "id": 4,
        "name": "John Smith",
        "email": "john.smith@ust.com",
        "department": "Engineering",
        "role": "Engineer",
        "status": "Active"
    }
]

Sample Output for /employee/{id} (GET):
Input: /employee/1
Output:
{
    "id": 1,
    "name": "Asha Rao",
    "email": "asha.rao@ust.com",
    "department": "Engineering",
    "role": "Engineer",
    "status": "active"
}

Sample Output for /employee/{id} (PUT):
Input:
{
    "name": "Asha Rao",
    "email": "asha.rao@ust.com",
    "department": "Engineering",
    "role": "Senior Engineer",
    "status": "active"
}
Output:
{
    "id": 1,
    "name": "Asha Rao",
    "email": "asha.rao@ust.com",
    "department": "Engineering",
    "role": "Senior Engineer",
    "status": "active"
}

Sample Output for /employee/{id} (DELETE):
Input: /employee/1
Output:
{
    "id": 1,
    "name": "Asha Rao",
    "email": "asha.rao@ust.com",
    "department": "Engineering",
    "role": "Engineer",
    "status": "active"
}

Sample Output for /employee/{id}/checkin (POST):
Input: /employee/1/checkin
Output:
{
    "employee_id": 1,
    "date": "2025-11-24",
    "check_in": "14:30:00"
}

Sample Output for /employee/{id}/checkout (POST):
Input: /employee/1/checkout
Output:
{
    "employee_id": 1,
    "date": "2025-11-24",
    "check_in": "14:30:00",
    "check_out": "18:00:00"
}

Sample Output for /employee/{id}/leave-request (POST):
Input:
{
    "from_date": "2025-12-01",
    "to_date": "2025-12-05",
    "reason": "Vacation"
}
Output:
{
    "leave_id": 1,
    "employee_id": 1,
    "from_date": "2025-12-01",
    "to_date": "2025-12-05",
    "reason": "Vacation",
    "status": "Pending"
}
"""
