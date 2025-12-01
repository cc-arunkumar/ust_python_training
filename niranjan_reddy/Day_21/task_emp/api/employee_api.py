from typing import List  # Importing List from typing to define response type as a list
from fastapi import FastAPI, HTTPException  # Importing FastAPI for the web framework and HTTPException for error handling
from models.employee_model import EmployeeModel, EmployeeRequest  # Importing Pydantic models for employee data validation
from crud.emp_crud import get_all, get_by_id, insert_to_db, update_db, delete  # Importing CRUD operations for employee data

app = FastAPI(title="Employee Management System")  # Initializing the FastAPI app with a title

# Route to get the list of all employees
@app.get("/employees/", response_model=List[EmployeeModel])  # Defining the route and response model
def get_lists():
    rows = get_all()  # Fetching all employee records from the database
    return [EmployeeModel(**row) for row in rows]  # Returning the data as a list of EmployeeModel instances

# Route to get a specific employee by employee_id
@app.get("/employees/{employee_id}", response_model=EmployeeModel)  # Defining the route with employee_id in the URL path
def get_by_emp_id(employee_id: int):
    row = get_by_id(employee_id)  # Fetching the employee record by employee_id
    if not row:  # If the employee does not exist, raise an HTTP 404 error
        raise HTTPException(status_code=404, detail="Employee not found")

    return EmployeeModel(**row)  # Returning the employee data as an EmployeeModel instance

# Route to insert a new employee record
@app.post("/employees/", response_model=EmployeeModel)  # Defining the route for POST requests to insert data
def insert_data(new_data: EmployeeRequest):
    created = insert_to_db(new_data)  # Inserting the new employee data into the database
    if not created:  # If insertion fails, raise an HTTP 400 error
        raise HTTPException(status_code=400, detail="Unable to insert employee")

    return EmployeeModel(**created)  # Returning the newly created employee data as an EmployeeModel instance

# Route to update an existing employee record
@app.put("/employees/{employee_id}", response_model=dict)  # Defining the route for PUT requests to update data
def update_employee(employee_id: int, updated_data: EmployeeRequest):
    if not get_by_id(employee_id):  # Check if the employee exists before updating
        raise HTTPException(status_code=404, detail="Employee not found")  # Raise 404 if employee not found

    update_db(employee_id, updated_data)  # Updating the employee data in the database
    return {"message": "Employee updated successfully", "employee_id": employee_id}  # Return success message

# Route to delete an employee record
@app.delete("/employees/{employee_id}", response_model=dict)  # Defining the route for DELETE requests
def delete_employee(employee_id: int):
    if not delete(employee_id):  # Check if the employee exists before attempting to delete
        raise HTTPException(status_code=404, detail="Employee not found")  # Raise 404 if employee not found

    return {"message": "Employee deleted successfully", "employee_id": employee_id}  # Return success message after deletion
