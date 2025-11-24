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

attendance:List[dict]=[]  # Stores attendance records
leaves:List[dict]=[]  # Stores leave requests

next_emp_id=4  # Next available employee ID
next_leave_id=1  # Next available leave request ID


class Employee(BaseModel):
    name:str  # Employee name
    email:str  # Employee email
    department:str  # Employee department
    role:str  # Employee role
    status:str="active"  # Default status is active

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
    employee_id: int  # Employee ID
    date: str  # Attendance date
    check_in: str  # Check-in time
    check_out: str  # Check-out time

    # Manually convert model to dictionary
    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "date": self.date,
            "check_in": self.check_in,
            "check_out": self.check_out
        }


class LeaveRequest(BaseModel):
    from_date: str  # Start date of leave
    to_date: str  # End date of leave
    reason: str  # Reason for leave
    status: str = "pending"  # Default status is pending

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
    """
    API to create a new employee.
    - Checks if the employee already exists by email.
    - Adds the new employee to the list with a unique employee ID.
    """
    # Check if the employee already exists by email
    for emp in employees:
        if emp["email"] == employee.email:
            raise HTTPException(status_code=409, detail="Employee already exists")

    global next_emp_id
    new_employee = employee.to_dict()  # Use the custom to_dict method
    new_employee['id'] = next_emp_id  # Assign new employee ID
    employees.append(new_employee)  # Add the new employee to the list
    next_emp_id += 1  # Increment the employee ID counter
    return new_employee


@app.get("/employees", response_model=List[Employee])
def list_employee(department: str | None = None):
    """
    API to list all employees or filter employees by department.
    - If department is provided, filters employees by that department.
    """
    # If a department is specified, filter employees by department
    if department:
        filtered_employees = []
        for emp in employees:
            if emp['department'] == department:
                filtered_employees.append(emp)
        return filtered_employees
    return employees  # Return all employees if no department filter


@app.get("/employees/{id}", response_model=Employee)
def filter_employee(id: int):
    """
    API to get details of a specific employee by their ID.
    - Returns the employee details if found, or raises an error if not found.
    """
    # Find employee by ID
    employee = None
    for emp in employees:
        if emp['id'] == id:
            employee = emp
            break
    if employee is None:
        raise HTTPException(status_code=404,detail="Employee not found")  # Employee not found
    return employee


@app.put("/employees/{id}", response_model=Employee)
def update_employee(id: int, updated_employee: Employee):
    """
    API to update an employee's details.
    - Finds the employee by ID and updates their details.
    """
    # Find the employee to update
    employee = None
    for emp in employees:
        if emp['id'] == id:
            employee = emp
            break
    
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")  # Employee not found

    # Update the employee details
    employee["name"] = updated_employee.name
    employee["email"] = updated_employee.email
    employee["department"] = updated_employee.department
    employee["role"] = updated_employee.role
    employee["status"] = updated_employee.status

    return employee


@app.delete("/employees/{id}")
def delete_employee(id: int):
    """
    API to delete an employee by their ID.
    - Removes the employee from the list if found.
    """
    global employees  
    employee = None
    for emp in employees:
        if emp['id'] == id:
            employee = emp
            break
    
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")  # Employee not found
    
    updated_employees = []
    # Remove the employee from the list
    for emp in employees:
        if emp['id'] != id:
            updated_employees.append(emp)
    
    employees = updated_employees  # Update the employee list
    
    return {"detail": "Employee deleted successfully"}


@app.post("/employees/{id}/check_in")
def check_in(id: int, attendance_record: AttendanceRecord):
    """
    API to check in an employee.
    - Checks if the employee exists and if they are already checked in for the day.
    """
    # Find the employee by ID
    employee = None
    for emp in employees:
        if emp["id"] == id:
            employee = emp
            break
        
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")  # Employee not found
    
    # Check if attendance for this date already exists
    existing_record = None
    for att in attendance:
        if att['employee_id'] == id and att['date'] == attendance_record.date:
            existing_record = att
            break
    
    if existing_record:
        raise HTTPException(status_code=409, detail="Already checked in for this date")  # Already checked in
    
    # Create a new attendance record
    new_record = attendance_record.to_dict()  
    attendance.append(new_record)  # Add the new record to attendance list
    return new_record


@app.post("/employees/{id}/checkout")
def check_out(id: int, attendance_record: AttendanceRecord):
    """
    API to check out an employee.
    - Checks if the employee has checked in first.
    """
    # Find employee
    employee = None
    for emp in employees:
        if emp["id"] == id:
            employee = emp
            break

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")  # Employee not found

    # Find attendance record for this employee and date
    record = None
    for att in attendance:
        if att["employee_id"] == id and att["date"] == attendance_record.date:
            record = att
            break
    
    if not record:
        raise HTTPException(status_code=400, detail="Check-in required before checkout")  # No check-in record found

    if record["check_out"]:
        raise HTTPException(status_code=409, detail="Already checked out")  # Already checked out

    # Update checkout time
    record["check_out"] = attendance_record.check_out
    return record


