from pymongo import MongoClient
 
client = MongoClient('mongodb://localhost:27017/')
db = client['mongo_db']
print("Database 'mongo_db' created")
 
student = {
    "name": "Aks",
    "age": 22,
    "skills": ["python", "sql", "data analysis"]
}
 
 
result = db.students.insert_one(student)
print("Inserted id:", result.inserted_id)
 
for student in db.students.find():  
    print(student)
 
students=[
    {
        "name":"swetha",
        "age":24
    },
    {
        "name":"lessi",
        "age":23,
        "skills":["c","linux","cyber security"]
    },
    {  
        "name":"roshan",
        "age":25,
        "skills":["c","linux"],
        "city":"Mumbai",
        "country":"India"
    }
]
 
result=db.students.insert_many(students)
print("Inserted ids:",result.inserted_ids)
print("total documents inserted:",len(result.inserted_ids))
 
for student in db.students.find():  
    print(student)
   
db.students.delete_one({"name":"roshan"})
for student in db.students.find():  
    print(student)
 
result=db.students.find_one({"name":"Akshhh"})
print(result)
 
db.students.delete_many({"age":{"$lt":22}})
for student in db.students.find():  
    print(student)
 
result=db.students.update_one(
    {"name":"Aks"},
    {"$set":{"age":21}}
)
for student in db.students.find():  
    print(student)