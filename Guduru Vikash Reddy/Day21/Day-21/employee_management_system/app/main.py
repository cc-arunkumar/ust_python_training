from fastapi import FastAPI, HTTPException, status
from pydantic import EmailStr
from typing import List
from models import EmployeeCreate, EmployeeUpdate, EmployeeInDB
from db_connection import get_db_connection
import pymysql

app = FastAPI(title= "Employee Management System")

# 1. Add a new employee
@app.post("/employees/", response_model=int)
async def create_employee(employee: EmployeeCreate):
    with get_db_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO employees (first_name, last_name, email, position, salary, hire_date) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (employee.first_name, employee.last_name, employee.email, employee.position, employee.salary, employee.hire_date)
            )
            connection.commit()
            return cursor.lastrowid
        except pymysql.MySQLError as e:
            connection.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
@app.get("/employees/", response_model=List[EmployeeInDB])
async def get_all_employees():
    with get_db_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees")
        result = cursor.fetchall()
        if not result:
            raise HTTPException(status_code=404, detail="No employees found")
        return result        

# 2. Get employee details by ID
@app.get("/employees/{employee_id}", response_model=EmployeeInDB)
async def get_employee(employee_id: int):
    with get_db_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees WHERE employee_id = %s", (employee_id,))
        result = cursor.fetchone()
        if not result:
            raise HTTPException(status_code=404, detail="Employee not found")
        return result

# 3. Update an existing employee
@app.put("/employees/{employee_id}")
async def update_employee(employee_id: int, employee: EmployeeUpdate):
    with get_db_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees WHERE employee_id = %s", (employee_id,))
        existing_employee = cursor.fetchone()
        if not existing_employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        
        # Prepare updated data
        updated_data = {**existing_employee, **employee.dict(exclude_unset=True)}
        cursor.execute("""
            UPDATE employees
            SET first_name = %s, last_name = %s, email = %s, position = %s, salary = %s, hire_date = %s
            WHERE employee_id = %s
        """, (
            updated_data['first_name'], updated_data['last_name'], updated_data['email'], updated_data['position'],
            updated_data['salary'], updated_data['hire_date'], employee_id
        ))
        connection.commit()
        return {"message": "Employee updated successfully"}

# 4. Delete an employee
@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):
    with get_db_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees WHERE employee_id = %s", (employee_id,))
        existing_employee = cursor.fetchone()
        if not existing_employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        cursor.execute("DELETE FROM employees WHERE employee_id = %s", (employee_id,))
        connection.commit()
        return {"message": "Employee deleted successfully"}