@app.post("/employees/{id}/leave-requests", status_code=201)
def create_leave_request(id: int, leave_request: LeaveRequest):
    """
    API to create a leave request for an employee.
    - Validates leave dates and adds the leave request to the list.
    """
    # Check if employee exists
    employee = None
    for emp in employees:
        if emp["id"] == id:
            employee = emp
            break
    
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")  # Employee not found
    
    # Validate dates
    try:
        from_date = datetime.strptime(leave_request.from_date, "%Y-%m-%d")
        to_date = datetime.strptime(leave_request.to_date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")  # Invalid date format

    if from_date > to_date:
        raise HTTPException(status_code=400, detail="from_date must be on or before to_date")  # Invalid date range
    
    global next_leave_id
    new_leave_request = leave_request.to_dict()  # Use the custom to_dict method
    new_leave_request["leave_id"] = next_leave_id  # Assign new leave ID
    new_leave_request["employee_id"] = id  # Associate leave request with employee
    
    leaves.append(new_leave_request)  # Add the new leave request to the list
    next_leave_id += 1  # Increment the leave ID counter

    return new_leave_request


@app.get("/employees/{id}/leave-requests")
def list_leave_requests(id: int):
    """
    API to list all leave requests for an employee.
    - Returns a list of leave requests for the given employee ID.
    """
    # Check if employee exists
    employee = None
    for emp in employees:
        if emp["id"] == id:
            employee = emp
            break

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")  # Employee not found

    # Get all leave requests for this employee
    employee_leaves = []
    for leave in leaves:
        if leave["employee_id"] == id:
            employee_leaves.append(leave)

    return employee_leaves







#Sample output


# Sample Output for Day 14 Testing (Important Test Cases)

# Test 1: Create Employee
## Input:
# POST /employees
# {
#   "name": "Nisha Rao",
#   "email": "nisha@ust.com",
#   "department": "Engineering",
#   "role": "QA"
# }

# ## Output:
# HTTP Status: 201 Created
# {
#   "id": 4,
#   "name": "Nisha Rao",
#   "email": "nisha@ust.com",
#   "department": "Engineering",
#   "role": "QA",
#   "status": "active"
# }

# # Test 2: Create Employee (Email Already Exists)
# ## Input:
# POST /employees
# {
#   "name": "John Doe",
#   "email": "asha.rao@ust.com",
#   "department": "Sales",
#   "role": "Manager"
# }

# ## Output:
# HTTP Status: 409 Conflict
# {
#   "detail": "Employee already exists"
# }

# # Test 3: List Employees
# ## Input:
# GET /employees

# ## Output:
# HTTP Status: 200 OK
# [
#   {
#     "id": 1,
#     "name": "Asha Rao",
#     "email": "asha.rao@ust.com",
#     "department": "Engineering",
#     "role": "Engineer",
#     "status": "active"
#   },
#   {
#     "id": 2,
#     "name": "Vikram S",
#     "email": "vikram.s@ust.com",
#     "department": "Delivery",
#     "role": "Manager",
#     "status": "active"
#   },
#   {
#     "id": 3,
#     "name": "Meera N",
#     "email": "meera.n@ust.com",
#     "department": "HR",
#     "role": "HR",
#     "status": "active"
#   }
# ]

# # Test 4: Get Employee by ID
# ## Input:
# GET /employees/1

# ## Output:
# HTTP Status: 200 OK
# {
#   "id": 1,
#   "name": "Asha Rao",
#   "email": "asha.rao@ust.com",
#   "department": "Engineering",
#   "role": "Engineer",
#   "status": "active"
# }

# # Test 5: Update Employee (Email Conflict)
# ## Input:
# PUT /employees/1
# {
#   "name": "Asha Rao",
#   "email": "vikram.s@ust.com",
#   "department": "Engineering",
#   "role": "Sr Engineer",
#   "status": "active"
# }

# ## Output:
# HTTP Status: 409 Conflict
# {
#   "detail": "Email already exists"
# }

# # Test 6: Delete Employee (Success)
# ## Input:
# DELETE /employees/3

# ## Output:
# HTTP Status: 200 OK
# {
#   "detail": "Employee deleted successfully"
# }

# # Test 7: Check-in Employee
# ## Input:
# POST /employees/1/check_in
# {
#   "date": "2025-11-21",
#   "check_in": "09:10:00"
# }

# ## Output:
# HTTP Status: 201 Created
# {
#   "employee_id": 1,
#   "date": "2025-11-21",
#   "check_in": "09:10:00",
#   "check_out": null
# }

# # Test 8: Check-out Employee
# ## Input:
# POST /employees/1/checkout
# {
#   "date": "2025-11-21",
#   "check_out": "18:00:00"
# }

# ## Output:
# HTTP Status: 200 OK
# {
#   "employee_id": 1,
#   "date": "2025-11-21",
#   "check_in": "09:10:00",
#   "check_out": "18:00:00"
# }

# # Test 9: Create Leave Request
# ## Input:
# POST /employees/1/leave-requests
# {
#   "from_date": "2025-12-24",
#   "to_date": "2025-12-25",
#   "reason": "family"
# }

# ## Output:
# HTTP Status: 201 Created
# {
#   "leave_id": 1,
#   "employee_id": 1,
#   "from_date": "2025-12-24",
#   "to_date": "2025-12-25",
#   "reason": "family",
#   "status": "pending"
# }

# # Test 10: List Leave Requests for Employee
# ## Input:
# GET /employees/1/leave-requests

# ## Output:
# HTTP Status: 200 OK
# [
#   {
#     "leave_id": 1,
#     "employee_id": 1,
#     "from_date": "2025-12-24",
#     "to_date": "2025-12-25",
#     "reason": "family",
#     "status": "pending"
#   }
# ]


