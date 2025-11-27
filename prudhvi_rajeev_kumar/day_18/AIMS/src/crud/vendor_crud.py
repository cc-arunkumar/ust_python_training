from src.config.db_connection import get_connection
from src.models.vendor_model import VendorMaster

# CREATE
def create_vendor(vendor: VendorMaster):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO vendor_master
            (vendor_name, contact_person, contact_phone, gst_number,
             email, address, city, active_status)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """
            cursor.execute(sql, (
                vendor.vendor_name, vendor.contact_person, vendor.contact_phone,
                vendor.gst_number, vendor.email, vendor.address,
                vendor.city, vendor.active_status
            ))
            conn.commit()
            return cursor.lastrowid
    finally:
        conn.close()

# READ
def get_vendor_by_id(vendor_id: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM vendor_master WHERE vendor_id=%s", (vendor_id,))
            return cursor.fetchone()
    finally:
        conn.close()

def get_vendor_by_status(status: str):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM vendor_master WHERE active_status=%s", (status,))
            return cursor.fetchall()
    finally:
        conn.close()

        

def get_all_vendors():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM vendor_master")
            return cursor.fetchall()
    finally:
        conn.close()
        
def search(keyword: str, value: str):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            allowed_columns = [
                "vendor_id","vendor_name","contact_person","contact_phone",
                "gst_number","email","address","city","active_status"
            ]
            if keyword not in allowed_columns:
                raise ValueError("Invalid column name.")

            sql = f"SELECT * FROM vendor_master WHERE LOWER({keyword}) LIKE %s"
            cursor.execute(sql, (f"%{value.lower()}%",))
            return cursor.fetchall()
    finally:
        conn.close()

def count_len_vendors():
    vendors = get_all_vendors()
    return len(vendors)

def update_vendor(vendor_id : int, vendor : VendorMaster):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
            UPDATE vendor_master
            SET vendor_name = %s, contact_person = %s, contact_phone = %s, gst_number = %s,
                email = %s, address = %s, city = %s, active_status = %s
            WHERE vendor_id = %s
            """
            cursor.execute(sql, (vendor.vendor_name, vendor.contact_person, vendor.contact_phone, vendor.gst_number,
                                 vendor.email, vendor.address, vendor.city, vendor.active_status, vendor_id))
            conn.commit()
            return cursor.rowcount
    finally:
        conn.close()
        
# UPDATE
def update_vendor_status(vendor_id: int, new_status: str):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE vendor_master SET active_status=%s WHERE vendor_id=%s",
                           (new_status, vendor_id))
            conn.commit()
            return cursor.rowcount
    finally:
        conn.close()

# def count()
# DELETE
def delete_vendor(vendor_id: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM vendor_master WHERE vendor_id=%s", (vendor_id,))
            conn.commit()
            return cursor.rowcount
    finally:
        conn.close()
