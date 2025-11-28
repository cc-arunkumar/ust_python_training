from src.config import db_connection
from src.models import asset_model
from typing import Optional

# Create a new asset record
def create_asset(new_asset: asset_model.AssetInventory):

    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO ust_inventory_db.asset_inventory
            (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, 
             warranty_years, condition_status, assigned_to, location, asset_status, last_updated)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
            """,
            (
                new_asset.asset_tag,
                new_asset.asset_type,
                new_asset.serial_number,
                new_asset.manufacturer,
                new_asset.model,
                new_asset.purchase_date,
                new_asset.warranty_years,
                new_asset.condition_status,
                new_asset.assigned_to,
                new_asset.location,
                new_asset.asset_status
            )
        )
        conn.commit()
    except Exception as e:
        raise ValueError("Error: ", e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()


#Retrieve all assets (optionally filter by status)
def get_all_assets(status: Optional[str] = ""):

    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if status == "":
            cursor.execute("SELECT * FROM ust_inventory_db.asset_inventory")
            data = cursor.fetchall()
            return data
        else:
            cursor.execute(
                "SELECT * FROM ust_inventory_db.asset_inventory WHERE asset_status = %s",
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


#Search assets by field and keyword
def search_assets(field_type: str, keyword: str):

    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT * FROM ust_inventory_db.asset_inventory WHERE {field_type} LIKE %s",
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


# Get asset by ID
def get_asset_by_id(asset_id):

    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM ust_inventory_db.asset_inventory WHERE asset_id=%s",
            (asset_id,)
        )
        data = cursor.fetchone()
        return data
    except Exception as e:
        raise Exception(f"Error: {e}")
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Update asset by ID
def update_asset_by_id(asset_id: int, new_asset: asset_model.AssetInventory):

    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if get_asset_by_id(asset_id):
            cursor.execute(
                """
                UPDATE ust_inventory_db.asset_inventory
                SET asset_tag=%s, asset_type=%s, serial_number=%s, manufacturer=%s, model=%s,
                    purchase_date=%s, warranty_years=%s, assigned_to=%s, asset_status=%s, last_updated=NOW()
                WHERE asset_id=%s
                """,
                (
                    new_asset.asset_tag,
                    new_asset.asset_type,
                    new_asset.serial_number,
                    new_asset.manufacturer,
                    new_asset.model,
                    new_asset.purchase_date,
                    new_asset.warranty_years,
                    new_asset.assigned_to,
                    new_asset.asset_status,
                    asset_id
                )
            )
            conn.commit()
        else:
            raise ValueError("Asset not found")
    except Exception as e:
        raise ValueError("Error:", e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Delete asset by ID
def delete_asset_by_id(asset_id: int):

    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if get_asset_by_id(asset_id):
            cursor.execute(
                "DELETE FROM ust_inventory_db.asset_inventory WHERE asset_id=%s",
                (asset_id,)
            )
            conn.commit()
            return True
        else:
            raise ValueError("Asset not found")
    except Exception as e:
        raise ValueError("ERROR:", e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
