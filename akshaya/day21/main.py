from fastapi import FastAPI, HTTPException  # Import FastAPI and HTTPException for API creation and error handling
from db_connection import get_connection  # Import the custom database connection function
from pydantic import BaseModel, Field, EmailStr, field_validator  # Import Pydantic models and field validation
from typing import Optional  # Import Optional type for optional fields
from datetime import date  # Import date class for date handling

app = FastAPI(title="Employee Management System")  # Create the FastAPI app with a custom title

# Define the Employee model using Pydantic for data validation and serialization
class Employee(BaseModel):
    # First name must be a non-empty string, containing only letters, spaces, or hyphens
    first_name: str = Field(..., min_length=1, max_length=50, pattern=r"^[A-Za-z -]+$")
    
    # Last name with the same validation rules as first name
    last_name: str = Field(..., min_length=1, max_length=50, pattern=r"^[A-Za-z -]+$")
    
    # Email field with validation for a proper email format
    email: EmailStr = Field(..., max_length=100)
    
    # Position field is optional, allows letters, numbers, spaces, and hyphens
    position: Optional[str] = Field(None, max_length=50, pattern=r"^[A-Za-z0-9 -]+$")
    
    # Salary field is optional, must be greater than zero if provided
    salary: Optional[float] = Field(gt=0)
    
    # Hire date field with a validator function to ensure the date is not in the future
    hire_date: date

    # Validator function for hire_date to ensure it is not in the future
    @field_validator("hire_date")
    def validate_hire_date(cls, hd: date):
        if hd > date.today():
            raise ValueError("hire_date cannot be in future")  # Raise error if the hire date is in the future
        return hd

# POST endpoint to create a new employee
@app.post("/employees/")
def create_employee(emp: Employee):
    # Establish database connection
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            # Check if the email already exists in the database
            cur.execute("SELECT employee_id FROM employees WHERE email=%s", (emp.email,))
            if cur.fetchone():
                raise HTTPException(status_code=400, detail="email must be unique")  # Raise error if email is not unique

            # SQL query to insert a new employee into the employees table
            sql = """
            INSERT INTO employees (first_name, last_name, email, position, salary, hire_date)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cur.execute(sql, (
                emp.first_name,
                emp.last_name,
                emp.email,
                emp.position,
                emp.salary,
                emp.hire_date
            ))
            conn.commit()  # Commit the transaction to save the new employee
            return {"employee_id": cur.lastrowid}  # Return the ID of the newly inserted employee
    finally:
        conn.close()  # Close the database connection

# GET endpoint to retrieve an employee by their ID
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    conn = get_connection()  # Establish database connection
    try:
        with conn.cursor() as cur:
            # Query the database for the employee with the given ID
            cur.execute("SELECT * FROM employees WHERE employee_id=%s", (employee_id,))
            emp = cur.fetchone()  # Fetch the result
            if not emp:
                raise HTTPException(status_code=404, detail="Employee not found")  # Raise error if employee does not exist
            return emp  # Return the employee's data
    finally:
        conn.close()  # Close the database connection

# PUT endpoint to update an existing employee's details
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, emp: Employee):
    conn = get_connection()  # Establish database connection
    try:
        with conn.cursor() as cur:
            # SQL query to update the employee's details
            sql = """
            UPDATE employees
            SET first_name=%s, last_name=%s, email=%s, position=%s, salary=%s, hire_date=%s
            WHERE employee_id=%s
            """
            cur.execute(sql, (
                emp.first_name,
                emp.last_name,
                emp.email,
                emp.position,
                emp.salary,
                emp.hire_date,
                employee_id
            ))
            conn.commit()  # Commit the transaction to update the employee
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Employee not found")  # Raise error if no rows were updated
            return {"message": "Employee updated successfully"}  # Return success message
    finally:
        conn.close()  # Close the database connection

# DELETE endpoint to remove an employee by their ID
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    conn = get_connection()  # Establish database connection
    try:
        with conn.cursor() as cur:
            # SQL query to delete the employee with the given ID
            cur.execute("DELETE FROM employees WHERE employee_id=%s", (employee_id,))
            conn.commit()  # Commit the transaction to delete the employee
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Employee not found")  # Raise error if employee was not found
            return {"message": "Employee deleted successfully"}  # Return success message
    finally:
        conn.close()  # Close the database connection
