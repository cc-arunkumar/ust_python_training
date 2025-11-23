from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from datetime import date,datetime

app=FastAPI(title="Employee Management System")


leave_list=[]
attendence_list=[]

emp_id=int(3)
leave_id=0
class Employee(BaseModel):
        id:int=emp_id+1
        name:str
        email:str
        department:str
        role:str
        status:str="active"

# LeaveRequest
class AttendanceRecord(BaseModel):
    employee_id:int
    date:str
    check_in:str
    check_out:str

class LeaveRequest(BaseModel):
    leave_id:int=leave_id+1
    employee_id:int
    from_date:str
    to_date:str
    reason:str
    status:str="pending"

    
employee_list=[
 { "id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department":
"Engineering", "role": "Engineer", "status": "active" },
 { "id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department":
"Delivery", "role": "Manager", "status": "active" },
 { "id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department":
"HR", "role": "HR", "status": "active" }
]


@app.post("/employee")
def create_employee(emp:Employee):
        if emp.email not in employee_list:
            employee_list.append(emp)
            return emp
        else:
            raise HTTPException(status_code=409,detail="The email already exist")

@app.get("/employee")
def show_employee():
    return {"All employees":employee_list}

# 3) Get employee by id
@app.get("/employee/{id}")
def get_emp_with_id(id:int):
    try:
        for emp in employee_list:
            if emp["id"]==id:
                return {"id":emp}
    except HTTPException:
        raise HTTPException(status_code=404,detail="Employee not found")
    
# 4) Update employee (replace)

@app.put("/employee/{id}")
def update_employee(id:int,emp:Employee):
    try:
        if emp.email not in employee_list:
            for dic in employee_list:
                if dic["id"]==id:
                    dic["name"]=emp.name
                    dic["email"]=emp.email
                    dic["department"]=emp.department
                    dic["role"]=emp.role
                    dic["status"]=emp.status
                    print(dic)
            return emp
    except HTTPException:
        raise HTTPException(status_code=404,detail="User not found")
    
#5) Delete employee


@app.delete("/employee/{id}")
def delete_employee(id:int):
    index_count=-1
    try:
        for e in employee_list:
            index_count+=1
            if e["id"]==id:
                removed_emp=employee_list.pop(index_count)
    except HTTPException:
        raise HTTPException(status_code=404,detail="employee deleted")
    return removed_emp

@app.post("/employee/check-in/{id}")
def emp_check_in(id: int):
    for emp in employee_list:
        if id == emp["id"]:
            for atten in attendence_list:
                if atten["employee_id"] == id and atten["check_out"] == "null":
                    # If employee has already checked in, return error
                    return {"detail": "Already checked-in"}, 409
            
            current_time = datetime.now().time()
            formatted_time = current_time.strftime("%H:%M:%S")
            current_date = date.today()
            formatted_date = current_date.strftime("%d-%m-%Y")
            
            atten_dict = {
                "employee_id": id,
                "date": formatted_date,
                "check_in": formatted_time,
                "check_out": "null"
            }
            attendence_list.append(atten_dict)
            return atten_dict  # Return the check-in record

    raise HTTPException(status_code=404, detail="Employee not found")  # Employee not found

@app.post("/employee/check-out/{id}")
def emp_check_out(id: int):
    for emp in employee_list:
        if id == emp["id"]:
            for attendence in attendence_list:
                if attendence["employee_id"] == id and attendence["check_out"] == "null":
                    current_time = datetime.now().time()
                    formatted_time = current_time.strftime("%H:%M:%S")
                    current_date = date.today()
                    formatted_date = current_date.strftime("%d-%m-%Y")
                    
                    attendence["check_out"] = formatted_time
                    attendence["date"] = formatted_date  # Update the date as well
                    
                    return attendence  # Return the updated attendance record

            return {"detail": "Check-in required before checkout"}, 400  # No check-in found for checkout

    raise HTTPException(status_code=404, detail="Employee not found")  # Employee not found

@app.post("/employee/{id}/leave-requests")
def leave_request(id: int, leave: LeaveRequest):
    if leave.from_date > leave.to_date:
        raise HTTPException(status_code=400, detail="from_date must be on or before to_date")
    
    leave.employee_id = id  # Associate the leave request with the employee's ID
    leave_list.append(leave)
    return leave

# 9) List leave requests for employee
@app.get("/employee/{id}/leave-requests")
def display_leave_list(id: int):
    employee_leaves = []
    for detail in leave_list:
        if detail.employee_id == id:
            employee_leaves.append(detail)
    
    if not employee_leaves:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return employee_leaves  # Return a list of leave requests for the employee
