# # from pymongo import MongoClient

# # client=MongoClient('mongodb://localhost:27017/')
# # client['ust_db']
# # print("DB created successfully")

from pymongo import MongoClient

# Connect to MongoDB (default localhost:27017)
client = MongoClient("mongodb://localhost:27017/")

# This line is enough to create the database + collection when data is inserted
db = client["ust_db"]     # creates ust_db (but still invisible for now)

# student={
#     "name": "James Bond",
#     "age": 35,
#     "skills": ["Spycraft", "Advanced Driving", "Gadgets 101"]
# }

# result=db.students.insert_one(student)
# print("Inserted student with _id:", result.inserted_id)
# print("1 Student record inserted successfully.")

# for student in db.students.find():
#     print(student)


s2=[
    
{
    "name": "Ethan Hunt",
    "age": 40,
    "skills": ["Disguise", "Hand-to-Hand Combat", "High-Speed Driving"]
},
{
        "name": "Jason Bourne",
        "age": 38,
        "skills": ["Marksmanship", "Espionage", "Survival Skills"],
        "gender": "Male",
        "country": "USA"
},
{
        "name": "Natasha Romanoff",
        "age": 32,
        "skills": ["Martial Arts", "Espionage", "Interrogation"],
        "gender": "Female",
        "country": "Russia",
        "team":"Avengers"
}
]

# result=db.students.insert_many(s2)
# print("Inserted IDs:",result.inserted_ids)
# print(f"{len(result.inserted_ids)} Student records inserted successfully.")
# print("Multiple recoreds inserted.")


# nat=db.students.find_one({"name": "Natasha Romanoff"})
# print(nat)

# for i in db.students.find({"age":{"$gt":21}}):
#     print(i)
    
# db.students.delete_one({"name":"Jason Bourne"})
# db.students.delete_many({"age":{"$gte":40}})


for i in db.students.find():
    print(i)
    
res=db.students.update_one(
    {"name":"Ethan Hunt"},
    {"$set":{"age":40,"team":"IMF"}}
)
print("Number of documents updated:",res.modified_count)

for i in db.students.find():
    print(i)



# from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017/")

# print("Server status:")
# print(client.server_info()['version'])          # will raise error if not connected

# print("\nList of databases that actually exist right now:")
# print(client.list_database_names())

# # Force create ust_db again
# db = client["ust_db"]
# col = db["students"]
# col.insert_one({"test": "force create", "time": __import__('datetime').datetime.utcnow()})

# print("\nAfter insert - databases again:")
# print(client.list_database_names())

# print("\nIf you see 'ust_db' in the list above → it is created.")
# print("Refresh Compass → it MUST appear now.")