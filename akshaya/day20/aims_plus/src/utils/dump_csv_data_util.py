import csv
import pymysql

# Function to establish a database connection
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",   # change to your password
        database="aims_plus",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor  # Return rows as dictionaries
    )

# Function to dump asset inventory data from a CSV file into the database
def dump_asset_inventory(csv_file):
    conn = get_connection()  # Establish the database connection
    with conn.cursor() as cursor:  # Open a cursor to execute SQL queries
        with open(csv_file, "r", encoding="utf-8") as f:  # Open the CSV file
            reader = csv.DictReader(f)  # Read the CSV file into a dictionary
            for row in reader:  # Loop through each row in the CSV
                # Define the SQL query to insert data into the asset_inventory table
                sql = """INSERT INTO asset_inventory 
                         (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, 
                          warranty_years, condition_status, assigned_to, location, asset_status, last_updated)
                         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())"""
                # Execute the query with values from the CSV row
                cursor.execute(sql, (
                    row["asset_tag"], row["asset_type"], row["serial_number"], row["manufacturer"],
                    row["model"], row["purchase_date"], row["warranty_years"], row["condition_status"],
                    row.get("assigned_to"), row["location"], row["asset_status"]
                ))
        conn.commit()  # Commit the transaction to the database
    conn.close()  # Close the database connection
    print("Data dumped successfully into asset_inventory")  # Print a success message

# Function to dump employee directory data from a CSV file into the database
def dump_employee_directory(csv_file):
    conn = get_connection()  # Establish the database connection
    sql = """INSERT INTO employee_directory 
                (emp_code, full_name, email, phone, department, location, join_date, status)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""  # SQL query to insert employee data
    with conn.cursor() as cursor:  # Open a cursor to execute SQL queries
        with open(csv_file, "r", encoding="utf-8") as f:  # Open the CSV file
            reader = csv.DictReader(f)  # Read the CSV file into a dictionary
            for row in reader:  # Loop through each row in the CSV
                try:
                    # Execute the query with values from the CSV row
                    cursor.execute(sql, (
                        row["emp_code"], row["full_name"], row["email"],
                        row["phone"], row["department"], row["location"],
                        row["join_date"], row["status"]
                    ))
                except Exception as e:  # Handle any exceptions (e.g., if a row is invalid)
                    print(str(e))  # Print the exception error message
        conn.commit()  # Commit the transaction to the database
    conn.close()  # Close the database connection
    print("Data dumped into employee_directory")  # Print a success message

# Function to dump maintenance log data from a CSV file into the database
def dump_maintenance(csv_file):
    conn = get_connection()  # Establish the database connection
    with conn.cursor() as cursor:  # Open a cursor to execute SQL queries
        with open(csv_file, "r", encoding="utf-8") as f:  # Open the CSV file
            reader = csv.DictReader(f)  # Read the CSV file into a dictionary
            for row in reader:  # Loop through each row in the CSV
                if not row["log_id"].strip():  # Skip rows with empty log_id
                    continue
                # Define the SQL query to insert data into the maintenance_log table
                sql = """INSERT INTO maintenance_log 
                         (log_id, asset_tag, maintenance_type, vendor_name, description, cost, maintenance_date, technician_name, status)
                         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                # Execute the query with values from the CSV row
                cursor.execute(sql, (
                    int(row["log_id"]), row["asset_tag"], row["maintenance_type"], row["vendor_name"],
                    row["description"], row["cost"], row["maintenance_date"], row["technician_name"], row["status"]
                ))
        conn.commit()  # Commit the transaction to the database
    conn.close()  # Close the database connection
    print("Data dumped into maintenance_log")  # Print a success message

# Function to dump vendor data from a CSV file into the database
def dump_vendor(csv_file):
    conn = get_connection()  # Establish the database connection
    with conn.cursor() as cursor:  # Open a cursor to execute SQL queries
        with open(csv_file, "r", encoding="utf-8") as f:  # Open the CSV file
            reader = csv.DictReader(f)  # Read the CSV file into a dictionary
            for row in reader:  # Loop through each row in the CSV
                # Skip rows with missing vendor_name (or any required field)
                if not row["vendor_name"].strip():
                    continue
                # Define the SQL query to insert data into the vendor_master table
                sql = """INSERT INTO vendor_master 
                         (vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status)
                         VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
                # Execute the query with values from the CSV row
                cursor.execute(sql, (
                    row["vendor_name"], row["contact_person"], row["contact_phone"], row["gst_number"],
                    row["email"], row["address"], row["city"], row["active_status"]
                ))
        conn.commit()  # Commit the transaction to the database
    conn.close()  # Close the database connection
    print("Data dumped into vendor_master")  # Print a success message

# Main function to execute the dumping processes
if __name__ == "__main__":
    # Call the dump functions for each type of data (assets, employees, maintenance, vendors)
    dump_asset_inventory("C:/Users/Administrator/Desktop/aims_plus/src/result/validated_assets.csv")
    dump_employee_directory("C:/Users/Administrator/Desktop/aims_plus/src/result/validated_employees.csv")
    dump_maintenance("C:/Users/Administrator/Desktop/aims_plus/src/result/validated_maintenance.csv")
    dump_vendor("C:/Users/Administrator/Desktop/aims_plus/src/result/validated_vendors.csv")
