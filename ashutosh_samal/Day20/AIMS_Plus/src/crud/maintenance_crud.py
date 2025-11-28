import pymysql
from typing import List, Optional
from ..model.maintenance_model import MaintenanceCreate

def get_db_connection():
    # Establish a connection to the MySQL database
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db",  
    )


# Fetch maintenance logs from the database, optionally filtering by status
def fetch_maintenance_logs(status: Optional[str] = None):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        if status:
            cursor.execute("SELECT * FROM maintenance_log WHERE status = %s", (status,))  # Filter by status
        else:
            cursor.execute("SELECT * FROM maintenance_log")  # Fetch all logs
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


# Fetch a specific maintenance log by its ID
def fetch_maintenance_by_id(maintenance_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM maintenance_log WHERE log_id = %s", (maintenance_id,))  # Fetch log by ID
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()


# Create a new maintenance log entry in the database
def create_new_maintenance_log(log: MaintenanceCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO maintenance_log (asset_tag, maintenance_type, vendor_name, description, cost, 
            maintenance_date, technician_name, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                log.asset_tag,
                log.maintenance_type,
                log.vendor_name,
                log.description,
                log.cost,
                log.maintenance_date,
                log.technician_name,
                log.status
            )
        )
        conn.commit()  # Commit the transaction
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()


# Update an existing maintenance log in the database
def modify_maintenance_log(maintenance_id: int, log: MaintenanceCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            UPDATE maintenance_log 
            SET asset_tag = %s, maintenance_type = %s, vendor_name = %s, description = %s, cost = %s, 
                maintenance_date = %s, technician_name = %s, status = %s
            WHERE log_id = %s
            """, (
                log.asset_tag,
                log.maintenance_type,
                log.vendor_name,
                log.description,
                log.cost,
                log.maintenance_date,
                log.technician_name,
                log.status,
                maintenance_id
            )
        )
        conn.commit()  # Commit the transaction
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()


# Modify the status of an existing maintenance log
def modify_maintenance_status(maintenance_id: int, status: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE maintenance_log SET status = %s WHERE log_id = %s", (status, maintenance_id)  # Update status
        )
        conn.commit()  # Commit the transaction
    except Exception as e:
        conn.rollback()  # Rollback the transaction in case of error
        raise e
    finally:
        cursor.close()
        conn.close()


# Delete a maintenance log by its ID
def remove_maintenance_log(maintenance_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM maintenance_log WHERE log_id = %s", (maintenance_id,))  # Delete log by ID
        conn.commit()  # Commit the transaction
    except Exception as e:
        conn.rollback()  # Rollback the transaction in case of error
        raise e
    finally:
        cursor.close()
        conn.close()


# Search maintenance logs based on a keyword in description, vendor name, or technician name
def search_maintenance_logs(keyword: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = """
        SELECT * FROM maintenance_log WHERE 
        description LIKE %s OR 
        vendor_name LIKE %s OR 
        technician_name LIKE %s
        """
        like_keyword = f"%{keyword}%"
        cursor.execute(query, (like_keyword, like_keyword, like_keyword))  # Search with LIKE query
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


# Get the total number of maintenance logs in the database
def get_total_maintenance_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM maintenance_log")  # Count the logs
        return cursor.fetchone()[0]
    finally:
        cursor.close()
        conn.close()
