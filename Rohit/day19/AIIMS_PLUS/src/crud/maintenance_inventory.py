import pymysql  # Import pymysql to connect and interact with MySQL databases
from fastapi import FastAPI, HTTPException  # Import FastAPI framework and HTTPException for API error handling
from config.db_connection import get_connection  # Import custom function to establish DB connection

# Initialize FastAPI app instance
app = FastAPI()

# -----------------------------
# CREATE MAINTENANCE RECORD
# -----------------------------
def create_maintenance(log):
    """
    Insert a new maintenance record into the maintenance_log table.
    Accepts a Pydantic model or object 'log' containing maintenance details.
    """
    conn = None  # Initialize connection variable
    cursor = None  # Initialize cursor variable
    try:
        conn = get_connection()  # Establish DB connection
        cursor = conn.cursor()   # Create cursor object for executing SQL queries

        # SQL query for inserting new maintenance record
        sql = """
        INSERT INTO maintenance_log (
            log_id, asset_tag, maintenance_type, vendor_name,
            description, cost, maintenance_date, technician_name, status
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        # Values tuple extracted from log object
        values = (
            log.log_id,
            log.asset_tag,
            log.maintenance_type.value,  # Enum value converted to string
            log.vendor_name,
            log.description,
            log.cost,
            log.maintenance_date,
            log.technician_name,
            log.status.value,  # Enum value converted to string
        )

        cursor.execute(sql, values)  # Execute insert query
        conn.commit()  # Commit transaction to save changes

        # Return success message with log_id
        return {"message": "Maintenance record created successfully", "log_id": log.log_id}

    except Exception as e:
        if conn: conn.rollback()  # Rollback transaction if error occurs
        raise HTTPException(status_code=500, detail=f"Error creating maintenance record: {str(e)}")
    finally:
        if cursor: cursor.close()  # Close cursor safely
        if conn: conn.close()      # Close connection safely


# -----------------------------
# LIST ALL MAINTENANCE RECORDS
# -----------------------------
def list_maintenance():
    """
    Fetch all maintenance records from maintenance_log table.
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)  # DictCursor returns rows as dictionaries
        cursor.execute("SELECT * FROM maintenance_log")  # Query all records
        return cursor.fetchall()  # Return list of dicts
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching maintenance records: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# -----------------------------
# LIST MAINTENANCE RECORDS BY STATUS
# -----------------------------
def list_maintenance_by_status(status: str):
    """
    Fetch maintenance records filtered by status (e.g., Completed, Pending).
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM maintenance_log WHERE status=%s", (status,))
        return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching maintenance records: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# -----------------------------
# GET MAINTENANCE RECORD BY ID
# -----------------------------
def get_maintenance_by_id(log_id: int):
    """
    Fetch a single maintenance record by log_id.
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM maintenance_log WHERE log_id=%s", (log_id,))
        row = cursor.fetchone()  # Fetch single record
        if not row:  # If no record found
            raise HTTPException(status_code=404, detail=f"Maintenance record with id {log_id} not found")
        return row
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching maintenance record: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# -----------------------------
# UPDATE FULL MAINTENANCE RECORD
# -----------------------------
def update_maintenance(log_id: int, row: dict):
    """
    Update all fields of a maintenance record by log_id.
    Accepts a dictionary 'row' containing updated values.
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # SQL query to update maintenance record
        sql = """
        UPDATE maintenance_log
        SET asset_tag=%s, maintenance_type=%s, vendor_name=%s,
            description=%s, cost=%s, maintenance_date=%s,
            technician_name=%s, status=%s
        WHERE log_id=%s
        """

        # Values tuple for update query
        values = (
            row["asset_tag"],
            row["maintenance_type"],
            row["vendor_name"],
            row["description"],
            row["cost"],
            row["maintenance_date"],
            row["technician_name"],
            row["status"],
            log_id,
        )

        cursor.execute(sql, values)  # Execute update query
        conn.commit()  # Commit changes

        if cursor.rowcount == 0:  # If no rows updated
            raise HTTPException(status_code=404, detail=f"Maintenance record with id {log_id} not found")

        return {"message": "Maintenance record updated successfully", "log_id": log_id}

    except Exception as e:
        if conn: conn.rollback()  # Rollback if error occurs
        raise HTTPException(status_code=500, detail=f"Error updating maintenance record: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# -----------------------------
# UPDATE MAINTENANCE STATUS ONLY
# -----------------------------
def update_maintenance_status(log_id: int, status: str):
    """
    Update only the status field of a maintenance record.
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Update query for status
        cursor.execute("UPDATE maintenance_log SET status=%s WHERE log_id=%s", (status, log_id))
        conn.commit()

        if cursor.rowcount == 0:  # If no rows updated
            raise HTTPException(status_code=404, detail=f"Maintenance record with id {log_id} not found")

        return {"message": "Maintenance status updated successfully", "log_id": log_id, "status": status}

    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating maintenance status: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# -----------------------------
# DELETE MAINTENANCE RECORD
# -----------------------------
def delete_maintenance(log_id: int):
    """
    Delete a maintenance record by log_id.
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Delete query
        cursor.execute("DELETE FROM maintenance_log WHERE log_id=%s", (log_id,))
        conn.commit()

        if cursor.rowcount == 0:  # If no rows deleted
            raise HTTPException(status_code=404, detail=f"Maintenance record with id {log_id} not found")

        return {"message": "Maintenance record deleted successfully", "log_id": log_id}

    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting maintenance record: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
