from fastapi import APIRouter, HTTPException,Depends
from typing import List, Optional  
from models import EmployeeTraining
from auth import jwt_router,get_current_user,User
from crud import(
    fetch_all_employee,
    fetch_employee_by_id,
    create_new_emp_training,
    update_emp_training,
    update_emp_status,
    remove_emp_training
)

emp_router = APIRouter(prefix="/EmployeeTraining")

# Endpoint to get all employees
@emp_router.get("/")
def get_employees(current_user: User = Depends(get_current_user)):
    try:
        emp = fetch_all_employee()
        return emp
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to get employee by id
@emp_router.get("/{id}")
def get_emp_by_id(id: int,current_user: User = Depends(get_current_user)):
    try:
        employee = fetch_employee_by_id(id)  # Fetch employee by ID
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")  # Return error if not found
        return employee
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure


# Endpoint to create a new employee
@emp_router.post("/create")
def create_employee_endpoint(employee: EmployeeTraining,current_user: User = Depends(get_current_user)):
    try:
        create_new_emp_training(employee)  # Call CRUD function to create employee
        return employee  # Return created employee
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure
    

# Endpoint to update an existing employee by ID
@emp_router.put("/{id}")
async def update_employee_endpoint(id: int, emp :EmployeeTraining,current_user: User = Depends(get_current_user)):
    try:
        update_emp_training(id, emp)  # Update employee using the provided ID and data
        return emp  # Return updated employee
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Endpoint to delete an employee by ID
@emp_router.delete("/{id}")
async def delete_employee_endpoint(id: int,current_user: User = Depends(get_current_user)):
    try:
        remove_emp_training(id)  # Delete employee using the provided ID
        return {"message": "Employee deleted successfully"}  # Return success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to update the status of an employee
@emp_router.patch("/{id}/status")
async def update_employee_status_endpoint(id: int, status: str,current_user: User = Depends(get_current_user)):
    try:
        update_emp_status(id, status)  # Update employee status
        return {"message": "Employee status updated successfully"}  # Return success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
