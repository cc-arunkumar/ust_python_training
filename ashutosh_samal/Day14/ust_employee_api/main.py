from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date,time

app = FastAPI(title="UST Employee")

class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "Active"

class AttendanceRecord(BaseModel):
    employee_id: int
    date: date
    check_in: str | None = None
    check_out: str | None = None

class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: date
    to_date: date
    reason: str
    status: str = "pending"
    
employees: List[Employee] = [
 { "id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department":
"Engineering", "role": "Engineer", "status": "active" },
 { "id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department":
"Delivery", "role": "Manager", "status": "active" },
 { "id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department":
"HR", "role": "HR", "status": "active" }
]
attendance: List[AttendanceRecord] = []
leaves: List[LeaveRequest] = []

next_emp_id = 4

@app.post("/Employee")
def create_Employee(emp:Employee):
    global next_emp_id
    # Check if email already exists
    for i in employees:
        if i["email"] == emp.email:
            raise HTTPException(status_code=409, detail="Email already exists")
    emp.id = next_emp_id
    next_emp_id += 1
    employees.append(emp.model_dump())
    return {"Employee Created":emp}


@app.get("/Employee",response_model=List[Employee])
def get_employee(department: str | None = None):
    if department:
        return [emp for emp in employees if emp['department'] == department]
    return employees


@app.get("/Employee/{id}",response_model=Employee)
def get_employee(id:int):
    try:
        for emp in employees:
            if emp['id']==id:
                return emp
    except IndexError:
        raise HTTPException(status_code=404,detail="Employee not found")


@app.put("/employee/{id}")
def update(id: int, emp: Employee):
    for e in employees:
        if e["id"] == id:
            for other in employees:
                if other["email"] == emp.email:
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
    
       
@app.delete("/Employee/{id}")
def delete_employee(id:int):
    for emp in employees:
        if emp['id']==id:
            employees.remove(emp)
        return {"detail": "Employee deleted"}
    raise HTTPException(status_code=404,detail="Student not found")


@app.post("/Employee/{id}/checkin")
def emp_checkin(id:int,attendance_data: AttendanceRecord):
    for emp in employees:
        if emp['id'] == id:
            for record in attendance:
                if record["employee_id"] == id and record['date'] == attendance_data:
                    raise HTTPException(status_code=409, detail="Already checked in")
            attendance.append(attendance_data.model_dump())
            return attendance_data
    raise HTTPException(status_code=404, detail="Employee not found")

@app.post("/employee/{id}/checkout")
def check_in(id:int,data:dict):
    for e in employees:
        if e["id"]==id:
            for r in attendance:
                if r["employee_id"]==id and r["date"]==data["date"]:
                    if not r["check_in"]:
                        raise HTTPException(status_code=404,detail="First checkin")
                    if r["check_out"]:
                        raise HTTPException(status_code=409,detail="already checkout")
                    r["check_out"]=data["time"]
                    return r

    raise HTTPException(status_code=404,detail="Employee not found")
            
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
    for e in employees:
        if e["id"] == id:
            result = []
            for l in leaves:
                if l["employee_id"] == id:
                    result.append(l)
            return result
    raise HTTPException(status_code=404, detail="Employee not found")