#UST – Employee Skills & Project Tracking System (ESPTS)
#CRUD Operations
from pymongo import MongoClient
from typing import List

client = MongoClient('mongodb://localhost:27017/')  #mongodb connection
db = client['ust_db']                           #retrieves db from connection 'ust_db'
employees_collection = db['employees']          #retrieves collection from db 'employees'

#================= create operations ============================
#insert many employees
def insert_many_employees(employees_documents):
    result = employees_collection.insert_many(employees_documents)
    print("Inserted IDs:",result.inserted_ids)
    return result.inserted_ids

#insert one employee
def insert_one_employee(new_employee):
    result = employees_collection.insert_one(new_employee)
    print("Inserted ID:",result.inserted_id)
    return result.inserted_id


#================= read operations ==============================
#read employee by name
def find_employee_by_name(name: str):
    result = list(employees_collection.find({"name": name}))
    print("Employees:")
    return result

#read employee by department
def find_employee_by_department(department: str):
    result = list(employees_collection.find({"department": department}))
    print("Employees:")
    return result

#read employee by skills
def find_employee_by_skills(skills: List[str]):
    result = list(employees_collection.find({"skills": {"$all": skills}}))
    print("Employees:")
    return result

#read employee by city
def find_employee_by_city(city: str):
    result = list(employees_collection.find({"address.city": city}))
    print("Employees:")
    return result

#read employee by experience
def find_employee_by_experience(min_years: int):
    result = list(employees_collection.find({"experience_years": {"$gte": min_years}}))
    print("Employees:")
    return result

#read employees by missing skills
def find_employees_missing_skills():
    result=list(employees_collection.find({"skills": {"$exists": False}}))
    print("Employees:")
    return result
    
#read employees by project status
def find_employees_by_project_status(status: str):
    result = list(employees_collection.find({"projects.status": status}))
    print("Employees:")
    return result

#read employees by projection
def find_employees_projection():
    result=list(employees_collection.find({}, {"name": 1, "department": 1,"_id":0}))
    print("Employees:")
    return result

#read employees by sorting 
# age - ASC
# experience_years - DESC
# name - ASC
def sort_employees():
    result=list(employees_collection.find().sort([
        ("age", 1),
        ("experience_years", -1),
        ("name", 1)
    ]))
    print("Employees:")
    return result
    
    
#================= update operations ==============================
#update employee department
def update_employee_department(emp_id: int, new_department: str):
    employees_collection.update_one(
        {"emp_id": emp_id},
        {"$set": {"department": new_department}}
    )
    #printing updated employee details
    updated = employees_collection.find_one({"emp_id": emp_id})
    print("Updated Employee:", updated)
    return updated

#update by adding a new skill
def add_skill(emp_id: int, skill: str):
    employees_collection.update_one(
        {"emp_id": emp_id},
        {"$addToSet": {"skills": skill}}
    )
    updated = employees_collection.find_one({"emp_id": emp_id})
    print("Updated Employee:", updated)
    return updated

#update by removing a skill
def remove_skill(emp_id: int, skill: str):
    employees_collection.update_one(
        {"emp_id": emp_id},
        {"$pull": {"skills": skill}}
    )
    updated = employees_collection.find_one({"emp_id": emp_id})
    print("Updated Employee:", updated)
    return updated

#update project status
def update_project_status(emp_id: int, project_name: str, new_status: str):
    employees_collection.update_one(
        {"emp_id": emp_id, "projects.name": project_name},
        {"$set": {"projects.$.status": new_status}}
    )
    updated = employees_collection.find_one({"emp_id": emp_id})
    print("Updated Employee:", updated)
    return updated

#update by adding a new project
def add_new_project(emp_id: int, project: dict):
    employees_collection.update_one(
        {"emp_id": emp_id},
        {"$push": {"projects": project}}
    )
    updated = employees_collection.find_one({"emp_id": emp_id})
    print("Updated Employee:", updated)
    return updated

#update by incrementing 'experience years' 
def increment_experience(emp_id: int, years: int = 1):
    employees_collection.update_one(
        {"emp_id": emp_id},
        {"$inc": {"experience_years": years}}
    )
    updated = employees_collection.find_one({"emp_id": emp_id})
    print("Updated Employee:", updated)
    return updated

