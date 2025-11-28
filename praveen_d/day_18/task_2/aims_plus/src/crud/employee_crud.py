import pymysql
from typing import List, Optional
from datetime import datetime
from src.config.db_connection import get_connection


# 1. Create Employee
def create_employee(employee_data: dict):
    query = """
        INSERT INTO aims_db.employee_directory (emp_code, full_name, email, phone, department, location, join_date, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    params = (
        employee_data["emp_code"],
        employee_data["full_name"],
        employee_data["email"],
        employee_data["phone"],
        employee_data["department"],
        employee_data["location"],
        employee_data["join_date"],
        employee_data["status"]
    )
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    conn.close()

# 2. Get all employees
def get_all_employees() -> List[dict]:
    query = "SELECT * FROM aims_db.employee_directory"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# 3. Get employee by status
def get_employees_by_status(status: str) -> List[dict]:
    query = "SELECT * FROM aims_db.employee_directory WHERE status = %s"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, (status,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# 4. Get employee by ID
def get_employee_by_id(id: int) :
    query = "SELECT * FROM aims_db.employee_directory WHERE id = %s"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

# 5. Update employee
def update_employee(id: int, employee_data: dict):
    query = """
        UPDATE aims_db.employee_directory
        SET emp_code = %s, full_name = %s, email = %s, phone = %s, department = %s, 
            location = %s, join_date = %s, status = %s
        WHERE id = %s
    """
    params = (
        employee_data["emp_code"],
        employee_data["full_name"],
        employee_data["email"],
        employee_data["phone"],
        employee_data["department"],
        employee_data["location"],
        employee_data["join_date"],
        employee_data["status"],
        id
    )
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    conn.close()

# 6. Update employee status
def update_employee_status(id: int, status: str):
    query = "UPDATE aims_db.employee_directory SET status = %s WHERE id = %s"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, (status, id))
    conn.commit()
    cursor.close()
    conn.close()

# 7. Delete employee
def delete_employee(id: int):
    query = "DELETE FROM aims_db.employee_directory WHERE id = %s"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, (id,))
    conn.commit()
    cursor.close()
    conn.close()

# 8. Search employees by keyword
def search_employees_by_keyword(keyword: str) -> List[dict]:
    like_keyword = f"%{keyword}%"
    query = """
        SELECT * FROM aims_db.employee_directory
        WHERE emp_code LIKE %s OR full_name LIKE %s OR email LIKE %s
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, (like_keyword, like_keyword, like_keyword))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# 9. Get employee count
def get_employee_count() -> int:
    query = "SELECT COUNT(*) FROM aims_db.employee_directory"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result["COUNT(*)"]
