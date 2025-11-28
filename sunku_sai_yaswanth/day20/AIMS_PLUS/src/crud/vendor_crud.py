import csv
from typing import Optional

from fastapi import HTTPException
from src.config.db_connection import get_connection
from src.models.vendor_model import VendorModel


# Fetch all vendor records, with an optional filter by active status
def get_all_vendors(status_filter: Optional[str] = ""):
    try:
        # Establish a connection to the database and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # If no status filter is provided, fetch all vendor records
        if status_filter == "":
            cursor.execute("SELECT * FROM ust_aims_db.vendor_master")
        else:
            # If status filter is provided, fetch vendors based on active status
            cursor.execute("SELECT * FROM ust_aims_db.vendor_master WHERE active_status=%s", (status_filter,))
        
        # Fetch all rows matching the query
        rows = cursor.fetchall()
        
        # Return the rows if data is found, or None if no vendors are found
        return rows if rows else None
    except Exception as e:
        # Raise an HTTP exception if there's an error
        raise HTTPException(status_code=500, detail=f"Error fetching vendor records: {str(e)}")
    finally:
        # Close the database connection and cursor
        if conn:
            cursor.close()
            conn.close()


# Fetch a specific vendor by vendor_id
def get_vendor_by_id(vendor_id: int):
    try:
        # Establish a connection to the database and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # Execute a query to fetch the vendor record by its ID
        cursor.execute("SELECT * FROM ust_aims_db.vendor_master WHERE vendor_id= %s", (vendor_id,))
        row = cursor.fetchone()
        
        # Return the vendor record if found, or None if not
        return row 
    except Exception as e:
        # Raise an HTTP exception if there's an error
        raise HTTPException(status_code=500, detail=f"Error fetching vendor: {str(e)}")
    finally:
        # Close the database connection and cursor
        if conn:
            cursor.close()
            conn.close()


# Insert a new vendor into the vendor_master table
def insert_vendor(new_vendor: VendorModel):
    try:
        # Establish a connection to the database and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # Insert a new vendor into the database
        cursor.execute("""
            INSERT INTO ust_aims_db.vendor_master (
                vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            new_vendor.vendor_name,           # vendor_name
            new_vendor.contact_person,        # contact_person
            new_vendor.contact_phone,         # contact_phone
            new_vendor.gst_number,            # gst_number
            new_vendor.email,                 # email
            new_vendor.address,               # address
            new_vendor.city,                  # city
            new_vendor.active_status          # active_status
        ))
        
        # Commit the transaction to insert the vendor
        conn.commit()
    except Exception as e:
        # Raise an HTTP exception if there's an error
        raise HTTPException(status_code=500, detail=f"Error inserting vendor: {str(e)}")
    finally:
        # Close the database connection and cursor
        if conn:
            cursor.close()
            conn.close()


# Update an existing vendor by vendor_id
def update_vendor_by_id(vendor_id: int, updated_vendor: VendorModel):
    try:
        # Establish a connection to the database and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if the vendor exists before updating
        existing_vendor = get_vendor_by_id(vendor_id)
        if not existing_vendor:
            # If the vendor doesn't exist, raise an error
            raise HTTPException(status_code=404, detail=f"Vendor with ID {vendor_id} not found.")
        
        # Proceed with the update
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
            updated_vendor.vendor_name,           # vendor_name
            updated_vendor.contact_person,        # contact_person
            updated_vendor.contact_phone,         # contact_phone
            updated_vendor.gst_number,            # gst_number
            updated_vendor.email,                 # email
            updated_vendor.address,               # address
            updated_vendor.city,                  # city
            updated_vendor.active_status,         # active_status
            vendor_id
        ))
        
        # Commit the transaction to update the vendor
        conn.commit()
        return updated_vendor  # Return the updated vendor record
    except Exception as e:
        # Raise an HTTP exception if there's an error
        raise HTTPException(status_code=500, detail=f"Error updating vendor: {str(e)}")
    finally:
        # Close the database connection and cursor
        if conn:
            cursor.close()
            conn.close()


# Delete a vendor by vendor_id
def delete_vendor(vendor_id: int):
    try:
        # Establish a connection to the database and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if the vendor exists before deleting
        if get_vendor_by_id(vendor_id):
            # Execute a query to delete the vendor by its ID
            cursor.execute("DELETE FROM ust_aims_db.vendor_master WHERE vendor_id = %s", (vendor_id,))
            # Commit the transaction to delete the vendor
            conn.commit()
            return True  # Return True if deletion was successful
        else:
            raise HTTPException(status_code=404, detail=f"Vendor with ID {vendor_id} not found.")  # Raise an error if the vendor is not found
    except Exception as e:
        # Raise an HTTP exception if there's an error
        raise HTTPException(status_code=500, detail=f"Error deleting vendor: {str(e)}")
    finally:
        # Close the database connection and cursor
        if conn:
            cursor.close()
            conn.close()


# Search for vendors by a specific field (e.g., vendor_name, contact_phone)
def search_vendor(field_type: str, keyword: str):
    try:
        # Establish a connection to the database and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # Dynamically search based on field type (e.g., 'vendor_name', 'contact_phone', etc.)
        cursor.execute(f"SELECT * FROM ust_aims_db.vendor_master WHERE {field_type} LIKE %s", (f'%{keyword}%',))
        data = cursor.fetchall()  # Fetch all matching records
        
        return data if data else None  # Return the search results if found, or None if not
    except Exception as e:
        # Raise an HTTP exception if there's an error
        raise HTTPException(status_code=500, detail=f"Error searching vendors: {str(e)}")
    finally:
        # Close the database connection and cursor
        if conn:
            cursor.close()
            conn.close()


# The following block of code is commented out, it handles CSV import and validation for bulk insertion
# It checks for missing required fields, validates the data, and writes valid/invalid rows to separate CSV files.

# valid_rows_vendor = []
# invalid_rows_vendor = []

# required_fields_vendor = [
#     "vendor_id",
#     "vendor_name",
#     "contact_person",
#     "contact_phone",
#     "gst_number",
#     "email",
#     "address",
#     "city",
#     "active_status"
# ]

# # Read the CSV file and validate each row
# with open("vendor_master.csv", "r") as file:
#     csv_reader = csv.DictReader(file)
#     header = csv_reader.fieldnames

#     for row in csv_reader:
#         try:
#             valid = VendorModel(**row)  # Validate the row using the VendorModel
#             valid_rows_vendor.append(valid.model_dump())  # Store the valid rows  
#         except Exception as e:
#             row['error'] = str(e)  # Add the error message for invalid rows
#             invalid_rows_vendor.append(row)

# # Write valid rows to a CSV file
# with open("validated_vendor_master.csv", "w", newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=required_fields_vendor)
#     writer.writeheader()
#     for row in valid_rows_vendor:
#         writer.writerow(row)

# # Write invalid rows to a separate CSV file
# with open("invalid_rows_vendor.csv", "w", newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=required_fields_vendor + ['error'])
#     writer.writeheader()
#     for row in invalid_rows_vendor:
#         writer.writerow(row)
