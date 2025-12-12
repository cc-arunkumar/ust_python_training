from pymongo import MongoClient

# Connect to MongoDB Atlas cluster
client = MongoClient("mongodb+srv://msovan928_db_user:sovan@clusterfastapi.yrq0el1.mongodb.net/")
db = client["test_db"]
print("DB connected successfully!")

# Documents to insert
students = [
    {
        "name": "Pihoo",
        "age": 25,
        "skills": ["Java", "React"]
    },
    {
        "name": "Sohan",
        "age": 25,
        "skills": ["Java", "React", "Nextjs"]
    },
    {
        "name": "Itishree",
        "age": 25,
        "city": "Ranchi",
        "skills": ["Java", "React", "Nextjs"]
    },
    {
        "name": "Pihoo",
        "age": 25,
        "email": "pihoo@gmail.com",
        "skills": ["Java", "React", "Nextjs"]
    }
]

# Insert all documents
result = db.students.insert_many(students)
print("Inserted student record IDs:", result.inserted_ids)

# Find one student (case-sensitive)
sovan = db.students.find_one({"name": "Sovan"})
print("Found student:", sovan)

# Delete one student
db.students.delete_one({"name": "Pihoo"})
print("Deleted Pihoo")

db.students.update_one(
    {"name": "Sovan"},          
    {"$set": {"age": 90}}       
)




for student in db.students.find():
    print(student)
