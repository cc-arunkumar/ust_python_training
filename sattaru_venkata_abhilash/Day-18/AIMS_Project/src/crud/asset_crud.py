# Importing necessary modules for logging, database connection, and validation functions
import logging
import os
from config.db_connection import get_connection
from helpers.validators import validate_asset_tag, validate_asset_type, validate_warranty_years, validate_assigned_to, validate_asset_status, validate_serial_number, validate_asset_tag_unique

# Ensure the 'logs' directory exists for storing log files
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging to write logs to a file with a detailed format
logging.basicConfig(
    filename='logs/app.log',  # Log file location
    level=logging.DEBUG,  # Set logging level to capture DEBUG messages and higher
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define format for log messages
    datefmt='%Y-%m-%d %H:%M:%S'  # Specify timestamp format for log entries
)

# Log an informational message indicating the system initialization
logging.info('🚀 Asset Inventory Management System Initialized')

# Function to create a new asset in the inventory
def create_asset(asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status):
    cursor = None  # Initialize cursor here to ensure it's available in the finally block
    try:
        # Log the initiation of asset creation with the provided details
        logging.debug(f"🔄 Initiating asset creation with tag: {asset_tag}, serial: {serial_number}")
        
        # Validate the input values for the asset creation
        if not asset_tag.startswith("UST-"):
            raise ValueError("Asset tag must start with 'UST-'")
        if asset_type not in ["Laptop", "Monitor", "Docking Station", "Keyboard", "Mouse"]:
            raise ValueError("Invalid asset type")
        if warranty_years <= 0:
            raise ValueError("Warranty years must be greater than 0")
        if asset_status not in ["Available", "Assigned", "Repair", "Retired"]:
            raise ValueError("Invalid asset status")
        if asset_status == "Assigned" and not assigned_to:
            raise ValueError("Assigned to must not be null if asset status is 'Assigned'")
        if asset_status in ["Available", "Retired"] and assigned_to:
            raise ValueError("Assigned to must be null if asset status is 'Available' or 'Retired'")

        # Check if the asset tag or serial number already exists in the database
        conn = get_connection()
        cursor = conn.cursor()  # Initialize cursor for executing queries
        cursor.execute("SELECT asset_tag, serial_number FROM asset_inventory WHERE asset_tag = %s OR serial_number = %s", (asset_tag, serial_number))
        if cursor.fetchone():
            raise ValueError("Asset tag or serial number already exists.")
        
        # Insert the new asset into the database
        cursor.execute("""
            INSERT INTO asset_inventory (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status, last_updated)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
        """, (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status))
        
        conn.commit()  # Commit the changes to the database
        asset_id = cursor.lastrowid  # Get the ID of the last inserted asset
        logging.info(f"✅ Asset created successfully! Asset ID: {asset_id}, Tag: {asset_tag}, Status: {asset_status}")
        return f"🎉 Asset created successfully. Asset ID: {asset_id}"

    except Exception as e:
        # Log any error that occurs during the asset creation process
        logging.error(f"❌ Error creating asset: {str(e)}")
        return f"❌ Error: {str(e)}"
    
    finally:
        # Ensure the cursor and connection are closed after the operation to release resources
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Function to read all assets, optionally filtered by a specific status
def read_all_assets(status_filter="ALL"):
    try:
        # Log the status filter being used for reading assets
        logging.debug(f"🔄 Fetching assets with status filter: {status_filter}")
        
        # Establish a database connection and prepare to fetch assets
        conn = get_connection()
        cursor = conn.cursor()

        # Query assets based on the status filter
        if status_filter == "ALL":
            cursor.execute("SELECT * FROM asset_inventory ORDER BY asset_id ASC")
        else:
            cursor.execute("SELECT * FROM asset_inventory WHERE asset_status = %s ORDER BY asset_id ASC", (status_filter,))
        
        assets = cursor.fetchall()  # Fetch all assets that match the criteria
        if assets:
            # Log and print the assets retrieved
            logging.info(f"✅ Retrieved {len(assets)} assets.")
            for asset in assets:
                print(f"📑 Asset ID: {asset[0]}, Tag: {asset[1]}, Type: {asset[2]}, Serial: {asset[3]}, Manufacturer: {asset[4]}, Model: {asset[5]}, Status: {asset[8]}")
        else:
            logging.info("❗ No assets found.")
            print("❗ No assets found.")
    
    except Exception as e:
        # Log any error that occurs while fetching the assets
        logging.error(f"❌ Error reading assets: {str(e)}")
    
    finally:
        # Close the cursor and connection to release resources
        cursor.close()
        conn.close()

