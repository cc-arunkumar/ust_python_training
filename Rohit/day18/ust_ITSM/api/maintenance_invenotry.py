import pymysql
from fastapi import FastAPI, HTTPException
from db_connection.db import get_connection

app = FastAPI()

# --- CREATE ---
def create_maintenance(log):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
        INSERT INTO maintenance_log (
            log_id, asset_tag, maintenance_type, vendor_name,
            description, cost, maintenance_date, technician_name, status
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = (
            log.log_id,
            log.asset_tag,
            log.maintenance_type.value,
            log.vendor_name,
            log.description,
            log.cost,
            log.maintenance_date,
            log.technician_name,
            log.status.value,
        )
        cursor.execute(sql, values)
        conn.commit()
        return {"message": "Maintenance record created successfully", "log_id": log.log_id}
    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating maintenance record: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# --- LIST ALL ---
def list_maintenance():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM maintenance_log")
        return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching maintenance records: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# --- LIST BY STATUS ---
def list_maintenance_by_status(status: str):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM maintenance_log WHERE status=%s", (status,))
        return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching maintenance records: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# --- GET BY ID ---
def get_maintenance_by_id(log_id: int):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM maintenance_log WHERE log_id=%s", (log_id,))
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail=f"Maintenance record with id {log_id} not found")
        return row
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching maintenance record: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# --- UPDATE FULL ---
def update_maintenance(log_id: int, row: dict):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
        UPDATE maintenance_log
        SET asset_tag=%s, maintenance_type=%s, vendor_name=%s,
            description=%s, cost=%s, maintenance_date=%s,
            technician_name=%s, status=%s
        WHERE log_id=%s
        """
        values = (
            row["asset_tag"],
            row["maintenance_type"],
            row["vendor_name"],
            row["description"],
            row["cost"],
            row["maintenance_date"],
            row["technician_name"],
            row["status"],
            log_id,
        )
        cursor.execute(sql, values)
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Maintenance record with id {log_id} not found")
        return {"message": "Maintenance record updated successfully", "log_id": log_id}
    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating maintenance record: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# --- UPDATE STATUS ONLY ---
def update_maintenance_status(log_id: int, status: str):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE maintenance_log SET status=%s WHERE log_id=%s", (status, log_id))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Maintenance record with id {log_id} not found")
        return {"message": "Maintenance status updated successfully", "log_id": log_id, "status": status}
    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating maintenance status: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


# --- DELETE ---
def delete_maintenance(log_id: int):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM maintenance_log WHERE log_id=%s", (log_id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Maintenance record with id {log_id} not found")
        return {"message": "Maintenance record deleted successfully", "log_id": log_id}
    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting maintenance record: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
