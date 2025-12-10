from pymongo import MongoClient

client= MongoClient('mongodb://localhost:27017/')

db=client['students']

print("Data base craetion succesfull")

student={
    "name" :"Amit ",
    "age":22,
    "skills":["Python","C"]
}
# result=db.students.insert_one(student)
studentslist=[{
    "name" :"Ajay ",
    "age":292,
    "skills":["Python","C","java"]
},{
    "name" :"Akash  ",
    "age":292,
    "skills":["Python","C","java","a","b"]
},{
    "name" :"Ajaykumar ",
    "age":2942,
    
    
}]
# result=db.students.insert_many(studentslist)
# print("inserted ids:",result.inserted_ids)


    
# db.students.delete_one({"name":"Akash  "})
# db.students.delete_many({"age":{"$lt":200}})

result=db.students.update_many({"name":"Ajay "},{"$pull":{"skills":"Python"}})
print("no of rows modified ",result.modified_count)
for student in db.students.find():
    print(student)
    
{"name":"Karen","age":28,"department":"Software Engineering","skills":["Python","FastAPI","MongoDB"],"projects":[{"project_name":"E-Commerce Platform","role":"Backend Developer"},{"project_name":"AI Chatbot","role":"Lead"}],"experiance_years":4}
