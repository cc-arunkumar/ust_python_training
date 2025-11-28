import csv
from typing import Optional
from src.models.asset_model import AssetInventory
from src.config.db_connection import get_connection



# Function to insert a new asset into the database
def insert_asset_to_db(new_asset: AssetInventory):
    try:
        # Establishing connection to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Check if the serial number already exists in the database
        cursor.execute("SELECT COUNT(*) FROM ust_aims_db.asset_inventory WHERE serial_number = %s", (new_asset.serial_number,))
        count = cursor.fetchone()[0]

        # If the serial number already exists, raise an error
        if count > 0:
            raise ValueError(f"Serial number {new_asset.serial_number} already exists.")
        
        # Insert the new asset if no duplicate found
        cursor.execute(
            """
            INSERT INTO ust_aims_db.asset_inventory(
                asset_tag, asset_type, serial_number, manufacturer, model, 
                purchase_date, warranty_years, condition_status, assigned_to, 
                location, asset_status, last_updated
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
            """, (
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
        # Print error if any issue occurs during insertion
        print(f"Error: {e}")
        
    finally:
        # Close the database connection
        if conn.open:
            cursor.close()
            conn.close()

# Function to retrieve all assets from the database, with optional status filter
def read_all_assets(status_filter: Optional[str] = ""):
    try:
        # Establishing connection to the database
        conn = get_connection()
        cursor = conn.cursor()
        
        # Execute query based on the provided status filter
        if status_filter == "":
            cursor.execute("SELECT * FROM ust_aims_db.asset_inventory")
        else:
            cursor.execute("SELECT * FROM ust_aims_db.asset_inventory WHERE asset_status=%s", (status_filter,))

        # Fetch all rows
        row = cursor.fetchall()
        return row
    except Exception as e:
        # Raise error if something goes wrong
        raise ValueError
    
    finally:
        # Close the connection to the database
        if conn:
            cursor.close()
            conn.close()

# Function to retrieve an asset by its asset_id
def read_asset_by_id(asset_id):
    try:
        # Establishing connection to the database
        conn = get_connection()
        cursor = conn.cursor()
        
        # Query to fetch asset data by asset_id
        cursor.execute("SELECT * FROM ust_aims_db.asset_inventory WHERE asset_id= %s", (asset_id,))
        row = cursor.fetchone()

        # Return asset data if found, else return an error message
        if row:
            return row
        else:
            return [False, f"Asset not found. {asset_id}"]
    except Exception as e:
        # Raise error if something goes wrong
        raise ValueError
    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()

# Function to update an asset's data by asset_id
def update_asset_by_id(asset_id: int, update_data: AssetInventory):
    try:
        # Establishing connection to the database
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if the asset exists
        if read_asset_by_id(asset_id):
            # Execute update query
            cursor.execute("UPDATE ust_aims_db.asset_inventory SET asset_tag=%s,asset_type=%s,serial_number=%s, manufacturer=%s, model=%s, warranty_years=%s,condition_status=%s, assigned_to=%s,location=%s, asset_status=%s WHERE asset_id=%s", 
                        (update_data.asset_tag, update_data.asset_type, update_data.serial_number, update_data.manufacturer, update_data.model, update_data.warranty_years, update_data.condition_status, update_data.assigned_to, update_data.location, update_data.asset_status, update_data.asset_id))
            conn.commit()
            return True
        else:
            raise ValueError
    except Exception as e:
        # Raise error if something goes wrong
        raise ValueError
    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()

# Function to delete an asset from the database by asset_id
def delete_asset(asset_id):
    try:
        # Establishing connection to the database
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if the asset exists before deleting
        if read_asset_by_id(asset_id):
            cursor.execute("DELETE FROM ust_aims_db.asset_inventory WHERE asset_id = %s", (asset_id,))
            conn.commit()
            return True
        else:
            # Raise error if asset is not found
            raise ValueError
        
    except Exception as e:
        # Raise error if something goes wrong
        raise ValueError
    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()

# Function to search assets based on a field and keyword
def search_assets(field_type: str, keyword: str):
    try:
        # Establishing connection to the database
        conn = get_connection()
        cursor = conn.cursor()
        
        # Execute search query with the given field and keyword
        cursor.execute(f"SELECT * FROM ust_aims_db.asset_inventory WHERE {field_type} LIKE %s", (f'%{keyword}%',))
        data = cursor.fetchall()
        return data
    except Exception as e:
        # Raise error if something goes wrong
        raise Exception(f"Error: {e}")
    finally:
        # Close the connection
        if conn.open:
            cursor.close()
            conn.close()
 