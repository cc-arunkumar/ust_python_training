import csv
from fastapi import HTTPException, status
from ..config import db_connection

# Define headers for vendor fields
headers = [
    "vendor_id","vendor_name","contact_person","contact_phone",
    "gst_number","email","address","city","active_status"
]



# Function to get all vendors or filter by status
def get_all(status):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_aims_plus.vendor_master")
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No vendors found")

        response = []
        if status == "":
            for row in rows:
                response.append(dict(zip(headers, row)))
            return response
        if status == "count":
            return {"count": len(rows)}
        else:
            for row in rows:
                if row[8] == status:  # active_status field
                    response.append(dict(zip(headers, row)))
            return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to get vendor by ID
def get_by_id(vendor_id):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_aims_plus.vendor_master WHERE VENDOR_ID=%s", (vendor_id,))
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendor not found")
        return dict(zip(headers, row))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to create a single vendor record
def create_asset(row):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO ust_aims_plus.vendor_master(
            vendor_name,contact_person,contact_phone,gst_number,
            email,address,city,active_status
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        data = (
            row.vendor_name, row.contact_person, row.contact_phone, row.gst_number,
            row.email, row.address, row.city, row.active_status
        )
        cursor.execute(query, data)
        conn.commit()
        return {"message": "Vendor record inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to update vendor record by ID
def update_by_id(vendor_id, row):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        query = """ 
        UPDATE ust_aims_plus.vendor_master SET vendor_name=%s,contact_person=%s,contact_phone=%s,gst_number=%s,
        email=%s,address=%s,city=%s,active_status=%s 
        WHERE VENDOR_ID=%s"""
        data = (
            row.vendor_name, row.contact_person, row.contact_phone, row.gst_number,
            row.email, row.address, row.city, row.active_status, vendor_id
        )
        cursor.execute(query, data)
        conn.commit()
        return {"message": "Vendor updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to update vendor status by ID
def update_by_status(vendor_id, status):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        query = "UPDATE ust_aims_plus.vendor_master SET active_status=%s WHERE VENDOR_ID=%s"
        cursor.execute(query, (status, vendor_id))
        conn.commit()
        return get_by_id(vendor_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to delete vendor record by ID
def delete_by_id(vendor_id):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        query = "DELETE FROM ust_aims_plus.vendor_master WHERE VENDOR_ID=%s"
        cursor.execute(query, (vendor_id,))
        conn.commit()
        return {"message": "Deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to search vendors by field and keyword
def get_by_search(field_type, keyword):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM ust_aims_plus.vendor_master WHERE {field_type} LIKE %s", (f'%{keyword}%',))
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No matching vendors found")
        return [dict(zip(headers, row)) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to get count of all vendors
def get_by_count():
    try:
        return {"count": get_all("count")}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Function to get vendors filtered by status
def get_assets_by_status(status):
    return get_all(status)

