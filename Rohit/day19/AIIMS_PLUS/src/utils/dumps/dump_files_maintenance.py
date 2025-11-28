import csv  # Import csv module to read data from CSV files
import pymysql  # Import pymysql to connect and interact with MySQL databases
from datetime import datetime  # Import datetime for parsing and formatting dates

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

# Open the input CSV file in read mode
with open(r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day18\ust_ITSM\data\new_inventory.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)  # Read CSV rows as dictionaries (keys = column names)

    # Iterate through each row in the CSV file
    for row in reader:
        purchase_date = row["purchase_date"]  # Extract purchase_date field from row
        if purchase_date:  # If purchase_date exists
            try:
                # Try parsing date in format DD/MM/YYYY
                parsed_date = datetime.strptime(purchase_date, "%d/%m/%Y").date()
            except ValueError:
                try:
                    # If that fails, try parsing date in format MM/DD/YYYY
                    parsed_date = datetime.strptime(purchase_date, "%m/%d/%Y").date()
                except ValueError:
                    # If both fail, set parsed_date to None
                    parsed_date = None  
            # Convert parsed_date to YYYY-MM-DD format if valid, else None
            purchase_date = parsed_date.strftime("%Y-%m-%d") if parsed_date else None
        else:
            purchase_date = None  # If no date provided, set to None

        # Execute SQL INSERT query with row data
        cursor.execute("""
        INSERT INTO asset_inventory (
            asset_tag, asset_type, serial_number, manufacturer, model,
            purchase_date, warranty_years, condition_status, assigned_to,
            location, asset_status
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row["asset_tag"],  # Asset tag
            row["asset_type"],  # Asset type
            row["serial_number"],  # Serial number
            row["manufacturer"],  # Manufacturer name
            row["model"],  # Model name
            purchase_date,  # Parsed purchase date in YYYY-MM-DD format
            int(row["warranty_years"]) if row["warranty_years"] else None,  # Warranty years as integer or None
            row["condition_status"],  # Condition status
            row["assigned_to"],  # Assigned employee
            row["location"],  # Location
            row["asset_status"],  # Asset status
        ))

# Commit all changes to the database (make sure inserts are saved)
conn.commit()
# Close the cursor object
cursor.close()
# Close the database connection
conn.close()

# Print confirmation message after successful insertion
print("CSV data successfully dumped into MySQL database!")
