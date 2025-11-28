import csv
from fastapi import HTTPException, status
from ..config import db_connection

# Define headers for maintenance log fields
headers = [
    "log_id","asset_tag","maintenance_type",
    "vendor_name","description","cost",
    "maintenance_date","technician_name","status"
]

# Function to get all maintenance records or filter by status
def get_all(status):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_aims_plus.maintenance_log")
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No maintenance records found")

        response = []
        if status == "":
            for row in rows:
                response.append(dict(zip(headers, row)))
            return response
        if status == "count":
            return {"count": len(rows)}
        else:
            for row in rows:
                if row[8] == status:  # status field
                    response.append(dict(zip(headers, row)))
            return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            
# Function to get maintenance record by ID
def get_by_id(log_id):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM maintenance_log WHERE LOG_ID=%s", (log_id,))
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Maintenance record not found")
        return dict(zip(headers, row))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to create a single maintenance record
def create_asset(row):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO ust_aims_plus.maintenance_log(
            asset_tag,maintenance_type,
            vendor_name,description,cost,
            maintenance_date,technician_name,status
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        data = (
            row.asset_tag, row.maintenance_type, row.vendor_name, row.description,
            row.cost, row.maintenance_date, row.technician_name, row.status
        )
        cursor.execute(query, data)
        conn.commit()
        return {"message": "Maintenance record inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to update maintenance record by ID
def update_by_id(log_id, row):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        query = """ 
        UPDATE ust_aims_plus.maintenance_log SET asset_tag=%s, maintenance_type=%s, vendor_name=%s,
            description=%s, cost=%s, maintenance_date=%s, 
            technician_name=%s, status=%s 
        WHERE LOG_ID=%s"""
        data = (
            row.asset_tag, row.maintenance_type, row.vendor_name, row.description,
            row.cost, row.maintenance_date, row.technician_name, row.status, log_id
        )
        cursor.execute(query, data)
        conn.commit()
        return {"message": "Maintenance record updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to update maintenance status by ID
def update_by_status(log_id, status):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        query = "UPDATE ust_aims_plus.maintenance_log SET status=%s WHERE LOG_ID=%s"
        cursor.execute(query, (status, log_id))
        conn.commit()
        return get_by_id(log_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to delete maintenance record by ID
def delete_by_id(log_id):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        query = "DELETE FROM maintenance_log WHERE LOG_ID=%s"
        cursor.execute(query, (log_id,))
        conn.commit()
        return {"message": "Deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to search maintenance records by field and keyword
def get_by_search(field_type, keyword):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM maintenance_log WHERE {field_type} LIKE %s", (f'%{keyword}%',))
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No matching maintenance records found")
        return [dict(zip(headers, row)) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to get count of all maintenance records
def get_by_count():
    try:
        return {"count": len(get_all(""))}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Function to get maintenance records filtered by status
def get_assets_by_status(status):
    return get_all(status)

