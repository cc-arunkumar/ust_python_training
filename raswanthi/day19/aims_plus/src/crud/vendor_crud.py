from src.config.db_connection import get_connection   # Import function to establish DB connection
from src.models.vendor_model import VendorModel       # Import VendorModel definition


# ------------------- CREATE -------------------
def create_vendor_db(vendor: VendorModel):
    """
    Insert a new vendor record into the database.
    - Accepts a VendorModel object.
    - Returns True if insertion is successful, False if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return False
    with conn.cursor() as cursor:
        sql = """INSERT INTO vendor_master 
                 (vendor_name, contact_person, contact_phone, gst_number,
                  email, address, city, active_status)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        # Execute SQL insert with vendor details
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
        conn.commit()  # Commit transaction
    conn.close()
    return True


# ------------------- READ ALL -------------------
def get_all_vendors_db():
    """
    Retrieve all vendors from the database.
    - Returns list of vendors or None if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM vendor_master")
        result = cursor.fetchall()
    conn.close()
    return result


# ------------------- LIST BY STATUS -------------------
def list_vendors_by_status_db(status: str):
    """
    Retrieve all vendors filtered by active_status (case-insensitive).
    - Returns list of vendors or None if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        sql = "SELECT * FROM vendor_master WHERE LOWER(active_status) = LOWER(%s)"
        cursor.execute(sql, (status,))
        result = cursor.fetchall()
    conn.close()
    return result


# ------------------- READ BY ID -------------------
def get_vendor_by_id_db(vendor_id: int):
    """
    Retrieve a single vendor by ID.
    - Returns vendor record or None if not found/DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM vendor_master WHERE vendor_id = %s", (vendor_id,))
        result = cursor.fetchone()
    conn.close()
    return result


# ------------------- UPDATE -------------------
def update_vendor_db(vendor_id: int, vendor: VendorModel):
    """
    Update an existing vendor record by ID.
    - Accepts VendorModel object with updated fields.
    - Returns True if update is successful, False if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return False
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
        conn.commit()
        updated = cursor.rowcount  # Number of rows updated
    conn.close()
    return updated > 0


# ------------------- UPDATE STATUS -------------------
def update_vendor_status_db(vendor_id: int, status: str):
    """
    Update only the active_status of a vendor by ID.
    - Returns True if update is successful, False if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return False
    with conn.cursor() as cursor:
        cursor.execute("UPDATE vendor_master SET active_status = %s WHERE vendor_id = %s",
                       (status, vendor_id))
        conn.commit()
        updated = cursor.rowcount
    conn.close()
    return updated > 0


# ------------------- DELETE -------------------
def delete_vendor_db(vendor_id: int):
    """
    Delete a vendor record by ID.
    - Returns True if deletion is successful, False if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return False
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM vendor_master WHERE vendor_id=%s", (vendor_id,))
        deleted = cursor.rowcount  # Number of rows deleted
        conn.commit()
    conn.close()
    return deleted > 0


# ------------------- SEARCH -------------------
def search_vendors_db(keyword: str, value: str):
    """
    Search vendors dynamically by a given column (keyword) and value.
    - Uses LIKE for partial matches, exact match for numeric fields.
    - Only allows specific safe columns to prevent SQL injection.
    - Returns list of matching vendors or empty list if keyword invalid.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        allowed_columns = ["vendor_id", "vendor_name", "contact_person",
                           "email", "contact_phone", "gst_number", "address", "city", "active_status"]
        # Validate keyword to prevent SQL injection
        if keyword not in allowed_columns:
            return []

        # Exact match for numeric column vendor_id
        if keyword == "vendor_id":
            sql = "SELECT * FROM vendor_master WHERE vendor_id = %s"
            cursor.execute(sql, (value,))
        else:
            like = f"%{value}%"
            sql = f"SELECT * FROM vendor_master WHERE {keyword} LIKE %s"
            cursor.execute(sql, (like,))

        result = cursor.fetchall()
    conn.close()
    return result


# ------------------- COUNT -------------------
def count_vendors_db():
    """
    Count total number of vendors in the database.
    - Returns integer count or None if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM vendor_master")
        result = cursor.fetchone()
    conn.close()
    return result
