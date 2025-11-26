# Importing necessary modules for logging and file handling
import logging
import os

# Ensure the 'logs' directory exists for storing log files
if not os.path.exists('logs'):
    os.makedirs('logs')

# Set up logging configuration to capture logs into a file with detailed information
logging.basicConfig(
    filename='logs/app.log',  # Log file location
    level=logging.DEBUG,  # Ensure it captures DEBUG messages and higher (INFO, WARNING, ERROR, etc.)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define log message format
    datefmt='%Y-%m-%d %H:%M:%S'  # Define timestamp format for log entries
)

# Function to validate asset tag format
def validate_asset_tag(asset_tag):
    logging.debug(f"Validating asset tag: {asset_tag}")  # Log debug message for validation attempt
    if asset_tag.startswith("UST-"):  # Check if the asset tag starts with 'UST-'
        logging.info(f"Validation success: Asset tag '{asset_tag}' is valid and follows the 'UST-' format.")  # Log success message
        return True
    else:
        logging.warning(f"Validation failed: Asset tag '{asset_tag}' is invalid. It must start with 'UST-'.")  # Log warning message on failure
        return False

# Function to validate asset type
def validate_asset_type(asset_type):
    logging.debug(f"Validating asset type: {asset_type}")  # Log debug message for validation attempt
    valid_types = ["Laptop", "Monitor", "Docking Station", "Keyboard", "Mouse"]  # Define valid asset types
    if asset_type in valid_types:  # Check if the asset type is in the valid types list
        logging.info(f"Validation success: Asset type '{asset_type}' is recognized as a valid type.")  # Log success message
        return True
    else:
        logging.warning(f"Validation failed: Asset type '{asset_type}' is invalid. Must be one of {valid_types}.")  # Log warning on failure
        return False

# Function to validate warranty years
def validate_warranty_years(warranty_years):
    logging.debug(f"Validating warranty years: {warranty_years}")  # Log debug message for validation attempt
    if warranty_years > 0:  # Check if the warranty years is greater than 0
        logging.info(f"Validation success: Warranty years '{warranty_years}' is valid. Warranty period is greater than 0.")  # Log success message
        return True
    else:
        logging.warning(f"Validation failed: Warranty years '{warranty_years}' is invalid. It must be greater than 0.")  # Log warning on failure
        return False

# Function to validate 'assigned_to' field based on asset status
def validate_assigned_to(asset_status, assigned_to):
    logging.debug(f"Validating 'assigned_to' for status '{asset_status}' and assigned_to '{assigned_to}'")  # Log debug message
    if asset_status == "Assigned" and not assigned_to:  # If asset is assigned, 'assigned_to' must not be empty
        logging.warning(f"Validation failed: Asset status is 'Assigned', but 'assigned_to' is missing. Please assign to a user.")  # Log failure
        return False
    elif asset_status in ["Available", "Retired"] and assigned_to:  # If asset is available or retired, 'assigned_to' should be empty
        logging.warning(f"Validation failed: Asset status is '{asset_status}', but 'assigned_to' should be empty.")  # Log failure
        return False
    else:
        logging.info(f"Validation success: 'assigned_to' '{assigned_to}' is valid for asset status '{asset_status}'.")  # Log success message
        return True

# Function to validate asset status
def validate_asset_status(asset_status):
    logging.debug(f"Validating asset status: {asset_status}")  # Log debug message for validation attempt
    valid_statuses = ["Available", "Assigned", "Repair", "Retired"]  # Define valid asset statuses
    if asset_status in valid_statuses:  # Check if the asset status is valid
        logging.info(f"Validation success: Asset status '{asset_status}' is valid.")  # Log success message
        return True
    else:
        logging.warning(f"Validation failed: Asset status '{asset_status}' is invalid. Must be one of {valid_statuses}.")  # Log warning on failure
        return False

# Function to validate serial number uniqueness in the database
def validate_serial_number(conn, serial_number):
    logging.debug(f"Validating serial number: {serial_number}")  # Log debug message for validation attempt
    cursor = conn.cursor()  # Initialize database cursor
    cursor.execute("SELECT COUNT(*) FROM asset_inventory WHERE serial_number = %s", (serial_number,))  # Query database for the serial number
    count = cursor.fetchone()[0]  # Get the count of records with the same serial number
    cursor.close()  # Close the cursor after use
    if count == 0:  # If no records found, the serial number is unique
        logging.info(f"Validation success: Serial number '{serial_number}' is unique and available.")  # Log success message
        return True
    else:
        logging.warning(f"Validation failed: Serial number '{serial_number}' already exists in the database.")  # Log warning on failure
        return False

# Function to validate asset tag uniqueness in the database
def validate_asset_tag_unique(conn, asset_tag):
    logging.debug(f"Validating asset tag uniqueness: {asset_tag}")  # Log debug message for validation attempt
    cursor = conn.cursor()  # Initialize database cursor
    cursor.execute("SELECT COUNT(*) FROM asset_inventory WHERE asset_tag = %s", (asset_tag,))  # Query database for the asset tag
    count = cursor.fetchone()[0]  # Get the count of records with the same asset tag
    cursor.close()  # Close the cursor after use
    if count == 0:  # If no records found, the asset tag is unique
        logging.info(f"Validation success: Asset tag '{asset_tag}' is unique and available for use.")  # Log success message
        return True
    else:
        logging.warning(f"Validation failed: Asset tag '{asset_tag}' already exists in the database.")  # Log warning on failure
        return False
