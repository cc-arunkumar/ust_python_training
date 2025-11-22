from fastapi import FastAPI,HTTPException
from typing import List
from pydantic import BaseModel
import datetime 
app=FastAPI(title="UST Employee Managment system")
employees:List[Employee]=[
    {"id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active"},
    {"id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active"},
    {"id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department": "HR", "role": "HR", "status": "active"}
]
attendence:List[AttandanceRecord]=[]
leaves:List[LeaveRequest]=[]
global next_emp_id
next_emp_id=4
global next_leave_id
next_leave_id=1
class Employee(BaseModel):
    id:int
    name:str
    email:str
    department:str
    role:str
    status:str="active"
class AttandanceRecord(BaseModel):
    date:datetime.date
    cheak_in:datetime.time=None
    cheak_out:datetime.time=None
class LeaveRequest(BaseModel):
    leave_id:int=0
    employee_id:int=0
    from_date:datetime.date
    to_date:datetime.date
    reason:str
    status:str="pending"
    
next_emp_id=3
next_leave_id=0

@app.post("/employees",response_model=Employee)
def create_employee(employee:Employee):
    for emp in employees:
        if employee.email==emp.email:
            raise HTTPException(status_code=409,detail="email already exists")

        global next_emp_id
        employee.id=next_emp_id
        next_emp_id+=1
        employees.append(employee)
        return {'Employee created:':employee}
            

@app.get("/employees",response_model=List[Employee])
def get_all_employee(department:str=""):
    if department=="":
        return employees
    new_leave=[]
    for emp in employees:
        if emp.department==department:
            new_leave.append(emp)
    return new_leave

@app.get("/employees/{id}",response_model=Employee)
def search_by_id(ind:int):
    try:
        return employees[id-1]
    except IndexError:
        raise HTTPException(status_code=404,detail="employee not found by that id")

@app.post("/employees/{id}",response_model=Employee)
def update_employee(id:int,employee:Employee):
    try:
        for emp in employee:
            if employee.email==emp.email and emp.id !=id:
                raise HTTPException(status_code=409,detail="Email already exists")
        employee.id=id
        employees[id-1]=employee
        return employee
    except IndexError:
        raise HTTPException(status_code=404,detail="Employee not found")

@app.delete("/employees/{id}")
def delete_by_id(id:int):
    try:
        employees.pop(id-1)
        return{"msg":"employee deleted"}
    except IndexError:
        raise HTTPException(status_code=404,detail="employee not found")

@app.post("/employee/{id}/cheakin")
def cheak_in(id:int,attend:AttandanceRecord):
    if not any(employee.id==id for employee in employees):
        raise HTTPException(status_code=404,detail="Employee already cheaked in")
    
    for att in attendence:
        attendence.append(attend)
        return {"msg:":"cheak in success", "rocord:":attend}

@app.put("/employee/{id}/cheakout")
def cheakout(id:int,attend:AttandanceRecord):
    if not any(employee.id==id for employee in employees):
        raise HTTPException(status_code=404,detail="Employee not found")
    
    for att in attendence:
        if att.employee_if ==id and att.date==attend.date:
            if att.cheak_in is None:
                raise HTTPException(status_code=400, detail="Check-in required before checkout")
            if att.check_out is not None:
                raise HTTPException(status_code=409, detail="Already checked out")
            
            att.check_out = attend.check_out
            return {"detail": "Checkout successful", "record": att}
    raise HTTPException(status_code=404, detail="No check-in record found for this date")

@app.post("/employees/{id}/leave-requests",response_model=LeaveRequest)
def create_leave(id:int,leave:LeaveRequest):
    global next_leave_id
    next_leave_id+=1
    leave.leave_id=next_leave_id
    leave.employee_id=id
    if leave.from_date>leave.to_date:
        raise HTTPException(status_code=400,detail="to date cannot be less that from date")
    leaves.append(leave)
    return leave

@app.get("/employees/{id}/leave-requests",response_model=List[LeaveRequest])
def display_all(id:int):
    new_leave=[]
    flag=True
    for emp in employees:
        if emp.id==id:
            flag=False
    if not flag:
        for leave in leaves:        
            if leave.employee_id==id:
                new_leave.append(leave)
    else:
        raise HTTPException(status_code=404,detail="Employee not found")
    return new_leave


        

                


    
    