import pymysql
import csv
from datetime import datetime

# Function to get the database connection
def get_connection():
    return pymysql.connect(
        host="localhost",         # Database host
        user="root",              # Database user
        password="pass@word1",    # Database password
        database="ust_asset_db"   # Database name
    )

print("DB connected")

# Function to insert vendor data into the database
def insert_vendors():
    # SQL query to insert data into vendor_master table
    query = """
    INSERT INTO ust_asset_db.vendor_master (
        vendor_name, contact_person, contact_phone, gst_number, email,
        address, city, active_status
    ) VALUES (
        %s, %s, %s, %s, %s,
        %s, %s, %s
    )
    """
    print("Inserting vendor data...")

    # Open the CSV file containing vendor data
    with open(r'C:\Users\Administrator\Desktop\Training\ust_python_training\Bhargavi\day 19\AIMS_Plus\database\sample_data\validated_vendor_master.csv', "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # Read the CSV file as a dictionary
        print("CSV headers:", reader.fieldnames)  # Print headers for verification
        
        # Establish database connection
        conn = get_connection()
        cursor = conn.cursor()
        
        # Iterate through each row in the CSV and insert data into the database
        for row in reader:
            try:
                # Prepare the data tuple for insertion into the database
                data = (
                    row['vendor_name'],    # vendor_name
                    row['contact_person'], # contact_person
                    row['contact_phone'],  # contact_phone
                    row['gst_number'],     # gst_number
                    row['email'],          # email
                    row['address'],        # address
                    row['city'],           # city
                    row['active_status'],  # active_status
                )
                
                # Execute the query to insert data into the database
                cursor.execute(query, data)
                
            except Exception as e:
                # Print any error that occurs during insertion
                print(f"Error inserting vendor: {e}")

        # Commit the transaction to the database
        conn.commit()
        print("Vendors inserted successfully")  # Confirmation message

# Call the function to insert vendors from the CSV file
insert_vendors()
