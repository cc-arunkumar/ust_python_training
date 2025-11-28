from fastapi import Depends, HTTPException
from typing import List
from src.models.employee_model import EmployeeDirectory
from src.crud.employee_crud import (
    create_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee_by_id,
    update_employee_status,
    delete_employee,
    search_employees,
    count_employee,
    
)
from src.auth.jwt_auth import get_current_user, User

def register_employee_api(app):
    """
    Register all employee-related API endpoints with the FastAPI app.
    Each endpoint interacts with the CRUD functions defined in employee_crud.
    """

    # 1. Create a new employee
    @app.post("/employees/create")
    def add_employee(emp: EmployeeDirectory,current_user: User = Depends(get_current_user)):
        """
        Endpoint: POST /employees/create
        Input: EmployeeDirectory object (validated by Pydantic model)
        Action: Calls create_employee() to insert a new employee into DB
        Returns: Created employee record
        """
        try:
            return create_employee(emp)
        except Exception as e:
            print(f"Error in create_employee: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")

    # 2. List all employees (optionally filter by status)
    @app.get("/employees/list")
    def list_employees(status: str | None = None,current_user: User = Depends(get_current_user)):
        """
        Endpoint: GET /employees/list
        Query param: status (optional)
        Action: Fetch all employees, optionally filtered by status
        Returns: List of employees
        """
        return get_all_employees(status)

    # 3. Count total employees
    @app.get("/employees/count")
    def count(current_user: User = Depends(get_current_user)):
        """
        Endpoint: GET /employees/count
        Action: Returns total count of employees
        """
        return count_employee()

    # 4. Search employees by column and keyword
    @app.get("/employees/search")
    def search(column_name: str, keyword: str,current_user: User = Depends(get_current_user)):
        """
        Endpoint: GET /employees/search
        Query params: column_name, keyword
        Action: Search employees based on column and keyword
        Returns: Matching employees
        """
        return search_employees(column_name, keyword)

    # 5. Get employee by ID
    @app.get("/employees/{id}")
    def read_employee(id: int,current_user: User = Depends(get_current_user)):
        """
        Endpoint: GET /employees/{id}
        Path param: id
        Action: Fetch employee by ID
        Returns: Employee record or 404 if not found
        """
        result = get_employee_by_id(id)
        if not result:
            raise HTTPException(status_code=404, detail="Employee not found")
        return result

    # 6. Update full employee record
    @app.put("/employees/{id}")
    def update_employee(id: int, emp: EmployeeDirectory,current_user: User = Depends(get_current_user)):
        """
        Endpoint: PUT /employees/{id}
        Path param: id
        Body: EmployeeDirectory object
        Action: Replace employee record with new data
        Returns: Updated employee or 404 if not found
        """
        result = update_employee_by_id(id, emp)
        if not result:
            raise HTTPException(status_code=404, detail="Employee not found")
        return result

    # 7. Update only employee status
    @app.patch("/employees/{id}/status")
    def update_status(id: int, new_status: str,current_user: User = Depends(get_current_user)):
        """
        Endpoint: PATCH /employees/{id}/status
        Path param: id
        Body: new_status string
        Action: Update only the status field of an employee
        Returns: Updated employee or 404 if not found
        """
        result = update_employee_status(id, new_status)
        if not result:
            raise HTTPException(status_code=404, detail="Employee not found")
        return result

    # 8. Delete employee
    @app.delete("/employees/{id}")
    def remove_employee(id: int,current_user: User = Depends(get_current_user)):
        """
        Endpoint: DELETE /employees/{id}
        Path param: id
        Action: Delete employee by ID
        Returns: Deleted employee or 404 if not found
        """
        result = delete_employee(id)
        if not result:
            raise HTTPException(status_code=404, detail="Employee not found")
        return result

