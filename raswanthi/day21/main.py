from fastapi import FastAPI, HTTPException
from validation_model import EmployeeInfo
from pydantic import EmailStr
from datetime import date
from db_connection import get_connection

app = FastAPI(title="Employee Management System")


@app.post("/employees/")
def create_employee(emp:EmployeeInfo):
    conn = get_connection()
    try:
        with conn.cursor() as curs:
            sql = """
            INSERT INTO employees (first_name, last_name, email, position, salary, hire_date)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            curs.execute(sql, (
                emp.first_name,
                emp.last_name,
                emp.email,
                emp.position,
                emp.salary,
                emp.hire_date
            ))
            conn.commit()
            return {"employee_id": curs.lastrowid}
    
    finally:
        conn.close()

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    conn = get_connection()
    try:
        with conn.cursor() as curs:
            curs.execute("SELECT * FROM employees WHERE employee_id=%s", (employee_id,))
            emp = curs.fetchone()
            if not emp:
                raise HTTPException(status_code=404, detail="Employee not found")
            return emp

    finally:
        conn.close()
        
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, emp: EmployeeInfo):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
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
            conn.commit()
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Employee not found")
            return {"message": "Employee updated successfully"}
    finally:
        conn.close()
        
        
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id:int):
    conn=get_connection()
    try:
        with conn.cursor() as curs:
            curs.execute("DELETE from employees where employee_id=%s",(employee_id,))
            if curs.rowcount == 0:
                raise HTTPException(status_code=404, detail="Employee not found")
            conn.commit()
            return {"message": "Employee deleted successfully"}
    finally:
        conn.close()
            