from src.config.db_connection import get_connection
from ..models.asset_model import AssetModel

# 1. Function to create an asset in the database
def create_asset_db(asset: AssetModel):
    """
    Inserts a new asset record into the 'asset_inventory' table.
    Returns True if successful, None if the database connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        sql = """INSERT INTO asset_inventory 
                 (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, 
                  warranty_years, condition_status, assigned_to, location, asset_status, last_updated)
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())"""
        cursor.execute(sql, (
            asset.asset_tag, asset.asset_type, asset.serial_number, asset.manufacturer,
            asset.model, asset.purchase_date, asset.warranty_years, asset.condition_status,
            asset.assigned_to, asset.location, asset.asset_status
        ))
        conn.commit()
    conn.close()
    return True

# 2. Function to get all assets or filter by status
def get_all_assets_db(status=None):
    """
    Fetches all assets or filters assets by the given status.
    Returns the list of assets or None if the database connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        if status:
            cursor.execute("SELECT * FROM asset_inventory WHERE asset_status=%s", (status,))
        else:
            cursor.execute("SELECT * FROM asset_inventory")
        result = cursor.fetchall()
    conn.close()
    return result

# 3. Function to get an asset by its ID
def get_asset_by_id_db(asset_id: int):
    """
    Fetches an asset based on the provided asset ID.
    Returns the asset record or None if not found or if the database connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        result = cursor.fetchone()
    conn.close()
    return result

# 4. Function to search assets based on a keyword and value
def search_assets_db(keyword: str, value: str):
    """
    Searches the 'asset_inventory' table for assets based on the keyword and value.
    If the keyword is valid, it uses LIKE query to find matching records.
    Returns the search results or an empty list if no matches are found.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        like = f"%{value}%"
        if keyword not in ["asset_tag", "model", "manufacturer", "asset_id", "asset_type", 
                            "warranty_years", "condition_status", "assigned_to", "location", 
                            "purchase_date", "serial_number"]:
            return []
        sql = f"SELECT * FROM asset_inventory WHERE {keyword} LIKE %s"
        cursor.execute(sql, (like,))
        result = cursor.fetchall()
    conn.close()
    return result

# 5. Function to count the total number of assets
def count_assets_db():
    """
    Counts the total number of assets in the 'asset_inventory' table.
    Returns the total count or 0 if there is an issue.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS total FROM asset_inventory")
        result = cursor.fetchone()
    conn.close()
    return result["total"] if result else 0

# 6. Function to list assets by status
def list_assets_by_status_db(asset_status: str):
    """
    Lists all assets with the specified status.
    Returns the list of assets or None if the database connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        sql = "SELECT * FROM asset_inventory WHERE LOWER(asset_status) = LOWER(%s)"
        cursor.execute(sql, (asset_status,))
        result = cursor.fetchall()
    conn.close()
    return result

# 7. Function to update an asset's details
def update_asset_db(asset_id: int, asset: AssetModel):
    """
    Updates an existing asset's information in the 'asset_inventory' table.
    The asset ID must be provided, and all asset details will be updated.
    Returns True if the update is successful, or None if the database connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        sql = """UPDATE asset_inventory SET 
                 asset_tag=%s, asset_type=%s, serial_number=%s, manufacturer=%s, model=%s, 
                 purchase_date=%s, warranty_years=%s, condition_status=%s, assigned_to=%s, 
                 location=%s, asset_status=%s, last_updated=NOW()
                 WHERE asset_id=%s"""
        cursor.execute(sql, (
            asset.asset_tag, asset.asset_type, asset.serial_number, asset.manufacturer,
            asset.model, asset.purchase_date, asset.warranty_years, asset.condition_status,
            asset.assigned_to, asset.location, asset.asset_status, asset_id
        ))
        conn.commit()
    conn.close()
    return True

# 8. Function to update only the asset's status
def update_asset_status_db(asset_id: int, status: str):
    """
    Updates only the asset's status field in the 'asset_inventory' table.
    Returns True if the status is updated, or None if the database connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        cursor.execute("UPDATE asset_inventory SET asset_status=%s, last_updated=NOW() WHERE asset_id=%s", (status, asset_id))
        conn.commit()
    conn.close()
    return True

# 9. Function to delete an asset from the database
def delete_asset_db(asset_id: int):
    """
    Deletes an asset based on the provided asset ID from the 'asset_inventory' table.
    Returns True if the deletion is successful, or None if the database connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        conn.commit()
    conn.close()
    return True
