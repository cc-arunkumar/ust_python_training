# Import FastAPI framework and HTTPException for building APIs and handling errors
from fastapi import FastAPI, HTTPException
# Import the Employee Pydantic model for request validation and response serialization
from employee_model import Employee
# Import CRUD operations for employee management
import employee_crud

# Initialize FastAPI application with a custom title
app = FastAPI(title="Employee Management System")

# -------------------------------
# GET endpoint: Fetch employee by ID
# -------------------------------
@app.get("/employees/{employee_id}", response_model=Employee)
def get_employee_by_id(employee_id: int):
    # """
    # Retrieve a single employee record by its ID.
    # Args:
    #     employee_id (int): Unique identifier of the employee.
    # Returns:
    #     Employee object if found, otherwise raises 404 error.
    # """
    x = employee_crud.read_employee_by_id(employee_id)  # Call CRUD function
    if x is not None:
        return x                                      # Return employee record
    raise HTTPException(status_code=404, detail="Id Not Found")  # Raise error if not found

# -------------------------------
# POST endpoint: Create new employee
# -------------------------------
@app.post("/employees", response_model=Employee)
def create_employee(emp: Employee):
    # """
    # Create a new employee record.
    # Args:
    #     emp (Employee): Employee object with details to insert.
    # Returns:
    #     Newly created Employee object if successful, otherwise raises 409 error.
    # """
    x = employee_crud.create_employee(emp)  # Call CRUD function
    if x is not None:
        return x                             # Return created employee record
    raise HTTPException(status_code=409, detail="Error in employee Fields")  # Raise error if insertion fails

# -------------------------------
# PUT endpoint: Update employee by ID
# -------------------------------
@app.put("/employees/{employee_id}", response_model=Employee)
def update_by_id(employee_id: int, emp: Employee):
    # """
    # Update an existing employee record by ID.
    # Args:
    #     employee_id (int): Unique identifier of the employee.
    #     emp (Employee): Employee object with updated details.
    # Returns:
    #     Updated Employee object if successful, otherwise raises 404 error.
    # """
    success = employee_crud.update_employee_by_id(employee_id, emp)  # Call CRUD function
    if success:
        return employee_crud.read_employee_by_id(employee_id)        # Return updated record
    raise HTTPException(status_code=404, detail="Id Not Found")      # Raise error if not found

# -------------------------------
# DELETE endpoint: Delete employee by ID
# -------------------------------
@app.delete("/employees/{employee_id}")
def delete_by_id(employee_id: int):
    # """
    # Delete an employee record by ID.
    # Args:
    #     employee_id (int): Unique identifier of the employee.
    # Returns:
    #     Success message if deleted, otherwise raises 404 error.
    # """
    success = employee_crud.delete_employee_by_id(employee_id)  # Call CRUD function
    if success:
        return {"detail": "Employee Deleted"}                   # Return confirmation message
    raise HTTPException(status_code=404, detail="Employee Not Found")  # Raise error if not found
