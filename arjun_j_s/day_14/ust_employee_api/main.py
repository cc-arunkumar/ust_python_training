from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List
from datetime import date,datetime,time

app = FastAPI(title="UST Employee API")

class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "active" 

class EmpUpdate(BaseModel):
    name: str
    email: str
    department: str
    role: str
    status: str 

class EmpCreate(BaseModel):
    name: str
    email: str
    department: str
    role: str

class AttendanceRecord(BaseModel):
    employee_id: int
    date: date
    check_in: time = None
    check_out: time = None


class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: date
    to_date: date
    reason: str
    status: str = "pending"

class CreateLeave(BaseModel):
    from_date: date
    to_date: date
    reason: str


employees : List[Employee] = [
 { "id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department":
"Engineering", "role": "Engineer", "status": "active" },
 { "id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department":
"Delivery", "role": "Manager", "status": "active" },
 { "id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department":
"HR", "role": "HR", "status": "active" }
]

attendance : List[AttendanceRecord] = []
leave_list : List[LeaveRequest] = []

next_emp = 4
next_leave_id = 1

@app.post("/employees",response_model=Employee)
def add_employee(employee:EmpCreate):
    for data in employees:
        if(data["email"]==employee.email):
            raise HTTPException(status_code=409,detail="Email already exists")
    global next_emp
    
    new_emp = Employee(id=next_emp,
                             name=employee.name,
                             email=employee.email,
                             department=employee.department,
                             role=employee.role
                             )
    employees.append(new_emp.__dict__)
    next_emp+=1
    return new_emp

@app.get("/employees",response_model=List[Employee])
def get_all_employees():
    return employees

@app.get("/employees/{id}",response_model=Employee)
def get_employee_by_id(id:int):
    for data in employees:
        if(data["id"]==id):
            return data
    
    raise HTTPException(status_code=404,detail="Employee Not Found")

@app.put("/employees/{id}",response_model=Employee)
def update_employee(id:int,employee:EmpUpdate):
    for i in range(len(employees)):
        if (employees[i]["id"]!=id and employees[i]["email"]==employee.email):
                raise HTTPException(status_code=409,detail="Email already exists")
    for i in range(len(employees)):
        if(employees[i]["id"]==id):
                new_data = Employee(id=id,
                            name=employee.name,
                            email=employee.email,
                            department=employee.department,
                            role=employee.role,
                            status=employee.status
                            )
                employees[i] = new_data.__dict__
                return new_data

    raise HTTPException(status_code=404,detail="Employee Not Found")

@app.delete("/employees/{id}",response_model=Employee)
def delete_employee(id:int):
    for i in range(len(employees)):
        if(employees[i]["id"]==id):
            return employees.pop(i)
        
    raise HTTPException(status_code=404,detail="Employee Not Found")

@app.post("/employees/{id}/checkin",response_model=AttendanceRecord)
def checkin(id:int):
    if(get_employee_by_id(id)):
        for i in range(len(attendance)):
            if(attendance[i]["employee_id"]==id and attendance[i]["date"]==date.today()):
                raise HTTPException(status_code=409,detail="Already Checked In")
        check_in_data = AttendanceRecord(
            employee_id=id,
            date=date.today(),
            check_in=datetime.now().time()
        )
        attendance.append(check_in_data.__dict__)
        return check_in_data

@app.post("/employees/{id}/checkout",response_model=AttendanceRecord)
def checkout(id:int):
    global current
    if(get_employee_by_id(id)):
        for i in range(len(attendance)):
            if(attendance[i]["employee_id"]==id and (attendance[i]["check_in"]==None)):
                raise HTTPException(status_code=409,detail="No Data to Checkout")
            if(attendance[i]["employee_id"]==id and attendance[i]["check_out"]==None):
                current = attendance[i]
                check_out_data = AttendanceRecord(
                employee_id=id,
                date=current["date"],
                check_in=current["check_in"],
                check_out=datetime.now().time()
                )
                break
                 
        
        attendance.append(check_out_data.__dict__)
    return check_out_data
    
@app.post("/employees/{id}/leave-requests",response_model=LeaveRequest)
def leave_request(id:int,leave:CreateLeave):
    if(get_employee_by_id(id)):
        if(leave.from_date<leave.to_date):
            global next_leave_id
            new_leave=LeaveRequest(
                leave_id=next_leave_id,
                employee_id=id,
                from_date=leave.from_date,
                to_date=leave.to_date,
                reason=leave.reason,
            )
            next_leave_id+=1
            leave_list.append(new_leave.__dict__)
            return new_leave
        else:
            raise HTTPException(status_code=400,detail="From date cannot be a less than  date")
    else:
        raise HTTPException(status_code=404,detail="Employee Data not found")

@app.get("/employees/{id}/leave-requests",response_model=List[LeaveRequest])
def leave_request(id:int):
    lis=[]
    if(get_employee_by_id(id)):
        for data in leave_list:
            if(data["employee_id"]==id):
                lis.append(data)
        return lis