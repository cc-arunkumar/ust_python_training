from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List,Optional
from datetime import date,time,timedelta

app = FastAPI(title="UST Employee API")

employees: List[Employee] =[
      { "id": 1, "name": "Asha Rao",   "email": "asha.rao@ust.com",  "department": 
"Engineering", "role": "Engineer", "status": "active" },
 { "id": 2, "name": "Vikram S",  "email": "vikram.s@ust.com",  "department": 
"Delivery",    "role": "Manager",  "status": "active" },
 { "id": 3, "name": "Meera N",   "email": "meera.n@ust.com",   "department": 
"HR",          "role": "HR",       "status": "active" }
]

next_emp_id = 4
next_leave_id=0
class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "active"

class Attendance(BaseModel):
    employee_id:int
    date:date
    check_in:Optional[time] = None
    check_out:Optional[time] = None
attendance:List[Attendance]=[]
class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: date
    to_date:Optional[date]=None
    reason: str
    status: str = "pending"
leaves:List[LeaveRequest]=[]
class CheckInRequest(BaseModel):
    date: date
    time: time
    
class CheckOutRequest(BaseModel):
    date: date
    time: time

class CheckLeaveRequest(BaseModel):
    from_date: date
    to_date: date
    reason: str

@app.post("/employees", response_model=Employee)
def create_employee(employee: Employee):
    global next_emp_id

    if any(e.email == employee.email for e in employees):
        raise HTTPException(status_code=409, detail="Email already exists")

    employee.id = next_emp_id
    employees.append(employee)
    next_emp_id += 1  

    return employee

@app.get("/employees", response_model=List[Employee])
def get_all_employees():
    return employees

@app.get("/employees/{id}", response_model=Employee)
def get_employee_by_id(id: int):
    
    employee = next((e for e in employees if e.id == id), None)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.put("/employees/{id}", response_model=Employee)
def update_employee(id: int, updated_employee: Employee):
    employee = next((e for e in employees if e.id == id), None)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    
    if updated_employee.email != employee.email:
        if any(e.email == updated_employee.email for e in employees):
            raise HTTPException(status_code=409, detail="Email already exists")
    
    for e in employees:
        if(e.id==id):
            employee.name = updated_employee.name
            employee.email = updated_employee.email
            employee.department = updated_employee.department
            employee.role = updated_employee.role
            employee.status = updated_employee.status

    return employee

@app.delete("/employees/{id}", response_model=Employee)
def delete_employee(id: int):
    employee = next((e for e in employees if e.id == id), None)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    employees.remove(employee)
    return employee


@app.post("/employees/{id}/checkin", response_model=Attendance, status_code=201)
def check_in(id: int, req: CheckInRequest):
    
    employee = next((e for e in employees if e["id"] == id), None)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    record = next((a for a in attendance if a["date"] == req.date and a["employee_id"] == id), None)

    if record:
        if record["check_in"] is not None:
            raise HTTPException(status_code=409, detail="Check In already done")
        else:
            record["check_in"] = req.time
            return Attendance(**record)
        
    n_record = {
        "employee_id": id,
        "date": req.date,
        "check_in": req.time,
        "check_out": None
    }
    attendance.append(n_record)
    return Attendance(**n_record)
    

@app.post("/employees/{id}/checkout", response_model=Attendance)
def check_out(id: int, req: CheckOutRequest):
    
    employee = next((e for e in employees if e["id"] == id), None)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    record = next((a for a in attendance if a["date"] == req.date and a["employee_id"] == id), None)
    
    if not record:
        raise HTTPException(status_code=400, detail="Check-in required before checkout")
    
    if record["check_in"] is None:
        raise HTTPException(status_code=400, detail="Check-in required before checkout")

    if record["check_out"] is not None:
            raise HTTPException(status_code=409, detail="Check In already done")
    
    record["check_out"] = req.time
    return Attendance(**record)

@app.post("/employees/{id}/leave-requests", response_model=LeaveRequest, status_code=201)

def create_leave_request(id: int, req: CheckLeaveRequest):
    global next_leave_id  
    employee = next((e for e in employees if e["id"] == id), None)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    to_date = req.to_date if req.to_date else req.from_date + timedelta(days=10)
    if req.from_date > to_date:
        raise HTTPException(status_code=400, detail="from_date must be on or before to_date")
    new_leave = {
        "leave_id": next_leave_id,
        "employee_id": id,
        "from_date": req.from_date,
        "to_date": req.to_date,
        "reason": req.reason,
        "status": "pending"
    }
    leaves.append(new_leave)
    next_leave_id += 1
    return LeaveRequest(**new_leave)
@app.get("/employees/{id}/leave-requests", response_model=List[LeaveRequest])
def list_leave_requests(id: int):
    employee = next((e for e in employees if e["id"] == id), None)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    emp_leaves = [LeaveRequest(**l) for l in leaves if l["employee_id"] == id]
    return emp_leaves

