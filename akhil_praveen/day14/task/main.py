from typing import List
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from datetime import date

app = FastAPI(title="UST Employee API ")

class Employees(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "Active"

class EmpModel(BaseModel):
    name: str
    email: str
    department: str
    role: str

class UpdateModel(BaseModel):
    name: str
    email: str
    department: str
    role: str
    status :str

class AttendanceRecord(BaseModel):
    employee_id: int
    date: str
    check_in: str = None
    check_out: str = None
    
class CheckIn(BaseModel):
    date: str
    check_in: str = None
    
class CheckOut(BaseModel):
    check_out: str = None
    
class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: str
    to_date: str
    reason: str
    status: str
    
emp_list =  [{ "id": 1, "name": "Asha Rao",   "email": "asha.rao@ust.com",  "department": "Engineering", "role": "Engineer", "status": "active" },{ "id": 2, "name": "Vikram S",  "email": "vikram.s@ust.com",  "department": "Delivery",    "role": "Manager",  "status": "active" },
 { "id": 3, "name": "Meera N",   "email": "meera.n@ust.com",   "department": "HR",          "role": "HR",       "status": "active" }
 ]

attendance= [] 
leaves= []
email_list = ["asha.rao@ust.com","meera.n@ust.com","vikram.s@ust.com"]
attendance_id_list = []
next_emp = 4
next_leave_id = 1

@app.post("/employee",response_model=Employees)
def create_emp( employee:EmpModel):
    if employee.email in email_list:
        raise HTTPException(status_code=409,detail="Email already exists!")
    email_list.append(employee.email)
    global next_emp
    new_emp = Employees(id=next_emp,name = employee.name,email=employee.email,department=employee.department,role=employee.role)
    emp_list.append(new_emp.__dict__)
    next_emp+=1
    return new_emp

@app.get("/employee",response_model=List[Employees])
def get_all_details():
    return emp_list

@app.get("/employee/{id}",response_model=Employees)
def get_details_byid(id:str):
    
    for emp in emp_list:
        if emp[id]==id:
            return emp
    raise HTTPException(status_code=404,detail="Id not found")

@app.put("/employee/{id}",response_model=Employees)
def update(id:int,update_emp:UpdateModel):
    
    if  update_emp.email in email_list:
            raise HTTPException(status_code=409,detail="Email already exists!")
    
    for i in range(len(emp_list)):
        if emp_list[i]["id"]==id:
            email_list.append(update_emp.email)
            email_list.remove(emp_list[i]["email"])
            new_emp = Employees(id=id,name = update_emp.name,email=update_emp.email,department=update_emp.department,role=update_emp.role)
            emp_list[i]=new_emp.__dict__
            return new_emp
    raise HTTPException(status_code=404,detail="Employee not found")

@app.delete("/employee/{id}",response_model=Employees)
def delete_student(id:int):
    for i in range(len(emp_list)):
        if emp_list[i]["id"]==id:
            removed = emp_list.pop(i)
            return removed
    raise HTTPException(status_code=404,detail="Employee not found")

@app.post("/employee/{id}/checkin")
def check_in(id:int,attend:CheckIn):
    for i in range(len(emp_list)):
        if emp_list[i]["id"]==id:
            if id in attendance_id_list:
                raise HTTPException(status_code=409,detail="already exists")
            new_attend = AttendanceRecord(
                employee_id=id,
                date=attend.date,
                check_in=attend.check_in
            )
            attendance.append(new_attend)
            attendance_id_list.append(id)
            return new_attend
    raise HTTPException(status_code=404,detail="Employee not found")

@app.post("/employee/{id}/checkout")
def check_out(id:int,attend:CheckOut):
    for i in range(len(emp_list)):
        if emp_list[i]["id"]==id:
            if id not in attendance_id_list:
                raise HTTPException(status_code=400,detail="Check-in required before checkout")
            temp_attend = None
            for j in attendance:
                if j.employee_id==id and j.check_out:
                    raise HTTPException(status_code=409,detail="already exists")
            for j in attendance:
                if j.employee_id == id:
                    temp_attend = j
            new_attend = AttendanceRecord(
                employee_id=id,
                date=temp_attend.date,
                check_in=temp_attend.check_in,
                check_out=attend.check_out
            )
            attendance.append(new_attend)
            return new_attend
    raise HTTPException(status_code=404,detail="Employee not found")

