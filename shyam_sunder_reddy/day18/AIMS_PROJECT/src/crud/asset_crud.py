# Import required modules
from confi import db_connection          # Database connection helper
from models import asset_model           # Asset model definition

# -------------------------------
# CREATE operation
# -------------------------------
def create_asset(new_asset: asset_model.Asset):
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ust_asset_db.asset_inventory "
            "(asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status, last_updated) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
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
                new_asset.last_updated
            )
        )
        conn.commit()
        print("Asset added successfully!")
    except Exception as e:
        print("Error:", e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# -------------------------------
# READ operation (all assets)
# -------------------------------
def get_all_assets():
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_asset_db.asset_inventory")
        rows = cursor.fetchall()
        print("asset_id | asset_tag | asset_type | serial_number | manufacturer | model | purchase_date | warranty_years | assigned_to | asset_status | last_updated")
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]} | {row[8]} | {row[9]} | {row[10]}")
    except Exception as e:
        print("Error:", e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# -------------------------------
# READ operation (by ID)
# -------------------------------
def get_asset_by_id(asset_id: int):
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_asset_db.asset_inventory WHERE asset_id=%s", (asset_id,))
        row = cursor.fetchone()
        if row:
            print("asset_id | asset_tag | asset_type | serial_number | manufacturer | model | purchase_date | warranty_years | assigned_to | asset_status | last_updated")
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]} | {row[8]} | {row[9]} | {row[10]}")
            return True
        else:
            print("ID NOT FOUND")
            return False
    except Exception as e:
        print("Error:", e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# -------------------------------
# UPDATE operation
# -------------------------------
def update_asset_by_id(asset_id: int, new_asset: asset_model.Asset):
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE ust_asset_db.asset_inventory SET asset_tag=%s, asset_type=%s, serial_number=%s, manufacturer=%s, model=%s, purchase_date=%s, warranty_years=%s, assigned_to=%s, asset_status=%s, last_updated=%s WHERE asset_id=%s",
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
        print("Asset updated successfully!")
    except Exception as e:
        print("Error:", e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# -------------------------------
# DELETE operation
# -------------------------------
def delete_asset_by_id(asset_id: int):
    try:
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        if get_asset_by_id(asset_id):
            cursor.execute("DELETE FROM ust_asset_db.asset_inventory WHERE asset_id=%s", (asset_id,))
            conn.commit()
            print("Asset Record Deleted successfully")
        else:
            print("ID NOT Exists to delete")
    except Exception as e:
        print("ERROR:", e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# -------------------------------
# Sample Usage
# -------------------------------
# from datetime import date, datetime
#
# # Create a sample asset object
# sample_asset = asset_model.Asset(
#     asset_tag="AST-1001",
#     asset_type="Laptop",
#     serial_number="SN123456789",
#     manufacturer="Dell",
#     model="Latitude 5420",
#     purchase_date=date(2023, 5, 20),
#     warranty_years=3,
#     assigned_to="Shyam Sunder",
#     asset_status="In Use",
#     last_updated=datetime.now()
# )
#
# # CREATE
# create_asset(sample_asset)
# Expected Output:
# Asset added successfully!
#
# # READ ALL
# get_all_assets()
# Expected Output (table view with all rows including the new one)
#
# # READ BY ID
# get_asset_by_id(10)
# Expected Output:
# asset_id | asset_tag | asset_type | serial_number | manufacturer | model | purchase_date | warranty_years | assigned_to | asset_status | last_updated
# 10 | AST-1001 | Laptop | SN123456789 | Dell | Latitude 5420 | 2023-05-20 | 3 | Shyam Sunder | In Use | 2025-11-26 17:30:00
#
# # UPDATE
# update_asset_by_id(10, sample_asset)
# Expected Output:
# Asset updated successfully!
#
# # DELETE
# delete_asset_by_id(10)
# Expected Output:
# Asset Record Deleted successfully
