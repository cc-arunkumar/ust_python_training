from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Create or switch to database
db = client['ust_db']

print("Database created successfully.")

# Create or switch to a collection
students = db['students']

# All 10 records
all_students = [
    # Original 3
    {"name": "Amit", "age": 21, "skills": ["python", "mongodb", "data analysis"]},
    {"name": "Amita", "age": 22, "skills": ["python", "java"], "address": "Rourkela", "state": "odisha"},
    {"name": "Anil", "age": 23, "skills": ["C", "Fullstack", "React"]},

    # New 7
    {"name": "Ravi", "age": 24, "skills": ["Go", "Docker"], "email": "ravi@example.com", "city": "Hyderabad"},  # extra attributes
    {"name": "Sneha"},  # fewer attributes
    {"name": "Kiran", "age": 25, "skills": ["AWS", "DevOps"], "joining_date": datetime(2024, 7, 10)},  # datetime attribute
    {"name": "Priya", "age": 20, "skills": ["HTML", "CSS", "JavaScript"], "address": "Bangalore"},
    {"name": "Arjun", "age": 26, "skills": ["Python", "Machine Learning"], "state": "Tamil Nadu"},
    {"name": "Meera", "age": 22, "skills": ["UI/UX", "Figma"], "email": "meera@example.com"},
    {"name": "Vikram", "age": 27, "skills": ["Java", "Spring Boot"], "joining_date": datetime(2023, 11, 5)}
]

# # Insert all documents at once
# insert_many_result = students.insert_many(all_students)
# print("Inserted IDs:", insert_many_result.inserted_ids)

# Print all documents in the collection
# print("\nAll students in collection:")
# for student in db.students.find():
#     print(student)
    

# db.students.delete_one({"name" : "Priya"})
# print("Priya deleted")

update_result = students.update_one(
    {"name": "Ravi"},   # filter condition
    {"$set": {"city": "Delhi"}, "$push": {"skills": "Kubernetes"}}  # update operations
)
print("Matched:", update_result.matched_count, "Modified:", update_result.modified_count)

# Example: Update many students (increase age by 1 for all students older than 25)
update_many_result = students.update_many(
    {"age": {"$gt": 25}},   # filter condition
    {"$inc": {"age": 1}}    # increment age by 1
)
print("Matched:", update_many_result.matched_count, "Modified:", update_many_result.modified_count)

# Example: Add a new field to all students (status = 'active')
students.update_many(
    {},   # empty filter means all documents
    {"$set": {"status": "active"}}
)

# Print all documents after update
print("\nAll students after update:")
for student in db.students.find():
    print(student)

# db.students.delete_many({"age" : {"$lte" : 22}})
# print("age lt 22 deleted.")





# import json
# import mysql.connector
# from pymongo import MongoClient

# # Step 1: Read the JSON file
# def read_json_file(file_path):
#     with open(file_path, 'r') as f:
#         data = json.load(f)
#     return data

# # Step 2: Insert data into MySQL
# def insert_data_into_mysql(data):
#     conn = mysql.connector.connect(
#         host="localhost",  # Change as per your MySQL setup
#         user="root",  # Your MySQL username
#         password="password",  # Your MySQL password
#         database="your_database"  # Replace with your database name
#     )
#     cursor = conn.cursor()

#     # Assuming data is a list of dictionaries
#     for item in data:
#         # Adjust the query based on your data structure
#         query = "INSERT INTO your_table_name (column1, column2) VALUES (%s, %s)"
#         cursor.execute(query, (item['key1'], item['key2']))  # Replace with actual keys
#     conn.commit()
#     cursor.close()
#     conn.close()

# # Step 3: Read data from MySQL
# def read_data_from_mysql():
#     conn = mysql.connector.connect(
#         host="localhost",  # Change as per your MySQL setup
#         user="root",  # Your MySQL username
#         password="password",  # Your MySQL password
#         database="your_database"  # Replace with your database name
#     )
#     cursor = conn.cursor(dictionary=True)  # Return data as a dictionary
#     cursor.execute("SELECT * FROM your_table_name")  # Replace with your table name
#     data = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return data

# # Step 4: Insert data into MongoDB
# def insert_data_into_mongodb(data):
#     client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI
#     db = client['your_database']  # Your MongoDB database
#     collection = db['your_collection']  # Your MongoDB collection

#     # Insert data
#     collection.insert_many(data)

# # Example usage
# json_data = read_json_file('data.json')  # Replace with your JSON file path
# insert_data_into_mysql(json_data)  # Insert JSON data into MySQL
# mysql_data = read_data_from_mysql()  # Read data back from MySQL
# insert_data_into_mongodb(mysql_data)  # Insert MySQL data into MongoDB
