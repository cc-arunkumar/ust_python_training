import pymysql
import csv
from datetime import datetime

# Function to get the database connection
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",   
        database="ust_asset_db"
    )

# Function to insert vendor data into the database
def insert_vendors():
    query = """
    INSERT INTO ust_asset_db.vendor_master (
        vendor_id, vendor_name, contact_person, contact_phone, gst_number,
        email, address, city, active_status
    ) VALUES (
        %s, %s, %s, %s, %s,
        %s, %s, %s, %s
    )
    """
    print("Inserting vendor data into the database...")

    # Correct file path
    input_file = r'C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day13\day19\AIMS_PLUS\database\sample_data\validated_vendor_master.csv'

    # Open the CSV file and read the data
    with open(input_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("CSV headers:", reader.fieldnames)
        
        # Connect to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Process each row from the CSV and insert into the database
        for row in reader:
            try:
                # Prepare data without the last_updated field
                data = tuple(row.values())
                
                # Execute the insert query
                cursor.execute(query, data)
            except Exception as e:
                # Handle any errors and print the row that failed
                print(f"Error inserting row: {row} | Error: {str(e)}")
        
        # Commit the transaction after inserting all rows
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

    print("Vendor data insertion completed successfully!")

# Call the function to insert vendors
insert_vendors()
