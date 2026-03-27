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

# Function to insert maintenance log data into the database
def insert_maintenance_logs():
    # SQL query to insert data into maintenance_log table
    query = """
    INSERT INTO ust_asset_db.maintenance_log (
        asset_tag, maintenance_type, vendor_name, description,
        cost, maintenance_date, technician_name, status, last_updated
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s
    )
    """
    print("Inserting maintenance logs...")

    # Open the CSV file containing maintenance log data
    with open(r'C:\Users\Administrator\Desktop\Training\ust_python_training\Bhargavi\day 19\AIMS_Plus\database\sample_data\validated_maintenance_log.csv', "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # Reading the CSV data into a dictionary
        print("CSV headers:", reader.fieldnames)  # Printing the CSV headers
        conn = get_connection()  # Establishing database connection
        cursor = conn.cursor()   # Creating a cursor to execute SQL queries
        
        # Loop through each row in the CSV file and insert it into the database
        for row in reader:
            try:
                # Prepare the data tuple for the INSERT query
                data = (
                    row['asset_tag'],  # asset_tag
                    row['maintenance_type'],  # maintenance_type
                    row['vendor_name'],  # vendor_name
                    row['description'],  # description
                    row['cost'],  # cost
                    row['maintenance_date'],  # maintenance_date
                    row['technician_name'],  # technician_name
                    row['status'],  # status
                    datetime.now()  # last_updated (current timestamp)
                )
                
                # Debugging output: Show the data being passed to the query
                print(f"Inserting row: {data}")
                
                # Execute the query with the data tuple
                cursor.execute(query, data)
                
            except Exception as e:
                # Print any errors that occur while inserting a row
                print(f"Error inserting row: {e}")
        
        # Commit the transaction to the database
        conn.commit()
        print("Maintenance logs inserted successfully.")  # Confirmation message

# Run the function to insert maintenance log data
insert_maintenance_logs()
