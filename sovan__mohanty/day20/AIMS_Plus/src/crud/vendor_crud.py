from src.config.db_connct import get_conn
from src.exception.custom_exceptions import RecordNotFoundException, DuplicateRecordException

def create_vendor(vendor):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT vendor_id FROM vendor_master WHERE email=%s", (vendor.email,))
        if cur.fetchone():
            raise DuplicateRecordException("Vendor email already exists")
        cur.execute("""
            INSERT INTO vendor_master
            (vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status, last_updated)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,NOW())
        """, (
            vendor.vendor_name, vendor.contact_person, vendor.contact_phone,
            vendor.gst_number, vendor.email, vendor.address, vendor.city, vendor.active_status
        ))
        conn.commit()
        return cur.lastrowid
    finally:
        cur.close()
        conn.close()

def update_vendor(vendor_id, vendor):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM vendor_master WHERE vendor_id=%s", (vendor_id,))
        if not cur.fetchone():
            raise RecordNotFoundException("Vendor not found")
        cur.execute("""
            UPDATE vendor_master SET
            vendor_name=%s, contact_person=%s, contact_phone=%s,
            gst_number=%s, email=%s, address=%s, city=%s,
            active_status=%s, last_updated=NOW()
            WHERE vendor_id=%s
        """, (
            vendor.vendor_name, vendor.contact_person, vendor.contact_phone,
            vendor.gst_number, vendor.email, vendor.address, vendor.city,
            vendor.active_status, vendor_id
        ))
        conn.commit()
    finally:
        cur.close()
        conn.close()

def delete_vendor(vendor_id):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM vendor_master WHERE vendor_id=%s", (vendor_id,))
        conn.commit()
        if cur.rowcount == 0:
            raise RecordNotFoundException("Vendor not found")
    finally:
        cur.close()
        conn.close()

def list_vendors(status=None):
    conn = get_conn()
    cur = conn.cursor()
    try:
        if status:
            cur.execute("SELECT * FROM vendor_master WHERE active_status=%s", (status,))
        else:
            cur.execute("SELECT * FROM vendor_master")
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()

def get_vendor(vendor_id):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM vendor_master WHERE vendor_id=%s", (vendor_id,))
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()

def update_status(vendor_id, status):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("UPDATE vendor_master SET active_status=%s, last_updated=NOW() WHERE vendor_id=%s",
                    (status, vendor_id))
        conn.commit()
        if cur.rowcount == 0:
            raise RecordNotFoundException("Vendor not found")
    finally:
        cur.close()
        conn.close()

def search_vendors(keyword):
    conn = get_conn()
    cur = conn.cursor()
    try:
        like = f"%{keyword}%"
        cur.execute("""
            SELECT * FROM vendor_master
            WHERE vendor_name LIKE %s OR contact_person LIKE %s OR city LIKE %s
        """, (like, like, like))
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()

def count_vendors():
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT COUNT(*) AS total FROM vendor_master")
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()
