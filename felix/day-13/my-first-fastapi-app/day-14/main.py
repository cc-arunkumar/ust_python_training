from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime,date,time

app = FastAPI(title="UST Employee API")


next_emp_id = 4
next_leave_id = 1

class Employee(BaseModel):
    id:int 
    name:str
    email:str
    department:str
    role:str
    status:str = "active"
    
class AttendanceRecord(BaseModel):
    employee_id:int
    date:date
    check_in:time = None
    check_out:time = None
    
class LeaveRequest(BaseModel):
    leave_id:int
    employee_id:int
    from_date:date = None
    to_date:date = None  
    reason:str
    status:str = "pending"
    
class EmailExistedError(Exception):
    pass

employee_list : List[Employee] = [
 { "id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department":
"Engineering", "role": "Engineer", "status": "active" },
 { "id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department":
"Delivery", "role": "Manager", "status": "active" },
 { "id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department":
"HR", "role": "HR", "status": "active" }
]

attendance: List[AttendanceRecord] = []

leaves: List[LeaveRequest] = []


@app.post("/employees")
def create_employee(employee:Employee):
    try:
        email =employee.email
        for i in employee_list:
            if email == i["email"]:
                raise EmailExistedError
        global next_emp_id
        employee.id = next_emp_id
        next_emp_id += 1
        employee_list.append(employee)
        return {"Employee Created: ":employee}
    except EmailExistedError:
        raise HTTPException(status_code=409,detail="Email already exist")
    

@app.get("/employees")
def list_employee(department:str = "not selected"):
    emp = []
    if department == "not selected":
        return employee_list
    else:
        for i in employee_list:
            if i["department"] == department:
                emp.append(i)
        return emp
    
@app.get("/employees/{id}")
def get_employee(id:int):
    for i in employee_list:
        if i["id"] == id:
            return i
    raise HTTPException(status_code=404,detail="Employee not found")

@app.put("/employees/{id}")
def update_employee(id:int,employee:Employee):
    try:
        email = employee.email
        for i in range(len(employee_list)):
            if email == employee_list[i]["email"]:
                raise EmailExistedError
    except EmailExistedError:
        raise HTTPException(status_code=409,detail="Email already exist")
    for i in range(len(employee_list)):
        if employee_list[i]["id"] == id:
            employee_list[i] = employee
            return {"Employee updated":employee}
    raise HTTPException(status_code=404,detail="Employee not found")

@app.delete("/employees/{id}")
def delete_employee(id:int):
    for i in range(len(employee_list)):
        if employee_list[i]["id"] == id:
            emp = employee_list.pop(i)
            return {"Employee Deleted: ":emp}
    raise HTTPException(status_code=404,detail="Employee not found")


@app.post("/employees/{id}/check_in")
def check_in(id:int):
    time = datetime.now().time()
    date1 = date.today()
    check_in_data = AttendanceRecord(
        employee_id=id,
        date=date1,
        check_in=time
    )
    for i in attendance:
        if i["date"] == date1:
            raise HTTPException(status_code=409,detail="Already checked in")
    attendance.append(check_in_data.__dict__)
    return {"Attendance":attendance}

@app.post("/employee/{id}/checkout")
def checkout(id:int):
    time = datetime.now().time()
    date1 = date.today()
    for i in range(len(attendance)):
        if attendance[i]["employee_id"] == id:
            if attendance[i]["check_in"] == None:
                raise HTTPException(status_code=400,detail="Check-in required before checkout")
            elif attendance[i]["check_out"] != None:
                raise HTTPException(status_code=409,detail="Already check out")
            else:
                attendance[i]["check_out"] = time
                return attendance[i]
    raise HTTPException(status_code=404,detail="Employee not found")

@app.post("/employees/{id}/leave-requests")
def leave_request(id:int,from_date:date,to_date:date,reason:str):
    if from_date>to_date:
        raise HTTPException(status_code=400,detail="From date is after to date")
    global next_leave_id
    leave = LeaveRequest(
        leave_id=next_leave_id,
        employee_id=id,
        from_date=from_date,
        to_date=to_date,
        reason=reason
    )
    leaves.append(leave.__dict__)
    next_leave_id += 1
    return HTTPException(status_code="201",detail="Leave request created")
            
@app.get("/employees/{id}/leave-requests")
def leave_request(id:int):
    req = []
    for i in leaves:
        if i["employee_id"] == id:
            req.append(i)
    if req:
        return req
    else:
        raise HTTPException(status_code=404,detail="Employee not found")
    
            