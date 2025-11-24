from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date, datetime

# Initialize the FastAPI app
app = FastAPI(title="Employee Management System")

# In-memory storage for employee data, attendance records, and leave requests
leave_list = []
attendence_list = []

emp_id = int(3)  # Starting employee ID
leave_id = 0  # Starting leave ID

# Pydantic model for Employee details
class Employee(BaseModel):
    id: int = emp_id + 1  # Default starting employee ID
    name: str
    email: str
    department: str
    role: str
    status: str = "active"  # Default status for employee

# Pydantic model for Attendance Record
class AttendanceRecord(BaseModel):
    employee_id: int
    date: str
    check_in: str
    check_out: str

# Pydantic model for Leave Request
class LeaveRequest(BaseModel):
    leave_id: int = leave_id + 1  # Default leave ID
    employee_id: int
    from_date: str
    to_date: str
    reason: str
    status: str = "pending"  # Default status for leave request

# Sample data for employees
employee_list = [
    { "id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department": "Engineering", "role": "Engineer", "status": "active" },
    { "id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department": "Delivery", "role": "Manager", "status": "active" },
    { "id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department": "HR", "role": "HR", "status": "active" }
]

# POST request to create a new employee
@app.post("/employee")
def create_employee(emp: Employee):
    # Check if email already exists
    if any(existing_emp["email"] == emp.email for existing_emp in employee_list):
        raise HTTPException(status_code=409, detail="The email already exists")
    employee_list.append(emp)
    return {"Employee Created": emp}

# GET request to display all employees
@app.get("/employee")
def show_employee():
    return {"All employees": employee_list}

# GET request to get an employee by their ID
@app.get("/employee/{id}")
def get_emp_with_id(id: int):
    for emp in employee_list:
        if emp["id"] == id:
            return {"id": emp}
    raise HTTPException(status_code=404, detail="Employee not found")

# PUT request to update an employee's details
@app.put("/employee/{id}")
def update_employee(id: int, emp: Employee):
    for dic in employee_list:
        if dic["id"] == id:
            dic["name"] = emp.name
            dic["email"] = emp.email
            dic["department"] = emp.department
            dic["role"] = emp.role
            dic["status"] = emp.status
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

# DELETE request to remove an employee by their ID
@app.delete("/employee/{id}")
def delete_employee(id: int):
    index_count = -1
    for e in employee_list:
        index_count += 1
        if e["id"] == id:
            removed_emp = employee_list.pop(index_count)
            return removed_emp
    raise HTTPException(status_code=404, detail="Employee not found")

# POST request for employee check-in
@app.post("/employee/check-in/{id}")
def emp_check_in(id: int):
    # Check if employee exists
    for emp in employee_list:
        if id == emp["id"]:
            # Check if the employee has already checked in
            for atten in attendence_list:
                if atten["employee_id"] == id and atten["check_out"] == "null":
                    return {"detail": "Already checked-in"}, 409
            
            # Record current time and date for check-in
            current_time = datetime.now().time()
            formatted_time = current_time.strftime("%H:%M:%S")
            current_date = date.today()
            formatted_date = current_date.strftime("%d-%m-%Y")
            
            # Create attendance record for the employee
            atten_dict = {
                "employee_id": id,
                "date": formatted_date,
                "check_in": formatted_time,
                "check_out": "null"
            }
            attendence_list.append(atten_dict)
            return atten_dict  # Return the check-in record

    raise HTTPException(status_code=404, detail="Employee not found")  # Employee not found

# POST request for employee check-out
@app.post("/employee/check-out/{id}")
def emp_check_out(id: int):
    # Check if employee exists
    for emp in employee_list:
        if id == emp["id"]:
            for attendence in attendence_list:
                # If employee has checked in, update check-out time
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

# POST request to create a leave request for an employee
@app.post("/employee/{id}/leave-requests")
def leave_request(id: int, leave: LeaveRequest):
    # Validate that the 'from_date' is not later than the 'to_date'
    if leave.from_date > leave.to_date:
        raise HTTPException(status_code=400, detail="from_date must be on or before to_date")
    
    leave.employee_id = id  # Associate the leave request with the employee's ID
    leave_list.append(leave)
    return leave

# GET request to list leave requests for an employee
@app.get("/employee/{id}/leave-requests")
def display_leave_list(id: int):
    employee_leaves = []
    for detail in leave_list:
        if detail.employee_id == id:
            employee_leaves.append(detail)
    
    if not employee_leaves:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return employee_leaves  # Return a list of leave requests for the employee
