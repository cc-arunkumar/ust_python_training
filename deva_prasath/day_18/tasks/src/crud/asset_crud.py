import mysql.connector
import re
from helpers.validators import validate_asset_tag,validate_asset_type,validate_assigned_to,validate_date,validate_serial_number,validate_warranty_years

# Creates and returns a connection to the MySQL database
def get_connection():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db"
    )
    return conn

# Inserts a new asset record into the database after all validations
def create_asset(new_asset_tag,new_asset_type,new_serial_number,new_manufacturer,new_model,new_purchase_date,new_warranty_years,new_assigned_to,new_asset_status):
    if not validate_asset_tag(new_asset_tag):
        return "Asset tag must start with UST-"
    if not validate_asset_type(new_asset_type):
        return "Asset type not in the list"
    if not validate_warranty_years(new_warranty_years):
        return "Warranty year must be greater than 0"
    if not validate_assigned_to(new_asset_status,new_assigned_to):
        return "Check asset status"
    if not validate_serial_number(new_serial_number):
        return "Serial number must be unique"
    if not validate_date(new_purchase_date):
        return "Check the date"        
    
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        # Inserting a new asset into the table
        cursor.execute("insert into asset_inventory (asset_tag,asset_type,serial_number,manufacturer,model,purchase_date,warranty_years,assigned_to,asset_status,last_updated) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())",(new_asset_tag,new_asset_type,new_serial_number,new_manufacturer,new_model,new_purchase_date,new_warranty_years,new_assigned_to,new_asset_status))
        conn.commit()
        print("Created Asset successfully")
    
    except Exception as e:
        print("Error",e)
    
    finally :
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed")

# Reads and returns all assets from the table
def read_all_assets():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM asset_inventory")
    rows=cursor.fetchall()
    return rows

# Reads an asset by its ID and prints feedback
def read_asset_id(asset_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("select * from asset_inventory where asset_id=%s",(asset_id,))
        row=cursor.fetchone()
        if row:
            print("Read data by asset_id:",end="")
            return row
        else:
            print(f"Record not found for:{asset_id}")
    except Exception as e:
        print("Error:",e)
    
    finally :
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed")

# Updates an existing asset based on passed fields
def update_asset(asset_id, asset_type=None, manufacturer=None, model=None,
                 warranty_years=None, asset_status=None, assigned_to=None):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute(
            "UPDATE asset_inventory SET asset_type=%s, manufacturer=%s, model=%s, warranty_years=%s, asset_status=%s, assigned_to=%s WHERE asset_id=%s",
            (asset_type, manufacturer, model, warranty_years, asset_status, assigned_to, asset_id)
        )
        conn.commit()
        print("Updated successfully")
        
    except Exception as e:
        print("Error: ", e)
    finally :
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed")
            
# Deletes an asset record permanently from the table
def delete_by_id(asset_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("delete from asset_inventory where asset_id=%s",(asset_id,))
        conn.commit()
        print("Asset deleted successfully")
    
    except Exception as e:
        print("error",e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        print("Connection closed")

# Function calls for testing CRUD operations
create_asset('UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', '2023-01-15', 3, 'NULL', 'Available')
rows = read_all_assets()
print(rows)
res = read_asset_id(1)
print(res)
update_asset(1, asset_type="Laptop", manufacturer="Dell", model="Latitude 5520",
             warranty_years=3, asset_status="Assigned", assigned_to="Rohit Sharma (UST Bangalore)")

delete_by_id(1)




#Sample output

# Created Asset successfully
# Connection closed
# [(1, 'UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', datetime.date(2023, 1, 15), 3, 'NULL', 'Available', datetime.datetime(2025, 11, 26, 15, 30, 12))]
# Read data by asset_id:Connection closed
# (1, 'UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', datetime.date(2023, 1, 15), 3, 'NULL', 'Available', datetime.datetime(2025, 11, 26, 15, 30, 12))
# Connection closed
# Updated successfully
#Connection closed
# Asset deleted successfully
# Connection closed
# Record not found for:1
# Connection closed





import mysql.connector
import csv

# MySQL Database connection setup
db_connection = mysql.connector.connect(
    host="localhost",  # Your MySQL server host
    user="root",  # Your MySQL username
    password="yourpassword",  # Your MySQL password
    database="yourdatabase"  # The name of your database
)

# Cursor for executing SQL queries
cursor = db_connection.cursor()

# Function to insert data into Asset Table
def insert_assets_from_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            query = """
            INSERT INTO asset_inventory 
            (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, 
            condition_status, assigned_to, location, asset_status) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                row["asset_tag"], row["asset_type"], row["serial_number"], row["manufacturer"], 
                row["model"], row["purchase_date"], row["warranty_years"], row["condition_status"], 
                row["assigned_to"], row["location"], row["asset_status"]
            )
            cursor.execute(query, values)
        db_connection.commit()

# Function to insert data into Vendor Table
def insert_vendors_from_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            query = """
            INSERT INTO vendor_master 
            (vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                row["vendor_name"], row["contact_person"], row["contact_phone"], row["gst_number"], 
                row["email"], row["address"], row["city"], row["active_status"]
            )
            cursor.execute(query, values)
        db_connection.commit()

# Function to insert data into Maintenance Table
def insert_maintenance_from_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            query = """
            INSERT INTO maintenance_log 
            (asset_tag, maintenance_type, vendor_name, description, cost, maintenance_date, technician_name, status) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                row["asset_tag"], row["maintenance_type"], row["vendor_name"], row["description"], 
                row["cost"], row["maintenance_date"], row["technician_name"], row["status"]
            )
            cursor.execute(query, values)
        db_connection.commit()

# Function to insert data into Employee Table
def insert_employees_from_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            query = """
            INSERT INTO employee_directory 
            (emp_code, full_name, email, phone, department, location, join_date, status) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                row["emp_code"], row["full_name"], row["email"], row["phone"], 
                row["department"], row["location"], row["join_date"], row["status"]
            )
            cursor.execute(query, values)
        db_connection.commit()

# Call functions to insert data into respective tables
insert_assets_from_csv(r"D:\path\to\your\validated_asset.csv")
insert_vendors_from_csv(r"D:\path\to\your\validated_vendor.csv")
insert_maintenance_from_csv(r"D:\path\to\your\validated_maintenance.csv")
insert_employees_from_csv(r"D:\path\to\your\validated_employee.csv")

# Close the database connection
cursor.close()
db_connection.close()

print("Data inserted successfully!")
