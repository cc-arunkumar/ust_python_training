import pymysql
from db_connection.db import get_connection
import datetime
from fastapi import HTTPException



def get_all_data():
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM ust_asset_inventory.vendor_master"
        cursor.execute(sql)
        ans = cursor.fetchall()   
        return ans
    except Exception as e:
        print("Error fetching tasks:", e)
        return []
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        
def get_data_by_status(active_status: str):
    
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM ust_asset_inventory.vendor_master WHERE active_status=%s"
        cursor.execute(sql, (active_status,))
        ans = cursor.fetchall()
        return ans
    except Exception as e:
        print("Error fetching vendors:", e)
        return []
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def get_data_by_id(id:int):
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = "select * from ust_asset_inventory.vendor_master where vendor_id=%s"
        cursor.execute(sql, (id,))
        ans =cursor.fetchone()
        return ans 
    except Exception as e:
        print("Error fetching vendors:", e)
        return []
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def create_vendor(vendor):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO vendor_master (
            vendor_id, vendor_name, contact_person, contact_phone,
            gst_number, email, address, city, active_status
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            str(vendor.vendor_id),       # UUID stored as string
            vendor.vendor_name,
            vendor.contact_person,
            vendor.contact_phone,
            vendor.gst_number,
            vendor.email,
            vendor.address,
            vendor.city.value,           # Enum → string
            vendor.activity_status.value # Enum → string
        )

        cursor.execute(sql, values)
        conn.commit()

        return {"message": "Vendor created successfully", "vendor_id": str(vendor.vendor_id)}

    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating vendor: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        
        
def update_vendor(id: str, vendor):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
        UPDATE vendor_master
        SET vendor_name=%s, contact_person=%s, contact_phone=%s,
            gst_number=%s, email=%s, address=%s, city=%s, active_status=%s
        WHERE vendor_id=%s
        """
        values = (
            vendor.vendor_name,
            vendor.contact_person,
            vendor.contact_phone,
            vendor.gst_number,
            vendor.email,
            vendor.address,
            vendor.city.value,
            vendor.activity_status.value,
            id,
        )
        cursor.execute(sql, values)
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Vendor with id {id} not found")
        return {"message": "Vendor updated successfully", "vendor_id": id}
    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating vendor: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# Update only status
def update_vendor_status(id: str, status: str):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "UPDATE vendor_master SET active_status=%s WHERE vendor_id=%s"
        cursor.execute(sql, (status, id))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Vendor with id {id} not found")
        return {"message": "Vendor status updated successfully", "vendor_id": id, "active_status": status}
    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating vendor status: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# Delete vendor
def delete_vendor(id: str):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM vendor_master WHERE vendor_id=%s"
        cursor.execute(sql, (id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Vendor with id {id} not found")
        return {"message": "Vendor deleted successfully", "vendor_id": id}
    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting vendor: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# Search vendors by keyword
def get_rows_by_column(column_name: str, keyword: str):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        allowed_columns = ["vendor_id", "vendor_name", "contact_person", "contact_phone",
                           "gst_number", "email", "address", "city", "active_status"]

        if column_name not in allowed_columns:
            return {"error": f"Invalid column name: {column_name}"}

        # Build query dynamically with safe column name
        sql = f"SELECT * FROM vendor_master WHERE {column_name} = %s"
        cursor.execute(sql, (keyword,))
        rows = cursor.fetchall()

        return rows if rows else {"message": f"No rows found where {column_name} = {keyword}"}

    except Exception as e:
        print("Error fetching rows:", e)
        return {"error": str(e)}
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# Count vendors
def count_vendors():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "SELECT COUNT(*) FROM vendor_master"
        cursor.execute(sql)
        total = cursor.fetchone()[0]
        return total
    except Exception as e:
        print("Error counting vendors:", e)
        return 0
    finally:
        if cursor: cursor.close()
        if conn: conn.close()