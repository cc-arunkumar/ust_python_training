from datetime import datetime
import json
import mysql.connector

# ---------------------------------------------------------------------------
# Database Utilities
# ---------------------------------------------------------------------------

def get_connection():
    """
    Establish a connection to the MySQL database.
    
    Returns:
        mysql.connector.connection.MySQLConnection: Active DB connection.
    """
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db"
    )
    return conn


# Allowed values for various asset fields
allowed_assert_status = ["Available", "Assigned", "Repair", "Repair"]  # Note: Duplicate entry
allowed_assert_type = ["Laptop", "Monitor", "Docking Station", "Keyboard", "Mouse"]


# ---------------------------------------------------------------------------
# Data Fetching
# ---------------------------------------------------------------------------

def get_all_assets():
    """
    Retrieve all records from the asset_inventory table.
    
    Returns:
        list: List of tuples containing asset rows.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM ust_asset_db.asset_inventory")
        rows = cursor.fetchall()
        return rows

    except Exception as e:
        print("ERROR:", e)

    finally:
        # Ensure connection cleanup
        if conn.is_connected():
            cursor.close()
            conn.close()


# ---------------------------------------------------------------------------
# Data Validation
# ---------------------------------------------------------------------------

def validation(data):
    """
    Validate asset data before insert/update operations.
    
    Args:
        data (dict): Asset data to be validated.
        
    Returns:
        bool: True only if all validations pass.
    """
    try:
        # Asset tag should start with 'UST-'
        if "asset_tag" in data:
            if data["asset_tag"].split("-")[0] != "UST":
                raise Exception("asset tag must start with UST-")

        # Validate asset type
        if data["asset_type"] not in allowed_assert_type:
            raise Exception("given asset type is not allowed")

        # Warranty must be positive
        if data["warranty_years"] <= 0:
            raise Exception("Warranty year should be greater than zero")

        # Validation: Assigned assets must have an assigned_to value
        if data["asset_status"] == "Assigned" and data["assigned_to"] is None:
            raise Exception("assigned_to must not be null when asset is assigned")

        # Validation: Non-assigned assets must not have an assigned_to value
        if data["asset_status"] in ("Available", "Retired") and data["assigned_to"] is not None:
            raise Exception("assigned_to must be null for Available/Retired assets")

        # Uniqueness checks require looking at existing records
        rows = get_all_assets()

        # Validate unique serial number
        if "serial_number" in data:
            for row in rows:
                if row[3] == data["serial_number"]:
                    raise Exception("serial_number must be unique")

        # Validate unique asset tag
        if "asset_tag" in data:
            for row in rows:
                if row[1] == data["asset_tag"]:
                    raise Exception("asset_tag must be unique")

    except Exception as e:
        print("ERROR:", e)

    else:
        return True


# ---------------------------------------------------------------------------
# Create Operation
# ---------------------------------------------------------------------------

def create_asset(data):
    """
    Insert a new asset record into the database.
    Uses predefined sample data for testing/demo purposes.
    """
    try:

        # Extract values from dict
        asset_tag = data["asset_tag"]
        asset_type = data["asset_type"]
        serial_number = data["serial_number"]
        manufacturer = data["manufacturer"]
        model = data["model"]
        purchase_date = data["purchase_date"]
        warranty_years = data["warranty_years"]
        assigned_to = data["assigned_to"]
        asset_status = data["asset_status"]
        last_updated = datetime.now()

        conn = get_connection()
        cursor = conn.cursor()

        # Validate input before DB operation
        if validation(data) != True:
            raise Exception("Validation failed")

        # Execute insert
        cursor.execute(
            "INSERT INTO ust_asset_db.asset_inventory "
            "(asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, "
            "warranty_years, assigned_to, asset_status, last_updated) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (asset_tag, asset_type, serial_number, manufacturer, model,
             purchase_date, warranty_years, assigned_to, asset_status, last_updated)
        )

        conn.commit()
        print("Asset inserted successfully:")

    except Exception as e:
        print("ERROR:", e)

    finally:
        # Ensure connection cleanup
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed successfully")


# ---------------------------------------------------------------------------
# Filtering & Reporting
# ---------------------------------------------------------------------------

def filter_rows(rows, filter):
    """
    Print assets that match a specific status filter.

    Args:
        rows (list): List of asset rows.
        filter (str): Asset status to filter by.
    """
    for row in rows:
        if row[9] == filter:  # row[9] corresponds to asset_status
            print(f"Asset ID: {row[0]} | Asset Tag: {row[1]} | Asset Type: {row[2]} | "
                  f"Serial Number: {row[3]} | Manufacturer: {row[4]} | Model: {row[5]} | "
                  f"Purchase Date: {row[6]} | Warranty_year {row[7]} | Assigned To: {row[8]} | "
                  f"Asset Status: {row[9]} | Last Updated {row[10]}")


def read_all_assets():
    """
    Display all assets based on user-selected filter criteria.
    """
    rows = get_all_assets()

    print("Select filter\n1.Available\n2.Assigned\n3.Repair\n4.Retired\n5.ALL")
    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            filter_rows(rows, "Available")
        case 2:
            filter_rows(rows, "Assigned")
        case 3:
            filter_rows(rows, "Repair")
        case 4:
            filter_rows(rows, "Retired")
        case 5:
            for row in rows:
                print(f"Asset ID: {row[0]} | Asset Tag: {row[1]} | Asset Type: {row[2]} | "
                      f"Serial Number: {row[3]} | Manufacturer: {row[4]} | Model: {row[5]} | "
                      f"Purchase Date: {row[6]} | Warranty_year {row[7]} | Assigned To: {row[8]} | "
                      f"Asset Status: {row[9]} | Last Updated {row[10]}")


# ---------------------------------------------------------------------------
# Read Operation
# ---------------------------------------------------------------------------

def read_asset_by_id(asset_id):
    """
    Fetch and display a single asset record based on asset_id.
    
    Args:
        asset_id (int): Unique identifier for the asset.
    
    Returns:
        tuple | None: The asset row if found, else None.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM ust_asset_db.asset_inventory WHERE asset_id = %s;", (asset_id,))
        row = cursor.fetchone()

        if row:
            print(f"Asset ID: {row[0]} | Asset Tag: {row[1]} | Asset Type: {row[2]} | "
                  f"Serial Number: {row[3]} | Manufacturer: {row[4]} | Model: {row[5]} | "
                  f"Purchase Date: {row[6]} | Warranty_year {row[7]} | Assigned To: {row[8]} | "
                  f"Asset Status: {row[9]} | Last Updated {row[10]}")
            return row
        else:
            print("Employee record not found with emp_id", asset_id)

    except Exception as e:
        print("Error:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed successfully")


