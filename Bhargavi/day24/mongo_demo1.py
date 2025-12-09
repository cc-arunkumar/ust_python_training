# The code connects to a MongoDB database, inserts multiple student records, performs operations such as reading, deleting,
# updating records, and prints the modified student data.
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["ust_db"]
# db.create_collection("students")
# print(client.list_database_names())

student = [
    {
        "name": "Bhargavi",
        "age": 22,
        "skills": ["python", "mongodb", "data analyst"]
    },
    {
        "name": "Vatsala",
        "age": 24,
        "skills": ["python", "machine learning"]
    },
    {
        "name": "Siddhi",
        "age": 25,
        "skills": ["cloud", "AWS", "data science"]
    },
    {
        "name": "Vatsala",
        "age": 24,
        "skills": ["python", "machine learning"],
        "hobbies": "doremone",
        "play": "games"
    },
    {
        "name": "Siddhi",
        "age": 25,
        "skills": ["cloud", "AWS", "data science"]
    },
    {
        "name": "Meena",
        "age": 22,
        "skills": ["python", "mongodb"],
        "email": "meena@abc.com"
    },
    {
        "name": "Chinnu",
        "age": 24,
        "skills": ["python", "mongodb", "Django"],
        "email": "chinnu@abc.com",
        "city": "Hyderabad",
        "State": "Chennai"
    }
]

db.students.insert_many(student)

# Read one record
print("Record of Meena: ", db.students.find_one({"name": "Meena"}))

# Delete one record
db.students.delete_one({"name": "Siddhi"})

# print records that satisfy a certain condition
for student in db.students.find({"age": {"$gte": 24}}):
    print(student)

# Delete many records
db.students.delete_many({"age": {"$lt": 24}})

# Update one record
db.students.update_one({"name": "Bhargavi"}, {"$set": {"age": 26}})
db.students.update_one({"name": "Bhargavi"}, {"$addToSet": {"skills": "Cloud Computing"}})

for student in db.students.find():
    print(student)
