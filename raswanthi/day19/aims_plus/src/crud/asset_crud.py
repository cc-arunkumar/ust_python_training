from src.config.db_connection import get_connection   # Import function to establish DB connection
from ..models.asset_model import AssetInventory       # Import AssetInventory model


# ------------------- CREATE -------------------
def create_asset_db(asset: AssetInventory):
    """
    Insert a new asset record into the database.
    - Accepts an AssetInventory object.
    - Returns True if insertion is successful, None if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        sql = """INSERT INTO asset_inventory 
                 (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, 
                  warranty_years, condition_status, assigned_to, location, asset_status, last_updated)
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())"""
        # Execute SQL insert with asset details
        cursor.execute(sql, (
            asset.asset_tag, asset.asset_type, asset.serial_number, asset.manufacturer,
            asset.model, asset.purchase_date, asset.warranty_years, asset.condition_status,
            asset.assigned_to, asset.location, asset.asset_status
        ))
        conn.commit()  # Commit transaction
    conn.close()
    return True


# ------------------- READ ALL -------------------
def get_all_assets_db(status=None):
    """
    Retrieve all assets from the database.
    - Optional filter by asset_status.
    - Returns list of assets or None if DB connection fails.
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


# ------------------- READ BY ID -------------------
def get_asset_by_id_db(asset_id: int):
    """
    Retrieve a single asset by its ID.
    - Returns asset record or None if not found/DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        result = cursor.fetchone()
    conn.close()
    return result


# ------------------- SEARCH -------------------
def search_assets_db(keyword: str, value: str):
    """
    Search assets dynamically by a given column (keyword) and value.
    - Uses LIKE for partial matches.
    - Only allows specific safe columns to prevent SQL injection.
    - Returns list of matching assets or empty list if keyword invalid.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        like = f"%{value}%"
        # Validate keyword to prevent SQL injection
        if keyword not in [
            "asset_tag", "model", "manufacturer", "purchase_date", "asset_id",
            "asset_type", "warranty_years", "condition_status", "assigned_to",
            "location", "serial_number"
        ]:
            return []
        sql = f"SELECT * FROM asset_inventory WHERE {keyword} LIKE %s"
        cursor.execute(sql, (like,))
        result = cursor.fetchall()
    conn.close()
    return result


# ------------------- COUNT -------------------
def count_assets_db():
    """
    Count total number of assets in the database.
    - Returns integer count or None if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM asset_inventory")
        result = cursor.fetchone()
    conn.close()
    return result


# ------------------- LIST BY STATUS -------------------
def list_assets_by_status_db(asset_status: str):
    """
    Retrieve all assets filtered by status (case-insensitive).
    - Returns list of assets or None if DB connection fails.
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


# ------------------- UPDATE -------------------
def update_asset_db(asset_id: int, asset: AssetInventory):
    """
    Update an existing asset record by ID.
    - Accepts AssetInventory object with updated fields.
    - Returns True if update is successful, None if DB connection fails.
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


# ------------------- UPDATE STATUS -------------------
def update_asset_status_db(asset_id: int, status: str):
    """
    Update only the status of an asset by ID.
    - Returns True if update is successful, None if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        cursor.execute(
            "UPDATE asset_inventory SET asset_status=%s, last_updated=NOW() WHERE asset_id=%s",
            (status, asset_id)
        )
        conn.commit()
    conn.close()
    return True


# ------------------- DELETE -------------------
def delete_asset_db(asset_id: int):
    """
    Delete an asset record by ID.
    - Returns True if deletion is successful, None if DB connection fails.
    """
    conn = get_connection()
    if conn is None:
        return None
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        conn.commit()
    conn.close()
    return True
