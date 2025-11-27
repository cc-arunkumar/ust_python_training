import pymysql
from src.config.db_connection import get_connection

# CREATE
def create_employee(emp_code, full_name, email, phone, department, location, join_date, status):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
    INSERT INTO employee_master (
        emp_code, full_name, email, phone, department, location, join_date, status
    ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    cursor.execute(sql, (emp_code, full_name, email, phone, department, location, join_date, status))
    conn.commit()
    emp_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return emp_id

# READ
def get_employee_by_id(emp_id):
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM employee_master WHERE emp_id=%s", (emp_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def get_all_employees(status=None):
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    if status:
        cursor.execute("SELECT * FROM employee_master WHERE status=%s", (status,))
    else:
        cursor.execute("SELECT * FROM employee_master")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def search_employees(keyword):
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    like = f"%{keyword}%"
    sql = """SELECT * FROM employee_master
             WHERE emp_code LIKE %s OR full_name LIKE %s OR email LIKE %s OR department LIKE %s"""
    cursor.execute(sql, (like, like, like, like))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def count_employees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM employee_master")
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return count

# UPDATE
def update_employee(emp_id, emp_code, full_name, email, phone, department, location, join_date, status):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """UPDATE employee_master
             SET emp_code=%s, full_name=%s, email=%s, phone=%s,
                 department=%s, location=%s, join_date=%s, status=%s
             WHERE emp_id=%s"""
    cursor.execute(sql, (emp_code, full_name, email, phone, department, location, join_date, status, emp_id))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def update_employee_status(emp_id, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE employee_master SET status=%s WHERE emp_id=%s", (status, emp_id))
    conn.commit()
    cursor.close()
    conn.close()
    return True

# DELETE
def delete_employee(emp_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employee_master WHERE emp_id=%s", (emp_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return True
