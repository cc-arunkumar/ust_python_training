import pymysql
import json

# Connect to the MySQL database
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="pass@word1",
    database="employee_db"
)

cursor = conn.cursor()

# Open and read the JSON file
with open(r"C:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_25\data.json", "r") as file:
    data = json.load(file)   # Load JSON data into Python list

# Iterate through each dictionary in the JSON list
for row in data:
    values = tuple(row.values())  # Convert dict values to tuple (in same order as JSON)

    # Insert each record into the MySQL table
    query = "INSERT INTO employee_table VALUES (%s, %s, %s, %s, %s)"

    cursor.execute(query, values)  # Execute insert query
    conn.commit()                  # Commit after each insert

print("Data inserted successfully!")

# Close cursor and connection
cursor.close()
conn.close()
