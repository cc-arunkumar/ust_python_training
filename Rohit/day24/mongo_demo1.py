from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ust_db"]
collection = db["talent_management"]

# Insert sample documents
sample_data = [
    {"name": "Alice", "role": "Software Engineer", "experience": 3},
    {"name": "Rohit", "role": "Software Engineer", "experience": 3, "email": "rohit@gmail.com"},
    {"name": "Harsh", "role": "Software Engineer", "experience": 3,
     "skills": ["c++", "linux", "networking", "cyber security", "python", "mongodb"]}
]
collection.insert_many(sample_data)

# result = collection.insert_many(sample_data)
# print("Inserted_id",result.inserted_ids) 
# print("Total documents inserted", len(result.inserted_ids)) 
# print("Database talent management created successfully") 
#print("Inserted document ID:", result.inserted_ids)

# alice = collection.find_one({"name":"Alice"}) 
# print(alice) # # delete one document 
# collection.delete_one({"name":"Alice"}) 
# # for row in collection.find({"role":"Software Engineer"}, {"name"}): 
# # print(row)
# print("Total documents inserted", len("talent_management"))






print("Initial documents:")
for doc in collection.find():
    print(doc)

collection.update_one({"name": "Rohit"}, {"$set": {"experience": 5, "email": "rohit_new@gmail.com"}})

collection.update_one({"name": "Rohit"}, {"$unset": {"email": ""}})

collection.update_one({"name": "Harsh"}, {"$rename": {"skills": "technical_skills"}})

collection.update_one({"name": "Alice"}, {"$inc": {"experience": 1}})

# 5. $mul → multiply a numeric field
collection.update_one({"name": "Alice"}, {"$mul": {"experience": 2}})

# 6. $min / $max → conditional updates
collection.update_one({"name": "Alice"}, {"$min": {"experience": 2}})
collection.update_one({"name": "Alice"}, {"$max": {"experience": 10}})


collection.update_one({"name": "Harsh"}, {"$push": {"technical_skills": "docker"}})

# 8. $addToSet → add element only if not present
collection.update_one({"name": "Harsh"}, {"$addToSet": {"technical_skills": "python"}})

# 9. $pop → remove first or last element
collection.update_one({"name": "Harsh"}, {"$pop": {"technical_skills": 1}})   # remove last
collection.update_one({"name": "Harsh"}, {"$pop": {"technical_skills": -1}})  # remove first

# 10. $pull → remove specific element
collection.update_one({"name": "Harsh"}, {"$pull": {"technical_skills": "linux"}})

# 11. $each with $push → add multiple elements
collection.update_one({"name": "Harsh"}, {"$push": {"technical_skills": {"$each": ["git", "aws", "kubernetes"]}}})

# 12. $position → insert at specific index
collection.update_one({"name": "Harsh"}, {"$push": {"technical_skills": {"$each": ["golang"], "$position": 1}}})

# ---------------- RESULTS ----------------
print("\nDocuments after updates:")
for doc in collection.find():
    print(doc)
