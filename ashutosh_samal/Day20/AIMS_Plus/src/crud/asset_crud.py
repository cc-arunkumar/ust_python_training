import pymysql
from typing import Optional, List
from src.model.asset_model import AssetCreate

# Function to establish a connection to the MySQL database
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db",  # Database name where asset information is stored
    )

# Fetch all assets or filter them by status if provided
def fetch_assets(status: Optional[str] = None):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        if status:
            # Execute query to fetch assets with the provided status
            cursor.execute("SELECT * FROM asset_inventory WHERE asset_status=%s", (status,))
        else:
            # Execute query to fetch all assets if no status is provided
            cursor.execute("SELECT * FROM asset_inventory")
        return cursor.fetchall()  # Return all assets matching the condition
    finally:
        cursor.close()
        conn.close()

# Fetch a single asset by its asset_id
def fetch_asset_by_id(asset_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Execute query to fetch the asset by its ID
        cursor.execute("SELECT * FROM ust_asset_db.asset_inventory WHERE asset_id=%s", (asset_id,))
        return cursor.fetchone()  # Return the single asset matching the given ID
    finally:
        cursor.close()
        conn.close()

# Create a new asset entry in the database
def create_new_asset(ob: AssetCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Execute query to insert a new asset record into the asset_inventory table
        cursor.execute(
            """
            INSERT INTO asset_inventory(asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, 
            warranty_years, condition_status, assigned_to, location, asset_status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                ob.asset_tag,
                ob.asset_type,
                ob.serial_number,
                ob.manufacturer,
                ob.model,
                ob.purchase_date,
                ob.warranty_years,
                ob.condition_status,
                ob.assigned_to,
                ob.location,
                ob.asset_status
            )
        )
        conn.commit()  # Commit the transaction to make the changes permanent
    except Exception as e:
        raise e  # Raise the exception if any error occurs
    finally:
        cursor.close()
        conn.close()

# Modify an existing asset by its ID
def modify_asset(asset_id: int, ob: AssetCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Execute query to update the asset details in the database using the provided ID
        cursor.execute(
            """
            UPDATE asset_inventory 
            SET asset_tag = %s, asset_type = %s, serial_number = %s, manufacturer = %s, model = %s, 
                purchase_date = %s, warranty_years = %s, condition_status = %s, assigned_to = %s, 
                location = %s, asset_status = %s
            WHERE asset_id = %s
            """, (
                ob.asset_tag,
                ob.asset_type,
                ob.serial_number,
                ob.manufacturer,
                ob.model,
                ob.purchase_date,
                ob.warranty_years,
                ob.condition_status,
                ob.assigned_to,
                ob.location,
                ob.asset_status,
                asset_id  # The ID of the asset to update
            )
        )
        conn.commit()  # Commit the transaction to save changes
    except Exception as e:
        raise e  # Raise an exception if the update fails
    finally:
        cursor.close()
        conn.close()

# Modify the status of an existing asset
def modify_asset_status(asset_id: int, asset_status: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Execute query to update only the asset's status
        cursor.execute(
            "UPDATE asset_inventory SET asset_status = %s WHERE asset_id = %s", (asset_status, asset_id)
        )
        conn.commit()  # Commit the transaction to apply the status change
    except Exception as e:
        conn.rollback()  # Rollback changes if an error occurs
        raise e  # Raise the exception to notify failure
    finally:
        cursor.close()
        conn.close()

# Delete an asset by its asset_id
def remove_asset(asset_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Execute query to delete the asset from the inventory using its asset_id
        cursor.execute("DELETE FROM asset_inventory WHERE asset_id = %s", (asset_id,))
        conn.commit()  # Commit the transaction to delete the asset
    except Exception as e:
        raise e  # Raise an exception if the delete operation fails
    finally:
        cursor.close()
        conn.close()

# Search assets by a keyword (used in asset_tag, model, or manufacturer)
def find_assets_by_keyword(keyword: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = """
        SELECT * FROM asset_inventory WHERE 
        asset_tag LIKE %s OR 
        model LIKE %s OR 
        manufacturer LIKE %s
        """
        like_keyword = f"%{keyword}%"  # Create a LIKE pattern for searching
        cursor.execute(query, (like_keyword, like_keyword, like_keyword))
        return cursor.fetchall()  # Return all assets that match the keyword
    finally:
        cursor.close()
        conn.close()

# Get the total number of assets in the inventory
def get_total_asset_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM asset_inventory")  # Execute query to count assets
        return cursor.fetchone()[0]  # Return the total count of assets
    finally:
        cursor.close()
        conn.close()

