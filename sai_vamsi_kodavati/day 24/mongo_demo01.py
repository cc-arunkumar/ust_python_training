from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Select the database
db = client['ust_db']

print("Db Connected")

# # Correct dictionary syntax
# students = {
#     "name": "Sai Vamsi",
#     "age": 22,
#     "skills": ["Python", "MongoDb","Fast API"]
# }

# # Insert the document
# result = db.students.insert_one(students)

# print("Inserted ID:", result.inserted_id)
# print("1 student document inserted successfully")

# # Read all student documents
# for students in db.students.find():
#     print(students)

students = [
    {
    "name" : "Vijay",
    "age" : 22
    },
    {
    "name"  :"Karan",
    "age"  : 23,
    "skills" : ["Python","Java","Mongodb"],
    "Gender" : "Male"
    },
    {
        "name" : "Sai Vamsi",
        "age" : 22,
        "skills" : ["Python","Fast API","Mongodb","Mysql","Html","css","Javascript"],
        "Gender"  :"Male",
        "City" : "Trivandrum",
        "Ciuntry" : "India" 
    }
]

# result = db.students.insert_many(students)
# print("Inserted IDs:",result.inserted_ids)
# print("Total documents inserted:",len(result.inserted_ids))
# print("Multiple student document inserted successfully")

# for student in db.students.find():
#     print(student)

# # read students with age greater than equal to 22

# for student in db.students.find({"age":{"$gte" : 22}}):
#     print(student)

# # Read specific student document

# karan = db.students.find_one({"name":'Karan'})
# print(karan)
    
# # Delete one document

# db.students.delete_one({"name":"Karan"})

# # Delete many documents

# db.students.delete_many({"age":{"$lt":22}})

# for student in db.students.find():
#     print(student)

# Update 

result = db.students.update_one(
    {"name":"Amit"},
    {"$set" : {"age":35}}
)

print("Number of documents updated:",result.modified_count)

for student in db.students.find():
    print(student)


