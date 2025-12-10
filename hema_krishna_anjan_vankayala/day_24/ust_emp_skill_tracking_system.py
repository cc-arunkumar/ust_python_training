#UST wants to build an internal Employee Skills & Project Tracking System(ESPTS) 
# to maintain accurate information about employees, skills, departments,project allocations, and experience levels.
# This system will be used by:
# HR team
# Delivery Managers
# Resource Allocation team
# Internal L&D team
# The backend database for this system must be built using MongoDB, utilizing its
# flexible document model

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client['ust_db']

collection = db['employees']

collection.create_index('emp_id',unique=True)

data = [
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


def insert_one(emp):
    try:
        data = db.employees.insert_one(emp)
    
        return 'Insertd One Employee'
    except Exception as e:
        return f'{e}'

def insert_many(emps):
    try:
        data = db.employees.insert_many(emps)
    
        return 'Inserted Many Employees'
    except Exception as e:
        return f'{e}'

def find_one(department=None,skillset=None,city=None,experience_min=None,experience_max=None,nested_field=None,
    nested_value=None,projection=None):
    try:
        query ={}
        if department:
            query["department"] = department
        if skillset:
            query["skills"] = {"$in": skillset}
        if city:
            query['city'] = city 
        if experience_min:
            query["experience_years"] = {"$gte": experience_min}
        if experience_max:
            query['experience_years'] = {"$lte": experience_max}
        if nested_field and nested_value:
            query[f"projects.{nested_field}"] = nested_value
        if projection:
            projection_dict = {}
            for field in projection:
                projection_dict[field] = 1
            projection = projection_dict
                

        data = collection.find_one(query,projection)
        return data
    except Exception as e:
        return f'Error:{e}'


def find_all(department=None,skillset=None,city=None,experience_min=None,experience_max=None,nested_field=None,
    nested_value=None,
    projection=None,sort_fields=None):
    try:
        query ={}
        if department:
            query["department"] = department
        if skillset:
            query["skills"] = {"$in": skillset}
        if city:
            query['city'] = city 
        if experience_min:
            query["experience_years"] = {"$gte": experience_min}
        if experience_max:
            query['experience_years'] = {"$lte": experience_max}
        if nested_field and nested_value:
            query[f"projects.{nested_field}"] = nested_value
        if projection:
            projection_dict = {}
            for field in projection:
                projection_dict[field] = 1
            projection = projection_dict
                

        data = collection.find(query,projection)
        
        if sort_fields:
            data = data.sort(sort_fields)
            
        return list(data)
    except Exception as e:
        return f'Error:{e}'

# 4.3 Update Operations
# Modify employee department
# Add or remove skills
# Update nested project status
# Add new project entries
# Increment experience counter
# Rename and delete fields
# Bulk update based on conditions
# Upsert employee profile if not found
# def update_employee(emp_id=None,department=None,add_skill=None,remove_skill=None,
#                     project_name=None,project_status=None,increase_experience=None,
#                     rename_field=None,delete_field=None,
#                     bulk_update_conditions=None,bulk_update_values=None):
#     try:
#         #if emp_id is not found then it should create a new employee profile 
#         query ={}
#         if emp_id :
#             query["emp_id"] = emp_id
#         if department:
#             query["department"] = department
#         if add_skill:
#             query["skills"] = {"$addToSet": add_skill}
#         if remove_skill:
#             query["skills"] = {"$pull": remove_skill}
#         if project_name and project_status:
#             query[f'projects.{project_name}'] = project_status
#         if increase_experience:
#             query["experience_years"] = {"$inc": increase_experience}
#         if rename_field:
#             field, newfield = rename_field
#             query[field] = {"$rename": newfield}
#         if delete_field:
#             query[delete_field] = {"$unset":""}
#         if bulk_update_conditions and bulk_update_values:
#             data = collection.update_many(bulk_update_conditions,{"$set":bulk_update_values})
#             return f'Bulk Updated {data.modified_count} Employees'
#         data = collection.update_one({"emp_id":emp_id},{"$set":query})
#         return 'Employee Updated Successfully'
#     except Exception as e:
#         return f'Error:{e}'


def update_department(name, new_department):
    return collection.update_one(
        {"name": name},
        {"$set": {"department": new_department}}
    )

def add_skill(name, skill):
    return collection.update_one(
        {"name": name},
        {"$push": {"skills": skill}}
    )

def remove_skill(name, skill):
    return collection.update_one(
        {"name": name},
        {"$pull": {"skills": skill}}
    )

def update_project_status(name, status):
    return collection.update_one(
        {"name": name},
        {"$set": {"project.status": status}}
    )


def add_project(name, project_entry):
    return collection.update_one(
        {"name": name},
        {"$push": {"projects": project_entry}}
    )


def increment_experience(name, years=1):
    return collection.update_one(
        {"name": name},
        {"$inc": {"experience_years": years}}
    )

def rename_field(name, old_field, new_field):
    return collection.update_one(
        {"name": name},
        {"$rename": {old_field: new_field}}
    )

def delete_field(name, field):
    return collection.update_one(
        {"name": name},
        {"$unset": {field: ""}}
    )

def bulk_update_department(old_dept, new_dept):
    return collection.update_many(
        {"department": old_dept},
        {"$set": {"department": new_dept}}
    )

def upsert_employee(name, department, experience_years):
    return collection.update_one(
        {"name": name},
        {"$set": {"department": department, "experience_years": experience_years}},
        upsert=True
    )
    

def delete_employee(name):
    return collection.delete_one({"name": name})

def delete_low_experience(threshold):
    return collection.delete_many({"experience_years": {"$lt": threshold}})

def delete_field(name, field):
    return collection.update_one(
        {"name": name},
        {"$unset": {field: ""}}
    )

def remove_skill(name, skill):
    return collection.update_one(
        {"name": name},
        {"$pull": {"skills": skill}}
    )

def remove_project(name, project_name):
    return collection.update_one(
        {"name": name},
        {"$pull": {"projects": {"name": project_name}}}
    )



# insert_many(data)
# a=find_one(department="AI",skillset=["python"],nested_field="status",nested_value="completed",projection=["name","projects"])
# print(a)  

