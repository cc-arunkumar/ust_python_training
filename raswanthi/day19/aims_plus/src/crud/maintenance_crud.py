from src.config.db_connection import get_connection   # Import function to establish DB connection
from src.models.maintenance_model import MaintenanceLog   # Import MaintenanceLog model definition


# ------------------- CREATE -------------------
def create_maintenance_db(log: MaintenanceLog):
    """
    Insert a new maintenance log record into the database.
    - Accepts a MaintenanceLog object.
    - Returns True if insertion is successful, None if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    
    # The cursor object is opened when you enter the 'with' block 
    # and automatically closed when you exit it — even if an exception occurs.
    #context manager
    with conn.cursor() as cursor:
        sql = """INSERT INTO maintenance_log 
                 (asset_tag, maintenance_type, vendor_name, description,
                  cost, maintenance_date, technician_name, status)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (
            log.asset_tag,
            log.maintenance_type,
            log.vendor_name,
            log.description,
            log.cost,
            log.maintenance_date,
            log.technician_name,
            log.status
        ))
        conn.commit()  # Commit transaction
        
    conn.close()
    return True


# ------------------- READ ALL -------------------
def get_all_maintenance_db():
    """
    Retrieve all maintenance logs from the database.
    - Returns list of logs or None if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM maintenance_log")
        result = cursor.fetchall()
    
    conn.close()
    return result


# ------------------- LIST BY STATUS -------------------
def list_maintenance_by_status_db(status: str):
    """
    Retrieve all maintenance logs filtered by status (case-insensitive).
    - Returns list of logs or None if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    
    with conn.cursor() as cursor:
        sql = "SELECT * FROM maintenance_log WHERE LOWER(status) = LOWER(%s)"
        cursor.execute(sql, (status,))
        result = cursor.fetchall()
    
    conn.close()
    return result


# ------------------- READ BY ID -------------------
def get_maintenance_by_id_db(log_id: int):
    """
    Retrieve a single maintenance log by ID.
    - Returns log record or None if not found/DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM maintenance_log WHERE log_id = %s", (log_id,))
        result = cursor.fetchone()
    conn.close()
    return result


# ------------------- UPDATE -------------------
def update_maintenance_db(log_id: int, log: MaintenanceLog):
    """
    Update an existing maintenance log record by ID.
    - Accepts MaintenanceLog object with updated fields.
    - Returns True if update is successful, False if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return False
    with conn.cursor() as cursor:
        sql = """UPDATE maintenance_log 
                 SET asset_tag=%s, maintenance_type=%s, vendor_name=%s, description=%s,
                     cost=%s, maintenance_date=%s, technician_name=%s, status=%s
                 WHERE log_id=%s"""
        cursor.execute(sql, (
            log.asset_tag,
            log.maintenance_type,
            log.vendor_name,
            log.description,
            log.cost,
            log.maintenance_date,
            log.technician_name,
            log.status,
            log_id
        ))
        conn.commit()
        updated = cursor.rowcount  # Number of rows updated
    conn.close()
    return updated > 0


# ------------------- UPDATE STATUS -------------------
def update_maintenance_status_db(log_id: int, status: str):
    """
    Update only the status of a maintenance log by ID.
    - Returns True if update is successful, False if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return False
    with conn.cursor() as cursor:
        cursor.execute("UPDATE maintenance_log SET status = %s WHERE log_id = %s",
                       (status, log_id))
        conn.commit()
        updated = cursor.rowcount
    conn.close()
    return updated > 0


# ------------------- DELETE -------------------
def delete_maintenance_db(log_id: int):
    """
    Delete a maintenance log record by ID.
    - Returns True if deletion is successful, False if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return False
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM maintenance_log WHERE log_id = %s", (log_id,))
        deleted = cursor.rowcount  # Number of rows deleted
        conn.commit()
    conn.close()
    return deleted > 0


# ------------------- SEARCH -------------------
def search_maintenance_db(keyword: str, value: str):
    """
    Search maintenance logs dynamically by a given column (keyword) and value.
    - Uses LIKE for partial matches, exact match for numeric fields.
    - Only allows specific safe columns to prevent SQL injection.
    - Returns list of matching logs or empty list if keyword invalid.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        allowed_columns = ["log_id", "asset_tag", "maintenance_type", "vendor_name",
                           "description", "cost", "maintenance_date", "technician_name", "status"]
        # Validate keyword to prevent SQL injection
        if keyword not in allowed_columns:
            return []

        # Exact match for numeric fields
        if keyword in ["log_id", "cost"]:
            sql = f"SELECT * FROM maintenance_log WHERE {keyword} = %s"
            cursor.execute(sql, (value,))
        else:
            like = f"%{value}%"
            sql = f"SELECT * FROM maintenance_log WHERE {keyword} LIKE %s"
            cursor.execute(sql, (like,))

        result = cursor.fetchall()
    conn.close()
    return result


# ------------------- COUNT -------------------
def count_maintenance_db():
    """
    Count total number of maintenance logs in the database.
    - Returns integer count or None if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM maintenance_log")
        result = cursor.fetchone()
    conn.close()
    return result
