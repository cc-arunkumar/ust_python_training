import csv  # Importing the csv module to handle CSV file operations
from typing import Optional  # Importing Optional for optional type annotations

from fastapi import HTTPException  # Importing HTTPException for error handling in FastAPI
from src.config.db_connection import get_connection  # Importing the get_connection function to establish DB connection
from src.models.maintenance_model import MaintenanceLogModel  # Importing the MaintenanceLogModel for structured data handling

# Fetch all maintenance logs, with an optional status filter
def get_all(status_filter: Optional[str] = ""):
    """
    Retrieves all maintenance logs from the database.
    If a status filter is provided, only logs matching the status are retrieved.
    
    :param status_filter: Optional filter for the status (e.g., 'completed', 'pending')
    :return: List of maintenance logs or None if no logs are found
    """
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object to interact with the database
        
        # If no status filter is provided, fetch all maintenance logs; otherwise, fetch logs by status
        if status_filter == "":
            cursor.execute("SELECT * FROM ust_aims_db.maintenance_log")
        else:
            cursor.execute("SELECT * FROM ust_aims_db.maintenance_log WHERE status = %s", (status_filter,))
        
        row = cursor.fetchall()  # Fetch all results
        return row if row else None  # Return fetched rows or None if no data is found
    except Exception as e:
        raise ValueError(f"Error fetching maintenance logs: {str(e)}")  # Raise an error if fetching fails
    finally:
        if conn:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()

# Fetch a maintenance log by its log_id
def get_by_id(log_id):
    """
    Retrieves a single maintenance log by its log_id from the database.
    
    :param log_id: The ID of the maintenance log to fetch
    :return: Maintenance log data if found, None if not found
    """
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Execute the SQL query to fetch the maintenance log by its log_id
        cursor.execute("SELECT * FROM ust_aims_db.maintenance_log WHERE log_id = %s", (log_id,))
        row = cursor.fetchone()  # Fetch a single row
        
        return row if row else None  # Return the found log or None if not found
    except Exception as e:
        raise ValueError(f"Error fetching maintenance log with ID {log_id}: {str(e)}")  # Raise an error if fetching fails
    finally:
        if conn:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()

# Insert a new maintenance log entry
def insert_maintenance_log(updated_log):
    """
    Inserts a new maintenance log into the database.
    
    :param updated_log: The maintenance log data to insert into the database
    """
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Execute the SQL query to insert a new maintenance log entry into the database
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
        conn.commit()  # Commit the transaction to the database
        
    except Exception as e:
        print(f"Error: {e}")  # Print any errors that occur during insertion
        
    finally:
        if conn:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()

# Update a maintenance log entry by log_id
def update_maintenance_log_by_id(log_id: int, updated_log: MaintenanceLogModel):
    """
    Updates an existing maintenance log entry by its log_id.
    
    :param log_id: The ID of the maintenance log to update
    :param updated_log: The updated maintenance log data
    :return: The updated maintenance log data
    :raises HTTPException: If the log ID is not found
    """
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Check if the maintenance log exists before trying to update
        existing_log = get_by_id(log_id)
        if not existing_log:
            raise HTTPException(status_code=404, detail=f"Maintenance log with ID {log_id} not found.")
        
        # Execute the SQL query to update the maintenance log entry
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
            log_id                            # log_id
        ))
        
        conn.commit()  # Commit the transaction to the database
        return updated_log  # Return the updated maintenance log  
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating maintenance log: {str(e)}")  # Raise error if update fails
    finally:
        if conn:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()

# Delete a maintenance log entry by log_id
def delete_maintenance_log(log_id):
    """
    Deletes a maintenance log from the database by its log_id.
    
    :param log_id: The ID of the maintenance log to delete
    :return: True if the deletion was successful
    :raises ValueError: If the log ID is not found
    """
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Check if the maintenance log exists before attempting to delete
        if get_by_id(log_id):
            cursor.execute("DELETE FROM ust_aims_db.maintenance_log WHERE log_id = %s", (log_id,))
            conn.commit()  # Commit the deletion to the database
            return True  # Return True indicating the deletion was successful
        else:
            raise ValueError("Log ID not found")  # Raise an error if the log ID is not found
        
    except Exception as e:
        raise ValueError(f"Error deleting maintenance log: {str(e)}")  # Raise an error if deletion fails
    finally:
        if conn:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()

# Search for maintenance logs based on a field and keyword (e.g., searching by vendor name or technician)
def search_maintenance_log(field_type: str, keyword: str):
    """
    Searches for maintenance logs based on a field and a keyword.
    
    :param field_type: The field to search (e.g., 'vendor_name', 'technician_name', etc.)
    :param keyword: The keyword to search for in the specified field
    :return: List of maintenance logs matching the search criteria
    :raises Exception: If an error occurs during the search
    """
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Dynamically search based on the field type (e.g., 'vendor_name', 'technician_name', etc.)
        cursor.execute(f"SELECT * FROM ust_aims_db.maintenance_log WHERE {field_type} LIKE %s", (f'%{keyword}%',))
        data = cursor.fetchall()  # Fetch all matching results
        return data if data else None  # Return the search results or None if no matching data is found

    except Exception as e:
        raise Exception(f"Error: {e}")  # Raise an error if the search fails
    
    finally:
        if conn:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()
