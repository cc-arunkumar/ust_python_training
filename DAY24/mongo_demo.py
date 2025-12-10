from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["ust_db"]

print("Database Created Successfully")

students = [
    {
        "name": "arun",
        "age": 24,
        "skills": ["c++", "js", "db"],
        "city":"Trichy"
    },
    {
        "name": "Sks",
        "age": 24,
        "skills": ["c++", "js", "db","full stack","AI"]
    },
    {
        "name": "varun",
        "age": 23,
        "skills": ["c#", "anugular", "gen-ai"],
        "gender":"female"
    }
]

result = db.students.update_one(
    {"name":"Gowtham"},
    {"$rename":{"age":"living"}}
)

print("Inserted IDs:", result.modified_count)
# print("Students added successfully")

for student in db.students.find():
    print(student)


# result=db.students.insert_many(students)
# print("Inserted id: ",result.inserted_ids)
# print("Documents Inserted :",len(result.inserted_ids))

# db.students.delete_one({"age":{"$gt":24}})
# result = db.students.delete_one({"age": {"$gt": 24}})
# print(f"Deleted {result.deleted_count} document")



for s in db.students.find_one():
    print(s)
    
    
    
    
    
    
""" SAMPLE OUTPUT

Database Created Successfully
Inserted IDs: 0
{'_id': ObjectId('6937a37a3b1c157bdff8532b'), 'name': 'Gowtham', 'skills': ['python', 'mongodb', 'Data analysis'], 'living': 22}
{'_id': ObjectId('6937a58a0c39a7441f65c335'), 'name': 'Mani', 'age': 23, 'skills': ['java', 'React', 'Web']}
_id
name
skills
living
  
  """