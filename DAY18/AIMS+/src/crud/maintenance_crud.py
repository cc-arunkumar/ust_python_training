# src/crud/maintenance_crud.py
from src.config.db_connection import get_connection
from src.models.maintanance_model import MaintenanceCreate, MaintenanceUpdate

def create_maintenance(maint: MaintenanceCreate):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Check if asset exists
        cursor.execute("SELECT 1 FROM asset_inventory WHERE asset_tag = %s", (maint.asset_tag,))
        if not cursor.fetchone():
            return {"error": "Asset not found with this tag!", "asset_tag": maint.asset_tag}

        query = """
        INSERT INTO maintenance_log 
        (asset_tag, maintenance_type, vendor_name, description, cost, maintenance_date, technician_name, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            maint.asset_tag,
            maint.maintenance_type,
            maint.vendor_name,
            maint.description,
            maint.cost,
            maint.maintenance_date,
            maint.technician_name,
            maint.status or "Pending"
        ))
        conn.commit()
        return {"success": True, "message": "Maintenance created successfully!"}

    except Exception as e:
        return {"error": str(e)}
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def get_all_maintenance(status_filter=None):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        if status_filter and status_filter != "ALL":
            cursor.execute("SELECT * FROM maintenance_log WHERE status = %s ORDER BY log_id", (status_filter,))
        else:
            cursor.execute("SELECT * FROM maintenance_log ORDER BY log_id")
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return result
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def count_maintenance():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM maintenance_log")
        count = cursor.fetchone()[0]
        return {"total": count}
    finally:
        cursor.close()
        conn.close()

def search_maintenance(keyword):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        like = f"%{keyword}%"
        query = """
        SELECT * FROM maintenance_log 
        WHERE asset_tag LIKE %s OR vendor_name LIKE %s OR technician_name LIKE %s OR description LIKE %s
        """
        cursor.execute(query, (like, like, like, like))
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return result
    finally:
        cursor.close()
        conn.close()

def get_maintenance_by_id(log_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM maintenance_log WHERE log_id = %s", (log_id,))
        row = cursor.fetchone()
        if row:
            columns = [desc[0] for desc in cursor.description]
            return dict(zip(columns, row))
        return None
    finally:
        cursor.close()
        conn.close()

def update_maintenance(log_id: int, maint: MaintenanceUpdate):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Build update fields only if not None
        fields = []
        values = []
        if maint.asset_tag is not None:
            fields.append("asset_tag = %s")
            values.append(maint.asset_tag)
        if maint.maintenance_type is not None:
            fields.append("maintenance_type = %s")
            values.append(maint.maintenance_type)
        if maint.vendor_name is not None:
            fields.append("vendor_name = %s")
            values.append(maint.vendor_name)
        if maint.description is not None:
            fields.append("description = %s")
            values.append(maint.description)
        if maint.cost is not None:
            fields.append("cost = %s")
            values.append(maint.cost)
        if maint.maintenance_date is not None:
            fields.append("maintenance_date = %s")
            values.append(maint.maintenance_date)
        if maint.technician_name is not None:
            fields.append("technician_name = %s")
            values.append(maint.technician_name)
        if maint.status is not None:
            fields.append("status = %s")
            values.append(maint.status)

        if not fields:
            return {"success": False, "message": "Nothing to update"}

        query = f"UPDATE maintenance_log SET {', '.join(fields)} WHERE log_id = %s"
        values.append(log_id)

        cursor.execute(query, values)
        conn.commit()
        return {"success": cursor.rowcount > 0}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def update_status_only(log_id: int, new_status: str):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE maintenance_log SET status = %s WHERE log_id = %s", (new_status, log_id))
        conn.commit()
        return {"success": cursor.rowcount > 0}
    finally:
        cursor.close()
        conn.close()

def delete_maintenance(log_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM maintenance_log WHERE log_id = %s", (log_id,))
        conn.commit()
        return {"success": cursor.rowcount > 0}
    finally:
        cursor.close()
        conn.close()