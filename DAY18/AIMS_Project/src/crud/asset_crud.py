# asset_crud.py
from helpers.validators import *
from config.db_connection import get_connection

def create_asset(asset_tag, asset_type, serial_number, manufacturer, model,
                 purchase_date, warranty_years, assigned_to, asset_status):

    # --- VALIDATIONS ---
    if not validate_asset_tag(asset_tag):
        print("ERROR: Asset Tag must start with UST-")
        return

    if not validate_asset_type(asset_type):
        print("ERROR: Invalid Asset type")
        return

    if not validate_warranty_years(warranty_years):
        print("ERROR: Warranty years must be > 0")
        return

    if not validate_status(asset_status):
        print("ERROR: Invalid Asset Status")
        return

    if not validate_assignment(asset_status, assigned_to):
        print("ERROR: Invalid Assignment")
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """INSERT INTO asset_inventory
                   (asset_tag, asset_type, serial_number, manufacturer, model,
                    purchase_date, warranty_years, assigned_to, asset_status, last_updated)
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())"""

        cursor.execute(query, (asset_tag, asset_type, serial_number, manufacturer,
                               model, purchase_date, warranty_years, assigned_to, asset_status))

        conn.commit()
        print("Asset Added Successfully. ID:", cursor.lastrowid)

    except Exception as e:
        print("Exception:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection Closed Successfully - create")


def read_all_assets(status_filter="ALL"):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        if status_filter == "ALL":
            cursor.execute("SELECT * FROM asset_inventory ORDER BY asset_id ASC")
        else:
            cursor.execute("SELECT * FROM asset_inventory WHERE asset_status=%s ORDER BY asset_id ASC",
                           (status_filter,))

        rows = cursor.fetchall()

        if rows:
            for r in rows:
                print(r)
        else:
            print("No assets found.")

    except Exception as e:
        print("Exception:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection Closed Successfully - read_all")


def read_asset_by_id(asset_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        row = cursor.fetchone()

        if row:
            print(row)
            return row
        else:
            print("Asset not found.")
            return None

    except Exception as e:
        print("Exception:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection Closed Successfully - read_by_id")


def update_asset(asset_id, asset_type, manufacturer, model,
                 warranty_years, assigned_to, asset_status):

    if not validate_asset_type(asset_type):
        print("ERROR: Invalid Asset type")
        return

    if not validate_warranty_years(warranty_years):
        print("ERROR: Warranty years must be > 0")
        return

    if not validate_status(asset_status):
        print("ERROR: Invalid Asset Status")
        return

    if not validate_assignment(asset_status, assigned_to):
        print("ERROR: Invalid Assignment")
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """UPDATE asset_inventory
                   SET asset_type=%s, manufacturer=%s, model=%s,
                       warranty_years=%s, assigned_to=%s, asset_status=%s,
                       last_updated=NOW()
                   WHERE asset_id=%s"""

        cursor.execute(query, (asset_type, manufacturer, model,
                               warranty_years, assigned_to, asset_status, asset_id))
        conn.commit()

        if cursor.rowcount > 0:
            print("Asset Updated Successfully")
        else:
            print("Asset not found.")

    except Exception as e:
        print("Error:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection Closed Successfully - update")


def delete_asset(asset_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print("Asset Deleted Successfully")
        else:
            print("Asset not found.")

    except Exception as e:
        print("Exception:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection Closed Successfully - delete")
