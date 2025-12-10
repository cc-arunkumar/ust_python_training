from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ust_mongo_db"]
collection = db["employees"]

collection.insert_one({
    "emp_id": 206,
    "name": "Prithvi Rajeev",
    "department": "AI",
    "age": 22,
    "city": "Bhubaneswar",
    "category": "Fresher"
})


for doc in collection.find():
    print(doc)


collection.update_one({"emp_id": 202}, {"$set": {"city": "Mumbai", "department": "DevOps"}})

collection.delete_one({"emp_id": 203})

collection.delete_many({"department": "Testing"})
