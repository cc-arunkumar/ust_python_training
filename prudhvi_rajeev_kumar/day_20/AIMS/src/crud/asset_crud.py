# Import necessary modules: Database connection utility and AssetInventory model
from src.config.db_connection import get_connection
from src.models.asset_model import AssetInventory

# Function to create a new asset in the database
import datetime

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
                asset.location, asset.asset_status,
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # last_updated
            ))
            conn.commit()
            return cursor.lastrowid
    finally:
        conn.close()

# Function to retrieve an asset by its ID
def get_asset_by_id(asset_id: int):
    # Establish a connection to the database
    conn = get_connection()
    try:
        # Use a cursor to execute the SQL query
        with conn.cursor() as cursor:
            # Execute the query to get asset by asset_id
            cursor.execute("SELECT * FROM asset_inventory WHERE asset_id=%s", (asset_id,))
            # Return the first result (should be a single asset)
            return cursor.fetchone()
    finally:
        # Ensure the database connection is always closed
        conn.close()

# Function to get all assets from the database
def get_all_assets():
    # Establish a connection to the database
    conn = get_connection()
    try:
        # Use a cursor to execute the SQL query
        with conn.cursor() as cursor:
            # Execute the query to get all assets
            cursor.execute("SELECT * FROM asset_inventory")
            # Return all the results
            return cursor.fetchall()
    finally:
        # Ensure the database connection is always closed
        conn.close()

# Function to get assets based on their status
def get_assets_by_status(status: str):
    # Establish a connection to the database
    conn = get_connection()
    try:
        # Use a cursor to execute the SQL query
        with conn.cursor() as cursor:
            # Execute the query to get assets with the given status
            cursor.execute("SELECT * FROM asset_inventory WHERE asset_status=%s", (status,))
            # Return all the matching assets
            return cursor.fetchall()
    finally:
        # Ensure the database connection is always closed
        conn.close()

# Function to search assets based on a given column and value
def search_assets(column_name: str, value : str):
    # Establish a connection to the database
    conn = get_connection()
    try:
        # List of allowed column names for validation
        allowed_columns = [
            "asset_id", "asset_tag", "asset_type", "serial_number", "manufacturer",
            "model", "purchase_date", "warranty_years", "condition_status",
            "assigned_to", "location", "asset_status", "last_updated"
        ]
        # Check if the given column name is valid
        if column_name not in allowed_columns:
            raise ValueError("Invalid Column name.")  # Raise error if invalid column
        # Construct and execute the SQL query for searching assets
        sql = f"SELECT * FROM asset_inventory WHERE {column_name} = %s"
        with conn.cursor() as cursor:
            cursor.execute(sql, (value,))
            # Return all the matching assets
            return cursor.fetchall()
    finally:
        # Ensure the database connection is always closed
        conn.close()

# Function to count the total number of assets
def count_assets():
    # Get all assets and return their count
    assets = get_all_assets()
    return len(assets)

# Function to update an asset in the database by its ID
def update_asset(asset_id: int, asset: AssetInventory):
    # Establish a connection to the database
    conn = get_connection()
    try:
        # Use a cursor to execute the SQL query
        with conn.cursor() as cursor:
            # Define the SQL query to update an existing asset
            sql = """
            UPDATE asset_inventory
            SET asset_tag=%s, asset_type=%s, serial_number=%s, manufacturer=%s, model=%s,
                purchase_date=%s, warranty_years=%s, condition_status=%s, assigned_to=%s,
                location=%s, asset_status=%s, last_updated=%s
            WHERE asset_id=%s
            """
            # Execute the query with values from the asset object and the asset_id
            cursor.execute(sql, (
                asset.asset_tag, asset.asset_type, asset.serial_number, asset.manufacturer,
                asset.model, asset.purchase_date, asset.warranty_years, asset.condition_status,
                asset.assigned_to, asset.location, asset.asset_status, asset.last_updated,
                asset_id
            ))
            # Commit the transaction to the database
            conn.commit()
            # Return the number of affected rows (should be 1 if successful)
            return cursor.rowcount
    finally:
        # Ensure the database connection is always closed
        conn.close()

# Function to update the status of an asset
def update_asset_status(asset_id: int, new_status: str):
    # Establish a connection to the database
    conn = get_connection()
    try:
        # Use a cursor to execute the SQL query
        with conn.cursor() as cursor:
            # Execute the query to update the asset's status
            cursor.execute("UPDATE asset_inventory SET asset_status=%s WHERE asset_id=%s",
                           (new_status, asset_id))
            # Commit the transaction to the database
            conn.commit()
            # Return the number of affected rows (should be 1 if successful)
            return cursor.rowcount
    finally:
        # Ensure the database connection is always closed
        conn.close()

# Function to delete an asset from the database by its ID
def delete_asset(asset_id: int):
    # Establish a connection to the database
    conn = get_connection()
    try:
        # Use a cursor to execute the SQL query
        with conn.cursor() as cursor:
            # Execute the query to delete the asset
            cursor.execute("DELETE FROM asset_inventory WHERE asset_id=%s", (asset_id,))
            # Commit the transaction to the database
            conn.commit()
            # Return the number of affected rows (should be 1 if successful)
            return cursor.rowcount
    finally:
        # Ensure the database connection is always closed
        conn.close()
