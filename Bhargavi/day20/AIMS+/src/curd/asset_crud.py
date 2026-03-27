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

print("db connected")

# Function to insert asset data into the database
def insert_assets():
    # SQL query to insert data into asset_inventory table
    query = """
    INSERT INTO ust_asset_db.asset_inventory (
        asset_tag, asset_type, serial_number, manufacturer, model,
        purchase_date, warranty_years, condition_status, assigned_to,
        location, asset_status, last_updated
    ) VALUES (
        %s, %s, %s, %s, %s,
        %s, %s, %s, %s,
        %s, %s,%s
    )
    """
    print("Inserting assets...")
    
    # Open the CSV file containing asset data
    with open(r'C:\Users\Administrator\Desktop\Training\ust_python_training\Bhargavi\day 19\AIMS_Plus\database\sample_data\validated_inventory.csv', "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # Reading the CSV data into a dictionary
        print("CSV headers:", reader.fieldnames)  # Printing the CSV headers
        conn = get_connection()  # Establishing database connection
        cursor = conn.cursor()   # Creating a cursor to execute SQL queries
        
        # Loop through each row in the CSV file and insert it into the database
        for row in reader:
            try:
                # Prepare the data tuple (add current timestamp to each row)
                data = tuple(row.values()) + (datetime.now(),)
                cursor.execute(query, data)  # Execute the insert query
            except Exception as e:
                print(str(e))  # Print any errors that occur during insertion

        conn.commit()  # Commit the transaction to save the changes
        print("Assets inserted successfully.")  # Confirmation message

# Calling the function to insert asset data
insert_assets()
