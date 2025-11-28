import pymysql
import csv
from datetime import datetime

# ---------------------------
# Database Connection Utility
# ---------------------------
def get_Connection():
    """
    Establish and return a connection to the MySQL database.
    Uses pymysql for connectivity.
    """
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_aims_plus"
    )

# ---------------------------
# Generic CSV-to-Database Loader
# ---------------------------
def create_assets(query, path, col):
    """
    Insert records from a CSV file into the database using a provided SQL query.

    Parameters:
        query (str): SQL INSERT statement with placeholders (%s).
        path (str): Path to the CSV file containing data.
        col (list): List of column names to extract from the CSV file.

    Workflow:
        1. Establish DB connection.
        2. Read CSV file using DictReader.
        3. For each row, extract required columns in order.
        4. Execute INSERT query with extracted data.
        5. Commit transaction and close connection.
    """
    try:
        conn = get_Connection()
        cursor = conn.cursor()

        # Open CSV file and iterate through rows
        with open(path, "r") as file:
            content = csv.DictReader(file)
            for row in content:
                try:
                    # Extract data in the same order as 'col'
                    data = [row[column] for column in col]
                    cursor.execute(query, tuple(data))
                except Exception as e:
                    # Log error and problematic row for debugging
                    print("Row insert error:", e, row)

        # Commit all successful inserts
        conn.commit()
        print("Asset records inserted successfully")
    except Exception as e:
        # Handle database-level errors (connection, query execution, etc.)
        print("Database error:", e)
    finally:
        # Ensure resources are closed properly
        if conn.open:
            cursor.close()
            conn.close()
        print("Connection closed")

# ---------------------------
# File Path for Final CSVs
# ---------------------------
path = "C:/Users/Administrator/Desktop/ust_python_training-1/yashaswini/day-13/my-first-fastapi-app/day-18/aims_final_project/database/sample_data/final_data/"

# ---------------------------
# Insert Asset Inventory Data
# ---------------------------
query = """
    INSERT INTO ust_aims_plus.asset_inventory (
        asset_tag, asset_type, serial_number, manufacturer,
        model, purchase_date, warranty_years, condition_status,
        assigned_to, location, asset_status, last_updated
    )
    VALUES (%s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s, %s)
"""
col = [
    "asset_tag", "asset_type", "serial_number", "manufacturer",
    "model", "purchase_date", "warranty_years", "condition_status",
    "assigned_to", "location", "asset_status", "last_updated"
]
create_assets(query, path + "validated_asset_inventory.csv", col)

# ---------------------------
# Insert Employee Directory Data
# ---------------------------
query = """
    INSERT INTO ust_aims_plus.employee_directory (
        emp_code, full_name, email, phone,
        department, location, join_date, status
    )
    VALUES (%s, %s, %s, %s,
            %s, %s, %s, %s)
"""
col = [
    "emp_code", "full_name", "email", "phone",
    "department", "location", "join_date", "status"
]
create_assets(query, path + "validated_employee_directory.csv", col)

# ---------------------------
# Insert Maintenance Log Data
# ---------------------------
query = """
    INSERT INTO ust_aims_plus.maintenance_log (
        asset_tag, maintenance_type, vendor_name, description,
        cost, maintenance_date, technician_name, status
    )
    VALUES (%s, %s, %s, %s,
            %s, %s, %s, %s)
"""
col = [
    "asset_tag", "maintenance_type", "vendor_name", "description",
    "cost", "maintenance_date", "technician_name", "status"
]
create_assets(query, path + "validated_maintenance_log.csv", col)

# ---------------------------
# Insert Vendor Master Data
# ---------------------------
query = """
    INSERT INTO ust_aims_plus.vendor_master (
        vendor_name, contact_person, contact_phone,
        gst_number, email, address,
        city, active_status
    )
    VALUES (%s, %s, %s,
            %s, %s, %s,
            %s, %s)
"""
col = [
    "vendor_name", "contact_person", "contact_phone",
    "gst_number", "email", "address",
    "city", "active_status"
]
create_assets(query, path + "validated_vendor_master.csv", col)