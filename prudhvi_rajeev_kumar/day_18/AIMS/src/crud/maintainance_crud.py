from src.config.db_connection import get_connection
from src.models.maintainance_model import MaintenanceLog

# CREATE
def create_log(log: MaintenanceLog):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO maintenance_log
            (asset_tag, maintenance_type, vendor_name, description,
             cost, maintenance_date, technician_name, status)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """
            cursor.execute(sql, (
                log.asset_tag, log.maintenance_type, log.vendor_name,
                log.description, log.cost, log.maintenance_date,
                log.technician_name, log.status
            ))
            conn.commit()
            return cursor.lastrowid
    finally:
        conn.close()

# READ
def get_log_by_id(log_id: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM maintenance_log WHERE log_id=%s", (log_id,))
            return cursor.fetchone()
    finally:
        conn.close()

def get_all_logs():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM maintenance_log")
            return cursor.fetchall()
    finally:
        conn.close()

# UPDATE
def update_log_status(log_id: int, new_status: str):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE maintenance_log SET status=%s WHERE log_id=%s",
                           (new_status, log_id))
            conn.commit()
            return cursor.rowcount
    finally:
        conn.close()

# DELETE
def delete_log(log_id: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM maintenance_log WHERE log_id=%s", (log_id,))
            conn.commit()
            return cursor.rowcount
    finally:
        conn.close()
