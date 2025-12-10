from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017/')
db = client['mongo_db']  
employees_collection = db['employees'] 

employees_data = [
    {
        "emp_id": 101,
        "name": "Anu Joseph",
        "age": 23,
        "department": "AI",
        "skills": ["python", "mongodb"],
        "address": { "city": "Trivandrum", "state": "Kerala" },
        "projects": [
            { "name": "VisionAI", "status": "completed" },
            { "name": "DocScan", "status": "in-progress" }
        ],
        "experience_years": 1
    },
    {
        "emp_id": 102,
        "name": "Rahul Menon",
        "age": 26,
        "department": "Cloud",
        "skills": ["aws", "docker"],
        "address": { "city": "Kochi", "state": "Kerala" },
        "projects": [
            { "name": "USTCloudPortal", "status": "planned" }
        ],
        "experience_years": 3
    },
    {
        "emp_id": 103,
        "name": "Sahana R",
        "age": 22,
        "department": "Testing",
        "skills": ["selenium"],
        "address": { "city": "Chennai", "state": "TN" },
        "projects": [],
        "experience_years": 1
    },
    {
        "emp_id": 104,
        "name": "Vishnu Prakash",
        "age": 29,
        "department": "Cybersecurity",
        "skills": ["networking", "siem"],
        "address": { "city": "Trivandrum", "state": "Kerala" },
        "projects": [
            { "name": "SecureBank", "status": "in-progress" }
        ],
        "experience_years": 5
    },
    {
        "emp_id": 105,
        "name": "Maya Kumar",
        "age": 25,
        "department": "AI",
        "skills": ["python", "deep-learning"],
        "address": { "city": "Bangalore", "state": "KA" },
        "projects": [
            { "name": "VisionAI", "status": "completed" }
        ],
        "experience_years": 2
    },
    {
        "emp_id": 106,
        "name": "Arjun S",
        "age": 28,
        "department": "Cloud",
        "skills": ["azure"],
        "address": { "city": "Kochi", "state": "Kerala" },
        "projects": [
            { "name": "DevOpsBoost", "status": "in-progress" }
        ],
        "experience_years": 4
    },
    {
        "emp_id": 107,
        "name": "Neha Mohan",
        "age": 24,
        "department": "Data",
        "skills": ["sql", "tableau"],
        "address": { "city": "Chennai", "state": "TN" },
        "projects": [
            { "name": "USTAnalyticsHub", "status": "planned" }
        ],
        "experience_years": 2
    },
    {
        "emp_id": 108,
        "name": "Suresh B",
        "age": 27,
        "department": "Data",
        "address": { "city": "Kochi", "state": "Kerala" },
        "projects": [],
        "experience_years": 3
    },
    {
        "emp_id": 109,
        "name": "Lavanya N",
        "age": 21,
        "department": "Testing",
        "skills": [],
        "address": { "city": "Trivandrum", "state": "Kerala" },
        "projects": [
            { "name": "QualityX", "status": "in-progress" }
        ],
        "experience_years": 0
    },
    {
        "emp_id": 110,
        "name": "Rakesh Pillai",
        "age": 30,
        "department": "Cybersecurity",
        "skills": ["networking", "firewall", "linux"],
        "projects": [
            { "name": "SecuritySuite", "status": "deployed" }
        ],
        "experience_years": 7
    }
]

def insert_employee(employee_data):
    result=employees_collection.insert_one(employee_data)
    print(result)
    
def bulk_insert_employees(employee_data):
    result=employees_collection.insert_many(employee_data)
    print(result)
    
def find_employee_by_department(department):
    result=employees_collection.find({"department":department})
    for emp in result:
        print(emp)
        
def find_employee_by_skillset(skills):
    result=employees_collection.find({"skills":skills})
    for emp in result:
        print(emp)
        
def find_by_city(city):
    result=employees_collection.find({"address.city":city})
    for emp in result:
        print(emp)
        
def find_missing_field(field):
    result=employees_collection.find({field:{"$exists":False}})
    for emp in result:
        print(emp)
        
def filter_experience(min_exp,max_exp):
    result=employees_collection.find({"experience_years":{"$gte":min_exp,"$lte":max_exp}})
    for emp in result:
        print(emp)
        
def find_project_status(status):
    result=employees_collection.find({"projects.status":status})
    for emp in result:
        print(emp)
        
def employee_with_projection():
    result=employees_collection.find({},{"name":1,"department":1})
    for emp in result:
        print(emp)
        
def sort_employee(sort="age"):
    if sort=="age":
        result=employees_collection.find().sort("age",1)
    elif sort=="experience_years":
        result=employees_collection.find().sort("experience_years",1)
    elif sort=="name":
        result=employees_collection.find().sort("name",1)
    for emp in result:
        print(emp)
        
