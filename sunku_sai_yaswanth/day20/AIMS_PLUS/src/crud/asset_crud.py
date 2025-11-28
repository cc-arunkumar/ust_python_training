import csv
from typing import Optional
from src.models.asset_model import AssetInventory
from src.config.db_connection import get_connection

# Function to insert a new asset into the database
def insert_asset_to_db(new_asset: AssetInventory):
    try:
        # Get database connection and create a cursor for executing SQL queries
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if the serial number already exists in the asset inventory table
        cursor.execute("SELECT COUNT(*) FROM ust_aims_db.asset_inventory WHERE serial_number = %s", (new_asset.serial_number,))
        count = cursor.fetchone()[0]
        
        # If the serial number already exists, raise a ValueError
        if count > 0:
            raise ValueError(f"Serial number {new_asset.serial_number} already exists.")
        
        # Insert the new asset into the database if no duplicate serial number
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
        # Commit the transaction to save changes in the database
        conn.commit()
        
    except Exception as e:
        # Print error message if something goes wrong
        print(f"Error: {e}")
        
    finally:
        # Close the cursor and connection to the database
        if conn.open:
            cursor.close()
            conn.close()


# Function to retrieve all assets, optionally filtered by status
def read_all_assets(status_filter: Optional[str] = ""):
    try:
        # Get database connection and create a cursor
        conn = get_connection()
        cursor = conn.cursor()

        # If no status filter is provided, fetch all assets
        if status_filter == "":
            cursor.execute("SELECT * FROM ust_aims_db.asset_inventory")
        else:
            cursor.execute("SELECT * FROM ust_aims_db.asset_inventory WHERE asset_status = %s", (status_filter,))
        
        # Fetch all matching rows from the database
        row = cursor.fetchall()
        
        return row  # Return the result set
    except Exception as e:
        # Raise an exception in case of any error
        raise ValueError
    finally:
        # Close the cursor and connection to the database
        if conn:
            cursor.close()
            conn.close()


# Function to retrieve an asset by its ID
def read_asset_by_id(asset_id):
    try:
        # Get database connection and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # Query the database to find the asset by its ID
        cursor.execute("SELECT * FROM ust_aims_db.asset_inventory WHERE asset_id = %s", (asset_id,))
        row = cursor.fetchone()  # Fetch the first row (if any)
        
        if row:
            return row  # Return the asset details if found
        else:
            # Return an error message if the asset is not found
            return [False, f"Asset not found. {asset_id}"]
    except Exception as e:
        # Raise an exception in case of any error
        raise ValueError
    finally:
        # Close the cursor and connection to the database
        if conn:
            cursor.close()
            conn.close()


# Function to update an asset's details by its ID
def update_asset_by_id(asset_id: int, update_data: AssetInventory):
    try:
        # Get database connection and create a cursor
        conn = get_connection()
        cursor = conn.cursor()

        # Check if the asset exists before attempting to update it
        if read_asset_by_id(asset_id):
            # Execute the SQL update statement
            cursor.execute(
                """
                UPDATE ust_aims_db.asset_inventory 
                SET asset_tag = %s, asset_type = %s, serial_number = %s, 
                    manufacturer = %s, model = %s, warranty_years = %s, 
                    condition_status = %s, assigned_to = %s, location = %s, 
                    asset_status = %s 
                WHERE asset_id = %s
                """, 
                (update_data.asset_tag, update_data.asset_type, update_data.serial_number, 
                 update_data.manufacturer, update_data.model, update_data.warranty_years, 
                 update_data.condition_status, update_data.assigned_to, 
                 update_data.location, update_data.asset_status, update_data.asset_id)
            )
            # Commit the transaction to apply changes
            conn.commit()
            return True  # Return True indicating the update was successful
        else:
            # If the asset is not found, raise an error
            raise ValueError
    except Exception as e:
        # Raise an exception if something goes wrong
        raise ValueError
    finally:
        # Close the cursor and connection to the database
        if conn:
            cursor.close()
            conn.close()
            

# Function to delete an asset by its ID
def delete_asset(asset_id):
    try:
        # Get database connection and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if the asset exists before attempting to delete it
        if read_asset_by_id(asset_id):
            # Execute the SQL delete statement
            cursor.execute("DELETE FROM ust_aims_db.asset_inventory WHERE asset_id = %s", (asset_id,))
            # Commit the transaction to apply changes
            conn.commit()
            return True  # Return True indicating the deletion was successful
        else:
            # If the asset is not found, raise an error
            raise ValueError
        
    except Exception as e:
        # Raise an exception if something goes wrong
        raise ValueError
    finally:
        # Close the cursor and connection to the database
        if conn:
            cursor.close()
            conn.close()


# Function to search assets based on a field and keyword (e.g., asset_tag, manufacturer)
def search_assets(field_type: str, keyword: str):
    try:
        # Get database connection and create a cursor
        conn = get_connection()
        cursor = conn.cursor()
        
        # Construct and execute the SQL query to search for the asset
        cursor.execute(f"SELECT * FROM ust_aims_db.asset_inventory WHERE {field_type} LIKE %s", (f'%{keyword}%',))
        data = cursor.fetchall()  # Fetch all matching rows
        
        return data  # Return the search results
    except Exception as e:
        # Raise an exception if something goes wrong
        raise Exception(f"Error: {e}")
    finally:
        # Close the cursor and connection to the database
        if conn.open:
            cursor.close()
            conn.close()

# The commented code below is for handling CSV data for bulk asset insertion.
# It processes the input CSV file, validates the rows, and writes valid and invalid rows to separate files.

# valid_rows_asset = []
# invalid_rows_asset = []

# required_fields_asset = [
#     "asset_tag", "asset_type", "serial_number", "manufacturer", "model", 
#     "purchase_date", "warranty_years", "condition_status", "assigned_to", 
#     "location", "asset_status"
# ]

# with open("asset_inventory.csv", "r") as file:
#     csv_reader = csv.DictReader(file)

#     for row in csv_reader:
#         try:
#             valid = AssetInventory(**row)
#             valid_rows_asset.append(valid.model_dump())  
#         except Exception as e:
#             row['error'] = str(e)  
#             invalid_rows_asset.append(row)

# fieldnames_asset_invalid = [
#     "asset_id", "asset_tag", "asset_type", "serial_number", "manufacturer", "model", 
#     "purchase_date", "warranty_years", "condition_status", "assigned_to", "location", 
#     "asset_status", "last_updated", "error" 
# ]
# fieldnames_asset_valid = [
#      "asset_tag", "asset_type", "serial_number", "manufacturer", "model", 
#     "purchase_date", "warranty_years", "condition_status", "assigned_to", "location", 
#     "asset_status", "last_updated"
# ]

# with open("validated_asset_inventory.csv", "w", newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames_asset_valid)
#     writer.writeheader()
    
#     for row in valid_rows_asset:
#         row.pop('asset_id', None)
#         if 'last_updated' in row:
#             row['last_updated'] = row['last_updated'].strftime('%Y-%m-%d %H:%M:%S') 
#         writer.writerow(row)

# with open("invalid_rows.csv", "w", newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames_asset_invalid)
#     writer.writeheader()
#     for row in invalid_rows_asset:
#         writer.writerow(row)
