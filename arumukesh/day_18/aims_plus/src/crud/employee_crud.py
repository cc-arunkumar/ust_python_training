# from services import (
#     create_emp, get_all_emp, get_emp_by_id, 
#     get_emp_by_status, update_emp, update_emp_status, 
#     delete_emp, get_emp_count, search_emp_key
# )
from src.model.model_employees import Employee
import pymysql
from src.config.get_connection import get_connection

# ---------- CREATE EMPLOYEE ----------
def create_employee(emp:Employee):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO employee_directory
        (emp_code, full_name, email, phone, department, location, join_date, status)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    # Check duplicate
    # cursor.execute("SELECT emp_code FROM employee_directory WHERE emp_code=%s", (emp.emp_code,))
    # if cursor.fetchone():
        # raise Exception(f"Employee '{emp.emp_code}' already exists.")

    cursor.execute(query, (
        emp.emp_code, emp.full_name, emp.email, emp.phone, emp.department,
        emp.location, emp.join_date, emp.status
    ))
    conn.commit()
    conn.close()
    return {"Employee added successfully."}


# ---------- GET ALL EMPLOYEES ----------
def get_all():
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM employee_directory")
    employees = cursor.fetchall()

    conn.close()
    return employees


# ---------- GET EMPLOYEE BY ID ----------
def get_by_id(emp_id):
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM employee_directory WHERE emp_id=%s", (emp_id,))
    employee = cursor.fetchone()

    conn.close()

    if not employee:
        raise Exception("Employee not found!")

    return employee


# ---------- GET EMPLOYEE BY STATUS ----------
def get_emp_by_status(status):
    conn = get_connection()
    cursor=conn.cursor()
    # cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM employee_directory WHERE status=%s", (status,))
    employees = cursor.fetchall()

    conn.close()
    return employees


# ---------- UPDATE FULL EMPLOYEE ----------
def update(emp_id, emp):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE employee_directory
        SET emp_code=%s, full_name=%s, email=%s, phone=%s,
            department=%s, location=%s, join_date=%s, status=%s
        WHERE emp_id=%s
    """

    cursor.execute(query, (
        emp.emp_code, emp.full_name, emp.email, emp.phone, emp.department,
        emp.location, emp.join_date, emp.status, emp_id
    ))

    if cursor.rowcount == 0:
        raise Exception("Update failed. Employee does not exist.")

    conn.close()
    return "Employee updated successfully."

# update,
#     delete,
#     get_by_stat,
#     get_count,
#     find
# ---------- UPDATE EMPLOYEE STATUS ONLY ----------
def update_emp_status(emp_id, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE employee_directory SET status=%s WHERE emp_id=%s",
        (status, emp_id)
    )

    if cursor.rowcount == 0:
        raise Exception("Employee not found!")

    conn.close()
    return "Employee status updated."


# ---------- DELETE EMPLOYEE ----------
def delete(emp_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM employee_directory WHERE emp_id=%s", (emp_id,))

    if cursor.rowcount == 0:
        raise Exception("Employee not found!")

    conn.close()
    return "Employee deleted."


# ---------- EMPLOYEE COUNT ----------
def get_count():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM employee_directory")
    count = cursor.fetchone()[0]

    conn.close()
    return count


# ---------- SEARCH EMPLOYEE BY COLUMN ----------
def find(column, value):
    conn = get_connection()
    cursor = conn.cursor()

    allowed_columns = ["emp_code", "full_name", "email", "phone", "department", "location", "status"]

    if column not in allowed_columns:
        raise Exception(f"Invalid search field: {column}")

    cursor.execute(f"SELECT * FROM employee_directory WHERE {column} LIKE %s", (f"%{value}%",))
    results = cursor.fetchall()

    conn.close()
    return results
