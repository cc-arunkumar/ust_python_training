import pymongo
from pymongo import MongoClient

db = client = MongoClient('mongodb://localhost:27017/')
print("Database 'ust_db' creadted")

student = {
    "name" : "Deva",
    "age" : 26,
    "skills" : ["Python", "React"]
}
result = db.ust.students.insert_one(student)
print("Insert student record ID : ", result.inserted_id)
print("1 Student inserted successfully !")


students = [
    {
    "name" : "Sohan",
    "age" : 26,
    "skills" : ["Python", "React"]
    },
    {
    "name" : "Rohit",
    "age" : 26,
    "skills" : ["Python", "React","Java","Mongodb","Sql"]
    },
    {
    "name" : "Sneha",
    "age" : 26,
    "email" : "sneha@gmail.com",
    "gender" : "female",
    "city" : "Mumbai",
    "skills" : ["Python", "React","Java","Mongodb","Sql"]
    }
]

result = db.ust.students.insert_many(students)
print("Insert ID : ", result.inserted_ids)
print("Total documents inserted: ",len(result.inserted_ids))

# Read all student documents
for student in db.ust.students.find():
    print(student)

# Read specific student document
sneha = db.ust.students.find_one({"name":"Sneha"})
print(sneha)

for student in db.ust.students.find({"age":{"$lt":26}}):
    print(student)

# delete one document
db.ust.students.delete_one({"name":"Sohan"})
for student in db.ust.students.find():
    print(student)

result = db.ust.students.update_one(
    {"name":"Rohit"},
    {"$set":{"age":23}}
)
print("Number of documents updated: ",result.modified_count)
for student in db.ust.students.find():
    print(student)