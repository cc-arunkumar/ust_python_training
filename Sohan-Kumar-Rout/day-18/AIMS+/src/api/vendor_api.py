from config.db_connection import get_connection
import pymysql
from fastapi import HTTPException
from datetime import datetime

def get_vendor():
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)  
        sql = "SELECT * FROM vendor_valid"   
        cursor.execute(sql)
        ans = cursor.fetchall()
        return ans
    except Exception as e:
        print("Error fetching tasks:", e)
        raise HTTPException(status_code=500, detail="Database query failed")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        
import pymysql
from fastapi import HTTPException
from config.db_connection import get_connection  # adjust import if needed

def vendor_by_id(vendor_id: int):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        sql = "SELECT * FROM ust_asset_db.vendor_valid WHERE vendor_id = %s"
        cursor.execute(sql, (vendor_id,))
        row = cursor.fetchone()

        if not row:
            raise HTTPException(status_code=404, detail=f"Vendor not found")

        return row

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching vendor: {str(e)}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            
def vendor_by_status(status: str):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)  

        sql = "SELECT * FROM ust_asset_db.vendor_valid WHERE active_status = %s"
        cursor.execute(sql, (status,))
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail=f"No assets found with status '{status}'")

        return rows

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching assets: {str(e)}")

    finally:
        if cursor: cursor.close()
        if conn: conn.close()
def vendor_searching(keyword: str):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        sql = """
        SELECT * FROM ust_asset_db.vendor_valid
        WHERE vendor_name LIKE %s OR active_status LIKE %s OR contact_person LIKE %s
        """
        like_pattern = f"%{keyword}%"
        cursor.execute(sql, (like_pattern, like_pattern, like_pattern))
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail=f"No assets found for keyword ")

        return rows

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching assets: {str(e)}")

    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        
def count_vendor():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "SELECT COUNT(*) FROM ust_asset_db.vendor_valid"
        cursor.execute(sql)
        total = cursor.fetchone()[0]
        return total

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error counting assets: {str(e)}")

    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        
def delete_vendor(vendor_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = "DELETE FROM ust_asset_db.asset_inventory WHERE vendor_id=%s"
        cursor.execute(sql, (vendor_id,))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Asset with id  not found")

        return {"message": "Asset deleted successfully", "vendor_id": vendor_id}

    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting asset: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        
def creating_vendor(vendor_id, vendor_name, contact_person, contact_phone,
                    gst_number, email, address, city, active_status):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        last_updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        sql = """
        INSERT INTO ust_asset_db.vendor_valid (
            vendor_id, vendor_name, contact_person, contact_phone,
            gst_number, email, address, city, active_status, last_updated
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            vendor_id, vendor_name, contact_person, contact_phone,
            gst_number, email, address, city, active_status, last_updated
        )

        cursor.execute(sql, values)
        conn.commit()

        new_id = cursor.lastrowid if vendor_id is None else vendor_id

        return {"vendor_id": new_id, "message": "Vendor created successfully"}
    except Exception as e:
        if conn:
            conn.rollback()
        print("Error creating vendor:", e)
        return {"error": str(e)}
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            
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

