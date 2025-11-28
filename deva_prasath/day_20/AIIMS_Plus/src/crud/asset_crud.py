import pymysql  # MySQL connector for database interaction
from typing import Optional, List  # Type hinting for Optional and List
from ..models.asset_model import AssetCreate  # Importing AssetCreate model from asset_model

# Function to establish a connection to the MySQL database
def get_db_connection():
    return pymysql.connect(
        host="localhost",  # Database host
        user="root",  # Database username
        password="pass@word1",  # Database password
        database="aiims",  # Database name
    )

# Function to get assets, optionally filtered by status
def get_assets(status: Optional[str] = None):
    print("at crud")
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor for database operations
    print("Connection established")
    try:
        if status:  # If status filter is provided
            cursor.execute("select * FROM asset_inventory WHERE asset_status=%s", (status,))
        else:  # No filter, return all assets
            cursor.execute("select * FROM asset_inventory")
            print("query executed")
        return cursor.fetchall()  # Return all the fetched assets
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection
        print("closed")

# Function to get a specific asset by its ID
def get_asset_by_id(asset_id: int):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute("select * FROM aiims.asset_inventory WHERE asset_id=%s", (asset_id,))
        return cursor.fetchone()  # Return the asset data
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to create a new asset in the database
def create_asset(ob: AssetCreate):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute(
            """
            INSERT INTO asset_inventory(asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, 
            warranty_years, condition_status, assigned_to, location, asset_status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                ob.asset_tag,  # Asset tag
                ob.asset_type,  # Asset type
                ob.serial_number,  # Serial number
                ob.manufacturer,  # Manufacturer
                ob.model,  # Model
                ob.purchase_date,  # Purchase date
                ob.warranty_years,  # Warranty years
                ob.condition_status,  # Condition status
                ob.assigned_to,  # Assigned to
                ob.location,  # Location
                ob.asset_status  # Asset status
            )
        )
        conn.commit()  # Commit transaction
    except Exception as e:  # Handle any exceptions
        raise e
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to update an existing asset's information
def update_asset(asset_id: int, ob: AssetCreate):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create a cursor
    try:
        cursor.execute(
            """
            UPDATE asset_inventory 
            SET asset_tag = %s, asset_type = %s, serial_number = %s, manufacturer = %s, model = %s, 
                purchase_date = %s, warranty_years = %s, condition_status = %s, assigned_to = %s, 
                location = %s, asset_status = %s
            WHERE asset_id = %s
            """, (
                ob.asset_tag,  # Asset tag
                ob.asset_type,  # Asset type
                ob.serial_number,  # Serial number
                ob.manufacturer,  # Manufacturer
                ob.model,  # Model
                ob.purchase_date,  # Purchase date
                ob.warranty_years,  # Warranty years
                ob.condition_status,  # Condition status
                ob.assigned_to,  # Assigned to
                ob.location,  # Location
                ob.asset_status,  # Asset status
                asset_id  # Asset ID to update
            )
        )
        conn.commit()  # Commit transaction
    except Exception as e:  # Handle any exceptions
        raise e
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to update the status of an asset
def update_asset_status(asset_id: int, asset_status: str):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create cursor for dictionary output
    try:
        cursor.execute(
            "update asset_inventory SET asset_status = %s WHERE asset_id = %s", (asset_status, asset_id)
        )
        conn.commit()  # Commit transaction
    except Exception as e:  # Handle any exceptions
        raise e
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to delete an asset by its ID
def delete_asset(asset_id: int):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create cursor
    try:
        cursor.execute("delete from asset_inventory WHERE asset_id = %s", (asset_id,))
        conn.commit()  # Commit transaction
    except Exception as e:  # Handle any exceptions
        raise e
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

# Function to search for assets based on a keyword
def search_assets(keyword: str):
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create cursor
    try:
        query = """
        select * FROM asset_inventory WHERE 
        asset_tag LIKE %s OR 
        model LIKE %s OR 
        manufacturer LIKE %s
        """
        like_keyword = f"%{keyword}%"  # Prepare the keyword for SQL LIKE query
        cursor.execute(query, (like_keyword, like_keyword, like_keyword))
        return cursor.fetchall()  # Return all results
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection




# Function to count the total number of assets
def count_assets():
    conn = get_db_connection()  # Get database connection
    cursor = conn.cursor()  # Create cursor
    try:
        cursor.execute("SELECT COUNT(*) FROM asset_inventory")  # Count all assets
        return cursor.fetchone()[0]  # Return the count
    finally:
        cursor.close()  # Close cursor
        conn.close()  # Close connection

