from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client['ust_db']
print("Database 'ust_db' created successfully")

student = {
    "name":"Tanu",
    "age":22,
    "skills":["Python","mongodb"]
}
# result = db.student.insert_one(student)
# print("Inserted id:",result.inserted_id)

student = [{
    "name":"Riya",
    "age":23,
    "skills":["Python","mongodb","sql","networking"]
    },{
        "name":"Amit",
        "age":23,
        "skills":["Python","cyber security","c++","linux"],
        "city":"mumbai",
        "country":"India",
        "Gender":"Male"
    },
    {
        "name":"muskan",
        "age":22
    }]

# result=db.student.insert_many(student)
# print("Inserted ids:",result.inserted_ids)
# print("total document inserted:",len(result.inserted_ids))
# print("multiple data inserted successfully")


# amit = db.student.find_one({"name":"Amit"})
# print(amit)

# for student in db.student.find({"age":{"$gt":22}}):
#     print(student)


# db.student.delete_one({"name":"Amit"})


# db.student.delete_many({"age":{"$gt":22}})
# for student in db.student.find():
#     print(student)
    
result = db.student.update_one(
    {"name":"Tanu"},
    {"$set":{"age":24}}
)

# db.student.update_one(
#     {"name":"Taniya"},
#     {"$push":{"skills":"django"}}
# )

db.student.update_one(
    {"name":"Tanu"},
    {"$addToSet":{"hobby":"dance"}}
)
db.student.update_one(
    {"name":"Tanu"},
    {"$addToSet":{"hobby":"cooking"}}
)

for student in db.student.find():
    print(student)

