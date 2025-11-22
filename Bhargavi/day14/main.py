
# from fastapi import FastAPI,HTTPException
# from pydantic import BaseModel
# from typing import List

# app = FastAPI(title="Student Management System")

# class Student(BaseModel):
#     name : str
#     age : int
#     grade : str = "Not Provided"

# students : List[Student] = []

# @app.post("/students",response_model=Student)
# def add_student(student:Student):
#     students.append(student)
#     return student

# @app.get("/students",response_model=List[Student])
# def get_all_students():
#     return students

# @app.get("/students/{index}",response_model=Student)
# def get_student_by_index(index:int):
#     try:
#         return students[index]
#     except IndexError:
#         raise HTTPException(status_Code=404,detail="student not found")
    
# @app.put("/students/{index}", response_model= List[Student])
# def update_student(index: int, updated_student: Student):
#     try:
#         students[index] = updated_student
#         return updated_student
#     except IndexError:
#         raise HTTPException(status_code=404,detail="student not found")
    
# @app.delete("/students/{index}",response_model=Student)
# def delete_student(index: int):
#     try:
#         removed = students.pop(index)
#         return removed
#     except IndexError:
#         raise HTTPException(status_code=404,detail="student not found")
 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, date, time

app = FastAPI(title="UST Employee API")

# Employee Pydantic model
class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "active"

# AttendanceRecord model
class AttendanceRecord(BaseModel):
    employee_id: int
    date: date
    check_in: Optional[time] = None
    check_out: Optional[time] = None

# LeaveRequest model
class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: date
    to_date: date
    reason: str
    status: str = "pending"


employees: List[Employee] = [
    {"id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active"},
    {"id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active"},
    {"id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department": "HR", "role": "HR", "status": "active"}
]

attendance: List[AttendanceRecord] = []
leaves: List[LeaveRequest] = []

next_emp_id = 4
next_leave_id = 1


# 1. Create employee
@app.post("/employees", status_code=201)
def create_employee(emp: Employee):
    global next_emp_id
    for i in employees:
        if i["email"] == emp.email:
            raise HTTPException(status_code=409, detail="Email already exists")
    emp.id = next_emp_id
    next_emp_id += 1
    employees.append(emp.dict())
    return {"Employee Created": emp}


# 2. List all employees 
@app.get("/employees", response_model=List[Employee])
def list_employees(department: Optional[str] = None):
    if department:
        return [emp for emp in employees if emp["department"] == department]
    return employees


# 3. Get employee by ID 
@app.get("/employees/{id}", response_model=Employee)
def get_employee(id: int):
    for emp in employees:
        if emp["id"] == id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")


# 4. Update employee 
@app.put("/employees/{id}")
def update_employee(id: int, emp: Employee):
    for i in range(len(employees)):
        if employees[i]["id"] == id:
            if any(e["email"] == emp.email for e in employees if e["id"] != id):
                raise HTTPException(status_code=409, detail="Email already exists")
            employees[i] = emp.dict()
            return employees[i]
    raise HTTPException(status_code=404, detail="Employee not found")


# 5. Delete employee 
@app.delete("/employees/{id}")
def delete_employee(id: int):
    global employees
    for i in range(len(employees)):
        if employees[i]["id"] == id:
            employees.pop(i)
            return {"detail": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")


# 6. Check-in (attendance)
@app.post("/employees/{id}/checkin", status_code=201)
def check_in(id: int, record: AttendanceRecord):
    for emp in employees:
        if emp["id"] == id:
            for att in attendance:
                if att.employee_id == id and att.date == record.date and att.check_in is not None:
                    raise HTTPException(status_code=409, detail="Already checked in")
            attendance.append(record)
            return record
    raise HTTPException(status_code=404, detail="Employee not found")


# 7. Check-out (attendance)
@app.post("/employees/{id}/checkout")
def check_out(id: int, record: AttendanceRecord):
    for emp in employees:
        if emp["id"] == id:
            for att in attendance:
                if att.employee_id == id and att.date == record.date and att.check_in is not None:
                    if att.check_out is not None:
                        raise HTTPException(status_code=409, detail="Already checked out")
                    att.check_out = record.check_out
                    return att
            raise HTTPException(status_code=400, detail="Check-in required before checkout")
    raise HTTPException(status_code=404, detail="Employee not found")


# 8. Create leave request 
@app.post("/employees/{id}/leave-requests", status_code=201)
def create_leave_request(id: int, leave_request: LeaveRequest):
    global next_leave_id
    if leave_request.from_date > leave_request.to_date:
        raise HTTPException(status_code=400, detail="from_date must be on or before to_date")
    for emp in employees:
        if emp["id"] == id:
            leave_request.leave_id = next_leave_id
            next_leave_id += 1
            leaves.append(leave_request.dict())
            return leave_request
    raise HTTPException(status_code=404, detail="Employee not found")


# 9. List leave requests for an employee
@app.get("/employees/{id}/leave-requests")
def list_leave_requests(id: int):
    for emp in employees:
        if emp["id"] == id:
            return [leave for leave in leaves if leave["employee_id"] == id]
    raise HTTPException(status_code=404, detail="Employee not found")
