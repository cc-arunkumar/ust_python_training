import csv  # Importing the csv module to handle CSV file operations
from typing import Optional  # Importing Optional for optional type annotations
from src.models.asset_model import AssetInventory  # Importing the AssetInventory model
from src.config.db_connection import get_connection  # Importing the get_connection function to establish DB connection

# This function inserts a new asset into the database
def insert_asset_to_db(new_asset: AssetInventory):
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object to interact with the database
        
        # Check if the serial_number already exists in the database
        cursor.execute("SELECT COUNT(*) FROM ust_aims_db.asset_inventory WHERE serial_number = %s", (new_asset.serial_number,))
        count = cursor.fetchone()[0]
        
        # If the serial number exists, raise a ValueError to prevent duplicates
        if count > 0:
            raise ValueError(f"Serial number {new_asset.serial_number} already exists.")
        
        # If no duplicate, proceed with inserting the new asset into the database
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
        conn.commit()  # Commit the transaction to the database
        
    except Exception as e:
        print(f"Error: {e}")  # Print any errors that occur during insertion
        
    finally:
        if conn.open:  # Close the connection if it's open
            cursor.close()
            conn.close()

# This function retrieves all assets from the database, optionally filtered by status
def read_all_assets(status_filter: Optional[str] = ""):
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object to interact with the database
        
        # If no status filter is provided, fetch all assets; otherwise, fetch assets by status
        if status_filter == "":
            cursor.execute("SELECT * FROM ust_aims_db.asset_inventory")
        else:
            cursor.execute("SELECT * FROM ust_aims_db.asset_inventory WHERE asset_status=%s", (status_filter,))
        
        row = cursor.fetchall()  # Fetch all results
        
        return row  # Return the fetched rows
    except Exception as e:
        raise ValueError  # Raise a ValueError if any error occurs during fetching
    finally:
        if conn:  # Close the connection if it's open
            cursor.close()
            conn.close()

# This function retrieves an asset by its ID
def read_asset_by_id(asset_id):
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Execute the SQL query to fetch the asset by its ID
        cursor.execute("SELECT * FROM ust_aims_db.asset_inventory WHERE asset_id= %s", (asset_id,))
        row = cursor.fetchone()  # Fetch a single row
        
        if row:  # If the asset is found, return the row
            return row
        else:  # If the asset is not found, return a custom error message
            return [False, f"Asset not found. {asset_id}"]
    except Exception as e:
        raise ValueError  # Raise a ValueError if any error occurs during fetching
    finally:
        if conn:  # Close the connection if it's open
            cursor.close()
            conn.close()

# This function updates an asset's details by its ID
def update_asset_by_id(asset_id: int, update_data: AssetInventory):
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Check if the asset exists before trying to update it
        if read_asset_by_id(asset_id):
            cursor.execute(
                "UPDATE ust_aims_db.asset_inventory SET asset_tag=%s, asset_type=%s, serial_number=%s, manufacturer=%s, model=%s, warranty_years=%s, condition_status=%s, assigned_to=%s, location=%s, asset_status=%s WHERE asset_id=%s", 
                (update_data.asset_tag, update_data.asset_type, update_data.serial_number, update_data.manufacturer, update_data.model, update_data.warranty_years, update_data.condition_status, update_data.assigned_to, update_data.location, update_data.asset_status, update_data.asset_id)
            )
            
            conn.commit()  # Commit the transaction to the database
            return True  # Return True indicating the update was successful
        else:
            raise ValueError  # Raise a ValueError if the asset is not found
    except Exception as e:
        raise ValueError  # Raise a ValueError if any error occurs during updating
    finally:
        if conn:  # Close the connection if it's open
            cursor.close()
            conn.close()

# This function deletes an asset by its ID
def delete_asset(asset_id):
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Check if the asset exists before attempting to delete it
        if read_asset_by_id(asset_id):
            cursor.execute("DELETE FROM ust_aims_db.asset_inventory WHERE asset_id = %s", (asset_id,))
            conn.commit()  # Commit the deletion to the database
            return True  # Return True indicating the deletion was successful
        else:
            # If the asset is not found, raise an error
            raise ValueError
        
    except Exception as e:
        # Catch and handle any exceptions that occur during deletion
        raise ValueError
    finally:
        # Close the database connection
        if conn:
            cursor.close()
            conn.close()

# This function searches assets based on a specific field and keyword
def search_assets(field_type: str, keyword: str):
    try:
        conn = get_connection()  # Establish a connection to the database
        cursor = conn.cursor()  # Create a cursor object
        
        # Execute the SQL query to search assets based on the field and keyword
        cursor.execute(f"SELECT * FROM ust_aims_db.asset_inventory WHERE {field_type} LIKE %s", (f'%{keyword}%',))
        data = cursor.fetchall()  # Fetch all matching results
        return data  # Return the search results
   
    except Exception as e:
        # If an error occurs during the search, raise an exception with the error message
        raise Exception(f"Error: {e}")
   
    finally:
        if conn.open:  # Ensure the connection is closed properly
            cursor.close()
            conn.close()