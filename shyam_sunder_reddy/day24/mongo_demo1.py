from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/")
db=client["ust_db"]

# print("database created successfully")

## insert one
# student={
#     "name":"ram",
#     "age":21,
#     "skills":["python","mongodb"]
# }
# result=db.students.insert_one(student)
# print("Inserted ID:",result.inserted_id)
# print("student record successfully")


# # insert many
# student=[{
#     "name":"anjan",
#     "age":23,
#     "skills":["python","mongodb"]
#     },
#     {"name":"vikas",
#     "age":25,
#     "skills":["python","java"]
#     }
#     ]

# result=db.students.insert_many(student)
# print("student record successfully")
#{'_id': ObjectId('6937b2d09de60a8b66b5054f'), 'name': 'shyam', 'age': 21, 'skills': ['python', 'java']}
# {'_id': ObjectId('6937b2fc3397a7fa98f1f311'), 'name': 'ram', 'age': 21, 'skills': ['python', 'mongodb', 'java']}
# {'_id': ObjectId('6937b3adbe83851436add9fc'), 'name': 'anjan', 'age': 21, 'skills': ['python', 'mongodb']}      
# {'_id': ObjectId('6937b3adbe83851436add9fd'), 'name': 'vikas', 'age': 21, 'skills': ['python', 'java']}
# {'_id': ObjectId('6937ce95f959f6076dedfd0e'), 'name': 'anjan', 'age': 23, 'skills': ['python', 'mongodb']}      
# {'_id': ObjectId('6937ce95f959f6076dedfd0f'), 'name': 'vikas', 'age': 25, 'skills': ['python', 'java']}

##find all
# for stud in db.students.find():
#     print(stud) 

##find one
# print(db.students.find_one({"name":"anjan"}))

##find all by query
# for stud in db.students.find({"age":{"$gte":21}}):
#     print(stud)


##delete
# db.students.delete_one({"name":"vikas"})
## Sample output
# {'_id': ObjectId('6937b2d09de60a8b66b5054f'), 'name': 'shyam', 'age': 21, 'skills': ['python', 'java']}
# {'_id': ObjectId('6937b2fc3397a7fa98f1f311'), 'name': 'ram', 'age': 21, 'skills': ['python', 'mongodb', 'java']}
# {'_id': ObjectId('6937b3adbe83851436add9fc'), 'name': 'anjan', 'age': 21, 'skills': ['python', 'mongodb']}


## delete many
# db.students.delete_many({"age":{"$gte":22}})
# print("deleted people where age greater than 21")
# {'_id': ObjectId('6937b2d09de60a8b66b5054f'), 'name': 'shyam', 'age': 21, 'skills': ['python', 'java']}
# {'_id': ObjectId('6937b2fc3397a7fa98f1f311'), 'name': 'ram', 'age': 21, 'skills': ['python', 'mongodb', 'java']}
# {'_id': ObjectId('6937b3adbe83851436add9fc'), 'name': 'anjan', 'age': 21, 'skills': ['python', 'mongodb']}      
# {'_id': ObjectId('6937b3adbe83851436add9fd'), 'name': 'vikas', 'age': 21, 'skills': ['python', 'java']}

#update
# db.students.update_one({"name":"anjan"},{"$set":{"name":"paul"}})
# {'_id': ObjectId('6937b2d09de60a8b66b5054f'), 'name': 'shyam', 'age': 21, 'skills': ['python', 'java']}
# {'_id': ObjectId('6937b2fc3397a7fa98f1f311'), 'name': 'ram', 'age': 21, 'skills': ['python', 'mongodb', 'java']}
# {'_id': ObjectId('6937b3adbe83851436add9fc'), 'name': 'paul', 'age': 21, 'skills': ['python', 'mongodb']} 

#update many
# db.students.update_many({"age":21},{"$set":{"age":25}})
# {'_id': ObjectId('6937b2d09de60a8b66b5054f'), 'name': 'shyam', 'age': 25, 'skills': ['python', 'java']}
# {'_id': ObjectId('6937b2fc3397a7fa98f1f311'), 'name': 'ram', 'age': 25, 'skills': ['python', 'mongodb', 'java']}
# {'_id': ObjectId('6937b3adbe83851436add9fc'), 'name': 'paul', 'age': 25, 'skills': ['python', 'mongodb']}

for stud in db.students.find():
    print(stud) 