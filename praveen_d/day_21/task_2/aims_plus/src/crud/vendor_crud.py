# src/crud/vendor_crud.py
from typing import List
from pymysql import connect
from models.vendor_model import Vendor  # Import the Pydantic model for validation
from config.db_connection import get_connection

# 1. Create Vendor
def create_vendor(vendor):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO aims_db.vendor_master
        (vendor_code, vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        data = (vendor.vendor_code, vendor.vendor_name, vendor.contact_person, vendor.contact_phone, 
                vendor.gst_number, vendor.email, vendor.address, vendor.city, vendor.active_status)
        cursor.execute(query, data)
        conn.commit()
        return {"message": "Vendor created successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

# 2. Get All Vendors
def get_all_vendors():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM aims_db.vendor_master"
        cursor.execute(query)
        vendors = cursor.fetchall()  # Returns list of tuples
        return vendors
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

# 3. Get Vendors by Status
def get_vendors_by_status(status):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM aims_db.vendor_master WHERE active_status=%s"
        cursor.execute(query, (status,))
        vendors = cursor.fetchall()  # Returns list of tuples
        return vendors
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

# 4. Get Vendor by ID
def get_vendor_by_id(vendor_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM aims_db.vendor_master WHERE vendor_id=%s"
        cursor.execute(query, (vendor_id,))
        vendor = cursor.fetchone()  # Returns a single tuple
        return vendor
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

# 5. Update Vendor by ID
def update_vendor(vendor_id, vendor_data):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE aims_db.vendor_master
        SET vendor_code=%s, vendor_name=%s, contact_person=%s, contact_phone=%s,
        gst_number=%s, email=%s, address=%s, city=%s, active_status=%s
        WHERE vendor_id=%s
        """
        data = (vendor_data['vendor_code'], vendor_data['vendor_name'], vendor_data['contact_person'],
                vendor_data['contact_phone'], vendor_data['gst_number'], vendor_data['email'], 
                vendor_data['address'], vendor_data['city'], vendor_data['active_status'], vendor_id)
        cursor.execute(query, data)
        conn.commit()
        return {"message": "Vendor updated successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

# 6. Update Vendor Status by ID
def update_vendor_status(vendor_id, status):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "UPDATE aims_db.vendor_master SET active_status=%s WHERE vendor_id=%s"
        cursor.execute(query, (status, vendor_id))
        conn.commit()
        return {"message": f"Vendor {vendor_id} status updated to {status}"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

# 7. Delete Vendor by ID
def delete_vendor(vendor_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM aims_db.vendor_master WHERE vendor_id=%s"
        cursor.execute(query, (vendor_id,))
        conn.commit()
        return {"message": f"Vendor {vendor_id} deleted successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

# 8. Search Vendors by Keyword
def search_vendors_by_keyword(keyword):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM aims_db.vendor_master WHERE vendor_name LIKE %s OR contact_person LIKE %s"
        cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
        vendors = cursor.fetchall()  # Returns list of tuples
        return vendors
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

# 9. Get the count of Vendors
def get_vendor_count():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM aims_db.vendor_master"
        cursor.execute(query)
        count = cursor.fetchone()  # Returns a single tuple (count,)
        return count[0]  # Get the count value from the tuple
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()
