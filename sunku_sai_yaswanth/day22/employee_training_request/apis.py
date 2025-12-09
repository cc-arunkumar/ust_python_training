from fastapi import FastAPI, HTTPException, APIRouter, status
from typing import List, Optional
from validations import EmployeeValidations
from datetime import datetime
from crud import insert_employee, get_by_id, get_all_employees, update_employee_by_id, delete_emp
from auth_jwt import User,get_current_user,Depends

employee_router = APIRouter(prefix="/employee")

# Create a new employee
@employee_router.post("/create", response_model=EmployeeValidations, status_code=status.HTTP_201_CREATED)
def create_employee(new_employee: EmployeeValidations,current_user: User = Depends(get_current_user)):
    try:
        data = insert_employee(new_employee)
        return new_employee  # Return the created employee details
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")

# Get all employees
@employee_router.get("/", response_model=List[EmployeeValidations])
def get_all_requests(current_user: User = Depends(get_current_user)):
    try:
        requests = get_all_employees()
        if not requests:
            return []  # Return an empty list if no records are found
        return [EmployeeValidations(**request) for request in requests]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")

# Get a single employee by ID
@employee_router.get("/{id}", response_model=EmployeeValidations)
def get_request_by_id(id: int,current_user: User = Depends(get_current_user)):
    try:
        request = get_by_id(id)
        if not request:
            raise HTTPException(status_code=404, detail=f"Training Request with ID {id} not found")
        return EmployeeValidations(**request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")

# Update an existing employee by ID
@employee_router.put("/{id}", response_model=EmployeeValidations)
def update_request(id: int, updated_request: EmployeeValidations,current_user: User = Depends(get_current_user)):
    try:
        updated_request_dict = updated_request.dict()  # Use .dict() instead of model_dump()

        # Set the last_updated field before updating
        updated_request_dict["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Update the employee record in the database
        update_employee_by_id(id, updated_request_dict)
        return EmployeeValidations(**updated_request_dict)  # Return the updated employee

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")

# Delete an employee by ID
@employee_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_request(id: int,current_user: User = Depends(get_current_user)):
    try:
        # Attempt to delete the request from the database
        delete_emp(id)

        # Return a success message with status code 204 (No Content)
        return {"detail": f"Training Request with ID {id} has been deleted successfully."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
