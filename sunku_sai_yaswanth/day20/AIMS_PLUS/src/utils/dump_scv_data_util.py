#dump_csv_data_ytil.py
 
# SQL query for inserting new asset data into the asset_inventory table
import csv
from config.db_connection import get_connection
 
 
query = """
INSERT INTO ust_aims_db.asset_inventory (
    asset_tag, asset_type, serial_number, manufacturer, model,
    purchase_date, warranty_years, condition_status, assigned_to,
    location, asset_status,last_updated
) VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s,NOW()
)
"""
 
try:
    # Establishing connection to the database
    conn = get_connection()
    cursor = conn.cursor()
 
    # Open the CSV file containing valid asset data
    with open("valid_rows.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
 
        # Iterate over each row in the CSV file
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
            # Execute the insertion query for each asset
            cursor.execute(query, data)
   
    # Commit the transaction to save changes
    conn.commit()
 
except Exception as e:
    # Print any errors that occur during execution
    print(f"Error: {e}")
 
finally:
    # Close the connection and cursor to the database
    if conn:
        cursor.close()
        conn.close()
        print("Connection closed successfully")
       
       
 
# SQL query for inserting new employee data into the database
query = """
INSERT INTO ust_aims_db.employee_directory (
    emp_code, full_name, email, phone, department, location, join_date, status
) VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s
)
"""
 
# Try-except block to handle file reading and database insertion for employee data
try:
    conn = get_connection()  # Establish connection to the database
    cursor = conn.cursor()
   
    # Open CSV file with valid employee rows
    with open("valid_rows_emp.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # Read the CSV data
       
        for row in reader:
            # Prepare the data tuple to insert into the database
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
            cursor.execute(query, data)  # Execute the insert query for each row
   
    conn.commit()  # Commit the transaction
 
except Exception as e:
    print(f"Error", e)  # Print any error that occurs during the process
 
finally:
    # Ensure the connection is closed after the operation
    if conn:
        cursor.close()
        conn.close()
       
       
       
       
 
query = """
INSERT INTO ust_aims_db.maintenance_log (
    asset_tag, maintenance_type, vendor_name, description, cost, maintenance_date, technician_name, status
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s
)
"""
 
try:
    conn = get_connection()
    cursor = conn.cursor()
 
    # Open the CSV file that contains maintenance log data
    with open("valid_rows_maintain.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
 
        for row in reader:
            if 'asset_tag' not in row or 'maintenance_type' not in row or 'vendor_name' not in row:
                print(f"Missing required column(s) in row: {row}")
                continue  
 
            data = (
                row["asset_tag"],          
                row["maintenance_type"],   # maintenance_type
                row["vendor_name"],        # vendor_name
                row["description"],        # description
                row["cost"],               # cost
                row["maintenance_date"],   # maintenance_date
                row["technician_name"],    # technician_name
                row["status"]              # status
            )
 
            cursor.execute(query, data)
   
    conn.commit()
 
except Exception as e:
    print(f"Error: {e}")
 
finally:
    if conn:
        cursor.close()
        conn.close()
 
 
# SQL query to insert vendor details into the vendor_master table
query = """
INSERT INTO ust_aims_db.vendor_master (
    vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s
)
"""
 
try:
    # Establishing a connection to the database
    conn = get_connection()
    cursor = conn.cursor()
 
    # Open the CSV file containing valid vendor data
    with open("valid_rows_vendor.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
 
        # Iterate over each row in the CSV file
        for row in reader:
            # Extract the vendor data and prepare it for insertion
            data = (
                row["vendor_name"],       # vendor_name
                row["contact_person"],    # contact_person
                row["contact_phone"],     # contact_phone
                row["gst_number"],        # gst_number
                row["email"],             # email
                row["address"],           # address
                row["city"],              # city
                row["active_status"]      # active_status
            )
            # Execute the SQL query to insert the vendor data
            cursor.execute(query, data)
   
    # Commit the transaction to save changes
    conn.commit()
 
except Exception as e:
    # If any error occurs during the insertion, print the error message
    print(f"Error: {e}")
 
finally:
    # Close the connection and cursor
    if conn:
        cursor.close()
        conn.close()