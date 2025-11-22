from typing import List
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from datetime import datetime
from datetime import datetime,date

app = FastAPI(title="madhan CRUD (In-Memory)")


class Employee(BaseModel):
    id: int
    name: str
    email: str
    dep: str
    role: str
    status: str = "active"

class AttendanceRecord(BaseModel):
    emp_id: int
    date: date
    check_in: str | None=None
    check_out: str | None=None
    
class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: date | None=None
    to_date: date | None=None
    reason: str
    status: str= "pending"

Employee = [
 { "id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department":
"Engineering", "role": "Engineer", "status": "active" },
 { "id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department":
"Delivery", "role": "Manager", "status": "active" },
 { "id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department":
"HR", "role": "HR", "status": "active" }
]

employee : List[Employee] = []
attendance : List[AttendanceRecord] = []
Leaves : List[LeaveRequest] = []

next_emp_id = 4
next_leave_id = 1


@app.post("/employee")
def create_student(emp:Employee):
    employee.append(emp)
    return {"Student created":emp}




    
