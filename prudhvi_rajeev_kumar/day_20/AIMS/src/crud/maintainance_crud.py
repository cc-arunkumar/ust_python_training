# Import necessary modules: Database connection utility and MaintenanceLog model
from src.config.db_connection import get_connection
from src.models.maintainance_model import MaintenanceLog

# CREATE: Insert a new maintenance log into the database
def create_log(log: MaintenanceLog):
    # Establish a connection to the database
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # SQL query to insert a new maintenance log
            sql = """
            INSERT INTO maintenance_log
            (asset_tag, maintenance_type, vendor_name, description,
             cost, maintenance_date, technician_name, status)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """
            # Execute the query with the log data
            cursor.execute(sql, (
                log.asset_tag, log.maintenance_type, log.vendor_name,
                log.description, log.cost, log.maintenance_date,
                log.technician_name, log.status
            ))
            # Commit the transaction
            conn.commit()
            # Return the ID of the newly created log
            return cursor.lastrowid
    finally:
        # Ensure the connection is closed
        conn.close()

# READ: Get a maintenance log by its ID
def get_log_by_id(log_id: int):
    # Establish a connection to the database
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Execute the query to fetch the log by ID
            cursor.execute("SELECT * FROM maintenance_log WHERE log_id=%s", (log_id,))
            # Return the result (single log)
            return cursor.fetchone()
    finally:
        # Ensure the connection is closed
        conn.close()

# UPDATE: Update an existing maintenance log
def update_log(log_id: int, maintenance: MaintenanceLog):
    # Establish a connection to the database
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # SQL query to update the maintenance log details
            sql = """
            UPDATE maintenance_log
            SET asset_tag=%s, maintenance_type=%s, vendor_name=%s, description=%s,
                cost=%s, maintenance_date=%s, technician_name=%s, status=%s
            WHERE log_id=%s
            """
            # Execute the query to update the log
            cursor.execute(sql, (
                maintenance.asset_tag, maintenance.maintenance_type, maintenance.vendor_name,
                maintenance.description, maintenance.cost, maintenance.maintenance_date,
                maintenance.technician_name, maintenance.status, log_id
            ))
            # Commit the transaction
            conn.commit()
            # Return the number of affected rows
            return cursor.rowcount
    finally:
        # Ensure the connection is closed
        conn.close()

# UPDATE: Update the status of a maintenance log
def update_asset_status(log_id: int, new_status: str):
    # Establish a connection to the database
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Execute the query to update the log status
            cursor.execute("UPDATE maintenance_log SET status=%s WHERE log_id=%s",
                           (new_status, log_id))
            # Commit the transaction
            conn.commit()
            # Return the number of affected rows
            return cursor.rowcount
    finally:
        # Ensure the connection is closed
        conn.close()

# READ: Get the total number of maintenance logs
def count_total():
    # Get all logs and return the count
    total = get_all_logs()
    return len(total)

# READ: Search for maintenance logs based on a column name and value
def search_assets(column_name: str, value: str):
    # Establish a connection to the database
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # List of allowed column names for searching
            allowed_columns = [
                "asset_tag", "maintenance_type", "vendor_name", "description",
                "cost", "maintenance_date", "technician_name", "status"
            ]
            # Check if the column name is valid
            if column_name not in allowed_columns:
                raise ValueError("Invalid Column name.")
            # Execute the search query based on the provided column name and value
            sql = f"SELECT * FROM maintenance_log WHERE {column_name} = %s"
            cursor.execute(sql, (value,))
            # Return all matching logs
            return cursor.fetchall()
    finally:
        # Ensure the connection is closed
        conn.close()

# READ: Get maintenance logs by status
def get_log_by_status(status: str):
    # Establish a connection to the database
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Execute the query to fetch logs with the given status
            cursor.execute("SELECT * FROM maintenance_log WHERE status = %s", (status,))
            # Return all matching logs
            return cursor.fetchall()
    finally:
        # Ensure the connection is closed
        conn.close()

# READ: Get all maintenance logs
def get_all_logs():
    # Establish a connection to the database
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Execute the query to fetch all logs
            cursor.execute("SELECT * FROM maintenance_log")
            # Return all logs
            return cursor.fetchall()
    finally:
        # Ensure the connection is closed
        conn.close()

# UPDATE: Update the status of a maintenance log
def update_log_status(log_id: int, new_status: str):
    # Establish a connection to the database
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Execute the query to update the log's status
            cursor.execute("UPDATE maintenance_log SET status=%s WHERE log_id=%s",
                           (new_status, log_id))
            # Commit the transaction
            conn.commit()
            # Return the number of affected rows
            return cursor.rowcount
    finally:
        # Ensure the connection is closed
        conn.close()

# DELETE: Delete a maintenance log by its ID
def delete_log(log_id: int):
    # Establish a connection to the database
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Execute the query to delete the log by ID
            cursor.execute("DELETE FROM maintenance_log WHERE log_id=%s", (log_id,))
            # Commit the transaction
            conn.commit()
            # Return the number of affected rows
            return cursor.rowcount
    finally:
        # Ensure the connection is closed
        conn.close()
