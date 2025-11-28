import pymysql
from typing import List, Optional
from ..model.vendor_model import VendorCreate


# Function to establish database connection
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db",  # Ensure you use the correct database name
    )


# Function to get all vendors, optionally filtered by active status
def get_vendors(status: Optional[str] = None):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        if status:
            cursor.execute("SELECT * FROM vendor_master WHERE active_status=%s", (status,))
        else:
            cursor.execute("SELECT * FROM vendor_master")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


# Function to fetch a vendor by its ID
def get_vendor_by_id(vendor_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM vendor_master WHERE vendor_id=%s", (vendor_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()


# Function to create a new vendor record in the database
def create_vendor(vendor: VendorCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO vendor_master (vendor_name, contact_person, contact_phone, gst_number, 
            email, address, city, active_status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                vendor.vendor_name,
                vendor.contact_person,
                vendor.contact_phone,
                vendor.gst_number,
                vendor.email,
                vendor.address,
                vendor.city,
                vendor.active_status
            )
        )
        conn.commit()
    except Exception as e:
        raise e  # Raise the error if the insert fails
    finally:
        cursor.close()
        conn.close()


# Function to update an existing vendor's details
def update_vendor(vendor_id: int, vendor: VendorCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            UPDATE vendor_master 
            SET vendor_name = %s, contact_person = %s, contact_phone = %s, gst_number = %s, email = %s, 
                address = %s, city = %s, active_status = %s
            WHERE vendor_id = %s
            """, (
                vendor.vendor_name,
                vendor.contact_person,
                vendor.contact_phone,
                vendor.gst_number,
                vendor.email,
                vendor.address,
                vendor.city,
                vendor.active_status,
                vendor_id
            )
        )
        conn.commit()
    except Exception as e:
        raise e  # Raise the error if the update fails
    finally:
        cursor.close()
        conn.close()


# Function to update the status (active/inactive) of a vendor
def update_vendor_status(vendor_id: int, active_status: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE vendor_master SET active_status = %s WHERE vendor_id = %s", (active_status, vendor_id)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()  # Rollback the transaction if the status update fails
        raise e
    finally:
        cursor.close()
        conn.close()


# Function to delete a vendor record by ID
def delete_vendor(vendor_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM vendor_master WHERE vendor_id = %s", (vendor_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()  # Rollback if deletion fails
        raise e
    finally:
        cursor.close()
        conn.close()


# Function to search for vendors based on a keyword in the name, contact person, or email
def search_vendors(keyword: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = """
        SELECT * FROM vendor_master WHERE 
        vendor_name LIKE %s OR 
        contact_person LIKE %s OR 
        email LIKE %s
        """
        like_keyword = f"%{keyword}%"
        cursor.execute(query, (like_keyword, like_keyword, like_keyword))
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


# Function to get the total count of vendors in the database
def count_vendors():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM vendor_master")
        return cursor.fetchone()[0]
    finally:
        cursor.close()
        conn.close()