# Function to read a single asset by its ID
def read_asset_by_id(asset_id):
    try:
        # Log the asset ID being fetched
        logging.debug(f"🔄 Fetching asset with ID: {asset_id}")
        
        # Establish database connection and query for the asset
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id = %s", (asset_id,))
        asset = cursor.fetchone()  # Fetch a single asset by ID
        
        if asset:
            # Log and print asset details if found
            logging.info(f"✅ Asset found: ID: {asset[0]}")
            print(f"📑 Asset ID: {asset[0]}, Tag: {asset[1]}, Type: {asset[2]}, Serial: {asset[3]}, Manufacturer: {asset[4]}, Model: {asset[5]}, Status: {asset[8]}")
        else:
            # Log and print a message if the asset isn't found
            logging.warning(f"❗ Asset not found with ID: {asset_id}")
            print("❗ Asset not found.")
    
    except Exception as e:
        # Log any error that occurs while reading the asset
        logging.error(f"❌ Error reading asset by ID: {str(e)}")
    
    finally:
        # Close the cursor and connection to release resources
        cursor.close()
        conn.close()

# Function to update the details of an existing asset
def update_asset(asset_id, asset_type=None, manufacturer=None, model=None, warranty_years=None, asset_status=None, assigned_to=None):
    try:
        # Log the asset ID being updated
        logging.debug(f"🔄 Updating asset with ID: {asset_id}")
        
        # Establish a connection and check if the asset exists
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id = %s", (asset_id,))
        
        if not cursor.fetchone():
            # Log and return a message if the asset does not exist
            logging.warning(f"❗ Asset not found with ID: {asset_id}")
            return "❗ Asset not found."
        
        # Update the asset details if the asset exists
        cursor.execute("""
            UPDATE asset_inventory
            SET asset_type = COALESCE(%s, asset_type), manufacturer = COALESCE(%s, manufacturer),
                model = COALESCE(%s, model), warranty_years = COALESCE(%s, warranty_years),
                asset_status = COALESCE(%s, asset_status), assigned_to = COALESCE(%s, assigned_to), last_updated = NOW()
            WHERE asset_id = %s
        """, (asset_type, manufacturer, model, warranty_years, asset_status, assigned_to, asset_id))

        conn.commit()  # Commit the changes to the database
        logging.info(f"✅ Asset with ID: {asset_id} updated successfully.")
        return "🎉 Asset updated successfully."

    except Exception as e:
        # Log any error that occurs while updating the asset
        logging.error(f"❌ Error updating asset: {str(e)}")
        return f"❌ Error: {str(e)}"
    
    finally:
        # Close the cursor and connection to release resources
        cursor.close()
        conn.close()

# Function to delete an asset by its ID
def delete_asset(asset_id):
    try:
        # Log the asset ID being deleted
        logging.debug(f"🔄 Deleting asset with ID: {asset_id}")
        
        # Establish connection and check if the asset exists
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id = %s", (asset_id,))
        
        if not cursor.fetchone():
            # Log and return a message if the asset isn't found
            logging.warning(f"❗ Asset not found with ID: {asset_id}")
            return "❗ Asset not found."
        
        # Delete the asset from the database
        cursor.execute("DELETE FROM asset_inventory WHERE asset_id = %s", (asset_id,))
        conn.commit()  # Commit the deletion to the database
        logging.info(f"✅ Asset with ID: {asset_id} deleted successfully.")
        return "🎉 Asset deleted successfully."

    except Exception as e:
        # Log any error that occurs while deleting the asset
        logging.error(f"❌ Error deleting asset: {str(e)}")
        return f"❌ Error: {str(e)}"
    
    finally:
        # Close the cursor and connection to release resources
        cursor.close()
        conn.close()
