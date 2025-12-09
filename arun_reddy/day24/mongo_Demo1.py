from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017/')
client["ust_db"]
print(client.list_database_names())
print("Database created successfully")
db=client["ust_db"]
# db.create_collection("students")
print("Collection created successfully")
# insert one into database
# student={
#     "name":"John Doe",
#     "age":21,
#     "skills":["Python","MongoDB","Data Analysis"]
# }
# result=db.students.insert_one(student)
# print("Inserted to", result.inserted_id)
# print("1 student inserted successfully")

# insert one into database
# student2={
#     "name":"Jane Smith",
#     "age":22,
#     "skills":["Java","SQL","Machine Learning"]
# }
# result2=db.students.insert_one(student2)
# print("Inserted to", result2.inserted_id)
# print("1 student inserted successfully")
# print("All students in the collection:")



# insert many
# db.students.insert_many([
#     {"name":"Arun","age":"89","skills":["python","c++"]},
#     {"name":"felix","age":"78","skills":["java","c"]}
# ])
# insert many
# db.students.insert_many([
#     {"name":"Aryan","age":"34","skills":["python","c++"]},
#     {"name":"David","age":"45","skills":["java","c"]}
# ])

# find_one
print("the finded collection object ",db.students.find_one({"name":"John Doe"}))


# update_one
# db.students.update_one(
#     {"name":"John Doe"},
#     {"$set": {"age":1000}}
# )

# update_many
db.students.update_many(
    {"age":{"$gt":30}},
    {"$set":{"status":"Senior"}}
)

# find_one and delete_one
db.students.find_one_and_delete(
    {"name":"John Doe"}
)


db.students.delete_many({
    "age":{"$gt":50}
})







results=db.students.update_one(
    {"name":"Arun"},
    {"$set":{"age":32}}
)
print(results)
for student in db.students.find():
    print(student)