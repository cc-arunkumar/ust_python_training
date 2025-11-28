from src.config.db_connection import get_connection
from src.models.vendor_model import VendorMaster
from datetime import datetime
from fastapi import HTTPException

# CREATE
def create_vendor(vendor: VendorMaster):
    
    try:
        conn = get_connection()
        cursor=conn.cursor()
        query = """
            INSERT INTO vendor_master
            (vendor_name, contact_person, contact_phone, gst_number,
             email, address, city, active_status)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """
        values=(
                vendor.vendor_name, vendor.contact_person, vendor.contact_phone,
                vendor.gst_number, vendor.email, vendor.address,
                vendor.city, vendor.active_status
            )
        
        cursor.execute(query,values)
        conn.commit()
        return {"message":"Vendor created sucessfully"}
    except Exception as e:
       raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()


def get_vendor_by_id(vendor_id: int):
    try:
        conn = get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM vendor_master WHERE vendor_id=%s", (vendor_id,))
        result=cursor.fetchone()
        if not result:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return result
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()

def get_all_vendors():
    try:
        conn = get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM vendor_master")
        results = cursor.fetchall()
        return results
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# UPDATE
def update_vendor_status(vendor_id: int, new_status: str):
    
    try:
        conn = get_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE vendor_master SET active_status=%s WHERE vendor_id=%s",(new_status, vendor_id))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return {"message": "Vendor status updated successfully"}
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# DELETE
def delete_vendor(vendor_id: int):
    
    try:
        conn = get_connection()
        cursor=conn.cursor()
        cursor.execute("DELETE FROM vendor_master WHERE vendor_id=%s", (vendor_id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return {"message": "Vendor deleted successfully"}
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def get_all_vendor_by_status(status: str | None = None):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if status:
            cursor.execute("SELECT * FROM vendor_master WHERE active_status=%s", (status,))
        else:
            cursor.execute("SELECT * FROM vendor_master")
        results = cursor.fetchall()
        return results
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        
def count_vendor():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM vendor_master")
        result = cursor.fetchone()
        return result
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def search_vendor(column_name:str,keyword:str):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        allowed_column=["vendor_name", "contact_person", "contact_phone", "gst_number",
                        "email", "address", "city", "active_status"]
        if column_name not in allowed_column:
            raise ValueError("Invalid column name")
        query=f"SELECT * FROM vendor_master WHERE {column_name} LIKE %s "
        cursor.execute(query, (f"%{keyword}%",))
        results = cursor.fetchall()
        return results
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        
def update_vendor_by_id(vendor_id: int, vendor: VendorMaster):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT asset_id FROM vendor_master WHERE vendor_id=%s", (vendor_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Asset not found")
        query = """
            UPDATE vendor_master
            SET vendor_name=%s, contact_person=%s, contact_phone=%s, 
            gst_number=%s, email=%s, address=%s, 
            city=%s, active_status=%s

        """
        values = (
                vendor.vendor_name, vendor.contact_person, vendor.contact_phone,
                vendor.gst_number, vendor.email, vendor.address,
                vendor.city, vendor.active_status
        )
        cursor.execute(query, values)
        conn.commit()
        return {"message": "Vendor updated successfully"}
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        
def bulk_upload_vendor(csv_data: list[VendorMaster]):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO vendor_master (
             vendor_name, contact_person, contact_phone, gst_number,
             email, address, city, active_status
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        for vendor in csv_data:
            values = (
               vendor.vendor_name, vendor.contact_person, vendor.contact_phone, vendor.gst_number,
             vendor.email, vendor.address, vendor.city, vendor.active_status
            )
            cursor.execute(query, values)
        conn.commit()
        return {"message": "Bulk upload successful"}
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()