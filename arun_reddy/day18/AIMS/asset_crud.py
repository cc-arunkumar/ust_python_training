from datetime import datetime, date
from typing import Optional
from mysql.connector import Error
from db_connection import get_Connection
from validators import validating


# -----------------------------
# CREATE
# -----------------------------
def create_asset(
    asset_tag: str,
    asset_type: str,
    serial_number: str,
    manufacturer: str,
    model: str,
    purchase_date: date,
    warranty_years: int,
    assigned_to: Optional[str],
    asset_status: str,
    last_updated: Optional[datetime] = None
):
    conn, cursor = None, None
    try:
        # Validation
        if validating((
            asset_tag, asset_type, serial_number, manufacturer, model,
            purchase_date, warranty_years, assigned_to, asset_status
        )) != "valid":
            raise Exception("Invalid details")

        conn = get_Connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO ust_asset_db.asset_inventory 
        (ASSET_TAG, ASSET_TYPE, SERIAL_NUMBER, MANUFACTURER, MODEL, PURCHASE_DATE,
         WARRANTY_YEARS, ASSIGNED_TO, ASSET_STATUS, LAST_UPDATED)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = (
            asset_tag, asset_type, serial_number, manufacturer, model,
            purchase_date, warranty_years, assigned_to, asset_status,
            last_updated or datetime.now()
        )

        cursor.execute(query, values)
        conn.commit()
        print("Asset inserted successfully.")

    except Exception as e:
        print("Error:", e)
    finally:
        if cursor: cursor.close()
        if conn and conn.is_connected(): conn.close()


# -----------------------------
# READ ALL
# -----------------------------
def read_all_assets(status: Optional[str] = "ALL"):
    conn, cursor = None, None
    try:
        conn = get_Connection()
        cursor = conn.cursor()

        if status == "ALL":
            cursor.execute("SELECT * FROM ust_asset_db.asset_inventory")
        else:
            cursor.execute("SELECT * FROM ust_asset_db.asset_inventory WHERE ASSET_STATUS=%s", (status,))

        rows = cursor.fetchall()
        for asset in rows:
            print(
                f"ID: {asset[0]} | TAG: {asset[1]} | TYPE: {asset[2]} | SERIAL: {asset[3]} | "
                f"MANUFACTURER: {asset[4]} | MODEL: {asset[5]} | PURCHASE_DATE: {asset[6]} | "
                f"WARRANTY: {asset[7]} | ASSIGNED_TO: {asset[8]} | STATUS: {asset[9]} | LAST_UPDATED: {asset[10]}"
            )

    except Error as e:
        print("Error:", e)
    finally:
        if cursor: cursor.close()
        if conn and conn.is_connected(): conn.close()


# -----------------------------
# READ BY ID
# -----------------------------
def read_asset_by_id(asset_id: int):
    conn, cursor = None, None
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_asset_db.asset_inventory WHERE ASSET_ID=%s", (asset_id,))
        row = cursor.fetchone()
        print(row)

    except Error as e:
        print("Error:", e)
    finally:
        if cursor: cursor.close()
        if conn and conn.is_connected(): conn.close()


# -----------------------------
# UPDATE
# -----------------------------
def update_asset(
    asset_type: str,
    manufacturer: str,
    model: str,
    warranty_years: int,
    asset_status: str,
    assigned_to: Optional[str],
    asset_id: int
):
    
    try:

        conn = get_Connection()
        cursor = conn.cursor()
        # Validation
        if validating((asset_type, manufacturer, model, warranty_years, asset_status, assigned_to, asset_id)) != "valid":
            raise Exception("Invalid Details")

        query = """
        UPDATE ust_asset_db.asset_inventory
        SET ASSET_TYPE=%s,
            MANUFACTURER=%s,
            MODEL=%s,
            WARRANTY_YEARS=%s,
            ASSET_STATUS=%s,
            ASSIGNED_TO=%s,
            LAST_UPDATED=%s
        WHERE ASSET_ID=%s
        """
        values = (asset_type, manufacturer, model, warranty_years, asset_status, assigned_to, datetime.now(), asset_id)

        cursor.execute(query, values)
        conn.commit()
        print(" Asset updated successfully.")

    except Exception as e:
        print("Error:", e)
    finally:
        if cursor: cursor.close()
        if conn and conn.is_connected(): conn.close()


# -----------------------------
# DELETE
# -----------------------------
def delete_asset(asset_id: int):
    conn, cursor = None, None
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ust_asset_db.asset_inventory WHERE ASSET_ID=%s", (asset_id,))
        conn.commit()
        print(f"Asset {asset_id} deleted successfully.")

    except Error as e:
        print("Error:", e)
    finally:
        if cursor: cursor.close()
        if conn and conn.is_connected(): conn.close()
