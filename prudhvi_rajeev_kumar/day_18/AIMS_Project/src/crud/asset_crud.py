from config.db_connection import get_connection
from models.asset_model import Asset

def create_asset(asset_tag, asset_type, serial_number, manufacturer, model,
                 purchase_date, warranty_years, assigned_to, asset_status):
    conn = get_connection()
    if not conn: return None
    try:
        with conn.cursor() as cursor:
            sql = """INSERT INTO asset_inventory
                     (asset_tag, asset_type, serial_number, manufacturer, model,
                      purchase_date, warranty_years, assigned_to, asset_status)
                     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (asset_tag, asset_type, serial_number, manufacturer,
                                 model, purchase_date, warranty_years, assigned_to, asset_status))
        conn.commit()
        print("[CREATE] Asset inserted successfully")
        return cursor.lastrowid
    except Exception as e:
        print(f"[CREATE ERROR] {e}")
        return None
    finally:
        conn.close()

def read_all_assets(status_filter=None):
    conn = get_connection()
    if not conn: return []
    try:
        with conn.cursor() as cursor:
            if status_filter:
                cursor.execute("SELECT * FROM asset_inventory WHERE asset_status=%s", (status_filter,))
            else:
                cursor.execute("SELECT * FROM asset_inventory")
            rows = cursor.fetchall()
            return [Asset(r) for r in rows]
    except Exception as e:
        print(f"[READ ERROR] {e}")
        return []
    finally:
        conn.close()

def read_asset_by_id(asset_id):
    conn = get_connection()
    if not conn: return None
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM asset_inventory WHERE asset_id=%s", (asset_id,))
            row = cursor.fetchone()
            return Asset(row) if row else None
    except Exception as e:
        print(f"[READ ERROR] {e}")
        return None
    finally:
        conn.close()

def update_asset(asset_id, **fields):
    conn = get_connection()
    if not conn: return False
    try:
        with conn.cursor() as cursor:
            set_clause = ", ".join([f"{k}=%s" for k in fields.keys()])
            sql = f"UPDATE asset_inventory SET {set_clause} WHERE asset_id=%s"
            values = list(fields.values()) + [asset_id]
            cursor.execute(sql, values)
            print("[UPDATE] Asset updated successfully")
            return True
    except Exception as e:
        print(f"[UPDATE ERROR] {e}")
        return False
    finally:
        conn.close()

def delete_asset(asset_id):
    conn = get_connection()
    if not conn: return False
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM asset_inventory WHERE asset_id=%s", (asset_id,))
            print("[DELETE] Asset deleted successfully")
            return True
    except Exception as e:
        print(f"[DELETE ERROR] {e}")
        return False
    finally:
        conn.close()
