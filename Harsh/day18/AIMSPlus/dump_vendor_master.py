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

# SQL query to insert records into vendor_master table
query = """
INSERT INTO vendor_master (
    vendor_id,vendor_name,contact_person,contact_phone,
    gst_number,email,address,city,active_status
) VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s
)
"""

# Open the validated vendor CSV file
with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\updated_vendor_master.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    # Iterate through each row in the CSV
    for row in reader:
        # Prepare data tuple for insertion
        data = (
            row["vendor_id"],
            row["vendor_name"],
            row["contact_person"],
            row["contact_phone"],
            row["gst_number"],
            row["email"],
            row["address"],
            row["city"],
            row["active_status"],
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
