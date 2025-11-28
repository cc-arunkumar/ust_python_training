import csv  # Importing the csv module to handle CSV file operations
from typing import Optional  # Importing Optional for optional type annotations

from fastapi import HTTPException  # Importing HTTPException for error handling in FastAPI
from src.config.db_connection import get_connection  # Importing the get_connection function to establish DB connection
from src.models.vendor_model import VendorModel  # Importing the VendorModel for structured data handling

# This function retrieves all vendor records from the database, optionally filtered by status
def get_all_vendors(status_filter: Optional[str] = ""):
    """
    Retrieves all vendor records from the database.
    If a status filter is provided, only vendors with the specified status are retrieved.
    
    :param status_filter: Optional filter for the vendor status (e.g., 'active', 'inactive')
    :return: List of vendor records or None if no records are found
    """
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object to interact with the database
        
        # If no status filter is provided, fetch all vendors; otherwise, fetch vendors by status
        if status_filter == "":
            cursor.execute("SELECT * FROM ust_aims_db.vendor_master")
        else:
            cursor.execute("SELECT * FROM ust_aims_db.vendor_master WHERE active_status=%s", (status_filter,))
        
        rows = cursor.fetchall()  # Fetch all matching rows
        
        return rows if rows else None  # Return the rows if any are found, or None if no data is found
    except Exception as e:
        # If any error occurs during fetching, raise an HTTPException with the error details
        raise HTTPException(status_code=500, detail=f"Error fetching vendor records: {str(e)}")
    finally:
        if conn:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()

# This function retrieves a specific vendor by their vendor_id
def get_vendor_by_id(vendor_id: int):
    """
    Retrieves a vendor record by the given vendor_id.
    
    :param vendor_id: The vendor ID to search for
    :return: Vendor record if found, None if not found
    """
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Execute the SQL query to fetch the vendor by its vendor_id
        cursor.execute("SELECT * FROM ust_aims_db.vendor_master WHERE vendor_id= %s", (vendor_id,))
        row = cursor.fetchone()  # Fetch a single row
        
        return row  # Return the found vendor or None if not found
    except Exception as e:
        # If any error occurs during fetching, raise an HTTPException with the error details
        raise HTTPException(status_code=500, detail=f"Error fetching vendor: {str(e)}")
    finally:
        if conn:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()

# This function inserts a new vendor into the database
def insert_vendor(new_vendor: VendorModel):
    """
    Inserts a new vendor record into the database.
    
    :param new_vendor: The vendor data to insert into the database
    """
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Execute the SQL query to insert a new vendor into the vendor_master table
        cursor.execute("""
            INSERT INTO ust_aims_db.vendor_master (
                vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            new_vendor.vendor_name,  # vendor_name
            new_vendor.contact_person,  # contact_person
            new_vendor.contact_phone,  # contact_phone
            new_vendor.gst_number,  # gst_number
            new_vendor.email,  # email
            new_vendor.address,  # address
            new_vendor.city,  # city
            new_vendor.active_status  # active_status
        ))
        
        conn.commit()  # Commit the transaction to the database
    except Exception as e:
        # If any error occurs during insertion, raise an HTTPException with the error details
        raise HTTPException(status_code=500, detail=f"Error inserting vendor: {str(e)}")
    finally:
        if conn:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()

# This function updates an existing vendor by their vendor_id
def update_vendor_by_id(vendor_id: int, updated_vendor: VendorModel):
    """
    Updates an existing vendor record by its vendor_id.
    
    :param vendor_id: The vendor ID to update
    :param updated_vendor: The updated vendor data
    :return: The updated vendor record
    :raises HTTPException: If the vendor with the given ID is not found
    """
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Check if the vendor exists before trying to update
        existing_vendor = get_vendor_by_id(vendor_id)
        if not existing_vendor:
            raise HTTPException(status_code=404, detail=f"Vendor with ID {vendor_id} not found.")
        
        # Execute the SQL query to update the vendor record
        cursor.execute("""
            UPDATE ust_aims_db.vendor_master 
            SET 
                vendor_name = %s,
                contact_person = %s,
                contact_phone = %s,
                gst_number = %s,
                email = %s,
                address = %s,
                city = %s,
                active_status = %s
            WHERE vendor_id = %s
        """, (
            updated_vendor.vendor_name,  # vendor_name
            updated_vendor.contact_person,  # contact_person
            updated_vendor.contact_phone,  # contact_phone
            updated_vendor.gst_number,  # gst_number
            updated_vendor.email,  # email
            updated_vendor.address,  # address
            updated_vendor.city,  # city
            updated_vendor.active_status,  # active_status
            vendor_id  # vendor_id
        ))
        
        conn.commit()  # Commit the transaction to the database
        return updated_vendor  # Return the updated vendor record  
    except Exception as e:
        # If any error occurs during updating, raise an HTTPException with the error details
        raise HTTPException(status_code=500, detail=f"Error updating vendor: {str(e)}")
    finally:
        if conn:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()

# This function deletes a vendor by their vendor_id
def delete_vendor(vendor_id: int):
    """
    Deletes a vendor record from the database by its vendor_id.
    
    :param vendor_id: The vendor ID to delete
    :return: True if the deletion was successful
    :raises HTTPException: If the vendor with the given ID is not found
    """
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Check if the vendor exists before attempting to delete
        if get_vendor_by_id(vendor_id):
            cursor.execute("DELETE FROM ust_aims_db.vendor_master WHERE vendor_id = %s", (vendor_id,))
            conn.commit()  # Commit the deletion to the database
            return True  # Return True indicating the deletion was successful
        else:
            raise HTTPException(status_code=404, detail=f"Vendor with ID {vendor_id} not found.")  # If vendor is not found, raise error
        
    except Exception as e:
        # If any error occurs during deletion, raise an HTTPException with the error details
        raise HTTPException(status_code=500, detail=f"Error deleting vendor: {str(e)}")
    finally:
        if conn:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()

# This function searches for vendors by a specific field (e.g., vendor_name, contact_phone)
def search_vendor(field_type: str, keyword: str):
    """
    Searches for vendors based on a specific field and keyword.
    
    :param field_type: The field to search (e.g., 'vendor_name', 'contact_phone', etc.)
    :param keyword: The keyword to search for in the specified field
    :return: List of vendor records matching the search criteria
    :raises HTTPException: If any error occurs during the search
    """
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Execute the SQL query to search for vendors based on the field and keyword
        cursor.execute(f"SELECT * FROM ust_aims_db.vendor_master WHERE {field_type} LIKE %s", (f'%{keyword}%',))
        data = cursor.fetchall()  # Fetch all matching results
        
        return data if data else None  # Return the search results or None if no data is found

    except Exception as e:
        # If any error occurs during searching, raise an HTTPException with the error details
        raise HTTPException(status_code=500, detail=f"Error searching vendors: {str(e)}")
    
    finally:
        if conn:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()