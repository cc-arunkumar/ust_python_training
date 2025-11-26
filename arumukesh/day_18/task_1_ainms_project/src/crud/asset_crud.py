"""
ASSET MANAGEMENT CRUD OPERATIONS
--------------------------------
This module provides Create, Read, Update, Delete operations
for the `asset_inventory` table using MySQL + PyMySQL.

Author: Your Name
"""

from src.helpers.validators import val_asset_status, val_asset_tag, val_asset_type
from src.config.data_base_connection import get_connection
import datetime

# -------------------------------------------
# CREATE ASSET RECORD
# -------------------------------------------
def create_asset(asset_tag, asset_type, serial_number, manufacturer, model,
                 purchase_date, warranty_years, assigned_to, asset_status):
    """
    Inserts a new asset record into the database after validating business logic.

    SAMPLE CALL:
        create_asset('UST-LTP-0050', 'Laptop', 'SN-12345', 'Dell', 'Latitude 5520', 
                     '2024-01-20', 3, None, 'Available')

    EXPECTED OUTPUT:
        executed
        closing the database
    """

    # --- Validation Rules ---
    asset_tag = val_asset_tag(asset_tag)
    asset_type = val_asset_type(asset_type)
    asset_status = val_asset_status(asset_status)

    if warranty_years <= 0:
        raise ValueError("warranty year must be greater than 0")

    if asset_status == "Assigned" and assigned_to is None:
        raise ValueError("assigned_to cannot be NULL when asset status is Assigned")

    if asset_status in ("Available", "Retired") and assigned_to is not None:
        raise ValueError("Available or Retired asset cannot be assigned")

    last_updated = datetime.datetime.now()

    # --- DB Execution ---
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO asset_inventory
            (ASSET_TAG, ASSET_TYPE, SERIAL_NUMBER, MANUFACTURER, MODEL, PURCHASE_DATE,
             WARRANTY_YEARS, ASSIGNED_TO, ASSET_STATUS, LAST_UPDATED)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW());
        """, (asset_tag, asset_type, serial_number, manufacturer, model,
              purchase_date, warranty_years, assigned_to, asset_status))
        conn.commit()
        print("executed")

    except Exception as e:
        print("Error", e)

    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("closing the database")


# -------------------------------------------
# READ ALL ASSETS
# -------------------------------------------
def read_all_users():
    """
    Fetches and prints all asset records.

    SAMPLE OUTPUT:
        [(1, 'UST-LTP-0001', 'Laptop', ...), (2, 'UST-MNT-0002', 'Monitor', ...)]
        executed
        closing the database
    """

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM asset_inventory;")
        rows = cursor.fetchall()
        print(rows)
        print("executed")

    except Exception as e:
        print("Error", e)

    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("closing the database")


# -------------------------------------------
# READ ASSET BY ID
# -------------------------------------------
def read_user_by_id(id):
    """
    Returns asset details if found, otherwise False.

    SAMPLE OUTPUT:
        (1, 'UST-LTP-0001', 'Laptop', ...)
        closing the database
    """

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM asset_inventory WHERE ASSET_ID=%s;", (id,))
        row = cursor.fetchone()
        print(row)

        return bool(row)

    except Exception as e:
        print("Error", e)

    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("closing the database")


# -------------------------------------------
# UPDATE ASSET
# -------------------------------------------
def update_asset(asset_id, asset_type, manufacturer, model,
                 warranty_years, asset_status, assigned_to):
    """
    Updates an existing asset record.

    SAMPLE CALL:
        update_asset(1, "Laptop", "Dell", "Latitude 5520", 4, "Assigned", "Aakash")

    EXPECTED OUTPUT:
        database updated
        closing the database
    """

    try:
        conn = get_connection()
        cursor = conn.cursor()
        last_updated = datetime.datetime.now()

        cursor.execute("""
            UPDATE asset_inventory 
            SET ASSET_TYPE=%s, MANUFACTURER=%s, MODEL=%s, WARRANTY_YEARS=%s,
                ASSET_STATUS=%s, ASSIGNED_TO=%s, LAST_UPDATED=%s
            WHERE ASSET_ID=%s;
        """, (asset_type, manufacturer, model, warranty_years,
              asset_status, assigned_to, last_updated, asset_id))

        conn.commit()
        print("database updated")

    except Exception as e:
        print("Error", e)

    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("closing the database")


# -------------------------------------------
# DELETE ASSET
# -------------------------------------------
def delete_asset(asset_id):
    """
    Deletes an asset record if it exists.

    SAMPLE CALL:
        delete_asset(2)

    EXPECTED OUTPUT:
        deletion successful
        closing the database
    """

    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Verify record exists before deleting
        exists = read_user_by_id(asset_id)
        if exists:
            cursor.execute("DELETE FROM asset_inventory WHERE ASSET_ID=%s;", (asset_id,))
            conn.commit()
            print("deletion successful")
        else:
            print("No record found")

    except Exception as e:
        print("Error", e)

    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("closing the database")
