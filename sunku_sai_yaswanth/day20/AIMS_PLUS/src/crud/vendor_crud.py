

import csv
from typing import Optional

from fastapi import HTTPException
from config.db_connection import get_connection
from models.vendor_model import VendorModel

# query = """
# INSERT INTO ust_aims_db.vendor_master (
#     vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status
# ) VALUES (
#     %s, %s, %s, %s, %s, %s, %s, %s
# )
# """

# try:
#     conn = get_connection()
#     cursor = conn.cursor()

#     with open("valid_rows_vendor.csv", "r", encoding="utf-8") as file:
#         reader = csv.DictReader(file)

#         for row in reader:
#             # Adjust the data to match the 'vendor_master' table's columns (excluding vendor_id)
#             data = (
#                 row["vendor_name"],       # vendor_name
#                 row["contact_person"],    # contact_person
#                 row["contact_phone"],     # contact_phone
#                 row["gst_number"],        # gst_number
#                 row["email"],             # email
#                 row["address"],           # address
#                 row["city"],              # city
#                 row["active_status"]      # active_status
#             )
#             cursor.execute(query, data)
    
#     conn.commit()

# except Exception as e:
#     print(f"Error: {e}")

# finally:
#     if conn:
#         cursor.close()
#         conn.close()

def get_all_vendors(status_filter: Optional[str] = ""):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if status_filter == "":
            cursor.execute("SELECT * FROM ust_aims_db.vendor_master")
        else:
            cursor.execute("SELECT * FROM ust_aims_db.vendor_master WHERE active_status=%s", (status_filter,))
        
        rows = cursor.fetchall()
        
        return rows if rows else None
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching vendor records: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()

# Get a specific vendor by vendor_id
def get_vendor_by_id(vendor_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM ust_aims_db.vendor_master WHERE vendor_id= %s", (vendor_id,))
        row = cursor.fetchone()
        
        return row 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching vendor: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()

# Insert a new vendor
def insert_vendor(new_vendor: VendorModel):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
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
        
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inserting vendor: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()

# Update an existing vendor by vendor_id
def update_vendor_by_id(vendor_id: int, updated_vendor: VendorModel):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if the vendor exists
        existing_vendor = get_vendor_by_id(vendor_id)
        if not existing_vendor:
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
        
        conn.commit()
        return updated_vendor  
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating vendor: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()

# Delete a vendor by vendor_id
def delete_vendor(vendor_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        if get_vendor_by_id(vendor_id):
            cursor.execute("DELETE FROM ust_aims_db.vendor_master WHERE vendor_id = %s", (vendor_id,))
            conn.commit()
            return True
        else:
            raise HTTPException(status_code=404, detail=f"Vendor with ID {vendor_id} not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting vendor: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()

# Search for vendors by a specific field (e.g., vendor_name, contact_phone)
def search_vendor(field_type: str, keyword: str):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM ust_aims_db.vendor_master WHERE {field_type} LIKE %s", (f'%{keyword}%',))
        data = cursor.fetchall()
        
        return data if data else None
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching vendors: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()


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


# with open("vendor_master.csv", "r") as file:
#     csv_reader = csv.DictReader(file)
#     header = csv_reader.fieldnames

#     for row in csv_reader:
#         try:
#             valid = VendorModel(**row)
#             valid_rows_vendor.append(valid.model_dump())  
            
#         except Exception as e:
#             row['error'] = str(e)  
#             invalid_rows_vendor.append(row)

# fieldnames_vendor = required_fields_vendor + ['error']  

# with open("valid_rows_vendor.csv", "w", newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=required_fields_vendor)
#     writer.writeheader()
#     for row in valid_rows_vendor:
#         writer.writerow(row) 

# with open("invalid_rows_vendor.csv", "w", newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames_vendor)
#     writer.writeheader()
#     for row in invalid_rows_vendor:
#         writer.writerow(row)
