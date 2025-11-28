# -------------------------------
# Import required libraries
# -------------------------------
from fastapi import FastAPI, HTTPException, APIRouter   # FastAPI classes for app, routing, and error handling
from pydantic import BaseModel                         # For request/response validation
import pymysql                                         # MySQL client library

# -------------------------------
# Initialize FastAPI app and router
# -------------------------------
# The main FastAPI app is created with a title for documentation.
# A router is defined for employee-related endpoints, grouped under "/employees".
app = FastAPI(title="Employee Directory API")
employee_router = APIRouter(prefix="/employees", tags=['Employees'])

# -------------------------------
# Database Connection Function
# -------------------------------
# Creates and returns a connection to the MySQL database.
# DictCursor ensures query results are returned as dictionaries instead of tuples.
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db",
        cursorclass=pymysql.cursors.DictCursor
    )

# -------------------------------
# Pydantic Model for Employee
# -------------------------------
# Defines the structure of an Employee record.
# Used for validation when creating or updating employees.
class Employee(BaseModel):
    emp_code: str
    full_name: str
    email: str
    phone: int
    join_date: str
    department: str
    location: str
    status: str  # Possible values: 'Active', 'Inactive', 'Resigned'


# -------------------------------
# GET Endpoints
# -------------------------------

# GET /employees/list
# Fetch all employees, with optional filtering by status.
@employee_router.get("/list")
def get_employees(status: str = None):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        if status:
            # Case-insensitive filter by status
            query = "SELECT * FROM employee_directory WHERE LOWER(status) = LOWER(%s)"
            cursor.execute(query, (status,))
        else:
            # Fetch all employees
            query = "SELECT * FROM employee_directory"
            cursor.execute(query)

        employees = cursor.fetchall()
        cursor.close()
        connection.close()
        return employees
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# GET /employees/search?keyword=
# Search employees by keyword across multiple fields.
@employee_router.get("/search")
def search_employees(keyword: str):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT * FROM employee_directory 
        WHERE emp_code LIKE %s OR full_name LIKE %s OR email LIKE %s 
        OR phone LIKE %s OR join_date LIKE %s OR department LIKE %s OR status LIKE %s
    """
    like_pattern = f"%{keyword}%"
    cursor.execute(query, (like_pattern,) * 7)  # Apply keyword to all 7 fields
    employees = cursor.fetchall()

    cursor.close()
    connection.close()
    return employees


# GET /employees/count
# Return the total number of employees in the directory.
@employee_router.get("/count")
def get_employee_count():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) AS count FROM employee_directory")
    count = cursor.fetchone()["count"]
    cursor.close()
    connection.close()
    return {"count": count}


# GET /employees/{id}
# Retrieve a single employee by their unique ID.
@employee_router.get("/{id}")
def get_employee_by_id(id: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employee_directory WHERE emp_id = %s", (id,))
    employee = cursor.fetchone()
    cursor.close()
    connection.close()

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


# -------------------------------
# POST Endpoint
# -------------------------------

# POST /employees/create
# Create a new employee record in the database.
@employee_router.post("/create")
def create_employee(employee: Employee):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """INSERT INTO employee_directory 
                   (emp_code, full_name, email, phone, department, location, join_date, status)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (employee.emp_code, employee.full_name, employee.email,
                               employee.phone, employee.department, employee.location, employee.join_date, employee.status))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Employee created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# -------------------------------
# PUT Endpoint
# -------------------------------

# PUT /employees/{id}
# Update an existing employee record by ID (full update of all fields).
@employee_router.put("/{id}")
def update_employee(id: int, employee: Employee):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Check if employee exists before updating
        cursor.execute("SELECT COUNT(*) AS count FROM employee_directory WHERE emp_id = %s", (id,))
        count = cursor.fetchone()["count"]

        if count == 0:
            cursor.close()
            connection.close()
            raise HTTPException(status_code=404, detail="Employee not found")

        # Update employee record
        query = """UPDATE employee_directory 
                   SET emp_code = %s, full_name = %s, email = %s, phone = %s, department = %s,
                       location = %s, join_date = %s, status = %s 
                   WHERE emp_id = %s"""
        cursor.execute(query, (employee.emp_code, employee.full_name, employee.email,
                               employee.phone, employee.department, employee.location, employee.join_date, employee.status, id))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Employee updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# -------------------------------
# PATCH Endpoint
# -------------------------------

# PATCH /employees/{id}/status
# Update only the status field of an employee (partial update).
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


# -------------------------------
# DELETE Endpoint
# -------------------------------

# DELETE /employees/{id}
# Delete an employee record by ID.
# After deletion, reorder emp_id values to be sequential and reset AUTO_INCREMENT.
@employee_router.delete("/{id}")
def delete_employee(id: int):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Delete the employee
        query = "DELETE FROM employee_directory WHERE emp_id = %s"
        cursor.execute(query, (id,))
        connection.commit()

        # Reorder emp_id values sequentially
        reorder_query = """
            SET @count = 0;
            UPDATE employee_directory SET emp_id = (@count:=@count+1) ORDER BY emp_id;
        """
        for stmt in reorder_query.split(";"):
            if stmt.strip():
                cursor.execute(stmt)
        connection.commit()

        # Reset AUTO_INCREMENT to max(emp_id)+1
        cursor.execute("SELECT COALESCE(MAX(emp_id), 0) + 1 AS next_id FROM employee_directory")
        next_id = cursor.fetchone()["next_id"]
        cursor.execute(f"ALTER TABLE employee_directory AUTO_INCREMENT = {next_id}")
        connection.commit()

        cursor.close()
        connection.close()
        return {"message": "Employee deleted successfully, IDs reordered and AUTO_INCREMENT reset"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# -------------------------------
# Register Router with App
# -------------------------------
# Attach the employee router to the main FastAPI app.
app.include_router(employee_router)
