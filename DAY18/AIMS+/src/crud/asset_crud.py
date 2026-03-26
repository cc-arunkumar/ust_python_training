# src/crud/asset_crud.py
from src.config.db_connection import get_connection

def create_asset(asset_tag, asset_type, serial_number, manufacturer, model,
                 purchase_date, warranty_years, condition_status, assigned_to, location, asset_status):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT 1 FROM asset_inventory WHERE serial_number = %s", (serial_number,))
        if cursor.fetchone():
            return {"error": "Serial number already exists!"}

        query = """
        INSERT INTO asset_inventory
        (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date,
         warranty_years, condition_status, assigned_to, location, asset_status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (asset_tag, asset_type, serial_number, manufacturer, model,
                               purchase_date, warranty_years, condition_status,
                               assigned_to or "", location, asset_status))
        conn.commit()
        return {"message": f"Asset created successfully! ID: {cursor.lastrowid}"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def get_all_assets(status_filter="ALL"):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        if status_filter == "ALL":
            cursor.execute("SELECT * FROM asset_inventory ORDER BY asset_id")
        else:
            cursor.execute("SELECT * FROM asset_inventory WHERE asset_status = %s ORDER BY asset_id", (status_filter,))
        rows = cursor.fetchall()
        if not rows:
            return {"message": "No assets found"}
        return {"assets": rows}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def get_asset_by_id(asset_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id = %s", (asset_id,))
        row = cursor.fetchone()
        if row:
            return {"asset": row}
        else:
            return {"message": "Asset not found"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def update_asset(asset_id, asset_tag, asset_type, serial_number, manufacturer, model,
                 purchase_date, warranty_years, condition_status, assigned_to, location, asset_status):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = """
        UPDATE asset_inventory SET
        asset_tag=%s, asset_type=%s, serial_number=%s, manufacturer=%s, model=%s,
        purchase_date=%s, warranty_years=%s, condition_status=%s,
        assigned_to=%s, location=%s, asset_status=%s, last_updated=NOW()
        WHERE asset_id=%s
        """
        cursor.execute(query, (asset_tag, asset_type, serial_number, manufacturer, model,
                               purchase_date, warranty_years, condition_status,
                               assigned_to or "", location, asset_status, asset_id))
        conn.commit()
        if cursor.rowcount > 0:
            return {"message": "Asset updated successfully!"}
        else:
            return {"message": "Asset not found"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def update_status_only(asset_id, new_status):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE asset_inventory SET asset_status=%s WHERE asset_id=%s", (new_status, asset_id))
        conn.commit()
        if cursor.rowcount > 0:
            return {"message": f"Status updated to '{new_status}'"}
        else:
            return {"message": "Asset not found"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def delete_asset(asset_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        conn.commit()
        if cursor.rowcount > 0:
            return {"message": "Asset deleted successfully!"}
        else:
            return {"message": "Asset not found"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def search_assets(keyword):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        like = f"%{keyword}%"
        cursor.execute("""
            SELECT * FROM asset_inventory
            WHERE asset_tag LIKE %s OR model LIKE %s OR manufacturer LIKE %s OR serial_number LIKE %s
        """, (like, like, like, like))
        rows = cursor.fetchall()
        if not rows:
            return {"message": "No assets found"}
        return {"search_results": rows}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def count_assets():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM asset_inventory")
        count = cursor.fetchone()[0]
        return {"total_assets": count}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()