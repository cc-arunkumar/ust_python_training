import csv
from typing import Optional

from fastapi import HTTPException
from src.config.db_connection import get_connection
from src.models.maintenance_model import MaintenanceLogModel


# Fetch all maintenance logs, with an optional status filter
def get_all(status_filter: Optional[str] = ""):
    try:
        # Establish a connection to the database and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # If no status filter is provided, fetch all maintenance logs
        if status_filter == "":
            cursor.execute("SELECT * FROM ust_aims_db.maintenance_log")
        else:
            cursor.execute("SELECT * FROM ust_aims_db.maintenance_log WHERE status = %s", (status_filter,))
        
        # Fetch all rows matching the query
        row = cursor.fetchall()
        return row if row else None  # Return the rows or None if no data is found
    except Exception as e:
        # Raise an error if the query execution fails
        raise ValueError(f"Error fetching maintenance logs: {str(e)}")
    finally:
        # Close the database connection and cursor
        if conn:
            cursor.close()
            conn.close()


# Fetch a maintenance log by its log_id
def get_by_id(log_id):
    try:
        # Establish a connection to the database and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # Execute a query to fetch the maintenance log by ID
        cursor.execute("SELECT * FROM ust_aims_db.maintenance_log WHERE log_id = %s", (log_id,))
        row = cursor.fetchone()
        
        return row if row else None  # Return the maintenance log data if found, or None if not
    except Exception as e:
        # Raise an error if the query execution fails
        raise ValueError(f"Error fetching maintenance log with ID {log_id}: {str(e)}")
    finally:
        # Close the database connection and cursor
        if conn:
            cursor.close()
            conn.close()


# Insert a new maintenance log entry into the database
def insert_maintenance_log(updated_log):
    try:
        # Establish a connection to the database and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # Execute the insert query to add a new maintenance log
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
        # Commit the transaction to insert the log into the database
        conn.commit()
        
    except Exception as e:
        # Print an error message if something goes wrong during insertion
        print(f"Error: {e}")
        
    finally:
        # Close the database connection and cursor
        if conn:
            cursor.close()
            conn.close()


# Update a maintenance log entry by log_id
def update_maintenance_log_by_id(log_id: int, updated_log: MaintenanceLogModel):
    try:
        # Establish a connection to the database and create a cursor
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
        
        # Commit the transaction to update the maintenance log in the database
        conn.commit()
        return updated_log  # Return the updated maintenance log
    
    except Exception as e:
        # Raise an HTTP exception if an error occurs during the update
        raise HTTPException(status_code=500, detail=f"Error updating maintenance log: {str(e)}")
    finally:
        # Close the database connection and cursor
        if conn:
            cursor.close()
            conn.close()


# Delete a maintenance log entry by log_id
def delete_maintenance_log(log_id):
    try:
        # Establish a connection to the database and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if the maintenance log exists
        if get_by_id(log_id):
            # Execute a query to delete the maintenance log from the database
            cursor.execute("DELETE FROM ust_aims_db.maintenance_log WHERE log_id = %s", (log_id,))
            # Commit the transaction to delete the log
            conn.commit()
            return True  # Return True if deletion was successful
        else:
            raise ValueError("Log ID not found")  # Raise an error if the log ID is not found
        
    except Exception as e:
        # Raise an error if deletion fails
        raise ValueError(f"Error deleting maintenance log: {str(e)}")
    finally:
        # Close the database connection and cursor
        if conn:
            cursor.close()
            conn.close()


# Search for maintenance logs based on a field and keyword (e.g., searching by vendor name or technician)
def search_maintenance_log(field_type: str, keyword: str):
    try:
        # Establish a connection to the database and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # Dynamically search based on field type (e.g., 'vendor_name', 'technician_name', etc.)
        cursor.execute(f"SELECT * FROM ust_aims_db.maintenance_log WHERE {field_type} LIKE %s", (f'%{keyword}%',))
        data = cursor.fetchall()  # Fetch all matching records
        return data if data else None  # Return the search results if found, or None if not

    except Exception as e:
        # Raise an error if the query execution fails
        raise Exception(f"Error: {e}")
    
    finally:
        # Close the database connection and cursor
        if conn:
            cursor.close()
            conn.close()




# The following block of code is commented out, it is for bulk insertion of data from a CSV file.
# It checks for missing required fields, validates the data, and writes valid/invalid rows to separate CSV files.

# query = """
# INSERT INTO ust_aims_db.maintenance_log (
#     asset_tag, maintenance_type, vendor_name, description, cost, maintenance_date, technician_name, status
# ) VALUES (
#     %s, %s, %s, %s, %s, %s, %s, %s
# )
# """

# try:
#     conn = get_connection()
#     cursor = conn.cursor()

#     # Open the CSV file that contains maintenance log data
#     with open("valid_rows_maintain.csv", "r", encoding="utf-8") as file:
#         reader = csv.DictReader(file)

#         for row in reader:
#             if 'asset_tag' not in row or 'maintenance_type' not in row or 'vendor_name' not in row:
#                 print(f"Missing required column(s) in row: {row}")
#                 continue  

#             data = (
#                 row["asset_tag"],          
#                 row["maintenance_type"],   # maintenance_type
#                 row["vendor_name"],        # vendor_name
#                 row["description"],        # description
#                 row["cost"],               # cost
#                 row["maintenance_date"],   # maintenance_date
#                 row["technician_name"],    # technician_name
#                 row["status"]              # status
#             )

#             cursor.execute(query, data)
    
#     conn.commit()

# except Exception as e:
#     print(f"Error: {e}")

# finally:
#     if conn:
#         cursor.close()
#         conn.close()


# Code for handling CSV validation is commented out below, but it validates rows of data for correctness.
# Valid rows are written to a "valid_rows_maintain.csv" file, while invalid rows (with errors) are written
# to "invalid_rows_maintain.csv".

# valid_rows_maintain = []
# invalid_rows_maintain = []

# required_fields_maintain = [
#     "log_id",
#     "asset_tag",
#     "maintenance_type",
#     "vendor_name",
#     "description",
#     "cost",
#     "maintenance_date",
#     "technician_name",
#     "status"]
