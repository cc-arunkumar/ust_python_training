from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ust_db"]

print("Database 'ust_db' connected successfully")

new_students = [
    {"name": "madhan", "age": 22, "skills": ["python", "data science"]},
    {"name": "gowtham", "age": 44, "skills": ["java", "cloud computing"]},
    {"name": "deva", "age": 24, "skills": ["java", "cloud computing"]},
    {"name": "sujith", "age": 34, "skills": ["c++", "cloud computing"]},
    {"name": "mayil", "age": 22, "skills": ["C", "my_sql"]},
    {"name": "mahe", "age": 19, "skills": ["c", "cloud computing"]},
    {"name": "Arun", "age": 20, "skills": ["python", "html", "css"]},
    {"name": "Meera", "age": 22, "skills": ["java", "spring", "mysql"]},
    {"name": "Kavin", "age": 23, "skills": ["javascript", "react", "nodejs"]},
    {"name": "Riya", "age": 21, "skills": ["mongodb", "express", "api design"]},
    {"name": "Suresh", "age": 25, "skills": ["devops", "docker", "linux"]},
    {"name": "Nila", "age": 24, "skills": ["ui/ux", "figma", "illustrator"]},
    {"name": "Varun", "age": 26, "skills": ["aws", "lambda", "cloudwatch"]},
    {"name": "Divya", "age": 23, "skills": ["data analysis", "pandas", "numpy"]}
]

# Check for duplicates and insert only non-existing documents
for student in new_students:
    # Check if a student with the same name already exists
    existing_student = db.students.find_one({"name": student["name"]})

    if not existing_student:
        # Insert the student if they don't exist
        result = db.students.insert_one(student)

# Print the total number of students after the insertion
total_students = db.students.count_documents({})
print("Total number of students in the collection before deletion:", total_students)

# Delete students with age greater than 40
db.students.delete_many({"age": {"$gt": 40}})

# Recalculate the total number of students after deletion
total_students_after_deletion = db.students.count_documents({})
print("Total number of students in the collection after deletion:", total_students_after_deletion)

# Print all students in the collection
# for student in db.students.find():
#     print(student)

res = db.students.update_one({"name":"Nila"},
                       {"$set":{"age":99}}
                       )
print("Number of documents",res.modified_count)

for student in db.students.find():
    print(student)