#update by renaming a field
def rename_field(old_field: str, new_field: str):
    employees_collection.update_many(
        {},
        {"$rename": {old_field: new_field}}
    )
    updated = list(employees_collection.find())
    print("Updated Employees:", updated)
    return updated

#update by deleting a field
def delete_field(field: str):
    employees_collection.update_many(
        {},
        {"$unset": {field: ""}}
    )
    updated = list(employees_collection.find())
    print("Updated Employees:", updated)
    return updated

#bulk update - department
def bulk_update_department(old_department: str, new_department: str):
    employees_collection.update_many(
        {"department": old_department},
        {"$set": {"department": new_department}}
    )
    updated = list(employees_collection.find({"department": new_department}))
    print("Updated Employees:", updated)
    return updated
    
#update if employee already exists, or else insert a new document
def upsert_employee(emp_id: int, profile: dict):
    employees_collection.update_one(
        {"emp_id": emp_id},
        {"$set": profile},
        upsert=True
    )
    updated = employees_collection.find_one({"emp_id": emp_id})
    print("Updated Employee:", updated)
    return updated


#================ delete operations ==============================
#delete employee by id
def delete_employee(emp_id: int):
    employees_collection.delete_one({"emp_id": emp_id})
    deleted = list(employees_collection.find())
    print("Remaining Employees:",deleted)
    return deleted

#delete low experience years
def delete_low_experience(threshold: int):
    employees_collection.delete_many({"experience_years": {"$lt": threshold}})
    deleted= list(employees_collection.find())
    print("Remaining Employees:",deleted)
    return deleted

#delete a field from employee collection
def delete_field_from_employee(emp_id: int, field: str):
    employees_collection.update_one(
        {"emp_id": emp_id},
        {"$unset": {field: ""}}
    )
    deleted= employees_collection.find_one({"emp_id": emp_id})
    print("Updated Employee:",deleted)
    return deleted

#delete or remove a skill
def remove_skill(emp_id: int, skill: str):
    employees_collection.update_one(
        {"emp_id": emp_id},
        {"$pull": {"skills": skill}}
    )
    deleted = employees_collection.find_one({"emp_id": emp_id})
    print("Updated Employee:",deleted)
    return deleted

#remove a project from employee collection
def remove_project(emp_id: int, project_name: str):
    employees_collection.update_one(
        {"emp_id": emp_id},
        {"$pull": {"projects": {"name": project_name}}}
    )
    deleted = employees_collection.find_one({"emp_id": emp_id})
    print("Updated Employee:",deleted)
    return deleted
             
             
#================ documents =============================
employees_documents=[
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

#new document
new_employee={
    "emp_id": 111,
    "name": "Janet Sherin",
    "age": 24,
    "department": "Cybersecurity",
    "skills": ["networking", "firewall", "linux"],
    "projects": [
      { "name": "SecuritySuite", "status": "deployed" }
    ],
    "experience_years": 4
  }


#============ main function =========================
#calling all the functions
insert_many_employees(employees_documents)
insert_one_employee(new_employee)

find_employee_by_name("Lavanya N")
find_employee_by_department("Cybersecurity")
find_employee_by_city("Trivandrum")
find_employee_by_skills(["networking"])
find_employee_by_experience(3)
print(find_employees_missing_skills())
print(find_employees_by_project_status("in-progress"))
print(find_employees_projection())
print(sort_employees())

update_employee_department(101, "Data Science")
add_skill(102, "kubernetes")
remove_skill(105, "deep-learning")
update_project_status(104, "SecureBank", "completed")
add_new_project(103, {"name": "TestAutomation", "status": "planned"})
increment_experience(106, 2)
rename_field("city", "location")
delete_field("address")
bulk_update_department("Testing", "QA")
upsert_employee(112, {
    "emp_id": 112,
    "name": "New Employee",
    "age": 27,
    "department": "AI",
    "experience_years": 1
})

delete_employee(101)           
delete_low_experience(2)                      
delete_field_from_employee(102, "address")    
remove_skill(105, "deep-learning")            
remove_project(104, "SecureBank")

