from src.config import db_connection
from src.models import asset_model
from typing import Optional
from datetime import datetime
import csv

# Function: Create a new asset record in the database
def create_asset(new_asset: asset_model.Asset):
    # Insert a new asset into the asset_inventory table
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO ust_inventory_db.asset_inventory(
                asset_tag, asset_type, serial_number, manufacturer, model,
                purchase_date, warranty_years, condition_status, assigned_to,
                location, asset_status, last_updated
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
                new_asset.asset_status,
                new_asset.last_updated
            )
        )
        conn.commit()
        return True
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Function: Retrieve all assets, optionally filtered by status
def get_all_assets(status: Optional[str] = ""):
    # If status is empty, fetch all assets; otherwise filter by asset_status
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
                (status)
            )
            data = cursor.fetchall()
            return data
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Function: Retrieve a single asset by its ID
def get_asset_by_id(asset_id: int):
    # Query asset_inventory table for a specific asset_id
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM ust_inventory_db.asset_inventory WHERE asset_id=%s",
            (asset_id,)
        )
        data = cursor.fetchone()
        if data:
            return data
        else:
            return False
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Function: Update an existing asset by ID
def update_asset_by_id(asset_id: int, new_asset: asset_model.Asset):
    # Update asset record if it exists
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if get_asset_by_id(asset_id):
            cursor.execute(
                """
                UPDATE ust_inventory_db.asset_inventory
                SET asset_tag=%s, asset_type=%s, serial_number=%s, manufacturer=%s, model=%s,
                    purchase_date=%s, warranty_years=%s, assigned_to=%s, asset_status=%s,
                    last_updated=%s
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
                    new_asset.last_updated,
                    asset_id
                )
            )
            conn.commit()
            return True
        else:
            return False
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Function: Delete an asset by ID
def delete_asset_by_id(asset_id: int):
    # Remove asset record if it exists
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if get_asset_by_id(asset_id):
            cursor.execute("DELETE FROM ust_inventory_db.asset_inventory WHERE asset_id=%s", (asset_id,))
            conn.commit()
            return True
        else:
            return False
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Function: Search assets by a given field and value
def search_by_tag(field: str, value: str):
    # Perform a LIKE query on the specified field
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        query = f"SELECT * FROM ust_inventory_db.asset_inventory WHERE {field} LIKE %s"
        cursor.execute(query, (f"%{value}%",))
        data = cursor.fetchall()
        return data
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()


# Example usage (commented out for production):
# print(search_by_tag("manufacturer", "LG"))
# print(get_asset_by_id(69))

    
    
# def dump_asset_inventory(path):
#     try:
#         conn=db_connection.get_connection()
#         cursor=conn.cursor()
#         query = """
#             INSERT INTO asset_inventory (
#                 asset_tag, asset_type, serial_number, manufacturer, model,
#                 purchase_date, warranty_years, condition_status, assigned_to,
#                 location, asset_status,last_updated
#             ) VALUES (
#                 %s, %s, %s, %s, %s,
#                 %s, %s, %s, %s,
#                 %s, %s,%s
#             )
#             """
#         with open(path, "r", encoding="utf-8") as file:
#             reader = csv.DictReader(file)

#             for row in reader:
#                 data = (
#                     row["asset_tag"],
#                     row["asset_type"],
#                     row["serial_number"],
#                     row["manufacturer"],
#                     row["model"],
#                     row["purchase_date"],
#                     row["warranty_years"],
#                     row["condition_status"],
#                     row["assigned_to"],
#                     row["location"],
#                     row["asset_status"],
#                     datetime.now()
#                 )
#                 cursor.execute(query, data)
#             conn.commit()
#             print("Inserted int database successfully")
#     except Exception as e:
#         print("Error: ",e)
#     finally:
#         if conn.open:
#             cursor.close()
#             conn.close()
#         print("Connection closed successfully")
            
# # print(get_all_assets())
# # print(get_asset_by_id(69))