def update_employee_department(emp_id, new_department):
    result = employees_collection.update_one(
        {"emp_id": emp_id},
        {"$set": {"department": new_department}}
    )
    if result.modified_count > 0:
        print("employee updated")
    else:
        print("No employee found")
        
def update_skill(emp_id,new_skills):
    result = employees_collection.update_one(
        {"emp_id": emp_id},
        {"$set": {"department": new_skills}}
    )
    if result.modified_count > 0:
        print("employee updated")
    else:
        print("No employee found")
        
def update_project_status(emp_id, project_name, new_status):
    result = employees_collection.update_one(
        {"emp_id": emp_id, "projects.name": project_name},
        {"$set": {"projects.$.status": new_status}}
    )
    if result.modified_count > 0:
        print("Project status updated")
    else:
        print("Project not found")

def add_new_project(emp_id, new_project):
    result = employees_collection.update_one(
        {"emp_id": emp_id},
        {"$push": {"projects": new_project}}
    )
    if result.modified_count > 0:
        print("New project added")
    else:
        print("No employee found")

def increment_experience(emp_id, years=1):
    result = employees_collection.update_one(
        {"emp_id": emp_id},
        {"$inc": {"experience_years": years}}
    )
    if result.modified_count > 0:
        print("Employee experience incremented")
    else:
        print("No employee found")

def rename_field(emp_id, old_field_name, new_field_name):
    result = employees_collection.update_one(
        {"emp_id": emp_id},
        {"$set": {new_field_name: "$" + old_field_name}, "$unset": {old_field_name: ""}}
    )
    if result.modified_count > 0:
        print("Field renamed")
    else:
        print("No employee found")

def delete_field(emp_id, field_name):
    result = employees_collection.update_one(
        {"emp_id": emp_id},
        {"$unset": {field_name: ""}}
    )
    if result.modified_count > 0:
        print("Field deleted")
    else:
        print("No field found")

def bulk_update_department(old_department, new_department):
    result = employees_collection.update_many(
        {"department": old_department},
        {"$set": {"department": new_department}}
    )
    print("Updated employees")

def upsert_employee_profile(emp_id, employee_data):
    result = employees_collection.update_one(
        {"emp_id": emp_id},
        {"$set": employee_data},
        upsert=True  
    )
    if result.upserted_id:
        print("Employee profile created")
    else:
        print("Employee profile updated")

def delete_employee_profile(emp_id):
    result = employees_collection.delete_one({"emp_id": emp_id})
    if result.deleted_count > 0:
        print("Employee deleted.")
    else:
        print("No employee found")

def delete_employees_by_condition(min_experience):
    result = employees_collection.delete_many({"experience_years": {"$lt": min_experience}})
    print("Deleted employees with less than min years of experience.")

def delete_employee_field(emp_id, field_name):
    result = employees_collection.update_one(
        {"emp_id": emp_id},
        {"$unset": {field_name: ""}}
    )
    if result.modified_count > 0:
        print("Field deleted")
    else:
        print("No field found")

def remove_array_element(emp_id, field_name, value_to_remove):
    result = employees_collection.update_one(
        {"emp_id": emp_id},
        {"$pull": {field_name: value_to_remove}}
    )
    if result.modified_count > 0:
        print("Removed")
    else:
        print("No such value found")
        
bulk_insert_employees(employees_data)
find_employee_by_department("AI")
find_employee_by_skillset("python")
find_by_city("Kochi")
find_missing_field("skills")
filter_experience(1, 5)
find_project_status("in-progress")
employee_with_projection()
sort_employee("age")
sort_employee("experience_years")
sort_employee("name")
update_employee_department(101, "Cloud")
update_skill(101, "deep-learning")
update_project_status(101, "VisionAI", "completed")
new_project = {"name": "AI-Assistant", "status": "planned"}
add_new_project(101, new_project)
increment_experience(101, 2)
rename_field(101, "skills", "competencies")
delete_field(101, "address")
bulk_update_department("AI", "AI Research")
employee_data_to_upsert = {
    "emp_id": 111,
    "name": "New Employee",
    "age": 24,
    "department": "Data",
    "skills": ["python", "sql"],
    "projects": [{"name": "DataScience", "status": "planned"}],
    "experience_years": 1
}
upsert_employee_profile(111, employee_data_to_upsert)
delete_employee_profile(101)
delete_employees_by_condition(2)
delete_employee_field(101, "address")
remove_array_element(101, "skills", "python")
remove_array_element(101, "projects", {"name": "VisionAI"})
