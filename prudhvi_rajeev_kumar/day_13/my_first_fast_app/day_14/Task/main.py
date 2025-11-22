from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


app = FastAPI(title=" UST Employee API")

class Employee(BaseModel):
    id:int
    name:str
    email:str
    department:str
    role:str
    status:str="active"

class AttendanceRecord(BaseModel):
    employee_id: int
    date: str
    check_in: Optional[str] = None
    check_out: Optional[str] = None
    
class Checkinrequest(BaseModel):
    date : str
    time : str
    
class Checkoutrequest(BaseModel):
    date : str
    time : str

class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: str
    to_date: str
    reason: str
    status: str = "pending"

class leaverequest(BaseModel):
    from_date : str
    to_date : str
    reason : str
    
employees: List[Employee] =  [
 { "id": 1, "name": "Asha Rao",   "email": "asha.rao@ust.com",  "department": 
"Engineering", "role": "Engineer", "status": "active" },
 { "id": 2, "name": "Vikram S",  "email": "vikram.s@ust.com",  "department": 
"Delivery",    "role": "Manager",  "status": "active" },
 { "id": 3, "name": "Meera N",   "email": "meera.n@ust.com",   "department": 
"HR",          "role": "HR",       "status": "active" }
 ]
attendance: List[AttendanceRecord] = []
leaves: List[LeaveRequest] = []

next_emp_id = 4
next_leave_id = 1

@app.post("/employees")
def create_employee(emp:Employee):
    global next_emp_id
    for e in employees:
        if e["email"]==emp["email"]:
            raise HTTPException(status_code=409,detail="Email already exists")
        
    new_emp={
        "id": next_emp_id,
        "name":emp["name"],
        "email":emp["email"],
        "department":emp["department"],
        "role":emp["role"]
    }
    
    employees.append(new_emp)
    next_emp_id+=1
    return{"Employee created":new_emp}

@app.get("/employee")
def list_employees(department: Optional[str] = None):
    if department:
        result=[]
        for e in employees:
            if e["department"]==department:
                result.append(e)
        return result
    return employees

@app.get("/employee/{id}")
def getById(id:int):
    for e in employees:
        if e["id"]==id:
            return e
    raise HTTPException(status_code=404,detail="Employee not found")

@app.put("/employee/{id}")
def update(id:int,emp:Employee):
    for e in employees:
        if e["id"]==id:
            for other in employees:
                if other["email"]==emp["email"]:
                    raise HTTPException(status_code=409,detail="Email already exist")
            e["name"] = emp["name"]
            e["email"] = emp["email"]
            e["department"] = emp["department"]
            e["role"] = emp["role"]
            e["status"] = emp["status"]
            
            return e
    raise HTTPException(status_code=404,detail="Employee not found")


@app.delete("/employee/{id}")
def delete(id:int):
    for e in employees:
        if e["id"]==id:
            employees.remove(e)
            return {"detail":"Employee deleted"}
    raise HTTPException(status_code=404,detail="Employee not found")

@app.post("/employee/{id}/checkin")
def check_in(id:int,data:Checkinrequest):
    for e in employees:
        if e["id"]==id:
            for r in attendance:
                if r["employee_id"]==id and r["date"]==data.date:
                    if r["check_in"]:
                        raise HTTPException(status_code=409,detail="Already checkin")
                    r["check_in"]=data.time
                    return r
    
        newrecord={
            "employee_id":id,
            "date":data.date,
            "check_in": data.time,
            "check_out":None
        }    
        attendance.append(newrecord)
        return newrecord
    raise HTTPException(status_code=404,detail="Employee not found")

@app.post("/employee/{id}/checkout")
def check_out(id:int,data:Checkoutrequest):
    for e in employees:
        if e["id"]==id:
            for r in attendance:
                if r["employee_id"]==id and r["date"]==data.date:
                    if not r["check_in"]:
                        raise HTTPException(status_code=404,detail="First checkin")
                    if r["check_out"]:
                        raise HTTPException(status_code=409,detail="already checkout")
                    r["check_out"]=data.time
                    return r
        raise HTTPException(status_code=404, detail="No checkin record found for this file.")
    raise HTTPException(status_code=404,detail="Employee not found")
            
@app.post("/employees/{id}/leave-requests")
def create_leave(id: int, data: leaverequest):
    global next_leave_id
    for e in employees:
        if e["id"] == id:
            if data.from_date > data.to_date:
                raise HTTPException(status_code=400, detail="from_date must be on or before to_date")

            leave = {
                "leave_id": next_leave_id,
                "employee_id": id,
                "from_date": data.from_date,
                "to_date": data.to_date,
                "reason": data.reason,
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
