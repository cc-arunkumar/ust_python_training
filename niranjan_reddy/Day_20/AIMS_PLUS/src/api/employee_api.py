from fastapi import Depends, HTTPException, status, APIRouter
from typing import List, Optional
from src.auth.jwt_auth import User, get_curr_user
from src.models.employee_model import EmployeeDirectory
from src.crud.employee_crud import get_all, get_by_id, insert_emp, update_emp_by_id, delete_emp, search_emp

# Initialize the employee_router with a prefix "/employees"
employee_router = APIRouter(prefix="/employees")

# GET endpoint to fetch a list of employees with an optional status filter
@employee_router.get("/list", response_model=List[EmployeeDirectory])
def get_emp(status_filter: Optional[str] = "",current_user: User = Depends(get_curr_user)):
    try:
        # Fetch all employees or filter by status if provided
        rows = get_all(status_filter)
        emp_li = []
        for row in rows:
            # Create EmployeeDirectory objects from the rows returned by the database
            emp_li.append(EmployeeDirectory(**row))
        return emp_li  # Return the list of employees
    except Exception as e:
        # If an error occurs, raise an HTTP exception with a 400 Bad Request status
        raise HTTPException(status_code=400, detail=f"{e}")

# GET endpoint to search for employees based on a specific field and keyword
@employee_router.get("/search")
def search_by_word(field_type: str, keyword: str,current_user: User = Depends(get_curr_user)):
    try:
        # Call the search function from CRUD operations
        data = search_emp(field_type, keyword)
        return data  # Return the search results
    except Exception as e:
        # If an error occurs, raise an HTTP exception with a 400 Bad Request status
        raise HTTPException(status_code=400, detail=f"Unable to fetch data: {e}")

# GET endpoint to count the total number of employees
@employee_router.get("/count")
def count_data(current_user: User = Depends(get_curr_user)):
    try:
        # Fetch all employees to count them
        data = get_all()
        if data is None:
            # Raise a 404 Not Found error if no employees are found
            raise HTTPException(status_code=404, detail="No employee found.")
        return {"count": len(data)}  # Return the count of employees
    except Exception as e:
        # If an error occurs, raise an HTTP exception with a 500 Internal Server Error status
        raise HTTPException(status_code=500, detail=f"Error counting employees: {str(e)}")

# GET endpoint to fetch an employee by its ID
@employee_router.get("/{emp_id}", response_model=EmployeeDirectory)
def get_emp_by_id(emp_id: int,current_user: User = Depends(get_curr_user)):
    try:
        # Fetch the employee by ID from the database
        rows = get_by_id(emp_id)
        if not rows:
            # If no employee is found, raise a 404 Not Found error
            raise HTTPException(status_code=404, detail="Employee not exists")
        return EmployeeDirectory(**rows)  # Return the employee data
    except Exception as e:
        # If there is an error, raise a 400 Bad Request error
        raise HTTPException(status_code=400, detail="ID not found")

# POST endpoint to create a new employee
@employee_router.post('/create', response_model=EmployeeDirectory)
def create_asset(new_emp: EmployeeDirectory,current_user: User = Depends(get_curr_user)):
    try:
        existing_id=get_by_id(new_emp.emp_id)
        if existing_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User already Exists")
        
        # Insert the new employee into the database
        insert_emp(new_emp)
        return new_emp  # Return the created employee
    except Exception as e:
        # If there is an error, raise an HTTP exception with a 404 Not Found status
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")

# PUT endpoint to update an employee's details by employee ID
@employee_router.put("/{emp_id}", response_model=EmployeeDirectory)
def update_details(emp_id: int, update_emp: EmployeeDirectory,current_user: User = Depends(get_curr_user)):
    try:
        # Update the employee details by its ID
        update_emp_by_id(emp_id, update_emp)
        return update_emp  # Return the updated employee data
    except HTTPException as e:
        # If the update failed, raise the HTTPException raised in the CRUD operation
        raise e  
    except Exception as e:
        # If any other error occurs, raise a 400 Bad Request error
        raise HTTPException(status_code=400, detail=f"Update failed: {str(e)}")

# DELETE endpoint to delete an employee by its ID
@employee_router.delete("/{emp_id}")
def delete_asset_by_id(emp_id: int,current_user: User = Depends(get_curr_user)):
    try:
        # Attempt to delete the employee by its ID
        if delete_emp(emp_id):
            return {"detail": "Employee deleted successfully"}  # Return success message
    except Exception as e:
        # If there is an error, raise an HTTP exception with a 400 Bad Request status
        raise HTTPException(status_code=400, detail=f"Error deleting asset: {str(e)}")

# PATCH endpoint to update the status of an employee by its ID
@employee_router.patch("/{emp_id}/status")
def update_vendor_status(emp_id: int, status: str,current_user: User = Depends(get_curr_user)):
    try:
        # Fetch the employee by its ID
        data = get_by_id(emp_id)
        
        if not data:
            # If the employee is not found, raise a 404 Not Found error
            raise HTTPException(status_code=404, detail="Employee not found")
        
        # Update the active_status field of the employee
        data['active_status'] = status
        
        # Call the update function to apply the status change
        update_emp_by_id(emp_id, EmployeeDirectory(**data))
        
        return {"message": "Employee status updated successfully", "emp_id": emp_id, "new_status": status}
    except Exception as e:
        # If there is an error updating the status, raise a 400 Bad Request error
        raise HTTPException(status_code=400, detail=f"Error updating employee status: {str(e)}")
