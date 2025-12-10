from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017/')
db=client['ust_db']
# print("Database 'ust_db' created successfully")

# student={
#     "name":"lax",
#     "age":24,
#     "skills":["python","java","sql"]}

#insert 1 document
# result=db.students.insert_one(student)
# print("Inserted id:",result.inserted_id)

#read all students documents
# for student in db.students.find():
#     print(student)
    
# students=[
#     {"name":"john","age":22,"skills":["c++","html","css"]},
#     {"name":"alice","age":23,},
#     {"name":"bob","age":25, "skills":["javascript","react"]}
    
#         ]

# Insert multiple records

# result=db.students.insert_many(students)
# print("Inserted ids:",result.inserted_ids)
# print("Total documents inserted:",len(result.inserted_ids))

# for student in db.students.find():
#     print(student)



#Read a specific student
# bob=db.students.find_one({"name":"bob"})
# print(bob)
    
    
#Read students whose age is greater than 22
# for student in db.students.find({"age":{"$gt":22}}):
#     print(student)

#Delete one Document
# db.students.delete_one({"name":"lax"})
# for student in db.students.find():
#     print(student)
    
#Delete many documents
# db.students.delete_many({"age":{"$lte":22}})
# for student in db.students.find():
#     print(student)
    
    
#Update
#db.students.update_one(filter,update)

#update one document
result=db.students.update_one(
    {"name":"alice"},       #filter
    {"$set":{"age":25}}     #update
    )

# print("Numer od doc updated:",result.modified_count)

# print(db.students.find({"name":"alice"}))
for student in db.students.find():
    print(student)