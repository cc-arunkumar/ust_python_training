from typing import List
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel 
import datetime

# create FastAPI app instance
app = FastAPI(title="UST Employee API")

# global counters used to generate simple incremental ids
next_emp_id = 4
next_leave_id = 0
class Employee(BaseModel):
    # employee model used for request/response validation
    id:int = next_emp_id
    name: str
    email: str
    department: str
    role: str
    status: str = "active"

class AttendanceRecord(BaseModel):
    # attendance record for a single date
    employee_id: int
    date: datetime.date
    check_in: datetime.time = None
    check_out: datetime.time = None

class LeaveRequest(BaseModel):
    # simple leave request model
    leave_id: int = next_leave_id
    employee_id: int
    from_date: datetime.date 
    to_date: datetime.date
    reason: str
    status : str = "pending"

# in-memory storage (list of dicts) for demo/testing
employees : List[Employee] = [
 { "id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department":"Engineering", "role": "Engineer", "status": "active" },
 { "id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department":"Delivery", "role": "Manager", "status": "active" },
 { "id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department":"HR", "role": "HR", "status": "active" }
]

# attendance and leaves stored in-memory for this example
attendance : List[AttendanceRecord] = []
leaves : List[LeaveRequest]=[]

@app.post("/employees")

def create_employee(employee: Employee):
    # prevent duplicate emails
    for emp in employees:
        if employee.email == emp['email']:
            raise HTTPException(status_code=409,detail="Email Already Exists")
        
    # assign a new id and increment the global counter
    global next_emp_id
    employee.id = next_emp_id
    next_emp_id += 1 

    # store the Pydantic model (could also store employee.dict())
    employees.append(employee)
    return {"Employee Created":employee}

@app.get('/employees')
def get_all_employees(department:str=""):
    if department=="":
        return employees
    else:
        new_list = []
        for emp in employees:
            if emp['department'] == department:
                new_list.append(emp)
        if len(new_list)>0:
            return new_list
        else:
            # no employees for given department
            return {"details":"Employee not found in Department"}
        
@app.get('/employees/{id}',response_model=Employee)
def get_emp_id(new_id:int):
    for emp in employees:
        if emp['id'] == new_id:
            return emp
    # not found -> 404-like response body
    return {"details":"Employee Not Found!"}

@app.put('/employees/{id}',response_model=Employee)
def update_employee(id:int,employee:Employee):
    for emp in employees:
        if emp['id'] == id:
            emp['name'] = employee.name
            for emp in employees:
                if employee.email == emp['email']:
                    raise HTTPException(status_code=409,detail="Email Already Exists")
            emp['email'] = employee.email
            emp['department'] = employee.department
            emp['role'] = employee.role 
            emp['status'] = employee.status
            return employee
    raise HTTPException(status_code=404,detail="ID Not Found")

@app.delete('/employees/{id}')
def delete_employee(id:int):
    for emp in employees:
        if emp['id'] == id:
            # remove by index (assumes ids match list order)
            employees.pop(id-1)
            return {"detail":"Employee deleted"} 
    raise HTTPException(status_code=404,detail="Employee Not Found")

    
@app.post('/employees/{id}/checkin',response_model=AttendanceRecord)
def update_checkin(id:int,attendance_obj:AttendanceRecord):
    for emp in employees:
        if emp['id']==id:
            # ensure we don't double check-in for same date
            for att in attendance:
                if att.employee_id == id and att.check_in is not None and att.date == attendance_obj.date:
                    raise HTTPException(status_code=409,detail="Already Check in")
            # set employee id on the record and store it
            attendance_obj.employee_id = id
            attendance.append(attendance_obj)
            return attendance_obj
    raise HTTPException(status_code=404,detail="Employee Not Found!")

@app.post('/employees/{id}/checkout',response_model=AttendanceRecord)
def update_checkout(id:int,attendance_obj:AttendanceRecord):
    for emp in employees:
        if emp['id']==id:
            # enforce check-in before check-out and prevent double checkout
            for att in attendance:
                if att.employee_id == id and att.check_in is not None and att.date== attendance_obj.date:
                    raise HTTPException(status_code=400,detail="Check-in required before checkout")
                if att.employee_id == id and att.check_out is not None and att.date== attendance_obj.date:
                    raise HTTPException(status_code=409,detail="Already Checked Out")
            attendance_obj.employee_id = id
            attendance.append(attendance_obj)
            return attendance_obj
    raise HTTPException(status_code=404,detail="Employee Not Found!")


@app.post('/employees/{id}/leave-requests',response_model=LeaveRequest)
def create_leave_req(id:int,new_leave:LeaveRequest):
    for emp in employees:
        if emp['id']==id:
            if new_leave.from_date  <  new_leave.to_date:
                # assign an incremental leave id and save the request
                global next_leave_id 
                new_leave.leave_id = next_leave_id 
                next_leave_id += 1 
                leaves.append(new_leave)
                return new_leave
            else:
                raise HTTPException(status_code=400,detail="Invalid From Date and To Date")
    raise HTTPException(status_code=404,detail="Employee Not Found!")

@app.get('/employees/{id}/leave-requests')
def list_requests(id:int):
    for emp in employees:
        if emp['id']==id:
            return leaves 
    raise HTTPException(status_code=404,detail="Employee Not Found!")

    
             
    