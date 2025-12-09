from pymongo import MongoClient
client=MongoClient('mongodb://localhost:27017/')
db=client['ust_db']

# print("Database created successfully")

student={
    "name":"Tara",
    "age":25,
    "skills":["Python","mongodb","data analytics"]
}

# insert 1 document
result=db.students.insert_one(student)
print("Inserted ID:",result.inserted_id)
print("Student 1 document inserted successfully")

students=[
    {"name":"Sneha",
     "age":23,
     "skills":["C++","linux","networking","cyber","mongodb"]
     
     },
    
    {
        "name":"Jeffrey",
        "age":24
    },
    {
        "name":"Karan",
        "age":22,
        "email":"karan@example.com",
        "gender":"male",
        "city":"Mumbai"
        
    }
]

result=db.students.insert_many(students)
print("Inserted IDs:",result.inserted_ids)
print("Total documents inserted:",len(result.inserted_ids))
print("Multiple documents inserted successfully")


tara=db.students.find_one({"name":"Tara"})
print(tara)

for student in db.students.find({"age":{"$gte":22}}):
    print(student)
  
db.students.delete_one({"name":"Amit"})
db.students.delete_many({"age":{"$lt":22}})


result=db.students.update_one(
    {"name":"Tara"},           #filter
    {"$set":{"age":27}}        #update
)
print("Number of documents updated",result.modified_count)

# reading all student documents
for student in db.students.find():
    print(student)