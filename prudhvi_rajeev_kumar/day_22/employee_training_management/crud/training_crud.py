from config.db_connection import get_connection
from models.training_model import TrainingRequest
import datetime

def create_request(req : TrainingRequest):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO training_requests
            (employee_id, employee_name, training_title,training_description, request_date, status, manager_id, last_updated)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            cursor.execute(sql, (req.employee_id, req.employee_name, req.training_title,
                                 req.training_description, datetime.datetime.now().strftime("%Y-%m-%d"), req.status, req.manager_id,
                                 datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            conn.commit()
            return cursor.lastrowid
    finally:
        conn.close()
        
def get_all_requests():
    conn = get_connection()
    try:
        with conn.cursor() as cursor: 
            cursor.execute("SELECT * FROM training_requests")
            return cursor.fetchall()
    finally:
        conn.close()
        
def get_req_by_id(id: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM training_requests WHERE id=%s", (id,))
            return cursor.fetchone()
    finally:
        conn.close()

def update_requests(id: int, new_req: TrainingRequest):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
            UPDATE training_requests
            SET employee_id=%s, employee_name=%s, training_title=%s, training_description=%s, request_date=%s,
                status=%s, manager_id=%s, last_updated=%s
            WHERE id=%s
            """
            cursor.execute(sql, (
                new_req.employee_id,
                new_req.employee_name,
                new_req.training_title,
                new_req.training_description,
                new_req.request_date.strftime("%Y-%m-%d"),
                new_req.status.value,
                new_req.manager_id,
                new_req.last_updated or datetime.now(),
                id
            ))
            conn.commit()
            return cursor.rowcount
    finally:
        conn.close()

        
def delete_request(id: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM training_requests WHERE id=%s", (id,))
            conn.commit()
            return cursor.rowcount
    finally:
        conn.close()
