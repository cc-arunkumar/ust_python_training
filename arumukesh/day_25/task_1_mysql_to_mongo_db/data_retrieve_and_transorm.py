from db_connection import get_connection
from pymongo import MongoClient
import pymongo

# Get MySQL connection
conn = get_connection()
cursor = conn.cursor()

# Fetch all rows from MySQL table
cursor.execute("SELECT * FROM employee_table;")
result = cursor.fetchall()
print(result)   # Print raw MySQL data (list of dicts)

# Add new field "category" based on age
for data in result:
    if data["age"] < 25:
        data["category"] = "Fresher"         # Age less than 25 → Fresher
    else:
        data["category"] = "Experienced"     # Age 25 or above → Experienced

print(result)   # Print transformed records

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["employee_db"]
collection = db["employee_table"]

# Insert the transformed data into MongoDB
result = collection.insert_many(result)

# Check if insertion was successful
if result.inserted_ids:
    print("Insertion Success!")
