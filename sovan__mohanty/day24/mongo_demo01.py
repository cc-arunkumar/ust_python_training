from pymongo import MongoClient

client=MongoClient("mongodb+srv://msovan928_db_user:sovan@clusterfastapi.yrq0el1.mongodb.net/")
client['ust_db']
# print("Database 'ust_db' created successfully.")
db=client["ust_db"]
student=[{
    "name":"Rohit",
    "age":21
},
{
    "name":"Sneha",
    "age":23,
    "skills":["c++","linux","networking","cyber security","python"]
},
{
    "name":"Karan",
    "age":25,
    "email":"karan@example.com",
    "skills":["c++","linux","networking","cyber security"],
    "gender":"male",
    "city":"mumbai"
    
}
]



# result=db.students.insert_many(student)

# print("Inserted ID:",result.inserted_ids)
# print("Total ids inserted ",len(result.inserted_ids))
# print("Multiple students document inserted successfully")
# for student in db.students.find():
#     print(student)
# sneha=db.students.find_one({"name":"Senha"})
# print(sneha)

# for student in db.students.find({"age":{"$gte":22}}):
#     print(student)

# db.students.delete_one({"name":"Rohit"})

# db.students.delete_many({"age":{"$lt":22}})
result=db.students.update_one({"name":"Karan"},{"$set":{"age":52}})
print("Number of documents updated: ",result.modified_count)

for student in db.students.find():
    print(student)
