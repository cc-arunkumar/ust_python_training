from src.config import db_connection
from src.models import maintenance_model
from typing import Optional

# Create a new maintenance log
def create_log(new_asset: maintenance_model.MaintenanceLog):
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO ust_asset_db.maintenance_log
            (asset_tag, maintenance_type, vendor_name, description, cost, maintenance_date, technician_name, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                new_asset.asset_tag,
                new_asset.maintenance_type,
                new_asset.vendor_name,
                new_asset.description,
                new_asset.cost,
                new_asset.maintenance_date,
                new_asset.technician_name,
                new_asset.status
            )
        )
        conn.commit()
    except Exception as e:
        raise ValueError("Error: ", e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Get all maintenance logs (optionally filter by status)
def get_all_logs(status: Optional[str] = ""):
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if status == "":
            cursor.execute("SELECT * FROM ust_asset_db.maintenance_log")
            data = cursor.fetchall()
            return data
        else:
            cursor.execute(
                "SELECT * FROM ust_asset_db.maintenance_log WHERE status = %s",
                (status,)
            )
            data = cursor.fetchall()
            return data
    except Exception as e:
        raise Exception(f"Error: {e}")
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Search maintenance logs by field and keyword
def search_logs(field_type: str, keyword: str):
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT * FROM ust_asset_db.maintenance_log WHERE {field_type} LIKE %s",
            (f'%{keyword}%',)
        )
        data = cursor.fetchall()
        return data
    except Exception as e:
        raise Exception(f"Error: {e}")
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Get maintenance log by ID
def get_log_by_id(log_id):
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM ust_asset_db.maintenance_log WHERE log_id=%s",
            (log_id,)
        )
        data = cursor.fetchone()
        return data
    except Exception as e:
        raise Exception(f"Error: {e}")
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Update maintenance log by ID
def update_log_by_id(log_id: int, new_asset: maintenance_model.MaintenanceLog):
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if get_log_by_id(log_id):
            cursor.execute(
                """
                UPDATE ust_asset_db.maintenance_log
                SET asset_tag=%s, maintenance_type=%s, vendor_name=%s, description=%s,
                    cost=%s, maintenance_date=%s, technician_name=%s, status=%s
                WHERE log_id=%s
                """,
                (
                    new_asset.asset_tag,
                    new_asset.maintenance_type,
                    new_asset.vendor_name,
                    new_asset.description,
                    new_asset.cost,
                    new_asset.maintenance_date,
                    new_asset.technician_name,
                    new_asset.status,
                    log_id
                )
            )
            conn.commit()
        else:
            raise ValueError
    except Exception as e:
        raise ValueError("Error:", e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Delete maintenance log by ID
def delete_log_by_id(log_id: int):
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if get_log_by_id(log_id):
            cursor.execute(
                "DELETE FROM ust_asset_db.maintenance_log WHERE log_id=%s",
                (log_id,)
            )
            conn.commit()
            return True
        else:
            raise ValueError
    except Exception as e:
        raise ValueError("ERROR:", e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
         



