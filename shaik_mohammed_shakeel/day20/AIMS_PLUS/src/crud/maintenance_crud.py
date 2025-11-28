import csv
from typing import Optional

from fastapi import HTTPException
from src.config.db_connection import get_connection
from src.models.maintenance_model import MaintenanceLogModel



# Fetch all maintenance logs, with an optional status filter
def get_all(status_filter: Optional[str] = ""):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        if status_filter == "":
            cursor.execute("SELECT * FROM ust_aims_db.maintenance_log")
        else:
            cursor.execute("SELECT * FROM ust_aims_db.maintenance_log WHERE status = %s", (status_filter,))
        
        row = cursor.fetchall()
        return row if row else None
    except Exception as e:
        raise ValueError(f"Error fetching maintenance logs: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()


# Fetch a maintenance log by its log_id
def get_by_id(log_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM ust_aims_db.maintenance_log WHERE log_id = %s", (log_id,))
        row = cursor.fetchone()
        
        return row if row else None
    except Exception as e:
        raise ValueError(f"Error fetching maintenance log with ID {log_id}: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()


# Insert a new maintenance log entry
def insert_maintenance_log(updated_log):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            """
            INSERT INTO ust_aims_db.maintenance_log (
                asset_tag, maintenance_type, vendor_name, description, cost,
                maintenance_date, technician_name, status
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                updated_log.asset_tag,           # asset_tag
                updated_log.maintenance_type,    # maintenance_type
                updated_log.vendor_name,         # vendor_name
                updated_log.description,         # description
                updated_log.cost,                # cost
                updated_log.maintenance_date,    # maintenance_date
                updated_log.technician_name,     # technician_name
                updated_log.status               # status
            )
        )
        conn.commit()
        
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        if conn:
            cursor.close()
            conn.close()


# Update a maintenance log entry by log_id
def update_maintenance_log_by_id(log_id: int, updated_log:MaintenanceLogModel):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if the maintenance log exists
        existing_log = get_by_id(log_id)
        if not existing_log:
            raise HTTPException(status_code=404, detail=f"Maintenance log with ID {log_id} not found.")
        
        # Proceed with the update
        cursor.execute("""
        UPDATE ust_aims_db.maintenance_log 
        SET 
            asset_tag = %s,
            maintenance_type = %s,
            vendor_name = %s,
            description = %s,
            cost = %s,
            maintenance_date = %s,
            technician_name = %s,
            status = %s
        WHERE log_id = %s
        """, (
            updated_log.asset_tag,           # asset_tag
            updated_log.maintenance_type,    # maintenance_type
            updated_log.vendor_name,         # vendor_name
            updated_log.description,         # description
            updated_log.cost,                # cost
            updated_log.maintenance_date,    # maintenance_date
            updated_log.technician_name,     # technician_name
            updated_log.status,              # status
            log_id
        ))
        
        conn.commit()
        return updated_log  
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating maintenance log: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()


# Delete a maintenance log entry by log_id
def delete_maintenance_log(log_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        if get_by_id(log_id):
            cursor.execute("DELETE FROM ust_aims_db.maintenance_log WHERE log_id = %s", (log_id,))
            conn.commit()
            return True
        else:
            raise ValueError("Log ID not found")
        
    except Exception as e:
        raise ValueError(f"Error deleting maintenance log: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()


# Search for maintenance logs based on a field and keyword (e.g., searching by vendor name or technician)
def search_maintenance_log(field_type: str, keyword: str):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Dynamically search based on field type (e.g., 'vendor_name', 'technician_name', etc.)
        cursor.execute(f"SELECT * FROM ust_aims_db.maintenance_log WHERE {field_type} LIKE %s", (f'%{keyword}%',))
        data = cursor.fetchall()
        return data if data else None

    except Exception as e:
        raise Exception(f"Error: {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()



