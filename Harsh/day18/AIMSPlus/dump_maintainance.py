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

# SQL query to insert records into maintenance_log table
query = """
INSERT INTO maintenance_log (
    log_id,asset_tag,maintenance_type,vendor_name,
    description,cost,maintenance_date,technician_name,status
) VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s
)
"""

# Open the validated maintenance CSV file
with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\updated_maintenance_valid.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    # Iterate through each row in the CSV
    for row in reader:
        # Prepare data tuple for insertion
        data = (
            row["log_id"],
            row["asset_tag"],
            row["maintenance_type"],
            row["vendor_name"],
            row["description"],
            row["cost"],
            row["maintenance_date"],
            row["technician_name"],
            row["status"],
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
