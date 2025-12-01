# Import necessary modules: Database connection utility and VendorMaster model
from src.config.db_connection import get_connection
from src.models.vendor_model import VendorMaster

# CREATE: Add a new vendor to the database
def create_vendor(vendor: VendorMaster):
    # Establish a connection to the database
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # SQL query to insert a new vendor into the vendor_master table
            sql = """
            INSERT INTO vendor_master
            (vendor_name, contact_person, contact_phone, gst_number,
             email, address, city, active_status)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """
            # Execute the query with the vendor's details
            cursor.execute(sql, (
                vendor.vendor_name, vendor.contact_person, vendor.contact_phone,
                vendor.gst_number, vendor.email, vendor.address,
                vendor.city, vendor.active_status
            ))
            # Commit the transaction to save the vendor
            conn.commit()
            # Return the ID of the newly inserted vendor
            return cursor.lastrowid
    finally:
        # Ensure the connection is always closed
        conn.close()

# READ: Get vendor details by vendor ID
def get_vendor_by_id(vendor_id: int):
    # Establish a connection to the database
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Execute the query to fetch the vendor by ID
            cursor.execute("SELECT * FROM vendor_master WHERE vendor_id=%s", (vendor_id,))
            # Return the vendor's details (single record)
            return cursor.fetchone()
    finally:
        # Ensure the connection is always closed
        conn.close()

# READ: Get vendors based on their active status
def get_vendor_by_status(status: str):
    # Establish a connection to the database
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Execute the query to fetch vendors by their active status
            cursor.execute("SELECT * FROM vendor_master WHERE active_status=%s", (status,))
            # Return all matching vendors
            return cursor.fetchall()
    finally:
        # Ensure the connection is always closed
        conn.close()

# READ: Get all vendors from the database
def get_all_vendors():
    # Establish a connection to the database
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Execute the query to fetch all vendors
            cursor.execute("SELECT * FROM vendor_master")
            # Return all the vendors in a list
            return cursor.fetchall()
    finally:
        # Ensure the connection is always closed
        conn.close()

# READ: Search for vendors based on a specific column and value
def search(keyword: str, value: str):
    # Establish a connection to the database
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # List of allowed columns to search in
            allowed_columns = [
                "vendor_id","vendor_name","contact_person","contact_phone",
                "gst_number","email","address","city","active_status"
            ]
            # Ensure the keyword (column) is valid
            if keyword not in allowed_columns:
                raise ValueError("Invalid column name.")
            # SQL query to search for the value in the specified column
            sql = f"SELECT * FROM vendor_master WHERE LOWER({keyword}) LIKE %s"
            cursor.execute(sql, (f"%{value.lower()}%",))
            # Return all matching vendors
            return cursor.fetchall()
    finally:
        # Ensure the connection is always closed
        conn.close()

# READ: Count the total number of vendors
def count_len_vendors():
    # Get all vendors and return the count of vendors
    vendors = get_all_vendors()
    return len(vendors)

# UPDATE: Update an existing vendor's details
def update_vendor(vendor_id: int, vendor: VendorMaster):
    # Establish a connection to the database
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # SQL query to update vendor information
            sql = """
            UPDATE vendor_master
            SET vendor_name = %s, contact_person = %s, contact_phone = %s, gst_number = %s,
                email = %s, address = %s, city = %s, active_status = %s
            WHERE vendor_id = %s
            """
            # Execute the update query with the vendor's new details
            cursor.execute(sql, (vendor.vendor_name, vendor.contact_person, vendor.contact_phone, vendor.gst_number,
                                 vendor.email, vendor.address, vendor.city, vendor.active_status, vendor_id))
            # Commit the transaction to save changes
            conn.commit()
            # Return the number of rows affected (should be 1 if successful)
            return cursor.rowcount
    finally:
        # Ensure the connection is always closed
        conn.close()

# UPDATE: Change the active status of a vendor
def update_vendor_status(vendor_id: int, new_status: str):
    # Establish a connection to the database
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Execute the query to update the vendor's status
            cursor.execute("UPDATE vendor_master SET active_status=%s WHERE vendor_id=%s",
                           (new_status, vendor_id))
            # Commit the transaction to save changes
            conn.commit()
            # Return the number of rows affected (should be 1 if successful)
            return cursor.rowcount
    finally:
        # Ensure the connection is always closed
        conn.close()

# DELETE: Delete a vendor by their ID
def delete_vendor(vendor_id: int):
    # Establish a connection to the database
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Execute the query to delete the vendor by ID
            cursor.execute("DELETE FROM vendor_master WHERE vendor_id=%s", (vendor_id,))
            # Commit the transaction to remove the vendor
            conn.commit()
            # Return the number of rows affected (should be 1 if successful)
            return cursor.rowcount
    finally:
        # Ensure the connection is always closed
        conn.close()
