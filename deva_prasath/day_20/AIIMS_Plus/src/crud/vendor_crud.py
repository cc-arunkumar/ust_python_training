import pymysql # MySQL connector for database interaction
from typing import List, Optional  # Type hinting for List and Optional
from ..models.vendor_model import VendorCreate  # Importing VendorCreate model from vendor_model

# Function to establish a connection to the MySQL database
def get_db_connection():
    return pymysql.connect(
        host="localhost",  # Database host
        user="root",  # Database username
        password="pass@word1",  # Database password
        database="aiims",  # Database name
    )

# Function to get vendors, optionally filtered by active status
def get_vendors(status: Optional[str] = None):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor for database operations
    try:
        if status:  # If status filter is provided
            cursor.execute("select * FROM vendor_master WHERE active_status=%s", (status,))
        else:  # No filter, return all vendors
            cursor.execute("select * FROM vendor_master")
        return cursor.fetchall()  # Return all the fetched vendors
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection


# Function to get a specific vendor by their ID
def get_vendor_by_id(vendor_id: int):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute("select * FROM vendor_master WHERE vendor_id=%s", (vendor_id,))
        return cursor.fetchone()  # Return the vendor data
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection


# Function to create a new vendor in the database
def create_vendor(vendor: VendorCreate):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute(
            """
            insert into vendor_master (vendor_name, contact_person, contact_phone, gst_number, 
            email, address, city, active_status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                vendor.vendor_name,  # Vendor name
                vendor.contact_person,  # Contact person
                vendor.contact_phone,  # Contact phone
                vendor.gst_number,  # GST number
                vendor.email,  # Vendor email
                vendor.address,  # Vendor address
                vendor.city,  # Vendor city
                vendor.active_status  # Active status of vendor
            )
        )
        conn.commit()  # Commit transaction
    except Exception as e:  # Handle any exceptions
        raise e
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to update an existing vendor's information
def update_vendor(vendor_id: int, vendor: VendorCreate):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute(
            """
            UPDATE vendor_master 
            SET vendor_name = %s, contact_person = %s, contact_phone = %s, gst_number = %s, email = %s, 
                address = %s, city = %s, active_status = %s
            WHERE vendor_id = %s
            """, (
                vendor.vendor_name,  # Vendor name
                vendor.contact_person,  # Contact person
                vendor.contact_phone,  # Contact phone
                vendor.gst_number,  # GST number
                vendor.email,  # Vendor email
                vendor.address,  # Vendor address
                vendor.city,  # Vendor city
                vendor.active_status,  # Active status of vendor
                vendor_id  # Vendor ID to update
            )
        )
        conn.commit()  # Commit transaction
    except Exception as e:  # Handle any exceptions
        raise e
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to update the active status of a vendor
def update_vendor_status(vendor_id: int, active_status: str):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute(
            "UPDATE vendor_master SET active_status = %s WHERE vendor_id = %s", (active_status, vendor_id)
        )
        conn.commit()  # Commit transaction
    except Exception as e:  # Handle any exceptions
        conn.rollback()  # Rollback transaction in case of error
        raise e
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to delete a vendor by their ID
def delete_vendor(vendor_id: int):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute("DELETE FROM vendor_master WHERE vendor_id = %s", (vendor_id,))
        conn.commit()  # Commit transaction
    except Exception as e:  # Handle any exceptions
        conn.rollback()  # Rollback transaction in case of error
        raise e
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to search for vendors based on a keyword
def search_vendors(keyword: str):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor(dictionary=True)  # Create a cursor that returns results as dictionaries
    try:
        query = """
        SELECT * FROM vendor_master WHERE 
        vendor_name LIKE %s OR 
        contact_person LIKE %s OR 
        email LIKE %s
        """
        like_keyword = f"%{keyword}%"  # Prepare the keyword for SQL LIKE query
        cursor.execute(query, (like_keyword, like_keyword, like_keyword))
        return cursor.fetchall()  # Return all results
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to count the total number of vendors
def count_vendors():
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute("SELECT COUNT(*) FROM vendor_master")  # Count all vendors
        return cursor.fetchone()[0]  # Return the count
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection
