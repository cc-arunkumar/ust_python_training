from typing import List
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="UST Employee API")

# In memory storage for employees, attendance, and leaves
employees: List[dict] = [
    {"id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active"},
    {"id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active"},
    {"id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department": "HR", "role": "HR", "status": "active"}
]

attendance:List[dict]=[]
leaves:List[dict]=[]

next_emp_id=4
next_leave_id=1


class Employee(BaseModel):
    name:str
    email:str
    department:str
    role:str
    status:str="active"

    # Manually convert model to dictionary
    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "department": self.department,
            "role": self.role,
            "status": self.status
        }


class AttendanceRecord(BaseModel):
    employee_id: int
    date: str
    check_in: str
    check_out: str

    # Manually convert model to dictionary
    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "date": self.date,
            "check_in": self.check_in,
            "check_out": self.check_out
        }


class LeaveRequest(BaseModel):
    from_date: str
    to_date: str
    reason: str
    status: str = "pending"

    # Manually convert model to dictionary
    def to_dict(self):
        return {
            "from_date": self.from_date,
            "to_date": self.to_date,
            "reason": self.reason,
            "status": self.status
        }


@app.post("/employees", status_code=201)
def create_employee(employee: Employee):
    # Check if the employee already exists by email
    for emp in employees:
        if emp["email"] == employee.email:
            raise HTTPException(status_code=409, detail="Employee already exists")

    global next_emp_id
    new_employee = employee.to_dict()  # Use the custom to_dict method
    new_employee['id'] = next_emp_id
    employees.append(new_employee)
    next_emp_id += 1
    return new_employee


@app.get("/employees", response_model=List[Employee])
def list_employee(department: str | None = None):
    if department:
        filtered_employees = []
        for emp in employees:
            if emp['department'] == department:
                filtered_employees.append(emp)
        return filtered_employees
    return employees


@app.get("/employees/{id}", response_model=Employee)
def filter_employee(id: int):
    employee = None
    for emp in employees:
        if emp['id'] == id:
            employee = emp
            break
    if employee is None:
        raise HTTPException(status_code=404,detail="Employee not found")
    return employee


@app.put("/employees/{id}", response_model=Employee)
def update_employee(id: int, updated_employee: Employee):
    employee = None
    for emp in employees:
        if emp['id'] == id:
            employee = emp
            break
    
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    employee["name"] = updated_employee.name
    employee["email"] = updated_employee.email
    employee["department"] = updated_employee.department
    employee["role"] = updated_employee.role
    employee["status"] = updated_employee.status

    return employee


@app.delete("/employees/{id}")
def delete_employee(id: int):
    global employees  
    employee = None
    for emp in employees:
        if emp['id'] == id:
            employee = emp
            break
    
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    updated_employees = []
    for emp in employees:
        if emp['id'] != id:
            updated_employees.append(emp)
    
    employees = updated_employees
    
    return {"detail": "Employee deleted successfully"}


@app.post("/employees/{id}/check_in")
def check_in(id: int, attendance_record: AttendanceRecord):
    employee = None
    for emp in employees:
        if emp["id"] == id:
            employee = emp
            break
        
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    # Check if attendance for this date already exists
    existing_record = None
    for att in attendance:
        if att['employee_id'] == id and att['date'] == attendance_record.date:
            existing_record = att
            break
    
    if existing_record:
        raise HTTPException(status_code=409, detail="Already checked in for this date")   
    
    # Create a new attendance record
    new_record = attendance_record.to_dict()  
    attendance.append(new_record)
    return new_record


@app.post("/employees/{id}/checkout")
def check_out(id: int, attendance_record: AttendanceRecord):
    # Find employee
    employee = None
    for emp in employees:
        if emp["id"] == id:
            employee = emp
            break

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    # Find attendance record for this employee and date
    record = None
    for att in attendance:
        if att["employee_id"] == id and att["date"] == attendance_record.date:
            record = att
            break
    
    if not record:
        raise HTTPException(status_code=400, detail="Check-in required before checkout")

    if record["check_out"]:
        raise HTTPException(status_code=409, detail="Already checked out")

    # Update checkout time
    record["check_out"] = attendance_record.check_out
    return record


@app.post("/employees/{id}/leave-requests", status_code=201)
def create_leave_request(id: int, leave_request: LeaveRequest):
    # Check if employee exists
    employee = None
    for emp in employees:
        if emp["id"] == id:
            employee = emp
            break
    
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    # Validate dates
    try:
        from_date = datetime.strptime(leave_request.from_date, "%Y-%m-%d")
        to_date = datetime.strptime(leave_request.to_date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    if from_date > to_date:
        raise HTTPException(status_code=400, detail="from_date must be on or before to_date")
    
    global next_leave_id
    new_leave_request = leave_request.to_dict()  # Use the custom to_dict method
    new_leave_request["leave_id"] = next_leave_id
    new_leave_request["employee_id"] = id
    
    leaves.append(new_leave_request)
    next_leave_id += 1

    return new_leave_request


@app.get("/employees/{id}/leave-requests")
def list_leave_requests(id: int):
    # Check if employee exists
    employee = None
    for emp in employees:
        if emp["id"] == id:
            employee = emp
            break

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    # Get all leave requests for this employee
    employee_leaves = []
    for leave in leaves:
        if leave["employee_id"] == id:
            employee_leaves.append(leave)

    return employee_leaves
