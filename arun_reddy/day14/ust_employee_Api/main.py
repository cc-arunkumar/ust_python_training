"""
UST Employee Management API
This API manages employee data, attendance records, and leave requests.
Provides endpoints for CRUD operations on employees, attendance tracking, and leave management.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime, date, time

# Initialize FastAPI application
app = FastAPI(title="UST Employee API")

# ========== GLOBAL COUNTERS ==========
# These counters auto-increment to assign unique IDs when new records are created

# next_emp_id: Tracks the next employee ID to assign (starts at 4, since IDs 1-3 are pre-existing)
next_emp_id = 4

# next_leave_id: Tracks the next leave request ID to assign
next_leave_id = 1

# ========== PYDANTIC MODELS (Data Validation) ==========
# These models define the structure of our API request/response data

class Employee(BaseModel):
    """Employee data model - represents an employee in the system"""
    id: int  # Unique employee identifier
    name: str  # Employee's full name
    email: str  # Employee's email (must be unique)
    department: str  # Department name (e.g., Engineering, HR)
    role: str  # Job role/position
    status: str = "active"  # Employment status: 'active' or 'inactive' (defaults to 'active')


class Attendance(BaseModel):
    """Attendance tracking model - records daily check-in and check-out times"""
    employee_id: int  # ID of the employee
    date: date  # Date of the attendance record
    check_in: time | None = None  # Time when employee checked in (None if not checked in)
    check_out: time | None = None  # Time when employee checked out (None if not checked out)


class Leave(BaseModel):
    """Leave request model - represents a leave application"""
    leave_id: int  # Unique leave request identifier
    employee_id: int  # ID of the employee requesting leave
    from_date: date  # Start date of leave
    to_date: date  # End date of leave
    reason: str  # Reason for taking leave
    status: str = "pending"  # Leave status: 'pending', 'approved', or 'rejected' (defaults to 'pending')


# ========== IN-MEMORY DATA STORAGE ==========
# In production, this would be replaced with a database

# emp_data: List of all employee records
emp_data: List[Employee] = [
    Employee(id=1, name="Asha Rao", email="asha.rao@ust.com",
             department="Engineering", role="Engineer", status="active"),
    Employee(id=2, name="Vikram S", email="vikram.s@ust.com",
             department="Delivery", role="Manager", status="active"),
    Employee(id=3, name="Meera N", email="meera.n@ust.com",
             department="HR", role="HR", status="active")
]

# attendance_records: List of all attendance check-in/check-out records
attendance_records: List[Attendance] = []

# leave_records: List of all leave requests
leave_records: List[Leave] = []

# ========== EMPLOYEE ENDPOINTS (CREATE, READ, UPDATE, DELETE Operations) =========

@app.post("/employees", response_model=Employee, status_code=201)
def add_employee(emp: Employee):
    """
    CREATE: Add a new employee to the system
    
    Process:
    1. Validates that the email doesn't already exist (ensures uniqueness)
    2. Auto-assigns the next available ID from next_emp_id counter
    3. Increments the counter for the next new employee
    4. Adds the employee to the emp_data list
    5. Returns the newly created employee with assigned ID
    
    Request: Employee object without ID (will be auto-assigned)
    Response: Created employee with assigned ID (201 Created)
    Raises: 409 Conflict if email already exists
    """
    global next_emp_id
    
    # Check if email already exists - prevent duplicate emails
    for e in emp_data:
        if e.email == emp.email:
            raise HTTPException(status_code=409, detail="Email already exists")
    
    # Assign auto-incremented ID to the new employee
    emp.id = next_emp_id
    # Increment counter for next employee
    next_emp_id += 1
    
    # Add employee to the list
    emp_data.append(emp)
    return emp


@app.get("/employees", response_model=List[Employee])
def get_all_employees(department: str | None = None):
    """
    READ: Get all employees, optionally filtered by department
    
    Parameters:
    - department (optional): Filter results by department name
    
    Returns:
    - If department provided: List of employees in that department
    - If no department: All employees in the system
    """
    if department:
        # Filter employees by department
        return [e for e in emp_data if e.department == department]
    # Return all employees
    return emp_data


@app.get("/employees/{emp_id}", response_model=Employee)
def get_employee(emp_id: int):
    """
    READ: Get a specific employee by their ID
    
    Parameters:
    - emp_id: The unique employee ID to search for
    
    Returns: Employee object if found
    Raises: 404 Not Found if employee with that ID doesn't exist
    """
    # Search for employee by ID
    for e in emp_data:
        if e.id == emp_id:
            return e
    # Employee not found
    raise HTTPException(status_code=404, detail="Employee not found")


@app.put("/employees/{emp_id}", response_model=Employee)
def modify_employee(emp_id: int, emp: Employee):
    """
    UPDATE: Modify an existing employee's details
    
    Important: The employee ID cannot be changed by the user - it will be preserved from the original record.
    
    Process:
    1. Validates that the new email doesn't conflict with other employees
    2. Finds the employee with the given ID
    3. Replaces their data with updated data
    4. Forces the ID to remain unchanged (security feature)
    5. Returns the updated employee
    
    Parameters:
    - emp_id: ID of the employee to update
    - emp: Updated employee data (ID field will be ignored and overwritten)
    
    Returns: Updated employee with original ID preserved
    Raises: 
    - 404 Not Found if employee doesn't exist
    - 409 Conflict if new email already exists for another employee
    """
    # Check if new email conflicts with another employee (but allow same email for this employee)
    for e in emp_data:
        if e.email == emp.email and e.id != emp_id:
            raise HTTPException(status_code=409, detail="Email already exists")
    
    # Find and update the employee
    for i in range(len(emp_data)):
        if emp_data[i].id == emp_id:
            # Force the ID to remain unchanged (user-provided ID is ignored)
            emp.id = emp_id
            # Replace the entire employee record
            emp_data[i] = emp
            return emp
    
    # Employee not found
    raise HTTPException(status_code=404, detail="Employee not found")


@app.delete("/employees/{emp_id}")
def remove_employee(emp_id: int):
    """
    DELETE: Remove an employee from the system
    
    Parameters:
    - emp_id: ID of the employee to delete
    
    Returns: Confirmation message if deletion successful
    Raises: 404 Not Found if employee doesn't exist
    """
    # Find and delete the employee by ID
    for i in range(len(emp_data)):
        if emp_data[i].id == emp_id:
            emp_data.pop(i)
            return {"detail": "Employee deleted"}
    # Employee not found
    raise HTTPException(status_code=404, detail="Employee not found")


# ========== ATTENDANCE ENDPOINTS (Daily Check-in/Check-out) =========


@app.post("/employees/{emp_id}/checkin", response_model=Attendance, status_code=201)
def checkin(emp_id: int):
    """
    ATTENDANCE: Record employee check-in for today
    
    Process:
    1. Gets today's date and current time
    2. Checks if employee already checked in today (prevents duplicate check-ins)
    3. Creates a new attendance record with check-in time
    4. Adds record to attendance_records
    5. Returns the attendance record
    
    Parameters:
    - emp_id: ID of the employee checking in
    
    Returns: Attendance record with check-in time (201 Created)
    Raises: 409 Conflict if employee already checked in today
    """
    today = date.today()
    now = datetime.now().time()
    
    # Check if already checked in today - prevent duplicate check-ins
    for rec in attendance_records:
        if rec.employee_id == emp_id and rec.date == today and rec.check_in is not None:
            raise HTTPException(status_code=409, detail="Already checked in")
    
    # Create new attendance record with check-in time
    new_rec = Attendance(employee_id=emp_id, date=today, check_in=now)
    attendance_records.append(new_rec)
    return new_rec


@app.post("/employees/{emp_id}/checkout", response_model=Attendance)
def checkout(emp_id: int):
    """
    ATTENDANCE: Record employee check-out for today
    
    Process:
    1. Gets today's date and current time
    2. Finds today's attendance record for the employee
    3. Validates that check-in exists before allowing check-out
    4. Prevents duplicate check-outs (only one checkout allowed per day)
    5. Records the check-out time
    6. Returns the updated attendance record
    
    Parameters:
    - emp_id: ID of the employee checking out
    
    Returns: Attendance record with check-out time
    Raises:
    - 404 Not Found if no attendance record exists for today
    - 400 Bad Request if employee hasn't checked in yet
    - 409 Conflict if employee already checked out today
    """
    today = date.today()
    now = datetime.now().time()
    
    # Find today's attendance record for this employee
    for rec in attendance_records:
        if rec.employee_id == emp_id and rec.date == today:
            # Validate check-in exists before allowing check-out
            if rec.check_in is None:
                raise HTTPException(status_code=400, detail="Check-in required before checkout")
            # Prevent duplicate check-outs
            if rec.check_out is not None:
                raise HTTPException(status_code=409, detail="Already checked out")
            # Record check-out time
            rec.check_out = now
            return rec
    
    # No attendance record found for today
    raise HTTPException(status_code=404, detail="Attendance record not found")


# ========== LEAVE ENDPOINTS (Leave Request Management) =========


@app.post("/employees/{emp_id}/leave-requests", response_model=Leave, status_code=201)
def request_leave(emp_id: int, from_date: date, to_date: date, reason: str):
    """
    LEAVE: Submit a new leave request
    
    Process:
    1. Validates that from_date is not after to_date (date range validation)
    2. Creates a new leave request with auto-incremented leave_id
    3. Sets initial status to 'pending' (waiting for approval)
    4. Increments the leave ID counter for next request
    5. Returns the created leave request
    
    Parameters:
    - emp_id: ID of the employee requesting leave
    - from_date: Start date of leave
    - to_date: End date of leave
    - reason: Reason for taking leave
    
    Returns: Leave request object with assigned ID (201 Created)
    Raises: 400 Bad Request if from_date is after to_date
    """
    global next_leave_id
    
    # Validate date range - from_date must be on or before to_date
    if from_date > to_date:
        raise HTTPException(status_code=400, detail="from_date must be on or before to_date")
    
    # Create new leave request with auto-incremented ID
    new_leave = Leave(
        leave_id=next_leave_id,
        employee_id=emp_id,
        from_date=from_date,
        to_date=to_date,
        reason=reason,
        status="pending"  # Initially pending approval
    )
    leave_records.append(new_leave)
    # Increment counter for next leave request
    next_leave_id += 1
    return new_leave


@app.get("/employees/{emp_id}/leave-requests", response_model=List[Leave])
def list_leaves(emp_id: int):
    """
    LEAVE: Get all leave requests for a specific employee
    
    Parameters:
    - emp_id: ID of the employee
    
    Returns: List of all leave requests submitted by this employee
    Raises: 404 Not Found if employee has no leave requests
    """
    # Filter leave requests for this specific employee
    result = [lr for lr in leave_records if lr.employee_id == emp_id]
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result
