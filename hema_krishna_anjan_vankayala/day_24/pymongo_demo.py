from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client['ust_db']

print(db)
# Create a new collection
collection = db["students"]

# student = {
#     "name":"Anita",
#     "age": 22,
#     "skills" : ['python','mongodb','qwerty']
# }

students = [
    {
        "name":"Anita",
        "age": 22,
        "skills" : ['python','mongodb','qwerty']
    },
    {
        "name":"Ravi",
        "age": 23,
        "skills" : ['java','sql','html','css','js']
    },
    {
        "name":"Sonal",
        "age": 21,
        "email":"sonal@example.com",
        "skills" : ['c++','linux','aws'],
        "city":"Pune",
        "country":"India"
        
    }
]
# print(client.list_database_names())
# result = db.students.insert_many(students)
# for student in db.students.find({"age": {"$gte":22}}):
#     print(student)

# db.students.delete_one({"name":"Anita"})
# for student in db.students.find():
#     print(student)

# for student in db.students.find({"skills":{"$in":["python"]}}):
#     print(student)


result = db.students.update_one( {"name":"Amit"},{"$set":{"age":30}})

print(result.modified_count)

for student in db.students.find():
    print(student)