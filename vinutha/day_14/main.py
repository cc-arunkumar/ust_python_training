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
# @app.put("/students/{index}",response_model=Student)
# def update_student(index:int,updated_student:Student):
#     try:
#         students[index]=updated_student
#         return updated_student
#     except IndexError:
#         raise HTTPException(status_code=404,detail="Student not found")
    
# @app.delete("/students/{index}",response_model=Student)
# def delete_student(index:int):
#     try:
#         removed=students.pop(index)
#         return removed
#     except IndexError:
#         raise HTTPException(status_code=404,detail="Student not found")
        





# Task CRUD 
# Simpler use-case: UST Employee API

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import date, datetime, time

# Initialize FastAPI app with a title
app = FastAPI(title="UST Employee API")

# Define a Pydantic model for Employee data
class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "active"  # Default status is "active"

# Define a Pydantic model for updating Employee data
class EmpUpdate(BaseModel):
    name: str
    email: str
    department: str
    role: str
    status: str

# Define a Pydantic model for creating an Employee (without id)
class EmpCreate(BaseModel):
    name: str
    email: str
    department: str
    role: str

# Define a Pydantic model for Attendance Record
class AttendanceRecord(BaseModel):
    employee_id: int
    date: date
    check_in: time = None  # Default value is None for check-in
    check_out: time = None  # Default value is None for check-out

# Define a Pydantic model for Leave Request
class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: date
    to_date: date
    reason: str
    status: str = "pending"  # Default status is "pending"

# Define a Pydantic model for creating a leave request (without leave_id)
class CreateLeave(BaseModel):
    from_date: date
    to_date: date
    reason: str

# Initial dummy employee data
employees: List[Employee] = [
    {"id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active"},
    {"id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active"},
    {"id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department": "HR", "role": "HR", "status": "active"}
]

# Empty list to track attendance and leave requests
attendance: List[AttendanceRecord] = []
leave_list: List[LeaveRequest] = []

# Track the next employee and leave ID
next_emp = 4
next_leave_id = 1

# Endpoint to add a new employee
@app.post("/employees", response_model=Employee)
def add_employee(employee: EmpCreate):
    # Check if the email already exists
    for data in employees:
        if data["email"] == employee.email:
            raise HTTPException(status_code=409, detail="Email already exists")

    # Add the new employee
    global next_emp
    new_emp = Employee(id=next_emp, name=employee.name, email=employee.email, department=employee.department, role=employee.role)
    employees.append(new_emp.dict())  # Add employee to list
    next_emp += 1  # Increment the employee ID for the next employee
    return new_emp

# Endpoint to get all employees
@app.get("/employees", response_model=List[Employee])
def get_all_employees():
    return employees

# Endpoint to get an employee by ID
@app.get("/employees/{id}", response_model=Employee)
def get_employee_by_id(id: int):
    # Search for the employee by ID
    for data in employees:
        if data["id"] == id:
            return data
    # Raise an exception if employee not found
    raise HTTPException(status_code=404, detail="Employee Not Found")

# Endpoint to update an employee's details
@app.put("/employees/{id}", response_model=Employee)
def update_employee(id: int, employee: EmpUpdate):
    # Check if another employee has the same email
    for i in range(len(employees)):
        if employees[i]["id"] != id and employees[i]["email"] == employee.email:
            raise HTTPException(status_code=409, detail="Email already exists")

    # Update the employee data if ID matches
    for i in range(len(employees)):
        if employees[i]["id"] == id:
            new_data = Employee(id=id, name=employee.name, email=employee.email, department=employee.department, role=employee.role, status=employee.status)
            employees[i] = new_data.dict()  # Replace with new data
            return new_data

    # Raise an exception if employee not found
    raise HTTPException(status_code=404, detail="Employee Not Found")

# Endpoint to delete an employee by ID
@app.delete("/employees/{id}", response_model=Employee)
def delete_employee(id: int):
    # Search for the employee by ID and remove it from the list
    for i in range(len(employees)):
        if employees[i]["id"] == id:
            return employees.pop(i)  # Remove employee from list
    # Raise an exception if employee not found
    raise HTTPException(status_code=404, detail="Employee Not Found")

# Endpoint for employee check-in
@app.post("/employees/{id}/checkin", response_model=AttendanceRecord)
def checkin(id: int):
    # Ensure the employee exists
    if get_employee_by_id(id):
        # Check if the employee has already checked in today
        for i in range(len(attendance)):
            if attendance[i]["employee_id"] == id and attendance[i]["date"] == date.today():
                raise HTTPException(status_code=409, detail="Already Checked In")

        # Record the check-in time
        check_in_data = AttendanceRecord(employee_id=id, date=date.today(), check_in=datetime.now().time())
        attendance.append(check_in_data.dict())  # Add to attendance list
        return check_in_data

# Endpoint for employee check-out
@app.post("/employees/{id}/checkout", response_model=AttendanceRecord)
def checkout(id: int):
    # Ensure the employee exists
    if get_employee_by_id(id):
        # Check if the employee has checked in and not checked out yet
        for i in range(len(attendance)):
            if attendance[i]["employee_id"] == id and attendance[i]["check_in"] is None:
                raise HTTPException(status_code=409, detail="No Data to Checkout")
            if attendance[i]["employee_id"] == id and attendance[i]["check_out"] is None:
                current = attendance[i]
                check_out_data = AttendanceRecord(
                    employee_id=id,
                    date=current["date"],
                    check_in=current["check_in"],
                    check_out=datetime.now().time()
                )
                attendance.append(check_out_data.dict())  # Add to attendance list
                return check_out_data

    # Raise an exception if employee not found
    raise HTTPException(status_code=404, detail="Employee Not Found")

# Endpoint for submitting a leave request
@app.post("/employees/{id}/leave-requests", response_model=LeaveRequest)
def leave_request(id: int, leave: CreateLeave):
    # Ensure the employee exists
    if get_employee_by_id(id):
        # Validate that the from_date is before to_date
        if leave.from_date < leave.to_date:
            global next_leave_id
            new_leave = LeaveRequest(leave_id=next_leave_id, employee_id=id, from_date=leave.from_date, to_date=leave.to_date, reason=leave.reason)
            next_leave_id += 1  # Increment leave ID
            leave_list.append(new_leave.dict())  # Add to leave list
            return new_leave
        else:
            raise HTTPException(status_code=400, detail="From date cannot be less than the To date")
    else:
        raise HTTPException(status_code=404, detail="Employee Data not found")

# Endpoint to get leave requests by employee ID
@app.get("/employees/{id}/leave-requests", response_model=List[LeaveRequest])
def get_leave_requests(id: int):
    lis = []
    # Ensure the employee exists
    if get_employee_by_id(id):
        # Search for leave requests related to the employee
        for data in leave_list:
            if data["employee_id"] == id:
                lis.append(data)
        return lis
    # Raise an exception if employee not found
    raise HTTPException(status_code=404, detail="Employee Not Found")
