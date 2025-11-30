from fastapi import FastAPI, HTTPException
from pydantic import Field, field_validator, EmailStr, BaseModel
from typing import Optional
import pymysql
import datetime

# FastAPI app initialization
app = FastAPI(title="Employee Management System")

# Database connection function
def get_connection():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="pass@word1",
            database="ust_ems_db"  # Database name
        )
        print("Database connection successful")
        return conn
    except pymysql.MySQLError as e:
        print(f"Database connection error: {e}")
        return None

# Employee Pydantic model for validation
class Employee(BaseModel):
    first_name: str = Field(..., max_length=50, description="First name cannot exceed more than 50 characters")
    last_name: str = Field(..., max_length=50, description="Last name cannot exceed more than 50 characters")
    email: EmailStr = Field(..., max_length=100, description="Email must be a valid email address format")
    position: Optional[str] = Field(None, max_length=50, description="Position cannot exceed 50 characters")
    salary: Optional[float] = Field(None, ge=1, description="Salary must be greater than 0")
    hire_date: str  # Should be in YYYY-MM-DD format

    # Validate first and last names (only alphabets, spaces, or hyphens)
    @field_validator("first_name", "last_name")
    def validate_names(cls, v):
        if not v.strip():
            raise ValueError("Name must not be empty")
        if not all(c.isalpha() or c in [' ', '-'] for c in v):
            raise ValueError("Name must contain only alphabets, spaces, or hyphens")
        return v
    
    # Validate position (no special characters allowed)
    @field_validator("position")
    def validate_position(cls, v):
        if v and any(c in "@#$%" for c in v):
            raise ValueError("Position must not contain special characters like @, #, $, %")
        return v
    
    # Validate hire_date (should follow correct date format and not be in the future)
    @field_validator("hire_date")
    def validate_hire_date(cls, v):
        try:
            date_obj = datetime.datetime.strptime(v, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("hire_date must follow YYYY-MM-DD format")
        if date_obj > datetime.date.today():
            raise ValueError("hire_date cannot be a future date")
        return v

# Route to create an employee (POST)
@app.post("/employees/")
def create_employee(employee: Employee):
    conn = get_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = conn.cursor()
    try:
        # Insert into employee_info table in the ust_ems_db database
        cursor.execute("""
            INSERT INTO ust_ems_db.employee_info (first_name, last_name, email, position, salary, hire_date)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (employee.first_name, employee.last_name, employee.email,
              employee.position, employee.salary, employee.hire_date))
        
        # Commit the transaction
        conn.commit()

        # Return the generated employee_id (from AUTO_INCREMENT)
        return {"employee_id": cursor.lastrowid, "msg": "Employee created successfully"}

    except pymysql.MySQLError as e:
        # Rollback the transaction in case of error
        conn.rollback()
        raise HTTPException(status_code=400, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

# Route to get an employee by ID (GET)
@app.get("/employees/{employee_id}")
def get_employee_by_id(employee_id: int):
    conn = get_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = conn.cursor()
    try:
        # Fetch employee data using employee_id
        cursor.execute("SELECT * FROM ust_ems_db.employee_info WHERE employee_id = %s", (employee_id,))
        result = cursor.fetchone()

        # If no employee is found, raise an exception
        if not result:
            raise HTTPException(status_code=404, detail="Employee not found")

        # Return the result
        return result
    except pymysql.MySQLError as e:
        raise HTTPException(status_code=400, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

# Route to get all employees (GET all)
@app.get("/employees/")
def get_all_employees():
    conn = get_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = conn.cursor()
    try:
        # Fetch all employee data
        cursor.execute("SELECT * FROM ust_ems_db.employee_info")
        result = cursor.fetchall()

        # If no employees are found, raise an exception
        if not result:
            raise HTTPException(status_code=404, detail="No employees found")

        # Return the result
        return result
    except pymysql.MySQLError as e:
        raise HTTPException(status_code=400, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

# Route to update an employee (PUT)
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: Employee):
    conn = get_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = conn.cursor()
    try:
        # Check if employee exists
        cursor.execute("SELECT * FROM ust_ems_db.employee_info WHERE employee_id = %s", (employee_id,))
        existing_employee = cursor.fetchone()

        if not existing_employee:
            raise HTTPException(status_code=404, detail="Employee not found")

        # Update employee data in the database
        cursor.execute("""
            UPDATE employee_info
            SET first_name = %s, last_name = %s, email = %s, position = %s, salary = %s, hire_date = %s
            WHERE employee_id = %s
        """, (employee.first_name, employee.last_name, employee.email, 
              employee.position, employee.salary, employee.hire_date, employee_id))
        
        # Commit the transaction
        conn.commit()

        return {"msg": f"Employee with ID {employee_id} updated successfully"}
    
    except pymysql.MySQLError as e:
        conn.rollback()  # Rollback the transaction in case of error
        raise HTTPException(status_code=400, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

# Route to delete an employee (DELETE)
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    conn = get_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = conn.cursor()
    try:
        # Check if employee exists
        cursor.execute("SELECT * FROM ust_ems_db.employee_info WHERE employee_id = %s", (employee_id,))
        existing_employee = cursor.fetchone()

        if not existing_employee:
            raise HTTPException(status_code=404, detail="Employee not found")

        # Delete employee data from the database
        cursor.execute("DELETE FROM ust_ems_db.employee_info WHERE employee_id = %s", (employee_id,))
        
        # Commit the transaction
        conn.commit()

        return {"msg": f"Employee with ID {employee_id} deleted successfully"}
    
    except pymysql.MySQLError as e:
        conn.rollback()  # Rollback the transaction in case of error
        raise HTTPException(status_code=400, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

