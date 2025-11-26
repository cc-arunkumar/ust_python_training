from config.db_connection import get_connection
from helper import validators
from datetime import datetime

def create_asset(asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status):
    
    try:  
        conn = get_connection()
        cursor = conn.cursor()
        if not validators.validate_asset_tag(asset_tag):
            raise ValueError("asset_tag must start with 'UST-'")
        if not validators.validate_asset_type(asset_type):
            raise ValueError("Invalid asset_type")
        if not validators.validate_warranty(warranty_years):
            raise ValueError("warranty_years must be > 0")
        if not validators.validate_status_and_assignment(asset_status, assigned_to):
            raise ValueError("Invalid status/assignment combination")

        
        
        query = """INSERT INTO asset_inventory 
                    (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status, last_updated)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status, datetime.now())
        cursor.execute(query, values)
        conn.commit()
        return f"Asset created successfully with ID {cursor.lastrowid}"
    except Exception as err:
        return f"Database error: {err}"
    finally:
        cursor.close()
        conn.close()

def read_all_assets(status_filter="ALL"):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        if status_filter == "ALL":
            cursor.execute("SELECT * FROM asset_inventory ORDER BY asset_id ASC")
        else:
            cursor.execute("SELECT * FROM asset_inventory WHERE asset_status=%s ORDER BY asset_id ASC", (status_filter,))
        results = cursor.fetchall()
        return results
    except Exception as err:
            return f"Database error: {err}"
            
    finally:
        cursor.close()
        conn.close()

def read_asset_by_id(asset_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        result = cursor.fetchone()
        return result
    except Exception as err:
        return f"Database error: {err}"
        
    finally:
        cursor.close()
        conn.close()

def delete_asset(asset_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        conn.commit()
    except Exception as err:
        return f"Database error: {err}"
    finally:
        cursor.close()
        conn.close()

from config.db_connection import get_connection
from datetime import datetime

def update_asset(asset_id, asset_type, manufacturer, model, warranty_years, asset_status, assigned_to):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Check if asset exists
        cursor.execute("SELECT asset_id FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        if not cursor.fetchone():
            return "Asset not found."

        # Manual update of all allowed columns
        query = """
            UPDATE asset_inventory
            SET asset_type=%s,
                manufacturer=%s,
                model=%s,
                warranty_years=%s,
                asset_status=%s,
                assigned_to=%s,
                last_updated=%s
            WHERE asset_id=%s
        """
        values = (asset_type, manufacturer, model, warranty_years, asset_status, assigned_to, datetime.now(), asset_id)

        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount == 0:
            return "Update failed."
        return "Asset updated successfully."

    except Exception as err:
        return f"Database error: {err}"
    finally:
        cursor.close()
        conn.close()
