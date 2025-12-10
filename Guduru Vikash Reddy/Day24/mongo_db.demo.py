from pymongo import MongoClient
client=MongoClient('mongodb://localhost:27017')
db=client['ust_db']
collection=db["students"]
# print("Database 'ust_db' created successfully")
# student={
#    "name":"Anjan",
#    "age":23,
#    "skills":["python","fastapi","sql","DSA"]
    
# }
# result=db.students.insert_one(student)
# print("Inserted ID",result.inserted_id)
# print("1 student document inserted suceesfully")

# for student in db.students.find():
#     print(student)
    
    
# student=[
#    {
#    "name":"Arun",
#    "age":23,
   
#    },
# {
#    "name":"Amit",
#    "age":23,
#    "skills":["python","sql","DSA","linux","django","java","React"]
    
# },

# {
#    "name":"pattalam pandu",
#    "age":23,
#    "email":"pandu@gmail.com",
#    "gender":"male",
#    "skills":["python","sql"],
#    "city":"Bombay",
#    "country":"India"
    
# }
# ]
# result=db.students.insert_many(student)
# print("Inserted ID",result.inserted_ids)
# print("total documents inserted:",len(result.inserted_ids))
# print("multiple student record inserted")
# for student in db.students.find():
#     print(student)

# print(db.students.find_one({"name":"Amit"}))
# # print(amit)
# db.students.delete_one({"name":"pattalam pandu"})
for student in db.students.find({"age":{"$gt":22}}):
   print(student)
# db.students.delete_many({"age":{"$gte":24}})

# result=db.students.update_one(
#    {"name":"Amit"},
#    {"$set":{"age":24}}
# )
# print("no of documents updated:",result.modified_count)
# for student in db.students.find():
#     print(student)