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

# SQL query to insert records into employee_directory table
query = """
INSERT INTO employee_directory (
    emp_code,full_name,email,
    phone,department,location,join_date,status
) VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s
)
"""

# Open the validated employee CSV file
with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\validated_employee_directory.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    # Iterate through each row in the CSV
    for row in reader:
        # Prepare data tuple for insertion
        data = (
            row["emp_code"],
            row["full_name"],
            row["email"],
            row["phone"],
            row["department"],
            row["location"],
            row["join_date"],
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
