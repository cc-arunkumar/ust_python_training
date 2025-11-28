from src.config.db_connection import get_connection
import pymysql
import datetime
from src.model.model_vendor_master import VendorMaster


def create_vendor(vendor):
    """
    Insert a new vendor into the vendor_master table.
    Checks for duplicate vendor name or GST number before insertion.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Check if vendor already exists based on name or GST number
    cursor.execute(
        "SELECT vendor_id FROM vendor_master WHERE vendor_name=%s OR gst_number=%s",
        (vendor.vendor_name, vendor.gst_number)
    )

    # Prevent duplicates
    if cursor.fetchone():
        conn.close()
        raise Exception("Vendor already exists!")

    # Insert vendor record
    query = """
        INSERT INTO vendor_master
        (vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    cursor.execute(query, (
        vendor.vendor_name, vendor.contact_person, vendor.contact_phone,
        vendor.gst_number, vendor.email, vendor.address, vendor.city, vendor.active_status
    ))

    conn.commit()
    conn.close()
    return "Vendor created successfully."


def get_all():
    """
    Retrieve all vendor records sorted by latest (descending ID)
    """
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM vendor_master ORDER BY vendor_id DESC")
    data = cursor.fetchall()

    conn.close()
    return data


def get_by_stat(status):
    """
    Retrieve vendor list filtered by active/inactive status
    """
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM vendor_master WHERE active_status=%s", (status,))
    data = cursor.fetchall()

    conn.close()
    return data


def get_by_id(vendor_id):
    """
    Fetch a single vendor record by vendor_id.
    Raises exception if vendor not found.
    """
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM vendor_master WHERE vendor_id=%s", (vendor_id,))
    vendor = cursor.fetchone()

    conn.close()

    if not vendor:
        raise Exception("Vendor not found.")

    return vendor


def update(vendor_id, vendor):
    """
    Update vendor record completely (full row update).
    Raises exception if vendor not found.
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE vendor_master SET
        vendor_name=%s, contact_person=%s, contact_phone=%s, gst_number=%s,
        email=%s, address=%s, city=%s, active_status=%s
        WHERE vendor_id=%s
    """

    cursor.execute(query, (
        vendor.vendor_name, vendor.contact_person, vendor.contact_phone,
        vendor.gst_number, vendor.email, vendor.address, vendor.city,
        vendor.active_status, vendor_id
    ))

    # Check if record exists
    if cursor.rowcount == 0:
        conn.close()
        raise Exception("Vendor not found.")

    conn.commit()
    conn.close()
    return "Vendor updated successfully."


def update_ven_status(vendor_id, status):
    """
    Update only the active_status field of a vendor.
    Useful for activation/deactivation.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE vendor_master SET active_status=%s WHERE vendor_id=%s",
        (status, vendor_id)
    )

    if cursor.rowcount == 0:
        conn.close()
        raise Exception("Vendor not found.")

    conn.commit()
    conn.close()
    return "Vendor status updated successfully."


def delete(vendor_id):
    """
    Delete vendor record by vendor_id.
    Raises exception if vendor does not exist.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM vendor_master WHERE vendor_id=%s", (vendor_id,))

    if cursor.rowcount == 0:
        conn.close()
        raise Exception("Vendor not found.")

    conn.commit()
    conn.close()
    return "Vendor deleted."


def find(column, value):
    """
    Search vendor records dynamically using specific column and partial match.
    Example: search_ven('vendor_name', 'abc')
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM vendor_master WHERE {column} LIKE %s", (f"%{value}%",))
    result = cursor.fetchall()

    conn.close()
    return result


def get_count():
    """
    Return total number of vendors in vendor_master table.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM vendor_master")
    count = cursor.fetchone()[0]

    conn.close()
    return count
