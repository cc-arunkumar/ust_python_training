from src.config.db_connection import get_connection
from src.models.asset_model import AssetInventory

# CREATE
def create_asset(asset: AssetInventory):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO asset_inventory
            (asset_tag, asset_type, serial_number, manufacturer, model,
             purchase_date, warranty_years, condition_status, assigned_to,
             location, asset_status, last_updated)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            cursor.execute(sql, (
                asset.asset_tag, asset.asset_type, asset.serial_number,
                asset.manufacturer, asset.model, asset.purchase_date,
                asset.warranty_years, asset.condition_status, asset.assigned_to,
                asset.location, asset.asset_status, asset.last_updated
            ))
            conn.commit()
            return cursor.lastrowid
    finally:
        conn.close()

# READ
def get_asset_by_id(asset_id: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM asset_inventory WHERE asset_id=%s", (asset_id,))
            return cursor.fetchone()
    finally:
        conn.close()

def get_all_assets():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM asset_inventory")
            return cursor.fetchall()
    finally:
        conn.close()

# UPDATE
def update_asset_status(asset_id: int, new_status: str):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE asset_inventory SET asset_status=%s WHERE asset_id=%s",
                           (new_status, asset_id))
            conn.commit()
            return cursor.rowcount
    finally:
        conn.close()

# DELETE
def delete_asset(asset_id: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM asset_inventory WHERE asset_id=%s", (asset_id,))
            conn.commit()
            return cursor.rowcount
    finally:
        conn.close()
