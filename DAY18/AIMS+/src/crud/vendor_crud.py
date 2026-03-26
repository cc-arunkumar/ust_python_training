from src.config.db_connection import get_connection

def create_vendor(vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status="Active"):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM vendor_master WHERE gst_number = %s", (gst_number,))
        if cursor.fetchone():
            return {"status": "fail", "message": "GST number already exists!"}

        query = """
            INSERT INTO vendor_master
            (vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status))
        conn.commit()
        return {"status": "success", "message": f"Vendor created successfully! Name: {vendor_name} | GST: {gst_number}"}
    except Exception as e:
        return {"status": "fail", "message": f"Exception: {str(e)}"}
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def get_all_vendors(status_filter="ALL"):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if status_filter == "ALL" or status_filter is None:  # Update this line
            cursor.execute("SELECT * FROM vendor_master ORDER BY vendor_id")
        else:
            cursor.execute("SELECT * FROM vendor_master WHERE active_status = %s ORDER BY vendor_id", (status_filter,))
        rows = cursor.fetchall()
        if rows:
            return {"status": "success", "data": rows}
        else:
            return {"status": "fail", "message": f"No vendors found with status: {status_filter}"}
    except Exception as e:
        return {"status": "fail", "message": f"Exception: {str(e)}"}
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def get_vendor_by_id(vendor_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vendor_master WHERE vendor_id = %s", (vendor_id,))
        row = cursor.fetchone()
        if row:
            return {"status": "success", "data": row}
        else:
            return {"status": "fail", "message": f"Vendor not found with ID: {vendor_id}"}
    except Exception as e:
        return {"status": "fail", "message": f"Exception: {str(e)}"}
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def update_vendor(vendor_id, vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE vendor_master SET
        vendor_name=%s, contact_person=%s, contact_phone=%s, gst_number=%s,
        email=%s, address=%s, city=%s, active_status=%s
        WHERE vendor_id=%s
        """
        cursor.execute(query, (vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status, vendor_id))
        conn.commit()
        if cursor.rowcount > 0:
            return {"status": "success", "message": "Vendor updated successfully!"}
        else:
            return {"status": "fail", "message": f"Vendor not found with ID: {vendor_id}"}
    except Exception as e:
        return {"status": "fail", "message": f"Exception: {str(e)}"}
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def update_status_only(vendor_id, new_status):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE vendor_master SET active_status=%s WHERE vendor_id=%s", (new_status, vendor_id))
        conn.commit()
        if cursor.rowcount > 0:
            return {"status": "success", "message": f"Vendor status updated to '{new_status}' for ID: {vendor_id}"}
        else:
            return {"status": "fail", "message": "Vendor not found!"}
    except Exception as e:
        return {"status": "fail", "message": f"Exception: {str(e)}"}
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def delete_vendor(vendor_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM vendor_master WHERE vendor_id=%s", (vendor_id,))
        conn.commit()
        if cursor.rowcount > 0:
            return {"status": "success", "message": "Vendor deleted successfully!"}
        else:
            return {"status": "fail", "message": "Vendor not found!"}
    except Exception as e:
        return {"status": "fail", "message": f"Exception: {str(e)}"}
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def search_vendors(keyword):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        like = f"%{keyword}%"
        query = """
        SELECT * FROM vendor_master
        WHERE vendor_name LIKE %s
           OR contact_person LIKE %s
           OR contact_phone LIKE %s
           OR gst_number LIKE %s
        """
        cursor.execute(query, (like, like, like, like))
        rows = cursor.fetchall()
        if rows:
            return {"status": "success", "data": rows}
        else:
            return {"status": "fail", "message": f"No vendors found for keyword: {keyword}"}
    except Exception as e:
        return {"status": "fail", "message": f"Exception: {str(e)}"}
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def count_vendors():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM vendor_master")
        count = cursor.fetchone()[0]
        return {"status": "success", "total_vendors": count}
    except Exception as e:
        return {"status": "fail", "message": f"Exception: {str(e)}"}
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
