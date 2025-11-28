from src.config.db_connct import get_conn
from src.exception.custom_exceptions import RecordNotFoundException, DuplicateRecordException

def create_employee(emp):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT emp_id FROM employee_directory WHERE email=%s", (emp.email,))
        if cur.fetchone():
            raise DuplicateRecordException("Email already exists")
        cur.execute("""
            INSERT INTO employee_directory
            (emp_code, full_name, email, phone, department, location, join_date, status, last_updated)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,NOW())
        """, (
            emp.emp_code, emp.full_name, emp.email, emp.phone,
            emp.department, emp.location, emp.join_date, emp.status
        ))
        conn.commit()
        return cur.lastrowid
    finally:
        cur.close()
        conn.close()

def update_employee(emp_id, emp):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM employee_directory WHERE emp_id=%s", (emp_id,))
        if not cur.fetchone():
            raise RecordNotFoundException("Employee not found")
        cur.execute("""
            UPDATE employee_directory SET
            emp_code=%s, full_name=%s, email=%s, phone=%s,
            department=%s, location=%s, join_date=%s, status=%s, last_updated=NOW()
            WHERE emp_id=%s
        """, (
            emp.emp_code, emp.full_name, emp.email, emp.phone,
            emp.department, emp.location, emp.join_date, emp.status, emp_id
        ))
        conn.commit()
    finally:
        cur.close()
        conn.close()

def delete_employee(emp_id):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM employee_directory WHERE emp_id=%s", (emp_id,))
        conn.commit()
        if cur.rowcount == 0:
            raise RecordNotFoundException("Employee not found")
    finally:
        cur.close()
        conn.close()

def list_employees(status=None):
    conn = get_conn()
    cur = conn.cursor()
    try:
        if status:
            cur.execute("SELECT * FROM employee_directory WHERE status=%s", (status,))
        else:
            cur.execute("SELECT * FROM employee_directory")
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()

def get_employee(emp_id):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM employee_directory WHERE emp_id=%s", (emp_id,))
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()

def update_status(emp_id, status):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("UPDATE employee_directory SET status=%s, last_updated=NOW() WHERE emp_id=%s",
                    (status, emp_id))
        conn.commit()
        if cur.rowcount == 0:
            raise RecordNotFoundException("Employee not found")
    finally:
        cur.close()
        conn.close()

def search_employees(keyword):
    conn = get_conn()
    cur = conn.cursor()
    try:
        like = f"%{keyword}%"
        cur.execute("""
            SELECT * FROM employee_directory
            WHERE full_name LIKE %s OR email LIKE %s OR department LIKE %s
        """, (like, like, like))
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()

def count_employees():
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT COUNT(*) AS total FROM employee_directory")
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()
