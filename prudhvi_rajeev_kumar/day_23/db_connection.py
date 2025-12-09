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
