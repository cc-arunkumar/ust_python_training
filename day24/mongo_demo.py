from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['ust_db']
# db.create_collection("students")
# print("database 'ust_db' created Successfully")

# student = {
#     "name": "Amita",
#     "age": 27,
#     "skills": ["python", "mongodb", "data analysis"]
# }

# result = db.students.insert_one(student)
# print("Inserted ID:", result.inserted_id)
# print("1 Student document inserted Successfully.")

# student = {
#     "name": "varsha",
#     "age": 22,
#     "skills": ["python", "mongodb", "SQL"]
# }
# result = db.students.insert_one(student)
# print("Inserted ID:", result.inserted_id)

# student = {
#     "name": "hima",
#     "age": 25,
#     "skills": ["python", "mongodb", "HTML"]
# }
# result = db.students.insert_one(student)
# print("Inserted ID:", result.inserted_id)

# INSERT MANY
# students=[
#     {
#         "name": "yashu",
#         "age": 27,
#     },
#     {
#         "name": "tharun",
#         "age": 24,
#         "skills": ["java", "spring", "sql","linux","networking","Cyber security","C++"]
#     },
#     {
#         "name": "harthi",
#         "age": 30,
#         "email":"harthi@v.com",
#         "gender":"female",
#         "skills": ["python", "machine learning", "deep learning"],
#         "city":"chitoor",
#         "country":"India"
#     }
# ]

# result=db.students.insert_many(students)
# print("Inserted IDs:",result.inserted_ids)
# print("Total Documents",len(result.inserted_ids))
# print("Multiple students inserted successfully")


# Read specific student document
# result=db.students.find_one({"name":"varsha"})
# print(result)

# # Read all student documents
# for student in db.students.find():
#     print(student)


# # Read students with age greater than or equal to 22
# for student in db.students.find({"age":{"$gt":22}}):
#     print(student)
 
 
# delete one document   
# db.students.delete_one({"name":"harthi"})    

# delete many documents
# db.students.delete_many({"age":{"$gt":27}})


# update one
# set the value....

# result=db.students.update_one(
#     {"name":"Amita"},
#     {"$set":{"age":51}}
# )


# result=db.students.update_one(
#     {"name":"hima"},
#     {"$unset":{"age":"10"}}
# )


# update one push
result= db.students.update_one(
    {"name":"hima"},
    {"$push":{"skills":"c"}}
)



# Read all student documents
for student in db.students.find():
    print(student)
