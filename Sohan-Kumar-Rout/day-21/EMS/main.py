from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import date
import pymysql

# Employee model with validation rules
class Employee(BaseModel):
    first_name: str = Field(..., max_length=50, pattern=r"^[A-Za-z-]+$")
    last_name: str = Field(..., max_length=50, pattern=r"^[A-Za-z-]+$")
    email: str = Field(
        ...,
        max_length=100,
        pattern=r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    )
    position: str = Field(..., max_length=50, pattern=r"^[^@#$%]+$")
    salary: float = Field(..., ge=0)
    hire_date: date

# Database connection helper
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db",
        cursorclass=pymysql.cursors.DictCursor
    )

app = FastAPI(title="EMS")

# Temporary set for email uniqueness check (not persistent)
email_set = set()

# Create employee
@app.post("/employees/", response_model=Employee)
def create_employee(emp: Employee):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # Insert new employee record
        cursor.execute(
            """
            INSERT INTO emp_table (first_name, last_name, email, position, salary, hire_date)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (emp.first_name, emp.last_name, emp.email, emp.position, emp.salary, emp.hire_date)
        )
        conn.commit()
        # Basic checks
        if emp.email in email_set:
            raise HTTPException(status_code=404, detail="Email must be unique")
        if emp.hire_date > date.today():
            raise HTTPException(status_code=404, detail="Date is invalid")
        print("Employee record inserted successfully!")
        return emp
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Get employee by ID
@app.get("/employees/{employee_id}", response_model=Employee)
def get_by_id(employee_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM emp_table WHERE employee_id=%s", (employee_id,))
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Employee not found")
        return row
    finally:
        cursor.close()
        conn.close()

# Update employee
@app.put("/employees/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, employee: Employee):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # Update record
        cursor.execute(
            """
            UPDATE emp_table
            SET first_name=%s, last_name=%s, email=%s, position=%s, salary=%s, hire_date=%s
            WHERE employee_id=%s
            """,
            (employee.first_name, employee.last_name, employee.email,
             employee.position, employee.salary, employee.hire_date, employee_id)
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Employee not found")
        # Basic checks
        if employee.email in email_set:
            raise HTTPException(status_code=404, detail="Email must be unique")
        if employee.hire_date > date.today():
            raise HTTPException(status_code=404, detail="Date is invalid")
        return employee
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


# Delete employee
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # Delete record
        cursor.execute("DELETE FROM emp_table WHERE employee_id=%s", (employee_id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Employee not found")
        return {"status": "success", "message": f"Employee {employee_id} deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
