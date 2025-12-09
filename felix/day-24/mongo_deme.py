from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["ust_db"]
# db.create_collection("students")
# print(client.list_database_names())

# student = {
#     "name":"Felix",
#     "age":23,
#     "skills":["python","mongodb"]
# }

# result = db.students.insert_one({
#                                  "name":"Arun",
#     "age":23,
#     "skills":["python","mongodb","Git"]
# })

# student = [
#     {
#     "name":"Karan",
#     "age":20,
#     "skills":["python","mongodb","cyber security","c++"]
#     },
#     {
#         "name":"Akhil",
#     "age":22,
#     "skills":["python","mongodb"],
#     "email":"akhil@abc.com"
#     },
#     {
#         "name":"Arjun",
#     "age":23,
#     "skills":["python","mongodb","Git"],
#     "city":"Trivandrum",
#     "State":"Kerala"
#     }
# ]

# db.students.insert_many(student)

# # Read one record
# print("Record of Akhil: ",db.students.find_one({"name":"Akhil"}))

# # Delete one record
# db.students.delete_one({"name":"Arun"})

# # print record which are satisfiying certain condetion
# for student in db.students.find({"age":{"$gte":22}}):
#     print(student)

# Delete many record
# db.students.delete_many({"age":{"$lt":22}})

# update one record
db.students.update_one({"name":"Felix"},{"$set":{"age":25}})
db.students.update_one({"name":"Felix"},{"$addToSet":{"skills":"Cyber Security"}})

for student in db.students.find():
    print(student)