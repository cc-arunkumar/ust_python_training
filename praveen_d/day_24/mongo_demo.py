from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ust_db"]

# print("Db created")

# student = {
#     "name": "Amit",
#     "age": 20,
#     "skills": ["Python", "Java", "Pysql"]
# }
# student1 = {
#     "name": "Amita",
#     "age": 21,
#     "skills": ["Python", "Java", "Pysql"]
# }

# students_data=[{
#       "name": "Raju",
#     "age": 22,
#     "skills": ["Python", "Java", "Pysql","Linux"]
    
# },
#                {
#       "name": "Teju",
#     "age": 29,
#     "skills": ["Python", "Java", "Pysql","Linux"],
#     "Languages":["Tamil","Hindi","Malayalam"]
    
# },
#                {
#       "name": "Motu",
#     "age": 29,
#     "skills": ["Python", "Java", "Pysql","Linux"],
#     "Hobbies":["Cricket","Football","Carrom"]
    
# },
# ]

# result = db.students.insert_one(student1)
# result1=db.students.insert_many(students_data)



# print("Inserted successfully:", result.inserted_id)
# # print("Many students:",result1.inserted_ids)

# for st in db.students.find():
#     print(st)


# read one
# name=db.students.find_one({"name":"Motu"})
# print(name)

# # find with condition
# name1 =db.students.find_one({"age":{"$gt":20}})
# print(name1)

# for st in db.students.find({"age":{"$gt":22}}):
#     print(st)

# # delete one
# db.students.delete_one({"name":"Motu"})
# print("Deleted")
    
# delete many
# db.students.delete_many({"name":"Amit"})

# update
# db.students.update_many({"age":{"$lt":100}},
#                        {"$set":{"age":11}}
#                        )

# db.students.update_many({"age":{"$exists":True}},
#                        {"$rename":{"age":"ages"}})

db.students.update_many({"skills":{"$exists":True}},
                       {"$pull":{"skills":"Python"}}
                       )
for st in db.students.find():
    print(st)