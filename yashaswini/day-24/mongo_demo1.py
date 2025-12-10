from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['ust_db']

students = [
    {
        "name": "lucas",
        "age": 22
    },
    {
        "name": "will",
        "age": 23,
        "skills": ["python", "java", "c++", "javascript", "html", "css"]
    },
    {
        "name": "steeve",
        "age": 24,
        "email": "steeve@example.com",
        "gender": "male",
        "skills": ["javascript", "react"],   # <-- added missing comma here
        "city": "Bangalore",
        "country": "India"
    }
]

# result = db.students.insert_many(students)
# print("Inserted IDs:", result.inserted_ids)
# print("Total students inserted:", len(result.inserted_ids))
# print("Multiple students inserted successfully")

# for student in db.students.find():
#     print(student)


#find_one
# maxine = db.students.find_one({"name": "maxine"})
# print(maxine)

#find student with age greater than 22
# for student in db.students.find({"age": {"$gt": 22}}):
#     print(student)

#delete_one
# db.students.delete_one({"name": "will"})
# for student in db.students.find():
#     print(student)
    
# delete_many
# db.students.delete_many({"age": {"$lte": 20}})
# for student in db.students.find():
#     print(student)

# update_one
# result = db.students.update_one(
# {"name" : "steeve"}, #filter
# {"$set" : {"age" : 25}}) #update
# print("Documents updated :",result.modified_count)
# for student in db.students.find():
#     print(student)
    
    
# Remove the 'email' field from steeve
# db.students.update_one(
#     {"name": "steeve"},
#     {"$unset": {"email": ""}}
# )
# for student in db.students.find():
#     print(student)

# Increase lucas's age by 1
# db.students.update_one(
#     {"name": "lucas"},
#     {"$inc": {"age": 1}}
# )
# for student in db.students.find():
#     print(student)

# # Add mongodb skill to steeve skills array
# db.students.update_one(
#     {"name": "steeve"},
#     {"$push": {"skills": "mongodb"}}
# )
# for student in db.students.find():
#     print(student)

# # Add "python" skill to steeve only if it's not already there
# db.students.update_one(
#     {"name": "steeve"},
#     {"$addToSet": {"skills": "python"}}
# )
# for student in db.students.find():
#     print(student)

# # Rename 'city' field to 'hometown'
db.students.update_one(
    {"name": "steeve"},
    {"$rename": {"city": "hometown"}}
)
for student in db.students.find():
    print(student)

