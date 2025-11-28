import csv  # Import csv module to read data from CSV files
import pymysql  # Import pymysql to connect and interact with MySQL databases
from datetime import datetime  # Import datetime (not used here, but useful for date handling if needed)

# Function to establish a connection to the MySQL database
def get_connection():
    return pymysql.connect(
        host="localhost",       # Database server address (localhost = local machine)
        user="root",            # MySQL username
        password="pass@word1",  # MySQL password
        database="ust_asset_inventory"  # Target database name
    )

# Create a connection object
conn = get_connection()
# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# SQL query template for inserting rows into employee_directory table
# Uses placeholders (%s) for parameterized queries to prevent SQL injection
query = """
INSERT INTO employee_directory (
    emp_code,full_name,email,
    phone,department,location,join_date,status
) VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s
)
"""

# Open the input CSV file in read mode
with open(r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day20\AIIMS_PLUS\database\sample_data\final\validated_employee_directory(in).csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)  # Read CSV rows as dictionaries (keys = column names)

    # Iterate through each row in the CSV file
    for row in reader:
        # Extract values from the row into a tuple matching the SQL query placeholders
        data = (
            row["emp_code"],     # Employee code
            row["full_name"],    # Full name
            row["email"],        # Email address
            row["phone"],        # Phone number
            row["department"],   # Department name
            row["location"],     # Office location
            row["join_date"],    # Joining date
            row["status"],       # Employment status
        )
        # Execute the SQL insert query with the extracted data
        cursor.execute(query, data)

# Commit all changes to the database (make sure inserts are saved)
conn.commit()
# Close the cursor object
cursor.close()
# Close the database connection
conn.close()

# Print confirmation message after successful insertion
print("All CSV records inserted successfully!")
