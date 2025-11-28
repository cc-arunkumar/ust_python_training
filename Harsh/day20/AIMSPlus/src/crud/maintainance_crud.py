from typing import List
from src.config.db_connection import get_connection
from src.models.maintainance_model import MaintenanceLog
from fastapi import HTTPException

# CREATE a new maintenance log
def create_maintenance(log: MaintenanceLog):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO maintenance_log
            (asset_tag, maintenance_type, vendor_name, description,
             cost, maintenance_date, technician_name, status)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = (
            log.asset_tag, log.maintenance_type, log.vendor_name, log.description,
            log.cost, log.maintenance_date, log.technician_name, log.status
        )
        cursor.execute(query, values)
        conn.commit()
        return {"message": "Maintenance log created successfully", "log_id": cursor.lastrowid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()

# READ all maintenance logs (optional status filter)
def get_all_maintenance(status: str | None = None):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if status:
            cursor.execute("SELECT * FROM maintenance_log WHERE status=%s", (status,))
        else:
            cursor.execute("SELECT * FROM maintenance_log")
        results = cursor.fetchall()
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()

# READ maintenance log by ID
def get_maintenance_by_id(log_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM maintenance_log WHERE log_id=%s", (log_id,))
        result = cursor.fetchone()
        if not result:
            raise HTTPException(status_code=404, detail="Maintenance log not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()

# UPDATE full maintenance log record
def update_maintenance_by_id(log_id: int, log: MaintenanceLog):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT log_id FROM maintenance_log WHERE log_id=%s", (log_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Maintenance log not found")

        query = """
            UPDATE maintenance_log
            SET asset_tag=%s, maintenance_type=%s, vendor_name=%s, description=%s,
                cost=%s, maintenance_date=%s, technician_name=%s, status=%s
            WHERE log_id=%s
        """
        values = (
            log.asset_tag, log.maintenance_type, log.vendor_name, log.description,
            log.cost, log.maintenance_date, log.technician_name, log.status, log_id
        )
        cursor.execute(query, values)
        conn.commit()
        return {"message": "Maintenance log updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()

# UPDATE maintenance status only
def update_maintenance_status(log_id: int, new_status: str):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE maintenance_log SET status=%s WHERE log_id=%s", (new_status, log_id))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Maintenance log not found")
        return {"message": "Maintenance status updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()

# DELETE maintenance log by ID
def delete_maintenance(log_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM maintenance_log WHERE log_id=%s", (log_id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Maintenance log not found")
        return {"message": "Maintenance log deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()

# SEARCH maintenance logs by column and keyword
def search_maintenance(column_name: str, keyword: str):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        allowed_columns = [
            "asset_tag", "maintenance_type", "vendor_name", "description",
            "cost", "maintenance_date", "technician_name", "status"
        ]

        if column_name not in allowed_columns:
            raise ValueError("Invalid column name")

        query = f"SELECT * FROM maintenance_log WHERE {column_name} LIKE %s"
        cursor.execute(query, (f"%{keyword}%",))
        results = cursor.fetchall()
        return results

    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# COUNT total maintenance logs
def count_maintenance():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM maintenance_log")
        result = cursor.fetchone()
        return result
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

