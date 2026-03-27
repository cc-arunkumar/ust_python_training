from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
import pymysql

# Initialize FastAPI app and router
app = FastAPI(title="Employee Directory API")
employee_router = APIRouter(prefix="/employees", tags=['employees'])

# Database connection function
def get_connection():
    # Establishes a connection to the MySQL database
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db",  # Replace with your database name
        cursorclass=pymysql.cursors.DictCursor  # Return dicts instead of tuples
    )

# Pydantic model for Employee
class Employee(BaseModel):
    # Defines the structure for Employee data with validation
    emp_code: str
    full_name: str
    email: str
    phone: int
    join_date: str
    department: str
    location: str
    status: str  # 'Active', 'Inactive', 'Resigned
    
# GET /employees/list (with optional status filter)
@employee_router.get("/list")
def get_employees(status: str = None):
    try:
        # Fetches all employees or filters by status if provided
        connection = get_connection()
        cursor = connection.cursor()

        if status:
            query = "SELECT * FROM employee_directory WHERE LOWER(status) = LOWER(%s)"
            cursor.execute(query, (status,))
        else:
            query = "SELECT * FROM employee_directory"
            cursor.execute(query)

        employees = cursor.fetchall()
        cursor.close()
        connection.close()
        return employees
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Handles errors


# GET /employees/search?keyword=
@employee_router.get("/search")
def search_employees(keyword: str):
    # Searches for employees using the provided keyword across multiple fields
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT * FROM employee_directory 
        WHERE emp_code LIKE %s OR full_name LIKE %s OR email LIKE %s 
        OR phone LIKE %s OR join_date LIKE %s OR department LIKE %s OR status LIKE %s
    """
    like_pattern = f"%{keyword}%"
    cursor.execute(query, (like_pattern,) * 7)
    employees = cursor.fetchall()

    cursor.close()
    connection.close()
    return employees


# GET /employees/count
@employee_router.get("/count")
def get_employee_count():
    # Counts the total number of employees in the database
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) AS count FROM employee_directory")
    count = cursor.fetchone()["count"]
    cursor.close()
    connection.close()
    return {"count": count}


# GET /employees/{id}
@employee_router.get("/{id}")
def get_employee_by_id(id: int):
    # Fetches a specific employee by their emp_id
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employee_directory WHERE emp_id = %s", (id,))
    employee = cursor.fetchone()
    cursor.close()
    connection.close()

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


# POST /employees/create
@employee_router.post("/create")
def create_employee(employee: Employee):
    # Creates a new employee record in the database
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """INSERT INTO employee_directory 
                   (emp_code, full_name, email, phone, department, location, join_date, status)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (employee.emp_code, employee.full_name, employee.email,
                               employee.phone, employee.department, employee.location, employee.join_date, employee.status))
        connection.commit()  # Commit the transaction
        cursor.close()
        connection.close()
        return {"message": "Employee created successfully"}  # Return success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Handle errors during creation


# PUT /employees/{id}
@employee_router.put("/{id}")
def update_employee(id: int, employee: Employee):
    # Updates an existing employee record by emp_id
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) AS count FROM employee_directory WHERE emp_id = %s", (id,))
        count = cursor.fetchone()["count"]

        if count == 0:
            cursor.close()
            connection.close()
            raise HTTPException(status_code=404, detail="Employee not found")

        query = """UPDATE employee_directory 
                   SET emp_code = %s, full_name = %s, email = %s, phone = %s, department = %s
                       location = %s, join_date = %s, status = %s 
                   WHERE emp_id = %s"""
        cursor.execute(query, (employee.emp_code, employee.full_name, employee.email,
                               employee.phone, employee.department, employee.location, employee.join_date, employee.status))
        connection.commit()  # Commit the transaction
        cursor.close()
        connection.close()
        return {"message": "Employee updated successfully"}  # Return success message
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Handle errors


# PATCH /employees/{id}/status
@employee_router.patch("/{id}/status")
def update_employee_status(id: int, status: str):
    # Updates the status of an employee by emp_id
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "UPDATE employee_directory SET status = %s WHERE emp_id = %s"
        cursor.execute(query, (status, id))
        connection.commit()  # Commit the transaction
        cursor.close()
        connection.close()
        return {"message": "Employee status updated successfully"}  # Return success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Handle errors

# DELETE /employees/{id}
@employee_router.delete("/{id}")
def delete_employee(id: int):
    # Deletes an employee record by emp_id and reorders the employee IDs
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Delete the employee
        query = "DELETE FROM employee_directory WHERE emp_id = %s"
        cursor.execute(query, (id,))
        connection.commit()

        # Reorder emp_id values to be sequential
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
        raise HTTPException(status_code=400, detail=str(e))  # Handle errors


# Register router with app
app.include_router(employee_router)  # Add the employee router to the FastAPI app
