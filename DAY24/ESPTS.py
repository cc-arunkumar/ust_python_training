from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ESPTS"]

# ------------------ BULK UPLOAD DATA ------------------
def bulk_upload():
    with open("data.json", "r") as file:
        data = json.load(file)
    result = db.employees.insert_many(data)
    print("Bulk uploaded file count:", result.inserted_ids)

# ------------------ UPLOAD SINGLE DATA ------------------
def insert_employee(single_emp):
    result = db.employees.insert_one(single_emp)
    print("One employee added")

# Sample employee data
single_employee = {
    "emp_id": 110,
    "name": "Rakesh Pillai",
    "age": 30,
    "department": "Cybersecurity",
    "skills": ["networking", "firewall", "linux"],
    "projects": [
        {"name": "SecuritySuite", "status": "deployed"}
    ],
    "experience_years": 7
}

# ------------------ READ OPERATIONS ------------------
# Read by employee ID
def read_employee_by_id(emp_id):
    result = db.employees.find_one({"emp_id": emp_id})
    print(result)

# Read employee by department
def read_employee_by_dept(dept):
    result = db.employees.find({"department": dept})
    for i in result:
        print(i)

# Read employee by city
def read_employee_by_city(city):
    result = db.employees.find({"address.city": city})
    for i in result:
        print(i)

# Read employee by skill
def read_employee_by_skill(skill):
    result = db.employees.find({"skills": skill})
    for emp in result:
        print(emp)

# Read employee by experience
def read_employee_by_exp(exp):
    result = db.employees.find({"experience_years": exp})
    for emp in result:
        print(emp)

# Sort employees by age
def read_employee_age(sort=True):
    s = 1 if sort else -1
    results = db.employees.find().sort("age", s)
    for emp in results:
        print(emp)

# Sort employees by experience
def read_employee_experience(sort=True):
    s = 1 if sort else -1
    results = db.employees.find().sort("experience_years", s)
    for emp in results:
        print(emp)

# Sort employees by name
def read_employee_name(sort=True):
    s = 1 if sort else -1
    results = db.employees.find().sort("name", s)
    for emp in results:
        print(emp)

# Search employees by project status
def read_employee_by_project_status(status):
    results = db.employees.find({"projects.status": status})
    for emp in results:
        print(emp)

# ------------------ UPDATE OPERATIONS ------------------
# Update department of an employee
def update_department(emp_id, new_dept):
    result = db.employees.update_one(
        {"emp_id": emp_id}, 
        {"$set": {"department": new_dept}}
    )

# Increment experience years for all employees
def increment_experience(yrs=1):
    db.employees.update_many({}, {"$inc": {"experience_years": yrs}})

# Remove specific field from all employees
def remove_fields():
    result = db.employees.update_many(
        {}, 
        {"$unset": {"address.state": ""}}
    )

# Add a new skill to an employee
def add_skill(emp_id, skills):
    db.employees.update_one(
        {"emp_id": emp_id},
        {"$push": {"skills": skills}}
    )

# Remove a skill from an employee
def remove_skill(emp_id, skills):
    db.employees.update_one(
        {"emp_id": emp_id},
        {"$pull": {"skills": skills}}
    )

# Add unique skill to an employee
def add_unique_skill(emp_id, skills):
    db.employees.update_one(
        {"emp_id": emp_id},
        {"$addToSet": {"skills": skills}}  # Corrected "$addToSet" instead of "addToet"
    )

# Update project status for an employee
def update_project_status(emp_id, project_name, new_status):
    db.employees.update_one(
        {"emp_id": emp_id, "projects.name": project_name},
        {"$set": {"projects.$.status": new_status}}
    )

# Update all employees in Cloud department to Cloud-Engineer
def update_cloud_employees():
    db.employees.update_many(
        {"department": "cloud"},
        {"$set": {"department": "Cloud-Engineer"}}
    )

# ------------------ DELETE OPERATIONS ------------------
# Delete employee by ID
def delete_employee_by_id(emp_id):
    result = db.employees.delete_one({"emp_id": emp_id})
    if result.deleted_count > 0:
        print("Employee deleted successfully")
    else:
        print("Employee not found")

# Delete employees with low experience (less than 1 year)
def employee_low_experience():
    result = db.employees.delete_many({"experience_years": {"$lt": 1}})
    print(f"Deleted {result.deleted_count} employee(s)")

# Delete employees with no skills
def employee_no_skills():
    result = db.employees.delete_many({"skills": ""})

# Delete employees with no ongoing projects
def employee_no_project():
    result = db.employees.delete_many({"projects.status": {"$ne": "in-progress"}})

# Remove specific project from an employee
def remove_project_from_employee(emp_id, project_name):
    result = db.employees.update_one(
        {"emp_id": emp_id},
        {"$pull": {"projects": {"name": project_name}}}
    )

# Remove specific skill from an employee
def remove_skill_from_employee(emp_id, skill):
    result = db.employees.update_one(
        {"emp_id": emp_id},
        {"$pull": {"skills": skill}}
    )

# Remove department field from all employees
def remove_department_field():
    result = db.employees.update_many(
        {},
        {"$unset": {"department": ""}}
    )

# ------------------ Example usage ------------------
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ust_db"]
print("Database Created Successfully")

# Example student data
students = [
    {
        "name": "arun",
        "age": 24,
        "skills": ["c++", "js", "db"],
        "city": "Trichy"
    },
    {
        "name": "Sks",
        "age": 24,
        "skills": ["c++", "js", "db", "full stack", "AI"]
    },
    {
        "name": "varun",
        "age": 23,
        "skills": ["c#", "angular", "gen-ai"],
        "gender": "female"
    }
]

# Rename field 'age' to 'living' in student record with name 'Gowtham'
result = db.students.update_one(
    {"name": "Gowtham"}, 
    {"$rename": {"age": "living"}}
)
print("Modified count:", result.modified_count)

# Print all students
for student in db.students.find():
    print(student)

# Uncomment to insert students
# result = db.students.insert_many(students)
# print("Inserted IDs:", result.inserted_ids)
# print("Documents Inserted:", len(result.inserted_ids))

# Delete students older than 24 years
# result = db.students.delete_one({"age": {"$gt": 24}})
# print(f"Deleted {result.deleted_count} document(s)")

# Print each student's data
for s in db.students.find():
    print(s)


""" SAMPLE OUTPUT


Database Created Successfully
Modified count: 0
{'_id': ObjectId('6937a37a3b1c157bdff8532b'), 'name': 'Gowtham', 'skills': ['python', 'mongodb', 'Data analysis'], 'living': 22}
{'_id': ObjectId('6937a58a0c39a7441f65c335'), 'name': 'Mani', 'age': 23, 'skills': ['java', 'React', 'Web']}     
{'_id': ObjectId('6937a37a3b1c157bdff8532b'), 'name': 'Gowtham', 'skills': ['python', 'mongodb', 'Data analysis'], 'living': 22}
{'_id': ObjectId('6937a58a0c39a7441f65c335'), 'name': 'Mani', 'age': 23, 'skills': ['java', 'React', 'Web']}     
PS C:\Users\Administrator\Desktop\TRAINING> 
  
  """