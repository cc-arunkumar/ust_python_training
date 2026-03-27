
# Scenario: Employee Management System
# Objective:
# Create a simple Employee Management System (EMS) API using FastAPI that
# allows the user to perform basic CRUD operations (Create, Read, Update, Delete)
# on employee data. You will use MySQL for storing employee information. The
# system should include basic field validation and error handling.

# Task Requirements:
# 1. Database Design:
# Create a simple table in MySQL to store employee information with the following
# fields:
# employee_id: Integer (Primary Key, Auto Increment)
# first_name: String (Required, Max length 50)
# last_name: String (Required, Max length 50)
# email: String (Required, Unique, Max length 100)
# position: String (Optional, Max length 50)
# salary: Float (Optional, Must be greater than 0)
# hire_date: Date (Required)
# Table Schema:

# FastAPI Endpoints:
# 1. POST /employees/ - Add a new employee.
# Request Body: first_name , last_name , email , position , salary , hire_date
# Validation:
# Ensure all required fields are provided.
# Validate email format.
# Ensure salary is a positive value.
# Response: employee_id of the created employee.
# 2. GET /employees/{employee_id} - Get employee details by ID.
# URL Parameter: employee_id
# Response: Employee details.
# 3. PUT /employees/{employee_id} - Update employee information.
# Request Body: first_name , last_name , email , position , salary , hire_date

# Validation:
# Ensure the employee exists.
# Validate the email format and ensure it is unique.

# Response: Success or failure message.
# 4. DELETE /employees/{employee_id} - Delete an employee.
# URL Parameter: employee_id
# Response: Success or failure message.
# Steps to Implement:
# 1. Set up MySQL database:
# Install MySQL locally or use a cloud MySQL service (e.g., RDS).
# Create the employees table using the provided schema.
# 2. FastAPI Application Setup:
# Install required dependencies:
# pip install fastapi uvicorn pymysql
# 3. Create the FastAPI application:
# Define the models (Pydantic) for request validation.
# Create the API endpoints using FastAPI.
# 4. Basic Validations:
# Use FastAPI’s Pydantic models to validate the required fields.
# Ensure the correct data types are provided (e.g., email is valid, salary > 0).
# Ensure unique constraint on email.
# 5. MySQL Integration:
# Use pymysql or sqlalchemy to interact with the MySQL database.
# For each endpoint, create the necessary SQL queries to handle the CRUD
# operations.
# 6. Run and Test the API:
# Run the FastAPI app using uvicorn :

# uvicorn main:app --reload
# Test the API endpoints with Postman or cURL.
# Field Validation Rules
# Below are the exact validation rules that must be applied for each field when
# creating or updating an employee record.
# 1. first_name
# Type: String
# Required: Yes
# Validation Rules:
# Must not be empty.
# Maximum length: 50 characters.
# Should contain only alphabets (A–Z, a–z).
# No numbers or special characters allowed (except space or hyphen).
# Examples
# ✔ Valid: "John" , "Mary Ann" , "Jean-Paul"
# ❌ Invalid: "John123" , "" , "@Mike"
# 2.last_name
# Type: String
# Required: Yes
# Validation Rules:
# Must not be empty.
# Maximum length: 50 characters.
# Day 21 4
# Should contain only alphabets.
# No numbers or special characters (except space or hyphen).
# Examples
# ✔ Valid: "Doe" , "De Silva"
#  Invalid: "Doe99" , "!Smith"
# 3.email
# Type: String (Email Format)
# Required: Yes
# Validation Rules:
# Must be a valid email address format ( user@example.com ).
# Maximum length: 100 characters.
# Must be unique in the database.
# (System should reject if entered email already exists.)
# Must not contain spaces.
# Examples
# ✔ Valid: "john.doe@ust.com"
#  Invalid: "john@doe" , "john@.com" , "john doe@gmail.com"
# 4.position
# Type: String
# Required: No (Optional)
# Validation Rules:
# If provided, maximum length: 50 characters.
# Should not contain special characters like @, #, $, % etc.
# Can contain alphabets, numbers, spaces, and hyphens.
# Day 21 5
# Examples
# ✔ Valid: "Software Engineer" , "QA-1"
#  Invalid: "Dev@UST"
# 5.salary
# Type: Float
# Required: No (Optional)
# Validation Rules:
# If provided, must be a positive number.
# Must be greater than 0.
# Should not accept negative, zero, or non-numeric values.
# Examples
# ✔ Valid: 50000 , 60000.50
#  Invalid: 0 , -1000 , "abc"
# 6.hire_date
# Type: Date ( YYYY-MM-DD )
# Required: Yes
# Validation Rules:
# Must follow the format YYYY-MM-DD.
# Cannot be a future date.
# Must be a valid date (e.g., no 2025-02-30).
# Examples
# ✔ Valid: "2024-05-20"
#  Invalid: "20-05-2024" , "2024/05/20" , "2026-01-01"

# HTTP message validation rules
# A.Request Body
# Extra fields not defined in the model should be rejected.
# Missing required fields should return a 400 Bad Request .
# B.Error Messages Should Be Clear
# Examples:
# first_name is required
# email must be unique
# salary must be greater than 0
# Summary Table
# Field Required Type Max Length
# Validation
# Highlights
# first_name Yes String 50
# Alphabets only, no
# empty
# last_name Yes String 50 Alphabets only
# email Yes Email 100
# Valid format,
# unique
# position No String 50
# No special
# characters
# salary No Float — > 0, numeric
# hire_date Yes Date —
# Not future, valid
# date
# Deliverables:
# FastAPI project with the above endpoints.
# Database schema and connection logic.
# Day 21 7
# Validation for required fields and email uniqueness.


