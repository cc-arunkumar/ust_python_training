from fastapi import FastAPI,HTTPException
from datetime import datetime, date
from typing import List, Optional

# Add the necessary imports
from pydantic import BaseModel
app = FastAPI(title="UST Employee API") 
# In-memory data storage
employees: List[Employee] = [
    {"id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active"},
    {"id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active"},
    {"id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department": "HR", "role": "HR", "status": "active"}
]

attendance: List[AttendanceRecord] = []
leaves: List[LeaveRequest] = []

# The headers list as defined in your starting code
headers = list(employees[0].keys())

next_emp_id = 4
next_l_id = 1  # For leave request IDs

# Helper functions
def get_employee_by_id(id: int):
    for emp in employees:
        if emp[headers[0]] == id:  # Accessing employee id using headers
            return emp
    return None

# Models
class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "active"

class AttendanceRecord(BaseModel):
    employee_id: int
    date: datetime.date
    check_in: datetime.time  # Accepting check_in as a string in ISO 8601 format
    check_out: datetime.time # Accepting check_out as a string in ISO 8601 format

class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: datetime.date
    to_date: datetime.date
    reason: str
    status: str = "pending"

class CreateLeave(BaseModel):
    from_date: datetime.date
    to_date: datetime.date
    reason: str

# New Endpoints

# 1. Delete Employee
@app.delete("/employees/{id}", response_model=Employee)
def delete_employee(id: int):
    global employees
    for i in range(len(employees)):
        if employees[i][headers[0]] == id:  # Accessing employee id using headers
            return employees.pop(i)
    raise HTTPException(status_code=404, detail="Employee not found")
@app.post("/employees/{id}/checkin", response_model=AttendanceRecord)
def check_in(id: int):
    if get_employee_by_id(id):  # Check if employee exists
        for att in attendance:
            if att.employee_id == id and att.date == date.today():
                raise HTTPException(status_code=409, detail="Already Checked In")

        check_in_data = AttendanceRecord(
            employee_id=id,
            date=date.today(),
            check_in=datetime.now().isoformat()
        )
        attendance.append(check_in_data)  # Directly append the model instance
        return check_in_data
    else:
        raise HTTPException(status_code=404, detail="Employee not found")

# 3. Check-out Employee
@app.post("/employees/{id}/checkout", response_model=AttendanceRecord)
def check_out(id: int):
    if get_employee_by_id(id):  # Check if employee exists
        for att in attendance:
            if att.employee_id == id and att.date == date.today():
                if att.check_in is None:
                    raise HTTPException(status_code=409, detail="No Data to Checkout")
                if att.check_out is not None:
                    raise HTTPException(status_code=409, detail="Already Checked Out")

                # Perform checkout
                check_out_data = AttendanceRecord(
                    employee_id=id,
                    date=att.date,
                    check_in=att.check_in,
                    check_out=datetime.now().isoformat()
                )
                attendance.append(check_out_data)  # Directly append the model instance
                return check_out_data

        raise HTTPException(status_code=404, detail="No check-in found for today")
    else:
        raise HTTPException(status_code=404, detail="Employee not found")

# 4. Create Leave Request
@app.post("/employees/{id}/leave-requests", response_model=LeaveRequest)
def leave_request(id: int, leave: CreateLeave):
    if get_employee_by_id(id):  # Check if employee exists
        if leave.from_date > leave.to_date:
            raise HTTPException(status_code=400, detail="From date cannot be later than to date")

        global next_l_id
        new_leave = LeaveRequest(
            leave_id=next_l_id,
            employee_id=id,
            from_date=leave.from_date,
            to_date=leave.to_date,
            reason=leave.reason
        )
        next_l_id += 1
        leaves.append(new_leave)  # Directly append the model instance
        return new_leave
    else:
        raise HTTPException(status_code=404, detail="Employee not found")

# 5. Get Leave Requests
@app.get("/employees/{id}/leave-requests", response_model=List[LeaveRequest])
def get_leave_requests(id: int):
    if get_employee_by_id(id):  # Check if employee exists
        return [leave for leave in leaves if leave.employee_id == id]
    else:
        raise HTTPException(status_code=404, detail="Employee not found")