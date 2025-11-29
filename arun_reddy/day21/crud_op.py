import pymysql
from datetime import datetime
from fastapi import HTTPException, status

# Function to establish and return a connection to the MySQL database
def get_Connection():
    return pymysql.connect(
        host="localhost",      # Database server host
        user="root",           # Database username
        password="pass@word1", # Database password
        database="ust_mang_system" # Database name
    )

# Column headers used to map query results to dictionary keys
headers = ["employee_id", "first_name", "last_name", "email", "position", "salary", "hire_date"]

# Function to insert a new employee record into the database
def insert_emp(emp):
    try:
        conn = get_Connection()       # Establish connection
        cursor = conn.cursor()        # Create cursor object
        query = """INSERT INTO ust_mang_system.employees
                   (first_name, last_name, email, position, salary, hire_date)  
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        # Prepare data tuple from employee object
        data = (emp.first_name, emp.last_name, emp.email, emp.position, emp.salary, emp.hire_date)
        cursor.execute(query, data)   # Execute insert query
        conn.commit()                 # Commit transaction
        return {"message": "Inserted into database"}
    except Exception as e:
        # Raise HTTP 500 error if something goes wrong
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) 
    finally:
        # Ensure resources are closed properly
        if conn.open:
            cursor.close()
            conn.close()

# Function to fetch all employee records
def get_all():
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_mang_system.employees")  # Fetch all rows
        employees = cursor.fetchall()
        if len(employees) == 0:
            raise Exception("Employees not found")
        # Convert each row into a dictionary using headers
        responselist = [dict(zip(headers, emp)) for emp in employees]
        return responselist
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to fetch a single employee by ID
def get_by_id(emp_id):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        query = """SELECT * FROM ust_mang_system.employees WHERE EMPLOYEE_ID=%s"""
        data = (emp_id,)
        cursor.execute(query, data)
        employee = cursor.fetchone()   # Fetch one row
        print(employee)                # Debug print
        if employee:
            return dict(zip(headers, employee))  # Map to dictionary
        else:
            raise Exception("Employee ID not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to update an existing employee record
def update_employee(emp_id, emp):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        query = """UPDATE ust_mang_system.employees 
                   SET first_name=%s, last_name=%s, email=%s, position=%s, salary=%s, hire_date=%s 
                   WHERE EMPLOYEE_ID=%s"""
        data = (emp.first_name, emp.last_name, emp.email, emp.position, emp.salary, emp.hire_date, emp_id)
        cursor.execute(query, data)   # Execute update query
        conn.commit()                 # Commit changes
        return emp
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to delete an employee record by ID
def delete_by_id(emp_id):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        # NOTE: (emp_id,) must be a tuple, not just emp_id
        cursor.execute("DELETE FROM ust_mang_system.employees WHERE EMPLOYEE_ID=%s", (emp_id,))
        conn.commit()
        return {"message": "Employee deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()
