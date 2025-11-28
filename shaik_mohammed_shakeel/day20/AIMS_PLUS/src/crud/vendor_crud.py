import csv
from typing import Optional
from fastapi import HTTPException
from src.config.db_connection import get_connection
from src.models.vendor_model import VendorModel



# Function to retrieve all vendors with an optional status filter
def get_all_vendors(status_filter: Optional[str] = ""):
    try:
        # Establishing connection to the database
        conn = get_connection()
        cursor = conn.cursor()
        
        # Query to fetch all vendors or filtered by active status
        if status_filter == "":
            cursor.execute("SELECT * FROM ust_aims_db.vendor_master")
        else:
            cursor.execute("SELECT * FROM ust_aims_db.vendor_master WHERE active_status=%s", (status_filter,))
        
        # Fetch all results
        rows = cursor.fetchall()
        
        # Return the rows, or None if no rows are found
        return rows if rows else None
    except Exception as e:
        # Raise an HTTP exception if there is an error fetching vendor records
        raise HTTPException(status_code=500, detail=f"Error fetching vendor records: {str(e)}")
    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()

# Function to retrieve a specific vendor by vendor_id
def get_vendor_by_id(vendor_id: int):
    try:
        # Establishing connection to the database
        conn = get_connection()
        if conn is None:
            raise HTTPException(status_code=500, detail="Failed to connect to the database.")
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_aims_db.vendor_master WHERE vendor_id= %s", (vendor_id,))
        row = cursor.fetchone()
        
        # Return the vendor data or None if not found
        return row 
    except Exception as e:
        # Raise an HTTP exception if there is an error fetching vendor by ID
        raise HTTPException(status_code=500, detail=f"Error fetching vendor: {str(e)}")
    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()

# Function to insert a new vendor into the database
def insert_vendor(new_vendor: VendorModel):
    try:
        # Establishing connection to the database
        conn = get_connection()
        cursor = conn.cursor()
        
        # SQL query to insert a new vendor into the database
        cursor.execute("""
            INSERT INTO ust_aims_db.vendor_master (
                vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            new_vendor.vendor_name,
            new_vendor.contact_person,
            new_vendor.contact_phone,
            new_vendor.gst_number,
            new_vendor.email,
            new_vendor.address,
            new_vendor.city,
            new_vendor.active_status
        ))
        
        # Commit the transaction to save changes
        conn.commit()
    except Exception as e:
        # Raise an HTTP exception if there is an error inserting the vendor
        raise HTTPException(status_code=500, detail=f"Error inserting vendor: {str(e)}")
    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()

# Function to update an existing vendor's details by vendor_id
def update_vendor_by_id(vendor_id: int, updated_vendor: VendorModel):
    try:
        # Establishing connection to the database
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if the vendor exists before attempting the update
        existing_vendor = get_vendor_by_id(vendor_id)
        if not existing_vendor:
            raise HTTPException(status_code=404, detail=f"Vendor with ID {vendor_id} not found.")
        
        # Proceed with the update if the vendor exists
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
            updated_vendor.vendor_name,
            updated_vendor.contact_person,
            updated_vendor.contact_phone,
            updated_vendor.gst_number,
            updated_vendor.email,
            updated_vendor.address,
            updated_vendor.city,
            updated_vendor.active_status,
            vendor_id
        ))
        
        # Commit the transaction
        conn.commit()
        return updated_vendor  
    except Exception as e:
        # Raise an HTTP exception if there is an error updating the vendor
        raise HTTPException(status_code=500, detail=f"Error updating vendor: {str(e)}")
    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()

# Function to delete a vendor by vendor_id
def delete_vendor(vendor_id: int):
    try:
        # Establishing connection to the database
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if the vendor exists before attempting to delete
        if get_vendor_by_id(vendor_id):
            cursor.execute("DELETE FROM ust_aims_db.vendor_master WHERE vendor_id = %s", (vendor_id,))
            conn.commit()
            return True
        else:
            raise HTTPException(status_code=404, detail=f"Vendor with ID {vendor_id} not found.")
    except Exception as e:
        # Raise an HTTP exception if there is an error deleting the vendor
        raise HTTPException(status_code=500, detail=f"Error deleting vendor: {str(e)}")
    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()

# Function to search for vendors by a specific field (e.g., vendor_name, contact_phone)
def search_vendor(field_type: str, keyword: str):
    try:
        # Establishing connection to the database
        conn = get_connection()
        cursor = conn.cursor()
        
        # Query to search vendors based on a specific field and keyword
        cursor.execute(f"SELECT * FROM ust_aims_db.vendor_master WHERE {field_type} LIKE %s", (f'%{keyword}%',))
        data = cursor.fetchall()
        
        # Return the search results or None if no matches
        return data if data else None
    except Exception as e:
        # Raise an HTTP exception if there is an error searching vendors
        raise HTTPException(status_code=500, detail=f"Error searching vendors: {str(e)}")
    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()
