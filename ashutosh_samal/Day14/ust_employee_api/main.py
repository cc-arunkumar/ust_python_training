from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date,time

app = FastAPI(title="UST Employee")

# Define the Employee model using Pydantic
class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    status: str = "Active"

# Define the AttendanceRecord model using Pydantic
class AttendanceRecord(BaseModel):
    employee_id: int
    date: date
    check_in: str | None = None
    check_out: str | None = None

# Define the LeaveRequest model using Pydantic
class LeaveRequest(BaseModel):
    leave_id: int
    employee_id: int
    from_date: date
    to_date: date
    reason: str
    status: str = "pending"
    
employees: List[Employee] = [
 { "id": 1, "name": "Asha Rao", "email": "asha.rao@ust.com", "department":
"Engineering", "role": "Engineer", "status": "active" },
 { "id": 2, "name": "Vikram S", "email": "vikram.s@ust.com", "department":
"Delivery", "role": "Manager", "status": "active" },
 { "id": 3, "name": "Meera N", "email": "meera.n@ust.com", "department":
"HR", "role": "HR", "status": "active" }
]
attendance: List[AttendanceRecord] = []
leaves: List[LeaveRequest] = []

next_emp_id = 4

@app.post("/Employee")
def create_Employee(emp: Employee):
    global next_emp_id
    # Create a new employee and add to the employee list
    # Check if the email already exists to avoid duplicates
    for i in employees:
        if i["email"] == emp.email:
            raise HTTPException(status_code=409, detail="Email already exists")
    emp.id = next_emp_id
    next_emp_id += 1
    employees.append(emp.model_dump())  # Add the new employee to the list
    return {"Employee Created": emp}


@app.get("/Employee", response_model=List[Employee])
def get_employee(department: str | None = None):
    # Get the list of employees, optionally filter by department
    if department:
        return [emp for emp in employees if emp['department'] == department]
    return employees


@app.get("/Employee/{id}", response_model=Employee)
def get_employee(id: int):
    # Get a specific employee by ID
    try:
        for emp in employees:
            if emp['id'] == id:
                return emp
    except IndexError:
        raise HTTPException(status_code=404, detail="Employee not found")


@app.put("/employee/{id}")
def update(id: int, emp: Employee):
    # Update an existing employee's information
    for e in employees:
        if e["id"] == id:
            # Ensure the new email does not already exist
            for other in employees:
                if other["email"] == emp.email:
                    raise HTTPException(status_code=409, detail="Email already exists")
            e.update({
                "name": emp.name,
                "email": emp.email,
                "department": emp.department,
                "role": emp.role,
                "status": emp.status
            })
            return e
    raise HTTPException(status_code=404, detail="Employee not found")


@app.delete("/Employee/{id}")
def delete_employee(id: int):
    # Delete an employee by ID
    for emp in employees:
        if emp['id'] == id:
            employees.remove(emp)
            return {"detail": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")


@app.post("/Employee/{id}/checkin")
def emp_checkin(id: int, attendance_data: AttendanceRecord):
    # Check in an employee for a specific date
    for emp in employees:
        if emp['id'] == id:
            # Check if the employee has already checked in on the given date
            for record in attendance:
                if record["employee_id"] == id and record['date'] == attendance_data.date:
                    raise HTTPException(status_code=409, detail="Already checked in")
            attendance.append(attendance_data.model_dump())  # Add the check-in record
            return attendance_data
    raise HTTPException(status_code=404, detail="Employee not found")


@app.post("/employee/{id}/checkout")
def check_out(id: int, data: dict):
    # Check out an employee for a specific date
    for e in employees:
        if e["id"] == id:
            for r in attendance:
                if r["employee_id"] == id and r["date"] == data["date"]:
                    # Check if the employee has checked in before checking out
                    if not r["check_in"]:
                        raise HTTPException(status_code=404, detail="First check-in is required")
                    # Ensure the employee is not already checked out
                    if r["check_out"]:
                        raise HTTPException(status_code=409, detail="Already checked out")
                    r["check_out"] = data["time"]  # Record the check-out time
                    return r
    raise HTTPException(status_code=404, detail="Employee not found")


@app.post("/employees/{id}/leave-requests")
def create_leave(id: int, data: dict):
    global next_leave_id
    # Create a leave request for an employee
    for e in employees:
        if e["id"] == id:
            # Validate the leave date range
            if data["from_date"] > data["to_date"]:
                raise HTTPException(status_code=400, detail="from_date must be on or before to_date")
            
            # Create and store the leave request
            leave = {
                "leave_id": next_leave_id,
                "employee_id": id,
                "from_date": data["from_date"],
                "to_date": data["to_date"],
                "reason": data["reason"],
                "status": "pending"
            }
            leaves.append(leave)
            next_leave_id += 1
            return leave

    raise HTTPException(status_code=404, detail="Employee not found")


@app.get("/employees/{id}/leave-requests")
def list_leaves(id: int):
    # List all leave requests for a specific employee
    for e in employees:
        if e["id"] == id:
            result = []
            for l in leaves:
                if l["employee_id"] == id:
                    result.append(l)
            return result
    raise HTTPException(status_code=404, detail="Employee not found")
