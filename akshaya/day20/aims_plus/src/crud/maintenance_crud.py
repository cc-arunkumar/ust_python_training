from src.config.db_connection import get_connection
from src.models.maintenance_model import MaintenanceModel

# 1. Function to create a maintenance log in the database
def create_maintenance_db(log: MaintenanceModel):
    """
    Creates a new maintenance log entry in the 'maintenance_log' table.
    Returns True if the log is successfully created, otherwise False if there is a database connection issue.
    """
    conn = get_connection()
    if conn is None:
        return False  # Return False if the database connection fails
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
        conn.commit()  # Commit the transaction to save the log
    conn.close()  # Close the database connection
    return True  # Return True to indicate success

# 2. Function to get all maintenance logs from the database
def get_all_maintenance_db():
    """
    Retrieves all maintenance log records from the 'maintenance_log' table.
    Returns a list of all maintenance logs or None if the database connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None  # Return None if the database connection fails
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM maintenance_log")
        result = cursor.fetchall()  # Fetch all maintenance logs
    conn.close()  # Close the database connection
    return result  # Return the list of maintenance logs

# 3. Function to list maintenance logs by their status
def list_maintenance_by_status_db(status: str):
    """
    Retrieves maintenance log records filtered by the given status.
    Returns the list of logs with the specified status, or None if the database connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None  # Return None if the database connection fails
    with conn.cursor() as cursor:
        # Perform a case-insensitive search for maintenance logs with the given status
        sql = "SELECT * FROM maintenance_log WHERE LOWER(status) = LOWER(%s)"
        cursor.execute(sql, (status,))
        result = cursor.fetchall()  # Fetch all logs with the specified status
    conn.close()  # Close the database connection
    return result  # Return the list of logs with the specified status

# 4. Function to get a specific maintenance log by its ID
def get_maintenance_by_id_db(log_id: int):
    """
    Retrieves a maintenance log record by its log ID.
    Returns the log record or None if the log is not found or if there is a database connection failure.
    """
    conn = get_connection()
    if conn is None:
        return None  # Return None if the database connection fails
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM maintenance_log WHERE log_id = %s", (log_id,))
        result = cursor.fetchone()  # Fetch the log with the specified ID
    conn.close()  # Close the database connection
    return result  # Return the log record

# 5. Function to update an existing maintenance log
def update_maintenance_db(log_id: int, log: MaintenanceModel):
    """
    Updates an existing maintenance log in the 'maintenance_log' table.
    Returns True if the log is successfully updated, False if there is a database issue.
    """
    conn = get_connection()
    if conn is None:
        return False  # Return False if the database connection fails
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
        conn.commit()  # Commit the transaction
        updated = cursor.rowcount  # Check how many rows were updated
    conn.close()  # Close the database connection
    return updated > 0  # Return True if one or more rows were updated, otherwise False

# 6. Function to update the status of a maintenance log
def update_maintenance_status_db(log_id: int, status: str):
    """
    Updates only the status of an existing maintenance log.
    Returns True if the status was updated, False if no rows were affected (i.e., log not found).
    """
    conn = get_connection()
    if conn is None:
        return False  # Return False if the database connection fails
    with conn.cursor() as cursor:
        cursor.execute("UPDATE maintenance_log SET status = %s WHERE log_id = %s",
                       (status, log_id))
        conn.commit()  # Commit the transaction
        updated = cursor.rowcount  # Check how many rows were affected
    conn.close()  # Close the database connection
    return updated > 0  # Return True if one or more rows were updated, otherwise False

# 7. Function to delete a maintenance log by its ID
def delete_maintenance_db(log_id: int):
    """
    Deletes a maintenance log from the 'maintenance_log' table by the given log ID.
    Returns True if the log was deleted, False if the log was not found or there was a connection issue.
    """
    conn = get_connection()
    if conn is None:
        return False  # Return False if the database connection fails
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM maintenance_log WHERE log_id = %s", (log_id,))
        deleted = cursor.rowcount  # Check how many rows were deleted
        conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection
    return deleted > 0  # Return True if one or more rows were deleted, otherwise False

# 8. Function to search maintenance logs by a keyword and value
def search_maintenance_db(keyword: str, value: str):
    """
    Searches for maintenance logs based on a keyword and value in the 'maintenance_log' table.
    Supports exact match for numeric fields and LIKE search for string fields.
    Returns the search results or an empty list if no results are found.
    """
    conn = get_connection()
    if conn is None:
        return None  # Return None if the database connection fails
    with conn.cursor() as cursor:
        allowed_columns = ["log_id", "asset_tag", "maintenance_type", "vendor_name",
                           "description", "cost", "maintenance_date", "technician_name", "status"]
        if keyword not in allowed_columns:
            return []  # Return an empty list if the keyword is invalid

        # Perform exact match for numeric fields
        if keyword in ["log_id", "cost"]:
            sql = f"SELECT * FROM maintenance_log WHERE {keyword} = %s"
            cursor.execute(sql, (value,))
        else:
            like = f"%{value}%"  # Prepare the value for LIKE query
            sql = f"SELECT * FROM maintenance_log WHERE {keyword} LIKE %s"
            cursor.execute(sql, (like,))

        result = cursor.fetchall()  # Fetch all matching records
    conn.close()  # Close the database connection
    return result  # Return the search results

# 9. Function to count the total number of maintenance logs
def count_maintenance_db():
    """
    Returns the total count of maintenance logs in the 'maintenance_log' table.
    Returns 0 if no logs are found or there is a database connection issue.
    """
    conn = get_connection()
    if conn is None:
        return None  # Return None if the database connection fails
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS total FROM maintenance_log")
        result = cursor.fetchone()  # Fetch the total count of maintenance logs
    conn.close()  # Close the database connection
    return result["total"] if result else 0  # Return the total count, or 0 if no result
