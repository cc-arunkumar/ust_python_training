from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017/')

db=client['ust_db']

print("Database connected succesfully")


# student={
#     "name":"sai",
#     "age":20,
#     "skills":["python","java"]


# }



# result=db.students.insert_one(student)
# print("inserted id:",result.inserted_id)
# print("1 student inserted successfully")



# student=[
    
#     {
#         "name":"vikash",
#         "age":22
#     },
#     {
#         "name":"anjan",
#         "age":"23",
#         "skills":["python","java","sql","data analytics"]
#     },
#     {
#         "name":"arun",
#         "age":23,
#         "email":"vamshi@gmail.com",
#         "gender":"Male",
#         "skills":["python","java"],
#         "city":"Hyderabad"

#     }
# ]

# result=db.students.insert_many(student)
# print("Inserted ids",result.inserted_ids)
# print("Total documents inserted:",len(result.inserted_ids))
# print("Multiple records inserted successfully")

# for student in db.students.find():
#     print(student)


# sai=db.students.find_one({"name":"sai"})

# print(sai)

# for student in db.students.find({"age":{"$gte":22}}):
#     print(student)

# db.students.delete_one({"name":"arun"})

# db.students.delete_many({"age":{"$lte":22}})


# result=db.students.update_one(
#     {"name":"abhi"},
#     {"$set":{"age":"45"}}
# )
# print("Number of documents updated",result.modified_count)


# result=db.students.update_one(
#     {"name":"vamshi"},
#     {"$push":{"skills":"mysql"}}
# )



# result=db.students.update_one(
#     {"name":"anjan"},
#     {"$pull":{"skills":"sql"}}
# )
# print("Number of documents updated",result.modified_count)

result=db.students.update_one(
    {"name":"anjan"},
    {"$":{"skills":"sql"}}
)
print("Number of documents updated",result.modified_count)



for student in db.students.find():
    print(student)