from src.config import db_connection
from src.models import maintenance_model
from typing import Optional

# Function: Create a new maintenance log record in the database
def create_log(new_log: maintenance_model.MaintenanceLog):
    # Insert a new maintenance log into the maintenance_log table
    try: 
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO ust_inventory_db.maintenance_log (
                asset_tag, maintenance_type, vendor_name, description,
                cost, maintenance_date, technician_name, status
            ) VALUES (
                %s, %s, %s, %s,
                %s, %s, %s, %s
            )
        """
        # Prepare log data for insertion
        data = (
            new_log.asset_tag,
            new_log.maintenance_type,
            new_log.vendor_name,
            new_log.description,
            new_log.cost,
            new_log.maintenance_date,
            new_log.technician_name,
            new_log.status
        )

        cursor.execute(query, data)
        conn.commit()
        return True
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("Connection closed successfully")


# Function: Retrieve all maintenance logs, optionally filtered by status
def get_all_logs(status: Optional[str] = ""):
    # If status is empty, fetch all logs; otherwise filter by status
    try: 
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if status == "":
            cursor.execute("SELECT * FROM ust_inventory_db.maintenance_log")
            data = cursor.fetchall()
            return data
        else:
            cursor.execute("SELECT * FROM ust_inventory_db.maintenance_log WHERE status=%s", (status,))
            data = cursor.fetchall()
            return data
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Function: Retrieve a single maintenance log by ID
def get_log_by_id(log_id):
    # Query maintenance_log table for a specific log_id
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_inventory_db.maintenance_log WHERE log_id=%s", (log_id,))
        data = cursor.fetchone()
        if data:
            return data
        else:
            return False
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()    


# Function: Update an existing maintenance log by ID
def update_log_by_id(log_id: int, new_log: maintenance_model.MaintenanceLog):
    # Update maintenance log record if it exists
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if get_log_by_id(log_id):
            query = """
                UPDATE ust_inventory_db.maintenance_log
                SET asset_tag = %s,
                    maintenance_type = %s,
                    vendor_name = %s,
                    description = %s,
                    cost = %s,
                    maintenance_date = %s,
                    technician_name = %s,
                    status = %s
                WHERE log_id = %s
            """
            # Prepare updated log data
            data = (
                new_log.asset_tag,
                new_log.maintenance_type,
                new_log.vendor_name,
                new_log.description,
                new_log.cost,
                new_log.maintenance_date,
                new_log.technician_name,
                new_log.status,
                log_id
            )
            cursor.execute(query, data)
            conn.commit()
            return True
        else:
            return False
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Function: Delete a maintenance log by ID
def delete_log_by_id(log_id: int):
    # Remove maintenance log record if it exists
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if get_log_by_id(log_id):
            cursor.execute("DELETE FROM ust_inventory_db.maintenance_log WHERE log_id=%s", (log_id,))
            conn.commit()
            return True
        else:
            return False
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Function: Search maintenance logs by a given field and value
def search_by_tag_log(field, value):
    # Perform a LIKE query on the specified field
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        query = f"SELECT * FROM ust_inventory_db.maintenance_log WHERE {field} LIKE %s"
        cursor.execute(query, (f"%{value}%",))
        data = cursor.fetchall()
        return data
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()
