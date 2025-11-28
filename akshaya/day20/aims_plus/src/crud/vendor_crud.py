from src.config.db_connection import get_connection
from src.models.vendor_model import VendorModel

# 1. Function to create a vendor in the database
def create_vendor_db(vendor: VendorModel):
    """
    Creates a new vendor record in the 'vendor_master' table.
    Returns True if the vendor is successfully created, otherwise returns False if there is a database issue.
    """
    conn = get_connection()
    if conn is None:
        return False  # Return False if database connection fails
    with conn.cursor() as cursor:
        sql = """INSERT INTO vendor_master 
                 (vendor_name, contact_person, contact_phone, gst_number,
                  email, address, city, active_status)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (
            vendor.vendor_name,
            vendor.contact_person,
            vendor.contact_phone,
            vendor.gst_number,
            vendor.email,
            vendor.address,
            vendor.city,
            vendor.active_status
        ))
        conn.commit()  # Commit the transaction to save the vendor
    conn.close()  # Close the database connection
    return True  # Return True to indicate successful creation

# 2. Function to get all vendors from the database
def get_all_vendors_db():
    """
    Retrieves all vendor records from the 'vendor_master' table.
    Returns a list of all vendors or None if the database connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None  # Return None if the database connection fails
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM vendor_master")
        result = cursor.fetchall()  # Fetch all vendor records
    conn.close()  # Close the database connection
    return result  # Return the list of all vendors

# 3. Function to list vendors by their active status
def list_vendors_by_status_db(status: str):
    """
    Retrieves vendor records filtered by the given status (active/inactive).
    Returns a list of vendors with the specified status or None if the database connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None  # Return None if the database connection fails
    with conn.cursor() as cursor:
        # Perform a case-insensitive search for vendors with the given active status
        sql = "SELECT * FROM vendor_master WHERE LOWER(active_status) = LOWER(%s)"
        cursor.execute(sql, (status,))
        result = cursor.fetchall()  # Fetch all vendors with the specified status
    conn.close()  # Close the database connection
    return result  # Return the list of vendors with the specified status

# 4. Function to get a specific vendor by its ID
def get_vendor_by_id_db(vendor_id: int):
    """
    Retrieves a vendor record by its vendor ID.
    Returns the vendor record or None if the vendor is not found or if there is a database issue.
    """
    conn = get_connection()
    if conn is None:
        return None  # Return None if the database connection fails
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM vendor_master WHERE vendor_id = %s", (vendor_id,))
        result = cursor.fetchone()  # Fetch the vendor with the specified ID
    conn.close()  # Close the database connection
    return result  # Return the vendor record

# 5. Function to update an existing vendor in the database
def update_vendor_db(vendor_id: int, vendor: VendorModel):
    """
    Updates an existing vendor record in the 'vendor_master' table.
    Returns True if the vendor is successfully updated, False if there is a database issue.
    """
    conn = get_connection()
    if conn is None:
        return False  # Return False if the database connection fails
    with conn.cursor() as cursor:
        sql = """UPDATE vendor_master 
                 SET vendor_name=%s, contact_person=%s, contact_phone=%s, gst_number=%s,
                     email=%s, address=%s, city=%s, active_status=%s
                 WHERE vendor_id=%s"""
        cursor.execute(sql, (
            vendor.vendor_name,
            vendor.contact_person,
            vendor.contact_phone,
            vendor.gst_number,
            vendor.email,
            vendor.address,
            vendor.city,
            vendor.active_status,
            vendor_id
        ))
        conn.commit()  # Commit the transaction to save the updated vendor
        updated = cursor.rowcount  # Check how many rows were updated
    conn.close()  # Close the database connection
    return updated > 0  # Return True if one or more rows were updated, otherwise False

# 6. Function to update the active status of a vendor
def update_vendor_status_db(vendor_id: int, status: str):
    """
    Updates the active status of an existing vendor.
    Returns True if the status is successfully updated, False if no rows were affected.
    """
    conn = get_connection()
    if conn is None:
        return False  # Return False if the database connection fails
    with conn.cursor() as cursor:
        # Update the vendor's active status
        cursor.execute("UPDATE vendor_master SET active_status = %s WHERE vendor_id = %s",
                       (status, vendor_id))
        conn.commit()  # Commit the transaction
        updated = cursor.rowcount  # Check how many rows were affected
    conn.close()  # Close the database connection
    return updated > 0  # Return True if one or more rows were updated, otherwise False

# 7. Function to delete a vendor by its ID
def delete_vendor_db(vendor_id: int):
    """
    Deletes a vendor from the 'vendor_master' table by the given vendor ID.
    Returns True if the vendor is successfully deleted, False if the vendor is not found or there is a database issue.
    """
    conn = get_connection()
    if conn is None:
        return False  # Return False if the database connection fails
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM vendor_master WHERE vendor_id=%s", (vendor_id,))
        deleted = cursor.rowcount  # Check how many rows were deleted
        conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection
    return deleted > 0  # Return True if one or more rows were deleted, otherwise False

# 8. Function to search vendors based on a keyword and value
def search_vendors_db(keyword: str, value: str):
    """
    Searches for vendors based on a keyword and value in the 'vendor_master' table.
    Supports exact match for numeric fields (e.g., vendor_id) and LIKE search for string fields.
    Returns the search results or an empty list if no results are found.
    """
    conn = get_connection()
    if conn is None:
        return None  # Return None if the database connection fails
    with conn.cursor() as cursor:
        allowed_columns = ["vendor_id", "vendor_code", "vendor_name", "contact_person",
                           "email", "phone", "address", "city", "country", "status"]
        if keyword not in allowed_columns:
            return []  # Return an empty list if the keyword is not valid

        # Perform exact match for numeric column vendor_id
        if keyword == "vendor_id":
            sql = "SELECT * FROM vendor_master WHERE vendor_id = %s"
            cursor.execute(sql, (value,))
        else:
            like = f"%{value}%"  # Prepare the value for LIKE query
            sql = f"SELECT * FROM vendor_master WHERE {keyword} LIKE %s"
            cursor.execute(sql, (like,))

        result = cursor.fetchall()  # Fetch all matching records
    conn.close()  # Close the database connection
    return result  # Return the search results

# 9. Function to count the total number of vendors in the database
def count_vendors_db():
    """
    Returns the total count of vendors in the 'vendor_master' table.
    Returns 0 if no vendors are found or if there is a database connection issue.
    """
    conn = get_connection()
    if conn is None:
        return None  # Return None if the database connection fails
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS total FROM vendor_master")
        result = cursor.fetchone()  # Fetch the total count of vendors
    conn.close()  # Close the database connection
    return result["total"] if result else 0  # Return the total count, or 0 if no result
