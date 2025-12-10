from pymongo import MongoClient

# Step 1: Establish a connection to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Step 2: Access the 'ust_db' database. If it doesn't exist, MongoDB will create it.
db = client['ust_db']

# Step 3: Confirm that the database was successfully connected
print("Database 'ust_db' created successfully.")

# Step 4: Insert multiple student documents (Uncomment if you want to insert data)
# students = [
#     {"name": "varun", "age": 21, "courses": ["Python", "Math", "History"]},
#     {"name": "bharath", "age": 28, "courses": ["Math", "Physics", "Chemistry", "History"]},
#     {"name": "pandu", "age": 24, "city": "Kochi", "country": "India", "courses": ["Sociology", "Philosophy", "History"]},
# ]
# result = db.students.insert_many(students)  # Insert multiple students
# print("Inserted student IDs:", result.inserted_ids)  # Print the inserted IDs
# print("Student documents inserted successfully.")
# print("Total documents inserted:", len(result.inserted_ids))  # Show how many documents were inserted

# Step 5: Query all documents from the 'students' collection and print each document
print("All student documents:")
for student in db.students.find():  # Retrieve all students from the collection
    print(student)

# # Step 6: Find and print a specific student by name (Example: "pandu")
# pandu = db.students.find_one({"name": "pandu"})
# print("\nFound student 'pandu':")
# print(pandu)

# # Step 7: Query for students with a specific age (Example: age = 22)
# print("\nStudents with age 22:")
# for student in db.students.find({"age": 22}):  # Find students with age = 22
#     print(student)

# # Step 8: Delete one student document where name is "bharath"
# db.students.delete_one({"name": "bharath"})  # Delete the first matching document
# print("\nDeleted student 'bharath'.")

# # Step 9: Delete all students with age less than 22
# db.students.delete_many({"age": {"$lt": 22}})  # Delete all documents where age is less than 22
# print("Deleted students with age less than 22.")

# # Step 10: Print remaining documents in the collection after deletion
# print("\nRemaining student documents after deletion:")
# for student in db.students.find():  # Retrieve and print all remaining students
#     print(student) 
    

result=db.students.update_one(
    {"name": "pandu"},
    {"$set":{"age":53}}
    )    

print("Number of dsocuments updated:",result.modified_count)


for student in db.students.find():
    print(student)
    
    
    