from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
import pymysql
from typing import List

# Initialize FastAPI and employee_router
app = FastAPI()
employee_router = APIRouter(prefix="/employees")

# Database connection function
def get_connection():
    return pymysql.connect(
        host="localhost",  # MySQL host
        user="root",  # MySQL user
        password="pass@word1",  # MySQL password
        database="ust_asset_db"  # Your database name
    )

# Pydantic model for Employee
class Employee(BaseModel):
    emp_code: str
    full_name: str
    email: str
    phone: str
    department: str
    location: str
    join_date: str
    status: str

# POST endpoint to create a new employee
@employee_router.post("/create")
def create_employee(employee: Employee):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """INSERT INTO employee_directory (emp_code, full_name, email, phone, department, location, 
                    join_date, status) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (employee.emp_code, employee.full_name, employee.email, employee.phone, 
                               employee.department, employee.location, employee.join_date, employee.status))
        connection.commit()
        emp_id = cursor.lastrowid  # Get the ID of the newly created employee
        cursor.close()
        connection.close()
        return {"message": "Employee created successfully", "emp_id": emp_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# GET endpoint to fetch all employees
@employee_router.get("/emp/list")
def get_all_employees():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employee_directory")
        employees = cursor.fetchall()
        cursor.close()
        connection.close()
        return employees
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

# GET endpoint to filter employees by status (Active, Inactive, Resigned)
@employee_router.get("/list")
def get_employees_by_status(status: str):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM employee_directory WHERE status = %s"
        cursor.execute(query, (status,))
        employees = cursor.fetchall()
        cursor.close()
        connection.close()
        return employees
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

# GET endpoint to get employee by emp_id
@employee_router.get("/{id}")
def get_employee_by_id(id: int):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM employee_directory WHERE emp_id = %s"
        cursor.execute(query, (id,))
        employee = cursor.fetchone()
        cursor.close()
        connection.close()
        if employee is None:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

# PUT endpoint to update an employee by emp_id
@employee_router.put("/{id}")
def update_employee(id: int, employee: Employee):
    try:
        # First, check if the employee exists
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM employee_directory WHERE emp_id = %s", (id,))
        count = cursor.fetchone()[0]
        
        if count == 0:
            cursor.close()
            connection.close()
            raise HTTPException(status_code=404, detail="Employee not found")
        
        # If the employee exists, perform the update
        query = """UPDATE employee_directory SET emp_code = %s, full_name = %s, email = %s, phone = %s, 
                   department = %s, location = %s, join_date = %s, status = %s 
                   WHERE emp_id = %s"""
        
        cursor.execute(query, (employee.emp_code, employee.full_name, employee.email, employee.phone, 
                               employee.department, employee.location, employee.join_date, employee.status, id))
        connection.commit()  # Commit the transaction
        cursor.close()
        connection.close()
        
        return {"message": "Employee updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# PATCH endpoint to update employee status by emp_id
@employee_router.patch("/{id}/status")
def update_employee_status(id: int, status: str):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "UPDATE employee_directory SET status = %s WHERE emp_id = %s"
        cursor.execute(query, (status, id))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Employee status updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# DELETE endpoint to delete employee by emp_id
@employee_router.delete("/{id}")
def delete_employee(id: int):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "DELETE FROM employee_directory WHERE emp_id = %s"
        cursor.execute(query, (id,))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Employee deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# GET endpoint to search employees by column (keyword) and value
@employee_router.get("/emp/search")
def search_employees(keyword: str, value: str):
    # List of valid columns to prevent SQL injection
    valid_columns = ["emp_code", "full_name", "email", "phone", "department", "location", "join_date", "status"]
    
    # Check if the provided keyword is valid
    if keyword not in valid_columns:
        raise HTTPException(status_code=400, detail=f"Invalid column name: {keyword}")
    
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        # Construct the search query with LIKE operator
        query = f"SELECT * FROM employee_directory WHERE {keyword} LIKE %s"
        search_pattern = f"%{value}%"  # Use LIKE operator for pattern matching
        
        # Execute the query
        cursor.execute(query, (search_pattern,))
        employees = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        if not employees:
            raise HTTPException(status_code=404, detail=f"No employees found for {keyword}={value}")
        
        return {"employees": employees}  # Returning employees in a dictionary to standardize response
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error: {str(e)}")



# GET endpoint to count total employees
@employee_router.get("/emp/count")
def count_employees():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT COUNT(*) FROM employee_directory"
        cursor.execute(query)
        count = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return {"total_employees": count}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

# Include the employee_router in the main FastAPI application
app.include_router(employee_router)
