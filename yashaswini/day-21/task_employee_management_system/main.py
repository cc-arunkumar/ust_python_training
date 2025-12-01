# Import required libraries
from fastapi import FastAPI, HTTPException   # FastAPI framework and exception handling
from pydantic import Field, field_validator, EmailStr, BaseModel   # Data validation with Pydantic
from typing import Optional   # For optional fields
import pymysql   # MySQL database connector
import datetime   # For date validation

# Initialize FastAPI application with a title
app = FastAPI(title="Employee Management System")

# Function to establish connection with MySQL database
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_ems_db"
    )

# Employee model with validation rules using Pydantic
class Employee(BaseModel):
    employee_id: int   # Unique employee ID
    first_name: str = Field(..., max_length=50, description="cannot exceed more than 50 characters")
    last_name: str = Field(..., max_length=50, description="cannot exceed more than 50 characters")
    email: EmailStr = Field(..., max_length=100, description="must be a valid email address format")
    position: Optional[str] = Field(None, max_length=50)   # Optional field
    salary: Optional[float] = Field(None, ge=1, description='salary must be greater 0 and negative values are not accepted')
    hire_date: str   # Hire date in YYYY-MM-DD format

    # Validator for first_name and last_name
    @field_validator("first_name", "last_name")
    def validate_names(cls, v):
        if not v.strip():
            raise ValueError("Name must not be empty")
        if not all(c.isalpha() or c in [' ', '-'] for c in v):
            raise ValueError("Name must contain only alphabets, spaces, or hyphens")
        return v

    # Validator for position field
    @field_validator("position")
    def validate_position(cls, v):
        if v and any(c in "@#$%" for c in v):
            raise ValueError("Position must not contain special characters like @, #, $, %")
        return v

    # Validator for hire_date field
    @field_validator("hire_date")
    def validate_hire_date(cls, v):
        try:
            date_obj = datetime.datetime.strptime(v, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("hire_date must follow YYYY-MM-DD format")
        if date_obj > datetime.date.today():
            raise ValueError("hire_date cannot be a future date")
        return v


# API endpoint to create a new employee
@app.post("/employees/")
def create_employee(employee: Employee):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Insert employee record into database
        cursor.execute("""
            INSERT INTO ust_ems_db.employee (first_name, last_name, email, position, salary, hire_date)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (employee.first_name, employee.last_name, employee.email,
              employee.position, employee.salary, employee.hire_date))
        conn.commit()
        return {"employee_id": cursor.lastrowid}   # Return newly created employee ID
    except pymysql.err.IntegrityError:
        # Handle duplicate email error
        raise HTTPException(status_code=400, detail="Email must be unique")
    finally:
        conn.close()


# API endpoint to fetch employee details by ID
@app.get("/employees/{employee_id}")
def get_employee_by_id(employee_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ust_ems_db.employee WHERE employee_id=%s", (employee_id,))
    result = cursor.fetchone()
    conn.close()
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result   # Return employee record


# API endpoint to update employee details
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: Employee):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ust_ems_db.employee WHERE employee_id=%s", (employee_id,))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="Employee not found")

    try:
        # Update employee record in database
        cursor.execute("""
            UPDATE ust_ems_db.employee
            SET first_name=%s, last_name=%s, email=%s, position=%s, salary=%s, hire_date=%s
            WHERE employee_id=%s
        """, (employee.first_name, employee.last_name, employee.email,
              employee.position, employee.salary, employee.hire_date, employee_id))
        conn.commit()
        return {"message": "Employee updated successfully"}
    except pymysql.err.IntegrityError:
        # Handle duplicate email error
        raise HTTPException(status_code=400, detail="Email must be unique")
    finally:
        conn.close()


# API endpoint to delete employee by ID
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ust_ems_db.employee WHERE employee_id=%s", (employee_id,))
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Employee not found")
    conn.close()
    return {"message": "Employee deleted successfully"}