# Import necessary libraries
from fastapi import FastAPI, HTTPException
from pydantic import Field, field_validator, EmailStr, BaseModel
from typing import Optional
import pymysql
import datetime

# Create the FastAPI app
app = FastAPI(title="Employee Management System")

# Function to establish a database connection
def get_connection():
    # Return a connection to the MySQL database
    return pymysql.connect(
        host="localhost",       # Database host
        user="root",            # Database username
        password="pass@word1",  # Database password
        database="employee_db"  # Database name
    )

# Define the Employee model using Pydantic for data validation
class Employee(BaseModel):
    employee_id: int
    first_name: str = Field(..., max_length=50, description="cannot exceed more than 50 characters")
    last_name: str = Field(..., max_length=50, description="cannot exceed more than 50 characters")
    email: EmailStr = Field(..., max_length=100, description="must be a valid email address format")
    position: Optional[str] = Field(None, max_length=50)  # Position is optional
    salary: Optional[float] = Field(None, ge=1, description='salary must be greater than 0 and negative values are not accepted')
    hire_date: str

    # Validate the first name and last name
    @field_validator("first_name", "last_name")
    def validate_names(cls, v):
        # Check if the name is not empty or just spaces
        if not v.strip():
            raise ValueError("Name must not be empty")
        # Check if the name contains only alphabets, spaces, or hyphens
        if not all(c.isalpha() or c in [' ', '-'] for c in v):
            raise ValueError("Name must contain only alphabets, spaces, or hyphens")
        return v

    # Validate the position to ensure it doesn't have special characters
    @field_validator("position")
    def validate_position(cls, v):
        # Ensure the position does not contain special characters like @, #, $, %
        if v and any(c in "@#$%" for c in v):
            raise ValueError("Position must not contain special characters like @, #, $, %")
        return v

    # Validate the hire date to ensure it follows the correct format
    @field_validator("hire_date")
    def validate_hire_date(cls, v):
        try:
            # Attempt to parse the hire date to a datetime object
            date_obj = datetime.datetime.strptime(v, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("hire_date must follow YYYY-MM-DD format")  # Raise error if the date format is invalid
        # Ensure the hire date is not in the future
        if date_obj > datetime.date.today():
            raise ValueError("hire_date cannot be a future date")
        return v


# POST Endpoint to create a new employee
@app.post("/employees/")
def create_employee(employee: Employee):
    conn = get_connection()  # Get database connection
    cursor = conn.cursor()
    try:
        # Insert the employee data into the 'employees' table in the database
        cursor.execute("""
            INSERT INTO employee_db.employees (first_name, last_name, email, position, salary, hire_date)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (employee.first_name, employee.last_name, employee.email,
              employee.position, employee.salary, employee.hire_date))
        conn.commit()  # Commit the transaction to save the data
        return {"employee_id": cursor.lastrowid}  # Return the generated employee_id
    except pymysql.err.IntegrityError:
        # Handle the case where the email is not unique (integrity error)
        raise HTTPException(status_code=400, detail="Email must be unique")
    finally:
        conn.close()  # Close the database connection

# GET Endpoint to retrieve an employee by their ID
@app.get("/employees/{employee_id}")
def get_employee_by_id(employee_id: int):
    conn = get_connection()  # Get database connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee_db.employees WHERE employee_id=%s", (employee_id,))
    result = cursor.fetchone()  # Fetch the employee data
    conn.close()
    
    # If no employee is found, raise a 404 error
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    # Return the employee data
    return result

# PUT Endpoint to update an employee's information
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: Employee):
    conn = get_connection()  # Get database connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee_db.employees WHERE employee_id=%s", (employee_id,))
    
    # If the employee does not exist, raise a 404 error
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="Employee not found")
    
    try:
        # Update the employee data in the database
        cursor.execute("""
            UPDATE employee_db.employees
            SET first_name=%s, last_name=%s, email=%s, position=%s, salary=%s, hire_date=%s
            WHERE employee_id=%s
        """, (employee.first_name, employee.last_name, employee.email,
              employee.position, employee.salary, employee.hire_date, employee_id))
        conn.commit()  # Commit the changes
        return {"message": "Employee updated successfully"}  # Return a success message
    except pymysql.err.IntegrityError:
        # Handle the case where the email is not unique during the update
        raise HTTPException(status_code=400, detail="Email must be unique")
    finally:
        conn.close()  # Close the database connection

# DELETE Endpoint to delete an employee by their ID
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    conn = get_connection()  # Get database connection
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employee_db.employees WHERE employee_id=%s", (employee_id,))
    conn.commit()  # Commit the deletion
    
    # If no rows were affected (no employee found), raise a 404 error
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Employee not found")
    
    conn.close()  # Close the database connection
    return {"message": "Employee deleted successfully"}  # Return a success message



#output in database
# 1	Bhargavi	Meena	sbharg@ust.com	HR	100000	2024-02-02
# 3	Bhargavi	settipalli	sbhar@ust.com	HR	1000000	2024-02-02
# 4	Bhargavi	ssttipalli	sbhargavi@ust.com	HR	10000000	2023-02-03
						