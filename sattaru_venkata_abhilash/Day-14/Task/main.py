from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import date, datetime, time

# Create an instance of FastAPI
app = FastAPI(title="UST Employee API")

# Pydantic model to represent an Employee
class Employee(BaseModel):
    id: int  # Employee ID
    name: str  # Employee name
    email: str  # Employee email
    department: str  # Employee department
    role: str  # Employee role
    status: str = "active"  # Default status is "active"

# Pydantic model for updating employee details
class EmpUpdate(BaseModel):
    name: str
    email: str
    department: str
    role: str
    status: str

# Pydantic model for creating a new employee
class EmpCreate(BaseModel):
    name: str
    email: str
    department: str
    role: str

# Pydantic model to represent an attendance record
class AttendanceRecord(BaseModel):
    employee_id: int  # Employee ID associated with this attendance
    date: date  # The date of attendance
    check_in: time = None  # Check-in time
    check_out: time = None  # Check-out time

# Pydantic model for a leave request
class LeaveRequest(BaseModel):
    leave_id: int  # Unique leave request ID
    employee_id: int  # Employee ID
    from_date: date  # Start date of the leave
    to_date: date  # End date of the leave
    reason: str  # Reason for the leave
    status: str = "pending"  # Default leave status is "pending"

# Pydantic model for creating a leave request (without ID, as it is auto-generated)
class CreateLeave(BaseModel):
    from_date: date
    to_date: date
    reason: str

# In-memory "database" to store employees
employees: List[Employee] = [
    { "id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active" },
    { "id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active" },
    { "id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department": "HR", "role": "HR", "status": "active" }
]

# In-memory "database" for attendance and leave records
attendance: List[AttendanceRecord] = []
leave_list: List[LeaveRequest] = []

# Variables to track next available employee ID and leave ID
next_emp = 4
next_leave_id = 1

# POST endpoint to add a new employee
@app.post("/employees", response_model=Employee)
def add_employee(employee: EmpCreate):
    # Check if email already exists
    for data in employees:
        if data["email"] == employee.email:
            raise HTTPException(status_code=409, detail="Email already exists")  # Conflict error if email exists
    
    global next_emp
    # Create a new employee
    new_emp = Employee(id=next_emp, name=employee.name, email=employee.email, department=employee.department, role=employee.role)
    employees.append(new_emp.__dict__)  # Add the employee to the "database"
    next_emp += 1  # Increment the employee ID for the next employee
    return new_emp

# GET endpoint to retrieve all employees
@app.get("/employees", response_model=List[Employee])
def get_all_employees():
    return employees  # Return all employees in the list

# GET endpoint to retrieve a specific employee by ID
@app.get("/employees/{id}", response_model=Employee)
def get_employee_by_id(id: int):
    # Search for the employee by ID
    for data in employees:
        if data["id"] == id:
            return data  # Return the employee if found
    
    raise HTTPException(status_code=404, detail="Employee Not Found")  # Error if employee is not found

# PUT endpoint to update an existing employee by ID
@app.put("/employees/{id}", response_model=Employee)
def update_employee(id: int, employee: EmpUpdate):
    # Check for email conflicts before updating
    for i in range(len(employees)):
        if employees[i]["id"] != id and employees[i]["email"] == employee.email:
            raise HTTPException(status_code=409, detail="Email already exists")  # Conflict error for email
    
    # Search for the employee and update their information
    for i in range(len(employees)):
        if employees[i]["id"] == id:
            new_data = Employee(id=id, name=employee.name, email=employee.email, department=employee.department, role=employee.role, status=employee.status)
            employees[i] = new_data.__dict__  # Update the employee data
            return new_data
    
    raise HTTPException(status_code=404, detail="Employee Not Found")  # Error if employee is not found

# DELETE endpoint to delete an employee by ID
@app.delete("/employees/{id}", response_model=Employee)
def delete_employee(id: int):
    for i in range(len(employees)):
        if employees[i]["id"] == id:
            return employees.pop(i)  # Remove and return the deleted employee
    
    raise HTTPException(status_code=404, detail="Employee Not Found")  # Error if employee is not found

# POST endpoint for employee check-in
@app.post("/employees/{id}/checkin", response_model=AttendanceRecord)
def checkin(id: int):
    if get_employee_by_id(id):
        # Check if the employee has already checked in today
        for i in range(len(attendance)):
            if attendance[i]["employee_id"] == id and attendance[i]["date"] == date.today():
                raise HTTPException(status_code=409, detail="Already Checked In")  # Conflict if already checked in
        
        # Create a new check-in record
        check_in_data = AttendanceRecord(employee_id=id, date=date.today(), check_in=datetime.now().time())
        attendance.append(check_in_data.__dict__)  # Add the check-in record
        return check_in_data

# POST endpoint for employee check-out
@app.post("/employees/{id}/checkout", response_model=AttendanceRecord)
def checkout(id: int):
    global current
    if get_employee_by_id(id):
        # Check if the employee has checked in but not checked out yet
        for i in range(len(attendance)):
            if attendance[i]["employee_id"] == id and attendance[i]["check_in"] is None:
                raise HTTPException(status_code=409, detail="No Data to Checkout")  # Error if no check-in record found
            if attendance[i]["employee_id"] == id and attendance[i]["check_out"] is None:
                current = attendance[i]
                # Create a new check-out record
                check_out_data = AttendanceRecord(employee_id=id, date=current["date"], check_in=current["check_in"], check_out=datetime.now().time())
                break
        
        attendance.append(check_out_data.__dict__)  # Add the check-out record
        return check_out_data

# POST endpoint for employees to request leave
@app.post("/employees/{id}/leave-requests", response_model=LeaveRequest)
def leave_request(id: int, leave: CreateLeave):
    if get_employee_by_id(id):
        # Ensure that the from_date is earlier than the to_date
        if leave.from_date < leave.to_date:
            global next_leave_id
            # Create a new leave request
            new_leave = LeaveRequest(leave_id=next_leave_id, employee_id=id, from_date=leave.from_date, to_date=leave.to_date, reason=leave.reason)
            next_leave_id += 1  # Increment the leave ID for the next request
            leave_list.append(new_leave.__dict__)  # Add the leave request to the list
            return new_leave
        else:
            raise HTTPException(status_code=400, detail="From date cannot be later than To date")  # Error if date range is invalid
    
    else:
        raise HTTPException(status_code=404, detail="Employee Data not found")  # Error if employee not found

# GET endpoint to retrieve all leave requests for a specific employee
@app.get("/employees/{id}/leave-requests", response_model=List[LeaveRequest])
def get_leave_requests(id: int):
    lis = []
    if get_employee_by_id(id):
        # Collect all leave requests for the employee
        for data in leave_list:
            if data["employee_id"] == id:
                lis.append(data)
        return lis  # Return the list of leave requests