# ---------------------------------------------------------------------------
# Update Operation
# ---------------------------------------------------------------------------

def update_asset(asset_id):
    """
    Update an existing asset's details using a predefined payload.
    
    Args:
        asset_id (int): The ID of the asset to update.
    """
    try:
        data = {
            "asset_type": "Laptop",
            "manufacturer": "",
            "model": "F15",
            "warranty_years": 2025,
            "assigned_to": None,
            "asset_status": "Available"
        }

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM ust_asset_db.asset_inventory WHERE asset_id = %s;", (asset_id,))
        row = cursor.fetchone()

        if row:
            if validation(data) != True:
                raise Exception("Validation failed during update")

            cursor.execute(
                "UPDATE ust_asset_db.asset_inventory SET asset_type = %s, manufacturer = %s, "
                "model = %s, warranty_years = %s, assigned_to = %s, asset_status = %s "
                "WHERE asset_id = %s",
                (data["asset_type"], data["manufacturer"], data["model"],
                 data["warranty_years"], data["assigned_to"], data["asset_status"], asset_id)
            )

            conn.commit()

        else:
            print("Asset id does not exist")

        print("Asset updated successfully")

    except Exception as e:
        print("ERROR:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed successfully")


# ---------------------------------------------------------------------------
# Delete Operation
# ---------------------------------------------------------------------------

def delete_asset(asset_id):
    """
    Delete an asset record from the database after confirming existence.
    
    Args:
        asset_id (int): Unique ID of the asset to be deleted.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Pre-check for existence
        asset_to_be_deleted = read_asset_by_id(asset_id)

        if asset_to_be_deleted:
            cursor.execute("DELETE FROM ust_asset_db.asset_inventory WHERE asset_id = %s", (asset_id,))
            conn.commit()
            print("Employee deleted successfully")
        else:
            print("Employee record not found")

    except Exception as e:
        print("ERROR:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed successfully")

