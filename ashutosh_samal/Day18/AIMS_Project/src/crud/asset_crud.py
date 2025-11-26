import mysql.connector
from config.db_connection import get_connection
from helpers.validators import validate_asset

def create_asset(asset_tag, asset_type, serial_number, manufacturer, model,
                 purchase_date, warranty_years, assigned_to, asset_status):
    conn = None
    cursor = None
    try:
        # Validate input before inserting
        validate_asset(asset_tag, asset_type, warranty_years, assigned_to, asset_status)
        conn = get_connection()
        cursor = conn.cursor()

        # Insert new asset record
        sql = """
        INSERT INTO asset_inventory
        (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date,
         warranty_years, assigned_to, asset_status, last_updated)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())
        """
        cursor.execute(sql, (asset_tag, asset_type, serial_number, manufacturer, model,
                             purchase_date, warranty_years, assigned_to, asset_status))
        conn.commit()
        print("Asset created successfully with ID:", cursor.lastrowid)

    except Exception as e:
        print("Database Error:", e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def read_all_assets(status_filter="ALL"):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # Fetch all assets or filter by status
        if status_filter == "ALL":
            sql = "SELECT * FROM asset_inventory ORDER BY asset_id ASC"
            cursor.execute(sql)
        else:
            sql = "SELECT * FROM asset_inventory WHERE asset_status=%s ORDER BY asset_id ASC"
            cursor.execute(sql, (status_filter,))
        rows = cursor.fetchall()
        if not rows:
            print("No asset found")
        else:
            # Print asset details
            for asset in rows:
                print(f"ID: {asset[0]} | TAG: {asset[1]} | TYPE: {asset[2]} | SERIAL: {asset[3]} | "
                      f"MANUFACTURER: {asset[4]} | MODEL: {asset[5]} | PURCHASE_DATE: {asset[6]} | "
                      f"WARRANTY: {asset[7]} | ASSIGNED_TO: {asset[8]} | STATUS: {asset[9]} | "
                      f"LAST_UPDATED: {asset[10]}")
    except Exception as e:
        print("Error: ", e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        print("Connection closed successfully !")

def read_asset_by_id(asset_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # Fetch asset by ID
        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        row = cursor.fetchone()
        
        if not row:
            print("Asset not found.")
        else:
            # Print single asset details
            print(f"ID: {row[0]} | TAG: {row[1]} | TYPE: {row[2]} | SERIAL: {row[3]} | "
                  f"MANUFACTURER: {row[4]} | MODEL: {row[5]} | PURCHASE_DATE: {row[6]} | "
                  f"WARRANTY: {row[7]} | ASSIGNED_TO: {row[8]} | STATUS: {row[9]} | "
                  f"LAST_UPDATED: {row[10]}")
    except Exception as e:
        print("Error: ", e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def update_asset(asset_id, asset_type=None, manufacturer=None, model=None,
                 warranty_years=None, asset_status=None, assigned_to=None):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # Update asset details
        cursor.execute(
            "UPDATE asset_inventory SET asset_type=%s, manufacturer=%s, model=%s, warranty_years=%s, asset_status=%s, assigned_to=%s WHERE asset_id=%s",
            (asset_type, manufacturer, model, warranty_years, asset_status, assigned_to, asset_id)
        )
        conn.commit()
    except Exception as e:
        print("Error: ", e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def delete_asset(asset_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # Delete asset by ID
        cursor.execute("DELETE FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        conn.commit()
        print("Asset has been deleted successfully")
    except Exception as e:
        print("Error: ", e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        print("Connection got closed")