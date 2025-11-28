import csv
from src.config.db_connection import db_connector

# Paths to the CSV files for assets, vendors, maintenance, and employees
valid_asset_path = r"D:\training\ust_python_training\deva_prasath\day_20\AIIMS_Plus\database\sample_data\asset_inventory.csv"
valid_vendor_path = r"D:\training\ust_python_training\deva_prasath\day_20\AIIMS_Plus\database\sample_data\validated_vendor.csv"
valid_maintainance_path = r"D:\training\ust_python_training\deva_prasath\day_20\AIIMS_Plus\database\sample_data\validated_maintenance.csv"
valid_employee_path = r"D:\training\ust_python_training\deva_prasath\day_20\AIIMS_Plus\database\sample_data\validated_employee.csv"

# Function to insert valid asset records into the database
def dump_valid_asset():
    cursor = db_connector.cursor()  # Create cursor for database interaction
    query = """
    INSERT INTO ust_asset_db.asset_inventory (
        asset_tag, asset_type, serial_number, manufacturer, model,
        purchase_date, warranty_years, condition_status, assigned_to,
        location, asset_status
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Read the CSV file and insert each row into the database
    with open(valid_asset_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data = (
                row["asset_tag"],
                row["asset_type"],
                row["serial_number"],
                row["manufacturer"],
                row["model"],
                row["purchase_date"],
                row["warranty_years"],
                row["condition_status"],
                row["assigned_to"],
                row["location"],
                row["asset_status"]
            )
            cursor.execute(query, data)

    print("All CSV records inserted successfully!")  # Confirm successful insertion

# Function to insert valid vendor records into the database
def dump_valid_vendor():
    cursor = db_connector.cursor()  # Create cursor for database interaction
    query = """
    INSERT INTO aiims.vendor_master (
        vendor_name, contact_person, contact_phone, gst_number, 
        email, address, city, active_status
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Read the CSV file and insert each row into the database
    with open(valid_vendor_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data = (
                row["vendor_name"],
                row["contact_person"],
                row["contact_phone"],
                row["gst_number"],
                row["email"],
                row["address"],
                row["city"],
                row["active_status"]
            )
            cursor.execute(query, data)

    print("All CSV records inserted successfully!")  # Confirm successful insertion

# Function to insert valid maintenance records into the database
def dump_valid_maintainance():
    cursor = db_connector.cursor()  # Create cursor for database interaction
    query = """
    INSERT INTO aiims.maintenance_log (
        asset_tag, maintenance_type, vendor_name, description, cost, 
        maintenance_date, technician_name, status
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Read the CSV file and insert each row into the database
    with open(valid_maintainance_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data = (
                row["asset_tag"],
                row["maintenance_type"],
                row["vendor_name"],
                row["description"],
                row["cost"],
                row["maintenance_date"],
                row["technician_name"],
                row["status"]
            )
            cursor.execute(query, data)

    print("All CSV records inserted successfully!")  # Confirm successful insertion

# Function to insert valid employee records into the database
def dump_valid_employee():
    cursor = db_connector.cursor()  # Create cursor for database interaction
    query = """
    INSERT INTO aiims.employee_directory (
        emp_code, full_name, email, phone, department, location, 
        join_date, status
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Read the CSV file and insert each row into the database
    with open(valid_employee_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data = (
                row["emp_code"],
                row["full_name"],
                row["email"],
                row["phone"],
                row["department"],
                row["location"],
                row["join_date"],
                row["status"]
            )
            cursor.execute(query, data)

    # Commit the changes, close the cursor, and the connection
    db_connector.commit()
    cursor.close()
    db_connector.close()

    print("All CSV records inserted successfully!")  # Confirm successful insertion

# Execute the functions to dump all valid data
dump_valid_asset()
dump_valid_vendor()
dump_valid_maintainance()
dump_valid_employee()
