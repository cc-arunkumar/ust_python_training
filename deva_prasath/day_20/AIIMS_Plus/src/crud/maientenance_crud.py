import pymysql  # MySQL connector for database interaction
from typing import List, Optional  # Type hinting for List and Optional
from ..models.maientenance_model import MaintenanceCreate  # Importing MaintenanceCreate model from maintenance_model

# Function to establish a connection to the MySQL database
def get_db_connection():
    return pymysql.connect(
        host="localhost",  # Database host
        user="root",  # Database username
        password="pass@word1",  # Database password
        database="aiims",  # Database name
    )

# Function to get maintenance logs, optionally filtered by status
def get_maintenance_logs(status: Optional[str] = None):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor for database operations
    try:
        if status:  # If status filter is provided
            cursor.execute("select * FROM maintenance_log WHERE status = %s", (status,))
        else:  # No filter, return all maintenance logs
            cursor.execute("select * FROM maintenance_log")
        return cursor.fetchall()  # Return all fetched maintenance logs
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to get a specific maintenance log by its ID
def get_maintenance_by_id(maintenance_id: int):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute("select * FROM maintenance_log WHERE maintenance_id = %s", (maintenance_id,))
        return cursor.fetchone()  # Return the maintenance log data
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to create a new maintenance log in the database
def create_maintenance(ob: MaintenanceCreate):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute(
            """
            insert into maintenance_log (asset_tag, maintenance_type, vendor_name, description, cost, 
            maintenance_date, technician_name, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                ob.asset_tag,  # Asset tag
                ob.maintenance_type,  # Maintenance type
                ob.vendor_name,  # Vendor name
                ob.description,  # Description of maintenance
                ob.cost,  # Cost of maintenance
                ob.maintenance_date,  # Date of maintenance
                ob.technician_name,  # Technician's name
                ob.status  # Status of the maintenance
            )
        )
        conn.commit()  # Commit transaction
    except Exception as e:  # Handle any exceptions
        raise e
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to update an existing maintenance log
def update_maintenance(maintenance_id: int, ob: MaintenanceCreate):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute(
            """
            UPDATE maintenance_log 
            SET asset_tag = %s, maintenance_type = %s, vendor_name = %s, description = %s, cost = %s, 
                maintenance_date = %s, technician_name = %s, status = %s
            WHERE maintenance_id = %s
            """, (
                ob.asset_tag,  # Asset tag
                ob.maintenance_type,  # Maintenance type
                ob.vendor_name,  # Vendor name
                ob.description,  # Description of maintenance
                ob.cost,  # Cost of maintenance
                ob.maintenance_date,  # Date of maintenance
                ob.technician_name,  # Technician's name
                ob.status,  # Status of the maintenance
                maintenance_id  # Maintenance ID to update
            )
        )
        conn.commit()  # Commit transaction
    except Exception as e:  # Handle any exceptions
        raise e
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to update the status of a maintenance log
def update_maintenance_status(maintenance_id: int, status: str):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute(
            "UPDATE maintenance_log SET status = %s WHERE maintenance_id = %s", (status, maintenance_id)
        )
        conn.commit()  # Commit transaction
    except Exception as e:  # Handle any exceptions
        raise e
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to delete a maintenance log by its ID
def delete_maintenance(maintenance_id: int):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute("delete FROM maintenance_log WHERE maintenance_id = %s", (maintenance_id,))
        conn.commit()  # Commit transaction
    except Exception as e:  # Handle any exceptions
        raise e
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to search for maintenance logs based on a keyword
def search_maintenance(keyword: str):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        query = """
        select * FROM maintenance_log WHERE 
        description LIKE %s OR 
        vendor_name LIKE %s OR 
        technician_name LIKE %s
        """
        like_keyword = f"%{keyword}%"  # Prepare the keyword for SQL LIKE query
        cursor.execute(query, (like_keyword, like_keyword, like_keyword))
        return cursor.fetchall()  # Return all results
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to count the total number of maintenance logs
def count_maintenance():
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute("select COUNT(*) FROM maintenance_log")  # Count all maintenance logs
        return cursor.fetchone()[0]  # Return the count
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection
