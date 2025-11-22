from fastapi import FastAPI,HTTPException
from typing import List
import datetime
from pydantic import BaseModel

app=FastAPI(title="UST Employee API")

# global next_e_id
# next_e_id=3
# global next_l_id
# next_l_id=0
class Employee(BaseModel):
    id:int
    name:str
    email:str
    department:str
    role:str
    status:str="active"
    
class AttendenceRecord(BaseModel):
    employee_id:int
    date:datetime.date
    check_in:datetime.time=None
    check_out:datetime.time=None

class LeaveRequest(BaseModel):
    leave_id:int=0
    employee_id:int=0
    from_date:datetime.date
    to_date:datetime.date
    reason:str
    status:str="pending"

#initializing the lists
leaves:List[LeaveRequest]=[]
attendence:List[AttendenceRecord]=[]
employees:List[Employee]=[
 Employee(id= 1, name= "Asha Rao", email= "asha.rao@ust.com", department="Engineering", role= "Engineer", status="active" ),
 Employee( id= 2,name= "Vikram S", email= "vikram.s@ust.com", department="Delivery", role= "Manager", status= "active" ),
 Employee( id= 3, name= "Meera N", email="meera.n@ust.com", department="HR", role="HR",status="active" )
]

next_e_id=3
next_l_id=0
@app.post("/employees",response_model=Employee)
def create_emp(emp:Employee):
    for row in employees:
        if row.email==emp.email:
            raise HTTPException(status_code=409,detail=" Conflict email already exist")
    global next_e_id
    next_e_id+=1
    emp.id=next_e_id
    employees.append(emp)
    return emp

#displaying all the employees details
@app.get("/employees",response_model=List[Employee])
def display_all(dep:str=""):
    if dep=="":
        return employees       
    new_li=[]
    for row in employees:
        if row.department==dep:
            new_li.append(row)
    return new_li

#searching employee details by id
@app.get("/employees/{id}",response_model=Employee)
def search_by_id(id:int):
    try:
        return employees[id-1]
    except IndexError:
        raise HTTPException(status_code=404,detail="Employee not found")
    
#update the emplyee details
@app.post("/employees/{id}",response_model=Employee)
def update_emp(id:int,emp:Employee):
    try:
        for row in employees:
            if emp.email==row.email and row.id!=id:
                raise HTTPException(status_code=409,detail="Email already Exists")
        emp.id=id
        employees[id-1]=emp
        return emp
    except IndexError:
        raise HTTPException(status_code=404,detail="Employee not found")
    
#Delete employee record
@app.delete("/employees/{id}")
def delete_byid(id:int):
    try:
        # removed=employees[id-1]
        employees.pop(id-1)
        return {"detail": "Employee deleted"}
    except IndexError:
        raise HTTPException(status_code=404,detail="Employee not found")

#checkin for the employee
@app.post("/employees/{id}/checkin")
def check_in(id: int, attend: AttendenceRecord):
    # Verify employee exists
    if not any(emp.id == id for emp in employees):
        raise HTTPException(status_code=404, detail="Employee not found")

    # Prevent duplicate check-in for same date
    for att in attendence:
        if att.employee_id == id and att.date == attend.date and att.check_in is not None:
            raise HTTPException(status_code=409, detail="Already checked in")

    # Save record
    attend.employee_id = id
    attendence.append(attend)
    return {"detail": "Check-in successful", "record": attend}

#checkout for the employee
@app.post("/employees/{id}/checkout")
def checkout(id: int, attend: AttendenceRecord):
    # Verify employee exists
    if not any(emp.id == id for emp in employees):
        raise HTTPException(status_code=404, detail="Employee not found")

    # Find matching attendance record
    for att in attendence:
        if att.employee_id == id and att.date == attend.date:
            if att.check_in is None:
                raise HTTPException(status_code=400, detail="Check-in required before checkout")
            if att.check_out is not None:
                raise HTTPException(status_code=409, detail="Already checked out")

            # Perform checkout
            att.check_out = attend.check_out
            return {"detail": "Checkout successful", "record": att}

    # No matching check-in found
    raise HTTPException(status_code=404, detail="No check-in record found for this date")

#for posting the leave
@app.post("/employees/{id}/leave-requests",response_model=LeaveRequest)
def create_leave(id:int,leave:LeaveRequest):
    global next_l_id
    next_l_id+=1
    leave.leave_id=next_l_id
    leave.employee_id=id
    if leave.from_date>leave.to_date:
        raise HTTPException(status_code=400,detail="to date cannot be less that from date")
    leaves.append(leave)
    return leave
    
#for getting the leaves requests for employee id
@app.get("/employees/{id}/leave-requests",response_model=List[LeaveRequest])
def display_all(id:int):
    new_li=[]
    flag=True
    for emp in employees:
        if emp.id==id:
            flag=False
    if not flag:
        for leave in leaves:        
            if leave.employee_id==id:
                new_li.append(leave)
    else:
        raise HTTPException(status_code=404,detail="Employee not found")
    return new_li
    

    



