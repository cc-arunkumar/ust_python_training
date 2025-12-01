from db_connection import get_connection
from models import Employee

def create_training_request(employee: Employee):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO training_requests 
        (employee_id, employee_name, training_title, training_description, requested_date, status, manager_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        employee.employee_id,
        employee.employee_name,
        employee.training_title,
        employee.training_description,
        employee.requested_date,
        employee.status,
        employee.manager_id
    ))
    conn.commit()
    conn.close()
    return employee

def get_all_training_requests():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM training_requests")
    results = cursor.fetchall()
    conn.close()
    return results

def get_training_request_by_id(emp_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM training_requests WHERE employee_id=%s", (emp_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def update_training_request(id: int, employee: Employee):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        UPDATE training_requests
        SET employee_id=%s, employee_name=%s, training_title=%s, training_description=%s,
            requested_date=%s, status=%s, manager_id=%s
        WHERE id=%s
    """
    cursor.execute(query, (
        employee.employee_id,
        employee.employee_name,
        employee.training_title,
        employee.training_description,
        employee.requested_date,
        employee.status,
        employee.manager_id,
        id
    ))
    conn.commit()
    conn.close()
    return employee

def delete_training_request(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM training_requests WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return {"deleted_id": id}
