import pymysql
import csv

# Establish database connection
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="pass@word1",
    database="ust_aims_db"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# SQL query to insert records into asset_inventory table
query = """
INSERT INTO asset_inventory (
    asset_tag, asset_type, serial_number, manufacturer, model,
    purchase_date, warranty_years, condition_status, assigned_to,
    location, asset_status
) VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s
)
"""

# Open the validated CSV file for reading
with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\validated_asset_inventory.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    # Iterate through each row in the CSV
    for row in reader:
        # Prepare data tuple for insertion
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
        # Execute insert query with row data
        cursor.execute(query, data)

# Commit all changes to the database
conn.commit()

# Close cursor and connection
cursor.close()
conn.close()

# Print success message
print("All CSV records inserted successfully!")
