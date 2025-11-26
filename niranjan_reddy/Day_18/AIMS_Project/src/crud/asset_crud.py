# Importing necessary modules
from typing import Optional  # To handle optional parameters in function signatures
from tabulate import tabulate  # For formatting output as tables
from config.db_connection import get_connection  # To get the database connection
from helpers.validators import validate_asset  # To validate asset data before creating it

# Function to create a new asset in the system
def create_asset(asset_tag: str, asset_type: str, serial_number: str, manufacturer: str, model: str, purchase_date: str, warranty_years: int, assigned_to: Optional[str], asset_status: str):
    try:
        # Establish a connection to the database
        conn = get_connection()
        
        # Validate the asset details before inserting into the database
        validate_asset(conn, asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status)
        
        # Prepare the cursor and execute the SQL statement to insert the new asset
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ust_asset_db.asset_inventory (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status, last_updated)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
        """, (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status))
        
        # Commit the transaction and fetch the last inserted asset ID
        conn.commit()
        asset_id = cursor.lastrowid
        print(f"Asset created successfully : {asset_id}")
    except Exception as e:
        # Catch any exceptions that occur and print the error
        print("Error: ", e)
    finally:
        # Close the database connection
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed successfully")
            

# Function to read all assets, optionally filtering by status
def read_all_assets(status_filter="ALL"):
    try:
        # Establish a connection to the database
        conn = get_connection()
        cursor = conn.cursor()
        
        # If no filter is provided, fetch all assets, else filter by status
        if status_filter == "ALL":
            cursor.execute("SELECT * FROM asset_inventory ORDER BY asset_id ASC")
        else:
            cursor.execute("SELECT * FROM asset_inventory WHERE asset_status = %s ORDER BY asset_id ASC", (status_filter,))
        
        # Fetch all rows returned by the query
        row = cursor.fetchall()
        
        # If no rows are found, print a message, else format the output in a table
        if not row:
            print("No assets found.")
        else:
            print(tabulate(row, headers=["asset_id", "asset_tag", "asset_type", "serial_number", "manufacturer", "model", "purchase_date", "warranty_years", "assigned_to", "asset_status", "last_updated"]))
    
    except Exception as e:
        # Catch and print any exceptions
        print(f"Error: {e}")
    
    finally:
        # Close the database connection
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed successfully")


# Function to read a specific asset by its asset_id
def read_asset_by_id(asset_id):
    try:
        # Establish a connection to the database
        conn = get_connection()
        cursor = conn.cursor()
        
        # Query the database to get the asset by asset_id
        cursor.execute("SELECT * FROM ust_asset_db.asset_inventory WHERE asset_id= %s", (asset_id,))
        row = cursor.fetchone()
        
        # If the asset is found, print its details
        if row:
            print("Read asset by asset_id: ", end=" ")
            print(row)
        else:
            return [False, f"Asset not found. {asset_id}"]
    except Exception as e:
        # Catch and print any exceptions
        print("Error: ", e)
    finally:
        # Close the database connection
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed successfully")


# Function to update an existing asset's details
def update_asset(asset_id, asset_type, manufacturer, model, warranty_years, asset_status, assigned_to):
    try:
        # Establish a connection to the database
        conn = get_connection()
        cursor = conn.cursor()
        
        # Update the asset details using the provided parameters
        cursor.execute("UPDATE ust_asset_db.asset_inventory SET asset_type=%s, manufacturer=%s, model=%s, warranty_years=%s, asset_status=%s, assigned_to=%s WHERE asset_id=%s", 
                       (asset_type, manufacturer, model, warranty_years, asset_status, assigned_to, asset_id))
        
        # Commit the transaction
        conn.commit()
        print("Asset record updated successfully")
    except Exception as e:
        # Catch and print any exceptions
        print("Error: ", e)
    finally:
        # Close the database connection
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed successfully")
            

# Function to delete an asset by its asset_id
def delete_asset(asset_id):
    try:
        # Establish a connection to the database
        conn = get_connection()
        cursor = conn.cursor()
        
        # First, try to read the asset by its ID to check if it exists
        to_be_deleted, msg = read_asset_by_id(asset_id)
        if to_be_deleted:
            # If the asset exists, delete it from the database
            cursor.execute("DELETE FROM ust_asset_db.asset_inventory WHERE asset_id = %s", (asset_id,))
            conn.commit()
            print("Asset record deleted successfully!")
        else:
            # If the asset is not found, print the error message
            print(msg)
    except Exception as e:
        # Catch and print any exceptions
        print("Error: ", e)
    finally:
        # Close the database connection
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed successfully")
